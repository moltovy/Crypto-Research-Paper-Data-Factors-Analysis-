# CryptoQuant / ETH/Fund Data

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
| `Ethereum Coinbase Premium Gap - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 | `cd8ca1fb2925` |
| `Ethereum Coinbase Premium Index - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 | `32b3b56e85e2` |
| `Ethereum Fund Holdings - All Symbol - Day.csv` | Fund holdings | 2020-11-04 .. 2026-04-09 | 1,983 | daily | 0 | 3 | `8ee984b6e674` |
| `Ethereum Fund Market Premium - All Symbol - Day.csv` | Fund market premium | 2020-11-04 .. 2026-04-09 | 1,379 | daily | 604 | 3 | `907a39f6e396` |
| `Ethereum Fund Price (USD) - ETHE - Day.csv` | Fund price | 2019-06-14 .. 2026-04-02 | 1,710 | daily | 775 | 3 | `80b508e22438` |
| `Ethereum Fund Volume - All Symbol - Day.csv` | Fund volume | 2019-06-14 .. 2026-04-09 | 1,738 | daily | 754 | 3 | `eca58521c059` |
| `Ethereum Korea Premium Index - Day.csv` | Korea premium | 2020-07-16 .. 2026-04-10 | 2,095 | daily | 0 | 3 | `ed07d241b3b6` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Coinbase Premium Gap - Day.csv`**

```csv
date,timestamp_utc,Coinbase Premium Gap
2017-08-17,2017-08-17T00:00:00Z,-1.33
2017-08-18,2017-08-18T00:00:00Z,-1.09
```

**`Ethereum Coinbase Premium Index - Day.csv`**

```csv
date,timestamp_utc,Coinbase Premium Index
2017-08-17,2017-08-17T00:00:00Z,-0.44039735
2017-08-18,2017-08-18T00:00:00Z,-0.37079875
```

**`Ethereum Fund Holdings - All Symbol - Day.csv`**

```csv
date,timestamp_utc,Fund Holdings
2020-11-04,2020-11-04T00:00:00Z,2433070.0
2020-11-05,2020-11-05T00:00:00Z,2432987.0
```

**`Ethereum Fund Market Premium - All Symbol - Day.csv`**

```csv
date,timestamp_utc,Fund Market Premium
2020-11-04,2020-11-04T00:00:00Z,41.51715087369463
2020-11-05,2020-11-05T00:00:00Z,46.18453733018957
```

**`Ethereum Fund Price (USD) - ETHE - Day.csv`**

```csv
date,timestamp_utc,Fund Price (USD)
2019-06-14,2019-06-14T00:00:00Z,6.66666666667
2019-06-17,2019-06-17T00:00:00Z,6.66666666667
```

**`Ethereum Fund Volume - All Symbol - Day.csv`**

```csv
date,timestamp_utc,Fund Volume
2019-06-14,2019-06-14T00:00:00Z,100
2019-06-17,2019-06-17T00:00:00Z,0
```

**`Ethereum Korea Premium Index - Day.csv`**

```csv
date,timestamp_utc,Korea Premium Index
2020-07-16,2020-07-16T00:00:00Z,-0.74
2020-07-17,2020-07-17T00:00:00Z,-0.88
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
