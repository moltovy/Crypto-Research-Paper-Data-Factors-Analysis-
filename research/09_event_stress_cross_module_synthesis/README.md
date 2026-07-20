# 09_event_stress_cross_module_synthesis: Event Stress and Cross-Module Synthesis

## Overview

This module combines event-window stress diagnostics with the cross-module evidence ledger and final claim-quality synthesis.

## Questions Investigated

- How do registered event windows compare with empirical placebo windows?
- Which findings remain strongest after sample, uncertainty, measurement-risk, and limitation review?

## Data, Assets, and Sample

| artifact                         |   rows | sample                                   | coverage rule                  |
|:---------------------------------|-------:|:-----------------------------------------|:-------------------------------|
| tables/event_registry.csv        |      8 | 2022-05-09 to 2024-08-05, result rows=8  | module-specific matched sample |
| tables/event_response_matrix.csv |     48 | 2020-01-02 to 2026-04-14, result rows=48 | module-specific matched sample |
| tables/evidence_ledger.csv       |      6 | result rows=6                            | module-specific matched sample |
| tables/robustness_summary.csv    |      6 | result rows=6                            | module-specific matched sample |

## Methodologies and Calculations

| method             | calculation                                                                            |
|:-------------------|:---------------------------------------------------------------------------------------|
| Event windows      | fixed +1 through +10 windows are compared with empirical placebo blocks.               |
| Evidence synthesis | claim rows are graded by source depth, uncertainty, measurement risk, and limitations. |

## Formulas

$R_{event}=\sum_{h=1}^{10}r_{t+h}$, excluding event day.

$q$-values and evidence grades are synthesis diagnostics, not causal identification.

## Summary of Results

| finding                | estimate                          | interval                                                            | N/sample                                 | interpretation                               | sensitivity                                                            |
|:-----------------------|:----------------------------------|:--------------------------------------------------------------------|:-----------------------------------------|:---------------------------------------------|:-----------------------------------------------------------------------|
| Registered event atlas | 8 events and 48 asset-window rows | empirical non-event-window percentile and two-sided placebo p-value | 2020-01-02 to 2026-04-14, result rows=48 | Event responses remain appendix diagnostics. | +1/+5/+10 windows; event-day exclusion; non-overlapping placebo starts |

## Analytical Results and Visualizations

![09 Event Atlas Appendix](figures/09_event_atlas_appendix.png)

The event atlas shows +1 through +10 cumulative log returns and empirical percentile ranks. It is intentionally outside the root README.

## Robustness and Sensitivity

Sensitivity dimensions are: window length, placebo eligibility, FDR, measurement risk, claim grade. Tables report matched samples, frequencies, and timing conventions where available.

## Interpretation

Event and synthesis outputs are final review instruments. They preserve weak/null findings instead of using specification search.

## Limitations

Event windows are not an identification design; synthesis quality depends on upstream modules.

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
- Code: `src/cqresearch/research/analytical_modules.py`
