"""Single source of truth for maintained public analytical artifacts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PublicFigure:
    figure_id: str
    filename: str
    research_question: str
    source_tables: str
    caveat: str
    readme_section: str


PUBLIC_FIGURES: tuple[PublicFigure, ...] = (
    PublicFigure(
        "common_factor_tail_dependence",
        "research/01_cross_asset_dependence_regimes/figures/01_common_factor_tail_dependence.png",
        "How broad are common variation and lower-tail co-exceedance?",
        "research/01_cross_asset_dependence_regimes/tables/common_factor_results.csv; research/01_cross_asset_dependence_regimes/tables/tail_dependence.csv",
        "Fixed S2 membership; descriptive dependence only.",
        "selected-analytical-results",
    ),
    PublicFigure(
        "dynamic_tradfi_integration",
        "research/02_macro_tradfi_integration/figures/02_dynamic_tradfi_integration.png",
        "How do conditional TradFi exposures vary?",
        "research/02_macro_tradfi_integration/tables/dynamic_tradfi_exposures.csv; research/02_macro_tradfi_integration/tables/break_tests.csv",
        "Period comparison, not ETF-effect identification.",
        "selected-analytical-results",
    ),
    PublicFigure(
        "institutional_market_plumbing",
        "research/04_etf_institutional_flows/figures/04_institutional_market_plumbing.png",
        "How do ETF lag associations and CFTC positioning line up with markets?",
        "research/04_etf_institutional_flows/tables/etf_distributed_lags.csv; research/04_etf_institutional_flows/tables/institutional_positioning_eras.csv",
        "Timing and simultaneity prevent price-impact interpretation.",
        "selected-analytical-results",
    ),
    PublicFigure(
        "leverage_tail_connectedness",
        "research/03_derivatives_leverage_liquidations/figures/03_leverage_tail_connectedness.png",
        "How do leverage states coincide with tail stress and connectedness?",
        "research/03_derivatives_leverage_liquidations/tables/leverage_tail_model.csv; research/03_derivatives_leverage_liquidations/tables/connectedness.csv",
        "Stress-state association, not forecast or trading signal.",
        "selected-analytical-results",
    ),
    PublicFigure(
        "pit_concentration_turnover",
        "research/07_chain_fundamentals_sector_dynamics/figures/07_pit_concentration_turnover.png",
        "How did PIT effective breadth and turnover change?",
        "research/07_chain_fundamentals_sector_dynamics/tables/pit_concentration.csv; research/07_chain_fundamentals_sector_dynamics/tables/pit_membership_transitions.csv",
        "Monthly structure only; no daily constituent-performance inference.",
        "selected-analytical-results",
    ),
)

GALLERY_FIGURES: tuple[str, ...] = (
    "research/05_stablecoin_defi_liquidity/figures/05_liquidity_measurement_diagnostics.png",
    "research/09_event_stress_cross_module_synthesis/figures/09_event_atlas_appendix.png",
)

PUBLIC_TABLES: frozenset[str] = frozenset(
    {
        "research/01_cross_asset_dependence_regimes/tables/common_factor_results.csv",
        "research/01_cross_asset_dependence_regimes/tables/tail_dependence.csv",
        "research/02_macro_tradfi_integration/tables/dynamic_tradfi_exposures.csv",
        "research/03_derivatives_leverage_liquidations/tables/leverage_tail_model.csv",
        "research/04_etf_institutional_flows/tables/etf_distributed_lags.csv",
        "research/05_stablecoin_defi_liquidity/tables/liquidity_state.csv",
        "research/07_chain_fundamentals_sector_dynamics/tables/pit_concentration.csv",
        "research/09_event_stress_cross_module_synthesis/tables/evidence_ledger.csv",
    }
)


def public_figure_paths() -> list[str]:
    return [figure.filename for figure in PUBLIC_FIGURES]


def public_table_names() -> set[str]:
    return set(PUBLIC_TABLES)
