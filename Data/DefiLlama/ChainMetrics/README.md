# DefiLlama / ChainMetrics

**Source**: https://defillama.com/ + https://api.llama.fi/ (programmatic via harvest_defillama_simple.py)

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

**Date convention**: Originally mixed (`date`, `Date`, `day`, `Timestamp+Date`). After curation every time-series file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column. Snapshot entity lists (`Stablecoins/stablecoins.csv`, `DATs/dat-institutions.csv`, `ETFs/etf-overview.csv`, `TVL/Snapshot/*`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part website exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`. `TVL/` is the only subfolder managed by `harvest_defillama_simple.py`; the others are manual UI exports.

**Frequency hint**: Daily for time-series; `TVL/` also has Weekly aggregates; Snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (7)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `all_chains_metrics__daily.csv` | all_chains_metrics__daily | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 40 | `31867e37a761` |
| `all_chains_perp_volume_by_protocol__daily.csv` | all_chains_perp_volume_by_protocol__daily | 2021-02-25 .. 2026-04-17 | 1,878 | daily | 0 | 180 | `b7d5be0abade` |
| `all_dex_metrics__daily.csv` | all_dex_metrics__daily | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 5 | `998a1b09201c` |
| `chain_revenue_combined__daily.csv` | chain_revenue_combined__daily | 2018-08-18 .. 2026-04-17 | 2,793 | daily | 7 | 2 | `99bed5d7e506` |
| `chain_tvl_dominance__daily.csv` | TVL | 2020-08-04 .. 2026-04-15 | 521 | ~4d | — | 457 | `ff2983d343fe` |
| `ethereum_metrics__daily.csv` | ethereum_metrics__daily | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 | `73234f10b224` |
| `solana_metrics__daily.csv` | Solana | 2021-03-18 .. 2026-04-17 | 1,857 | daily | 0 | 38 | `118d38aace55` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`all_chains_metrics__daily.csv`**

```csv
date,tvl_tvl,tvl_staking,tvl_pool2,tvl_borrowed,tvl_doublecounted,tvl_vesting,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_treasury,... (+30 more)
2016-04-19,,,,,,,,,
2016-04-20,,,,,,,,,
```

**`all_chains_perp_volume_by_protocol__daily.csv`**

```csv
date,Hyperliquid,Aster,edgeX,Lighter,Grvt,ApeX Protocol,Variational,Pacifica,StandX,... (+170 more)
2021-02-25,,,,,,,,,
2021-02-26,,,,,,,,,
```

**`all_dex_metrics__daily.csv`**

```csv
date,TVL,DEXs Volume,Perps Volume,Stablecoins Mcap
2016-04-19,,607.0,,
2016-04-20,,1728.0,,
```

**`chain_revenue_combined__daily.csv`**

```csv
date,all
2018-08-18,8
2018-08-19,26
```

**`chain_tvl_dominance__daily.csv`**

```csv
date,Ethereum,Tron,Celo,AB,Tezos,Polygon,BSC,Kava,Terra Classic,... (+447 more)
2020-08-04,94.74384572891252,0.5048692034696479,4.751285067617815,,,,,,
2020-08-08,95.25657664996838,0.5003984216260704,4.243024928405544,,,,,,
```

**`ethereum_metrics__daily.csv`**

```csv
date,tvl_tvl,tvl_staking,tvl_pool2,tvl_borrowed,tvl_doublecounted,tvl_vesting,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_Masterchef,... (+38 more)
2017-09-27,0,,,,,,,,
2017-09-28,0,,,,,,,,
```

**`solana_metrics__daily.csv`**

```csv
date,tvl_tvl,tvl_doublecounted,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_staking,tvl_borrowed,tvl_pool2,tvl_vesting,tvl_OwnTokens,... (+28 more)
2021-03-18,148988798,,,,,,,,
2021-03-19,153204289,,,,,,,,
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
