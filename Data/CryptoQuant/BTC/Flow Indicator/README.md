# CryptoQuant / BTC/Flow Indicator

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (7)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Exchange Inflow CDD - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 2 | `31a28d91579e` |
| `Bitcoin Exchange Stablecoins Ratio - All Exchanges - Day.csv` | Stablecoin | 2023-07-16 .. 2026-04-10 | 1,000 | daily | 0 | 2 | `bce256ca2090` |
| `Bitcoin Exchange Stablecoins Ratio USD - All Exchanges - Day.csv` | Stablecoin | 2023-07-16 .. 2026-04-10 | 1,000 | daily | 0 | 2 | `004c2315316d` |
| `Bitcoin Exchange Supply Ratio - All Exchanges - Day.csv` | Bitcoin Exchange Supply Ratio - All Exchanges - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `6fb2bb20ef0f` |
| `Bitcoin Exchange Whale Ratio - All Exchanges - Day.csv` | Bitcoin Exchange Whale Ratio - All Exchanges - Day | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 2 | `67df1e86d9ab` |
| `Bitcoin Fund Flow Ratio - All Exchanges - Day.csv` | Bitcoin Fund Flow Ratio - All Exchanges - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `8336b0985b93` |
| `Bitcoin Stablecoin Supply Ratio (SSR) - Day.csv` | Stablecoin | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 2 | `ea4fb23c0abf` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Exchange Inflow CDD - All Exchanges - Day.csv`**

```csv
date,Exchange Inflow CDD
2012-04-02,0.10099236
2012-04-03,0.0
```

**`Bitcoin Exchange Stablecoins Ratio - All Exchanges - Day.csv`**

```csv
date,Exchange Stablecoins Ratio
2023-07-16,9.911e-05
2023-07-17,9.988e-05
```

**`Bitcoin Exchange Stablecoins Ratio USD - All Exchanges - Day.csv`**

```csv
date,Exchange Stablecoins Ratio USD
2023-07-16,2.97593134
2023-07-17,3.00691482
```

**`Bitcoin Exchange Supply Ratio - All Exchanges - Day.csv`**

```csv
date,Exchange Supply Ratio
2009-01-03,0.0
2009-01-04,0.0
```

**`Bitcoin Exchange Whale Ratio - All Exchanges - Day.csv`**

```csv
date,Exchange Whale Ratio
2012-04-02,1.0
2012-04-03,0.0
```

**`Bitcoin Fund Flow Ratio - All Exchanges - Day.csv`**

```csv
date,Fund Flow Ratio
2009-01-03,
2009-01-04,
```

**`Bitcoin Stablecoin Supply Ratio (SSR) - Day.csv`**

```csv
date,Stablecoin Supply Ratio (SSR)
2020-12-31,28.46344983
2021-01-01,28.39368116
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
