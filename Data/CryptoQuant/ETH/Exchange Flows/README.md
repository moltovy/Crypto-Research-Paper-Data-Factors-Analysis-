# CryptoQuant / ETH/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (13)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Exchange Depositing Addresses - All Exchanges - Day.csv` | Ethereum Exchange Depositing Addresses - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 2 | `b6a194b19d69` |
| `Ethereum Exchange Depositing Transactions - All Exchanges - Day.csv` | Ethereum Exchange Depositing Transactions - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 2 | `565b1b052105` |
| `Ethereum Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 2 | `c1256e45c42b` |
| `Ethereum Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 2 | `ca059c408134` |
| `Ethereum Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 2 | `c9cd9fab0b9b` |
| `Ethereum Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 2 | `7811dbb11d16` |
| `Ethereum Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 2 | `e7f25e71f9ed` |
| `Ethereum Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 2 | `86823263bb43` |
| `Ethereum Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 2 | `1b7c62d948a3` |
| `Ethereum Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 2 | `740f676e75cb` |
| `Ethereum Exchange Reserve USD - All Exchanges - Day.csv` | Exchange reserve | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 2 | `b9de8190db81` |
| `Ethereum Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Ethereum Exchange Withdrawing Addresses - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 2 | `7fa973f1338c` |
| `Ethereum Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Ethereum Exchange Withdrawing Transactions - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 2 | `51cf7283a7d8` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Addresses
2015-08-07,521
2015-08-08,315
```

**`Ethereum Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Transactions
2015-08-07,972
2015-08-08,533
```

**`Ethereum Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Mean)
2015-08-13,1205.30688035
2015-08-14,1352.59822787
```

**`Ethereum Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Top10)
2015-08-13,599999.99253232
2015-08-14,742268.87752263
```

**`Ethereum Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Total)
2015-08-13,1053438.2134284982
2015-08-14,1481095.059515229
```

**`Ethereum Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Netflow (Total)
2015-08-07,1435993.8023820375
2015-08-08,847425.7133057117
```

**`Ethereum Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Mean)
2015-08-13,573.56785581
2015-08-14,511.42644525
```

**`Ethereum Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Top10)
2015-08-13,448121.20189831
2015-08-14,370784.37758
```

**`Ethereum Exchange Outflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Total)
2015-08-13,634366.0485250115
2015-08-14,549783.4286395242
```

**`Ethereum Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,Exchange Reserve
2015-08-07,1435993.8023820375
2015-08-08,2283419.5156877493
```

**`Ethereum Exchange Reserve USD - All Exchanges - Day.csv`**

```csv
date,Exchange Reserve USD
2015-08-07,445158.0787384317
2015-08-08,6850258.547063248
```

**`Ethereum Exchange Withdrawing Addresses - All Exchanges - Day.csv`**

```csv
date,Exchange Withdrawing Addresses
2015-08-07,3
2015-08-08,58
```

_(1 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
