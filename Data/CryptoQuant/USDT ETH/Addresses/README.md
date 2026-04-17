# CryptoQuant / USDT ETH/Addresses

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (5)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Tether USD(ERC20) Active Addresses - Day.csv` | Active addresses | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 2 | `a71938348b6c` |
| `Tether USD(ERC20) Active Receiving Addresses (%) - Day.csv` | Tether USD(ERC20) Active Receiving Addresses (%) - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 2 | `03a4dfcb7a10` |
| `Tether USD(ERC20) Active Receiving Addresses - Day.csv` | Tether USD(ERC20) Active Receiving Addresses - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 2 | `9f7518f52f28` |
| `Tether USD(ERC20) Active Sending Addresses (%) - Day.csv` | Tether USD(ERC20) Active Sending Addresses (%) - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 2 | `0eedbee047e0` |
| `Tether USD(ERC20) Active Sending Addresses - Day.csv` | Tether USD(ERC20) Active Sending Addresses - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 2 | `11c99bb4280a` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(ERC20) Active Addresses - Day.csv`**

```csv
date,Active Addresses
2017-11-28,5
2017-12-21,2
```

**`Tether USD(ERC20) Active Receiving Addresses (%) - Day.csv`**

```csv
date,Active Receiving Addresses (%)
2017-11-28,80.0
2017-12-21,50.0
```

**`Tether USD(ERC20) Active Receiving Addresses - Day.csv`**

```csv
date,Active Receiving Addresses
2017-11-28,4
2017-12-21,1
```

**`Tether USD(ERC20) Active Sending Addresses (%) - Day.csv`**

```csv
date,Active Sending Addresses (%)
2017-11-28,80.0
2017-12-21,50.0
```

**`Tether USD(ERC20) Active Sending Addresses - Day.csv`**

```csv
date,Active Sending Addresses
2017-11-28,4
2017-12-21,1
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
