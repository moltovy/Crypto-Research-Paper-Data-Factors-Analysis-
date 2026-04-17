# DefiLlama / TVL/Daily

**Source**: https://defillama.com/ + https://api.llama.fi/ (programmatic via harvest_defillama_simple.py)

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

**Date convention**: Originally mixed (`date`, `Date`, `day`, `Timestamp+Date`). After curation every time-series file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column. Snapshot entity lists (`Stablecoins/stablecoins.csv`, `DATs/dat-institutions.csv`, `ETFs/etf-overview.csv`, `TVL/Snapshot/*`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part website exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`. `TVL/` is the only subfolder managed by `harvest_defillama_simple.py`; the others are manual UI exports.

**Frequency hint**: Daily for time-series; `TVL/` also has Weekly aggregates; Snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `tvl_all_chains_daily.csv` | TVL | 2017-09-27 .. 2026-04-14 | 3,122 | daily | 0 | 2 | `af94d2971c65` |
| `tvl_by_chain_long_daily.csv` | TVL | 2017-09-27 .. 2024-09-13 | 200,000 | daily | 0 | 3 | `e7f1961b573b` |
| `tvl_by_chain_wide_daily.csv` | TVL | 2017-09-27 .. 2026-04-14 | 3,122 | daily | 0 | 440 | `f49692cf767a` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`tvl_all_chains_daily.csv`**

```csv
date,TVL
2017-09-27,0
2017-09-28,0
```

**`tvl_by_chain_long_daily.csv`**

```csv
date,TVL,Chain
2017-09-27,0,Ethereum
2017-09-28,0,Ethereum
```

**`tvl_by_chain_wide_daily.csv`**

```csv
date,0g,ab,ailayer,alv,ao,abstract,acala,aeternity,agoric,... (+430 more)
2017-09-27,,,,,,,,,
2017-09-28,,,,,,,,,
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
