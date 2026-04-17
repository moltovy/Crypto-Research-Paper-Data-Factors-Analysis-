# CryptoQuant / BTC/Market Indicator

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (39)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Adjusted SOPR (aSOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `645f9474f8fe` |
| `Bitcoin Average Dormancy - Day.csv` | Bitcoin Average Dormancy - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `b4807df63ae6` |
| `Bitcoin Average Supply-Adjusted CDD - Day.csv` | Bitcoin Average Supply-Adjusted CDD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `ef28e1e8dd43` |
| `Bitcoin Binary CDD - Day.csv` | Bitcoin Binary CDD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `82372568ed1e` |
| `Bitcoin Long Term Holder SOPR - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `d53c1a17119f` |
| `Bitcoin Mean Coin Age - Day.csv` | Bitcoin Mean Coin Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `e24f8a322fdb` |
| `Bitcoin Mean Coin Dollar Age - Day.csv` | Bitcoin Mean Coin Dollar Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `2188c4c134ab` |
| `Bitcoin MVRV Ratio - Day.csv` | MVRV ratio | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `3e9275d78e8d` |
| `Bitcoin Net Unrealized Loss (NUL) - Day.csv` | Bitcoin Net Unrealized Loss (NUL) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `b5c25cb01f35` |
| `Bitcoin Net Unrealized Profit (NUP) - Day.csv` | Bitcoin Net Unrealized Profit (NUP) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `efbb97a06d68` |
| `Bitcoin Net Unrealized Profit_Loss (NUPL) - Day.csv` | NUPL | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `c1df3913c86b` |
| `Bitcoin NVM Ratio - Day.csv` | Bitcoin NVM Ratio - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `a69a87cf084b` |
| `Bitcoin NVT Golden Cross - Day.csv` | NVT | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `22599ffb9170` |
| `Bitcoin NVT Ratio - Day.csv` | NVT | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `814597130856` |
| `Bitcoin Puell Multiple - Day.csv` | Puell multiple | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `311c02ba47b2` |
| `Bitcoin Realized Price - Day.csv` | Realized price | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `5df553097577` |
| `Bitcoin Realized Price - UTXO Age Bands - Day.csv` | Realized price | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 | `5e27ab0ad43b` |
| `Bitcoin Short Term Holder SOPR - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `050c94fc8abb` |
| `Bitcoin SOPR Ratio (LTH-SOPR_STH-SOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `2d4f39991d76` |
| `Bitcoin Spent Output Age Bands (%) - Day.csv` | Bitcoin Spent Output Age Bands (%) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 | `460d618e4a63` |
| `Bitcoin Spent Output Age Bands - Day.csv` | Bitcoin Spent Output Age Bands - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 15 | `e8cb43e6ad12` |
| `Bitcoin Spent Output Age Bands USD - Day.csv` | Bitcoin Spent Output Age Bands USD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 | `898a96a7ae03` |
| `Bitcoin Spent Output Profit Ratio (SOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `40c9e98659f0` |
| `Bitcoin Spent Output Value Bands (%) - Day.csv` | Bitcoin Spent Output Value Bands (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 | `0a74ee15d13a` |
| `Bitcoin Spent Output Value Bands - Day.csv` | Bitcoin Spent Output Value Bands - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 | `f9888936873a` |
| `Bitcoin Spent Output Value Bands USD - Day.csv` | Bitcoin Spent Output Value Bands USD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 | `65717fe72d4c` |
| `Bitcoin Spot Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2017-01-01 .. 2026-04-11 | 3,388 | daily | 0 | 5 | `a54742dc27ef` |
| `Bitcoin Stock-to-Flow Ratio - Day.csv` | Bitcoin Stock-to-Flow Ratio - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `8608f3e15405` |
| `Bitcoin Stock-to-Flow Reversion - Day.csv` | Bitcoin Stock-to-Flow Reversion - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `72093cbabd91` |
| `Bitcoin Sum Coin Age - Day.csv` | Bitcoin Sum Coin Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `a5538de61f6d` |
| `Bitcoin Sum Coin Age Distribution (%) - Day.csv` | Bitcoin Sum Coin Age Distribution (%) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 | `2f64acd81af6` |
| `Bitcoin Sum Coin Age Distribution - Day.csv` | Bitcoin Sum Coin Age Distribution - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 15 | `2183c53e5d65` |
| `Bitcoin Sum Coin Dollar Age - Day.csv` | Bitcoin Sum Coin Dollar Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `c7660434d93a` |
| `Bitcoin Supply Adjusted Dormancy - Day.csv` | Bitcoin Supply Adjusted Dormancy - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `fd5cc7cb7e36` |
| `Bitcoin Supply in Loss (%) - Day.csv` | Bitcoin Supply in Loss (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `b479b9078188` |
| `Bitcoin Supply in Loss - Day.csv` | Bitcoin Supply in Loss - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `472d0bff65ae` |
| `Bitcoin Supply in Profit (%) - Day.csv` | Bitcoin Supply in Profit (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `eda5c3c981f4` |
| `Bitcoin Supply in Profit - Day.csv` | Bitcoin Supply in Profit - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `465c9e570584` |
| `Bitcoin Supply-Adjusted CDD - Day.csv` | Bitcoin Supply-Adjusted CDD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 | `0b237a1af19b` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Adjusted SOPR (aSOPR) - Day.csv`**

```csv
date,timestamp_utc,Adjusted SOPR (aSOPR)
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Average Dormancy - Day.csv`**

```csv
date,timestamp_utc,Average Dormancy
2020-12-31,2020-12-31T00:00:00Z,9.82981928
2021-01-01,2021-01-01T00:00:00Z,15.01804685
```

**`Bitcoin Average Supply-Adjusted CDD - Day.csv`**

```csv
date,timestamp_utc,Average Supply-Adjusted CDD
2020-12-31,2020-12-31T00:00:00Z,0.51305219
2021-01-01,2021-01-01T00:00:00Z,0.51323057
```

**`Bitcoin Binary CDD - Day.csv`**

```csv
date,timestamp_utc,Binary CDD
2009-01-03,2009-01-03T00:00:00Z,0
2009-01-04,2009-01-04T00:00:00Z,0
```

**`Bitcoin Long Term Holder SOPR - Day.csv`**

```csv
date,timestamp_utc,Long Term Holder SOPR
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Mean Coin Age - Day.csv`**

```csv
date,timestamp_utc,Mean Coin Age
2020-12-31,2020-12-31T00:00:00Z,1118.53347501
2021-01-01,2021-01-01T00:00:00Z,1118.18331516
```

**`Bitcoin Mean Coin Dollar Age - Day.csv`**

```csv
date,timestamp_utc,Mean Coin Dollar Age
2020-12-31,2020-12-31T00:00:00Z,2481022.16670295
2021-01-01,2021-01-01T00:00:00Z,2479412.61512363
```

**`Bitcoin MVRV Ratio - Day.csv`**

```csv
date,timestamp_utc,MVRV Ratio
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Net Unrealized Loss (NUL) - Day.csv`**

```csv
date,timestamp_utc,Net Unrealized Loss (NUL)
2020-12-31,2020-12-31T00:00:00Z,1.305e-05
2021-01-01,2021-01-01T00:00:00Z,9.95e-06
```

**`Bitcoin Net Unrealized Profit (NUP) - Day.csv`**

```csv
date,timestamp_utc,Net Unrealized Profit (NUP)
2020-12-31,2020-12-31T00:00:00Z,0.68440472
2021-01-01,2021-01-01T00:00:00Z,0.68348719
```

**`Bitcoin Net Unrealized Profit_Loss (NUPL) - Day.csv`**

```csv
date,timestamp_utc,Net Unrealized Profit/Loss (NUPL)
2020-12-31,2020-12-31T00:00:00Z,0.68229199
2021-01-01,2021-01-01T00:00:00Z,0.68363813
```

**`Bitcoin NVM Ratio - Day.csv`**

```csv
date,timestamp_utc,NVM Ratio
2020-12-31,2020-12-31T00:00:00Z,0.37138593
2021-01-01,2021-01-01T00:00:00Z,0.55061113
```

_(27 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
