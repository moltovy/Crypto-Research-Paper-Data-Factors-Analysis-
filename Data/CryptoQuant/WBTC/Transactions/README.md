# CryptoQuant / WBTC/Transactions

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
| `Wrapped BTC Tokens Transferred (Mean) - Day.csv` | Wrapped BTC Tokens Transferred (Mean) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `81b996a80907` |
| `Wrapped BTC Tokens Transferred (Median) - Day.csv` | Wrapped BTC Tokens Transferred (Median) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `eb1760e586cf` |
| `Wrapped BTC Tokens Transferred (Total) - Day.csv` | Wrapped BTC Tokens Transferred (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `e834849003a9` |
| `Wrapped BTC Transaction Count (Mean) - Day.csv` | Wrapped BTC Transaction Count (Mean) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `2e53e53dac84` |
| `Wrapped BTC Transaction Count (Total) - Day.csv` | Wrapped BTC Transaction Count (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `ad781cea3da5` |
| `Wrapped BTC Transfer Count (Total) - Day.csv` | Wrapped BTC Transfer Count (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `00a1369549c9` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Wrapped BTC Tokens Transferred (Mean) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Mean)
2018-11-24,2018-11-24T00:00:00Z,
2018-11-25,2018-11-25T00:00:00Z,
```

**`Wrapped BTC Tokens Transferred (Median) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Median)
2018-11-24,2018-11-24T00:00:00Z,
2018-11-25,2018-11-25T00:00:00Z,
```

**`Wrapped BTC Tokens Transferred (Total) - Day.csv`**

```csv
date,timestamp_utc,Tokens Transferred (Total)
2018-11-24,2018-11-24T00:00:00Z,0.0
2018-11-25,2018-11-25T00:00:00Z,0.0
```

**`Wrapped BTC Transaction Count (Mean) - Day.csv`**

```csv
date,timestamp_utc,Transaction Count (Mean)
2018-11-24,2018-11-24T00:00:00Z,0.00178891
2018-11-25,2018-11-25T00:00:00Z,
```

**`Wrapped BTC Transaction Count (Total) - Day.csv`**

```csv
date,timestamp_utc,Transaction Count (Total)
2018-11-24,2018-11-24T00:00:00Z,1
2018-11-25,2018-11-25T00:00:00Z,0
```

**`Wrapped BTC Transfer Count (Total) - Day.csv`**

```csv
date,timestamp_utc,Transfer Count (Total)
2018-11-24,2018-11-24T00:00:00Z,0
2018-11-25,2018-11-25T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
