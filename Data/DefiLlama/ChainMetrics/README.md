# DefiLlama / ChainMetrics

**Source**: https://defillama.com/ + https://api.llama.fi/ (programmatic via harvest_defillama_simple.py)

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

**Date convention**: Originally mixed (`date`, `Date`, `day`, `Timestamp+Date`). After curation every time-series file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column. Snapshot entity lists (`Stablecoins/stablecoins.csv`, `DATs/dat-institutions.csv`, `ETFs/etf-overview.csv`, `TVL/Snapshot/*`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part website exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`. `TVL/` is the only subfolder managed by `harvest_defillama_simple.py`; the others are manual UI exports.

**Frequency hint**: Daily for time-series; `TVL/` also has Weekly aggregates; Snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (6)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `all_metrics_2026-04-17 (1) volume.csv` | all_metrics_2026-04-17 (1) volume | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 38 | `c6cd5c47b6b7` |
| `all_metrics_2026-04-17.csv` | all_metrics_2026-04-17 | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 40 | `31867e37a761` |
| `ethereum_metrics_2026-04-17 (1).csv` | ethereum_metrics_2026-04-17 (1) | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 | `0be6076357d4` |
| `ethereum_metrics_2026-04-17 Fees and revenue.csv` | Fees | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 | `2740d69b8394` |
| `ethereum_metrics_2026-04-17 volume.csv` | ethereum_metrics_2026-04-17 volume | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 | `73234f10b224` |
| `solana_metrics_2026-04-17.csv` | Solana | 2021-03-18 .. 2026-04-17 | 1,857 | daily | 0 | 38 | `118d38aace55` |

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

**`solana_metrics_2026-04-17.csv`**

```csv
date,tvl_tvl,tvl_doublecounted,tvl_liquidstaking,tvl_dcAndLsOverlap,tvl_staking,tvl_borrowed,tvl_pool2,tvl_vesting,tvl_OwnTokens,... (+28 more)
2021-03-18,148988798,,,,,,,,
2021-03-19,153204289,,,,,,,,
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
