# DefiLlama / TVL/Snapshot

**Source**: https://defillama.com/ + https://api.llama.fi/ (programmatic via harvest_defillama_simple.py)

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

**Date convention**: Originally mixed (`date`, `Date`, `day`, `Timestamp+Date`). After curation every time-series file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column. Snapshot entity lists (`Stablecoins/stablecoins.csv`, `DATs/dat-institutions.csv`, `ETFs/etf-overview.csv`, `TVL/Snapshot/*`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part website exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`. `TVL/` is the only subfolder managed by `harvest_defillama_simple.py`; the others are manual UI exports.

**Frequency hint**: Daily for time-series; `TVL/` also has Weekly aggregates; Snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (2)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `tvl_chains_current.csv` | TVL | — | 440 | snapshot | — | 6 | `7668362522c5` |
| `tvl_protocols_current.csv` | TVL | — | 7,317 | snapshot | — | 56 | `75b1b5a82d59` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`tvl_chains_current.csv`**

```csv
gecko_id,tvl,tokensymbol,cmcid,name,chainid
ethereum,55619604790.62701,ETH,1027.0,Ethereum,1.0
solana,5795365523.651363,SOL,5426.0,Solana,
```

**`tvl_protocols_current.csv`**

```csv
id,name,address,symbol,url,description,chain,logo,audits,gecko_id,... (+46 more)
2269,Binance CEX,,BNB,https://www.binance.com,Binance is a cryptocurrency exchange ...,Multi-Chain,https://icons.llama.fi/binance-cex.jpg,0.0,
1599,Aave V3,0x7fc66500c84a76ad7e9c93437bfc5ac33e2...,AAVE,https://aave.com,Earn interest, borrow assets, and bui...,Multi-Chain,https://icons.llama.fi/aave-v3.png,2.0,
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
