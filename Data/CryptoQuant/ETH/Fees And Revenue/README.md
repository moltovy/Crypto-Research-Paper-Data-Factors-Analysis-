# CryptoQuant / ETH/Fees And Revenue

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (9)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Fees (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `cdf51a7a93f6` |
| `Ethereum Fees Burnt (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `1224d51a755a` |
| `Ethereum Fees Burnt per Transaction (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `9aaf33531f53` |
| `Ethereum Fees Burnt per Transaction (Median) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `490a3b81c6db` |
| `Ethereum Fees Burnt per Transaction USD (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `f413f8523ed4` |
| `Ethereum Fees Burnt per Transaction USD (Median) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `e3c143402cd6` |
| `Ethereum Fees Burnt USD (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `043dc2ee1bd2` |
| `Ethereum Fees per Transaction (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `a4b384d7b70f` |
| `Ethereum Fees per Transaction USD (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `e552cd6f45b8` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Fees (Total) - Day.csv`**

```csv
date,Fees (Total)
2020-11-02,4397.645830555131
2020-11-03,3354.799838846664
```

**`Ethereum Fees Burnt (Total) - Day.csv`**

```csv
date,Fees Burnt (Total)
2020-11-02,
2020-11-03,
```

**`Ethereum Fees Burnt per Transaction (Mean) - Day.csv`**

```csv
date,Fees Burnt per Transaction (Mean)
2020-11-02,
2020-11-03,
```

**`Ethereum Fees Burnt per Transaction (Median) - Day.csv`**

```csv
date,Fees Burnt per Transaction (Median)
2020-11-02,
2020-11-03,
```

**`Ethereum Fees Burnt per Transaction USD (Mean) - Day.csv`**

```csv
date,Fees Burnt per Transaction USD (Mean)
2020-11-02,
2020-11-03,
```

**`Ethereum Fees Burnt per Transaction USD (Median) - Day.csv`**

```csv
date,Fees Burnt per Transaction USD (Median)
2020-11-02,
2020-11-03,
```

**`Ethereum Fees Burnt USD (Total) - Day.csv`**

```csv
date,Fees Burnt USD (Total)
2020-11-02,
2020-11-03,
```

**`Ethereum Fees per Transaction (Mean) - Day.csv`**

```csv
date,Fees per Transaction (Mean)
2020-11-02,0.0038013310316242
2020-11-03,0.0029970722876634
```

**`Ethereum Fees per Transaction USD (Mean) - Day.csv`**

```csv
date,Fees per Transaction USD (Mean)
2020-11-02,1.4568409358214172
2020-11-03,1.163201816521348
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
