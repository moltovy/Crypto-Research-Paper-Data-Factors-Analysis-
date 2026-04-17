# CryptoQuant / USDT ETH/Exchange Flows

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
| `Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `2250978721aa` |
| `Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `e467bfea1c70` |
| `Tether USD(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `4ea1321257e3` |
| `Tether USD(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `3cdf2c6cfc98` |
| `Tether USD(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `6e299a19d22c` |
| `Tether USD(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `e45338712916` |
| `Tether USD(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `dcd357179ddb` |
| `Tether USD(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `c40aab41b4d0` |
| `Tether USD(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `9043b941b0e9` |
| `Tether USD(ERC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `ef78cf2fae60` |
| `Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `dc3ef3a531ed` |
| `Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 | `175d88abe69b` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Addresses
2017-12-28,2017-12-28T00:00:00Z,3
2017-12-29,2017-12-29T00:00:00Z,0
```

**`Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Transactions
2017-12-28,2017-12-28T00:00:00Z,4
2017-12-29,2017-12-29T00:00:00Z,0
```

**`Tether USD(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Mean)
2017-12-28,2017-12-28T00:00:00Z,296.25
2017-12-29,2017-12-29T00:00:00Z,0.0
```

**`Tether USD(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Top10)
2017-12-28,2017-12-28T00:00:00Z,296.25
2017-12-29,2017-12-29T00:00:00Z,0.0
```

**`Tether USD(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Total)
2017-12-28,2017-12-28T00:00:00Z,1185.0
2017-12-29,2017-12-29T00:00:00Z,0.0
```

**`Tether USD(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Netflow (Total)
2017-12-28,2017-12-28T00:00:00Z,867.0
2017-12-29,2017-12-29T00:00:00Z,0.0
```

**`Tether USD(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Mean)
2017-12-28,2017-12-28T00:00:00Z,79.5
2017-12-29,2017-12-29T00:00:00Z,0.0
```

**`Tether USD(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Top10)
2017-12-28,2017-12-28T00:00:00Z,79.5
2017-12-29,2017-12-29T00:00:00Z,0.0
```

**`Tether USD(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Total)
2017-12-28,2017-12-28T00:00:00Z,318.0
2017-12-29,2017-12-29T00:00:00Z,0.0
```

**`Tether USD(ERC20) Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Reserve
2017-12-28,2017-12-28T00:00:00Z,867.0
2017-12-29,2017-12-29T00:00:00Z,867.0
```

**`Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Withdrawing Addresses
2017-12-28,2017-12-28T00:00:00Z,2
2017-12-29,2017-12-29T00:00:00Z,0
```

**`Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Withdrawing Transactions
2017-12-28,2017-12-28T00:00:00Z,4
2017-12-29,2017-12-29T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
