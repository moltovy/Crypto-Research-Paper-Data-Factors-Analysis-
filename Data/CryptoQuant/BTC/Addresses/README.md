# CryptoQuant / BTC/Addresses

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
| `Bitcoin Active Addresses - Day.csv` | Active addresses | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `ab77f7ddb8fd` |
| `Bitcoin Active Receiving Addresses - Day.csv` | Bitcoin Active Receiving Addresses - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `5ce95f3c3c56` |
| `Bitcoin Active Sending Addresses - Day.csv` | Bitcoin Active Sending Addresses - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `5b63b770e502` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Active Addresses - Day.csv`**

```csv
date,Active Addresses
2009-01-03,1
2009-01-04,0
```

**`Bitcoin Active Receiving Addresses - Day.csv`**

```csv
date,Active Receiving Addresses
2009-01-03,1
2009-01-04,0
```

**`Bitcoin Active Sending Addresses - Day.csv`**

```csv
date,Active Sending Addresses
2009-01-03,0
2009-01-04,0
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
