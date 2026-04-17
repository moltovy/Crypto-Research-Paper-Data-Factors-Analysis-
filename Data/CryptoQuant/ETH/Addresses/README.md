# CryptoQuant / ETH/Addresses

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (6)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Active Addresses - Day.csv` | Active addresses | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `0b7391a1f21e` |
| `Ethereum Active Addresses - Internal, External, EOA - Day.csv` | Active addresses | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 | `170a0bf05af8` |
| `Ethereum Active Receiving Addresses - Day.csv` | Ethereum Active Receiving Addresses - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `7df97612a5fe` |
| `Ethereum Active Receiving Addresses - Internal, External, EOA - Day.csv` | Ethereum Active Receiving Addresses - Internal, External, EOA - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 | `f75a4de640f8` |
| `Ethereum Active Sending Addresses - Day.csv` | Ethereum Active Sending Addresses - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `038fc75062fc` |
| `Ethereum Active Sending Addresses - Internal, External, EOA - Day.csv` | Ethereum Active Sending Addresses - Internal, External, EOA - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 | `8a2a89511e7f` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Active Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Addresses
2020-11-02,2020-11-02T00:00:00Z,316567
2020-11-03,2020-11-03T00:00:00Z,307180
```

**`Ethereum Active Addresses - Internal, External, EOA - Day.csv`**

```csv
date,timestamp_utc,Active Addresses -  Internal, External, EOA
2020-11-02,2020-11-02T00:00:00Z,473277,,
2020-11-03,2020-11-03T00:00:00Z,449977,,
```

**`Ethereum Active Receiving Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses
2020-11-02,2020-11-02T00:00:00Z,228147
2020-11-03,2020-11-03T00:00:00Z,221136
```

**`Ethereum Active Receiving Addresses - Internal, External, EOA - Day.csv`**

```csv
date,timestamp_utc,Active Receiving Addresses - Internal, External, EOA
2020-11-02,2020-11-02T00:00:00Z,322570,,
2020-11-03,2020-11-03T00:00:00Z,298324,,
```

**`Ethereum Active Sending Addresses - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses
2020-11-02,2020-11-02T00:00:00Z,180350
2020-11-03,2020-11-03T00:00:00Z,177858
```

**`Ethereum Active Sending Addresses - Internal, External, EOA - Day.csv`**

```csv
date,timestamp_utc,Active Sending Addresses - Internal, External, EOA
2020-11-02,2020-11-02T00:00:00Z,357277,,
2020-11-03,2020-11-03T00:00:00Z,350898,,
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
