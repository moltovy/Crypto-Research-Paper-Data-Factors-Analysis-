# CryptoQuant / ETH/Fees And Revenue

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (9)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Fees (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `25cf3a66d9d9` |
| `Ethereum Fees Burnt (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `8964de862210` |
| `Ethereum Fees Burnt per Transaction (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `5466aa4a2278` |
| `Ethereum Fees Burnt per Transaction (Median) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `0bec32485238` |
| `Ethereum Fees Burnt per Transaction USD (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `8a05b7e6b9e1` |
| `Ethereum Fees Burnt per Transaction USD (Median) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `9a1c046ca61c` |
| `Ethereum Fees Burnt USD (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `a328b80061d6` |
| `Ethereum Fees per Transaction (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `69f67ef91caa` |
| `Ethereum Fees per Transaction USD (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `6c68c07fdfb7` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Fees (Total) - Day.csv`**

```csv
date,timestamp_utc,Fees (Total)
2020-11-02,2020-11-02T00:00:00Z,4397.645830555131
2020-11-03,2020-11-03T00:00:00Z,3354.799838846664
```

**`Ethereum Fees Burnt (Total) - Day.csv`**

```csv
date,timestamp_utc,Fees Burnt (Total)
2020-11-02,2020-11-02T00:00:00Z,
2020-11-03,2020-11-03T00:00:00Z,
```

**`Ethereum Fees Burnt per Transaction (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees Burnt per Transaction (Mean)
2020-11-02,2020-11-02T00:00:00Z,
2020-11-03,2020-11-03T00:00:00Z,
```

**`Ethereum Fees Burnt per Transaction (Median) - Day.csv`**

```csv
date,timestamp_utc,Fees Burnt per Transaction (Median)
2020-11-02,2020-11-02T00:00:00Z,
2020-11-03,2020-11-03T00:00:00Z,
```

**`Ethereum Fees Burnt per Transaction USD (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees Burnt per Transaction USD (Mean)
2020-11-02,2020-11-02T00:00:00Z,
2020-11-03,2020-11-03T00:00:00Z,
```

**`Ethereum Fees Burnt per Transaction USD (Median) - Day.csv`**

```csv
date,timestamp_utc,Fees Burnt per Transaction USD (Median)
2020-11-02,2020-11-02T00:00:00Z,
2020-11-03,2020-11-03T00:00:00Z,
```

**`Ethereum Fees Burnt USD (Total) - Day.csv`**

```csv
date,timestamp_utc,Fees Burnt USD (Total)
2020-11-02,2020-11-02T00:00:00Z,
2020-11-03,2020-11-03T00:00:00Z,
```

**`Ethereum Fees per Transaction (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees per Transaction (Mean)
2020-11-02,2020-11-02T00:00:00Z,0.0038013310316242
2020-11-03,2020-11-03T00:00:00Z,0.0029970722876634
```

**`Ethereum Fees per Transaction USD (Mean) - Day.csv`**

```csv
date,timestamp_utc,Fees per Transaction USD (Mean)
2020-11-02,2020-11-02T00:00:00Z,1.4568409358214172
2020-11-03,2020-11-03T00:00:00Z,1.163201816521348
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
