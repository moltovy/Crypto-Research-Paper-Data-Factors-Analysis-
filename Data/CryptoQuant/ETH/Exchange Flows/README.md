# CryptoQuant / ETH/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (13)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Exchange Depositing Addresses - All Exchanges - Day.csv` | Ethereum Exchange Depositing Addresses - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 | `5a59295ade47` |
| `Ethereum Exchange Depositing Transactions - All Exchanges - Day.csv` | Ethereum Exchange Depositing Transactions - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 | `f4eb49f73d90` |
| `Ethereum Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 | `a76198b2d922` |
| `Ethereum Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 | `2fb852366dd6` |
| `Ethereum Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 | `f87d88253b17` |
| `Ethereum Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 | `2a0c6ababe11` |
| `Ethereum Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 | `67beacf180e2` |
| `Ethereum Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 | `ed3c3fa3245f` |
| `Ethereum Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 | `2847f31773db` |
| `Ethereum Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 | `ffba03455608` |
| `Ethereum Exchange Reserve USD - All Exchanges - Day.csv` | Exchange reserve | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 | `d270646bc825` |
| `Ethereum Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Ethereum Exchange Withdrawing Addresses - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 | `2245b63d413e` |
| `Ethereum Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Ethereum Exchange Withdrawing Transactions - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 | `50ecfd397f1e` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Addresses
2015-08-07,2015-08-07T00:00:00Z,521
2015-08-08,2015-08-08T00:00:00Z,315
```

**`Ethereum Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Transactions
2015-08-07,2015-08-07T00:00:00Z,972
2015-08-08,2015-08-08T00:00:00Z,533
```

**`Ethereum Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Mean)
2015-08-13,2015-08-13T00:00:00Z,1205.30688035
2015-08-14,2015-08-14T00:00:00Z,1352.59822787
```

**`Ethereum Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Top10)
2015-08-13,2015-08-13T00:00:00Z,599999.99253232
2015-08-14,2015-08-14T00:00:00Z,742268.87752263
```

**`Ethereum Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Total)
2015-08-13,2015-08-13T00:00:00Z,1053438.2134284982
2015-08-14,2015-08-14T00:00:00Z,1481095.059515229
```

**`Ethereum Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Netflow (Total)
2015-08-07,2015-08-07T00:00:00Z,1435993.8023820375
2015-08-08,2015-08-08T00:00:00Z,847425.7133057117
```

**`Ethereum Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Mean)
2015-08-13,2015-08-13T00:00:00Z,573.56785581
2015-08-14,2015-08-14T00:00:00Z,511.42644525
```

**`Ethereum Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Top10)
2015-08-13,2015-08-13T00:00:00Z,448121.20189831
2015-08-14,2015-08-14T00:00:00Z,370784.37758
```

**`Ethereum Exchange Outflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Total)
2015-08-13,2015-08-13T00:00:00Z,634366.0485250115
2015-08-14,2015-08-14T00:00:00Z,549783.4286395242
```

**`Ethereum Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Reserve
2015-08-07,2015-08-07T00:00:00Z,1435993.8023820375
2015-08-08,2015-08-08T00:00:00Z,2283419.5156877493
```

**`Ethereum Exchange Reserve USD - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Reserve USD
2015-08-07,2015-08-07T00:00:00Z,445158.0787384317
2015-08-08,2015-08-08T00:00:00Z,6850258.547063248
```

**`Ethereum Exchange Withdrawing Addresses - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Withdrawing Addresses
2015-08-07,2015-08-07T00:00:00Z,3
2015-08-08,2015-08-08T00:00:00Z,58
```

_(1 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
