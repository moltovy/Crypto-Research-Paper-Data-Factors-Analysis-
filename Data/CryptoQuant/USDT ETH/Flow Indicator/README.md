# CryptoQuant / USDT ETH/Flow Indicator

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (1)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Tether USD(ERC20) Exchange Supply Ratio - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Supply Ratio - All Exchanges - Day | 2017-11-28 .. 2026-04-10 | 3,056 | daily | 0 | 2 | `6c7d0f898f51` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(ERC20) Exchange Supply Ratio - All Exchanges - Day.csv`**

```csv
date,Exchange Supply Ratio
2017-11-28,0.0
2017-11-29,0.0
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
