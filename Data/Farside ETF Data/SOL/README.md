# Farside ETF Data / SOL

**Source**: https://farside.co.uk/bitcoin-etf-flow-all-data/ (+ /ethereum/, /sol/)

Daily US$m net flows for US spot BTC, ETH, and SOL ETFs. See `Farside_ETF_Data_Summary.txt` for ticker list per asset.

**Date convention**: Originally `Date` (`YYYY-MM-DD`, trading-day cadence). After curation the column is lowercase `date`.

**Units**: US$m (millions of USD). Empty cells mean 'no flow / not applicable'; outflows are negative numbers.

**Frequency hint**: Trading-day daily (NYSE calendar; weekends and holidays absent).

**Licensing**: Farside publishes daily; treat attribution per their terms.

## Files (1)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `solana_etf_flow_all_data.csv` | ETF | 2026-03-25 .. 2026-04-10 | 12 | daily | 5 | 8 | `6524141f4c18` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`solana_etf_flow_all_data.csv`**

```csv
date,BSOL,VSOL,FSOL,TSOL,SOEZ,GSOL,Total
2026-03-25,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2026-03-26,0.0,-0.3,-0.8,0.0,0.0,0.0,-1.1
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
