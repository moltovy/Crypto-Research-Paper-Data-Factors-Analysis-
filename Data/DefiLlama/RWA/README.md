# DefiLlama / RWA

**Source**: https://defillama.com/ + https://api.llama.fi/ (programmatic via harvest_defillama_simple.py)

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

**Date convention**: Originally mixed (`date`, `Date`, `day`, `Timestamp+Date`). After curation every time-series file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column. Snapshot entity lists (`Stablecoins/stablecoins.csv`, `DATs/dat-institutions.csv`, `ETFs/etf-overview.csv`, `TVL/Snapshot/*`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part website exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`. `TVL/` is the only subfolder managed by `harvest_defillama_simple.py`; the others are manual UI exports.

**Frequency hint**: Daily for time-series; `TVL/` also has Weekly aggregates; Snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (5)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `rwa_active_mcap_all__daily.csv` | rwa_active_mcap_all__daily | 2021-09-04 .. 2026-04-17 | 1,687 | daily | 0 | 22 | `955e3b36b4f0` |
| `rwa_defi_active_tvl_all__daily.csv` | TVL | 2021-10-25 .. 2026-04-14 | 1,633 | daily | 0 | 19 | `27d4bb2df5f1` |
| `rwa_mcap_by_category__daily.csv` | rwa_mcap_by_category__daily | 2021-09-04 .. 2026-04-17 | 1,687 | daily | 0 | 13 | `f12c25e59199` |
| `rwa_onchain_mcap_all__daily.csv` | rwa_onchain_mcap_all__daily | 2021-09-04 .. 2026-04-17 | 1,687 | daily | 0 | 24 | `acfff04ac634` |
| `rwa_onchain_mcap_by_platform__daily.csv` | rwa_onchain_mcap_by_platform__daily | 2021-09-04 .. 2026-04-17 | 1,687 | daily | 0 | 63 | `efffe6e33a92` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`rwa_active_mcap_all__daily.csv`**

```csv
date,Total Active Mcap,Bonds,Precious Metals,Private Credit,Public Equities,Reinsurance,Digital Assets,Private Equity & Venture,Equity Indices,... (+12 more)
2021-09-04,355043159.0,,339983760.0,,,,,,
2021-09-05,353464278.0,,338799850.0,,,,,,
```

**`rwa_defi_active_tvl_all__daily.csv`**

```csv
date,Private Credit,Bonds,Real Estate,Reinsurance,Precious Metals,Digital Assets,Private Equity & Venture,Public Equities,Equity Indices,... (+9 more)
2021-10-25,,,,,,,,,
2021-10-26,,,,,,,,,
```

**`rwa_mcap_by_category__daily.csv`**

```csv
date,all_Carbon & Environment,all_Gold & Commodities,all_Stocks & Equities,all_Real Estate,all_Bond & MMF Funds,all_RWA Wrappers,all_Private Credit,all_Crypto Funds,all_ETFs,... (+3 more)
2021-09-04,15059399.0,339983760.0,52577555.0,0.0,0.0,0.0,0.0,0.0,0.0
2021-09-05,14664428.0,338799850.0,43089293.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`rwa_onchain_mcap_all__daily.csv`**

```csv
date,Total Onchain Mcap,Bonds,Precious Metals,Private Credit,Public Equities,Real Estate,Reinsurance,Digital Assets,Private Equity & Venture,... (+14 more)
2021-09-04,407620714.0,,339983760.0,,,,,,52577555.0
2021-09-05,396553571.0,,338799850.0,,,,,,43089293.0
```

**`rwa_onchain_mcap_by_platform__daily.csv`**

```csv
date,Total Onchain Mcap,Securitize,Maple,Tether,Ondo,Circle,Paxos,Centrifuge,Spiko,... (+53 more)
2021-09-04,407620714.0,,,,,,332696137.0,,
2021-09-05,396553571.0,,,,,,331519881.0,,
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
