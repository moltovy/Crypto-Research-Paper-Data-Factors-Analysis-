# Tradingview / Weekly

**Source**: https://www.tradingview.com/

Manual chart-to-CSV exports from TradingView. Organised into two subfolders: `Daily/` (1D bars — CME BTC/ETH/Micro BTC/Micro ETH/SOL futures, CME basis and ratio series, spot-proxy ETFs, miner/crypto stocks, Deribit DVOL, IBIT/ETHA ETF premiums, DXY) and `Weekly/` (1W continuous contracts, index ETFs, commodities).

**Date convention**: Originally `time` as Unix epoch seconds. After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column — no `timestamp_utc`.

**Units**: OHLC in instrument quote currency; Volume in contracts / shares; Open Interest in contracts.

> Note: These files explicitly cover CME BTC/ETH futures, which CryptoQuant aggregates away. DXY files were deduplicated by keeping the longest-history version.

**Frequency hint**: Daily bars under `Daily/`, weekly bars under `Weekly/`.

**Licensing**: TradingView chart data is for research use only; redistribution restricted.

## Files (11)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `CME_BTC1_continuous_futures__weekly.csv` | CME BTC futures | 2017-12-17 .. 2026-04-12 | 435 | weekly | — | 11 | `7010acf5b6a4` |
| `CME_ETH1_continuous_futures__weekly.csv` | CME ETH futures | 2021-01-31 .. 2026-04-12 | 272 | weekly | — | 11 | `b52289abe1cc` |
| `CME_Micro_Bitcoin_MBT1_continuous__weekly.csv` | CME Micro BTC futures | 2018-03-25 .. 2026-04-12 | 350 | weekly | — | 11 | `e529031639d0` |
| `CME_Micro_Ether_MET1_continuous__weekly.csv` | CME Micro ETH futures | 2021-11-28 .. 2026-04-12 | 229 | weekly | — | 11 | `1c1396d7b4d9` |
| `COIN_coinbase_stock__weekly.csv` | COIN_coinbase_stock__weekly | 2021-04-12 .. 2026-04-13 | 262 | weekly | — | 11 | `f030b1ad1181` |
| `DXY_us_dollar_index__weekly.csv` | DXY_us_dollar_index__weekly | 1967-01-29 .. 2026-04-12 | 2,933 | weekly | — | 11 | `9a620dc85a81` |
| `MSTR_microstrategy_stock__weekly.csv` | MSTR_microstrategy_stock__weekly | 2011-07-11 .. 2026-04-13 | 771 | weekly | — | 11 | `9aee62acf384` |
| `QQQ_nasdaq100_etf__weekly.csv` | ETF | 2005-10-17 .. 2026-04-13 | 1,070 | weekly | — | 11 | `3ffdff9bc20c` |
| `RIOT_riot_miner_stock__weekly.csv` | RIOT_riot_miner_stock__weekly | 2003-01-21 .. 2026-04-13 | 1,204 | weekly | — | 11 | `b1103f12f737` |
| `SPY_sp500_etf__weekly.csv` | ETF | 1993-01-25 .. 2026-04-13 | 1,734 | weekly | — | 11 | `342070f09761` |
| `XAUUSD_gold_spot__weekly.csv` | XAUUSD_gold_spot__weekly | 1992-04-19 .. 2026-04-12 | 1,748 | weekly | — | 11 | `2ab8c2d68282` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`CME_BTC1_continuous_futures__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2017-12-17,20650,20650,12265,14135,5650,489,,,
2017-12-24,13900,16545,13360,14470,2737,498,,,
```

**`CME_ETH1_continuous_futures__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-01-31,1745.0,1745.0,1745.0,1745.0,280,0,,,
2021-02-07,1669.75,1879.75,1604.25,1868.25,1478,451,,,
```

**`CME_Micro_Bitcoin_MBT1_continuous__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2018-03-25,0.9,0.9,0.2,0.6,0,0,,,
2018-04-01,0.8,1.0,-0.7,1.0,0,0,,,
```

**`CME_Micro_Ether_MET1_continuous__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-11-28,4543.5,4543.5,4214.0,4214.0,143,0,,,
2021-12-05,4199.5,4505.0,3930.0,4040.0,19826,2339,,,
```

**`COIN_coinbase_stock__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-04-12,381.0,429.54,310.0,342.0,143498146,,,,
2021-04-19,337.26,341.01,282.07,291.6,64474796,,,,
```

**`DXY_us_dollar_index__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
1967-01-29,119.89,119.89,119.89,119.89,,,,,
1967-02-26,119.81,119.81,119.81,119.81,,,,,
```

**`MSTR_microstrategy_stock__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2011-07-11,16.302,17.645,15.606,16.969,12377550,,,,
2011-07-18,16.942999,17.858,16.432001,17.167999,7949150,,,,
```

**`QQQ_nasdaq100_etf__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2005-10-17,38.06,38.86,37.61,38.55,527982432,,,,
2005-10-24,38.71201,39.274,37.92,38.32201,519587744,,,,
```

**`RIOT_riot_miner_stock__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2003-01-21,480.0,936.0,480.0,936.0,72,,,,
2003-01-27,936.0,1116.0,816.0,816.0,161,,,,
```

**`SPY_sp500_etf__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
1993-01-25,43.9688,43.96899,43.75,43.938,1003200,,,,
1993-02-01,43.96875,45.09375,43.96875,44.96875,2234800,,,,
```

**`XAUUSD_gold_spot__weekly.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
1992-04-19,338.6,343.0,336.7,337.5,0,,,,
1992-04-26,337.5,339.4,334.9,339.3,0,,,,
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
