# DefiLlama / CSV/Weekly

**Source**: https://api.llama.fi/ (via harvest_defillama_simple.py at repo root)

Programmatically generated TVL panels (all-chain aggregates and per-chain breakdowns), plus point-in-time snapshots of chains and protocols.

**Date convention**: Originally `Date` column; after curation it is `date` (ISO `YYYY-MM-DD`). Snapshot files (`Snapshot/`) have no date column.

**Units**: USD for TVL.

**Frequency hint**: Daily (`Daily/`) and Weekly (`Weekly/`) panels.

**Licensing**: DefiLlama public data.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `tvl_all_chains_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 447 | weekly | — | 2 | `6c58b587f7e8` |
| `tvl_by_chain_long_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 60,392 | weekly | — | 3 | `91c9918609bf` |
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
