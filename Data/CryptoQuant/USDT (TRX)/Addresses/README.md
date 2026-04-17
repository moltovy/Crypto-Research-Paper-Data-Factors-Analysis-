# CryptoQuant / USDT (TRX)/Addresses

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
| `Tether USD(TRC20) Active Addresses - Day.csv` | Active addresses | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 | `1ca3b390a082` |
| `Tether USD(TRC20) Active Receiving Addresses (%) - Day.csv` | Tether USD(TRC20) Active Receiving Addresses (%) - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 | `08363ca97fd4` |
| `Tether USD(TRC20) Active Receiving Addresses - Day.csv` | Tether USD(TRC20) Active Receiving Addresses - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 | `674ea342d92e` |
| `Tether USD(TRC20) Active Sending Addresses (%) - Day.csv` | Tether USD(TRC20) Active Sending Addresses (%) - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 | `7689103cf215` |
| `Tether USD(TRC20) Active Sending Addresses - Day.csv` | Tether USD(TRC20) Active Sending Addresses - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 | `6e647dce5b02` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Tether USD(TRC20) Active Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Addresses
2019-07-01,2019-07-01T00:00:00Z,0
2019-07-02,2019-07-02T00:00:00Z,0
```

**`Tether USD(TRC20) Active Receiving Addresses (%) - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses (%)
2019-07-01,2019-07-01T00:00:00Z,0.0
2019-07-02,2019-07-02T00:00:00Z,0.0
```

**`Tether USD(TRC20) Active Receiving Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses
2019-07-01,2019-07-01T00:00:00Z,0
2019-07-02,2019-07-02T00:00:00Z,0
```

**`Tether USD(TRC20) Active Sending Addresses (%) - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses (%)
2019-07-01,2019-07-01T00:00:00Z,0.0
2019-07-02,2019-07-02T00:00:00Z,0.0
```

**`Tether USD(TRC20) Active Sending Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses
2019-07-01,2019-07-01T00:00:00Z,0
2019-07-02,2019-07-02T00:00:00Z,0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
