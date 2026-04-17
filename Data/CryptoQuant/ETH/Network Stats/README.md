# CryptoQuant / ETH/Network Stats

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
| `Ethereum Destroyed Contracts - Day.csv` | Ethereum Destroyed Contracts - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `b77fa3bedd00` |
| `Ethereum New Contracts - Day.csv` | Ethereum New Contracts - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `4af3c8c0ef0b` |
| `Ethereum Number of Contracts - Day.csv` | Ethereum Number of Contracts - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 | `97c1a2a2ee3e` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Destroyed Contracts - Day.csv`**

```csv
date,timestamp_utc,Destroyed Contracts
2020-11-02,2020-11-02T00:00:00Z,29662
2020-11-03,2020-11-03T00:00:00Z,22467
```

**`Ethereum New Contracts - Day.csv`**

```csv
date,timestamp_utc,New Contracts
2020-11-02,2020-11-02T00:00:00Z,26385
2020-11-03,2020-11-03T00:00:00Z,63768
```

**`Ethereum Number of Contracts - Day.csv`**

```csv
date,timestamp_utc,Number of Contracts
2020-11-02,2020-11-02T00:00:00Z,19107945
2020-11-03,2020-11-03T00:00:00Z,19149246
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
