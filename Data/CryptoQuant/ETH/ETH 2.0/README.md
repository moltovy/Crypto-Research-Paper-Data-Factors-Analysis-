# CryptoQuant / ETH/ETH 2.0

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (8)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Cumulative TXs to ETH 2.0 Contract - Day.csv` | Ethereum Cumulative TXs to ETH 2.0 Contract - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 2 | `08ae5f170b65` |
| `Ethereum ETH 2.0 Staking Rate (%) - Day.csv` | Ethereum ETH 2.0 Staking Rate (%) - Day | 2020-11-03 .. 2026-04-10 | 1,985 | daily | 0 | 2 | `83f5b37e6024` |
| `Ethereum New Depositors - Day.csv` | Ethereum New Depositors - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 2 | `cbfe9de83f03` |
| `Ethereum Number of ETH 2.0 Deposits - Day.csv` | Ethereum Number of ETH 2.0 Deposits - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 2 | `038d9db77145` |
| `Ethereum Number of Unique Depositors - Day.csv` | Ethereum Number of Unique Depositors - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 2 | `7ea6334138fd` |
| `Ethereum Phase 0 Success Rate (%) - Day.csv` | Ethereum Phase 0 Success Rate (%) - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 2 | `004e15854fe6` |
| `Ethereum Staking Inflow Total - Day.csv` | Ethereum Staking Inflow Total - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 2 | `a8756a6498c6` |
| `Ethereum Total Value Staked - Day.csv` | Ethereum Total Value Staked - Day | 2020-11-03 .. 2026-04-10 | 1,985 | daily | 0 | 2 | `4399a411b126` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Cumulative TXs to ETH 2.0 Contract - Day.csv`**

```csv
date,Cumulative TXs to ETH 2.0 Contract
2020-11-03,1
2020-11-04,368
```

**`Ethereum ETH 2.0 Staking Rate (%) - Day.csv`**

```csv
date,ETH 2.0 Staking Rate (%)
2020-11-03,0.6
2020-11-04,0.6
```

**`Ethereum New Depositors - Day.csv`**

```csv
date,New Depositors
2020-11-03,0
2020-11-04,367
```

**`Ethereum Number of ETH 2.0 Deposits - Day.csv`**

```csv
date,Number of ETH 2.0 Deposits
2020-11-03,0
2020-11-04,367
```

**`Ethereum Number of Unique Depositors - Day.csv`**

```csv
date,Number of Unique Depositors
2020-11-03,1
2020-11-04,368
```

**`Ethereum Phase 0 Success Rate (%) - Day.csv`**

```csv
date,Phase 0 Success Rate (%)
2020-11-03,0.0
2020-11-04,2.22
```

**`Ethereum Staking Inflow Total - Day.csv`**

```csv
date,Staking Inflow Total
2020-11-03,0.0
2020-11-04,11620.0
```

**`Ethereum Total Value Staked - Day.csv`**

```csv
date,Total Value Staked
2020-11-03,674144.0
2020-11-04,674144.0
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
