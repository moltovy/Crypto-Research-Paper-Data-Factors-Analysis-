"""Monthly point-in-time, liquidity-state, chain-panel, and measurement models."""

from __future__ import annotations

from itertools import pairwise
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

from cqresearch.data.contracts import DATA_CUTOFF


def pit_market_structure(pit: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Build concentration, membership-transition, and HHI decomposition tables."""

    frame = pit.copy()
    frame["snapshot_date"] = pd.to_datetime(frame["snapshot_date"])
    partial = frame.get("is_partial_month", pd.Series(False, index=frame.index)).fillna(False)
    frame = frame[
        frame["snapshot_date"].le(DATA_CUTOFF)
        & ~partial
        & pd.to_numeric(frame["rank_full_market"], errors="coerce").le(100)
    ].copy()
    frame["market_cap_usd"] = pd.to_numeric(frame["market_cap_usd"], errors="coerce")
    frame = frame[frame["market_cap_usd"].gt(0)]
    rows = []
    memberships: dict[pd.Timestamp, set[str]] = {}
    shares_by_month: dict[pd.Timestamp, pd.Series] = {}
    for date, group in frame.groupby("snapshot_date"):
        group = group.sort_values("rank_full_market")
        shares = group.set_index("asset_key")["market_cap_usd"]
        shares = shares / shares.sum()
        shares_by_month[pd.Timestamp(date)] = shares
        memberships[pd.Timestamp(date)] = set(shares.index.astype(str))
        entropy = float(-(shares * np.log(shares)).sum())
        rows.append(
            {
                "snapshot_date": pd.Timestamp(date).date().isoformat(),
                "assets": len(shares),
                "top1_share": float(shares.nlargest(1).sum()),
                "top5_share": float(shares.nlargest(5).sum()),
                "top10_share": float(shares.nlargest(10).sum()),
                "hhi": float((shares**2).sum()),
                "entropy": entropy,
                "effective_asset_count": float(np.exp(entropy)),
                "denominator": "sum of positive market capitalization for full-market top 100 snapshot",
            }
        )
    transition_rows = []
    decomposition_rows = []
    dates = sorted(memberships)
    for prior_date, date in pairwise(dates):
        prior_members = memberships[prior_date]
        current_members = memberships[date]
        entrants = current_members - prior_members
        exits = prior_members - current_members
        continuing = current_members & prior_members
        prior_shares = shares_by_month[prior_date]
        current_shares = shares_by_month[date]
        transition_rows.append(
            {
                "snapshot_date": date.date().isoformat(),
                "prior_snapshot_date": prior_date.date().isoformat(),
                "entries": len(entrants),
                "exits": len(exits),
                "continuing": len(continuing),
                "turnover_rate": (len(entrants) + len(exits))
                / max(len(prior_members | current_members), 1),
                "one_month_survival_rate": len(continuing) / max(len(prior_members), 1),
            }
        )
        continuing_effect = sum(
            current_shares.get(asset, 0.0) ** 2 - prior_shares.get(asset, 0.0) ** 2
            for asset in sorted(continuing)
        )
        entry_effect = sum(current_shares.get(asset, 0.0) ** 2 for asset in sorted(entrants))
        exit_effect = -sum(prior_shares.get(asset, 0.0) ** 2 for asset in sorted(exits))
        actual_change = float((current_shares**2).sum() - (prior_shares**2).sum())
        decomposition_rows.append(
            {
                "snapshot_date": date.date().isoformat(),
                "prior_snapshot_date": prior_date.date().isoformat(),
                "hhi_change": actual_change,
                "continuing_share_effect": continuing_effect,
                "entry_effect": entry_effect,
                "exit_effect": exit_effect,
                "decomposition_sum": continuing_effect + entry_effect + exit_effect,
                "residual": actual_change - continuing_effect - entry_effect - exit_effect,
            }
        )
    return pd.DataFrame(rows), pd.DataFrame(transition_rows), pd.DataFrame(decomposition_rows)


def price_adjusted_liquidity_state(
    daily: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Residualize USD TVL growth on broad crypto returns using HAC inference."""

    columns = [
        "defi_tvl_growth",
        "stablecoin_supply_growth",
        "btc_ret",
        "eth_ret",
        "total3_ret",
    ]
    frame = daily[columns].apply(pd.to_numeric, errors="coerce").dropna()
    x_columns = ["btc_ret", "eth_ret", "total3_ret"]
    model = sm.OLS(frame["defi_tvl_growth"], sm.add_constant(frame[x_columns])).fit(
        cov_type="HAC", cov_kwds={"maxlags": 10}
    )
    state = frame.copy()
    state["fitted_valuation_component"] = model.fittedvalues
    state["price_adjusted_tvl_residual"] = model.resid
    rolling_mean = model.resid.rolling(365, min_periods=180).mean()
    rolling_std = model.resid.rolling(365, min_periods=180).std()
    state["price_adjusted_tvl_residual_z365"] = (model.resid - rolling_mean) / rolling_std
    state.index.name = "date"
    state = state.reset_index()
    state["date"] = pd.to_datetime(state["date"]).dt.date.astype(str)
    coefficients = []
    for feature in ["const", *x_columns]:
        coefficients.append(
            {
                "feature": feature,
                "coefficient": float(model.params[feature]),
                "se_hac": float(model.bse[feature]),
                "ci_low": float(model.conf_int().loc[feature, 0]),
                "ci_high": float(model.conf_int().loc[feature, 1]),
                "pvalue": float(model.pvalues[feature]),
                "r_squared": float(model.rsquared),
                "n": int(model.nobs),
                "sample_start": frame.index.min().date().isoformat(),
                "sample_end": frame.index.max().date().isoformat(),
                "method": "HAC OLS residualization of raw USD TVL growth on BTC, ETH, and TOTAL3 returns",
            }
        )
    return state, pd.DataFrame(coefficients)


def mvrv_measurement_mechanics(daily: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "btc_ret",
        "d_log_mvrv",
        "d_log_market_cap",
        "d_log_realized_cap",
        "identity_residual",
    ]
    frame = daily[columns].apply(pd.to_numeric, errors="coerce")
    rows = []
    for left, right in [
        ("btc_ret", "d_log_mvrv"),
        ("d_log_mvrv", "d_log_market_cap"),
        ("d_log_mvrv", "d_log_realized_cap"),
        ("btc_ret", "identity_residual"),
    ]:
        pair = frame[[left, right]].dropna()
        rows.append(
            {
                "metric": f"correlation__{left}__{right}",
                "value": float(pair[left].corr(pair[right])),
                "n": len(pair),
                "sample_start": pair.index.min().date().isoformat(),
                "sample_end": pair.index.max().date().isoformat(),
                "interpretation": "measurement-mechanics diagnostic; excluded from primary BTC/ETH models",
            }
        )
    residual = frame["identity_residual"].dropna()
    rows.append(
        {
            "metric": "identity_residual_absolute_median",
            "value": float(residual.abs().median()),
            "n": len(residual),
            "sample_start": residual.index.min().date().isoformat(),
            "sample_end": residual.index.max().date().isoformat(),
            "interpretation": "measurement-mechanics residual from source timing and conventions in dlog(MVRV)=dlog(market cap)-dlog(realized cap)",
        }
    )
    return pd.DataFrame(rows)


def chain_panel_model(root: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Estimate a monthly four-chain FE association if the preregistered gate passes."""

    source = root / "data_local" / "raw" / "artemis"
    chain_names = ["Ethereum", "Solana", "Avalanche C-Chain", "Near"]
    metrics = {
        "market_cap": ("Chains - Market Cap.csv", "last"),
        "fees": ("Chains - Fees.csv", "sum"),
        "revenue": ("Chains - Revenue.csv", "sum"),
    }
    panels = {}
    coverage_rows = []
    for metric, (filename, aggregation) in metrics.items():
        frame = pd.read_csv(source / filename, parse_dates=["date"]).set_index("date")
        available = frame[chain_names].apply(pd.to_numeric, errors="coerce")
        monthly = (
            available.resample("ME").last()
            if aggregation == "last"
            else available.resample("ME").sum(min_count=1)
        )
        panels[metric] = monthly
        for chain in chain_names:
            valid = monthly[chain].dropna()
            coverage_rows.append(
                {
                    "chain": chain,
                    "metric": metric,
                    "months": len(valid),
                    "first_month": valid.index.min().date().isoformat() if len(valid) else "",
                    "last_month": valid.index.max().date().isoformat() if len(valid) else "",
                }
            )
    common = pd.concat(
        {metric: panel.stack(future_stack=True).rename(metric) for metric, panel in panels.items()},
        axis=1,
    ).dropna()
    common.index.names = ["month", "chain"]
    complete_months = (
        common.reset_index()
        .groupby("month")["chain"]
        .nunique()
        .loc[lambda value: value.eq(4)]
        .index
    )
    common = common.loc[common.index.get_level_values("month").isin(complete_months)]
    eligible = (
        common.reset_index().groupby("chain")["month"].nunique().ge(36).sum() >= 4
        and common.index.get_level_values("month").nunique() >= 36
    )
    if not eligible:
        coverage = pd.DataFrame(coverage_rows)
        coverage["gate_status"] = "fail"
        return pd.DataFrame(), coverage
    common["market_cap_share"] = common["market_cap"] / common.groupby(level="month")[
        "market_cap"
    ].transform("sum")
    common["market_cap_share_change"] = common.groupby(level="chain")["market_cap_share"].diff()
    for metric in ["fees", "revenue"]:
        common[f"log_{metric}_lag1"] = common.groupby(level="chain")[metric].transform(
            lambda series: np.log1p(series).shift(1)
        )
    rows = []
    for feature in ["log_fees_lag1", "log_revenue_lag1"]:
        estimation = (
            common[["market_cap_share_change", feature]]
            .dropna()
            .reorder_levels(["chain", "month"])
            .sort_index()
        )
        standardized = estimation.copy()
        standardized[feature] = standardized.groupby(level="chain")[feature].transform(
            lambda series: (series - series.mean()) / series.std(ddof=0)
        )
        model = PanelOLS(
            standardized["market_cap_share_change"],
            standardized[[feature]],
            entity_effects=True,
            time_effects=True,
            drop_absorbed=True,
        ).fit(cov_type="kernel", kernel="bartlett", bandwidth=4)
        rows.append(
            {
                "feature": feature,
                "coefficient": float(model.params[feature]),
                "standard_error_driscoll_kraay": float(model.std_errors[feature]),
                "ci_low": float(model.conf_int().loc[feature, "lower"]),
                "ci_high": float(model.conf_int().loc[feature, "upper"]),
                "pvalue": float(model.pvalues[feature]),
                "within_r_squared": float(model.rsquared_within),
                "entities": int(estimation.index.get_level_values("chain").nunique()),
                "periods": int(estimation.index.get_level_values("month").nunique()),
                "n": int(model.nobs),
                "sample_start": estimation.index.get_level_values("month").min().date().isoformat(),
                "sample_end": estimation.index.get_level_values("month").max().date().isoformat(),
                "method": "two-way fixed effects with Driscoll-Kraay covariance",
            }
        )
    coverage = pd.DataFrame(coverage_rows)
    coverage["gate_status"] = "pass"
    return pd.DataFrame(rows), coverage


__all__ = [
    "chain_panel_model",
    "mvrv_measurement_mechanics",
    "pit_market_structure",
    "price_adjusted_liquidity_state",
]
