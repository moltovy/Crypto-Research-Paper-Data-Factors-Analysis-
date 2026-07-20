# 04_etf_institutional_flows: ETF and Institutional Flows

## Overview

This module replaces the old cumulative-flow root figure with ETF lag-response, source-timing, and flow-shock/placebo diagnostics.

## Questions Investigated

- How do BTC and ETH ETF flow-intensity associations vary over lags 0-5?
- Do plotted ETF series begin only at valid source observations?

## Data, Assets, and Sample

| artifact                                    |   rows | sample                                  | coverage rule                                    |
|:--------------------------------------------|-------:|:----------------------------------------|:-------------------------------------------------|
| tables/corporate_exposure_eras.csv          |      1 | result rows=1                           | module-specific matched sample                   |
| tables/etf_cumulative_lags.csv              |      4 | 2024-01-22 to 2026-04-10, n=426-557     | ETF source rows only; no pre-inception zero fill |
| tables/etf_distributed_lags.csv             |     24 | 2024-01-22 to 2026-04-10, n=426-557     | ETF source rows only; no pre-inception zero fill |
| tables/etf_flow_concentration.csv           |      2 | 2024-01-11 to 2026-04-10, result rows=2 | ETF source rows only; no pre-inception zero fill |
| tables/etf_nonlinear_sensitivity.csv        |      6 | 2024-01-12 to 2026-04-10, n=431-562     | ETF source rows only; no pre-inception zero fill |
| tables/etf_timing_sensitivity.csv           |      4 | 2024-01-12 to 2026-04-10, n=430-562     | ETF source rows only; no pre-inception zero fill |
| tables/institutional_positioning.csv        |      6 | 2020-01-14 to 2026-04-14, n=262-327     | module-specific matched sample                   |
| tables/institutional_positioning_eras.csv   |     12 | 2018-04-10 to 2026-06-30, n=102-301     | module-specific matched sample                   |
| tables/institutional_positioning_points.csv |    704 | result rows=704                         | module-specific matched sample                   |

## Methodologies and Calculations

| method                 | calculation                                                              |
|:-----------------------|:-------------------------------------------------------------------------|
| Lag response           | ETF net flows are scaled by lagged market cap and shifted over lags 0-5. |
| Moving-block bootstrap | deterministic block resampling produces correlation intervals.           |
| Timing audit           | first plotted dates must equal or follow first valid source dates.       |

## Formulas

$f_t=\text{ETF net flow}_t/\text{market cap}_{t-1}$.

$\rho_l=\operatorname{corr}(r_t, f_{t-l})$ for lags $l=0,\dots,5$.

## Summary of Results

| finding                     | estimate                                                                                                                                   | interval                                                    | N/sample                            | interpretation                                                            | sensitivity                                                                             |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|:------------------------------------|:--------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| ETF return lag coefficients | Across 12 asset-lag return coefficients, 2 have 95% moving-block simultaneous intervals excluding zero under the reported-date convention. | 2,000-replication moving-block max-t simultaneous intervals | 2024-01-22 to 2026-04-10, n=426-557 | Weak coefficients remain weak rather than being rescued by lag selection. | reported-date and one-session-shift timing conventions; returns and realized volatility |

## Analytical Results and Visualizations

![04 Institutional Market Plumbing](figures/04_institutional_market_plumbing.png)

ETF lag coefficients use simultaneous bands and no pre-inception or holiday zero fill. CFTC panels use standard contracts only and report period averages as context.

## Robustness and Sensitivity

Sensitivity dimensions are: lags 0-5, BTC/ETH separate starts, block-bootstrap interval, shock threshold. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

ETF flows are market-plumbing associations with timing and simultaneity concerns, not causal return estimates.

## Limitations

Issuer flow timing, non-reporting days, holidays, and launch-date differences require asset-specific samples.

## Reproduce This Module

```bash
uv run python scripts/run_research.py --module 04_etf_institutional_flows
uv run python scripts/build_research_figures.py --module 04_etf_institutional_flows
uv run python scripts/check_research_surface.py --module 04_etf_institutional_flows
```

## Files and Code

- [`claims.csv`](tables/claims.csv)
- [`corporate_exposure_eras.csv`](tables/corporate_exposure_eras.csv)
- [`etf_cumulative_lags.csv`](tables/etf_cumulative_lags.csv)
- [`etf_distributed_lags.csv`](tables/etf_distributed_lags.csv)
- [`etf_flow_concentration.csv`](tables/etf_flow_concentration.csv)
- [`etf_nonlinear_sensitivity.csv`](tables/etf_nonlinear_sensitivity.csv)
- [`etf_timing_sensitivity.csv`](tables/etf_timing_sensitivity.csv)
- [`institutional_positioning.csv`](tables/institutional_positioning.csv)
- [`institutional_positioning_eras.csv`](tables/institutional_positioning_eras.csv)
- [`institutional_positioning_points.csv`](tables/institutional_positioning_points.csv)

- [Methodology](methodology.md)
- [Findings](findings.md)
- [Interpretation](interpretation.md)
- [Limitations](limitations.md)
- Code: `src/cqresearch/research/analytical_modules.py`
