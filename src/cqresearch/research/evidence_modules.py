"""Direct-build analytical modules for the four registered research questions."""

from __future__ import annotations

import math
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from cqresearch.core.artifacts import write_csv, write_json
from cqresearch.data.contracts import result_sample_summary
from cqresearch.modeling.dependence import (
    dynamic_tradfi_exposures,
    leave_one_out_factor,
    tail_dependence,
)
from cqresearch.modeling.etf_plumbing import (
    cftc_positioning_associations,
    distributed_lag_models,
    flow_concentration,
    nonlinear_flow_sensitivity,
)
from cqresearch.modeling.leverage_tail import (
    connectedness_grid,
    leverage_horizon_sensitivity,
    leverage_tail_model,
    quantile_and_expected_shortfall,
    systemic_tail_associations,
)
from cqresearch.modeling.market_structure import (
    chain_panel_model,
    mvrv_measurement_mechanics,
    pit_market_structure,
    price_adjusted_liquidity_state,
)
from cqresearch.pipelines.final_research import load_events
from cqresearch.research.samples import stable_core_returns
from cqresearch.viz.theme import PALETTE, TOKENS, add_figure_header, apply_theme, style_axis

SEED = 20260713


@dataclass
class EvidenceBuild:
    tables: dict[str, pd.DataFrame]
    figures: list[Path]
    key_results: list[dict[str, Any]]
    claims: list[dict[str, Any]]
    figure_notes: dict[str, str]


def build_dependence(root: Path, module_dir: Path) -> EvidenceBuild:
    returns = stable_core_returns(root)
    overview, factors = leave_one_out_factor(returns)
    tails = tail_dependence(returns)
    relative_risk = _relative_risk(returns)
    coverage = _coverage(returns, "S2 fixed PIT-eligible stable core")
    full_pc1 = float(overview.loc[overview["component"].eq("PC1"), "variance_share"].iat[0])
    common = factors.assign(full_system_pc1_share=full_pc1)
    figures_dir = module_dir / "figures"
    figure = _figure_dependence(
        common,
        tails,
        figures_dir / "01_common_factor_tail_dependence.png",
    )
    q5 = tails[tails["quantile"].eq(0.05) & tails["primary_specification"]]
    median_excess = float(q5["excess_probability"].median())
    sample = result_sample_summary(common)
    claim_text = (
        f"Within S2, full-system PC1 accounts for {full_pc1:.1%} of standardized return "
        f"variation, while median 5% lower-tail co-exceedance is {median_excess:.1%} above "
        "the independence benchmark."
    )
    return EvidenceBuild(
        tables={
            "asset_return_coverage.csv": coverage,
            "common_factor_overview.csv": overview,
            "common_factor_results.csv": common,
            "tail_dependence.csv": tails,
            "relative_risk_diagnostics.csv": relative_risk,
        },
        figures=[figure],
        key_results=[
            _result(
                "Common variation and lower-tail dependence",
                f"PC1={full_pc1:.1%}; median q=5% excess={median_excess:.1%}",
                "HAC factor-beta intervals and 2,000-replication moving-block tail intervals",
                sample,
                "Dependence is broad but heterogeneous across assets.",
                "Tail thresholds 1%, 2.5%, 5%, 10%; block lengths 5, 10, 20",
            )
        ],
        claims=[
            _claim(
                "dependence_01",
                "01_cross_asset_dependence_regimes",
                claim_text,
                "tables/common_factor_results.csv; tables/tail_dependence.csv",
                "figures/01_common_factor_tail_dependence.png",
                sample,
                "Leave-one-out PCA/HAC factor regressions and moving-block tail inference.",
                "S2 is a fixed 2021 PIT-eligible universe; results do not establish causation, forecasting value, or investability.",
            )
        ],
        figure_notes={
            figure.name: "Panel A excludes each target from its own factor. Panel B compares BTC pair co-exceedance with the q-squared independence benchmark using moving-block intervals."
        },
    )


def build_tradfi(root: Path, module_dir: Path) -> EvidenceBuild:
    panel = _panel(root, "feature_store_tradfi_daily.parquet")
    rolling, breaks, diagnostics = dynamic_tradfi_exposures(panel)
    figure = _figure_tradfi(
        rolling,
        breaks,
        module_dir / "figures" / "02_dynamic_tradfi_integration.png",
    )
    qqq = breaks[breaks["feature_id"].eq("qqq_ret")]
    estimate = "; ".join(
        f"{row.asset} {row.pre_beta:.2f} to {row.era_beta:.2f} "
        f"(change p={row.era_beta_change_pvalue:.3f})"
        for row in qqq.itertuples(index=False)
    )
    sample = result_sample_summary(breaks)
    return EvidenceBuild(
        tables={
            "dynamic_tradfi_exposures.csv": rolling,
            "break_tests.csv": breaks,
            "tradfi_diagnostics.csv": diagnostics,
        },
        figures=[figure],
        key_results=[
            _result(
                "Conditional QQQ exposure around the registered BTC ETF era",
                estimate,
                "HAC 95% intervals and era-interaction p-values",
                sample,
                "Conditional equity co-movement changes are period comparisons.",
                "252-session rolling windows; multivariate controls; predeclared break date",
            )
        ],
        claims=[
            _claim(
                "tradfi_01",
                "02_macro_tradfi_integration",
                f"Conditional QQQ exposure estimates differ across the predeclared BTC ETF-era split: {estimate}.",
                "tables/dynamic_tradfi_exposures.csv; tables/break_tests.csv",
                "figures/02_dynamic_tradfi_integration.png",
                sample,
                "252-session multivariate HAC exposures and formal era interactions.",
                "The split is descriptive; contemporaneous exposures do not identify ETF effects or causal transmission.",
            )
        ],
        figure_notes={
            figure.name: "Rolling QQQ coefficients condition on VIX, DXY, real-yield changes, and gold; the forest reports formal predeclared era interactions."
        },
    )


def build_leverage(root: Path, module_dir: Path) -> EvidenceBuild:
    daily = _panel(root, "feature_store_daily.parquet")
    returns = stable_core_returns(root)
    curve, diagnostics = leverage_tail_model(daily)
    horizon_sensitivity = leverage_horizon_sensitivity(daily)
    quantile, expected_shortfall = quantile_and_expected_shortfall(daily)
    systemic = systemic_tail_associations(returns)
    connectedness = connectedness_grid(returns)
    quantile_es = _combine_quantile_es(quantile, expected_shortfall)
    figure = _figure_leverage(
        curve,
        connectedness,
        module_dir / "figures" / "03_leverage_tail_connectedness.png",
    )
    probability_low = float(curve["predicted_tail_probability"].min())
    probability_high = float(curve["predicted_tail_probability"].max())
    primary = connectedness[connectedness["specification"].eq("primary")]
    connectedness_low = float(primary["connectedness_pct"].min() / 100)
    connectedness_high = float(primary["connectedness_pct"].max() / 100)
    sample = result_sample_summary(curve)
    return EvidenceBuild(
        tables={
            "leverage_tail_model.csv": curve,
            "leverage_tail_diagnostics.csv": diagnostics,
            "leverage_tail_horizon_sensitivity.csv": horizon_sensitivity,
            "quantile_es.csv": quantile_es,
            "quantile_regression.csv": quantile,
            "expected_shortfall.csv": expected_shortfall,
            "systemic_tail_association.csv": systemic,
            "connectedness.csv": connectedness,
        },
        figures=[figure],
        key_results=[
            _result(
                "Lagged leverage state and tail stress",
                f"fitted tail probability range {probability_low:.1%}-{probability_high:.1%}",
                "HAC spline-GLM confidence band",
                sample,
                "The fitted association is nonlinear and should not be read as a directional rule.",
                "Quantile regression, state expected shortfall, FEVD window/horizon grid",
            ),
            _result(
                "Stable-core volatility connectedness",
                f"primary generalized-FEVD range {connectedness_low:.1%}-{connectedness_high:.1%}",
                "descriptive rolling estimate; row-sum diagnostics in source table",
                result_sample_summary(primary),
                "Absolute-return connectedness varies materially over time.",
                "180/252/365 windows and 5/10/20 horizons",
            ),
        ],
        claims=[
            _claim(
                "leverage_01",
                "03_derivatives_leverage_liquidations",
                f"Across observed support, lagged BTC leverage states coincide with fitted next-session lower-tail probabilities from {probability_low:.1%} to {probability_high:.1%}.",
                "tables/leverage_tail_model.csv; tables/quantile_es.csv; tables/connectedness.csv",
                "figures/03_leverage_tail_connectedness.png",
                sample,
                "Spline logistic association with HAC covariance, quantile/ES diagnostics, and generalized-FEVD connectedness.",
                "The relationship is associational, nonlinear, and not a forecast, trading signal, or liquidation-cause estimate.",
            )
        ],
        figure_notes={
            figure.name: "The spline is restricted to the central observed leverage support. Connectedness uses a stable-core generalized FEVD and is a stress-transmission description, not a forecast."
        },
    )


def build_institutional(root: Path, module_dir: Path) -> EvidenceBuild:
    etf = _panel(root, "feature_store_etf_trading_daily.parquet")
    daily = _panel(root, "feature_store_daily.parquet")
    coefficients, cumulative, timing = distributed_lag_models(etf)
    nonlinear = nonlinear_flow_sensitivity(etf)
    concentration = flow_concentration()
    cftc = pd.read_parquet(root / "data_local" / "processed" / "cftc_financial_futures.parquet")
    positioning, positioning_eras, positioning_points = cftc_positioning_associations(cftc, daily)
    corporate = pd.DataFrame(
        [
            {
                "analysis": "corporate_exposure_eras",
                "status": "not_run",
                "reason": "SEC EDGAR eligibility probe returned HTTP 403 for official anonymous endpoints",
                "fallback": "no corporate holdings or exposure-era claim",
            }
        ]
    )
    figure = _figure_institutional(
        coefficients,
        positioning_eras,
        module_dir / "figures" / "04_institutional_market_plumbing.png",
    )
    return_rows = coefficients[coefficients["response"].eq("return")]
    supported = return_rows[
        (return_rows["simultaneous_ci_low"] > 0) | (return_rows["simultaneous_ci_high"] < 0)
    ]
    sample = result_sample_summary(return_rows)
    claim_text = (
        f"Across {len(return_rows)} asset-lag return coefficients, {len(supported)} have 95% "
        "moving-block simultaneous intervals excluding zero under the reported-date convention."
    )
    return EvidenceBuild(
        tables={
            "etf_distributed_lags.csv": coefficients,
            "etf_cumulative_lags.csv": cumulative,
            "etf_timing_sensitivity.csv": timing,
            "etf_nonlinear_sensitivity.csv": nonlinear,
            "etf_flow_concentration.csv": concentration,
            "institutional_positioning.csv": positioning,
            "institutional_positioning_eras.csv": positioning_eras,
            "institutional_positioning_points.csv": positioning_points,
            "corporate_exposure_eras.csv": corporate,
        },
        figures=[figure],
        key_results=[
            _result(
                "ETF return lag coefficients",
                claim_text,
                "2,000-replication moving-block max-t simultaneous intervals",
                sample,
                "Weak coefficients remain weak rather than being rescued by lag selection.",
                "reported-date and one-session-shift timing conventions; returns and realized volatility",
            )
        ],
        claims=[
            _claim(
                "institutional_01",
                "04_etf_institutional_flows",
                claim_text + " Simultaneity prevents a price-impact interpretation.",
                "tables/etf_distributed_lags.csv; tables/etf_timing_sensitivity.csv; tables/institutional_positioning.csv",
                "figures/04_institutional_market_plumbing.png",
                sample,
                "Distributed-lag HAC OLS with moving-block simultaneous bands; CFTC positioning is separate contemporaneous context.",
                "ETF reporting time is unresolved, CFTC data is weekly and released after the as-of date, and neither design identifies causality.",
            )
        ],
        figure_notes={
            figure.name: "ETF lag coefficients use simultaneous bands and no pre-inception or holiday zero fill. CFTC panels use standard contracts only and report period averages as context."
        },
    )


def build_liquidity(root: Path, module_dir: Path) -> EvidenceBuild:
    daily = _panel(root, "feature_store_daily.parquet")
    state, coefficients = price_adjusted_liquidity_state(daily)
    mechanics = mvrv_measurement_mechanics(daily)
    summary = _liquidity_summary(state)
    figure = _figure_liquidity(
        state,
        mechanics,
        module_dir / "figures" / "05_liquidity_measurement_diagnostics.png",
    )
    r_squared = float(coefficients["r_squared"].iloc[0])
    mvrv_corr = float(
        mechanics.loc[mechanics["metric"].eq("correlation__btc_ret__d_log_mvrv"), "value"].iat[0]
    )
    sample = result_sample_summary(coefficients)
    return EvidenceBuild(
        tables={
            "liquidity_state.csv": state,
            "liquidity_state_coefficients.csv": coefficients,
            "liquidity_state_summary.csv": summary,
            "measurement_mechanics.csv": mechanics,
        },
        figures=[figure],
        key_results=[
            _result(
                "Price-adjusted USD TVL state",
                f"market-return controls explain R-squared={r_squared:.3f}",
                "HAC coefficient intervals",
                sample,
                "The residual is an endogenous state proxy, not an exogenous liquidity shock.",
                "BTC, ETH, and TOTAL3 controls; rolling residual standardization",
            ),
            _result(
                "MVRV measurement mechanics",
                f"corr(BTC return, change in log MVRV)={mvrv_corr:.3f}",
                "descriptive identity diagnostic",
                result_sample_summary(mechanics),
                "Same-day MVRV remains excluded from primary BTC/ETH models.",
                "market-cap/realized-cap identity residual",
            ),
        ],
        claims=[
            _claim(
                "liquidity_01",
                "05_stablecoin_defi_liquidity",
                f"Crypto-market return controls explain {r_squared:.1%} of daily raw USD TVL growth in the stated HAC residualization; the remaining series is an endogenous liquidity-state proxy.",
                "tables/liquidity_state.csv; tables/liquidity_state_coefficients.csv; tables/measurement_mechanics.csv",
                "figures/05_liquidity_measurement_diagnostics.png",
                sample,
                "HAC residualization of USD TVL growth; MVRV identity audit is appendix measurement evidence.",
                "USD TVL remains valuation-sensitive, stablecoin and TVL measures are endogenous, and same-day MVRV is mechanically price-linked.",
            )
        ],
        figure_notes={
            figure.name: "The liquidity residual is standardized only after contemporaneous market-return controls. The MVRV panel is a measurement warning, not factor evidence."
        },
    )


def build_market_structure(root: Path, module_dir: Path) -> EvidenceBuild:
    pit = pd.read_parquet(root / "data_local" / "processed" / "market_structure_monthly.parquet")
    concentration, transitions, decomposition = pit_market_structure(pit)
    chain_panel, chain_coverage = chain_panel_model(root)
    figure = _figure_market_structure(
        concentration,
        transitions,
        module_dir / "figures" / "07_pit_concentration_turnover.png",
    )
    first = concentration.iloc[0]
    last = concentration.iloc[-1]
    median_turnover = float(transitions["turnover_rate"].median())
    sample = result_sample_summary(concentration.rename(columns={"snapshot_date": "sample_end"}))
    claim_text = (
        f"Across complete monthly PIT snapshots, effective asset count changed from "
        f"{first.effective_asset_count:.1f} to {last.effective_asset_count:.1f}, while median "
        f"one-month membership turnover was {median_turnover:.1%}."
    )
    return EvidenceBuild(
        tables={
            "pit_concentration.csv": concentration,
            "pit_membership_transitions.csv": transitions,
            "pit_concentration_decomposition.csv": decomposition,
            "chain_panel.csv": chain_panel,
            "chain_panel_coverage.csv": chain_coverage,
        },
        figures=[figure],
        key_results=[
            _result(
                "Point-in-time concentration and turnover",
                claim_text,
                "descriptive monthly census within available top-100 snapshots",
                sample,
                "Composition and concentration changed materially over the sample.",
                "HHI identity decomposition; entries, exits, survival; partial-month exclusion",
            )
        ],
        claims=[
            _claim(
                "market_structure_01",
                "07_chain_fundamentals_sector_dynamics",
                claim_text,
                "tables/pit_concentration.csv; tables/pit_membership_transitions.csv; tables/pit_concentration_decomposition.csv",
                "figures/07_pit_concentration_turnover.png",
                sample,
                "Monthly point-in-time concentration, entropy, effective count, membership transition, and exact HHI decomposition.",
                "Monthly snapshots support market-structure statements only; they do not establish daily constituent performance or historical altseason behavior.",
            )
        ],
        figure_notes={
            figure.name: "Effective asset count is an entropy transformation; turnover uses entries plus exits relative to the membership union. June 2026 partial data is excluded."
        },
    )


def build_synthesis(root: Path, module_dir: Path) -> EvidenceBuild:
    daily = _panel(root, "feature_store_daily.parquet")
    events = load_events(root)
    events["date"] = pd.to_datetime(events["date"])
    events = events[events["date"].le(pd.Timestamp("2026-06-30"))].copy()
    responses = _event_responses(events, daily)
    ledger = _claim_ledger(root)
    robustness = _robustness_summary(ledger)
    figure = _figure_events(
        responses,
        module_dir / "figures" / "09_event_atlas_appendix.png",
    )
    return EvidenceBuild(
        tables={
            "event_registry.csv": events,
            "event_response_matrix.csv": responses,
            "evidence_ledger.csv": ledger,
            "robustness_summary.csv": robustness,
        },
        figures=[figure],
        key_results=[
            _result(
                "Registered event atlas",
                f"{events['event_id'].nunique()} events and {len(responses)} asset-window rows",
                "empirical non-event-window percentile and two-sided placebo p-value",
                result_sample_summary(responses),
                "Event responses remain appendix diagnostics.",
                "+1/+5/+10 windows; event-day exclusion; non-overlapping placebo starts",
            )
        ],
        claims=[
            _claim(
                "synthesis_01",
                "09_event_stress_cross_module_synthesis",
                "Registered event-window responses vary substantially across events and assets and remain appendix sensitivity evidence rather than causal estimates.",
                "tables/event_response_matrix.csv; tables/evidence_ledger.csv",
                "figures/09_event_atlas_appendix.png",
                result_sample_summary(responses),
                "Fixed post-event windows with empirical non-event-window comparison and cross-module claim ledger.",
                "Event windows are not an identification design; overlapping market developments and event selection constrain interpretation.",
            )
        ],
        figure_notes={
            figure.name: "The event atlas shows +1 through +10 cumulative log returns and empirical percentile ranks. It is intentionally outside the root README."
        },
    )


def build_evidence_figures(module_id: str, root: Path) -> list[Path]:
    """Regenerate figures strictly from canonical analytical tables."""

    module_dir = root / "research" / module_id
    tables = module_dir / "tables"
    figures = module_dir / "figures"
    if module_id == "01_cross_asset_dependence_regimes":
        return [
            _figure_dependence(
                _read(tables, "common_factor_results.csv"),
                _read(tables, "tail_dependence.csv"),
                figures / "01_common_factor_tail_dependence.png",
            )
        ]
    if module_id == "02_macro_tradfi_integration":
        return [
            _figure_tradfi(
                _read(tables, "dynamic_tradfi_exposures.csv"),
                _read(tables, "break_tests.csv"),
                figures / "02_dynamic_tradfi_integration.png",
            )
        ]
    if module_id == "03_derivatives_leverage_liquidations":
        return [
            _figure_leverage(
                _read(tables, "leverage_tail_model.csv"),
                _read(tables, "connectedness.csv"),
                figures / "03_leverage_tail_connectedness.png",
            )
        ]
    if module_id == "04_etf_institutional_flows":
        return [
            _figure_institutional(
                _read(tables, "etf_distributed_lags.csv"),
                _read(tables, "institutional_positioning_eras.csv"),
                figures / "04_institutional_market_plumbing.png",
            )
        ]
    if module_id == "05_stablecoin_defi_liquidity":
        return [
            _figure_liquidity(
                _read(tables, "liquidity_state.csv"),
                _read(tables, "measurement_mechanics.csv"),
                figures / "05_liquidity_measurement_diagnostics.png",
            )
        ]
    if module_id == "07_chain_fundamentals_sector_dynamics":
        return [
            _figure_market_structure(
                _read(tables, "pit_concentration.csv"),
                _read(tables, "pit_membership_transitions.csv"),
                figures / "07_pit_concentration_turnover.png",
            )
        ]
    if module_id == "09_event_stress_cross_module_synthesis":
        return [
            _figure_events(
                _read(tables, "event_response_matrix.csv"), figures / "09_event_atlas_appendix.png"
            )
        ]
    raise KeyError(module_id)


def _panel(root: Path, name: str) -> pd.DataFrame:
    frame = pd.read_parquet(root / "data_local" / "processed" / name)
    frame.index = pd.to_datetime(frame.index)
    return frame.sort_index()


def _read(tables: Path, name: str) -> pd.DataFrame:
    return pd.read_csv(tables / name)


def _coverage(frame: pd.DataFrame, rule: str) -> pd.DataFrame:
    rows = []
    for column in frame:
        valid = frame[column].dropna()
        rows.append(
            {
                "asset": column,
                "first_date": valid.index.min().date().isoformat(),
                "last_date": valid.index.max().date().isoformat(),
                "observations": len(valid),
                "coverage": float(valid.notna().sum() / len(frame)),
                "rule": rule,
            }
        )
    return pd.DataFrame(rows)


def _relative_risk(returns: pd.DataFrame) -> pd.DataFrame:
    clean = returns.dropna()
    btc_tail = clean["BTC"].le(clean["BTC"].quantile(0.05))
    rows = []
    for asset in clean:
        tail = clean[asset].le(clean[asset].quantile(0.05))
        downside = clean.loc[btc_tail, [asset, "BTC"]]
        beta = np.nan
        if asset != "BTC" and downside["BTC"].var() > 0:
            beta = float(downside[asset].cov(downside["BTC"]) / downside["BTC"].var())
        rows.append(
            {
                "asset": asset,
                "annualized_volatility": float(clean[asset].std() * math.sqrt(365)),
                "expected_shortfall_5pct": float(clean.loc[tail, asset].mean()),
                "btc_tail_downside_beta": beta,
                "n": len(clean),
                "sample_start": clean.index.min().date().isoformat(),
                "sample_end": clean.index.max().date().isoformat(),
                "method": "matched S2 descriptive risk diagnostics",
            }
        )
    return pd.DataFrame(rows)


def _combine_quantile_es(quantile: pd.DataFrame, es: pd.DataFrame) -> pd.DataFrame:
    q = quantile.assign(
        result_type="quantile_regression",
        metric=quantile["feature"],
        estimate=quantile["coefficient"],
    )
    e = es.assign(
        result_type="expected_shortfall",
        metric="leverage_state_" + es["leverage_state"].astype(str),
        estimate=es["expected_shortfall_5pct"],
    )
    columns = [
        "result_type",
        "metric",
        "estimate",
        "ci_low",
        "ci_high",
        "n",
        "sample_start",
        "sample_end",
    ]
    return pd.concat([q.reindex(columns=columns), e.reindex(columns=columns)], ignore_index=True)


def _liquidity_summary(state: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for column in [
        "stablecoin_supply_growth",
        "price_adjusted_tvl_residual",
        "price_adjusted_tvl_residual_z365",
    ]:
        values = pd.to_numeric(state[column], errors="coerce").dropna()
        rows.append(
            {
                "feature": column,
                "mean": float(values.mean()),
                "standard_deviation": float(values.std()),
                "q05": float(values.quantile(0.05)),
                "median": float(values.median()),
                "q95": float(values.quantile(0.95)),
                "n": len(values),
                "sample_start": pd.to_datetime(state.loc[values.index, "date"])
                .min()
                .date()
                .isoformat(),
                "sample_end": pd.to_datetime(state.loc[values.index, "date"])
                .max()
                .date()
                .isoformat(),
            }
        )
    return pd.DataFrame(rows)


def _event_responses(events: pd.DataFrame, daily: pd.DataFrame) -> pd.DataFrame:
    rows = []
    registered = pd.DatetimeIndex(events["date"])
    for event in events.itertuples(index=False):
        for asset in ["BTC", "ETH"]:
            series = pd.to_numeric(daily[f"{asset.lower()}_ret"], errors="coerce").dropna()
            date = pd.Timestamp(event.date)
            position = series.index.searchsorted(date)
            for window in [1, 5, 10]:
                actual = series.iloc[position + 1 : position + 1 + window]
                placebo = _placebo_windows(series, registered, window)
                estimate = float(actual.sum()) if len(actual) == window else np.nan
                percentile = (
                    float((placebo <= estimate).mean())
                    if len(placebo) and np.isfinite(estimate)
                    else np.nan
                )
                pvalue = 2 * min(percentile, 1 - percentile) if np.isfinite(percentile) else np.nan
                rows.append(
                    {
                        "event_id": event.event_id,
                        "event_date": date.date().isoformat(),
                        "category": event.category,
                        "asset": asset,
                        "window_days": window,
                        "post_event_log_return": estimate,
                        "placebo_percentile": percentile,
                        "two_sided_placebo_pvalue": pvalue,
                        "placebo_windows": len(placebo),
                        "sample_start": series.index.min().date().isoformat(),
                        "sample_end": series.index.max().date().isoformat(),
                        "timing": f"+1 through +{window}, event day excluded",
                    }
                )
    return pd.DataFrame(rows)


def _placebo_windows(series: pd.Series, event_dates: pd.DatetimeIndex, window: int) -> np.ndarray:
    event_positions = [series.index.searchsorted(date) for date in event_dates]
    values = []
    for start in range(0, len(series) - window, window):
        if any(abs(start - event_position) <= window for event_position in event_positions):
            continue
        chunk = series.iloc[start + 1 : start + 1 + window]
        if len(chunk) == window:
            values.append(float(chunk.sum()))
    return np.asarray(values)


def _claim_ledger(root: Path) -> pd.DataFrame:
    rows = []
    for module_id in EVIDENCE_BUILDERS:
        if module_id == "09_event_stress_cross_module_synthesis":
            continue
        path = root / "research" / module_id / "tables" / "claims.csv"
        if path.exists():
            frame = pd.read_csv(path)
            rows.extend(frame.to_dict("records"))
    return pd.DataFrame(rows)


def _robustness_summary(ledger: pd.DataFrame) -> pd.DataFrame:
    if ledger.empty:
        return pd.DataFrame(columns=["module_id", "claims", "evidence_grades", "status"])
    return (
        ledger.groupby("module_id", as_index=False)
        .agg(
            claims=("claim_id", "count"),
            evidence_grades=("evidence_grade", lambda values: "|".join(sorted(set(values)))),
            status=("status", lambda values: "|".join(sorted(set(values)))),
        )
        .sort_values("module_id")
    )


def _figure_dependence(factors: pd.DataFrame, tails: pd.DataFrame, path: Path) -> Path:
    apply_theme()
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    plot = factors.sort_values("common_variance_share")
    axes[0].barh(plot["asset"], plot["common_variance_share"], color=PALETTE["eth"])
    axes[0].set_xlim(0, 1)
    axes[0].set_xlabel("Leave-one-out common variance share")
    axes[0].set_title("A. Common variation excludes the target asset")
    style_axis(axes[0], x_grid=True, y_grid=False)
    tail = tails[
        tails["quantile"].eq(0.05)
        & tails["primary_specification"].astype(bool)
        & ((tails["asset_i"].eq("BTC")) | (tails["asset_j"].eq("BTC")))
    ].copy()
    tail["peer"] = np.where(tail["asset_i"].eq("BTC"), tail["asset_j"], tail["asset_i"])
    tail = tail.sort_values("excess_probability")
    xerr = np.vstack(
        [
            tail["excess_probability"] - tail["excess_ci_low"],
            tail["excess_ci_high"] - tail["excess_probability"],
        ]
    )
    axes[1].errorbar(
        tail["excess_probability"],
        tail["peer"],
        xerr=xerr,
        fmt="o",
        color=PALETTE["btc_dark"],
        ecolor=PALETTE["slate"],
        capsize=3,
    )
    axes[1].axvline(0, color=TOKENS["muted"], linewidth=1)
    axes[1].set_xlabel("Excess joint probability above q-squared")
    axes[1].set_title("B. BTC lower-tail co-exceedance, q=5%")
    style_axis(axes[1], x_grid=True, y_grid=False)
    add_figure_header(
        fig,
        "Common crypto variation and lower-tail dependence",
        "S2 fixed stable core, 2021-01-02 to 2026-06-30; bars are descriptive, intervals use 2,000 moving-block replications.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.87), w_pad=3)
    source = pd.concat(
        [
            plot.assign(plot_key="factor__" + plot["asset"], panel="common_factor"),
            tail.assign(plot_key="tail__BTC__" + tail["peer"], panel="tail_dependence"),
        ],
        ignore_index=True,
        sort=False,
    )
    return _save_figure(
        fig,
        path,
        source,
        "common_factor_tail_dependence",
        "tables/common_factor_results.csv; tables/tail_dependence.csv",
    )


def _figure_tradfi(rolling: pd.DataFrame, breaks: pd.DataFrame, path: Path) -> Path:
    apply_theme()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
    plot = rolling[rolling["feature_id"].eq("qqq_ret")].copy()
    plot["date"] = pd.to_datetime(plot["date"])
    for asset, color in [("BTC", PALETTE["btc"]), ("ETH", PALETTE["eth"])]:
        values = plot[plot["asset"].eq(asset)]
        axes[0].plot(values["date"], values["beta"], label=asset, color=color, linewidth=1.8)
    axes[0].axvline(pd.Timestamp("2024-01-11"), color=TOKENS["muted"], linestyle="--", linewidth=1)
    axes[0].axhline(0, color=TOKENS["axis"], linewidth=1)
    axes[0].set_ylabel("Conditional QQQ beta")
    axes[0].set_title("A. 252-session conditional exposure")
    axes[0].legend(loc="upper left")
    style_axis(axes[0])
    forest = breaks[breaks["feature_id"].eq("qqq_ret")].copy()
    y = np.arange(len(forest))
    axes[1].errorbar(
        forest["era_beta_change"],
        y,
        xerr=1.96 * forest["era_beta_change_se_hac"],
        fmt="o",
        color=PALETTE["risk_dark"],
        ecolor=PALETTE["slate"],
        capsize=4,
    )
    axes[1].axvline(0, color=TOKENS["muted"], linewidth=1)
    axes[1].set_yticks(y, forest["asset"])
    axes[1].set_xlabel("ETF-era QQQ beta change (95% HAC interval)")
    axes[1].set_title("B. Predeclared era interaction")
    style_axis(axes[1], x_grid=True, y_grid=False)
    add_figure_header(
        fig,
        "Dynamic TradFi integration",
        "Crypto returns are joined to native-session TradFi returns after calculation; contemporaneous association only.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.86), w_pad=3)
    source = pd.concat(
        [
            plot.assign(
                plot_key="rolling__" + plot["asset"] + "__" + plot["date"].dt.strftime("%Y-%m-%d"),
                panel="rolling",
            ),
            forest.assign(plot_key="break__" + forest["asset"], panel="break"),
        ],
        ignore_index=True,
        sort=False,
    )
    return _save_figure(
        fig,
        path,
        source,
        "dynamic_tradfi_integration",
        "tables/dynamic_tradfi_exposures.csv; tables/break_tests.csv",
    )


def _figure_leverage(curve: pd.DataFrame, connectedness: pd.DataFrame, path: Path) -> Path:
    apply_theme()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
    axes[0].plot(
        curve["leverage"],
        curve["predicted_tail_probability"],
        color=PALETTE["stress_dark"],
        linewidth=2,
    )
    axes[0].fill_between(
        curve["leverage"], curve["ci_low"], curve["ci_high"], color=PALETTE["stress"], alpha=0.2
    )
    axes[0].set_xlabel("Lagged leverage percentile")
    axes[0].set_ylabel("Conditional lower-tail probability")
    axes[0].set_title("A. Fitted association on observed support")
    style_axis(axes[0])
    primary = connectedness[connectedness["specification"].eq("primary")].copy()
    primary["date"] = pd.to_datetime(primary["date"])
    axes[1].plot(
        primary["date"], primary["connectedness_pct"], color=PALETTE["eth_dark"], linewidth=1.8
    )
    axes[1].set_ylabel("Generalized-FEVD connectedness (%)")
    axes[1].set_title("B. Stable-core absolute-return connectedness")
    style_axis(axes[1])
    add_figure_header(
        fig,
        "Leverage states, tail stress, and connectedness",
        "Lagged-state spline with HAC band; rolling generalized FEVD uses 252 observations and a 10-step horizon.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.86), w_pad=3)
    axes[0].xaxis.set_label_coords(0.5, -0.09)
    source = pd.concat(
        [
            curve.assign(
                plot_key="curve__" + curve["leverage"].round(6).astype(str), panel="tail_curve"
            ),
            primary.assign(
                plot_key="connectedness__" + primary["date"].dt.strftime("%Y-%m-%d"),
                panel="connectedness",
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    return _save_figure(
        fig,
        path,
        source,
        "leverage_tail_connectedness",
        "tables/leverage_tail_model.csv; tables/connectedness.csv",
    )


def _figure_institutional(coefficients: pd.DataFrame, eras: pd.DataFrame, path: Path) -> Path:
    apply_theme()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
    plot = coefficients[coefficients["response"].eq("return")].copy()
    for asset, color, offset in [("BTC", PALETTE["btc"], -0.08), ("ETH", PALETTE["eth"], 0.08)]:
        values = plot[plot["asset"].eq(asset)]
        x = values["lag_sessions"] + offset
        yerr = np.vstack(
            [
                values["coefficient_per_flow_bps"] - values["simultaneous_ci_low"],
                values["simultaneous_ci_high"] - values["coefficient_per_flow_bps"],
            ]
        )
        axes[0].errorbar(
            x,
            values["coefficient_per_flow_bps"],
            yerr=yerr,
            fmt="o",
            label=asset,
            color=color,
            capsize=3,
        )
    axes[0].axhline(0, color=TOKENS["muted"], linewidth=1)
    axes[0].set_xlabel("Flow lag (reporting sessions)")
    axes[0].set_ylabel("Return coefficient per flow-intensity bp")
    axes[0].set_title("A. ETF distributed lags, simultaneous bands")
    axes[0].legend(loc="best")
    style_axis(axes[0])
    era_plot = eras[eras["category"].eq("leveraged_money")].copy()
    era_labels = era_plot["era"].map(
        {
            "pre_us_spot_etf": "Pre-U.S. spot ETF",
            "us_spot_etf_era": "U.S. spot ETF era",
        }
    )
    era_plot["label"] = era_plot["asset"] + " | " + era_labels.fillna(era_plot["era"])
    colors = [PALETTE["btc"] if asset == "BTC" else PALETTE["eth"] for asset in era_plot["asset"]]
    axes[1].barh(era_plot["label"], era_plot["mean_net_share_oi"], color=colors)
    axes[1].axvline(0, color=TOKENS["muted"], linewidth=1)
    axes[1].set_xlabel("Mean leveraged-money net share of OI")
    axes[1].set_title("B. CFTC standard-contract positioning eras")
    style_axis(axes[1], x_grid=True, y_grid=False)
    add_figure_header(
        fig,
        "ETF flows and regulated-futures positioning",
        "ETF timing remains unresolved; CFTC Tuesday positions use a Friday availability proxy and are separate descriptive context.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.85), w_pad=3)
    source = pd.concat(
        [
            plot.assign(
                plot_key="etf__" + plot["asset"] + "__lag" + plot["lag_sessions"].astype(str),
                panel="etf_lags",
            ),
            era_plot.assign(
                plot_key="cftc__" + era_plot["asset"] + "__" + era_plot["era"], panel="cftc_eras"
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    return _save_figure(
        fig,
        path,
        source,
        "institutional_market_plumbing",
        "tables/etf_distributed_lags.csv; tables/institutional_positioning_eras.csv",
    )


def _figure_liquidity(state: pd.DataFrame, mechanics: pd.DataFrame, path: Path) -> Path:
    apply_theme()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
    plot = state.copy()
    plot["date"] = pd.to_datetime(plot["date"])
    axes[0].plot(
        plot["date"],
        plot["price_adjusted_tvl_residual_z365"],
        color=PALETTE["stable_dark"],
        linewidth=1.3,
    )
    axes[0].axhline(0, color=TOKENS["muted"], linewidth=1)
    axes[0].set_ylabel("Rolling 365-day residual z-score")
    axes[0].set_title("A. Price-adjusted USD TVL residual state")
    style_axis(axes[0])
    mech = mechanics[mechanics["metric"].str.startswith("correlation")].copy()
    labels = {
        "correlation__btc_ret__d_log_mvrv": "BTC return vs. MVRV log change",
        "correlation__d_log_mvrv__d_log_market_cap": ("MVRV log change vs. market-cap log change"),
        "correlation__d_log_mvrv__d_log_realized_cap": (
            "MVRV log change vs. realized-cap log change"
        ),
        "correlation__btc_ret__identity_residual": "BTC return vs. MVRV identity residual",
    }
    mech["label"] = mech["metric"].map(labels)
    axes[1].barh(
        mech["label"],
        mech["value"],
        color=[PALETTE["btc"], PALETTE["eth"], PALETTE["slate"], PALETTE["risk"]][: len(mech)],
    )
    axes[1].axvline(0, color=TOKENS["muted"], linewidth=1)
    axes[1].set_xlim(-1.05, 1.05)
    axes[1].set_xlabel("Same-day correlation")
    axes[1].set_title("B. MVRV identity mechanics warning")
    style_axis(axes[1], x_grid=True, y_grid=False)
    add_figure_header(
        fig,
        "Liquidity-state and measurement diagnostics",
        "The residual is endogenous; same-day MVRV is mechanically price-linked and excluded from primary BTC/ETH models.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.85), w_pad=3)
    source = pd.concat(
        [
            plot.assign(
                plot_key="liquidity__" + plot["date"].dt.strftime("%Y-%m-%d"),
                panel="liquidity_state",
            ),
            mech.assign(plot_key="mechanics__" + mech["metric"], panel="measurement"),
        ],
        ignore_index=True,
        sort=False,
    )
    return _save_figure(
        fig,
        path,
        source,
        "liquidity_measurement_diagnostics",
        "tables/liquidity_state.csv; tables/measurement_mechanics.csv",
    )


def _figure_market_structure(
    concentration: pd.DataFrame, transitions: pd.DataFrame, path: Path
) -> Path:
    apply_theme()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
    left = concentration.copy()
    left["snapshot_date"] = pd.to_datetime(left["snapshot_date"])
    axes[0].plot(
        left["snapshot_date"], left["effective_asset_count"], color=PALETTE["eth_dark"], linewidth=2
    )
    axes[0].set_ylabel("Entropy-implied effective asset count")
    axes[0].set_title("A. Concentration through effective breadth")
    style_axis(axes[0])
    right = transitions.copy()
    right["snapshot_date"] = pd.to_datetime(right["snapshot_date"])
    axes[1].plot(
        right["snapshot_date"], right["turnover_rate"], color=PALETTE["btc_dark"], linewidth=1.6
    )
    axes[1].set_ylabel("One-month membership turnover")
    axes[1].set_title("B. Top-100 entries and exits")
    style_axis(axes[1])
    add_figure_header(
        fig,
        "Point-in-time market concentration and turnover",
        "Complete monthly top-100 snapshots, January 2020-May 2026; no daily constituent-performance inference.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.86), w_pad=3)
    source = pd.concat(
        [
            left.assign(
                plot_key="breadth__" + left["snapshot_date"].dt.strftime("%Y-%m-%d"),
                panel="breadth",
            ),
            right.assign(
                plot_key="turnover__" + right["snapshot_date"].dt.strftime("%Y-%m-%d"),
                panel="turnover",
            ),
        ],
        ignore_index=True,
        sort=False,
    )
    return _save_figure(
        fig,
        path,
        source,
        "pit_concentration_turnover",
        "tables/pit_concentration.csv; tables/pit_membership_transitions.csv",
    )


def _figure_events(responses: pd.DataFrame, path: Path) -> Path:
    apply_theme()
    fig, ax = plt.subplots(figsize=(12, 6.4))
    plot = responses[responses["window_days"].eq(10)].copy()
    matrix = plot.pivot(index="event_id", columns="asset", values="post_event_log_return")
    image = ax.imshow(matrix.to_numpy(), cmap="RdBu_r", aspect="auto", vmin=-0.35, vmax=0.35)
    ax.set_xticks(np.arange(len(matrix.columns)), matrix.columns)
    event_labels = {
        "bitcoin_halving_2024": "Bitcoin halving (2024)",
        "btc_spot_etf_launch": "BTC spot ETF launch",
        "dencun_upgrade": "Dencun upgrade",
        "eth_spot_etf_launch": "ETH spot ETF launch",
        "ftx_collapse_2022": "FTX collapse (2022)",
        "luna_collapse_2022": "LUNA collapse (2022)",
        "svb_crisis_2023": "SVB crisis (2023)",
        "yen_carry_unwind_2024": "Yen carry unwind (2024)",
    }
    ax.set_yticks(
        np.arange(len(matrix.index)),
        [event_labels.get(label, label.replace("_", " ").title()) for label in matrix.index],
    )
    ax.set_title("Registered +1 through +10 cumulative log returns")
    fig.colorbar(image, ax=ax, label="Cumulative log return", fraction=0.035, pad=0.03)
    style_axis(ax, y_grid=False, x_grid=False)
    add_figure_header(
        fig,
        "Event atlas appendix",
        "Event day excluded; cells are descriptive and do not identify event effects.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.88))
    source = plot.assign(
        plot_key="event__" + plot["event_id"] + "__" + plot["asset"], panel="event_atlas"
    )
    return _save_figure(
        fig, path, source, "event_atlas_appendix", "tables/event_response_matrix.csv"
    )


def _save_figure(
    fig: plt.Figure,
    path: Path,
    source: pd.DataFrame,
    figure_id: str,
    source_tables: str,
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if source["plot_key"].duplicated().any():
        duplicate = source.loc[source["plot_key"].duplicated(), "plot_key"].iloc[0]
        raise ValueError(f"duplicate plot key: {duplicate}")
    svg = path.with_suffix(".svg")
    png_temporary = path.with_suffix(".png.tmp")
    svg_temporary = path.with_suffix(".svg.tmp")
    try:
        fig.savefig(
            png_temporary,
            format="png",
            dpi=220,
            bbox_inches="tight",
            facecolor=TOKENS["background"],
        )
        fig.savefig(
            svg_temporary,
            format="svg",
            bbox_inches="tight",
            facecolor=TOKENS["background"],
            metadata={"Date": None},
        )
        with suppress(OSError):
            svg_temporary.write_text(
                "\n".join(
                    line.rstrip() for line in svg_temporary.read_text(encoding="utf-8").splitlines()
                )
                + "\n",
                encoding="utf-8",
                newline="\n",
            )
        png_temporary.replace(path)
        svg_temporary.replace(svg)
    finally:
        png_temporary.unlink(missing_ok=True)
        svg_temporary.unlink(missing_ok=True)
        plt.close(fig)
    source_path = path.with_suffix(".source.csv")
    metadata_path = path.with_suffix(".metadata.json")
    write_csv(source_path, source)
    write_json(
        metadata_path,
        {
            "figure_id": figure_id,
            "png": path.name,
            "svg": svg.name,
            "source_csv": source_path.name,
            "source_tables": source_tables,
            "plot_key": "plot_key",
            "rows": len(source),
        },
    )
    return path


def _result(
    finding: str,
    estimate: str,
    interval: str,
    sample: str,
    interpretation: str,
    sensitivity: str,
) -> dict[str, str]:
    return {
        "finding": finding,
        "estimate": estimate,
        "interval": interval,
        "N/sample": sample,
        "interpretation": interpretation,
        "sensitivity": sensitivity,
    }


def _claim(
    claim_id: str,
    module_id: str,
    claim_text: str,
    source_table: str,
    source_figure: str,
    sample: str,
    method: str,
    limitation: str,
) -> dict[str, str]:
    return {
        "claim_id": claim_id,
        "module_id": module_id,
        "claim_text": claim_text,
        "sample": sample,
        "method": method,
        "uncertainty": "Intervals, diagnostics, and sensitivity specifications are reported in the linked source tables.",
        "evidence_grade": "B",
        "source_table": source_table,
        "source_figure": source_figure,
        "limitation": limitation,
        "status": "accepted_qualified",
    }


EVIDENCE_BUILDERS = {
    "01_cross_asset_dependence_regimes": build_dependence,
    "02_macro_tradfi_integration": build_tradfi,
    "03_derivatives_leverage_liquidations": build_leverage,
    "04_etf_institutional_flows": build_institutional,
    "05_stablecoin_defi_liquidity": build_liquidity,
    "07_chain_fundamentals_sector_dynamics": build_market_structure,
    "09_event_stress_cross_module_synthesis": build_synthesis,
}


__all__ = ["EVIDENCE_BUILDERS", "EvidenceBuild", "build_evidence_figures"]
