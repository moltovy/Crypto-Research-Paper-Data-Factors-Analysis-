# DefiLlama / CSV/Snapshot

**Source**: https://api.llama.fi/ (via harvest_defillama_simple.py at repo root)

Programmatically generated TVL panels (all-chain aggregates and per-chain breakdowns), plus point-in-time snapshots of chains and protocols.

**Date convention**: Originally `Date` column; after curation it is `date` (ISO `YYYY-MM-DD`). Snapshot files (`Snapshot/`) have no date column.

**Units**: USD for TVL.

**Frequency hint**: Daily (`Daily/`) and Weekly (`Weekly/`) panels.

**Licensing**: DefiLlama public data.

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
