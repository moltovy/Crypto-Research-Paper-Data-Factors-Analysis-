# CryptoQuant / BTC/Addresses

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Active Addresses - Day.csv` | Active addresses | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `3f92521c86aa` |
| `Bitcoin Active Receiving Addresses - Day.csv` | Bitcoin Active Receiving Addresses - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `0cd34e5aadcd` |
| `Bitcoin Active Sending Addresses - Day.csv` | Bitcoin Active Sending Addresses - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `085cf3ffdfac` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Active Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Addresses
2009-01-03,2009-01-03T00:00:00Z,1
2009-01-04,2009-01-04T00:00:00Z,0
```

**`Bitcoin Active Receiving Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses
2009-01-03,2009-01-03T00:00:00Z,1
2009-01-04,2009-01-04T00:00:00Z,0
```

**`Bitcoin Active Sending Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses
2009-01-03,2009-01-03T00:00:00Z,0
2009-01-04,2009-01-04T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
