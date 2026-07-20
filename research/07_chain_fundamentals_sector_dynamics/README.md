# 07_chain_fundamentals_sector_dynamics: Chain Fundamentals and Sector Dynamics

## Overview

This module measures concentration, breadth, and membership change from complete monthly point-in-time top-100 snapshots and runs the chain panel only after its support gate passes.

## Questions Investigated

- How did PIT concentration, entropy-implied breadth, turnover, entry, exit, and survival change across complete months?
- Can each concentration change be reconciled exactly to incumbent, entry, and exit components, and is the optional chain panel eligible?

## Data, Assets, and Sample

| artifact                                   |   result_rows | analytical_sample                                                             | coverage rule                              |
|:-------------------------------------------|--------------:|:------------------------------------------------------------------------------|:-------------------------------------------|
| tables/chain_panel.csv                     |             2 | 2021-06-30 to 2026-04-30, n=236                                               | module-specific matched sample             |
| tables/chain_panel_coverage.csv            |            12 | 4 chains x 3 metrics = 12 coverage records; model support is 59 common months | module-specific matched sample             |
| tables/pit_concentration.csv               |            77 | 77 complete monthly snapshots x top 100 = 7,700 asset-months                  | monthly point-in-time state variables only |
| tables/pit_concentration_decomposition.csv |            76 | 76 adjacent-month transitions derived from 77 complete top-100 snapshots      | monthly point-in-time state variables only |
| tables/pit_membership_transitions.csv      |            76 | 76 adjacent-month transitions derived from 77 complete top-100 snapshots      | monthly point-in-time state variables only |

## Methodologies and Calculations

| method                      | calculation                                                                                                                         |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| PIT census                  | compute HHI, entropy, effective asset count, top shares, turnover, entry, exit, and survival for each complete monthly snapshot.    |
| Concentration decomposition | reconcile each HHI change to incumbent-share changes, entries, exits, and a numerical residual.                                     |
| Optional chain panel        | require at least four valid chains and 36 common months before two-way fixed-effects estimation with panel-appropriate uncertainty. |

## Formulas

$HHI_t=\sum_i s_{i,t}^2$; $N_{eff,t}=\exp(-\sum_i s_{i,t}\log s_{i,t})$.

$Turnover_t=(Entries_t+Exits_t)/|U_t\cup U_{t-1}|$.

$\Delta HHI_t=Incumbent_t+Entry_t+Exit_t+Residual_t$.

## Summary of Results

| finding                                  | estimate                                                                                                                                    | interval                                                      | N/sample                                                                            | interpretation                                                    | sensitivity                                                                   |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------|:------------------------------------------------------------------------------|
| Point-in-time concentration and turnover | Across complete monthly PIT snapshots, effective asset count changed from 5.1 to 7.6, while median one-month membership turnover was 14.8%. | descriptive monthly census within available top-100 snapshots | January 2020 to May 2026; 77 complete monthly snapshots; 7,700 top-100 asset-months | Composition and concentration changed materially over the sample. | HHI identity decomposition; entries, exits, survival; partial-month exclusion |

## Analytical Results and Visualizations

![07 Pit Concentration Turnover](figures/07_pit_concentration_turnover.png)

Effective asset count is an entropy transformation; turnover uses entries plus exits relative to the membership union. June 2026 partial data is excluded.

## Robustness and Sensitivity

Sensitivity dimensions are: concentration measure, turnover component, partial-month rule, chain support. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

The monthly census supports composition, concentration, category-share, and turnover statements only.

## Limitations

PIT snapshots cannot recover daily constituent performance or historical altseason returns. June 2026 partial data is context-only and excluded from primary estimates.

## Reproduce This Module

```bash
uv run python scripts/run_research.py --module 07_chain_fundamentals_sector_dynamics
uv run python scripts/build_research_figures.py --module 07_chain_fundamentals_sector_dynamics
uv run python scripts/check_research_surface.py --module 07_chain_fundamentals_sector_dynamics
```

## Files and Code

- [`chain_panel.csv`](tables/chain_panel.csv)
- [`chain_panel_coverage.csv`](tables/chain_panel_coverage.csv)
- [`claims.csv`](tables/claims.csv)
- [`pit_concentration.csv`](tables/pit_concentration.csv)
- [`pit_concentration_decomposition.csv`](tables/pit_concentration_decomposition.csv)
- [`pit_membership_transitions.csv`](tables/pit_membership_transitions.csv)

- [Methodology](methodology.md)
- [Findings](findings.md)
- [Interpretation](interpretation.md)
- [Limitations](limitations.md)
- [Code: `evidence_modules.py`](../../src/cqresearch/research/evidence_modules.py)
- [Code: `market_structure.py`](../../src/cqresearch/modeling/market_structure.py)
- [Test: `test_market_structure_models.py`](../../tests/unit/test_market_structure_models.py)
