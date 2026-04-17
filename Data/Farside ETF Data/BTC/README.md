# Farside ETF Data / BTC

**Source**: https://farside.co.uk/bitcoin-etf-flow-all-data/ (+ /ethereum/, /sol/)

Daily US$m net flows for US spot BTC, ETH, and SOL ETFs. See `Farside_ETF_Data_Summary.txt` for ticker list per asset.

**Date convention**: Originally `Date` (`YYYY-MM-DD`, trading-day cadence). After curation the column is lowercase `date`.

**Units**: US$m (millions of USD). Empty cells mean 'no flow / not applicable'; outflows are negative numbers.

**Frequency hint**: Trading-day daily (NYSE calendar; weekends and holidays absent).

**Licensing**: Farside publishes daily; treat attribution per their terms.

## Files (1)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `bitcoin_etf_flow_all_data.csv` | ETF | 2024-01-11 .. 2026-04-10 | 579 | daily | 242 | 14 | `1f080620fed7` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`bitcoin_etf_flow_all_data.csv`**

```csv
date,IBIT,FBTC,BITB,ARKB,BTCO,EZBC,BRRR,HODL,BTCW,... (+4 more)
2024-01-11,111.7,227.0,237.9,65.3,17.4,50.1,29.4,10.6,1.0
2024-01-12,386.0,195.3,17.4,39.8,28.4,0.0,20.2,0.0,0.0
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
