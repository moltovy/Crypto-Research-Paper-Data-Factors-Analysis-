# CryptoQuant / BTC/Fund Data

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
| `Bitcoin Coinbase Premium Gap - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 2 | `670bc61f3739` |
| `Bitcoin Coinbase Premium Index - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 2 | `c3f7c64907ce` |
| `Bitcoin Fund Holdings - All Symbol - Day.csv` | Fund holdings | 2020-06-09 .. 2026-04-09 | 2,131 | daily | 0 | 2 | `9b4fd46884d5` |
| `Bitcoin Fund Market Premium - All Symbol - Day.csv` | Fund market premium | 2020-06-09 .. 2026-04-09 | 1,506 | daily | 625 | 2 | `fe841e60f5e7` |
| `Bitcoin Fund Price (USD) - GBTC - Day.csv` | Fund price | 2015-05-04 .. 2026-04-02 | 2,746 | daily | 1241 | 2 | `b355532d8f67` |
| `Bitcoin Fund Volume - All Symbol - Day.csv` | Fund volume | 2015-05-04 .. 2026-04-09 | 2,792 | daily | 1202 | 2 | `49d01ff2a7f1` |
| `Bitcoin Korea Premium Index - Day.csv` | Korea premium | 2020-07-16 .. 2026-04-10 | 2,095 | daily | 0 | 2 | `eeb4eaa9e14b` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Coinbase Premium Gap - Day.csv`**

```csv
date,Coinbase Premium Gap
2017-08-17,-5.07
2017-08-18,-6.65
```

**`Bitcoin Coinbase Premium Index - Day.csv`**

```csv
date,Coinbase Premium Index
2017-08-17,-0.11831751
2017-08-18,-0.16186468
```

**`Bitcoin Fund Holdings - All Symbol - Day.csv`**

```csv
date,Fund Holdings
2020-06-09,365088.04499003815
2020-06-10,365191.0
```

**`Bitcoin Fund Market Premium - All Symbol - Day.csv`**

```csv
date,Fund Market Premium
2020-06-09,24.249014272912504
2020-06-10,31.016299277094504
```

**`Bitcoin Fund Price (USD) - GBTC - Day.csv`**

```csv
date,Fund Price (USD)
2015-05-04,0.412399908898
2015-05-05,0.540047499747
```

**`Bitcoin Fund Volume - All Symbol - Day.csv`**

```csv
date,Fund Volume
2015-05-04,765
2015-05-05,435
```

**`Bitcoin Korea Premium Index - Day.csv`**

```csv
date,Korea Premium Index
2020-07-16,-0.78
2020-07-17,-0.86
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
