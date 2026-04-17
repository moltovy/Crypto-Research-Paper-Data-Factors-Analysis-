# CryptoQuant / BTC/Fees And Revenue

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (11)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Block Rewards - Day.csv` | Bitcoin Block Rewards - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `6cc3f6f6a457` |
| `Bitcoin Block Rewards USD - Day.csv` | Bitcoin Block Rewards USD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `c6ebfc793e5e` |
| `Bitcoin Fees (Total) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `96dbd906a249` |
| `Bitcoin Fees per Block (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `4ff065471bb9` |
| `Bitcoin Fees per Block USD (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `f4a8a4d5dc85` |
| `Bitcoin Fees per Transaction (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `ca7ccbb7b100` |
| `Bitcoin Fees per Transaction (Median) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `3bce0cb2569c` |
| `Bitcoin Fees per Transaction USD (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `73a771e2e687` |
| `Bitcoin Fees per Transaction USD (Median) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `1d6e9c084763` |
| `Bitcoin Fees to Reward Ratio - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `88f95c033476` |
| `Bitcoin Fees USD (Total) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `5df19beff574` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Block Rewards - Day.csv`**

```csv
date,timestamp_utc,Block Rewards
2009-01-03,2009-01-03T00:00:00Z,50.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Block Rewards USD - Day.csv`**

```csv
date,timestamp_utc,Block Rewards USD
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Fees (Total) - Day.csv`**

```csv
date,timestamp_utc,Fees (Total)
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Fees per Block (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees per Block (Mean)
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Fees per Block USD (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees per Block USD (Mean)
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Fees per Transaction (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees per Transaction (Mean)
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Fees per Transaction (Median) - Day.csv`**

```csv
date,timestamp_utc,Fees per Transaction (Median)
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Fees per Transaction USD (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees per Transaction USD (Mean)
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Fees per Transaction USD (Median) - Day.csv`**

```csv
date,timestamp_utc,Fees per Transaction USD (Median)
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Fees to Reward Ratio - Day.csv`**

```csv
date,timestamp_utc,Fees to Reward Ratio
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Fees USD (Total) - Day.csv`**

```csv
date,timestamp_utc,Fees USD (Total)
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
