# DefiLlama / Stablecoins

**Source**: https://defillama.com/ + https://api.llama.fi/ (programmatic via harvest_defillama_simple.py)

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

**Date convention**: Originally mixed (`date`, `Date`, `day`, `Timestamp+Date`). After curation every time-series file has `date` (ISO `YYYY-MM-DD`, UTC) as its first column. Snapshot entity lists (`Stablecoins/stablecoins.csv`, `DATs/dat-institutions.csv`, `ETFs/etf-overview.csv`, `TVL/Snapshot/*`) have no date column.

**Units**: USD for all flow / mcap / TVL / fees / revenue / volume figures unless stated.

> Note: Multi-part website exports (stablecoin-mcap parts 1..7, cex-inflows parts 1..3) were merged via outer join on `date`. Originals are archived under `_raw_parts/`. `TVL/` is the only subfolder managed by `harvest_defillama_simple.py`; the others are manual UI exports.

**Frequency hint**: Daily for time-series; `TVL/` also has Weekly aggregates; Snapshots are point-in-time.

**Licensing**: DefiLlama data is free and public; attribution is appreciated.

## Files (4)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `stablecoin_mcap_by_defillama_id__daily.csv` | Stablecoin | 2017-11-29 .. 2026-04-17 | 3,062 | daily | 0 | 201 | `80c661791efa` |
| `stablecoin_mcap_id_to_name.csv` | Stablecoin | — | 200 | snapshot | — | 4 | `832b0277c455` |
| `stablecoins-chains.csv` | Stablecoin | — | 175 | snapshot | — | 3 | `c964f70eb32c` |
| `stablecoins.csv` | Stablecoin | — | 360 | snapshot | — | 10 | `b0be302a115e` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`stablecoin_mcap_by_defillama_id__daily.csv`**

```csv
date,165,202,282,245,244,247,242,46,51,... (+191 more)
2017-11-29,,,,,,,,,
2017-11-30,,,,,,,,,
```

**`stablecoin_mcap_id_to_name.csv`**

```csv
defillama_id,name,symbol,pegType
165.0,,,
202.0,,,
```

**`stablecoins-chains.csv`**

```csv
name,tokenSymbol,totalCirculatingUSD
Ethereum,ETH,166965875107.55618
Tron,TRON,86956659514.15155
```

**`stablecoins.csv`**

```csv
name,symbol,pegType,pegMechanism,circulating,circulatingPrevDay,circulatingPrevWeek,circulatingPrevMonth,chains,price
Tether,USDT,peggedUSD,fiat-backed,{"peggedUSD":185800396864.63583},{"peggedUSD":185468907564.97412},{"peggedUSD":184102575595.57303},{"peggedUSD":184062297760.86575},Tron, Ethereum, BSC, Solana, Plasma, ...,1.00011983686696
USD Coin,USDC,peggedUSD,fiat-backed,{"peggedUSD":78765092743.57936},{"peggedUSD":78863449534.77673},{"peggedUSD":78183197916.39285},{"peggedUSD":79289211604.47865},Ethereum, Solana, Hyperliquid L1, Bas...,0.9998596133049042
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
