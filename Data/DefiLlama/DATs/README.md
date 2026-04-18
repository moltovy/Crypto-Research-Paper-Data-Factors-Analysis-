# DefiLlama / DATs

**Source**: https://defillama.com/ + https://api.llama.fi/ (programmatic via harvest_defillama_simple.py)

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

**Date convention**: Originally mixed (`date`, `Date`, `day`, `Timestamp+Date`). After curation every time-series file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column. Snapshot entity lists (`Stablecoins/stablecoins.csv`, `DATs/dat-institutions.csv`, `ETFs/etf-overview.csv`, `TVL/Snapshot/*`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part website exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`. `TVL/` is the only subfolder managed by `harvest_defillama_simple.py`; the others are manual UI exports.

**Frequency hint**: Daily for time-series; `TVL/` also has Weekly aggregates; Snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (1)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `dat-institutions.csv` | Public-company digital-asset treasuries | — | 86 | snapshot | — | 11 | `4743249d89d9` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`dat-institutions.csv`**

```csv
ticker,name,type,price,priceChange24h,volume24h,mcapRealized,realized_mNAV,totalUsdValue,totalCost,... (+1 more)
MSTR,Strategy, Inc. (Formerly: MicroStrate...,Stock,132.36000061,2.891792006871815,12370800.0,51789425149.91897,0.9543192801119242,54268446870.15546,58055861719.0
BMNR,BitMine Immersion Technologies, Inc.,Stock,21.51000023,1.0808248709694843,54464200.0,9784091425.628365,0.9278018391795634,10545453794.616571,
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
