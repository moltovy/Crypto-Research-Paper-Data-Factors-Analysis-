# CryptoQuant / USDT (TRX)/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (9)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `12d3d362425d` |
| `Tether USD(TRC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `4ab6fd025035` |
| `Tether USD(TRC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `a51ab06f5a34` |
| `Tether USD(TRC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `0e9cb3079f46` |
| `Tether USD(TRC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `02456f1c3cd3` |
| `Tether USD(TRC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `1ad7b99ed709` |
| `Tether USD(TRC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `be760d6c8893` |
| `Tether USD(TRC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `2e5402eaf10f` |
| `Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 2 | `e162b1b77706` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Transactions
2019-07-17,3
2019-07-18,78
```

**`Tether USD(TRC20) Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Mean)
2019-07-17,2934.595604
2019-07-18,4926.74772354
```

**`Tether USD(TRC20) Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Top10)
2019-07-17,8803.786812
2019-07-18,383345.085037
```

**`Tether USD(TRC20) Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Total)
2019-07-17,8803.786812
2019-07-18,384286.322436
```

**`Tether USD(TRC20) Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Netflow (Total)
2019-07-17,8784.767639
2019-07-18,383360.675501
```

**`Tether USD(TRC20) Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Mean)
2019-07-17,19.019173
2019-07-18,308.54897833
```

**`Tether USD(TRC20) Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Top10)
2019-07-17,19.019173
2019-07-18,925.646935
```

**`Tether USD(TRC20) Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,Reserve
2019-07-17,8784.767639
2019-07-18,392145.44314
```

**`Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Withdrawing Transactions
2019-07-17,1
2019-07-18,3
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
