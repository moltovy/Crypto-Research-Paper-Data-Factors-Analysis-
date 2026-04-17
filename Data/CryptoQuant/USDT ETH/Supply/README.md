# CryptoQuant / USDT ETH/Supply

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (1)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Tether USD(ERC20) Total Supply - Day.csv` | Tether USD(ERC20) Total Supply - Day | 2017-11-28 .. 2026-04-11 | 3,057 | daily | 0 | 3 | `dc17e83e8939` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(ERC20) Total Supply - Day.csv`**

```csv
date,timestamp_utc,Total Supply
2017-11-28,2017-11-28T00:00:00Z,110000.0
2017-11-29,2017-11-29T00:00:00Z,110000.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
