# Research Surface

This directory is the canonical public research surface for Crypto Market Dynamics. It contains generated modules, tables, figures, manifests, and the root figure-selection audit.

## Module Map

| Module | Title | Tables | Figures |
|---|---|---:|---:|
| [00](00_data_measurement_foundation/README.md) | Data and Measurement Foundation | 11 | 2 |
| [01](01_cross_asset_dependence_regimes/README.md) | Cross-Asset Dependence and Regimes | 6 | 1 |
| [02](02_macro_tradfi_integration/README.md) | Macro and TradFi Integration | 4 | 1 |
| [03](03_derivatives_leverage_liquidations/README.md) | Derivatives, Leverage, and Liquidations | 9 | 1 |
| [04](04_etf_institutional_flows/README.md) | ETF and Institutional Flows | 10 | 1 |
| [05](05_stablecoin_defi_liquidity/README.md) | Stablecoin and DeFi Liquidity State | 5 | 1 |
| [07](07_chain_fundamentals_sector_dynamics/README.md) | Chain Fundamentals and Sector Dynamics | 6 | 1 |
| [09](09_event_stress_cross_module_synthesis/README.md) | Event Stress and Cross-Module Synthesis | 5 | 1 |

## Root Figure Set

![Common variation is broad, and BTC lower-tail co-exceedance is above its independence benchmark for the shown pairs.](01_cross_asset_dependence_regimes/figures/01_common_factor_tail_dependence.png)

Source: `research/01_cross_asset_dependence_regimes/tables/common_factor_results.csv; research/01_cross_asset_dependence_regimes/tables/tail_dependence.csv`. Boundary: Fixed PIT-eligible membership supports within-sample dependence statements, not forecasts, causal transmission, or investability claims.

![Conditional QQQ exposure varies over time, while formal ETF-era interaction estimates are weak.](02_macro_tradfi_integration/figures/02_dynamic_tradfi_integration.png)

Source: `research/02_macro_tradfi_integration/tables/dynamic_tradfi_exposures.csv; research/02_macro_tradfi_integration/tables/break_tests.csv`. Boundary: Contemporaneous period comparisons do not identify ETF effects or causal transmission.

![ETF lag evidence is mostly weak under simultaneous bands; CFTC positioning provides separate weekly context.](04_etf_institutional_flows/figures/04_institutional_market_plumbing.png)

Source: `research/04_etf_institutional_flows/tables/etf_distributed_lags.csv; research/04_etf_institutional_flows/tables/institutional_positioning_eras.csv`. Boundary: Reporting-time uncertainty and simultaneity prevent a price-impact interpretation.

![Tail probabilities vary nonlinearly over observed leverage support, while stable-core connectedness changes through time.](03_derivatives_leverage_liquidations/figures/03_leverage_tail_connectedness.png)

Source: `research/03_derivatives_leverage_liquidations/tables/leverage_tail_model.csv; research/03_derivatives_leverage_liquidations/tables/connectedness.csv`. Boundary: These are stress-state associations, not forecasts, trading signals, or liquidation-cause estimates.

![Effective market breadth and constituent turnover changed materially across complete monthly snapshots.](07_chain_fundamentals_sector_dynamics/figures/07_pit_concentration_turnover.png)

Source: `research/07_chain_fundamentals_sector_dynamics/tables/pit_concentration.csv; research/07_chain_fundamentals_sector_dynamics/tables/pit_membership_transitions.csv`. Boundary: Monthly PIT evidence supports market-structure statements only, not daily historical constituent performance.

## Data-Usage Status Counts

- diagnostic only: 68
- excluded for ambiguous definition or unit: 129
- excluded for insufficient coverage: 2
- primary analysis: 25
- robustness or sensitivity: 2

## Provenance

- Root manifest: [`manifest.json`](manifest.json)
- Figure specifications: [`figure_specs.csv`](figure_specs.csv)
- Root figure selection: [`root_figure_selection.csv`](root_figure_selection.csv)
- Cross-module evidence ledger: [`09_event_stress_cross_module_synthesis/tables/evidence_ledger.csv`](09_event_stress_cross_module_synthesis/tables/evidence_ledger.csv)

## Rebuild

```bash
uv run python scripts/run_research.py --module all
uv run python scripts/build_research_figures.py --module all
uv run python scripts/check_research_surface.py --module all
```
