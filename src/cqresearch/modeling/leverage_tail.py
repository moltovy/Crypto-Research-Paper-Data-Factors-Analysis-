"""Lagged leverage, tail-risk, systemic-risk, and connectedness estimators."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import build_design_matrices, dmatrix
from statsmodels.stats.proportion import proportion_confint

from cqresearch.modeling.rolling_connectedness import rolling_fevd_connectedness

DEFAULT_SEED = 20260713


def leverage_tail_model(daily: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fit a descriptive next-session tail logit using lagged state variables."""

    frame = pd.DataFrame(
        {
            "next_return": pd.to_numeric(daily["btc_ret"], errors="coerce").shift(-1),
            "leverage": pd.to_numeric(daily["btc_leverage_ratio_percentile_lag1"], errors="coerce"),
            "volatility": pd.to_numeric(daily["btc_realized_vol_30d"], errors="coerce").shift(1),
        }
    ).dropna()
    threshold = float(frame["next_return"].quantile(0.05))
    frame["tail"] = frame["next_return"].le(threshold).astype(int)
    design = dmatrix(
        "bs(leverage, df=4, degree=3, include_intercept=False) + "
        "bs(volatility, df=4, degree=3, include_intercept=False)",
        frame,
        return_type="dataframe",
    )
    model = sm.GLM(frame["tail"], design, family=sm.families.Binomial()).fit(
        cov_type="HAC", cov_kwds={"maxlags": 10}
    )
    leverage_grid = np.linspace(
        frame["leverage"].quantile(0.05), frame["leverage"].quantile(0.95), 19
    )
    prediction_frame = pd.DataFrame(
        {"leverage": leverage_grid, "volatility": frame["volatility"].median()}
    )
    prediction_design = build_design_matrices(
        [design.design_info], prediction_frame, return_type="dataframe"
    )[0]
    prediction = model.get_prediction(prediction_design).summary_frame()
    fitted = np.asarray(model.predict(design), dtype=float)
    clipped = np.clip(fitted, 1e-8, 1 - 1e-8)
    calibration_design = sm.add_constant(np.log(clipped / (1 - clipped)))
    calibration = sm.GLM(frame["tail"], calibration_design, family=sm.families.Binomial()).fit()
    influence = model.get_influence(observed=True)
    curve = prediction_frame.assign(
        predicted_tail_probability=prediction["mean"].to_numpy(),
        ci_low=prediction["mean_ci_lower"].to_numpy(),
        ci_high=prediction["mean_ci_upper"].to_numpy(),
        observed_leverage_min=frame["leverage"].min(),
        observed_leverage_max=frame["leverage"].max(),
        fixed_volatility=frame["volatility"].median(),
        tail_threshold=threshold,
        n=len(frame),
        sample_start=frame.index.min().date().isoformat(),
        sample_end=frame.index.max().date().isoformat(),
        method="binomial GLM with cubic splines and HAC covariance; descriptive lagged-state association",
    )
    diagnostics = pd.DataFrame(
        [
            {
                "model": "btc_next_session_tail_logit",
                "n": len(frame),
                "tail_events": int(frame["tail"].sum()),
                "tail_rate": float(frame["tail"].mean()),
                "deviance": float(model.deviance),
                "pearson_chi2": float(model.pearson_chi2),
                "converged": bool(model.converged),
                "design_condition_number": float(np.linalg.cond(design)),
                "brier_score": float(np.mean((frame["tail"].to_numpy() - fitted) ** 2)),
                "calibration_intercept": float(calibration.params.iloc[0]),
                "calibration_slope": float(calibration.params.iloc[1]),
                "maximum_cooks_distance": float(np.nanmax(influence.cooks_distance[0])),
                "leverage_support_q05": float(frame["leverage"].quantile(0.05)),
                "leverage_support_q95": float(frame["leverage"].quantile(0.95)),
                "sample_start": frame.index.min().date().isoformat(),
                "sample_end": frame.index.max().date().isoformat(),
            }
        ]
    )
    return curve, diagnostics


def quantile_and_expected_shortfall(
    daily: pd.DataFrame, reps: int = 2000, block_length: int = 10
) -> tuple[pd.DataFrame, pd.DataFrame]:
    frame = pd.DataFrame(
        {
            "next_return": pd.to_numeric(daily["btc_ret"], errors="coerce").shift(-1),
            "leverage": pd.to_numeric(daily["btc_leverage_ratio_percentile_lag1"], errors="coerce"),
            "volatility": pd.to_numeric(daily["btc_realized_vol_30d"], errors="coerce").shift(1),
        }
    ).dropna()
    quantile_rows = []
    design = sm.add_constant(frame[["leverage", "volatility"]])
    for quantile in (0.05, 0.10):
        model = sm.QuantReg(frame["next_return"], design).fit(q=quantile, max_iter=5000)
        for feature in ("leverage", "volatility"):
            quantile_rows.append(
                {
                    "quantile": quantile,
                    "feature": feature,
                    "coefficient": float(model.params[feature]),
                    "standard_error": float(model.bse[feature]),
                    "ci_low": float(model.conf_int().loc[feature, 0]),
                    "ci_high": float(model.conf_int().loc[feature, 1]),
                    "n": len(frame),
                    "sample_start": frame.index.min().date().isoformat(),
                    "sample_end": frame.index.max().date().isoformat(),
                    "method": "quantile regression on lagged leverage and volatility states",
                }
            )
    frame["leverage_state"] = pd.qcut(frame["leverage"], 5, labels=False, duplicates="drop")
    rng = np.random.default_rng(DEFAULT_SEED)
    es_rows = []
    for state, group in frame.groupby("leverage_state"):
        threshold = group["next_return"].quantile(0.05)
        tail_values = group.loc[group["next_return"].le(threshold), "next_return"].to_numpy()
        bootstrap = _moving_block_es(frame, int(state), reps, block_length, rng)
        es_rows.append(
            {
                "leverage_state": int(state) + 1,
                "state_min": float(group["leverage"].min()),
                "state_max": float(group["leverage"].max()),
                "expected_shortfall_5pct": float(tail_values.mean()),
                "ci_low": float(np.quantile(bootstrap, 0.025)),
                "ci_high": float(np.quantile(bootstrap, 0.975)),
                "tail_observations": len(tail_values),
                "n": len(group),
                "bootstrap_reps": reps,
                "block_length": block_length,
                "sample_start": group.index.min().date().isoformat(),
                "sample_end": group.index.max().date().isoformat(),
            }
        )
    return pd.DataFrame(quantile_rows), pd.DataFrame(es_rows)


def leverage_horizon_sensitivity(daily: pd.DataFrame) -> pd.DataFrame:
    """Summarize non-overlapping five-session tail outcomes by lagged leverage state."""

    returns = pd.to_numeric(daily["btc_ret"], errors="coerce")
    forward_five = sum(returns.shift(-offset) for offset in range(1, 6))
    frame = pd.DataFrame(
        {
            "forward_five_session_return": forward_five,
            "leverage": pd.to_numeric(daily["btc_leverage_ratio_percentile_lag1"], errors="coerce"),
        }
    ).dropna()
    frame = frame.iloc[::5].copy()
    threshold = float(frame["forward_five_session_return"].quantile(0.05))
    frame["tail"] = frame["forward_five_session_return"].le(threshold)
    frame["leverage_state"] = pd.qcut(frame["leverage"], 5, labels=False, duplicates="drop")
    rows = []
    for state, group in frame.groupby("leverage_state"):
        events = int(group["tail"].sum())
        low, high = proportion_confint(events, len(group), alpha=0.05, method="wilson")
        rows.append(
            {
                "leverage_state": int(state) + 1,
                "state_min": float(group["leverage"].min()),
                "state_max": float(group["leverage"].max()),
                "tail_probability": float(group["tail"].mean()),
                "ci_low": float(low),
                "ci_high": float(high),
                "tail_threshold": threshold,
                "tail_events": events,
                "n": len(group),
                "sample_start": group.index.min().date().isoformat(),
                "sample_end": group.index.max().date().isoformat(),
                "method": "non-overlapping five-session forward return; leverage-state Wilson interval",
            }
        )
    return pd.DataFrame(rows)


def systemic_tail_associations(
    returns: pd.DataFrame, reps: int = 2000, block_length: int = 10
) -> pd.DataFrame:
    clean = returns.dropna()
    btc_threshold = clean["BTC"].quantile(0.05)
    btc_tail = clean["BTC"].le(btc_threshold)
    rng = np.random.default_rng(DEFAULT_SEED + 77)
    rows = []
    for asset in [column for column in clean if column != "BTC"]:
        values = clean.loc[btc_tail, asset]
        covar = float(values.quantile(0.05))
        unconditional_var = float(clean[asset].quantile(0.05))
        mes = float(values.mean())
        baseline = float(clean[asset].mean())
        paired = pd.DataFrame({"asset": clean[asset], "tail": btc_tail.astype(float)})
        bootstrap = _block_bootstrap_tail_means(paired, reps, block_length, rng)
        rows.append(
            {
                "asset": asset,
                "btc_tail_threshold": float(btc_threshold),
                "conditional_var_5pct": covar,
                "unconditional_var_5pct": unconditional_var,
                "delta_covar_5pct": covar - unconditional_var,
                "marginal_expected_shortfall": mes,
                "delta_mes_vs_unconditional_mean": mes - baseline,
                "mes_ci_low": float(np.nanquantile(bootstrap, 0.025)),
                "mes_ci_high": float(np.nanquantile(bootstrap, 0.975)),
                "btc_tail_observations": int(btc_tail.sum()),
                "n": len(clean),
                "sample_start": clean.index.min().date().isoformat(),
                "sample_end": clean.index.max().date().isoformat(),
                "method": "asset return distribution conditional on BTC lower-tail dates",
            }
        )
    return pd.DataFrame(rows)


def connectedness_grid(returns: pd.DataFrame) -> pd.DataFrame:
    """Run primary and sensitivity rolling generalized-FEVD specifications."""

    columns = [column for column in ["BTC", "ETH", "XRP", "DOT", "ADA"] if column in returns]
    absolute = returns[columns].abs().dropna()
    specifications = [
        (252, 10, "primary"),
        (180, 10, "window_180"),
        (365, 10, "window_365"),
        (252, 5, "horizon_5"),
        (252, 20, "horizon_20"),
    ]
    outputs = []
    for window, horizon, specification in specifications:
        result = rolling_fevd_connectedness(
            absolute, window=window, step=21, horizon=horizon, maxlags=5
        )
        result["specification"] = specification
        result["variables"] = "|".join(columns)
        outputs.append(result)
    reversed_columns = list(reversed(columns))
    reversed_result = rolling_fevd_connectedness(
        absolute[reversed_columns], window=252, step=21, horizon=10, maxlags=5
    )
    reversed_result["specification"] = "order_reversed"
    reversed_result["variables"] = "|".join(reversed_columns)
    outputs.append(reversed_result)
    return pd.concat(outputs, ignore_index=True)


def _moving_block_es(
    frame: pd.DataFrame,
    state: int,
    reps: int,
    block_length: int,
    rng: np.random.Generator,
) -> np.ndarray:
    values = frame[["next_return", "leverage_state"]].to_numpy()
    n = len(values)
    blocks = math.ceil(n / block_length)
    offsets = np.arange(block_length)
    output = np.full(reps, np.nan)
    for index in range(reps):
        starts = rng.integers(0, n - block_length + 1, size=blocks)
        sampled = values[(starts[:, None] + offsets).ravel()[:n]]
        state_returns = sampled[sampled[:, 1] == state, 0]
        if len(state_returns) < 20:
            continue
        threshold = np.quantile(state_returns, 0.05)
        output[index] = state_returns[state_returns <= threshold].mean()
    return output


def _block_bootstrap_tail_means(
    frame: pd.DataFrame,
    reps: int,
    block_length: int,
    rng: np.random.Generator,
) -> np.ndarray:
    n = len(frame)
    blocks = math.ceil(n / block_length)
    offsets = np.arange(block_length)
    output = np.empty(reps)
    values = frame.to_numpy()
    for index in range(reps):
        starts = rng.integers(0, n - block_length + 1, size=blocks)
        sampled = values[(starts[:, None] + offsets).ravel()[:n]]
        tail_values = sampled[sampled[:, 1].astype(bool), 0]
        output[index] = tail_values.mean() if len(tail_values) else np.nan
    return output


__all__ = [
    "connectedness_grid",
    "leverage_tail_model",
    "leverage_horizon_sensitivity",
    "quantile_and_expected_shortfall",
    "systemic_tail_associations",
]
