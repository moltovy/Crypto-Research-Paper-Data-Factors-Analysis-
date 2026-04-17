# CryptoQuant / WBTC/Transactions

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
| `Wrapped BTC Tokens Transferred (Mean) - Day.csv` | Wrapped BTC Tokens Transferred (Mean) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `123f58ac9563` |
| `Wrapped BTC Tokens Transferred (Median) - Day.csv` | Wrapped BTC Tokens Transferred (Median) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `568669891b45` |
| `Wrapped BTC Tokens Transferred (Total) - Day.csv` | Wrapped BTC Tokens Transferred (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `990e67a1b5eb` |
| `Wrapped BTC Transaction Count (Mean) - Day.csv` | Wrapped BTC Transaction Count (Mean) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `91e53b3ad7b9` |
| `Wrapped BTC Transaction Count (Total) - Day.csv` | Wrapped BTC Transaction Count (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `8ff16edf94b3` |
| `Wrapped BTC Transfer Count (Total) - Day.csv` | Wrapped BTC Transfer Count (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `546fe0a6115a` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Wrapped BTC Tokens Transferred (Mean) - Day.csv`**

```csv
date,Tokens Transferred (Mean)
2018-11-24,
2018-11-25,
```

**`Wrapped BTC Tokens Transferred (Median) - Day.csv`**

```csv
date,Tokens Transferred (Median)
2018-11-24,
2018-11-25,
```

**`Wrapped BTC Tokens Transferred (Total) - Day.csv`**

```csv
date,Tokens Transferred (Total)
2018-11-24,0.0
2018-11-25,0.0
```

**`Wrapped BTC Transaction Count (Mean) - Day.csv`**

```csv
date,Transaction Count (Mean)
2018-11-24,0.00178891
2018-11-25,
```

**`Wrapped BTC Transaction Count (Total) - Day.csv`**

```csv
date,Transaction Count (Total)
2018-11-24,1
2018-11-25,0
```

**`Wrapped BTC Transfer Count (Total) - Day.csv`**

```csv
date,Transfer Count (Total)
2018-11-24,0
2018-11-25,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
