# CryptoQuant / BTC/Exchange Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (18)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Exchange Depositing Addresses - All Exchanges - Day.csv` | Bitcoin Exchange Depositing Addresses - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `20805572cabb` |
| `Bitcoin Exchange Depositing Transactions - All Exchanges - Day.csv` | Bitcoin Exchange Depositing Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `376bb3a33476` |
| `Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day.csv` | Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `28f1e638de43` |
| `Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day.csv` | Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `d388890df7e4` |
| `Bitcoin Exchange In-House Transactions - All Exchanges - Day.csv` | Bitcoin Exchange In-House Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `e8f1c9d8c5f6` |
| `Bitcoin Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `662bbb3cba20` |
| `Bitcoin Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `9857709376c7` |
| `Bitcoin Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `ca36b63c0cd1` |
| `Bitcoin Exchange Inflow - Spent Output Age Bands - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 14 | `0c18c062732f` |
| `Bitcoin Exchange Inflow - Spent Output Value Bands - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 9 | `c04be8fb7d91` |
| `Bitcoin Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `d2fa3d856c64` |
| `Bitcoin Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `ac4e3fc99693` |
| `Bitcoin Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `7ed344026833` |
| `Bitcoin Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `7a2eeec6d919` |
| `Bitcoin Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2012-04-02 .. 2026-04-11 | 5,123 | daily | 0 | 3 | `c68cb2fcc906` |
| `Bitcoin Exchange Reserve USD - All Exchanges - Day.csv` | Exchange reserve | 2012-04-02 .. 2026-04-11 | 5,123 | daily | 0 | 2 | `bda105ac7e59` |
| `Bitcoin Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Bitcoin Exchange Withdrawing Addresses - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `ecc5baeaa245` |
| `Bitcoin Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Bitcoin Exchange Withdrawing Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `0b2b24ae3b06` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Exchange Depositing Addresses - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Addresses
2009-01-01,0
2009-01-02,0
```

**`Bitcoin Exchange Depositing Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange Depositing Transactions
2009-01-01,0
2009-01-02,0
```

**`Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange In-House Flow (Mean)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange In-House Flow (Total)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange In-House Transactions - All Exchanges - Day.csv`**

```csv
date,Exchange In-House Transactions
2009-01-01,0
2009-01-02,0
```

**`Bitcoin Exchange Inflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Mean)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange Inflow (Top10) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Top10)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange Inflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow (Total)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange Inflow - Spent Output Age Bands - All Exchanges - Day.csv`**

```csv
date,0d ~ 1d,1d ~ 1w,1w ~ 1m,1m ~ 3m,3m ~ 6m,6m ~ 12m,12m ~ 18m,18m ~ 2y,2y ~ 3y,... (+4 more)
2012-04-02,0.0,0.02,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2012-04-03,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Exchange Inflow - Spent Output Value Bands - All Exchanges - Day.csv`**

```csv
date,0 ~ 0.01 BTC,0.01 ~ 0.1 BTC,0.1 ~ 1 BTC,1 ~ 10 BTC,10 ~ 100 BTC,100 ~ 1K BTC,1K ~ 10K BTC,10K ~ BTC
2012-04-02,0.0,0.0,0.02,0.0,0.0,0.0,0.0,0.0
2012-04-03,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Exchange Netflow (Total) - All Exchanges - Day.csv`**

```csv
date,Exchange Netflow (Total)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange Outflow (Mean) - All Exchanges - Day.csv`**

```csv
date,Exchange Outflow (Mean)
2009-01-01,0.0
2009-01-02,0.0
```

_(6 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
