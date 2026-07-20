# 03_derivatives_leverage_liquidations: Derivatives, Leverage, and Liquidations

## Overview

This module studies lagged leverage, funding, open-interest scaling, and liquidation stress as state diagnostics for volatility and tail outcomes.

## Questions Investigated

- Where do lagged leverage states coincide with volatility and bottom-tail outcomes?
- How do liquidation event windows compare with stress-state summaries?

## Data, Assets, and Sample

| artifact                                     |   rows | sample                               | coverage rule                  |
|:---------------------------------------------|-------:|:-------------------------------------|:-------------------------------|
| tables/connectedness.csv                     |    502 | 2021-06-30 to 2026-06-27, n=180-365  | module-specific matched sample |
| tables/expected_shortfall.csv                |      5 | 2020-02-01 to 2026-04-12, n=452-453  | module-specific matched sample |
| tables/leverage_tail_diagnostics.csv         |      1 | 2020-02-01 to 2026-04-12, n=2263     | module-specific matched sample |
| tables/leverage_tail_horizon_sensitivity.csv |      5 | 2020-02-01 to 2026-04-05, n=90-91    | module-specific matched sample |
| tables/leverage_tail_model.csv               |     19 | 2020-02-01 to 2026-04-12, n=2263     | module-specific matched sample |
| tables/quantile_es.csv                       |      9 | 2020-02-01 to 2026-04-12, n=452-2263 | module-specific matched sample |
| tables/quantile_regression.csv               |      4 | 2020-02-01 to 2026-04-12, n=2263     | module-specific matched sample |
| tables/systemic_tail_association.csv         |     13 | 2021-01-02 to 2026-06-30, n=2006     | module-specific matched sample |

## Methodologies and Calculations

| method           | calculation                                                             |
|:-----------------|:------------------------------------------------------------------------|
| State bins       | leverage metrics are lagged before quintile/state assignment.           |
| Tail diagnostics | bottom-tail rates and logit-style tail summaries are reported by state. |
| Event/placebo    | liquidation windows exclude same-day initiation signatures.             |

## Formulas

$\text{tail rate}_q = N_q^{-1}\sum_t 1[r_t \le Q_{0.05}]$.

$\text{liq intensity}=\text{liquidations}/\text{lagged OI or market cap}$.

## Summary of Results

| finding                               | estimate                                   | interval                                                          | N/sample                         | interpretation                                                                    | sensitivity                                                             |
|:--------------------------------------|:-------------------------------------------|:------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| Lagged leverage state and tail stress | fitted tail probability range 3.2%-7.4%    | HAC spline-GLM confidence band                                    | 2020-02-01 to 2026-04-12, n=2263 | The fitted association is nonlinear and should not be read as a directional rule. | Quantile regression, state expected shortfall, FEVD window/horizon grid |
| Stable-core volatility connectedness  | primary generalized-FEVD range 44.0%-67.1% | descriptive rolling estimate; row-sum diagnostics in source table | 2021-09-10 to 2026-06-19, n=252  | Absolute-return connectedness varies materially over time.                        | 180/252/365 windows and 5/10/20 horizons                                |

## Analytical Results and Visualizations

![03 Leverage Tail Connectedness](figures/03_leverage_tail_connectedness.png)

The spline is restricted to the central observed leverage support. Connectedness uses a stable-core generalized FEVD and is a stress-transmission description, not a forecast.

## Robustness and Sensitivity

Sensitivity dimensions are: state bins, lags, tail threshold, denominator scaling, event windows. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Derivatives variables are stress-state diagnostics. They are not trading rules and do not establish directional liquidation attribution.

## Limitations

Liquidation timestamps, denominator price content, and same-day simultaneity constrain interpretation.

## Reproduce This Module

```bash
uv run python scripts/run_research.py --module 03_derivatives_leverage_liquidations
uv run python scripts/build_research_figures.py --module 03_derivatives_leverage_liquidations
uv run python scripts/check_research_surface.py --module 03_derivatives_leverage_liquidations
```

## Files and Code

- [`claims.csv`](tables/claims.csv)
- [`connectedness.csv`](tables/connectedness.csv)
- [`expected_shortfall.csv`](tables/expected_shortfall.csv)
- [`leverage_tail_diagnostics.csv`](tables/leverage_tail_diagnostics.csv)
- [`leverage_tail_horizon_sensitivity.csv`](tables/leverage_tail_horizon_sensitivity.csv)
- [`leverage_tail_model.csv`](tables/leverage_tail_model.csv)
- [`quantile_es.csv`](tables/quantile_es.csv)
- [`quantile_regression.csv`](tables/quantile_regression.csv)
- [`systemic_tail_association.csv`](tables/systemic_tail_association.csv)

- [Methodology](methodology.md)
- [Findings](findings.md)
- [Interpretation](interpretation.md)
- [Limitations](limitations.md)
- Code: `src/cqresearch/research/analytical_modules.py`
