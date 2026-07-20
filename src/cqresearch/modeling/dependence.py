"""Dependence, common-factor, tail, and dynamic-integration estimators."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests

DEFAULT_SEED = 20260713


def leave_one_out_factor(returns: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Estimate a market factor without mechanically including the target asset."""

    clean = returns.apply(pd.to_numeric, errors="coerce").dropna()
    if clean.shape[1] < 3 or len(clean) < 60:
        raise ValueError("leave-one-out factor requires at least three assets and 60 rows")
    standardized = (clean - clean.mean()) / clean.std(ddof=0)
    _, singular, _ = np.linalg.svd(standardized.to_numpy(), full_matrices=False)
    variance = singular**2 / np.sum(singular**2)
    overview = pd.DataFrame(
        {
            "component": [f"PC{index + 1}" for index in range(len(variance))],
            "variance_share": variance,
            "cumulative_variance_share": np.cumsum(variance),
            "n": len(clean),
            "assets": clean.shape[1],
            "sample_start": clean.index.min().date().isoformat(),
            "sample_end": clean.index.max().date().isoformat(),
            "method": "full-system PCA for aggregate variance share; target-specific rows use leave-one-out PCA",
        }
    )
    rows = []
    for asset in clean:
        others = standardized.drop(columns=asset)
        u, singular_loo, _ = np.linalg.svd(others.to_numpy(), full_matrices=False)
        factor = u[:, 0] * singular_loo[0]
        if np.corrcoef(factor, others.mean(axis=1))[0, 1] < 0:
            factor *= -1
        design = sm.add_constant(factor)
        model = sm.OLS(standardized[asset].to_numpy(), design).fit(
            cov_type="HAC", cov_kwds={"maxlags": 10}
        )
        rows.append(
            {
                "asset": asset,
                "factor_beta": float(model.params[1]),
                "factor_beta_se_hac": float(model.bse[1]),
                "factor_beta_ci_low": float(model.conf_int(alpha=0.05)[1, 0]),
                "factor_beta_ci_high": float(model.conf_int(alpha=0.05)[1, 1]),
                "common_variance_share": float(model.rsquared),
                "idiosyncratic_variance_share": float(1 - model.rsquared),
                "factor_assets": "|".join(others.columns),
                "self_included": False,
                "n": len(clean),
                "sample_start": clean.index.min().date().isoformat(),
                "sample_end": clean.index.max().date().isoformat(),
                "method": "HAC OLS on PC1 estimated from all other S2 assets",
            }
        )
    return overview, pd.DataFrame(rows)


def tail_dependence(
    returns: pd.DataFrame,
    quantiles: tuple[float, ...] = (0.01, 0.025, 0.05, 0.10),
    reps: int = 2000,
    block_length: int = 10,
    sensitivity_blocks: tuple[int, ...] = (5, 20),
    seed: int = DEFAULT_SEED,
) -> pd.DataFrame:
    """Estimate lower-tail joint, conditional, and excess co-exceedance."""

    clean = returns.apply(pd.to_numeric, errors="coerce").dropna()
    if len(clean) < 100 or clean.shape[1] < 2:
        raise ValueError("tail dependence requires at least 100 rows and two assets")
    pairs = [(i, j) for i in range(clean.shape[1]) for j in range(i + 1, clean.shape[1])]
    specifications = [(quantile, block_length) for quantile in quantiles]
    specifications.extend((0.05, block) for block in sensitivity_blocks)
    rows = []
    for spec_index, (quantile, block) in enumerate(specifications):
        thresholds = clean.quantile(quantile)
        events = clean.le(thresholds).to_numpy(dtype=np.float32)
        joint = events.T @ events / len(events)
        boot = _bootstrap_joint(
            events,
            reps=reps,
            block_length=block,
            seed=seed + spec_index * 1009,
        )
        for left, right in pairs:
            excess_samples = boot[:, left, right] - quantile**2
            joint_value = float(joint[left, right])
            rows.append(
                {
                    "asset_i": clean.columns[left],
                    "asset_j": clean.columns[right],
                    "quantile": quantile,
                    "joint_probability": joint_value,
                    "independence_probability": quantile**2,
                    "conditional_probability": joint_value / quantile,
                    "excess_probability": joint_value - quantile**2,
                    "excess_ci_low": float(np.quantile(excess_samples, 0.025)),
                    "excess_ci_high": float(np.quantile(excess_samples, 0.975)),
                    "block_length": block,
                    "bootstrap_reps": reps,
                    "primary_specification": block == block_length,
                    "n": len(clean),
                    "sample_start": clean.index.min().date().isoformat(),
                    "sample_end": clean.index.max().date().isoformat(),
                }
            )
    return pd.DataFrame(rows)


def dynamic_tradfi_exposures(
    frame: pd.DataFrame,
    assets: tuple[str, ...] = ("btc_ret", "eth_ret"),
    features: tuple[str, ...] = ("qqq_ret", "vix_d1", "dxy_ret", "real_yield_d1", "gold_ret"),
    window: int = 252,
    minimum: int = 126,
    step: int = 5,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Estimate rolling conditional exposures and formal ETF-era interactions."""

    available_features = [feature for feature in features if feature in frame]
    if len(available_features) < 3:
        raise ValueError("dynamic integration requires at least three TradFi features")
    rolling_rows = []
    break_rows = []
    diagnostic_rows = []
    for asset in assets:
        columns = [asset, *available_features]
        sample = frame[columns].replace([np.inf, -np.inf], np.nan).dropna()
        if len(sample) < window:
            continue
        standardized = (sample - sample.mean()) / sample.std(ddof=0)
        condition_number = float(np.linalg.cond(sm.add_constant(standardized[available_features])))
        diagnostic_rows.append(
            {
                "asset": asset.removesuffix("_ret").upper(),
                "diagnostic": "full_sample_condition_number",
                "value": condition_number,
                "threshold": 30.0,
                "status": "pass" if condition_number < 30 else "review",
                "n": len(sample),
            }
        )
        for end in range(window, len(sample) + 1, step):
            chunk = sample.iloc[end - window : end]
            x = sm.add_constant(chunk[available_features])
            model = sm.OLS(chunk[asset], x).fit(cov_type="HAC", cov_kwds={"maxlags": 10})
            for feature in available_features:
                rolling_rows.append(
                    {
                        "date": chunk.index[-1].date().isoformat(),
                        "asset": asset.removesuffix("_ret").upper(),
                        "feature_id": feature,
                        "beta": float(model.params[feature]),
                        "se_hac": float(model.bse[feature]),
                        "ci_low": float(model.conf_int().loc[feature, 0]),
                        "ci_high": float(model.conf_int().loc[feature, 1]),
                        "r_squared": float(model.rsquared),
                        "window": window,
                        "n": len(chunk),
                        "sample_start": chunk.index.min().date().isoformat(),
                        "sample_end": chunk.index.max().date().isoformat(),
                    }
                )
        post = (sample.index >= pd.Timestamp("2024-01-11")).astype(float)
        for feature in available_features:
            design = pd.DataFrame(
                {
                    "feature": sample[feature],
                    "post": post,
                    "interaction": sample[feature] * post,
                },
                index=sample.index,
            )
            model = sm.OLS(sample[asset], sm.add_constant(design)).fit(
                cov_type="HAC", cov_kwds={"maxlags": 10}
            )
            break_rows.append(
                {
                    "asset": asset.removesuffix("_ret").upper(),
                    "feature_id": feature,
                    "pre_beta": float(model.params["feature"]),
                    "era_beta_change": float(model.params["interaction"]),
                    "era_beta_change_se_hac": float(model.bse["interaction"]),
                    "era_beta_change_pvalue": float(model.pvalues["interaction"]),
                    "era_beta": float(model.params["feature"] + model.params["interaction"]),
                    "break_date": "2024-01-11",
                    "n": int(model.nobs),
                    "sample_start": sample.index.min().date().isoformat(),
                    "sample_end": sample.index.max().date().isoformat(),
                    "method": "HAC era-interaction test; descriptive break at predeclared ETF date",
                }
            )
    if not rolling_rows:
        raise ValueError(f"no rolling windows met minimum={minimum} and window={window}")
    breaks = pd.DataFrame(break_rows)
    breaks["era_beta_change_qvalue_bh"] = multipletests(
        breaks["era_beta_change_pvalue"], method="fdr_bh"
    )[1]
    return pd.DataFrame(rolling_rows), breaks, pd.DataFrame(diagnostic_rows)


def _bootstrap_joint(
    events: np.ndarray,
    reps: int,
    block_length: int,
    seed: int,
    chunk_size: int = 100,
) -> np.ndarray:
    n, assets = events.shape
    if block_length <= 0 or block_length > n:
        raise ValueError("block_length must be between one and the sample length")
    rng = np.random.default_rng(seed)
    output = np.empty((reps, assets, assets), dtype=np.float32)
    blocks = math.ceil(n / block_length)
    offsets = np.arange(block_length)
    for first in range(0, reps, chunk_size):
        count = min(chunk_size, reps - first)
        starts = rng.integers(0, n - block_length + 1, size=(count, blocks))
        indices = (starts[:, :, None] + offsets).reshape(count, -1)[:, :n]
        sampled = events[indices]
        output[first : first + count] = (
            np.einsum("bni,bnj->bij", sampled, sampled, optimize=True) / n
        )
    return output


__all__ = ["dynamic_tradfi_exposures", "leave_one_out_factor", "tail_dependence"]
