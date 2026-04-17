# CryptoQuant / BTC/Market Indicator

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (39)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Adjusted SOPR (aSOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `76c276649bc2` |
| `Bitcoin Average Dormancy - Day.csv` | Bitcoin Average Dormancy - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `cf6d85b972a7` |
| `Bitcoin Average Supply-Adjusted CDD - Day.csv` | Bitcoin Average Supply-Adjusted CDD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `39b3d31aa16c` |
| `Bitcoin Binary CDD - Day.csv` | Bitcoin Binary CDD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `c743bdb390b8` |
| `Bitcoin Long Term Holder SOPR - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `43e6cd959a27` |
| `Bitcoin Mean Coin Age - Day.csv` | Bitcoin Mean Coin Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `60529c96db22` |
| `Bitcoin Mean Coin Dollar Age - Day.csv` | Bitcoin Mean Coin Dollar Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `269f9278e854` |
| `Bitcoin MVRV Ratio - Day.csv` | MVRV ratio | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `a1effd437db9` |
| `Bitcoin Net Unrealized Loss (NUL) - Day.csv` | Bitcoin Net Unrealized Loss (NUL) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `3998a67b4543` |
| `Bitcoin Net Unrealized Profit (NUP) - Day.csv` | Bitcoin Net Unrealized Profit (NUP) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `efd90da16a9c` |
| `Bitcoin Net Unrealized Profit_Loss (NUPL) - Day.csv` | NUPL | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `a9866343bfe1` |
| `Bitcoin NVM Ratio - Day.csv` | Bitcoin NVM Ratio - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `abd925c438ac` |
| `Bitcoin NVT Golden Cross - Day.csv` | NVT | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `9010c2d5f93d` |
| `Bitcoin NVT Ratio - Day.csv` | NVT | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `bb76549bcaba` |
| `Bitcoin Puell Multiple - Day.csv` | Puell multiple | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `fcb3c544e84f` |
| `Bitcoin Realized Price - Day.csv` | Realized price | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `44af6911db96` |
| `Bitcoin Realized Price - UTXO Age Bands - Day.csv` | Realized price | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `f0baa533c4ad` |
| `Bitcoin Short Term Holder SOPR - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `a323b9577e5e` |
| `Bitcoin SOPR Ratio (LTH-SOPR_STH-SOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `0f19c9076fba` |
| `Bitcoin Spent Output Age Bands (%) - Day.csv` | Bitcoin Spent Output Age Bands (%) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `3ec6f1169f1f` |
| `Bitcoin Spent Output Age Bands - Day.csv` | Bitcoin Spent Output Age Bands - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 14 | `8572f18f8e78` |
| `Bitcoin Spent Output Age Bands USD - Day.csv` | Bitcoin Spent Output Age Bands USD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `a35a3a74fa55` |
| `Bitcoin Spent Output Profit Ratio (SOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `55776a99d958` |
| `Bitcoin Spent Output Value Bands (%) - Day.csv` | Bitcoin Spent Output Value Bands (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 9 | `e86048dc8a7f` |
| `Bitcoin Spent Output Value Bands - Day.csv` | Bitcoin Spent Output Value Bands - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 9 | `5da438878760` |
| `Bitcoin Spent Output Value Bands USD - Day.csv` | Bitcoin Spent Output Value Bands USD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 9 | `e62f67bda2a3` |
| `Bitcoin Spot Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2017-01-01 .. 2026-04-11 | 3,388 | daily | 0 | 4 | `77f5fef5dc47` |
| `Bitcoin Stock-to-Flow Ratio - Day.csv` | Bitcoin Stock-to-Flow Ratio - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `c2a42c5bdfe3` |
| `Bitcoin Stock-to-Flow Reversion - Day.csv` | Bitcoin Stock-to-Flow Reversion - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `4c3f869f5e9f` |
| `Bitcoin Sum Coin Age - Day.csv` | Bitcoin Sum Coin Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `17f3bc1e11ce` |
| `Bitcoin Sum Coin Age Distribution (%) - Day.csv` | Bitcoin Sum Coin Age Distribution (%) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `bd88490ea836` |
| `Bitcoin Sum Coin Age Distribution - Day.csv` | Bitcoin Sum Coin Age Distribution - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 14 | `f13a588df6ea` |
| `Bitcoin Sum Coin Dollar Age - Day.csv` | Bitcoin Sum Coin Dollar Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `44db5010f8c9` |
| `Bitcoin Supply Adjusted Dormancy - Day.csv` | Bitcoin Supply Adjusted Dormancy - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `391c7129c089` |
| `Bitcoin Supply in Loss (%) - Day.csv` | Bitcoin Supply in Loss (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `f87ad9ab46d0` |
| `Bitcoin Supply in Loss - Day.csv` | Bitcoin Supply in Loss - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `a0bc22aba2c4` |
| `Bitcoin Supply in Profit (%) - Day.csv` | Bitcoin Supply in Profit (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `ffa459b79431` |
| `Bitcoin Supply in Profit - Day.csv` | Bitcoin Supply in Profit - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `2aa17572e0e7` |
| `Bitcoin Supply-Adjusted CDD - Day.csv` | Bitcoin Supply-Adjusted CDD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `b0bdc88bed02` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Adjusted SOPR (aSOPR) - Day.csv`**

```csv
date,Adjusted SOPR (aSOPR)
2009-01-03,
2009-01-04,
```

**`Bitcoin Average Dormancy - Day.csv`**

```csv
date,Average Dormancy
2020-12-31,9.82981928
2021-01-01,15.01804685
```

**`Bitcoin Average Supply-Adjusted CDD - Day.csv`**

```csv
date,Average Supply-Adjusted CDD
2020-12-31,0.51305219
2021-01-01,0.51323057
```

**`Bitcoin Binary CDD - Day.csv`**

```csv
date,Binary CDD
2009-01-03,0
2009-01-04,0
```

**`Bitcoin Long Term Holder SOPR - Day.csv`**

```csv
date,Long Term Holder SOPR
2009-01-03,
2009-01-04,
```

**`Bitcoin Mean Coin Age - Day.csv`**

```csv
date,Mean Coin Age
2020-12-31,1118.53347501
2021-01-01,1118.18331516
```

**`Bitcoin Mean Coin Dollar Age - Day.csv`**

```csv
date,Mean Coin Dollar Age
2020-12-31,2481022.16670295
2021-01-01,2479412.61512363
```

**`Bitcoin MVRV Ratio - Day.csv`**

```csv
date,MVRV Ratio
2009-01-03,
2009-01-04,
```

**`Bitcoin Net Unrealized Loss (NUL) - Day.csv`**

```csv
date,Net Unrealized Loss (NUL)
2020-12-31,1.305e-05
2021-01-01,9.95e-06
```

**`Bitcoin Net Unrealized Profit (NUP) - Day.csv`**

```csv
date,Net Unrealized Profit (NUP)
2020-12-31,0.68440472
2021-01-01,0.68348719
```

**`Bitcoin Net Unrealized Profit_Loss (NUPL) - Day.csv`**

```csv
date,Net Unrealized Profit/Loss (NUPL)
2020-12-31,0.68229199
2021-01-01,0.68363813
```

**`Bitcoin NVM Ratio - Day.csv`**

```csv
date,NVM Ratio
2020-12-31,0.37138593
2021-01-01,0.55061113
```

_(27 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
