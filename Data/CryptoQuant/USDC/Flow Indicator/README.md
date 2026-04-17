# CryptoQuant / USDC/Flow Indicator

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
| `USD Coin(ERC20) Exchange Supply Ratio - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Supply Ratio - All Exchanges - Day | 2018-09-10 .. 2026-04-11 | 2,771 | daily | 0 | 3 | `4894a202be4f` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`USD Coin(ERC20) Exchange Supply Ratio - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Exchange Supply Ratio
2018-09-10,2018-09-10T00:00:00Z,0.0
2018-09-11,2018-09-11T00:00:00Z,0.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
