# CryptoQuant / WBTC/Addresses

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Wrapped BTC Active Addresses - Day.csv` | Active addresses | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `9f6541ba26fd` |
| `Wrapped BTC Active Receiving Addresses - Day.csv` | Wrapped BTC Active Receiving Addresses - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `4ed62cdf9997` |
| `Wrapped BTC Active Sending Addresses - Day.csv` | Wrapped BTC Active Sending Addresses - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 | `96375ed584a9` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Wrapped BTC Active Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Addresses
2018-11-24,2018-11-24T00:00:00Z,0
2018-11-25,2018-11-25T00:00:00Z,0
```

**`Wrapped BTC Active Receiving Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses
2018-11-24,2018-11-24T00:00:00Z,0
2018-11-25,2018-11-25T00:00:00Z,0
```

**`Wrapped BTC Active Sending Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses
2018-11-24,2018-11-24T00:00:00Z,0
2018-11-25,2018-11-25T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
