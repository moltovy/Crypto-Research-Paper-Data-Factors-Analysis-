# CryptoQuant / BTC/Derivatives

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (8)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Estimated Leverage Ratio - All Exchanges - Day.csv` | Estimated leverage ratio | 2019-03-30 .. 2026-04-10 | 2,569 | daily | 0 | 2 | `fec96e3c14e9` |
| `Bitcoin Funding Rates - All Exchanges - Day.csv` | Funding rates | 2016-05-15 .. 2026-04-11 | 3,619 | daily | 0 | 2 | `4ff4e722509c` |
| `Bitcoin Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2019-01-13 .. 2026-04-11 | 2,646 | daily | 0 | 4 | `3dac7f913435` |
| `Bitcoin Long Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 2 | `0981e0d427bc` |
| `Bitcoin Long Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 2 | `0d4a1c25101b` |
| `Bitcoin Open Interest - All Exchanges, All Symbol - Day.csv` | Open interest | 2019-03-30 .. 2026-04-11 | 2,570 | daily | 0 | 2 | `a403723ed095` |
| `Bitcoin Short Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 2 | `c276007ca194` |
| `Bitcoin Short Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 2 | `59b725244084` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Estimated Leverage Ratio - All Exchanges - Day.csv`**

```csv
date,Estimated Leverage Ratio
2019-03-30,0.11725685
2019-03-31,0.11904454
```

**`Bitcoin Funding Rates - All Exchanges - Day.csv`**

```csv
date,Funding Rates
2016-05-15,0.0080575816666666
2016-05-16,0.0075417016666666
```

**`Bitcoin Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv`**

```csv
date,Neutral,Taker Buy Dominant,Taker Sell Dominant
2019-01-13,3513,-,-
2019-01-14,3663,-,-
```

**`Bitcoin Long Liquidations - All Exchanges, All Symbol - Day.csv`**

```csv
date,Long Liquidations
2018-12-20,0.0
2018-12-21,3.11874701
```

**`Bitcoin Long Liquidations USD - All Exchanges, All Symbol - Day.csv`**

```csv
date,Long Liquidations USD
2018-12-20,0.0
2018-12-21,12046.0
```

**`Bitcoin Open Interest - All Exchanges, All Symbol - Day.csv`**

```csv
date,Open Interest
2019-03-30,605258083.0
2019-03-31,618514013.0
```

**`Bitcoin Short Liquidations - All Exchanges, All Symbol - Day.csv`**

```csv
date,Short Liquidations
2018-12-20,0.24105098
2018-12-21,0.52411266
```

**`Bitcoin Short Liquidations USD - All Exchanges, All Symbol - Day.csv`**

```csv
date,Short Liquidations USD
2018-12-20,1000.0
2018-12-21,2100.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
