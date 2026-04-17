# DefiLlama / CSV/Daily

**Source**: https://api.llama.fi/ (via harvest_defillama_simple.py at repo root)

Programmatically generated TVL panels (all-chain aggregates and per-chain breakdowns), plus point-in-time snapshots of chains and protocols.

**Date convention**: Originally `Date` column; after curation it is `date` (ISO `YYYY-MM-DD`). Snapshot files (`Snapshot/`) have no date column.

**Units**: USD for TVL.

**Frequency hint**: Daily (`Daily/`) and Weekly (`Weekly/`) panels.

**Licensing**: DefiLlama public data.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `tvl_all_chains_daily.csv` | TVL | 2017-09-27 .. 2026-04-14 | 3,122 | daily | 0 | 2 | `af94d2971c65` |
| `tvl_by_chain_long_daily.csv` | TVL | 2017-09-27 .. 2024-09-13 | 200,000 | daily | 0 | 3 | `bcdb0331f10c` |
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
