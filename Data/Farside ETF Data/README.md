# Farside ETF Data

**Source**: https://farside.co.uk/bitcoin-etf-flow-all-data/ (+ /ethereum/, /sol/)

Daily US$m net flows for US spot BTC, ETH, and SOL ETFs. See `Farside_ETF_Data_Summary.txt` for ticker list per asset.

**Date convention**: Originally `Date` (`YYYY-MM-DD`, trading-day cadence). After curation the column is lowercase `date`.

**Units**: US$m (millions of USD). Empty cells mean 'no flow / not applicable'; outflows are negative numbers.

**Frequency hint**: Trading-day daily (NYSE calendar; weekends and holidays absent).

**Licensing**: Farside publishes daily; treat attribution per their terms.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `farside_btc_etf_flows__daily.csv` | ETF | 2024-01-11 .. 2026-04-10 | 579 | daily | 242 | 14 | `1f080620fed7` |
| `farside_eth_etf_flows__daily.csv` | ETF | 2024-07-23 .. 2026-04-10 | 441 | daily | 186 | 12 | `5c43700e3eb2` |
| `farside_sol_etf_flows__daily.csv` | ETF | 2026-03-25 .. 2026-04-10 | 12 | daily | 5 | 8 | `6524141f4c18` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`farside_btc_etf_flows__daily.csv`**

```csv
date,IBIT,FBTC,BITB,ARKB,BTCO,EZBC,BRRR,HODL,BTCW,... (+4 more)
2024-01-11,111.7,227.0,237.9,65.3,17.4,50.1,29.4,10.6,1.0
2024-01-12,386.0,195.3,17.4,39.8,28.4,0.0,20.2,0.0,0.0
```

**`farside_eth_etf_flows__daily.csv`**

```csv
date,ETHA,ETHB,FETH,ETHW,TETH,ETHV,QETH,EZET,ETHE,... (+2 more)
2024-07-23,266.5,,71.3,204.0,7.5,7.6,5.5,13.2,-484.1
2024-07-24,17.4,,74.5,29.6,0.0,19.8,2.5,3.9,-326.9
```

**`farside_sol_etf_flows__daily.csv`**

```csv
date,BSOL,VSOL,FSOL,TSOL,SOEZ,GSOL,Total
2026-03-25,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2026-03-26,0.0,-0.3,-0.8,0.0,0.0,0.0,-1.1
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
