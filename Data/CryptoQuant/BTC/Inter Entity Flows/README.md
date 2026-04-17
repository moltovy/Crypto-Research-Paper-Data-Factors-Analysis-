# CryptoQuant / BTC/Inter Entity Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (6)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `903001e63ed0` |
| `Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `0b5a716cf8c3` |
| `Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 2 | `b75c935198d9` |
| `Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 2 | `2ef75b0de9fb` |
| `Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 2 | `9ee31c203b3f` |
| `Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 2 | `9420003938a8` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day.csv`**

```csv
date,Exchange to Exchange Flow (Mean)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day.csv`**

```csv
date,Exchange to Exchange Flow (Total)
2009-01-01,0.0
2009-01-02,0.0
```

**`Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day.csv`**

```csv
date,Exchange to Exchange Transactions
2009-01-01,0
2009-01-02,0
```

**`Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day.csv`**

```csv
date,Miner to Miner Flow (Mean)
2021-01-24,300.0
2021-01-25,0.0
```

**`Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day.csv`**

```csv
date,Miner to Miner Flow (Total)
2021-01-24,300.0
2021-01-25,0.0
```

**`Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day.csv`**

```csv
date,Miner to Miner Transactions
2021-01-24,1
2021-01-25,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
