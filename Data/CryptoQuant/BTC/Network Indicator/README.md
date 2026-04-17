# CryptoQuant / BTC/Network Indicator

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (14)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Coin Days Destroyed (CDD) - Day.csv` | Bitcoin Coin Days Destroyed (CDD) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `19db2d44360d` |
| `Bitcoin UTXO Age Bands (%) - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `a454c56ce130` |
| `Bitcoin UTXO Age Bands - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `f4a90c69ca0a` |
| `Bitcoin UTXO Age Bands USD - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `946c1864f680` |
| `Bitcoin UTXO Count - Age Bands (%) - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `d8ec60f3e82b` |
| `Bitcoin UTXO Count - Age Bands - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `25d7a59a6bb6` |
| `Bitcoin UTXO Count - Value Bands (%) - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 9 | `f6f7663ef841` |
| `Bitcoin UTXO Count - Value Bands - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 9 | `2e73c11dda46` |
| `Bitcoin UTXO Value Bands (%) - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 9 | `daaee4ca07fe` |
| `Bitcoin UTXO Value Bands - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 9 | `331142443b4b` |
| `Bitcoin UTXOs in Loss (%) - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `059afc336c04` |
| `Bitcoin UTXOs in Loss - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `ecc11c1662be` |
| `Bitcoin UTXOs in Profit (%) - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `b99fd39ab948` |
| `Bitcoin UTXOs in Profit - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `55dc75303669` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Coin Days Destroyed (CDD) - Day.csv`**

```csv
date,Coin Days Destroyed (CDD)
2020-12-31,19113095.80380446
2021-01-01,24065893.89497589
```

**`Bitcoin UTXO Age Bands (%) - Day.csv`**

```csv
date,0d ~ 1d (%),1d ~ 1w (%),1w ~ 1m (%),1m ~ 3m (%),3m ~ 6m (%),6m ~ 12m (%),12m ~ 18m (%),18m ~ 2y (%),2y ~ 3y (%),... (+4 more)
2009-01-03,100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin UTXO Age Bands - Day.csv`**

```csv
date,0d ~ 1d,1d ~ 1w,1w ~ 1m,1m ~ 3m,3m ~ 6m,6m ~ 12m,12m ~ 18m,18m ~ 2y,2y ~ 3y,... (+4 more)
2009-01-03,50.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,50.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin UTXO Age Bands USD - Day.csv`**

```csv
date,0d ~ 1d,1d ~ 1w,1w ~ 1m,1m ~ 3m,3m ~ 6m,6m ~ 12m,12m ~ 18m,18m ~ 2y,2y ~ 3y,... (+4 more)
2009-01-03,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin UTXO Count - Age Bands (%) - Day.csv`**

```csv
date,0d ~ 1d (%),1d ~ 1w (%),1w ~ 1m (%),1m ~ 3m (%),3m ~ 6m (%),6m ~ 12m (%),12m ~ 18m (%),18m ~ 2y (%),2y ~ 3y (%),... (+4 more)
2009-01-03,100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin UTXO Count - Age Bands - Day.csv`**

```csv
date,0d ~ 1d,1d ~ 1w,1w ~ 1m,1m ~ 3m,3m ~ 6m,6m ~ 12m,12m ~ 18m,18m ~ 2y,2y ~ 3y,... (+4 more)
2009-01-03,1,0,0,0,0,0,0,0,0
2009-01-04,1,0,0,0,0,0,0,0,0
```

**`Bitcoin UTXO Count - Value Bands (%) - Day.csv`**

```csv
date,0 ~ 0.01 BTC (%),0.01 ~ 0.1 BTC (%),0.1 ~ 1 BTC (%),1 ~ 10 BTC (%),10 ~ 100 BTC (%),100 ~ 1K BTC (%),1K ~ 10K BTC (%),10K BTC ~ (%)
2009-01-03,0.0,0.0,0.0,0.0,100.0,0.0,0.0,0.0
2009-01-04,0.0,0.0,0.0,0.0,100.0,0.0,0.0,0.0
```

**`Bitcoin UTXO Count - Value Bands - Day.csv`**

```csv
date,0 ~ 0.01 BTC,0.01 ~ 0.1 BTC,0.1 ~ 1 BTC,1 ~ 10 BTC,10 ~ 100 BTC,100 ~ 1K BTC,1K ~ 10K BTC,10K ~ BTC
2020-12-31,103627476,8196554,2911959,804146,147172,20736,1938,50
2021-01-01,103471445,8160006,2913189,805172,147035,20766,1948,50
```

**`Bitcoin UTXO Value Bands (%) - Day.csv`**

```csv
date,0 ~ 0.01 BTC (%),0.01 ~ 0.1 BTC (%),0.1 ~ 1 BTC (%),1 ~ 10 BTC (%),10 ~ 100 BTC (%),100 ~ 1K BTC (%),1K ~ 10K BTC (%),10K BTC ~ (%)
2020-12-31,0.32098712,1.36782679,4.80792787,11.11270815,25.39363222,27.08627302,22.43521086,7.47543396
2021-01-01,0.3191993,1.36244637,4.81155769,11.12160934,25.37931651,27.13032257,22.42447899,7.45106922
```

**`Bitcoin UTXO Value Bands - Day.csv`**

```csv
date,0 ~ 0.01 BTC,0.01 ~ 0.1 BTC,0.1 ~ 1 BTC,1 ~ 10 BTC,10 ~ 100 BTC,100 ~ 1K BTC,1K ~ 10K BTC,10K ~ BTC
2020-12-31,59661.64235863,254236.97138614,893646.05757446,2065510.98522389,4719895.95877106,5034505.87273878,4170016.33183877,1389453.47507923
2021-01-01,59332.31496285,253249.60325126,894365.53787855,2067269.01188744,4717471.45344671,5042945.98214158,4168230.43387064,1384994.20753193
```

**`Bitcoin UTXOs in Loss (%) - Day.csv`**

```csv
date,UTXOs in Loss (%)
2020-12-31,0.17239588
2021-01-01,0.07228353
```

**`Bitcoin UTXOs in Loss - Day.csv`**

```csv
date,UTXOs in Loss
2020-12-31,199473
2021-01-01,83499
```

_(2 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
