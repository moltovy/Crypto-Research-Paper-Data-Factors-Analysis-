# 05_stablecoin_defi_liquidity: Stablecoin and DeFi Liquidity State

## Overview

This module constructs an endogenous liquidity-state diagnostic after price-adjusting USD TVL growth and retains same-day MVRV only as a measurement-mechanics appendix.

## Questions Investigated

- What remains in USD TVL growth after contemporaneous crypto-market return controls?
- How mechanically does same-day MVRV inherit BTC price variation?

## Data, Assets, and Sample

| artifact                                |   result_rows | analytical_sample                                        | coverage rule                  |
|:----------------------------------------|--------------:|:---------------------------------------------------------|:-------------------------------|
| tables/liquidity_state.csv              |          2295 | 2,295 daily state observations; 2020-01-02 to 2026-04-14 | module-specific matched sample |
| tables/liquidity_state_coefficients.csv |             4 | 2020-01-02 to 2026-04-14, n=2295                         | module-specific matched sample |
| tables/liquidity_state_summary.csv      |             3 | 2020-01-02 to 2026-04-14, n=2116-2295                    | module-specific matched sample |
| tables/measurement_mechanics.csv        |             5 | 2020-01-02 to 2026-04-13, n=2291-2294                    | module-specific matched sample |

## Methodologies and Calculations

| method             | calculation                                                                                                                   |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Liquidity residual | regress daily USD TVL growth on BTC, ETH, and broad-market controls with HAC covariance, then standardize the residual state. |
| Stablecoin state   | report supply growth as an endogenous balance-sheet proxy with source-coverage guards.                                        |
| MVRV mechanics     | compare log-MVRV changes with BTC return and audit the market-cap/realized-cap identity residual.                             |

## Formulas

$\Delta\log(TVL_t)=\alpha+\beta'R_t+u_t$; the liquidity state is a rolling z-score of $u_t$.

$MVRV_t=MCap_t/RealizedCap_t$.

## Summary of Results

| finding                      | estimate                                       | interval                        | N/sample                              | interpretation                                                               | sensitivity                                                     |
|:-----------------------------|:-----------------------------------------------|:--------------------------------|:--------------------------------------|:-----------------------------------------------------------------------------|:----------------------------------------------------------------|
| Price-adjusted USD TVL state | market-return controls explain R-squared=0.004 | HAC coefficient intervals       | 2020-01-02 to 2026-04-14, n=2295      | The residual is an endogenous state proxy, not an exogenous liquidity shock. | BTC, ETH, and TOTAL3 controls; rolling residual standardization |
| MVRV measurement mechanics   | corr(BTC return, change in log MVRV)=0.997     | descriptive identity diagnostic | 2020-01-02 to 2026-04-13, n=2291-2294 | Same-day MVRV remains excluded from primary BTC/ETH models.                  | market-cap/realized-cap identity residual                       |

## Analytical Results and Visualizations

![05 Liquidity Measurement Diagnostics](figures/05_liquidity_measurement_diagnostics.png)

The liquidity residual is standardized only after contemporaneous market-return controls. The MVRV panel is a measurement warning, not factor evidence.

## Robustness and Sensitivity

Sensitivity dimensions are: market controls, HAC lag, z-score window, identity residual. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

The residual state is still endogenous and co-moves with market conditions. MVRV is a price-linked valuation diagnostic, not an independent factor.

## Limitations

Raw USD TVL is valuation-sensitive, source revisions are possible, and residualization does not create an exogenous liquidity shock.

## Reproduce This Module

```bash
uv run python scripts/run_research.py --module 05_stablecoin_defi_liquidity
uv run python scripts/build_research_figures.py --module 05_stablecoin_defi_liquidity
uv run python scripts/check_research_surface.py --module 05_stablecoin_defi_liquidity
```

## Files and Code

- [`claims.csv`](tables/claims.csv)
- [`liquidity_state.csv`](tables/liquidity_state.csv)
- [`liquidity_state_coefficients.csv`](tables/liquidity_state_coefficients.csv)
- [`liquidity_state_summary.csv`](tables/liquidity_state_summary.csv)
- [`measurement_mechanics.csv`](tables/measurement_mechanics.csv)

- [Methodology](methodology.md)
- [Findings](findings.md)
- [Interpretation](interpretation.md)
- [Limitations](limitations.md)
- [Code: `evidence_modules.py`](../../src/cqresearch/research/evidence_modules.py)
- [Code: `market_structure.py`](../../src/cqresearch/modeling/market_structure.py)
- [Test: `test_market_structure_models.py`](../../tests/unit/test_market_structure_models.py)
