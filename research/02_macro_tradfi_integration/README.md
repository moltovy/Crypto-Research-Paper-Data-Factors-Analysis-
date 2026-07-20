# 02_macro_tradfi_integration: Macro and TradFi Integration

## Overview

This module estimates BTC/ETH co-movement with equities, volatility, rates, the dollar, gold, and credit using synchronized calendars and same-support comparisons.

## Questions Investigated

- How do equity, volatility, dollar, rates, and gold blocks contribute to contemporaneous crypto exposure models?
- Are later-sample exposure differences robust to frequency, multicollinearity, FDR, and ridge sensitivity?

## Data, Assets, and Sample

| artifact                            |   rows | sample                           | coverage rule                  |
|:------------------------------------|-------:|:---------------------------------|:-------------------------------|
| tables/break_tests.csv              |     10 | 2020-01-03 to 2026-04-14, n=1577 | module-specific matched sample |
| tables/dynamic_tradfi_exposures.csv |   2660 | 2020-01-03 to 2026-04-14, n=252  | module-specific matched sample |
| tables/tradfi_diagnostics.csv       |      2 | n=1577                           | module-specific matched sample |

## Methodologies and Calculations

| method                       | calculation                                                                      |
|:-----------------------------|:---------------------------------------------------------------------------------|
| HAC OLS                      | synchronized daily and weekly panels estimate contemporaneous exposure models.   |
| Same-support block R-squared | full and reduced models use identical complete-case rows.                        |
| Stability diagnostics        | VIF, condition number, ridge paths, FDR q-values, and rolling beta are reported. |

## Formulas

$\Delta R^2_b = R^2_{full} - R^2_{reduced(-b)}$ on the same support.

$R^2_{partial}=(SSE_{reduced}-SSE_{full})/SSE_{reduced}$.

## Summary of Results

| finding                                                    | estimate                                                             | interval                                       | N/sample                         | interpretation                                                 | sensitivity                                                                |
|:-----------------------------------------------------------|:---------------------------------------------------------------------|:-----------------------------------------------|:---------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------------------------|
| Conditional QQQ exposure around the registered BTC ETF era | BTC 1.03 to 0.93 (change p=0.611); ETH 1.33 to 1.51 (change p=0.520) | HAC 95% intervals and era-interaction p-values | 2020-01-03 to 2026-04-14, n=1577 | Conditional equity co-movement changes are period comparisons. | 252-session rolling windows; multivariate controls; predeclared break date |

## Analytical Results and Visualizations

![02 Dynamic Tradfi Integration](figures/02_dynamic_tradfi_integration.png)

Rolling QQQ coefficients condition on VIX, DXY, real-yield changes, and gold; the forest reports formal predeclared era interactions.

## Robustness and Sensitivity

Sensitivity dimensions are: frequency, period split, HAC bandwidth, FDR, VIF, ridge. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Macro/TradFi integration is contemporaneous co-movement evidence, not macro causality or ETF-effect identification.

## Limitations

Business-date alignment, period splits, and rolling windows are descriptive. Same-day models cannot establish lead-lag direction.

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
- Code: `src/cqresearch/research/analytical_modules.py`
