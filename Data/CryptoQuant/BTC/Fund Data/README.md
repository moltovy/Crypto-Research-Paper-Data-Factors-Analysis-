# CryptoQuant / BTC/Fund Data

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
| `Bitcoin Coinbase Premium Gap - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 | `7d8964b28ef8` |
| `Bitcoin Coinbase Premium Index - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 | `247c5306d282` |
| `Bitcoin Fund Holdings - All Symbol - Day.csv` | Fund holdings | 2020-06-09 .. 2026-04-09 | 2,131 | daily | 0 | 3 | `0dd6bd0b2321` |
| `Bitcoin Fund Market Premium - All Symbol - Day.csv` | Fund market premium | 2020-06-09 .. 2026-04-09 | 1,506 | daily | 625 | 3 | `c5c491bf9175` |
| `Bitcoin Fund Price (USD) - GBTC - Day.csv` | Fund price | 2015-05-04 .. 2026-04-02 | 2,746 | daily | 1241 | 3 | `625cd0c1a13b` |
| `Bitcoin Fund Volume - All Symbol - Day.csv` | Fund volume | 2015-05-04 .. 2026-04-09 | 2,792 | daily | 1202 | 3 | `2fe3703d9490` |
| `Bitcoin Korea Premium Index - Day.csv` | Korea premium | 2020-07-16 .. 2026-04-10 | 2,095 | daily | 0 | 3 | `b897675af587` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Coinbase Premium Gap - Day.csv`**

```csv
date,timestamp_utc,Coinbase Premium Gap
2017-08-17,2017-08-17T00:00:00Z,-5.07
2017-08-18,2017-08-18T00:00:00Z,-6.65
```

**`Bitcoin Coinbase Premium Index - Day.csv`**

```csv
date,timestamp_utc,Coinbase Premium Index
2017-08-17,2017-08-17T00:00:00Z,-0.11831751
2017-08-18,2017-08-18T00:00:00Z,-0.16186468
```

**`Bitcoin Fund Holdings - All Symbol - Day.csv`**

```csv
date,timestamp_utc,Fund Holdings
2020-06-09,2020-06-09T00:00:00Z,365088.04499003815
2020-06-10,2020-06-10T00:00:00Z,365191.0
```

**`Bitcoin Fund Market Premium - All Symbol - Day.csv`**

```csv
date,timestamp_utc,Fund Market Premium
2020-06-09,2020-06-09T00:00:00Z,24.249014272912504
2020-06-10,2020-06-10T00:00:00Z,31.016299277094504
```

**`Bitcoin Fund Price (USD) - GBTC - Day.csv`**

```csv
date,timestamp_utc,Fund Price (USD)
2015-05-04,2015-05-04T00:00:00Z,0.412399908898
2015-05-05,2015-05-05T00:00:00Z,0.540047499747
```

**`Bitcoin Fund Volume - All Symbol - Day.csv`**

```csv
date,timestamp_utc,Fund Volume
2015-05-04,2015-05-04T00:00:00Z,765
2015-05-05,2015-05-05T00:00:00Z,435
```

**`Bitcoin Korea Premium Index - Day.csv`**

```csv
date,timestamp_utc,Korea Premium Index
2020-07-16,2020-07-16T00:00:00Z,-0.78
2020-07-17,2020-07-17T00:00:00Z,-0.86
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
