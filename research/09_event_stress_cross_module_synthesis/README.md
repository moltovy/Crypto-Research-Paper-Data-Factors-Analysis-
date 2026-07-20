# 09_event_stress_cross_module_synthesis: Event Stress and Cross-Module Synthesis

## Overview

This module retains the registered event atlas as appendix sensitivity evidence and consolidates qualified upstream claims for final review.

## Questions Investigated

- How do fixed post-event BTC/ETH windows compare with non-event placebo windows?
- Which upstream claims retain complete sample, method, uncertainty, provenance, grade, and limitation fields?

## Data, Assets, and Sample

| artifact                         |   result_rows | analytical_sample                                                   | coverage rule                  |
|:---------------------------------|--------------:|:--------------------------------------------------------------------|:-------------------------------|
| tables/event_registry.csv        |             8 | 8 registered events; 2022-05-09 to 2024-08-05                       | module-specific matched sample |
| tables/event_response_matrix.csv |            48 | 8 events x 2 assets x 3 horizons = 48 estimates; placebo n=212-2270 | module-specific matched sample |
| tables/evidence_ledger.csv       |             6 | 6 upstream claims; each row retains its own analytical sample       | module-specific matched sample |
| tables/robustness_summary.csv    |             6 | 6 upstream modules; summary rows are not model observations         | module-specific matched sample |

## Methodologies and Calculations

| method             | calculation                                                                                                           |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------|
| Event atlas        | sum +1, +5, and +10 post-event returns with event day excluded and compare them with non-overlapping placebo windows. |
| Evidence synthesis | consolidate module claim rows without changing estimates or upgrading weak evidence.                                  |

## Formulas

$R_{e,h}=\sum_{j=1}^{h}r_{t_e+j}$ for $h\in\{1,5,10\}$.

$p_e=2\min(\hat F_{placebo}(R_e),1-\hat F_{placebo}(R_e))$.

## Summary of Results

| finding                | estimate                          | interval                                                            | N/sample                                                                                                                                       | interpretation                               | sensitivity                                                            |
|:-----------------------|:----------------------------------|:--------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------|:-----------------------------------------------------------------------|
| Registered event atlas | 8 events and 48 asset-window rows | empirical non-event-window percentile and two-sided placebo p-value | 8 events x 2 assets x 3 horizons = 48 event-asset-horizon estimates; BTC/ETH return support 2020-01-02 to 2026-04-14; placebo windows 212-2270 | Event responses remain appendix diagnostics. | +1/+5/+10 windows; event-day exclusion; non-overlapping placebo starts |

## Analytical Results and Visualizations

![09 Event Atlas Appendix](figures/09_event_atlas_appendix.png)

The event atlas shows +1 through +10 cumulative log returns and empirical percentile ranks. It is intentionally outside the root README.

## Robustness and Sensitivity

Sensitivity dimensions are: window length, event-day exclusion, placebo eligibility, claim completeness. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Event windows are descriptive stress diagnostics. The synthesis preserves upstream uncertainty and does not turn associations into causal event effects.

## Limitations

Event selection, overlapping developments, and non-random timing preclude identification. Synthesis quality is bounded by upstream data and models.

## Reproduce This Module

```bash
uv run python scripts/run_research.py --module 09_event_stress_cross_module_synthesis
uv run python scripts/build_research_figures.py --module 09_event_stress_cross_module_synthesis
uv run python scripts/check_research_surface.py --module 09_event_stress_cross_module_synthesis
```

## Files and Code

- [`claims.csv`](tables/claims.csv)
- [`event_registry.csv`](tables/event_registry.csv)
- [`event_response_matrix.csv`](tables/event_response_matrix.csv)
- [`evidence_ledger.csv`](tables/evidence_ledger.csv)
- [`robustness_summary.csv`](tables/robustness_summary.csv)

- [Methodology](methodology.md)
- [Findings](findings.md)
- [Interpretation](interpretation.md)
- [Limitations](limitations.md)
- [Code: `evidence_modules.py`](../../src/cqresearch/research/evidence_modules.py)
- [Test: `test_reporting.py`](../../tests/unit/test_reporting.py)
- [Test: `test_feature_strength_outputs.py`](../../tests/unit/test_feature_strength_outputs.py)
