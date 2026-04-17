# CryptoQuant / BTC/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (18)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Exchange Depositing Addresses - All Exchanges - Day.csv` | Bitcoin Exchange Depositing Addresses - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `71bc69008de6` |
| `Bitcoin Exchange Depositing Transactions - All Exchanges - Day.csv` | Bitcoin Exchange Depositing Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `15a3560c83a3` |
| `Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day.csv` | Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `ac0d291379e9` |
| `Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day.csv` | Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `618117cdd011` |
| `Bitcoin Exchange In-House Transactions - All Exchanges - Day.csv` | Bitcoin Exchange In-House Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `15ac4c0619b0` |
| `Bitcoin Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `d2f5e9ba9994` |
| `Bitcoin Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `16477fda06cc` |
| `Bitcoin Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `84e11d0e94fa` |
| `Bitcoin Exchange Inflow - Spent Output Age Bands - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 15 | `7cf327b4df61` |
| `Bitcoin Exchange Inflow - Spent Output Value Bands - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 10 | `cb124f58f36c` |
| `Bitcoin Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `59ef2c0f1b0c` |
| `Bitcoin Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `2dba68c8e2f5` |
| `Bitcoin Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `d596deba5333` |
| `Bitcoin Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `31c2a46738e4` |
| `Bitcoin Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2012-04-02 .. 2026-04-11 | 5,123 | daily | 0 | 4 | `6754f1983c46` |
| `Bitcoin Exchange Reserve USD - All Exchanges - Day.csv` | Exchange reserve | 2012-04-02 .. 2026-04-11 | 5,123 | daily | 0 | 3 | `14cddc224af2` |
| `Bitcoin Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Bitcoin Exchange Withdrawing Addresses - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `4331236c0a36` |
| `Bitcoin Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Bitcoin Exchange Withdrawing Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `6e3b1755bca4` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Addresses
2009-01-01,2009-01-01T00:00:00Z,0
2009-01-02,2009-01-02T00:00:00Z,0
```

**`Bitcoin Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Depositing Transactions
2009-01-01,2009-01-01T00:00:00Z,0
2009-01-02,2009-01-02T00:00:00Z,0
```

**`Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange In-House Flow (Mean)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange In-House Flow (Total)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange In-House Transactions - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange In-House Transactions
2009-01-01,2009-01-01T00:00:00Z,0
2009-01-02,2009-01-02T00:00:00Z,0
```

**`Bitcoin Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Mean)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Top10)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Inflow (Total)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange Inflow - Spent Output Age Bands - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,0d ~ 1d,1d ~ 1w,1w ~ 1m,1m ~ 3m,3m ~ 6m,6m ~ 12m,12m ~ 18m,18m ~ 2y,... (+5 more)
2012-04-02,2012-04-02T00:00:00Z,0.0,0.02,0.0,0.0,0.0,0.0,0.0,0.0
2012-04-03,2012-04-03T00:00:00Z,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Exchange Inflow - Spent Output Value Bands - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,0 ~ 0.01 BTC,0.01 ~ 0.1 BTC,0.1 ~ 1 BTC,1 ~ 10 BTC,10 ~ 100 BTC,100 ~ 1K BTC,1K ~ 10K BTC,10K ~ BTC
2012-04-02,2012-04-02T00:00:00Z,0.0,0.0,0.02,0.0,0.0,0.0,0.0,0.0
2012-04-03,2012-04-03T00:00:00Z,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Netflow (Total)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Outflow (Mean)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

_(6 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
