# FRED

**Source**: https://fred.stlouisfed.org/

Macro / rates / liquidity / sentiment series pulled from the St Louis Fed `fred/series/observations` endpoint. Each series has its own 2-column CSV (`date,value`) plus one combined wide panel (`fred_macro_panel__daily.csv`) and a metadata table (`fred_series_metadata.csv`).

**Date convention**: `date` is ISO `YYYY-MM-DD` ascending. Missing observations (FRED `.` sentinel) are written as empty cells.

**Units**: Per-series — see `fred_series_metadata.csv` (column `units`).

> Note: Re-runnable via `python tools/data_collection/fetch_fred.py` (requires `FRED_API_KEY` in `.env`).

**Frequency hint**: Mix of daily, weekly, and monthly; the combined panel is daily-aligned.

**Licensing**: FRED data is public-domain / Federal Reserve Bank of St. Louis.

## Files (21)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `ANFCI__weekly.csv` | FRED: Chicago Fed NFCI | 1971-01-08 .. 2026-04-10 | 2,884 | weekly | — | 2 | `2a87235d93d2` |
| `BAMLH0A0HYM2__daily.csv` | FRED: High-yield OAS spread | 2023-04-18 .. 2026-04-16 | 795 | daily | 300 | 2 | `c126f47d5a57` |
| `CPIAUCSL__monthly.csv` | FRED: CPI headline | 1947-01-01 .. 2026-03-01 | 951 | monthly | — | 2 | `bbd9dfe3f10d` |
| `DCOILWTICO__daily.csv` | FRED: WTI crude oil | 1986-01-02 .. 2026-04-13 | 10,508 | daily | 4204 | 2 | `4bc7f7cdd03d` |
| `DFF__daily.csv` | FRED: Fed Funds Effective Rate | 1954-07-01 .. 2026-04-16 | 26,223 | daily | 0 | 2 | `4edce3e70283` |
| `DFII10__daily.csv` | FRED: 10Y TIPS (real yield) | 2003-01-02 .. 2026-04-16 | 6,076 | daily | 2430 | 2 | `2da223ef9a55` |
| `DGS10__daily.csv` | FRED: 10Y Treasury yield | 1962-01-02 .. 2026-04-16 | 16,773 | daily | 6708 | 2 | `fb4c00d50a81` |
| `DGS2__daily.csv` | FRED: 2Y Treasury yield | 1976-06-01 .. 2026-04-16 | 13,013 | daily | 5204 | 2 | `3ab5e6ee77a2` |
| `DGS30__daily.csv` | FRED: 30Y Treasury yield | 1977-02-15 .. 2026-04-16 | 12,828 | daily | 5130 | 2 | `9fe78b9cf8f0` |
| `DTWEXBGS__daily.csv` | FRED: Broad USD trade-weighted index | 2006-01-02 .. 2026-04-10 | 5,290 | daily | 2114 | 2 | `96be7f5af79a` |
| `fred_macro_panel__daily.csv` | FRED: combined daily panel | 1954-07-01 .. 2026-04-17 | 18,732 | daily | 7492 | 14 | `3a3a4bf96341` |
| `fred_series_metadata.csv` | FRED: series metadata | — | 19 | snapshot | — | 13 | `f7c14ed0611b` |
| `NFCI__weekly.csv` | FRED: Chicago Fed NFCI | 1971-01-08 .. 2026-04-10 | 2,884 | weekly | — | 2 | `ae1ef2006ad0` |
| `RRPONTSYD__daily.csv` | FRED: Reverse-repo facility | 2003-02-07 .. 2026-04-17 | 6,051 | daily | 2420 | 2 | `9ca37ac154a2` |
| `SOFR__daily.csv` | FRED: SOFR overnight rate | 2018-04-03 .. 2026-04-16 | 2,098 | daily | 838 | 2 | `12c6db914ae5` |
| `STLFSI4__weekly.csv` | FRED: St Louis Financial Stress Index | 1993-12-31 .. 2026-04-10 | 1,685 | weekly | — | 2 | `eb3de71df43a` |
| `T10Y2Y__daily.csv` | FRED: 10Y-2Y term spread | 1976-06-01 .. 2026-04-17 | 13,014 | daily | 5204 | 2 | `e1fb6f27b2e2` |
| `UNRATE__monthly.csv` | FRED: Unemployment rate | 1948-01-01 .. 2026-03-01 | 939 | monthly | — | 2 | `1b2d13330fb4` |
| `USEPUINDXD__daily.csv` | FRED: Economic Policy Uncertainty | 1985-01-01 .. 2026-04-15 | 15,080 | daily | 0 | 2 | `a76696dcc7f5` |
| `VIXCLS__daily.csv` | FRED: VIX | 1990-01-02 .. 2026-04-16 | 9,468 | daily | 3786 | 2 | `ebe60c5bf60a` |
| `WALCL__weekly.csv` | FRED: Fed balance sheet total assets | 2002-12-18 .. 2026-04-15 | 1,218 | weekly | — | 2 | `1894afa3df6d` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`ANFCI__weekly.csv`**

```csv
date,value
1971-01-08,0.513
1971-01-15,0.575
```

**`BAMLH0A0HYM2__daily.csv`**

```csv
date,value
2023-04-18,4.37
2023-04-19,4.41
```

**`CPIAUCSL__monthly.csv`**

```csv
date,value
1947-01-01,21.48
1947-02-01,21.62
```

**`DCOILWTICO__daily.csv`**

```csv
date,value
1986-01-02,25.56
1986-01-03,26.0
```

**`DFF__daily.csv`**

```csv
date,value
1954-07-01,1.13
1954-07-02,1.25
```

**`DFII10__daily.csv`**

```csv
date,value
2003-01-02,2.43
2003-01-03,2.43
```

**`DGS10__daily.csv`**

```csv
date,value
1962-01-02,4.06
1962-01-03,4.03
```

**`DGS2__daily.csv`**

```csv
date,value
1976-06-01,7.26
1976-06-02,7.23
```

**`DGS30__daily.csv`**

```csv
date,value
1977-02-15,7.7
1977-02-16,7.67
```

**`DTWEXBGS__daily.csv`**

```csv
date,value
2006-01-02,101.4155
2006-01-03,100.7558
```

**`fred_macro_panel__daily.csv`**

```csv
date,DGS10,DGS2,DGS30,DFII10,T10Y2Y,SOFR,DFF,BAMLH0A0HYM2,VIXCLS,... (+4 more)
1954-07-01,,,,,,,1.13,,
1954-07-02,,,,,,,1.25,,
```

**`fred_series_metadata.csv`**

```csv
id,title,units,frequency,seasonal_adjustment,observation_start,observation_end,last_updated,notes,category,... (+3 more)
DGS10,Market Yield on U.S. Treasury Securit...,%,Daily,NSA,1962-01-02,2026-04-16,2026-04-17 15:16:35-05,H.15 Statistical Release (https://www...,rates_curve
DGS2,Market Yield on U.S. Treasury Securit...,%,Daily,NSA,1976-06-01,2026-04-16,2026-04-17 15:16:42-05,H.15 Statistical Release notes (https...,rates_curve
```

_(9 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
