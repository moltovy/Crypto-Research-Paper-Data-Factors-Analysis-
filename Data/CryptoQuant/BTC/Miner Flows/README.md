# CryptoQuant / BTC/Miner Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (24)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 3 | `dce227a45b27` |
| `Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 3 | `3547c2192739` |
| `Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 3 | `0c58bcfdfc84` |
| `Bitcoin Miner Depositing Addresses - All Miners - Day.csv` | Bitcoin Miner Depositing Addresses - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `6b5442273442` |
| `Bitcoin Miner Depositing Transactions - All Miners - Day.csv` | Bitcoin Miner Depositing Transactions - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `01e03fe4f079` |
| `Bitcoin Miner In-House Flow (Mean) - All Miners - Day.csv` | Bitcoin Miner In-House Flow (Mean) - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 3 | `af20e9232707` |
| `Bitcoin Miner In-House Flow (Total) - All Miners - Day.csv` | Bitcoin Miner In-House Flow (Total) - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 3 | `5dc46728c787` |
| `Bitcoin Miner In-House Transactions - All Miners - Day.csv` | Bitcoin Miner In-House Transactions - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 3 | `059894a7f311` |
| `Bitcoin Miner Inflow (Mean) - All Miners - Day.csv` | Bitcoin Miner Inflow (Mean) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `eb3d26b1b071` |
| `Bitcoin Miner Inflow (Top10) - All Miners - Day.csv` | Bitcoin Miner Inflow (Top10) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `a6922004a0c5` |
| `Bitcoin Miner Inflow (Total) - All Miners - Day.csv` | Bitcoin Miner Inflow (Total) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `f5e072b847bb` |
| `Bitcoin Miner Netflow Total - All Miners - Day.csv` | Miner netflow | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `202024401814` |
| `Bitcoin Miner Outflow (Mean) - All Miners - Day.csv` | Bitcoin Miner Outflow (Mean) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `a39d02546a29` |
| `Bitcoin Miner Outflow (Top10) - All Miners - Day.csv` | Bitcoin Miner Outflow (Top10) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `93926ae3e898` |
| `Bitcoin Miner Outflow (Total) - All Miners - Day.csv` | Bitcoin Miner Outflow (Total) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `ce9c0a6ee913` |
| `Bitcoin Miner Reserve - All Miners - Day.csv` | Miner reserve | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `c6675e1ee839` |
| `Bitcoin Miner Reserve USD - All Miners - Day.csv` | Miner reserve | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `1fe54785a851` |
| `Bitcoin Miner Supply Ratio - All Miners - Day.csv` | Bitcoin Miner Supply Ratio - All Miners - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `3bb9259e9a8f` |
| `Bitcoin Miner to Exchange Flow (Mean) - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Flow (Mean) - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 3 | `9ddfb7cc8c0d` |
| `Bitcoin Miner to Exchange Flow (Total) - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Flow (Total) - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 3 | `32adc7df4f28` |
| `Bitcoin Miner to Exchange Transactions - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Transactions - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 3 | `9d54056297f1` |
| `Bitcoin Miner Withdrawing Addresses - All Miners - Day.csv` | Bitcoin Miner Withdrawing Addresses - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `748b8afac93a` |
| `Bitcoin Miner Withdrawing Transactions - All Miners - Day.csv` | Bitcoin Miner Withdrawing Transactions - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 | `7942bc262ac0` |
| `Bitcoin Miners' Position Index (MPI) - Day.csv` | Bitcoin Miners' Position Index (MPI) - Day | 2011-01-07 .. 2026-04-10 | 5,573 | daily | 0 | 3 | `8c123cc407d6` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day.csv`**

```csv
date,timestamp_utc,Exchange to Miner Flow (Mean)
2012-07-11,2012-07-11T00:00:00Z,0.0005
2012-07-12,2012-07-12T00:00:00Z,0.0
```

**`Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day.csv`**

```csv
date,timestamp_utc,Exchange to Miner Flow (Total)
2012-07-11,2012-07-11T00:00:00Z,0.0005
2012-07-12,2012-07-12T00:00:00Z,0.0
```

**`Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day.csv`**

```csv
date,timestamp_utc,Exchange to Miner Transactions
2012-07-11,2012-07-11T00:00:00Z,1
2012-07-12,2012-07-12T00:00:00Z,0
```

**`Bitcoin Miner Depositing Addresses - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner Depositing Addresses
2009-01-09,2009-01-09T00:00:00Z,14
2009-01-10,2009-01-10T00:00:00Z,61
```

**`Bitcoin Miner Depositing Transactions - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner Depositing Transactions
2009-01-09,2009-01-09T00:00:00Z,14
2009-01-10,2009-01-10T00:00:00Z,61
```

**`Bitcoin Miner In-House Flow (Mean) - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner In-House Flow (Mean)
2009-01-12,2009-01-12T00:00:00Z,33.0
2009-01-13,2009-01-13T00:00:00Z,0.0
```

**`Bitcoin Miner In-House Flow (Total) - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner In-House Flow (Total)
2009-01-12,2009-01-12T00:00:00Z,165.0
2009-01-13,2009-01-13T00:00:00Z,0.0
```

**`Bitcoin Miner In-House Transactions - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner In-House Transactions
2009-01-12,2009-01-12T00:00:00Z,5
2009-01-13,2009-01-13T00:00:00Z,0
```

**`Bitcoin Miner Inflow (Mean) - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner Inflow (Mean)
2009-01-09,2009-01-09T00:00:00Z,50.0
2009-01-10,2009-01-10T00:00:00Z,50.0
```

**`Bitcoin Miner Inflow (Top10) - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner Inflow (Top10)
2009-01-09,2009-01-09T00:00:00Z,600.0
2009-01-10,2009-01-10T00:00:00Z,650.0
```

**`Bitcoin Miner Inflow (Total) - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner Inflow (Total)
2009-01-09,2009-01-09T00:00:00Z,700.0
2009-01-10,2009-01-10T00:00:00Z,3050.0
```

**`Bitcoin Miner Netflow Total - All Miners - Day.csv`**

```csv
date,timestamp_utc,Miner Netflow Total
2009-01-09,2009-01-09T00:00:00Z,700.0
2009-01-10,2009-01-10T00:00:00Z,3050.0
```

_(12 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
