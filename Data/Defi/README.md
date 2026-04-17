# Defi

**Source**: https://defillama.com/ (website export UI) + https://api.llama.fi/

Manual chart / dashboard exports from DefiLlama plus curated slices (stablecoins, CEX net inflows, ETFs, RWA categories, chain-level metrics).

**Date convention**: Originally mixed (`date`, `day`, `Timestamp+Date`). After curation every file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column where a date axis exists. Snapshot entity lists (`stablecoins.csv`, `dat-institutions.csv`, `etf-overview.csv`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`.

**Frequency hint**: Daily for time-series; snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (18)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `all_metrics_2026-04-17 (1) volume.csv` | all_metrics_2026-04-17 (1) volume | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 38 | `c6cd5c47b6b7` |
| `all_metrics_2026-04-17.csv` | all_metrics_2026-04-17 | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 40 | `31867e37a761` |
| `cex_net_inflows_by_exchange__daily.csv` | CEX net inflows | 2022-11-12 .. 2026-04-17 | 1,253 | daily | 0 | 76 | `f7427a64c432` |
| `dat-institutions.csv` | Public-company digital-asset treasuries | — | 86 | snapshot | — | 11 | `4743249d89d9` |
| `etf-history.csv` | ETF | 2024-01-11 .. 2026-04-14 | 565 | daily | 260 | 3 | `540236f084cc` |
| `etf-overview.csv` | ETF | — | 25 | snapshot | — | 6 | `515d406f7184` |
| `ethereum_metrics_2026-04-17 (1).csv` | ethereum_metrics_2026-04-17 (1) | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 | `0be6076357d4` |
| `ethereum_metrics_2026-04-17 Fees and revenue.csv` | Fees | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 | `2740d69b8394` |
| `ethereum_metrics_2026-04-17 volume.csv` | ethereum_metrics_2026-04-17 volume | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 | `73234f10b224` |
| `rwa-category-chart_combined_2026-04-17.csv` | Real-world assets (RWA) | 2021-09-04 .. 2026-04-17 | 1,687 | daily | 0 | 13 | `f12c25e59199` |
| `rwa-time-series-chart-active-mcap-all-2026-04-14.csv` | Real-world assets (RWA) | 2021-09-04 .. 2026-04-14 | 1,684 | daily | 0 | 19 | `9ba4134e36de` |
| `rwa-time-series-chart-defi-active-tvl-all-2026-04-14.csv` | TVL | 2021-10-25 .. 2026-04-14 | 1,633 | daily | 0 | 19 | `27d4bb2df5f1` |
| `rwa-time-series-chart-onchain-mcap-all-2026-04-14.csv` | Real-world assets (RWA) | 2021-09-04 .. 2026-04-14 | 1,684 | daily | 0 | 22 | `511a75a79f80` |
| `solana_metrics_2026-04-17.csv` | Solana | 2021-03-18 .. 2026-04-17 | 1,857 | daily | 0 | 38 | `118d38aace55` |
| `stablecoin_mcap_by_defillama_id__daily.csv` | Stablecoin | 2017-11-29 .. 2026-04-17 | 3,062 | daily | 0 | 201 | `80c661791efa` |
| `stablecoin_mcap_id_to_name.csv` | Stablecoin | — | 200 | snapshot | — | 4 | `832b0277c455` |
| `stablecoins-chains.csv` | Stablecoin | — | 175 | snapshot | — | 3 | `c964f70eb32c` |
| `stablecoins.csv` | Stablecoin | — | 360 | snapshot | — | 10 | `b0be302a115e` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`all_metrics_2026-04-17 (1) volume.csv`**

```csv
date,tvl_tvl,tvl_staking,tvl_pool2,tvl_borrowed,tvl_doublecounted,tvl_vesting,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_treasury,... (+28 more)
2016-04-19,,,,,,,,,
2016-04-20,,,,,,,,,
```

**`all_metrics_2026-04-17.csv`**

```csv
date,tvl_tvl,tvl_staking,tvl_pool2,tvl_borrowed,tvl_doublecounted,tvl_vesting,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_treasury,... (+30 more)
2016-04-19,,,,,,,,,
2016-04-20,,,,,,,,,
```

**`cex_net_inflows_by_exchange__daily.csv`**

```csv
date,binance-cex,okx,bitfinex,bybit,robinhood,bitget,gemini,htx,gate,... (+66 more)
2022-11-12,,2009512288.0,115636918.0,,,,,,
2022-11-13,-485659141.0,,-79894640.0,,,,,,
```

**`dat-institutions.csv`**

```csv
ticker,name,type,price,priceChange24h,volume24h,mcapRealized,realized_mNAV,totalUsdValue,totalCost,... (+1 more)
MSTR,Strategy, Inc. (Formerly: MicroStrate...,Stock,132.36000061,2.891792006871815,12370800.0,51789425149.91897,0.9543192801119242,54268446870.15546,58055861719.0
BMNR,BitMine Immersion Technologies, Inc.,Stock,21.51000023,1.0808248709694843,54464200.0,9784091425.628365,0.9278018391795634,10545453794.616571,
```

**`etf-history.csv`**

```csv
date,gecko_id,total_flow_usd
2024-01-11,bitcoin,655300000
2024-01-12,bitcoin,203000000
```

**`etf-overview.csv`**

```csv
Ticker,Issuer,Coin,Flows,AUM,Volume
GBTC,Grayscale,Bitcoin,15500000,10487256064.0,189476321.7
BSOL,Bitwise,Solana,0,,31404298.32
```

**`ethereum_metrics_2026-04-17 (1).csv`**

```csv
date,tvl_tvl,tvl_staking,tvl_pool2,tvl_borrowed,tvl_doublecounted,tvl_vesting,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_Masterchef,... (+38 more)
2017-09-27,0,,,,,,,,
2017-09-28,0,,,,,,,,
```

**`ethereum_metrics_2026-04-17 Fees and revenue.csv`**

```csv
date,tvl_tvl,tvl_staking,tvl_pool2,tvl_borrowed,tvl_doublecounted,tvl_vesting,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_Masterchef,... (+38 more)
2017-09-27,0,,,,,,,,
2017-09-28,0,,,,,,,,
```

**`ethereum_metrics_2026-04-17 volume.csv`**

```csv
date,tvl_tvl,tvl_staking,tvl_pool2,tvl_borrowed,tvl_doublecounted,tvl_vesting,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_Masterchef,... (+38 more)
2017-09-27,0,,,,,,,,
2017-09-28,0,,,,,,,,
```

**`rwa-category-chart_combined_2026-04-17.csv`**

```csv
date,all_Carbon & Environment,all_Gold & Commodities,all_Stocks & Equities,all_Real Estate,all_Bond & MMF Funds,all_RWA Wrappers,all_Private Credit,all_Crypto Funds,all_ETFs,... (+3 more)
2021-09-04,15059399.0,339983760.0,52577555.0,0.0,0.0,0.0,0.0,0.0,0.0
2021-09-05,14664428.0,338799850.0,43089293.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`rwa-time-series-chart-active-mcap-all-2026-04-14.csv`**

```csv
date,Bonds,Precious Metals,Private Credit,Public Equities,Reinsurance,Digital Assets,Private Equity & Venture,Equity Indices,Equity ETFs,... (+9 more)
2021-09-04,,339983760.0,,,,,,,
2021-09-05,,338799850.0,,,,,,,
```

**`rwa-time-series-chart-defi-active-tvl-all-2026-04-14.csv`**

```csv
date,Private Credit,Bonds,Real Estate,Reinsurance,Precious Metals,Digital Assets,Private Equity & Venture,Public Equities,Equity Indices,... (+9 more)
2021-10-25,,,,,,,,,
2021-10-26,,,,,,,,,
```

_(6 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
