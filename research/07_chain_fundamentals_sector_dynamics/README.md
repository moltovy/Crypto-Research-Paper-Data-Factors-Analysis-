# 07_chain_fundamentals_sector_dynamics: Chain Fundamentals and Sector Dynamics

## Overview

This module combines chain-fundamental coverage with point-in-time sector/market-structure state variables, without promoting raw concentration charts.

## Questions Investigated

- Which chain metrics and chains have enough coverage for descriptive panel work?
- How can PIT concentration/turnover variables be used as state variables without becoming headline raw charts?

## Data, Assets, and Sample

| artifact                                   |   rows | sample                          | coverage rule                              |
|:-------------------------------------------|-------:|:--------------------------------|:-------------------------------------------|
| tables/chain_panel.csv                     |      2 | 2021-06-30 to 2026-04-30, n=236 | module-specific matched sample             |
| tables/chain_panel_coverage.csv            |     12 | result rows=12                  | module-specific matched sample             |
| tables/pit_concentration.csv               |     77 | result rows=77                  | monthly point-in-time state variables only |
| tables/pit_concentration_decomposition.csv |     76 | result rows=76                  | monthly point-in-time state variables only |
| tables/pit_membership_transitions.csv      |     76 | result rows=76                  | monthly point-in-time state variables only |

## Methodologies and Calculations

| method                 | calculation                                                                         |
|:-----------------------|:------------------------------------------------------------------------------------|
| Coverage audit         | chain metrics are counted by chain and metric family before relationship claims.    |
| PIT state coefficients | monthly concentration and turnover are modeled as standardized state relationships. |

## Formulas

$z(x)=(x-\bar x)/\sigma_x$.

$z(y_t)=\alpha+\beta z(state_t)+u_t$ for monthly PIT state relationships.

## Summary of Results

| finding                                  | estimate                                                                                                                                    | interval                                                      | N/sample                           | interpretation                                                    | sensitivity                                                                   |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|:-----------------------------------|:------------------------------------------------------------------|:------------------------------------------------------------------------------|
| Point-in-time concentration and turnover | Across complete monthly PIT snapshots, effective asset count changed from 5.1 to 7.6, while median one-month membership turnover was 14.8%. | descriptive monthly census within available top-100 snapshots | through 2026-05-31, result rows=77 | Composition and concentration changed materially over the sample. | HHI identity decomposition; entries, exits, survival; partial-month exclusion |

## Analytical Results and Visualizations

![07 Pit Concentration Turnover](figures/07_pit_concentration_turnover.png)

Effective asset count is an entropy transformation; turnover uses entries plus exits relative to the membership union. June 2026 partial data is excluded.

## Robustness and Sensitivity

Sensitivity dimensions are: coverage threshold, chain mapping, monthly state model, partial period. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Chain and PIT outputs are coverage and state diagnostics. PIT variables support monthly state analysis, not daily constituent-performance claims.

## Limitations

Panel depth differs by metric/chain; monthly PIT snapshots have partial-month and survivorship constraints.

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
- Code: `src/cqresearch/research/analytical_modules.py`
