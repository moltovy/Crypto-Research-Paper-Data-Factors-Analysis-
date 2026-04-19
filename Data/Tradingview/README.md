# TradingView

**Source**: https://www.tradingview.com/

Manual chart-to-CSV exports from TradingView used for market-structure, TradFi bridge, crypto-equity, ETF proxy, futures, dominance, and total-market-cap analysis.

## Folder Layout

- `Daily/` - 1D bars for CME crypto futures and basis/ratio series, crypto equities, ETFs, DXY, gold, Deribit DVOL, ETF-vs-spot ratios, and CRYPTOCAP market-structure series.
- `Weekly/` - 1W bars for continuous futures, selected ETFs/equities, DXY, gold, and CRYPTOCAP market-structure series.

The detailed generated inventories live in:

- `Data/Tradingview/Daily/README.md`
- `Data/Tradingview/Weekly/README.md`

## Newly Added CRYPTOCAP Series

The April 2026 refresh added six curated TradingView CRYPTOCAP files:

- `Daily/CRYPTOCAP_BTC_dominance__daily.csv`
- `Daily/CRYPTOCAP_ETH_dominance__daily.csv`
- `Daily/CRYPTOCAP_TOTAL3__daily.csv`
- `Weekly/CRYPTOCAP_BTC_dominance__weekly.csv`
- `Weekly/CRYPTOCAP_ETH_dominance__weekly.csv`
- `Weekly/CRYPTOCAP_TOTAL3__weekly.csv`

These series support market-evolution analysis around BTC dominance, ETH dominance, and altcoin ex-BTC/ETH market capitalization (`TOTAL3`).

## Data Convention

Curated TradingView CSVs use:

- first column `date`,
- ISO `YYYY-MM-DD`,
- ascending order,
- OHLC columns where available,
- `Volume` and open-interest columns where TradingView exports them.

The current Daily/Weekly curated files do not keep a separate `timestamp_utc` column.

## Units

- CME futures: OHLC in instrument quote currency; volume/open interest in contracts.
- ETF/equity/commodity/DXY series: OHLC in the instrument's market units; volume in shares/contracts where available.
- CRYPTOCAP BTC/ETH dominance: percent-style index values from TradingView CRYPTOCAP dominance symbols.
- CRYPTOCAP TOTAL3: market capitalization level for crypto excluding BTC and ETH, as exported by TradingView.

## Research Use

TradingView data is especially useful for:

- explicit CME futures coverage not exposed in CryptoQuant aggregate derivatives exports,
- ETF and equity market bridge variables,
- dollar/gold/tech-equity controls,
- crypto-equity proxy analysis,
- market dominance and altcoin-cycle diagnostics using CRYPTOCAP.

Use `Data/MASTER_DATA.csv` and `Data/MASTER_DATA.md` as the canonical inventory for row counts, hashes, date ranges, and missingness.

## Licensing

TradingView chart data is for internal research use only; redistribution may be restricted by TradingView terms.

---
Manually maintained folder overview. Generated file-level inventories are produced by `tools/data_curation/06_build_inventory.py`.
