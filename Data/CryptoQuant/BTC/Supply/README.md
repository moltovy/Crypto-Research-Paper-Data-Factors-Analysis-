# CryptoQuant / BTC/Supply

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (2)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin New Supply - Day.csv` | Bitcoin New Supply - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `7ccb7aed24fe` |
| `Bitcoin Total Supply - Day.csv` | Bitcoin Total Supply - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `1439a721c3bb` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin New Supply - Day.csv`**

```csv
date,timestamp_utc,New Supply
2009-01-03,2009-01-03T00:00:00Z,50.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Total Supply - Day.csv`**

```csv
date,timestamp_utc,Total Supply
2009-01-03,2009-01-03T00:00:00Z,50.0
2009-01-04,2009-01-04T00:00:00Z,50.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
