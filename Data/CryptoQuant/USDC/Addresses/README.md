# CryptoQuant / USDC/Addresses

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
| `USD Coin(ERC20) Active Addresses - Day.csv` | Active addresses | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 | `e59685970a83` |
| `USD Coin(ERC20) Active Receiving Addresses (%) - Day.csv` | USD Coin(ERC20) Active Receiving Addresses (%) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 | `b712312491b5` |
| `USD Coin(ERC20) Active Receiving Addresses - Day.csv` | USD Coin(ERC20) Active Receiving Addresses - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 | `7c6e52d5913d` |
| `USD Coin(ERC20) Active Sending Addresses (%) - Day.csv` | USD Coin(ERC20) Active Sending Addresses (%) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 | `4613ba401536` |
| `USD Coin(ERC20) Active Sending Addresses - Day.csv` | USD Coin(ERC20) Active Sending Addresses - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 | `b591991dfd5a` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`USD Coin(ERC20) Active Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Addresses
2018-09-10,2018-09-10T00:00:00Z,6
2018-09-12,2018-09-12T00:00:00Z,5
```

**`USD Coin(ERC20) Active Receiving Addresses (%) - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses (%)
2018-09-10,2018-09-10T00:00:00Z,83.33333333
2018-09-12,2018-09-12T00:00:00Z,80.0
```

**`USD Coin(ERC20) Active Receiving Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses
2018-09-10,2018-09-10T00:00:00Z,5
2018-09-12,2018-09-12T00:00:00Z,4
```

**`USD Coin(ERC20) Active Sending Addresses (%) - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses (%)
2018-09-10,2018-09-10T00:00:00Z,33.33333333
2018-09-12,2018-09-12T00:00:00Z,60.0
```

**`USD Coin(ERC20) Active Sending Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses
2018-09-10,2018-09-10T00:00:00Z,2
2018-09-12,2018-09-12T00:00:00Z,3
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
