# CryptoQuant / BTC/Network Stats

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (7)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Block Interval (Mean) - Day.csv` | Bitcoin Block Interval (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `3470ccd63eba` |
| `Bitcoin Block Size (Mean) - Day.csv` | Bitcoin Block Size (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `23f3552cba5d` |
| `Bitcoin Blocks Mined - Day.csv` | Bitcoin Blocks Mined - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `0fa0a666788e` |
| `Bitcoin Difficulty - Day.csv` | Difficulty | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `cd0ce952be7f` |
| `Bitcoin Hashrate - Day.csv` | Hashrate | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `e555b81c810d` |
| `Bitcoin UTXO Count - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `be32f1cda924` |
| `Bitcoin Velocity - Day.csv` | Bitcoin Velocity - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `fc609a68441c` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Block Interval (Mean) - Day.csv`**

```csv
date,timestamp_utc,Block Interval (Mean)
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Block Size (Mean) - Day.csv`**

```csv
date,timestamp_utc,Block Size (Mean)
2009-01-03,2009-01-03T00:00:00Z,285.0
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Blocks Mined - Day.csv`**

```csv
date,timestamp_utc,Blocks Mined
2009-01-03,2009-01-03T00:00:00Z,1
2009-01-04,2009-01-04T00:00:00Z,0
```

**`Bitcoin Difficulty - Day.csv`**

```csv
date,timestamp_utc,Difficulty
2009-01-03,2009-01-03T00:00:00Z,1.0
2009-01-04,2009-01-04T00:00:00Z,1.0
```

**`Bitcoin Hashrate - Day.csv`**

```csv
date,timestamp_utc,Hashrate
2009-01-03,2009-01-03T00:00:00Z,4.971e-05
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin UTXO Count - Day.csv`**

```csv
date,timestamp_utc,UTXO Count
2009-01-03,2009-01-03T00:00:00Z,1
2009-01-04,2009-01-04T00:00:00Z,1
```

**`Bitcoin Velocity - Day.csv`**

```csv
date,timestamp_utc,Velocity
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
