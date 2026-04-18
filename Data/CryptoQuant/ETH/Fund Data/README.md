# CryptoQuant / ETH/Fund Data

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
| `Ethereum Coinbase Premium Gap - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 2 | `6e9e1831bcd7` |
| `Ethereum Coinbase Premium Index - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 2 | `90755c9688ca` |
| `Ethereum Fund Holdings - All Symbol - Day.csv` | Fund holdings | 2020-11-04 .. 2026-04-09 | 1,983 | daily | 0 | 2 | `b88fd1b2a038` |
| `Ethereum Fund Market Premium - All Symbol - Day.csv` | Fund market premium | 2020-11-04 .. 2026-04-09 | 1,379 | daily | 604 | 2 | `1126f8c139c8` |
| `Ethereum Fund Price (USD) - ETHE - Day.csv` | Fund price | 2019-06-14 .. 2026-04-02 | 1,710 | daily | 775 | 2 | `a829631030ae` |
| `Ethereum Fund Volume - All Symbol - Day.csv` | Fund volume | 2019-06-14 .. 2026-04-09 | 1,738 | daily | 754 | 2 | `a38cd636bf83` |
| `Ethereum Korea Premium Index - Day.csv` | Korea premium | 2020-07-16 .. 2026-04-10 | 2,095 | daily | 0 | 2 | `69df58a54d12` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Coinbase Premium Gap - Day.csv`**

```csv
date,Coinbase Premium Gap
2017-08-17,-1.33
2017-08-18,-1.09
```

**`Ethereum Coinbase Premium Index - Day.csv`**

```csv
date,Coinbase Premium Index
2017-08-17,-0.44039735
2017-08-18,-0.37079875
```

**`Ethereum Fund Holdings - All Symbol - Day.csv`**

```csv
date,Fund Holdings
2020-11-04,2433070.0
2020-11-05,2432987.0
```

**`Ethereum Fund Market Premium - All Symbol - Day.csv`**

```csv
date,Fund Market Premium
2020-11-04,41.51715087369463
2020-11-05,46.18453733018957
```

**`Ethereum Fund Price (USD) - ETHE - Day.csv`**

```csv
date,Fund Price (USD)
2019-06-14,6.66666666667
2019-06-17,6.66666666667
```

**`Ethereum Fund Volume - All Symbol - Day.csv`**

```csv
date,Fund Volume
2019-06-14,100
2019-06-17,0
```

**`Ethereum Korea Premium Index - Day.csv`**

```csv
date,Korea Premium Index
2020-07-16,-0.74
2020-07-17,-0.88
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
