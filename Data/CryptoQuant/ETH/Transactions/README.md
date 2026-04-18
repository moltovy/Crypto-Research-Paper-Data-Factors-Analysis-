# CryptoQuant / ETH/Transactions

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (45)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Contract Calls (Mean) - Day.csv` | Ethereum Contract Calls (Mean) - Day | 2015-07-30 .. 2026-04-10 | 3,908 | daily | 0 | 2 | `d092056f96bd` |
| `Ethereum Contract Calls (Total) - Day.csv` | Ethereum Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `93e10d9f9e01` |
| `Ethereum External Contract Calls (Mean) - Day.csv` | Ethereum External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `f0e9959ca3dc` |
| `Ethereum External Contract Calls (Total) - Day.csv` | Ethereum External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `41f3caee40f9` |
| `Ethereum Tokens Transferred (Mean) - Day.csv` | Ethereum Tokens Transferred (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `6962f03cac77` |
| `Ethereum Tokens Transferred (Median) - Day.csv` | Ethereum Tokens Transferred (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `076ec5100082` |
| `Ethereum Tokens Transferred (Total) - Day.csv` | Ethereum Tokens Transferred (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `b8781854d1c3` |
| `Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `c27a16337c12` |
| `Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `179250f39e2f` |
| `Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `30361c51a2c1` |
| `Ethereum Tokens Transferred Between EOA (Mean) - Day.csv` | Ethereum Tokens Transferred Between EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `a2ee9f832bc1` |
| `Ethereum Tokens Transferred Between EOA (Total) - Day.csv` | Ethereum Tokens Transferred Between EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `91f89129ac25` |
| `Ethereum Tokens Transferred Between EOA USD (Mean) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `38c30092f3ef` |
| `Ethereum Tokens Transferred Between EOA USD (Median) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `dad645e3b559` |
| `Ethereum Tokens Transferred Between EOA USD (Total) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Total) - Day | 2015-07-30 .. 2026-04-10 | 3,908 | daily | 0 | 2 | `e1336a47e7d7` |
| `Ethereum Tokens Transferred by Contract Calls (Mean) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `1d6522ec6399` |
| `Ethereum Tokens Transferred by Contract Calls (Median) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `b95ba244a77b` |
| `Ethereum Tokens Transferred by Contract Calls (Total) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `5a026193d527` |
| `Ethereum Tokens Transferred by Contract Calls USD (Mean) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `fe064bf8d078` |
| `Ethereum Tokens Transferred by Contract Calls USD (Median) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `95facc65f302` |
| `Ethereum Tokens Transferred by Contract Calls USD (Total) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `b67ba0c97ddf` |
| `Ethereum Tokens Transferred by External Contract Calls (Mean) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `3a5036a23e39` |
| `Ethereum Tokens Transferred by External Contract Calls (Median) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `77dbeeb41bc7` |
| `Ethereum Tokens Transferred by External Contract Calls (Total) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `0bcbb37e8349` |
| `Ethereum Tokens Transferred by External Contract Calls USD (Mean) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `81558e3e2228` |
| `Ethereum Tokens Transferred by External Contract Calls USD (Median) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Median) - Day | 2024-09-22 .. 2026-04-10 | 566 | daily | 0 | 2 | `9ebfb9d8ca90` |
| `Ethereum Tokens Transferred by External Contract Calls USD (Total) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `c8d2c73be86b` |
| `Ethereum Tokens Transferred USD (Mean) - Day.csv` | Ethereum Tokens Transferred USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `557693077c92` |
| `Ethereum Tokens Transferred USD (Median) - Day.csv` | Ethereum Tokens Transferred USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `17b891cad5b1` |
| `Ethereum Tokens Transferred USD (Total) - Day.csv` | Ethereum Tokens Transferred USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `7451806135ce` |
| `Ethereum Tokens Transferred USD - Internal, External, EOA (Mean) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `99b7be5b8418` |
| `Ethereum Tokens Transferred USD - Internal, External, EOA (Median) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `a9152e2a8bd8` |
| `Ethereum Tokens Transferred USD - Internal, External, EOA (Total) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `f23400d60428` |
| `Ethereum Transaction Count (Mean) - Day.csv` | Ethereum Transaction Count (Mean) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `cd65252b124f` |
| `Ethereum Transaction Count (Total) - Day.csv` | Ethereum Transaction Count (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `f1f2c34d2dad` |
| `Ethereum Transaction Count - Internal, External, EOA (Total) - Day.csv` | Ethereum Transaction Count - Internal, External, EOA (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 4 | `165dccda84e4` |
| `Ethereum Transactions Between EOA (Mean) - Day.csv` | Ethereum Transactions Between EOA (Mean) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `607b1e4ffcfd` |
| `Ethereum Transactions Between EOA (Total) - Day.csv` | Ethereum Transactions Between EOA (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `e73a912732fa` |
| `Ethereum Transfer Count - Internal, External, EOA (Mean) - Day.csv` | Ethereum Transfer Count - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `63997c39a0b2` |
| `Ethereum Transfer Count - Internal, External, EOA (Total) - Day.csv` | Ethereum Transfer Count - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 4 | `4e1aba5024e2` |
| `Ethereum Transfers Between EOA (Mean) - Day.csv` | Ethereum Transfers Between EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `876931abcd80` |
| `Ethereum Transfers Between EOA (Total) - Day.csv` | Ethereum Transfers Between EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `361230273d53` |
| `Ethereum Transfers by Contract Calls (Mean) - Day.csv` | Ethereum Transfers by Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `3af42686f200` |
| `Ethereum Transfers by External Contract Calls (Mean) - Day.csv` | Ethereum Transfers by External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `510d11d47fd6` |
| `Ethereum Transfers by External Contract Calls (Total) - Day.csv` | Ethereum Transfers by External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 2 | `92c5b60815d0` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Contract Calls (Mean) - Day.csv`**

```csv
date,Contract Calls (Mean)
2015-07-30,0.0
2015-07-31,0.0
```

**`Ethereum Contract Calls (Total) - Day.csv`**

```csv
date,Contract Calls (Total)
2025-04-11,7500806
2025-04-12,7443384
```

**`Ethereum External Contract Calls (Mean) - Day.csv`**

```csv
date,External Contract Calls (Mean)
2025-04-11,112.40928094
2025-04-12,98.1078445
```

**`Ethereum External Contract Calls (Total) - Day.csv`**

```csv
date,External Contract Calls (Total)
2025-04-11,806649
2025-04-12,704120
```

**`Ethereum Tokens Transferred (Mean) - Day.csv`**

```csv
date,Tokens Transferred (Mean)
2025-04-11,3.1719316641534907
2025-04-12,1.6057907503967506
```

**`Ethereum Tokens Transferred (Median) - Day.csv`**

```csv
date,Tokens Transferred (Median)
2025-04-11,0.0159846420186594
2025-04-12,0.014916685
```

**`Ethereum Tokens Transferred (Total) - Day.csv`**

```csv
date,Tokens Transferred (Total)
2025-04-11,1843770.9219441488
2025-04-12,867290.7958707858
```

**`Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day.csv`**

```csv
date,Tokens Transferred - Internal, External, EOA (Mean)
2025-04-11,2.8992988469577483,,
2025-04-12,1.9260737235161287,,
```

**`Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day.csv`**

```csv
date,Tokens Transferred - Internal, External, EOA (Median)
2025-04-11,0.014,,
2025-04-12,0.0132737606421519,,
```

**`Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day.csv`**

```csv
date,Tokens Transferred - Internal, External, EOA (Total)
2025-04-11,3074387.5043255268,,
2025-04-12,1912394.7479317177,,
```

**`Ethereum Tokens Transferred Between EOA (Mean) - Day.csv`**

```csv
date,Tokens Transferred Between EOA (Mean)
2025-04-11,3.431882569704737
2025-04-12,1.6856680048199963
```

**`Ethereum Tokens Transferred Between EOA (Total) - Day.csv`**

```csv
date,Tokens Transferred Between EOA (Total)
2025-04-11,1453759.1840572057
2025-04-12,644697.2137874461
```

_(33 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
