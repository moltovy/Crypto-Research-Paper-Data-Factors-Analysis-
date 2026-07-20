# Crypto Market Dynamics

## Project Overview

Crypto Market Dynamics is a reproducible empirical study of how crypto dependence, financial integration, institutional plumbing, leverage stress, liquidity state, and market structure evolved through the frozen 2026-06-30 acquisition cutoff.

The evidence is descriptive and associational. It does not forecast prices, propose trading rules, or identify causal effects.

## Evidence Map

| Question | Primary evidence | Sample boundary | Main limitation |
|---|---|---|---|
| How broad are common crypto variation, lower-tail dependence, and TradFi integration? | [Common-factor and tail tables](research/01_cross_asset_dependence_regimes/README.md); [dynamic TradFi exposures](research/02_macro_tradfi_integration/README.md) | S2 fixed stable core from 2021; XNYS-matched BTC/ETH from 2020 | Dependence and period comparisons are not causal or predictive. |
| How do institutional flows and positioning line up with market outcomes? | [ETF distributed lags and CFTC positioning](research/04_etf_institutional_flows/README.md) | Actual reporting lives; no pre-inception or holiday zero fill | Reporting time and simultaneity prevent price-impact interpretation. |
| Where do leverage states coincide with tails and connectedness? | [Leverage, expected shortfall, systemic-tail, and FEVD tables](research/03_derivatives_leverage_liquidations/README.md) | BTC state panel from 2020; S2 connectedness from 2021 | State associations are not forecasts, signals, or liquidation-cause estimates. |
| How did endogenous liquidity state and monthly market structure change? | [TVL residual and MVRV mechanics](research/05_stablecoin_defi_liquidity/README.md); [PIT structure and turnover](research/07_chain_fundamentals_sector_dynamics/README.md) | Daily liquidity panel; complete monthly PIT snapshots through May 2026 | USD TVL is valuation-sensitive; PIT data cannot recover daily constituent performance. |

## Data Universe and Asset Coverage

The [data-foundation module](research/00_data_measurement_foundation/README.md) indexes 1,518 local raw objects, 16,801 object-column records, 11 contracted logical series, and 31 engineered features as distinct ontology layers. Raw file counts are never presented as series counts. Feature dispositions are: diagnostic only: 68, excluded for ambiguous definition or unit: 129, excluded for insufficient coverage: 2, primary analysis: 25, robustness or sensitivity: 2.

S2 fixes PIT-eligible, identity-resolved assets using the January 2021 top-20 snapshot and requires at least 95% daily coverage. S4 uses monthly top-100 point-in-time snapshots only. S5 begins each institutional series at its actual reporting inception.

## Research Modules

| Module | Title | Scope |
|---|---|---|
| [00](research/00_data_measurement_foundation/README.md) | Data and Measurement Foundation | What data, assets, units, timing, coverage, identity, and release-risk constraints govern later empirical claims? |
| [01](research/01_cross_asset_dependence_regimes/README.md) | Cross-Asset Dependence and Regimes | How do crypto and TradFi return dependence, common-factor share, lower-tail co-exceedance, and regimes vary across matched samples? |
| [02](research/02_macro_tradfi_integration/README.md) | Macro and TradFi Integration | How do crypto exposures to equities, volatility, rates, the dollar, gold, and credit vary across calendars and periods? |
| [03](research/03_derivatives_leverage_liquidations/README.md) | Derivatives, Leverage, and Liquidations | Where do leverage, funding, open-interest scaling, and liquidation stress appear in volatility and tail outcomes? |
| [04](research/04_etf_institutional_flows/README.md) | ETF and Institutional Flows | How do ETF flow intensity, timing, lag response, and shock/placebo diagnostics line up with crypto outcomes? |
| [05](research/05_stablecoin_defi_liquidity/README.md) | Stablecoin and DeFi Liquidity State | What do stablecoin supply and DeFi TVL proxies say about liquidity-state associations after unit and valuation audits? |
| [07](research/07_chain_fundamentals_sector_dynamics/README.md) | Chain Fundamentals and Sector Dynamics | Which chain-level activity, sector, and point-in-time state measures have enough coverage and definition clarity for descriptive panel analysis? |
| [09](research/09_event_stress_cross_module_synthesis/README.md) | Event Stress and Cross-Module Synthesis | Which event-window, stress-state, and cross-module findings remain strongest after comparing sample, method, uncertainty, measurement risk, and limitations? |

## Qualified Findings

| Module | Finding | Grade | Source | Limitation |
|---|---|---|---|---|
| Cross-Asset Dependence and Regimes | Within S2, the median leave-one-out common-variance share is 61.0%, while median 5% lower-tail co-exceedance is 2.8% above the independence benchmark. | B | [research/01_cross_asset_dependence_regimes/tables/common_factor_results.csv](research/01_cross_asset_dependence_regimes/tables/common_factor_results.csv) | S2 is a fixed 2021 PIT-eligible universe; results do not establish causation, forecasting value, or investability. |
| Macro and TradFi Integration | Conditional QQQ exposure estimates differ across the predeclared BTC ETF-era split: BTC 1.03 to 0.93 (change p=0.611); ETH 1.33 to 1.51 (change p=0.520). | B | [research/02_macro_tradfi_integration/tables/dynamic_tradfi_exposures.csv](research/02_macro_tradfi_integration/tables/dynamic_tradfi_exposures.csv) | The split is descriptive; contemporaneous exposures do not identify ETF effects or causal transmission. |
| Derivatives, Leverage, and Liquidations | Across observed support, lagged BTC leverage states coincide with fitted next-session lower-tail probabilities from 3.2% to 7.4%. | B | [research/03_derivatives_leverage_liquidations/tables/leverage_tail_model.csv](research/03_derivatives_leverage_liquidations/tables/leverage_tail_model.csv) | The relationship is associational, nonlinear, and not a forecast, trading signal, or liquidation-cause estimate. |
| ETF and Institutional Flows | Across 12 asset-lag return coefficients, 2 have 95% moving-block simultaneous intervals excluding zero under the reported-date convention. Simultaneity prevents a price-impact interpretation. | B | [research/04_etf_institutional_flows/tables/etf_distributed_lags.csv](research/04_etf_institutional_flows/tables/etf_distributed_lags.csv) | ETF reporting time is unresolved, CFTC data is weekly and released after the as-of date, and neither design identifies causality. |
| Chain Fundamentals and Sector Dynamics | Across complete monthly PIT snapshots, effective asset count changed from 5.1 to 7.6, while median one-month membership turnover was 14.8%. | B | [research/07_chain_fundamentals_sector_dynamics/tables/pit_concentration.csv](research/07_chain_fundamentals_sector_dynamics/tables/pit_concentration.csv) | Monthly snapshots support market-structure statements only; they do not establish daily constituent performance or historical altseason behavior. |

## Evidence Figures

### Common variation is broad, and BTC lower-tail co-exceedance is above its independence benchmark for the shown pairs.

![Common variation is broad, and BTC lower-tail co-exceedance is above its independence benchmark for the shown pairs.](research/01_cross_asset_dependence_regimes/figures/01_common_factor_tail_dependence.png)

**Sample:** S2 fixed stable core, 2021-01-02 through 2026-06-30, n=2006 matched returns. **Method:** leave one out factor and tail forest.

**Result:** Common variation is broad, and BTC lower-tail co-exceedance is above its independence benchmark for the shown pairs. **Boundary:** Fixed PIT-eligible membership supports within-sample dependence statements, not forecasts, causal transmission, or investability claims. [Source table](research/01_cross_asset_dependence_regimes/tables/common_factor_results.csv).

### Conditional QQQ exposure varies over time, while formal ETF-era interaction estimates are weak.

![Conditional QQQ exposure varies over time, while formal ETF-era interaction estimates are weak.](research/02_macro_tradfi_integration/figures/02_dynamic_tradfi_integration.png)

**Sample:** XNYS-aligned BTC/ETH and TradFi observations, 2020-01-03 through 2026-04-14, n=1577. **Method:** rolling exposure and interaction forest.

**Result:** Conditional QQQ exposure varies over time, while formal ETF-era interaction estimates are weak. **Boundary:** Contemporaneous period comparisons do not identify ETF effects or causal transmission. [Source table](research/02_macro_tradfi_integration/tables/dynamic_tradfi_exposures.csv).

### ETF lag evidence is mostly weak under simultaneous bands; CFTC positioning provides separate weekly context.

![ETF lag evidence is mostly weak under simultaneous bands; CFTC positioning provides separate weekly context.](research/04_etf_institutional_flows/figures/04_institutional_market_plumbing.png)

**Sample:** Actual BTC/ETH ETF report dates through 2026-04-10 and CFTC standard contracts through 2026-06-30. **Method:** simultaneous lag forest and positioning eras.

**Result:** ETF lag evidence is mostly weak under simultaneous bands; CFTC positioning provides separate weekly context. **Boundary:** Reporting-time uncertainty and simultaneity prevent a price-impact interpretation. [Source table](research/04_etf_institutional_flows/tables/etf_distributed_lags.csv).

### Tail probabilities vary nonlinearly over observed leverage support, while stable-core connectedness changes through time.

![Tail probabilities vary nonlinearly over observed leverage support, while stable-core connectedness changes through time.](research/03_derivatives_leverage_liquidations/figures/03_leverage_tail_connectedness.png)

**Sample:** BTC state model, 2020-02-01 through 2026-04-12; S2 connectedness from 2021. **Method:** spline marginal association and generalized FEVD.

**Result:** Tail probabilities vary nonlinearly over observed leverage support, while stable-core connectedness changes through time. **Boundary:** These are stress-state associations, not forecasts, trading signals, or liquidation-cause estimates. [Source table](research/03_derivatives_leverage_liquidations/tables/leverage_tail_model.csv).

### Effective market breadth and constituent turnover changed materially across complete monthly snapshots.

![Effective market breadth and constituent turnover changed materially across complete monthly snapshots.](research/07_chain_fundamentals_sector_dynamics/figures/07_pit_concentration_turnover.png)

**Sample:** Complete monthly PIT top-100 snapshots, January 2020 through May 2026. **Method:** effective breadth and membership turnover.

**Result:** Effective market breadth and constituent turnover changed materially across complete monthly snapshots. **Boundary:** Monthly PIT evidence supports market-structure statements only, not daily historical constituent performance. [Source table](research/07_chain_fundamentals_sector_dynamics/tables/pit_concentration.csv).

## Methods Used

| Method family | Used for | Key boundary |
|---|---|---|
| Leave-one-out PCA and moving-block tail inference | common variation and co-exceedance | realized dependence only |
| Multivariate HAC exposure and era interactions | TradFi integration | contemporaneous period comparison |
| Distributed lags with max-t bands | ETF market plumbing | timing and simultaneity remain unresolved |
| Spline logit, quantile/ES, generalized FEVD | leverage and tail stress | descriptive state association |
| PIT concentration, turnover, and exact decomposition | monthly market structure | no daily constituent-performance inference |

## Important Limitations

- S2 is fixed from a January 2021 PIT snapshot; S3 current-cohort daily analysis remains survivorship-biased and cannot establish historical altseason behavior.
- ETF flows are market-plumbing associations with timing and simultaneity concerns.
- Stablecoin supply, DeFi TVL, and related balance-sheet measures are endogenous state proxies; raw USD TVL is valuation-sensitive.
- Same-day MVRV is a mechanically price-linked valuation-state diagnostic and is excluded from primary BTC/ETH models.
- Monthly point-in-time data supports composition, concentration, turnover, and state variables only, not daily constituent returns.

## Reproduce

```bash
uv sync --all-extras
uv run ruff check src/cqresearch scripts tests
uv run ruff format --check src/cqresearch scripts tests
uv run mypy src/cqresearch
uv run pytest -q
uv run python scripts/run_all.py --mode local
uv run python scripts/build_research_figures.py --module all
uv run python scripts/check_research_surface.py --module all
```

## Repository Structure

- [`research/`](research/README.md): canonical public research surface.
- [`src/cqresearch/`](src/cqresearch): contracts, samples, estimators, reporting, and visualization code.
- [`scripts/`](scripts): thin command-line entry points.
- [`config/`](config): data, sample, source, figure, and module registries.
- `data_local/`: local raw data, normalized panels, caches, and private QA evidence; intentionally untracked.

## Data Policy and Citation

Raw/provider data stays local under `data_local/` and outside Git. Public tables and figures are derived semantic outputs designed for review without redistributing provider exports.

This repository is independent research and is not affiliated with any data provider. See [`REFERENCES.md`](REFERENCES.md) for source and method attribution. Cite the commit, module, table, figure, sample definition, uncertainty statement, and limitation when referencing a result.
