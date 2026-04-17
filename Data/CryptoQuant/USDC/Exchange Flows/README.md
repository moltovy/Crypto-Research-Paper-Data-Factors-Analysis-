# CryptoQuant / USDC/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (12)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `4ec998652903` |
| `USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `1930047a90ad` |
| `USD Coin(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `992ec020d1d2` |
| `USD Coin(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `e1f93a1da72a` |
| `USD Coin(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 3 | `299f1160a142` |
| `USD Coin(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `1501c36c5fef` |
| `USD Coin(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `4cf36cf8a6e6` |
| `USD Coin(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `b61580bbaa99` |
| `USD Coin(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 3 | `439ebb7eb846` |
| `USD Coin(ERC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 3 | `5101dac065a9` |
| `USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `b6dfe17c183d` |
| `USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 | `6486a937500f` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Addresses
2018-09-12,2018-09-12T00:00:00Z,1
2018-09-13,2018-09-13T00:00:00Z,0
```

**`USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Transactions
2018-09-12,2018-09-12T00:00:00Z,1
2018-09-13,2018-09-13T00:00:00Z,0
```

**`USD Coin(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Mean)
2018-09-12,2018-09-12T00:00:00Z,1.0
2018-09-13,2018-09-13T00:00:00Z,0.0
```

**`USD Coin(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Top10)
2018-09-12,2018-09-12T00:00:00Z,1.0
2018-09-13,2018-09-13T00:00:00Z,0.0
```

**`USD Coin(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Total)
2018-09-12,2018-09-12T00:00:00Z,1.0
2018-09-13,2018-09-13T00:00:00Z,0.0
```

**`USD Coin(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Netflow (Total)
2018-09-12,2018-09-12T00:00:00Z,0.6
2018-09-13,2018-09-13T00:00:00Z,0.0
```

**`USD Coin(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Mean)
2018-09-12,2018-09-12T00:00:00Z,0.4
2018-09-13,2018-09-13T00:00:00Z,0.0
```

**`USD Coin(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Top10)
2018-09-12,2018-09-12T00:00:00Z,0.4
2018-09-13,2018-09-13T00:00:00Z,0.0
```

**`USD Coin(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Total)
2018-09-12,2018-09-12T00:00:00Z,0.4
2018-09-13,2018-09-13T00:00:00Z,0.0
```

**`USD Coin(ERC20) Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Reserve
2018-09-12,2018-09-12T00:00:00Z,0.6
2018-09-13,2018-09-13T00:00:00Z,0.6
```

**`USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Withdrawing Addresses
2018-09-12,2018-09-12T00:00:00Z,1
2018-09-13,2018-09-13T00:00:00Z,0
```

**`USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Withdrawing Transactions
2018-09-12,2018-09-12T00:00:00Z,1
2018-09-13,2018-09-13T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
