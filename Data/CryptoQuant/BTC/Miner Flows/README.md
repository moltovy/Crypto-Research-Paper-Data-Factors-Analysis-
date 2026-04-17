# CryptoQuant / BTC/Miner Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (24)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 2 | `d8f8cbe6ce09` |
| `Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 2 | `b7d19dc825ca` |
| `Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 2 | `555a246dc3e7` |
| `Bitcoin Miner Depositing Addresses - All Miners - Day.csv` | Bitcoin Miner Depositing Addresses - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `8e55584e229c` |
| `Bitcoin Miner Depositing Transactions - All Miners - Day.csv` | Bitcoin Miner Depositing Transactions - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `e4a6c9b776c1` |
| `Bitcoin Miner In-House Flow (Mean) - All Miners - Day.csv` | Bitcoin Miner In-House Flow (Mean) - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 2 | `161823939ab1` |
| `Bitcoin Miner In-House Flow (Total) - All Miners - Day.csv` | Bitcoin Miner In-House Flow (Total) - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 2 | `0921f5c064fd` |
| `Bitcoin Miner In-House Transactions - All Miners - Day.csv` | Bitcoin Miner In-House Transactions - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 2 | `9a0dce48e96f` |
| `Bitcoin Miner Inflow (Mean) - All Miners - Day.csv` | Bitcoin Miner Inflow (Mean) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `727ae3f21a87` |
| `Bitcoin Miner Inflow (Top10) - All Miners - Day.csv` | Bitcoin Miner Inflow (Top10) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `b35815b42ca8` |
| `Bitcoin Miner Inflow (Total) - All Miners - Day.csv` | Bitcoin Miner Inflow (Total) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `b962e15bed86` |
| `Bitcoin Miner Netflow Total - All Miners - Day.csv` | Miner netflow | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `90a2fb2dc59f` |
| `Bitcoin Miner Outflow (Mean) - All Miners - Day.csv` | Bitcoin Miner Outflow (Mean) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `f03931cec14f` |
| `Bitcoin Miner Outflow (Top10) - All Miners - Day.csv` | Bitcoin Miner Outflow (Top10) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `2d92ebee4bcd` |
| `Bitcoin Miner Outflow (Total) - All Miners - Day.csv` | Bitcoin Miner Outflow (Total) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `9cdfe6b6a972` |
| `Bitcoin Miner Reserve - All Miners - Day.csv` | Miner reserve | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `39690a46ae80` |
| `Bitcoin Miner Reserve USD - All Miners - Day.csv` | Miner reserve | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `0d767b0b1ec8` |
| `Bitcoin Miner Supply Ratio - All Miners - Day.csv` | Bitcoin Miner Supply Ratio - All Miners - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `699d452f5b14` |
| `Bitcoin Miner to Exchange Flow (Mean) - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Flow (Mean) - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 2 | `3cb1453ccaff` |
| `Bitcoin Miner to Exchange Flow (Total) - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Flow (Total) - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 2 | `4f1d0d28041c` |
| `Bitcoin Miner to Exchange Transactions - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Transactions - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 2 | `9cd0cee9efb4` |
| `Bitcoin Miner Withdrawing Addresses - All Miners - Day.csv` | Bitcoin Miner Withdrawing Addresses - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `355a9393dcf7` |
| `Bitcoin Miner Withdrawing Transactions - All Miners - Day.csv` | Bitcoin Miner Withdrawing Transactions - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 2 | `2b1d60125b12` |
| `Bitcoin Miners' Position Index (MPI) - Day.csv` | Bitcoin Miners' Position Index (MPI) - Day | 2011-01-07 .. 2026-04-10 | 5,573 | daily | 0 | 2 | `283e27d7ad51` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day.csv`**

```csv
date,Exchange to Miner Flow (Mean)
2012-07-11,0.0005
2012-07-12,0.0
```

**`Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day.csv`**

```csv
date,Exchange to Miner Flow (Total)
2012-07-11,0.0005
2012-07-12,0.0
```

**`Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day.csv`**

```csv
date,Exchange to Miner Transactions
2012-07-11,1
2012-07-12,0
```

**`Bitcoin Miner Depositing Addresses - All Miners - Day.csv`**

```csv
date,Miner Depositing Addresses
2009-01-09,14
2009-01-10,61
```

**`Bitcoin Miner Depositing Transactions - All Miners - Day.csv`**

```csv
date,Miner Depositing Transactions
2009-01-09,14
2009-01-10,61
```

**`Bitcoin Miner In-House Flow (Mean) - All Miners - Day.csv`**

```csv
date,Miner In-House Flow (Mean)
2009-01-12,33.0
2009-01-13,0.0
```

**`Bitcoin Miner In-House Flow (Total) - All Miners - Day.csv`**

```csv
date,Miner In-House Flow (Total)
2009-01-12,165.0
2009-01-13,0.0
```

**`Bitcoin Miner In-House Transactions - All Miners - Day.csv`**

```csv
date,Miner In-House Transactions
2009-01-12,5
2009-01-13,0
```

**`Bitcoin Miner Inflow (Mean) - All Miners - Day.csv`**

```csv
date,Miner Inflow (Mean)
2009-01-09,50.0
2009-01-10,50.0
```

**`Bitcoin Miner Inflow (Top10) - All Miners - Day.csv`**

```csv
date,Miner Inflow (Top10)
2009-01-09,600.0
2009-01-10,650.0
```

**`Bitcoin Miner Inflow (Total) - All Miners - Day.csv`**

```csv
date,Miner Inflow (Total)
2009-01-09,700.0
2009-01-10,3050.0
```

**`Bitcoin Miner Netflow Total - All Miners - Day.csv`**

```csv
date,Miner Netflow Total
2009-01-09,700.0
2009-01-10,3050.0
```

_(12 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
