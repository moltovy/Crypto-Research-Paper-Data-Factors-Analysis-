# CryptoQuant / BTC/Inter Entity Flows

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (6)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `973cbed9d6da` |
| `Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `dbff87638f43` |
| `Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 | `c74742ad12d1` |
| `Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 3 | `85e0e5a4818f` |
| `Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 3 | `ff50f5fe588e` |
| `Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 3 | `f1bc01c61c29` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange to Exchange Flow (Mean)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange to Exchange Flow (Total)
2009-01-01,2009-01-01T00:00:00Z,0.0
2009-01-02,2009-01-02T00:00:00Z,0.0
```

**`Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange to Exchange Transactions
2009-01-01,2009-01-01T00:00:00Z,0
2009-01-02,2009-01-02T00:00:00Z,0
```

**`Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day.csv`**

```csv
date,timestamp_utc,Miner to Miner Flow (Mean)
2021-01-24,2021-01-24T00:00:00Z,300.0
2021-01-25,2021-01-25T00:00:00Z,0.0
```

**`Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day.csv`**

```csv
date,timestamp_utc,Miner to Miner Flow (Total)
2021-01-24,2021-01-24T00:00:00Z,300.0
2021-01-25,2021-01-25T00:00:00Z,0.0
```

**`Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day.csv`**

```csv
date,timestamp_utc,Miner to Miner Transactions
2021-01-24,2021-01-24T00:00:00Z,1
2021-01-25,2021-01-25T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
