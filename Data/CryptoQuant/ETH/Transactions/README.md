# CryptoQuant / ETH/Transactions

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (45)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Contract Calls (Mean) - Day.csv` | Ethereum Contract Calls (Mean) - Day | 2015-07-30 .. 2026-04-10 | 3,908 | daily | 0 | 3 | `a1961943dbb5` |
| `Ethereum Contract Calls (Total) - Day.csv` | Ethereum Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `7c125cf51933` |
| `Ethereum External Contract Calls (Mean) - Day.csv` | Ethereum External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `ffe17bb7e356` |
| `Ethereum External Contract Calls (Total) - Day.csv` | Ethereum External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `250f6dd94700` |
| `Ethereum Tokens Transferred (Mean) - Day.csv` | Ethereum Tokens Transferred (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `bf72d2c4b948` |
| `Ethereum Tokens Transferred (Median) - Day.csv` | Ethereum Tokens Transferred (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `d7d27c6f436f` |
| `Ethereum Tokens Transferred (Total) - Day.csv` | Ethereum Tokens Transferred (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `532f3cfe758c` |
| `Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `c3ca090ca8d7` |
| `Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `3bf2263d5d5e` |
| `Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `3109e06d70f0` |
| `Ethereum Tokens Transferred Between EOA (Mean) - Day.csv` | Ethereum Tokens Transferred Between EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `cda42a300532` |
| `Ethereum Tokens Transferred Between EOA (Total) - Day.csv` | Ethereum Tokens Transferred Between EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `48fdc8c04a87` |
| `Ethereum Tokens Transferred Between EOA USD (Mean) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `494a72e54073` |
| `Ethereum Tokens Transferred Between EOA USD (Median) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `44fcbbb70252` |
| `Ethereum Tokens Transferred Between EOA USD (Total) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Total) - Day | 2015-07-30 .. 2026-04-10 | 3,908 | daily | 0 | 3 | `67c82b121470` |
| `Ethereum Tokens Transferred by Contract Calls (Mean) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `c029544cf783` |
| `Ethereum Tokens Transferred by Contract Calls (Median) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `81fff25d94bd` |
| `Ethereum Tokens Transferred by Contract Calls (Total) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `11f5fea8ed14` |
| `Ethereum Tokens Transferred by Contract Calls USD (Mean) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `1421d130b0f3` |
| `Ethereum Tokens Transferred by Contract Calls USD (Median) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `68391ae26f6e` |
| `Ethereum Tokens Transferred by Contract Calls USD (Total) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `65294f072796` |
| `Ethereum Tokens Transferred by External Contract Calls (Mean) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `3502dfae734d` |
| `Ethereum Tokens Transferred by External Contract Calls (Median) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `9b2ed336550a` |
| `Ethereum Tokens Transferred by External Contract Calls (Total) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `ea88313b1c6b` |
| `Ethereum Tokens Transferred by External Contract Calls USD (Mean) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `dd3b8ca875bf` |
| `Ethereum Tokens Transferred by External Contract Calls USD (Median) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Median) - Day | 2024-09-22 .. 2026-04-10 | 566 | daily | 0 | 3 | `f9413a0b3107` |
| `Ethereum Tokens Transferred by External Contract Calls USD (Total) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `5412218408f6` |
| `Ethereum Tokens Transferred USD (Mean) - Day.csv` | Ethereum Tokens Transferred USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `427dc75b3a83` |
| `Ethereum Tokens Transferred USD (Median) - Day.csv` | Ethereum Tokens Transferred USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `e193ae37f12b` |
| `Ethereum Tokens Transferred USD (Total) - Day.csv` | Ethereum Tokens Transferred USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `ec4bf584be85` |
| `Ethereum Tokens Transferred USD - Internal, External, EOA (Mean) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `15ee942b7887` |
| `Ethereum Tokens Transferred USD - Internal, External, EOA (Median) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `cd5f98d5f298` |
| `Ethereum Tokens Transferred USD - Internal, External, EOA (Total) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `90fdb2bd77cd` |
| `Ethereum Transaction Count (Mean) - Day.csv` | Ethereum Transaction Count (Mean) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `307b2361fe3b` |
| `Ethereum Transaction Count (Total) - Day.csv` | Ethereum Transaction Count (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `585ca930807c` |
| `Ethereum Transaction Count - Internal, External, EOA (Total) - Day.csv` | Ethereum Transaction Count - Internal, External, EOA (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 | `fc07a30ce64a` |
| `Ethereum Transactions Between EOA (Mean) - Day.csv` | Ethereum Transactions Between EOA (Mean) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `f2a07b261e04` |
| `Ethereum Transactions Between EOA (Total) - Day.csv` | Ethereum Transactions Between EOA (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `74b28186e2c2` |
| `Ethereum Transfer Count - Internal, External, EOA (Mean) - Day.csv` | Ethereum Transfer Count - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `aabafab189b1` |
| `Ethereum Transfer Count - Internal, External, EOA (Total) - Day.csv` | Ethereum Transfer Count - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 | `fc811ff2c75e` |
| `Ethereum Transfers Between EOA (Mean) - Day.csv` | Ethereum Transfers Between EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `4520b5aa4d8d` |
| `Ethereum Transfers Between EOA (Total) - Day.csv` | Ethereum Transfers Between EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `ab4bdd2a7e96` |
| `Ethereum Transfers by Contract Calls (Mean) - Day.csv` | Ethereum Transfers by Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `114f7adc083d` |
| `Ethereum Transfers by External Contract Calls (Mean) - Day.csv` | Ethereum Transfers by External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `6c67a236b166` |
| `Ethereum Transfers by External Contract Calls (Total) - Day.csv` | Ethereum Transfers by External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 | `cf2c258d4b8c` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Contract Calls (Mean) - Day.csv`**

```csv
date,timestamp_utc,Contract Calls (Mean)
2015-07-30,2015-07-30T00:00:00Z,0.0
2015-07-31,2015-07-31T00:00:00Z,0.0
```

**`Ethereum Contract Calls (Total) - Day.csv`**

```csv
date,timestamp_utc,Contract Calls (Total)
2025-04-11,2025-04-11T00:00:00Z,7500806
2025-04-12,2025-04-12T00:00:00Z,7443384
```

**`Ethereum External Contract Calls (Mean) - Day.csv`**

```csv
date,timestamp_utc,External Contract Calls (Mean)
2025-04-11,2025-04-11T00:00:00Z,112.40928094
2025-04-12,2025-04-12T00:00:00Z,98.1078445
```

**`Ethereum External Contract Calls (Total) - Day.csv`**

```csv
date,timestamp_utc,External Contract Calls (Total)
2025-04-11,2025-04-11T00:00:00Z,806649
2025-04-12,2025-04-12T00:00:00Z,704120
```

**`Ethereum Tokens Transferred (Mean) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Mean)
2025-04-11,2025-04-11T00:00:00Z,3.1719316641534907
2025-04-12,2025-04-12T00:00:00Z,1.6057907503967506
```

**`Ethereum Tokens Transferred (Median) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Median)
2025-04-11,2025-04-11T00:00:00Z,0.0159846420186594
2025-04-12,2025-04-12T00:00:00Z,0.014916685
```

**`Ethereum Tokens Transferred (Total) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Total)
2025-04-11,2025-04-11T00:00:00Z,1843770.9219441488
2025-04-12,2025-04-12T00:00:00Z,867290.7958707858
```

**`Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred - Internal, External, EOA (Mean)
2025-04-11,2025-04-11T00:00:00Z,2.8992988469577483,,
2025-04-12,2025-04-12T00:00:00Z,1.9260737235161287,,
```

**`Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred - Internal, External, EOA (Median)
2025-04-11,2025-04-11T00:00:00Z,0.014,,
2025-04-12,2025-04-12T00:00:00Z,0.0132737606421519,,
```

**`Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred - Internal, External, EOA (Total)
2025-04-11,2025-04-11T00:00:00Z,3074387.5043255268,,
2025-04-12,2025-04-12T00:00:00Z,1912394.7479317177,,
```

**`Ethereum Tokens Transferred Between EOA (Mean) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred Between EOA (Mean)
2025-04-11,2025-04-11T00:00:00Z,3.431882569704737
2025-04-12,2025-04-12T00:00:00Z,1.6856680048199963
```

**`Ethereum Tokens Transferred Between EOA (Total) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred Between EOA (Total)
2025-04-11,2025-04-11T00:00:00Z,1453759.1840572057
2025-04-12,2025-04-12T00:00:00Z,644697.2137874461
```

_(33 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
