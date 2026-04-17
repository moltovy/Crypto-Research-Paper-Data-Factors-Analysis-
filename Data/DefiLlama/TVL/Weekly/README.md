# DefiLlama / TVL/Weekly

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
| `tvl_all_chains_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 447 | weekly | — | 2 | `6c58b587f7e8` |
| `tvl_by_chain_long_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 60,392 | weekly | — | 3 | `124e2a07aa40` |
| `tvl_by_chain_wide_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 447 | weekly | — | 440 | `12091949b380` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`tvl_all_chains_weekly.csv`**

```csv
date,TVL
2017-10-01,0
2017-10-08,0
```

**`tvl_by_chain_long_weekly.csv`**

```csv
date,Chain,TVL
2017-10-01,Ethereum,0
2017-10-08,Ethereum,0
```

**`tvl_by_chain_wide_weekly.csv`**

```csv
date,0g,ab,ailayer,alv,ao,abstract,acala,aeternity,agoric,... (+430 more)
2017-10-01,,,,,,,,,
2017-10-08,,,,,,,,,
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
