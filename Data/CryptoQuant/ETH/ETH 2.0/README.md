# CryptoQuant / ETH/ETH 2.0

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (8)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Cumulative TXs to ETH 2.0 Contract - Day.csv` | Ethereum Cumulative TXs to ETH 2.0 Contract - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 | `16ae248b1f3a` |
| `Ethereum ETH 2.0 Staking Rate (%) - Day.csv` | Ethereum ETH 2.0 Staking Rate (%) - Day | 2020-11-03 .. 2026-04-10 | 1,985 | daily | 0 | 3 | `de35e3ce0786` |
| `Ethereum New Depositors - Day.csv` | Ethereum New Depositors - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 | `08daf61b888d` |
| `Ethereum Number of ETH 2.0 Deposits - Day.csv` | Ethereum Number of ETH 2.0 Deposits - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 | `74c03b0c3d29` |
| `Ethereum Number of Unique Depositors - Day.csv` | Ethereum Number of Unique Depositors - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 | `ebb631c8ccc5` |
| `Ethereum Phase 0 Success Rate (%) - Day.csv` | Ethereum Phase 0 Success Rate (%) - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 | `76ed0490348b` |
| `Ethereum Staking Inflow Total - Day.csv` | Ethereum Staking Inflow Total - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 | `a30985244ccd` |
| `Ethereum Total Value Staked - Day.csv` | Ethereum Total Value Staked - Day | 2020-11-03 .. 2026-04-10 | 1,985 | daily | 0 | 3 | `30cf56c5e1ab` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Cumulative TXs to ETH 2.0 Contract - Day.csv`**

```csv
date,timestamp_utc,Cumulative TXs to ETH 2.0 Contract
2020-11-03,2020-11-03T00:00:00Z,1
2020-11-04,2020-11-04T00:00:00Z,368
```

**`Ethereum ETH 2.0 Staking Rate (%) - Day.csv`**

```csv
date,timestamp_utc,ETH 2.0 Staking Rate (%)
2020-11-03,2020-11-03T00:00:00Z,0.6
2020-11-04,2020-11-04T00:00:00Z,0.6
```

**`Ethereum New Depositors - Day.csv`**

```csv
date,timestamp_utc,New Depositors
2020-11-03,2020-11-03T00:00:00Z,0
2020-11-04,2020-11-04T00:00:00Z,367
```

**`Ethereum Number of ETH 2.0 Deposits - Day.csv`**

```csv
date,timestamp_utc,Number of ETH 2.0 Deposits
2020-11-03,2020-11-03T00:00:00Z,0
2020-11-04,2020-11-04T00:00:00Z,367
```

**`Ethereum Number of Unique Depositors - Day.csv`**

```csv
date,timestamp_utc,Number of Unique Depositors
2020-11-03,2020-11-03T00:00:00Z,1
2020-11-04,2020-11-04T00:00:00Z,368
```

**`Ethereum Phase 0 Success Rate (%) - Day.csv`**

```csv
date,timestamp_utc,Phase 0 Success Rate (%)
2020-11-03,2020-11-03T00:00:00Z,0.0
2020-11-04,2020-11-04T00:00:00Z,2.22
```

**`Ethereum Staking Inflow Total - Day.csv`**

```csv
date,timestamp_utc,Staking Inflow Total
2020-11-03,2020-11-03T00:00:00Z,0.0
2020-11-04,2020-11-04T00:00:00Z,11620.0
```

**`Ethereum Total Value Staked - Day.csv`**

```csv
date,timestamp_utc,Total Value Staked
2020-11-03,2020-11-03T00:00:00Z,674144.0
2020-11-04,2020-11-04T00:00:00Z,674144.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
