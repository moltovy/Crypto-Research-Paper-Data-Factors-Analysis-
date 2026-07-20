# 01_cross_asset_dependence_regimes: Cross-Asset Dependence and Regimes

## Overview

This module replaces the former BTC/ETH returns-regime scaffold with a multi-asset dependence analysis spanning selected crypto majors and verified TradFi/macro return or change series.

## Questions Investigated

- How broad is common-factor crypto dependence across the selected-major universe?
- How do Pearson, Spearman, partial, lower-tail, rolling, and regime-difference dependence diagnostics compare?

## Data, Assets, and Sample

| artifact                             |   rows | sample                                   | coverage rule                                |
|:-------------------------------------|-------:|:-----------------------------------------|:---------------------------------------------|
| tables/asset_return_coverage.csv     |     14 | 2021-01-02 to 2026-06-30, result rows=14 | module-specific matched sample               |
| tables/common_factor_overview.csv    |     14 | 2021-01-02 to 2026-06-30, n=2006         | matched current-cohort selected-major window |
| tables/common_factor_results.csv     |     14 | 2021-01-02 to 2026-06-30, n=2006         | matched current-cohort selected-major window |
| tables/relative_risk_diagnostics.csv |     14 | 2021-01-02 to 2026-06-30, n=2006         | module-specific matched sample               |
| tables/tail_dependence.csv           |    546 | 2021-01-02 to 2026-06-30, n=2006         | module-specific matched sample               |

## Methodologies and Calculations

| method               | calculation                                                                                                 |
|:---------------------|:------------------------------------------------------------------------------------------------------------|
| Correlation matrices | Pearson and Spearman correlations are computed on matched daily observations with explicit coverage tables. |
| PCA/common factor    | standardized selected-major returns are decomposed with deterministic SVD.                                  |
| Tail dependence      | lower-tail co-exceedance counts joint bottom-5% days for each pair.                                         |

## Formulas

$\rho_{ij}=\operatorname{corr}(r_i,r_j)$.

$\text{PC share}_k = s_k^2 / \sum_j s_j^2$ from the standardized return matrix.

$\text{co-exceed}_{ij}=N^{-1}\sum_t 1[r_{i,t}\le q_i(0.05), r_{j,t}\le q_j(0.05)]$.

## Summary of Results

| finding                                    | estimate                           | interval                                                                    | N/sample                         | interpretation                                       | sensitivity                                                |
|:-------------------------------------------|:-----------------------------------|:----------------------------------------------------------------------------|:---------------------------------|:-----------------------------------------------------|:-----------------------------------------------------------|
| Common variation and lower-tail dependence | PC1=66.0%; median q=5% excess=2.8% | HAC factor-beta intervals and 2,000-replication moving-block tail intervals | 2021-01-02 to 2026-06-30, n=2006 | Dependence is broad but heterogeneous across assets. | Tail thresholds 1%, 2.5%, 5%, 10%; block lengths 5, 10, 20 |

## Analytical Results and Visualizations

![01 Common Factor Tail Dependence](figures/01_common_factor_tail_dependence.png)

Panel A excludes each target from its own factor. Panel B compares BTC pair co-exceedance with the q-squared independence benchmark using moving-block intervals.

## Robustness and Sensitivity

Sensitivity dimensions are: Pearson/Spearman, BTC-control partial correlations, regime split, tail threshold, rolling window. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Dependence results describe realized co-movement and common-factor structure. They do not imply investability, forecasts, or causal transmission.

## Limitations

Selected-major daily data uses a current-cohort source and is survivorship-biased. TradFi variables use available close alignment and should be interpreted as contemporaneous co-movement.

## Reproduce This Module

```bash
uv run python scripts/run_research.py --module 01_cross_asset_dependence_regimes
uv run python scripts/build_research_figures.py --module 01_cross_asset_dependence_regimes
uv run python scripts/check_research_surface.py --module 01_cross_asset_dependence_regimes
```

## Files and Code

- [`asset_return_coverage.csv`](tables/asset_return_coverage.csv)
- [`claims.csv`](tables/claims.csv)
- [`common_factor_overview.csv`](tables/common_factor_overview.csv)
- [`common_factor_results.csv`](tables/common_factor_results.csv)
- [`relative_risk_diagnostics.csv`](tables/relative_risk_diagnostics.csv)
- [`tail_dependence.csv`](tables/tail_dependence.csv)

- [Methodology](methodology.md)
- [Findings](findings.md)
- [Interpretation](interpretation.md)
- [Limitations](limitations.md)
- Code: `src/cqresearch/research/analytical_modules.py`
