# CryptoQuant / WBTC/Addresses

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Wrapped BTC Active Addresses - Day.csv` | Active addresses | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `2f1c362f931d` |
| `Wrapped BTC Active Receiving Addresses - Day.csv` | Wrapped BTC Active Receiving Addresses - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `19ddb96e9dee` |
| `Wrapped BTC Active Sending Addresses - Day.csv` | Wrapped BTC Active Sending Addresses - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 2 | `9bf6daa9aeab` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Wrapped BTC Active Addresses - Day.csv`**

```csv
date,Active Addresses
2018-11-24,0
2018-11-25,0
```

**`Wrapped BTC Active Receiving Addresses - Day.csv`**

```csv
date,Active Receiving Addresses
2018-11-24,0
2018-11-25,0
```

**`Wrapped BTC Active Sending Addresses - Day.csv`**

```csv
date,Active Sending Addresses
2018-11-24,0
2018-11-25,0
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
