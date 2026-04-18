# CryptoQuant / BTC/Network Stats

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (7)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Block Interval (Mean) - Day.csv` | Bitcoin Block Interval (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `742a683a9b4b` |
| `Bitcoin Block Size (Mean) - Day.csv` | Bitcoin Block Size (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `5ba220ab47ba` |
| `Bitcoin Blocks Mined - Day.csv` | Bitcoin Blocks Mined - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `118854b82902` |
| `Bitcoin Difficulty - Day.csv` | Difficulty | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `824090c2ac15` |
| `Bitcoin Hashrate - Day.csv` | Hashrate | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `0e3f869fe099` |
| `Bitcoin UTXO Count - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `2b52bb8dc5b0` |
| `Bitcoin Velocity - Day.csv` | Bitcoin Velocity - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `5fc39487b71b` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Block Interval (Mean) - Day.csv`**

```csv
date,Block Interval (Mean)
2009-01-03,0.0
2009-01-04,
```

**`Bitcoin Block Size (Mean) - Day.csv`**

```csv
date,Block Size (Mean)
2009-01-03,285.0
2009-01-04,
```

**`Bitcoin Blocks Mined - Day.csv`**

```csv
date,Blocks Mined
2009-01-03,1
2009-01-04,0
```

**`Bitcoin Difficulty - Day.csv`**

```csv
date,Difficulty
2009-01-03,1.0
2009-01-04,1.0
```

**`Bitcoin Hashrate - Day.csv`**

```csv
date,Hashrate
2009-01-03,4.971e-05
2009-01-04,
```

**`Bitcoin UTXO Count - Day.csv`**

```csv
date,UTXO Count
2009-01-03,1
2009-01-04,1
```

**`Bitcoin Velocity - Day.csv`**

```csv
date,Velocity
2009-01-03,0.0
2009-01-04,0.0
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
