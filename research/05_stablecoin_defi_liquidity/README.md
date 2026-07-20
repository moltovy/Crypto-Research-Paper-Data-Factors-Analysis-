# 05_stablecoin_defi_liquidity: Stablecoin and DeFi Liquidity State

## Overview

This module treats stablecoin supply, DeFi TVL, and related balances as endogenous liquidity-state proxies with explicit valuation-contamination checks.

## Questions Investigated

- Which stablecoin/DeFi state variables have usable weekly coverage?
- How much raw USD TVL behavior is plausibly valuation-sensitive?

## Data, Assets, and Sample

| artifact                                |   rows | sample                                     | coverage rule                  |
|:----------------------------------------|-------:|:-------------------------------------------|:-------------------------------|
| tables/liquidity_state.csv              |   2295 | 2020-01-02 to 2026-04-14, result rows=2295 | module-specific matched sample |
| tables/liquidity_state_coefficients.csv |      4 | 2020-01-02 to 2026-04-14, n=2295           | module-specific matched sample |
| tables/liquidity_state_summary.csv      |      3 | 2020-01-02 to 2026-04-14, n=2116-2295      | module-specific matched sample |
| tables/measurement_mechanics.csv        |      5 | 2020-01-02 to 2026-04-13, n=2291-2294      | module-specific matched sample |

## Methodologies and Calculations

| method                  | calculation                                                           |
|:------------------------|:----------------------------------------------------------------------|
| Weekly state analysis   | Sunday-ended weekly growth and lagged state variables are summarized. |
| Valuation contamination | raw USD TVL growth is screened against BTC/ETH returns.               |

## Formulas

$\Delta \log X_t = \log X_t - \log X_{t-1}$.

$\operatorname{corr}(r_t, \Delta \log TVL_t)$ is a price-content screen, not a liquidity shock.

## Summary of Results

| finding                      | estimate                                       | interval                        | N/sample                              | interpretation                                                               | sensitivity                                                     |
|:-----------------------------|:-----------------------------------------------|:--------------------------------|:--------------------------------------|:-----------------------------------------------------------------------------|:----------------------------------------------------------------|
| Price-adjusted USD TVL state | market-return controls explain R-squared=0.004 | HAC coefficient intervals       | 2020-01-02 to 2026-04-14, n=2295      | The residual is an endogenous state proxy, not an exogenous liquidity shock. | BTC, ETH, and TOTAL3 controls; rolling residual standardization |
| MVRV measurement mechanics   | corr(BTC return, change in log MVRV)=0.997     | descriptive identity diagnostic | 2020-01-02 to 2026-04-13, n=2291-2294 | Same-day MVRV remains excluded from primary BTC/ETH models.                  | market-cap/realized-cap identity residual                       |

## Analytical Results and Visualizations

![05 Liquidity Measurement Diagnostics](figures/05_liquidity_measurement_diagnostics.png)

The liquidity residual is standardized only after contemporaneous market-return controls. The MVRV panel is a measurement warning, not factor evidence.

## Robustness and Sensitivity

Sensitivity dimensions are: raw versus lagged, TVL price content, weekly calendar, state bins. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Stablecoin/DeFi variables are balance-sheet state proxies. Weak or valuation-sensitive results are reported as weak and not forced into the root README.

## Limitations

Raw USD TVL can mechanically rise when deposited-asset prices rise. No exogenous liquidity-shock design is present.

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
- Code: `src/cqresearch/research/analytical_modules.py`
