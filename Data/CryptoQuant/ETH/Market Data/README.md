# CryptoQuant / ETH/Market Data

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
| `Ethereum Market Cap - Day.csv` | Market cap | 2015-08-07 .. 2026-04-10 | 3,900 | daily | 0 | 2 | `d809f72a4315` |
| `Ethereum Price & Volume - Spot, All Exchanges, ETH-USD - Day.csv` | Price & volume | 2015-08-07 .. 2026-04-11 | 3,896 | daily | 5 | 6 | `09a19aead312` |
| `Ethereum Price & Volume KRW - Spot - Day.csv` | Price & volume | 2016-04-08 .. 2026-04-10 | 3,654 | daily | 1 | 6 | `f3a0889eb1fa` |
| `Ethereum Taker Buy Ratio - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 2 | `a6e5366d6bf6` |
| `Ethereum Taker Buy Sell Ratio - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 2 | `ae39f0d56e95` |
| `Ethereum Taker Buy Volume - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 2 | `8c7eac4efdae` |
| `Ethereum Taker Sell Ratio - All Exchanges - Day.csv` | Taker sell volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 2 | `f5e2319d6657` |
| `Ethereum Taker Sell Volume - All Exchanges - Day.csv` | Taker sell volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 2 | `70576ba943bd` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Market Cap - Day.csv`**

```csv
date,Market Cap
2015-08-07,216839758.68594
2015-08-08,86767989.442116
```

**`Ethereum Price & Volume - Spot, All Exchanges, ETH-USD - Day.csv`**

```csv
date,Open,High,Low,Close,Volume
2015-08-07,3.0,3.00001,3.0,3.0,123.93056831
2015-08-08,3.0,3.0,0.15,1.19998,1942.88814724
```

**`Ethereum Price & Volume KRW - Spot - Day.csv`**

```csv
date,Open,High,Low,Close,Volume
2016-04-08,14900.0,14900.0,13900.0,13900.0,0.11
2016-04-10,11100.0,11100.0,10900.0,10900.0,4.1512
```

**`Ethereum Taker Buy Ratio - All Exchanges - Day.csv`**

```csv
date,Taker Buy Ratio
2018-09-01,0.46625366
2018-09-02,0.53911541
```

**`Ethereum Taker Buy Sell Ratio - All Exchanges - Day.csv`**

```csv
date,Taker Buy Sell Ratio
2018-09-01,0.87354916
2018-09-02,1.16974057
```

**`Ethereum Taker Buy Volume - All Exchanges - Day.csv`**

```csv
date,Taker Buy Volume
2018-09-01,70580642.82033838
2018-09-02,84837296.9913435
```

**`Ethereum Taker Sell Ratio - All Exchanges - Day.csv`**

```csv
date,Taker Sell Ratio
2018-09-01,0.53374634
2018-09-02,0.46088459
```

**`Ethereum Taker Sell Volume - All Exchanges - Day.csv`**

```csv
date,Taker Sell Volume
2018-09-01,80797562.86968024
2018-09-02,72526591.95815454
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
