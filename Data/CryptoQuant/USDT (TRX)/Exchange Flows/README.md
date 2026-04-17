# CryptoQuant / USDT (TRX)/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (9)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `9fd7952d3e03` |
| `Tether USD(TRC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `14aae2b7ec2e` |
| `Tether USD(TRC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `36ecaa5fef48` |
| `Tether USD(TRC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `59775178f61e` |
| `Tether USD(TRC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `6d0bfe503cc9` |
| `Tether USD(TRC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `14480243570d` |
| `Tether USD(TRC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `7b322f4e6342` |
| `Tether USD(TRC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `a1fcdfa983f0` |
| `Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 | `32f88ad58d51` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Transactions
2019-07-17,2019-07-17T00:00:00Z,3
2019-07-18,2019-07-18T00:00:00Z,78
```

**`Tether USD(TRC20) Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Mean)
2019-07-17,2019-07-17T00:00:00Z,2934.595604
2019-07-18,2019-07-18T00:00:00Z,4926.74772354
```

**`Tether USD(TRC20) Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Top10)
2019-07-17,2019-07-17T00:00:00Z,8803.786812
2019-07-18,2019-07-18T00:00:00Z,383345.085037
```

**`Tether USD(TRC20) Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Total)
2019-07-17,2019-07-17T00:00:00Z,8803.786812
2019-07-18,2019-07-18T00:00:00Z,384286.322436
```

**`Tether USD(TRC20) Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Netflow (Total)
2019-07-17,2019-07-17T00:00:00Z,8784.767639
2019-07-18,2019-07-18T00:00:00Z,383360.675501
```

**`Tether USD(TRC20) Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Mean)
2019-07-17,2019-07-17T00:00:00Z,19.019173
2019-07-18,2019-07-18T00:00:00Z,308.54897833
```

**`Tether USD(TRC20) Exchange Outflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Top10)
2019-07-17,2019-07-17T00:00:00Z,19.019173
2019-07-18,2019-07-18T00:00:00Z,925.646935
```

**`Tether USD(TRC20) Exchange Reserve - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Reserve
2019-07-17,2019-07-17T00:00:00Z,8784.767639
2019-07-18,2019-07-18T00:00:00Z,392145.44314
```

**`Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Withdrawing Transactions
2019-07-17,2019-07-17T00:00:00Z,1
2019-07-18,2019-07-18T00:00:00Z,3
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
