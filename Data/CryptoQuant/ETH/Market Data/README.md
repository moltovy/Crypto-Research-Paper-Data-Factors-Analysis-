# CryptoQuant / ETH/Market Data

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (8)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Market Cap - Day.csv` | Market cap | 2015-08-07 .. 2026-04-10 | 3,900 | daily | 0 | 3 | `482797c71d7c` |
| `Ethereum Price & Volume - Spot, All Exchanges, ETH-USD - Day.csv` | Price & volume | 2015-08-07 .. 2026-04-11 | 3,896 | daily | 5 | 7 | `7b7c1ca837df` |
| `Ethereum Price & Volume KRW - Spot - Day.csv` | Price & volume | 2016-04-08 .. 2026-04-10 | 3,654 | daily | 1 | 7 | `e0a14355f4e9` |
| `Ethereum Taker Buy Ratio - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 | `b0139cc16c00` |
| `Ethereum Taker Buy Sell Ratio - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 | `b06998d5e803` |
| `Ethereum Taker Buy Volume - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 | `fb1934506884` |
| `Ethereum Taker Sell Ratio - All Exchanges - Day.csv` | Taker sell volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 | `e1e1888e24c8` |
| `Ethereum Taker Sell Volume - All Exchanges - Day.csv` | Taker sell volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 | `34d6039a9d6b` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Market Cap - Day.csv`**

```csv
date,timestamp_utc,Market Cap
2015-08-07,2015-08-07T00:00:00Z,216839758.68594
2015-08-08,2015-08-08T00:00:00Z,86767989.442116
```

**`Ethereum Price & Volume - Spot, All Exchanges, ETH-USD - Day.csv`**

```csv
date,timestamp_utc,Open,High,Low,Close,Volume
2015-08-07,2015-08-07T00:00:00Z,3.0,3.00001,3.0,3.0,123.93056831
2015-08-08,2015-08-08T00:00:00Z,3.0,3.0,0.15,1.19998,1942.88814724
```

**`Ethereum Price & Volume KRW - Spot - Day.csv`**

```csv
date,timestamp_utc,Open,High,Low,Close,Volume
2016-04-08,2016-04-08T00:00:00Z,14900.0,14900.0,13900.0,13900.0,0.11
2016-04-10,2016-04-10T00:00:00Z,11100.0,11100.0,10900.0,10900.0,4.1512
```

**`Ethereum Taker Buy Ratio - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Taker Buy Ratio
2018-09-01,2018-09-01T00:00:00Z,0.46625366
2018-09-02,2018-09-02T00:00:00Z,0.53911541
```

**`Ethereum Taker Buy Sell Ratio - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Taker Buy Sell Ratio
2018-09-01,2018-09-01T00:00:00Z,0.87354916
2018-09-02,2018-09-02T00:00:00Z,1.16974057
```

**`Ethereum Taker Buy Volume - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Taker Buy Volume
2018-09-01,2018-09-01T00:00:00Z,70580642.82033838
2018-09-02,2018-09-02T00:00:00Z,84837296.9913435
```

**`Ethereum Taker Sell Ratio - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Taker Sell Ratio
2018-09-01,2018-09-01T00:00:00Z,0.53374634
2018-09-02,2018-09-02T00:00:00Z,0.46088459
```

**`Ethereum Taker Sell Volume - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Taker Sell Volume
2018-09-01,2018-09-01T00:00:00Z,80797562.86968024
2018-09-02,2018-09-02T00:00:00Z,72526591.95815454
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
