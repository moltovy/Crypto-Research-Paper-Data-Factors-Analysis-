# Farside ETF Data / ETH

**Source**: https://farside.co.uk/bitcoin-etf-flow-all-data/ (+ /ethereum/, /sol/)

Daily US$m net flows for US spot BTC, ETH, and SOL ETFs. See `Farside_ETF_Data_Summary.txt` for ticker list per asset.

**Date convention**: Originally `Date` (`YYYY-MM-DD`, trading-day cadence). After curation the column is lowercase `date`.

**Units**: US$m (millions of USD). Empty cells mean 'no flow / not applicable'; outflows are negative numbers.

**Frequency hint**: Trading-day daily (NYSE calendar; weekends and holidays absent).

**Licensing**: Farside publishes daily; treat attribution per their terms.

## Files (1)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `ethereum_etf_flow_all_data.csv` | ETF | 2024-07-23 .. 2026-04-10 | 441 | daily | 186 | 12 | `5c43700e3eb2` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`ethereum_etf_flow_all_data.csv`**

```csv
date,ETHA,ETHB,FETH,ETHW,TETH,ETHV,QETH,EZET,ETHE,... (+2 more)
2024-07-23,266.5,,71.3,204.0,7.5,7.6,5.5,13.2,-484.1
2024-07-24,17.4,,74.5,29.6,0.0,19.8,2.5,3.9,-326.9
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
