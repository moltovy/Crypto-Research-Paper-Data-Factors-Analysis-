# 02_macro_tradfi_integration: Macro and TradFi Integration

## Overview

This module measures time-varying conditional BTC/ETH exposure to contract-valid TradFi returns and changes after computing each instrument's return on its native calendar.

## Questions Investigated

- How do 252-session multivariate HAC crypto-equity exposures vary through time?
- Do predeclared era interactions support a discrete change after accounting for uncertainty and multiple tests?

## Data, Assets, and Sample

| artifact                            |   result_rows | analytical_sample                | coverage rule                  |
|:------------------------------------|--------------:|:---------------------------------|:-------------------------------|
| tables/break_tests.csv              |            10 | 2020-01-03 to 2026-04-14, n=1577 | module-specific matched sample |
| tables/dynamic_tradfi_exposures.csv |          2660 | 2020-01-03 to 2026-04-14, n=252  | module-specific matched sample |
| tables/tradfi_diagnostics.csv       |             2 | n=1577                           | module-specific matched sample |

## Methodologies and Calculations

| method                | calculation                                                                                                  |
|:----------------------|:-------------------------------------------------------------------------------------------------------------|
| Calendar construction | compute TradFi returns on native sessions, preserve exchange holidays as missing, then join to crypto dates. |
| Dynamic exposure      | estimate 252-session multivariate HAC models with at least 126 matched sessions.                             |
| Break evidence        | estimate formal era interactions and structural-break diagnostics on same-support samples.                   |

## Formulas

$r_{crypto,t}=\alpha+\beta'X_t+u_t$ with HAC covariance.

$r_t=\alpha+\beta X_t+\gamma D_t+\delta(X_tD_t)+u_t$; $\delta$ is the predeclared era interaction.

## Summary of Results

| finding                                                    | estimate                                                             | interval                                       | N/sample                         | interpretation                                                 | sensitivity                                                                |
|:-----------------------------------------------------------|:---------------------------------------------------------------------|:-----------------------------------------------|:---------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------------------------|
| Conditional QQQ exposure around the registered BTC ETF era | BTC 1.03 to 0.93 (change p=0.611); ETH 1.33 to 1.51 (change p=0.520) | HAC 95% intervals and era-interaction p-values | 2020-01-03 to 2026-04-14, n=1577 | Conditional equity co-movement changes are period comparisons. | 252-session rolling windows; multivariate controls; predeclared break date |

## Analytical Results and Visualizations

![02 Dynamic Tradfi Integration](figures/02_dynamic_tradfi_integration.png)

Rolling QQQ coefficients condition on VIX, DXY, real-yield changes, and gold; the forest reports formal predeclared era interactions.

## Robustness and Sensitivity

Sensitivity dimensions are: window support, era boundary, control set, HAC lag. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Conditional equity exposure varies over time, while formal period differences are reported as weak when adjusted evidence does not reject the null.

## Limitations

Close-to-close alignment is contemporaneous and cannot identify transmission. Latest-vintage macro data and finite rolling windows add timing and revision risk.

## Reproduce This Module

```bash
uv run python scripts/run_research.py --module 02_macro_tradfi_integration
uv run python scripts/build_research_figures.py --module 02_macro_tradfi_integration
uv run python scripts/check_research_surface.py --module 02_macro_tradfi_integration
```

## Files and Code

- [`break_tests.csv`](tables/break_tests.csv)
- [`claims.csv`](tables/claims.csv)
- [`dynamic_tradfi_exposures.csv`](tables/dynamic_tradfi_exposures.csv)
- [`tradfi_diagnostics.csv`](tables/tradfi_diagnostics.csv)

- [Methodology](methodology.md)
- [Findings](findings.md)
- [Interpretation](interpretation.md)
- [Limitations](limitations.md)
- [Code: `evidence_modules.py`](../../src/cqresearch/research/evidence_modules.py)
- [Code: `dependence.py`](../../src/cqresearch/modeling/dependence.py)
- [Code: `calendars.py`](../../src/cqresearch/data/calendars.py)
- [Test: `test_dependence_models.py`](../../tests/unit/test_dependence_models.py)
- [Test: `test_calendars.py`](../../tests/unit/test_calendars.py)
