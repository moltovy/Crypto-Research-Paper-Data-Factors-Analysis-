# 03_derivatives_leverage_liquidations: Derivatives, Leverage, and Liquidations

## Overview

This module estimates how lagged leverage states coincide with next-day tail stress and how stable-core return connectedness evolves.

## Questions Investigated

- How does conditional next-day BTC tail probability vary over observed lagged leverage support?
- How do quantile, expected-shortfall, systemic-tail, and generalized-FEVD diagnostics change across specifications?

## Data, Assets, and Sample

| artifact                                     |   result_rows | analytical_sample                    | coverage rule                  |
|:---------------------------------------------|--------------:|:-------------------------------------|:-------------------------------|
| tables/connectedness.csv                     |           502 | 2021-06-30 to 2026-06-27, n=180-365  | module-specific matched sample |
| tables/expected_shortfall.csv                |             5 | 2020-02-01 to 2026-04-12, n=452-453  | module-specific matched sample |
| tables/leverage_tail_diagnostics.csv         |             1 | 2020-02-01 to 2026-04-12, n=2263     | module-specific matched sample |
| tables/leverage_tail_horizon_sensitivity.csv |             5 | 2020-02-01 to 2026-04-05, n=90-91    | module-specific matched sample |
| tables/leverage_tail_model.csv               |            19 | 2020-02-01 to 2026-04-12, n=2263     | module-specific matched sample |
| tables/quantile_es.csv                       |             9 | 2020-02-01 to 2026-04-12, n=452-2263 | module-specific matched sample |
| tables/quantile_regression.csv               |             4 | 2020-02-01 to 2026-04-12, n=2263     | module-specific matched sample |
| tables/systemic_tail_association.csv         |            13 | 2021-01-02 to 2026-06-30, n=2006     | module-specific matched sample |

## Methodologies and Calculations

| method           | calculation                                                                                             |
|:-----------------|:--------------------------------------------------------------------------------------------------------|
| Tail-state model | fit a spline logistic model using lagged OI-to-market-cap, funding, liquidation, and volatility states. |
| Tail severity    | estimate 5% and 10% quantile associations, expected shortfall, CoVaR, delta-CoVaR, and MES.             |
| Connectedness    | estimate rolling generalized FEVD on S2 using 252 observations, BIC lag at most five, and horizon 10.   |

## Formulas

$P(I[r_{t+1}\le Q_{0.05}]=1\mid X_t)=\operatorname{logit}^{-1}(\alpha+s(X_t))$.

$Q_\tau(r_{t+1}\mid X_t)=\alpha_\tau+\beta_\tau'X_t$.

$TCI_t=100N^{-1}\sum_{i\ne j}\tilde\theta_{ij,t}^{(H)}$.

## Summary of Results

| finding                               | estimate                                   | interval                                                          | N/sample                         | interpretation                                                                    | sensitivity                                                             |
|:--------------------------------------|:-------------------------------------------|:------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| Lagged leverage state and tail stress | fitted tail probability range 3.2%-7.4%    | HAC spline-GLM confidence band                                    | 2020-02-01 to 2026-04-12, n=2263 | The fitted association is nonlinear and should not be read as a directional rule. | Quantile regression, state expected shortfall, FEVD window/horizon grid |
| Stable-core volatility connectedness  | primary generalized-FEVD range 44.0%-67.1% | descriptive rolling estimate; row-sum diagnostics in source table | 2021-09-10 to 2026-06-19, n=252  | Absolute-return connectedness varies materially over time.                        | 180/252/365 windows and 5/10/20 horizons                                |

## Analytical Results and Visualizations

![03 Leverage Tail Connectedness](figures/03_leverage_tail_connectedness.png)

The spline is restricted to the central observed leverage support. Connectedness uses a stable-core generalized FEVD and is a stress-transmission description, not a forecast.

## Robustness and Sensitivity

Sensitivity dimensions are: outcome horizon, quantile, VAR window, FEVD horizon, variable order. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Differences over observed state support are conditional associations, not forecasts, signals, or liquidation-cause estimates.

## Limitations

Leverage measures are endogenous and USD-valued fields can contain price content. Tail samples are small, and rolling VAR windows require stability and row-sum diagnostics.

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
- [Code: `evidence_modules.py`](../../src/cqresearch/research/evidence_modules.py)
- [Code: `leverage_tail.py`](../../src/cqresearch/modeling/leverage_tail.py)
- [Test: `test_leverage_tail.py`](../../tests/unit/test_leverage_tail.py)
- [Test: `test_fevd_sensitivity.py`](../../tests/unit/test_fevd_sensitivity.py)
