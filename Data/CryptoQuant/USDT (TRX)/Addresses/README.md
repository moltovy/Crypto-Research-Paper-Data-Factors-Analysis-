# CryptoQuant / USDT (TRX)/Addresses

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
| `Tether USD(TRC20) Active Addresses - Day.csv` | Active addresses | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 2 | `9fccce3da2c0` |
| `Tether USD(TRC20) Active Receiving Addresses (%) - Day.csv` | Tether USD(TRC20) Active Receiving Addresses (%) - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 2 | `b5a5d9573739` |
| `Tether USD(TRC20) Active Receiving Addresses - Day.csv` | Tether USD(TRC20) Active Receiving Addresses - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 2 | `4f44ac07461e` |
| `Tether USD(TRC20) Active Sending Addresses (%) - Day.csv` | Tether USD(TRC20) Active Sending Addresses (%) - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 2 | `dbf41d02d1b9` |
| `Tether USD(TRC20) Active Sending Addresses - Day.csv` | Tether USD(TRC20) Active Sending Addresses - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 2 | `9de77365d329` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(TRC20) Active Addresses - Day.csv`**

```csv
date,Active Addresses
2019-07-01,0
2019-07-02,0
```

**`Tether USD(TRC20) Active Receiving Addresses (%) - Day.csv`**

```csv
date,Active Receiving Addresses (%)
2019-07-01,0.0
2019-07-02,0.0
```

**`Tether USD(TRC20) Active Receiving Addresses - Day.csv`**

```csv
date,Active Receiving Addresses
2019-07-01,0
2019-07-02,0
```

**`Tether USD(TRC20) Active Sending Addresses (%) - Day.csv`**

```csv
date,Active Sending Addresses (%)
2019-07-01,0.0
2019-07-02,0.0
```

**`Tether USD(TRC20) Active Sending Addresses - Day.csv`**

```csv
date,Active Sending Addresses
2019-07-01,0
2019-07-02,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
