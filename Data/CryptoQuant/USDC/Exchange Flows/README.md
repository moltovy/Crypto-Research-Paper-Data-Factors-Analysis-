# CryptoQuant / USDC/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (12)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `60bc0eb4cdb5` |
| `USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `32dfa246dd1a` |
| `USD Coin(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `d5c13278281b` |
| `USD Coin(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `2eb1b0219e2c` |
| `USD Coin(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 2 | `9ff4caabf9a4` |
| `USD Coin(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `3e6a40d7fdc7` |
| `USD Coin(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `5dfbc10b8c6f` |
| `USD Coin(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `c24b61662de3` |
| `USD Coin(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 2 | `4fe09fcf59cf` |
| `USD Coin(ERC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 2 | `47a2730872ee` |
| `USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `fda513cb2bcc` |
| `USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 2 | `ef906a35da8a` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Addresses
2018-09-12,1
2018-09-13,0
```

**`USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Transactions
2018-09-12,1
2018-09-13,0
```

**`USD Coin(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Mean)
2018-09-12,1.0
2018-09-13,0.0
```

**`USD Coin(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Top10)
2018-09-12,1.0
2018-09-13,0.0
```

**`USD Coin(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Total)
2018-09-12,1.0
2018-09-13,0.0
```

**`USD Coin(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Netflow (Total)
2018-09-12,0.6
2018-09-13,0.0
```

**`USD Coin(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Mean)
2018-09-12,0.4
2018-09-13,0.0
```

**`USD Coin(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Top10)
2018-09-12,0.4
2018-09-13,0.0
```

**`USD Coin(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Total)
2018-09-12,0.4
2018-09-13,0.0
```

**`USD Coin(ERC20) Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,Exchange Reserve
2018-09-12,0.6
2018-09-13,0.6
```

**`USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv`**

```csv
date,Exchange Withdrawing Addresses
2018-09-12,1
2018-09-13,0
```

**`USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Withdrawing Transactions
2018-09-12,1
2018-09-13,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
