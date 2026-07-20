"""ETF market-plumbing estimators with trading-date and simultaneity controls."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.stattools import durbin_watson, jarque_bera

from cqresearch.data.calendars import business_day_mask
from cqresearch.data.loaders import load_farside

DEFAULT_SEED = 20260713


def distributed_lag_models(
    frame: pd.DataFrame,
    lags: int = 5,
    reps: int = 2000,
    block_length: int = 10,
    seed: int = DEFAULT_SEED,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Estimate simultaneous ETF lag coefficients and max-t confidence bands."""

    coefficient_rows = []
    cumulative_rows = []
    timing_rows = []
    for asset_index, asset in enumerate(("BTC", "ETH")):
        lower = asset.lower()
        flow = pd.to_numeric(frame[f"{lower}_etf_net_flow_usd"], errors="coerce")
        lag_mcap = pd.to_numeric(frame[f"{lower}_mcap_lag1"], errors="coerce")
        intensity_bps = flow / lag_mcap * 10_000
        returns = pd.to_numeric(frame[f"{lower}_ret"], errors="coerce")
        responses = {
            "return": returns,
            "realized_volatility_20": returns.rolling(20, min_periods=15).std() * math.sqrt(252),
        }
        for response_index, (response_name, response) in enumerate(responses.items()):
            data = pd.DataFrame({"response": response})
            for lag in range(lags + 1):
                data[f"flow_lag_{lag}"] = intensity_bps.shift(lag)
            data = data.dropna()
            x_columns = [f"flow_lag_{lag}" for lag in range(lags + 1)]
            model = sm.OLS(data["response"], sm.add_constant(data[x_columns])).fit(
                cov_type="HAC", cov_kwds={"maxlags": lags}
            )
            exog = sm.add_constant(data[x_columns])
            condition_number = float(np.linalg.cond(exog))
            dw_statistic = float(durbin_watson(model.resid))
            _, jb_pvalue, _, _ = jarque_bera(model.resid)
            _, bp_pvalue, _, _ = het_breuschpagan(model.resid, exog)
            estimates = model.params[x_columns].to_numpy()
            bootstrap = _moving_block_coefficients(
                data,
                x_columns,
                reps=reps,
                block_length=block_length,
                seed=seed + asset_index * 10_000 + response_index * 1_000,
            )
            bootstrap_se = bootstrap.std(axis=0, ddof=1)
            safe_se = np.where(bootstrap_se > 0, bootstrap_se, np.nan)
            max_t = np.nanmax(np.abs((bootstrap - estimates) / safe_se), axis=1)
            critical = float(np.nanquantile(max_t, 0.95))
            for lag, column in enumerate(x_columns):
                coefficient_rows.append(
                    {
                        "asset": asset,
                        "response": response_name,
                        "lag_sessions": lag,
                        "coefficient_per_flow_bps": float(model.params[column]),
                        "se_hac": float(model.bse[column]),
                        "pvalue_hac": float(model.pvalues[column]),
                        "pointwise_ci_low": float(model.conf_int().loc[column, 0]),
                        "pointwise_ci_high": float(model.conf_int().loc[column, 1]),
                        "simultaneous_ci_low": float(estimates[lag] - critical * bootstrap_se[lag]),
                        "simultaneous_ci_high": float(
                            estimates[lag] + critical * bootstrap_se[lag]
                        ),
                        "bootstrap_reps": reps,
                        "block_length": block_length,
                        "design_condition_number": condition_number,
                        "durbin_watson": dw_statistic,
                        "jarque_bera_pvalue": float(jb_pvalue),
                        "breusch_pagan_pvalue": float(bp_pvalue),
                        "n": len(data),
                        "sample_start": data.index.min().date().isoformat(),
                        "sample_end": data.index.max().date().isoformat(),
                        "method": "simultaneous distributed-lag OLS with HAC and moving-block max-t bands",
                    }
                )
            cumulative = bootstrap.sum(axis=1)
            cumulative_rows.append(
                {
                    "asset": asset,
                    "response": response_name,
                    "lags_included": f"0-{lags}",
                    "cumulative_coefficient": float(estimates.sum()),
                    "ci_low": float(np.quantile(cumulative, 0.025)),
                    "ci_high": float(np.quantile(cumulative, 0.975)),
                    "bootstrap_reps": reps,
                    "block_length": block_length,
                    "n": len(data),
                    "sample_start": data.index.min().date().isoformat(),
                    "sample_end": data.index.max().date().isoformat(),
                }
            )
        for shift, convention in [(0, "reported_date"), (1, "one_session_later")]:
            aligned = pd.concat(
                [returns.rename("return"), intensity_bps.shift(shift).rename("flow_bps")], axis=1
            ).dropna()
            timing_rows.append(
                {
                    "asset": asset,
                    "timing_convention": convention,
                    "flow_shift_sessions": shift,
                    "return_correlation": float(aligned["return"].corr(aligned["flow_bps"])),
                    "absolute_return_correlation": float(
                        aligned["return"].abs().corr(aligned["flow_bps"])
                    ),
                    "n": len(aligned),
                    "sample_start": aligned.index.min().date().isoformat(),
                    "sample_end": aligned.index.max().date().isoformat(),
                }
            )
    return (
        pd.DataFrame(coefficient_rows),
        pd.DataFrame(cumulative_rows),
        pd.DataFrame(timing_rows),
    )


def nonlinear_flow_sensitivity(frame: pd.DataFrame) -> pd.DataFrame:
    """Estimate predeclared inflow/outflow and volatility-state interactions."""

    rows: list[dict[str, object]] = []
    for asset in ("BTC", "ETH"):
        lower = asset.lower()
        returns = pd.to_numeric(frame[f"{lower}_ret"], errors="coerce")
        flow = pd.to_numeric(frame[f"{lower}_etf_net_flow_usd"], errors="coerce")
        lag_mcap = pd.to_numeric(frame[f"{lower}_mcap_lag1"], errors="coerce")
        intensity = flow / lag_mcap * 10_000
        lagged_volatility = returns.rolling(20, min_periods=15).std().shift(1)
        high_volatility = lagged_volatility.gt(lagged_volatility.median()).astype(float)
        data = pd.DataFrame(
            {
                "response": returns,
                "inflow_bps": intensity.clip(lower=0),
                "outflow_bps": intensity.clip(upper=0),
                "high_volatility": high_volatility,
                "flow_x_high_volatility": intensity * high_volatility,
            }
        ).dropna()
        terms = ["inflow_bps", "outflow_bps", "flow_x_high_volatility"]
        design = sm.add_constant(data[[*terms, "high_volatility"]])
        model = sm.OLS(data["response"], design).fit(cov_type="HAC", cov_kwds={"maxlags": 5})
        for term in terms:
            rows.append(
                {
                    "asset": asset,
                    "term": term,
                    "coefficient": float(model.params[term]),
                    "se_hac": float(model.bse[term]),
                    "ci_low": float(model.conf_int().loc[term, 0]),
                    "ci_high": float(model.conf_int().loc[term, 1]),
                    "pvalue": float(model.pvalues[term]),
                    "design_condition_number": float(np.linalg.cond(design)),
                    "n": int(model.nobs),
                    "sample_start": data.index.min().date().isoformat(),
                    "sample_end": data.index.max().date().isoformat(),
                    "method": "HAC OLS with split flow direction and a lagged-volatility-state interaction",
                }
            )
    result = pd.DataFrame(rows)
    result["qvalue_bh"] = multipletests(result["pvalue"], method="fdr_bh")[1]
    return result


def flow_concentration() -> pd.DataFrame:
    """Summarize issuer concentration on actual XNYS report dates."""

    rows = []
    for asset in ("btc", "eth"):
        frame = load_farside(asset).df
        frame = frame.loc[business_day_mask(frame.index)]
        issuer_columns = [column for column in frame if not column.endswith("_total")]
        absolute = frame[issuer_columns].abs()
        denominator = absolute.sum(axis=1, min_count=1)
        shares = absolute.div(denominator.replace(0, np.nan), axis=0)
        hhi = shares.pow(2).sum(axis=1, min_count=1)
        total = frame[f"{asset}_etf_total"]
        rows.append(
            {
                "asset": asset.upper(),
                "issuer_count": len(issuer_columns),
                "report_dates": int(total.notna().sum()),
                "flow_hhi_median": float(hhi.median()),
                "flow_hhi_q10": float(hhi.quantile(0.10)),
                "flow_hhi_q90": float(hhi.quantile(0.90)),
                "total_flow_autocorrelation_1": float(total.autocorr(lag=1)),
                "sample_start": frame.index.min().date().isoformat(),
                "sample_end": frame.index.max().date().isoformat(),
                "method": "absolute issuer-flow shares on actual XNYS report dates",
            }
        )
    return pd.DataFrame(rows)


def cftc_positioning_associations(
    positioning: pd.DataFrame, daily: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Relate standard-contract CFTC position changes to same-week crypto returns."""

    contracts = positioning.loc[~positioning["is_micro"].astype(bool)].copy()
    contracts["report_date"] = pd.to_datetime(contracts["report_date"])
    contracts["available_date"] = pd.to_datetime(contracts["available_date"])
    categories = ["dealer", "asset_manager", "leveraged_money"]
    association_rows = []
    era_rows = []
    point_rows = []
    for asset, group in contracts.groupby("asset"):
        return_column = f"{str(asset).lower()}_ret"
        weekly_return = (
            pd.to_numeric(daily[return_column], errors="coerce")
            .rolling(7, min_periods=7)
            .sum()
            .rename("same_week_log_return")
        )
        group = group.sort_values("report_date").set_index("report_date")
        group = group.join(weekly_return, how="left")
        for category in categories:
            level = pd.to_numeric(group[f"{category}_net_share_oi"], errors="coerce")
            change = level.diff().rename("position_share_change")
            sample = pd.concat([group["same_week_log_return"], change], axis=1).dropna()
            model = sm.OLS(
                sample["same_week_log_return"], sm.add_constant(sample["position_share_change"])
            ).fit(cov_type="HAC", cov_kwds={"maxlags": 4})
            association_rows.append(
                {
                    "asset": asset,
                    "contract_name": group["contract_name"].iloc[0],
                    "category": category,
                    "coefficient_same_week_return_per_unit_net_share_change": float(
                        model.params["position_share_change"]
                    ),
                    "se_hac": float(model.bse["position_share_change"]),
                    "ci_low": float(model.conf_int().loc["position_share_change", 0]),
                    "ci_high": float(model.conf_int().loc["position_share_change", 1]),
                    "pvalue": float(model.pvalues["position_share_change"]),
                    "n": int(model.nobs),
                    "sample_start": sample.index.min().date().isoformat(),
                    "sample_end": sample.index.max().date().isoformat(),
                    "timing": "Tuesday position and seven-day crypto return ending Tuesday; report available Friday proxy",
                    "method": "HAC OLS contemporaneous association; standard contract only",
                }
            )
            for era, start, end in _institutional_eras(asset):
                values = level.loc[level.index.to_series().between(start, end)].dropna()
                if values.empty:
                    continue
                era_rows.append(
                    {
                        "asset": asset,
                        "contract_name": group["contract_name"].iloc[0],
                        "category": category,
                        "era": era,
                        "mean_net_share_oi": float(values.mean()) if len(values) else np.nan,
                        "median_net_share_oi": float(values.median()) if len(values) else np.nan,
                        "n": len(values),
                        "sample_start": values.index.min().date().isoformat()
                        if len(values)
                        else "",
                        "sample_end": values.index.max().date().isoformat() if len(values) else "",
                    }
                )
        point = group.reset_index()[
            [
                "report_date",
                "available_date",
                "asset",
                "contract_name",
                "open_interest",
                *[f"{category}_net_share_oi" for category in categories],
                "same_week_log_return",
            ]
        ]
        point_rows.extend(point.to_dict("records"))
    associations = pd.DataFrame(association_rows)
    associations["qvalue_bh"] = multipletests(associations["pvalue"], method="fdr_bh")[1]
    return (
        associations,
        pd.DataFrame(era_rows),
        pd.DataFrame(point_rows),
    )


def _institutional_eras(asset: str) -> list[tuple[str, pd.Timestamp, pd.Timestamp]]:
    start = pd.Timestamp("2017-01-01") if asset == "BTC" else pd.Timestamp("2021-01-01")
    etf_start = pd.Timestamp("2024-01-11") if asset == "BTC" else pd.Timestamp("2024-07-23")
    return [
        ("pre_us_spot_etf", start, etf_start - pd.Timedelta(days=1)),
        ("us_spot_etf_era", etf_start, pd.Timestamp("2026-06-30")),
    ]


def _moving_block_coefficients(
    data: pd.DataFrame,
    x_columns: list[str],
    reps: int,
    block_length: int,
    seed: int,
) -> np.ndarray:
    y = data["response"].to_numpy(dtype=float)
    x = sm.add_constant(data[x_columns]).to_numpy(dtype=float)
    n = len(data)
    blocks = math.ceil(n / block_length)
    offsets = np.arange(block_length)
    rng = np.random.default_rng(seed)
    coefficients = np.empty((reps, len(x_columns)), dtype=float)
    for index in range(reps):
        starts = rng.integers(0, n - block_length + 1, size=blocks)
        sampled = (starts[:, None] + offsets).ravel()[:n]
        beta, *_ = np.linalg.lstsq(x[sampled], y[sampled], rcond=None)
        coefficients[index] = beta[1:]
    return coefficients


__all__ = [
    "cftc_positioning_associations",
    "distributed_lag_models",
    "flow_concentration",
    "nonlinear_flow_sensitivity",
]
