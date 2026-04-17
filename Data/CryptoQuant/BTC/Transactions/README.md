# CryptoQuant / BTC/Transactions

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (5)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Tokens Transferred (Mean) - Day.csv` | Bitcoin Tokens Transferred (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `c05774b5c20c` |
| `Bitcoin Tokens Transferred (Median) - Day.csv` | Bitcoin Tokens Transferred (Median) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `b1081399c858` |
| `Bitcoin Tokens Transferred (Total) - Day.csv` | Bitcoin Tokens Transferred (Total) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `584264b8b86a` |
| `Bitcoin Transaction Count (Mean) - Day.csv` | Bitcoin Transaction Count (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `d0054af7f252` |
| `Bitcoin Transaction Count (Total) - Day.csv` | Bitcoin Transaction Count (Total) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `65b12decce80` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Tokens Transferred (Mean) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Mean)
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Tokens Transferred (Median) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Median)
2009-01-03,2009-01-03T00:00:00Z,
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Tokens Transferred (Total) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Total)
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Transaction Count (Mean) - Day.csv`**

```csv
date,timestamp_utc,Transactions Count (Mean)
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,
```

**`Bitcoin Transaction Count (Total) - Day.csv`**

```csv
date,timestamp_utc,Transactions Count (Total)
2009-01-03,2009-01-03T00:00:00Z,0
2009-01-04,2009-01-04T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
