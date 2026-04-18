# CryptoQuant / USDT ETH/Exchange Flows

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
| `Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `5fed3f0e2569` |
| `Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `7073fff681f4` |
| `Tether USD(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `672db4d874da` |
| `Tether USD(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `c844b0338ff2` |
| `Tether USD(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `dadaa29549df` |
| `Tether USD(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `741fdc0b7094` |
| `Tether USD(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `934059ed880e` |
| `Tether USD(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `cd6c203d5251` |
| `Tether USD(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `655fd1233619` |
| `Tether USD(ERC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `bc1c4a42a2b3` |
| `Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `a1e4f165ca30` |
| `Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 2 | `ea47628eba1c` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Addresses
2017-12-28,3
2017-12-29,0
```

**`Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Transactions
2017-12-28,4
2017-12-29,0
```

**`Tether USD(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Mean)
2017-12-28,296.25
2017-12-29,0.0
```

**`Tether USD(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Top10)
2017-12-28,296.25
2017-12-29,0.0
```

**`Tether USD(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Total)
2017-12-28,1185.0
2017-12-29,0.0
```

**`Tether USD(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Netflow (Total)
2017-12-28,867.0
2017-12-29,0.0
```

**`Tether USD(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Mean)
2017-12-28,79.5
2017-12-29,0.0
```

**`Tether USD(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Top10)
2017-12-28,79.5
2017-12-29,0.0
```

**`Tether USD(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Total)
2017-12-28,318.0
2017-12-29,0.0
```

**`Tether USD(ERC20) Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,Exchange Reserve
2017-12-28,867.0
2017-12-29,867.0
```

**`Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv`**

```csv
date,Exchange Withdrawing Addresses
2017-12-28,2
2017-12-29,0
```

**`Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Withdrawing Transactions
2017-12-28,4
2017-12-29,0
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
