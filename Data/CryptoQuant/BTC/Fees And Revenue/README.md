# CryptoQuant / BTC/Fees And Revenue

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (11)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Block Rewards - Day.csv` | Bitcoin Block Rewards - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `974a50e668cd` |
| `Bitcoin Block Rewards USD - Day.csv` | Bitcoin Block Rewards USD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `ff662106c7fa` |
| `Bitcoin Fees (Total) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `59857c126a05` |
| `Bitcoin Fees per Block (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `44e456ba4e19` |
| `Bitcoin Fees per Block USD (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `fcc0dd2651af` |
| `Bitcoin Fees per Transaction (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `7da41afbc1e5` |
| `Bitcoin Fees per Transaction (Median) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `b7b7085ef3ab` |
| `Bitcoin Fees per Transaction USD (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `5dab1c302074` |
| `Bitcoin Fees per Transaction USD (Median) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `2bf216827b7d` |
| `Bitcoin Fees to Reward Ratio - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `24429cbe8cd5` |
| `Bitcoin Fees USD (Total) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `309ca7f91efe` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Block Rewards - Day.csv`**

```csv
date,Block Rewards
2009-01-03,50.0
2009-01-04,0.0
```

**`Bitcoin Block Rewards USD - Day.csv`**

```csv
date,Block Rewards USD
2009-01-03,0.0
2009-01-04,0.0
```

**`Bitcoin Fees (Total) - Day.csv`**

```csv
date,Fees (Total)
2009-01-03,0.0
2009-01-04,0.0
```

**`Bitcoin Fees per Block (Mean) - Day.csv`**

```csv
date,Fees per Block (Mean)
2009-01-03,0.0
2009-01-04,
```

**`Bitcoin Fees per Block USD (Mean) - Day.csv`**

```csv
date,Fees per Block USD (Mean)
2009-01-03,0.0
2009-01-04,
```

**`Bitcoin Fees per Transaction (Mean) - Day.csv`**

```csv
date,Fees per Transaction (Mean)
2009-01-03,
2009-01-04,
```

**`Bitcoin Fees per Transaction (Median) - Day.csv`**

```csv
date,Fees per Transaction (Median)
2009-01-03,
2009-01-04,
```

**`Bitcoin Fees per Transaction USD (Mean) - Day.csv`**

```csv
date,Fees per Transaction USD (Mean)
2009-01-03,
2009-01-04,
```

**`Bitcoin Fees per Transaction USD (Median) - Day.csv`**

```csv
date,Fees per Transaction USD (Median)
2009-01-03,
2009-01-04,
```

**`Bitcoin Fees to Reward Ratio - Day.csv`**

```csv
date,Fees to Reward Ratio
2009-01-03,0.0
2009-01-04,
```

**`Bitcoin Fees USD (Total) - Day.csv`**

```csv
date,Fees USD (Total)
2009-01-03,0.0
2009-01-04,0.0
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
