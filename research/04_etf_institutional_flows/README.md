# 04_etf_institutional_flows: ETF and Institutional Flows

## Overview

This module evaluates ETF flow-intensity lag associations and regulated-futures positioning over actual reporting lives without pre-inception or holiday zero fills.

## Questions Investigated

- Which lag-0 through lag-5 ETF flow-intensity coefficients remain supported under simultaneous uncertainty?
- How concentrated and persistent are reported flows, and how does CFTC positioning provide separate weekly context?

## Data, Assets, and Sample

| artifact                                    |   result_rows | analytical_sample                                                          | coverage rule                                    |
|:--------------------------------------------|--------------:|:---------------------------------------------------------------------------|:-------------------------------------------------|
| tables/corporate_exposure_eras.csv          |             1 | source eligibility gate failed; no analytical sample or exposure-era claim | module-specific matched sample                   |
| tables/etf_cumulative_lags.csv              |             4 | 2024-01-22 to 2026-04-10, n=426-557                                        | ETF source rows only; no pre-inception zero fill |
| tables/etf_distributed_lags.csv             |            24 | 2024-01-22 to 2026-04-10, n=426-557                                        | ETF source rows only; no pre-inception zero fill |
| tables/etf_flow_concentration.csv           |             2 | BTC/ETH actual report dates, n=431-563 by asset; 2024-01-11 to 2026-04-10  | ETF source rows only; no pre-inception zero fill |
| tables/etf_nonlinear_sensitivity.csv        |             6 | 2024-01-12 to 2026-04-10, n=431-562                                        | ETF source rows only; no pre-inception zero fill |
| tables/etf_timing_sensitivity.csv           |             4 | 2024-01-12 to 2026-04-10, n=430-562                                        | ETF source rows only; no pre-inception zero fill |
| tables/institutional_positioning.csv        |             6 | 2020-01-14 to 2026-04-14, n=262-327                                        | module-specific matched sample                   |
| tables/institutional_positioning_eras.csv   |            12 | 2018-04-10 to 2026-06-30, n=102-301                                        | module-specific matched sample                   |
| tables/institutional_positioning_points.csv |           704 | 704 weekly CFTC contract-report observations; 2018-04-10 to 2026-06-30     | module-specific matched sample                   |

## Methodologies and Calculations

| method                 | calculation                                                                                                           |
|:-----------------------|:----------------------------------------------------------------------------------------------------------------------|
| Flow scaling           | divide reported BTC/ETH net flow by lagged market capitalization on actual report dates.                              |
| Distributed lags       | estimate HAC return, absolute-return, and volatility associations for lags 0 through 5.                               |
| Simultaneous inference | use a 2,000-replication moving-block max-t bootstrap and timing-shift sensitivity.                                    |
| Institutional context  | report issuer concentration where available and standard-contract CFTC positioning without combining micro contracts. |

## Formulas

$FI_t=Flow_t/MCap_{t-1}$.

$y_t=\alpha+\sum_{k=0}^{5}\beta_k FI_{t-k}+\Gamma'Z_t+u_t$.

$HHI_t=\sum_i (Flow_{i,t}/\sum_j |Flow_{j,t}|)^2$.

## Summary of Results

| finding                     | estimate                                                                                                                                   | interval                                                    | N/sample                            | interpretation                                                            | sensitivity                                                                             |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|:------------------------------------|:--------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| ETF return lag coefficients | Across 12 asset-lag return coefficients, 2 have 95% moving-block simultaneous intervals excluding zero under the reported-date convention. | 2,000-replication moving-block max-t simultaneous intervals | 2024-01-22 to 2026-04-10, n=426-557 | Weak coefficients remain weak rather than being rescued by lag selection. | reported-date and one-session-shift timing conventions; returns and realized volatility |

## Analytical Results and Visualizations

![04 Institutional Market Plumbing](figures/04_institutional_market_plumbing.png)

ETF lag coefficients use simultaneous bands and no pre-inception or holiday zero fill. CFTC panels use standard contracts only and report period averages as context.

## Robustness and Sensitivity

Sensitivity dimensions are: lag, timing shift, flow sign, volatility state, contract scope. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Supported coefficients are timing-sensitive market-plumbing associations. Simultaneity prevents price-impact language.

## Limitations

Reported dates do not resolve intraday availability, issuer archives are incomplete, and ETF samples begin at instrument-specific inception.

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
- [Code: `evidence_modules.py`](../../src/cqresearch/research/evidence_modules.py)
- [Code: `etf_plumbing.py`](../../src/cqresearch/modeling/etf_plumbing.py)
- [Test: `test_etf_models.py`](../../tests/unit/test_etf_models.py)
- [Test: `test_etf_semantics.py`](../../tests/unit/test_etf_semantics.py)
- [Test: `test_cftc_positioning.py`](../../tests/unit/test_cftc_positioning.py)
