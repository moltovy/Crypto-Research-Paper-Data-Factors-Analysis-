# 01_cross_asset_dependence_regimes: Cross-Asset Dependence and Regimes

## Overview

This module estimates broad common variation, lower-tail co-exceedance, and relative-risk diagnostics on the fixed S2 stable core. The former relative-major module is absorbed here.

## Questions Investigated

- How much of each S2 asset's matched return variation is shared with a leave-one-out crypto factor?
- How far does lower-tail co-exceedance depart from its independence benchmark across predeclared thresholds?

## Data, Assets, and Sample

| artifact                             |   result_rows | analytical_sample                                                     | coverage rule                               |
|:-------------------------------------|--------------:|:----------------------------------------------------------------------|:--------------------------------------------|
| tables/asset_return_coverage.csv     |            14 | 14 S2 assets; matched n=2006-2006 per asset; 2021-01-02 to 2026-06-30 | fixed PIT-eligible S2 matched daily support |
| tables/common_factor_overview.csv    |            14 | 2021-01-02 to 2026-06-30, n=2006                                      | fixed PIT-eligible S2 matched daily support |
| tables/common_factor_results.csv     |            14 | 2021-01-02 to 2026-06-30, n=2006                                      | fixed PIT-eligible S2 matched daily support |
| tables/relative_risk_diagnostics.csv |            14 | 2021-01-02 to 2026-06-30, n=2006                                      | module-specific matched sample              |
| tables/tail_dependence.csv           |           546 | 2021-01-02 to 2026-06-30, n=2006                                      | module-specific matched sample              |

## Methodologies and Calculations

| method                    | calculation                                                                                                                  |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| Leave-one-out PCA         | standardize matched S2 returns, exclude the target asset, estimate PC1, and report target common-variance share and loading. |
| Tail dependence           | estimate joint, conditional, and excess co-exceedance at 1%, 2.5%, 5%, and 10% thresholds.                                   |
| Moving-block inference    | use 2,000 replications, block length 10 primary, and lengths 5 and 20 as sensitivity.                                        |
| Relative-risk diagnostics | report annualized volatility, 5% expected shortfall, and BTC-tail downside beta on the same matched support.                 |

## Formulas

$f_{-i,t}=PC1(r_{-i,t})$ and $R_i^2=1-\operatorname{Var}(r_i-\hat r_i)/\operatorname{Var}(r_i)$.

$\lambda_{ij}(q)=P(r_i\le Q_i(q),r_j\le Q_j(q))-q^2$; $q\in\{0.01,0.025,0.05,0.10\}$.

$ES_i(5\%)=E[r_i\mid r_i\le Q_i(0.05)]$.

## Summary of Results

| finding                                    | estimate                                                      | interval                                                                    | N/sample                         | interpretation                                       | sensitivity                                                |
|:-------------------------------------------|:--------------------------------------------------------------|:----------------------------------------------------------------------------|:---------------------------------|:-----------------------------------------------------|:-----------------------------------------------------------|
| Common variation and lower-tail dependence | median leave-one-out R-squared=61.0%; median q=5% excess=2.8% | HAC factor-beta intervals and 2,000-replication moving-block tail intervals | 2021-01-02 to 2026-06-30, n=2006 | Dependence is broad but heterogeneous across assets. | Tail thresholds 1%, 2.5%, 5%, 10%; block lengths 5, 10, 20 |

## Analytical Results and Visualizations

![01 Common Factor Tail Dependence](figures/01_common_factor_tail_dependence.png)

Panel A excludes each target from its own factor. Panel B compares BTC pair co-exceedance with the q-squared independence benchmark using moving-block intervals.

## Robustness and Sensitivity

Sensitivity dimensions are: tail threshold, block length, factor composition. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Common-factor and tail estimates describe realized within-sample dependence. Evidence above an independence benchmark is not a forecast, diversification claim, or causal transmission estimate.

## Limitations

S2 is fixed from the 2021-01-31 PIT top 20 and requires matched Binance history. S3 is supplementary and survivorship-sensitive. Results depend on membership, threshold, and block-length choices.

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
- [Code: `evidence_modules.py`](../../src/cqresearch/research/evidence_modules.py)
- [Code: `dependence.py`](../../src/cqresearch/modeling/dependence.py)
- [Code: `samples.py`](../../src/cqresearch/research/samples.py)
- [Test: `test_dependence_models.py`](../../tests/unit/test_dependence_models.py)
