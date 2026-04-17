# Tradingview / Daily

**Source**: https://www.tradingview.com/

Manual chart-to-CSV exports from TradingView. Organised into two subfolders: `Daily/` (1D bars — CME BTC/ETH/Micro BTC/Micro ETH/SOL futures, CME basis and ratio series, spot-proxy ETFs, miner/crypto stocks, Deribit DVOL, IBIT/ETHA ETF premiums, DXY) and `Weekly/` (1W continuous contracts, index ETFs, commodities).

**Date convention**: Originally `time` as Unix epoch seconds. After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column — no `timestamp_utc`.

**Units**: OHLC in instrument quote currency; Volume in contracts / shares; Open Interest in contracts.

> Note: These files explicitly cover CME BTC/ETH futures, which CryptoQuant aggregates away. DXY files were deduplicated by keeping the longest-history version.

**Frequency hint**: Daily bars under `Daily/`, weekly bars under `Weekly/`.

**Licensing**: TradingView chart data is for research use only; redistribution restricted.

## Files (27)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `ARKK_innovation_etf__daily.csv` | ETF | 2014-10-31 .. 2026-04-17 | 2,873 | daily | 1314 | 11 | `d75b926e85ac` |
| `CME_BTC_front_month_futures__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,096 | daily | 946 | 11 | `abb1d7e30e63` |
| `CME_BTC_futures_minus_SPOT_BTC_basis__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,102 | daily | 940 | 11 | `004221e53a1c` |
| `CME_BTC_futures_over_SPOT_BTC_ratio__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,102 | daily | 940 | 11 | `16f9323ab557` |
| `CME_ETH_front_month_futures__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,307 | daily | 590 | 11 | `df626c05f6ac` |
| `CME_ETH_futures_minus_SPOT_ETH_basis__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,308 | daily | 589 | 11 | `76e7fe6588a3` |
| `CME_ETH_futures_over_SPOT_ETH_ratio__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,308 | daily | 589 | 11 | `067c1a021d28` |
| `CME_Micro_Bitcoin_futures__daily.csv` | CME Micro BTC futures | 2018-03-25 .. 2026-04-15 | 1,685 | daily | 1259 | 11 | `f9133442ef9b` |
| `CME_Micro_Ether_futures__daily.csv` | CME Micro ETH futures | 2021-12-01 .. 2026-04-15 | 1,099 | daily | 498 | 11 | `ce024fea16aa` |
| `CME_Solana_futures__daily.csv` | Solana | 2025-03-16 .. 2026-04-15 | 274 | daily | 122 | 11 | `0b34a29ba9a4` |
| `COIN_coinbase_stock__daily.csv` | COIN_coinbase_stock__daily | 2021-04-14 .. 2026-04-17 | 1,259 | daily | 571 | 11 | `8d79f5ff8c58` |
| `CRCL_circle_stock__daily.csv` | CRCL_circle_stock__daily | 2025-06-05 .. 2026-04-17 | 218 | daily | 99 | 11 | `54e615f579d4` |
| `Deribit_BTC_volatility_index_DVOL__daily.csv` | Deribit volatility index | 2021-03-24 .. 2026-04-16 | 1,850 | daily | 0 | 5 | `766d13db14a8` |
| `DXY_us_dollar_index__daily.csv` | DXY_us_dollar_index__daily | 2007-06-13 .. 2026-04-16 | 4,768 | daily | 2115 | 11 | `29f215890669` |
| `ETHA_ETF_over_SPOT_ETH__daily.csv` | ETF | 2024-07-23 .. 2026-04-16 | 435 | daily | 198 | 11 | `a0eb44df6098` |
| `GLD_gold_etf__daily.csv` | ETF | 2007-03-23 .. 2026-04-17 | 4,798 | daily | 2168 | 11 | `8e59a863b2d2` |
| `IBIT_ETF_over_SPOT_BTC__daily.csv` | ETF | 2024-01-11 .. 2026-04-16 | 567 | daily | 260 | 11 | `e5c685249ee2` |
| `IWM_russell2000_etf__daily.csv` | ETF | 2009-01-30 .. 2026-04-17 | 4,330 | daily | 1957 | 11 | `9d6b3a343aed` |
| `MARA_marathon_miner_stock__daily.csv` | MARA_marathon_miner_stock__daily | 2012-02-09 .. 2026-04-17 | 3,351 | daily | 1831 | 11 | `8073169ee589` |
| `MSTR_microstrategy_stock__daily.csv` | MSTR_microstrategy_stock__daily | 2010-09-08 .. 2026-04-17 | 3,926 | daily | 1775 | 11 | `e8a5b96cc9f8` |
| `QQQ_nasdaq100_etf__daily.csv` | ETF | 2007-07-20 .. 2026-04-17 | 4,716 | daily | 2131 | 11 | `7aac761e1799` |
| `RIOT_riot_miner_stock__daily.csv` | RIOT_riot_miner_stock__daily | 2011-03-14 .. 2026-04-17 | 3,797 | daily | 1717 | 11 | `0da6ad3cdcd4` |
| `SMH_vaneck_semiconductor_etf__daily.csv` | ETF | 2009-01-29 .. 2026-04-17 | 4,330 | daily | 1958 | 11 | `50104f127990` |
| `SOXX_ishares_semiconductor_etf__daily.csv` | ETF | 2007-05-09 .. 2026-04-17 | 4,766 | daily | 2153 | 11 | `867959844073` |
| `SPY_sp500_etf__daily.csv` | ETF | 2012-04-30 .. 2026-04-17 | 3,512 | daily | 1589 | 11 | `49a3578437df` |
| `XAUUSD_gold_spot__daily.csv` | XAUUSD_gold_spot__daily | 2021-08-01 .. 2026-04-16 | 1,216 | daily | 504 | 11 | `609b818406bf` |
| `XLK_tech_sector_etf__daily.csv` | ETF | 2007-03-09 .. 2026-04-17 | 4,808 | daily | 2172 | 11 | `ae3da3df7885` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`ARKK_innovation_etf__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2014-10-31,20.42,20.42,20.38,20.38,2661,,,,
2014-11-03,20.49,20.49,20.35,20.38,2270,,,,
```

**`CME_BTC_front_month_futures__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2017-12-17,20650,20650,18345,19100,1054,215,,,
2017-12-18,19135,19725,17180,18200,559,231,,,
```

**`CME_BTC_futures_minus_SPOT_BTC_basis__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2017-12-17,1521.6775000000016,1521.6775000000016,151.08000000000175,151.08000000000175,53763.87804825,,,,
2017-12-18,186.1525000000001,660.8525000000009,186.1525000000001,505.1899999999987,71126.17363502,,,,
```

**`CME_BTC_futures_over_SPOT_BTC_ratio__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2017-12-17,1.0795510165619595,1.0795510165619595,1.0079730137654284,1.0079730137654284,53763.87804825,,,,
2017-12-18,1.0098239483958062,1.0346646761938871,1.0098239483958062,1.028550179402887,71126.17363502,,,,
```

**`CME_ETH_front_month_futures__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-02-04,1745.0,1745.0,1745.0,1745.0,280,0,,,
2021-02-07,1669.75,1793.25,1604.25,1751.75,303,171,,,
```

**`CME_ETH_futures_minus_SPOT_ETH_basis__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-02-04,146.885,152.90249999999992,-19.36500000000001,23.762500000000045,666960.75824011,,,,
2021-02-07,54.382499999999936,54.382499999999936,-1.3424999999999727,-1.3424999999999727,742156.19297846,,,,
```

**`CME_ETH_futures_over_SPOT_ETH_ratio__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-02-04,1.0919114081277004,1.0960384021707212,0.989024379876046,1.0138054742590723,666960.75824011,,,,
2021-02-07,1.0336657138391108,1.0336657138391108,0.9992342104024744,0.9992342104024744,742156.19297846,,,,
```

**`CME_Micro_Bitcoin_futures__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2018-03-25,0.9,0.9,0.2,0.2,0,0,,,
2018-03-26,0.5,0.5,0.5,0.5,0,0,,,
```

**`CME_Micro_Ether_futures__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-12-01,4543.5,4543.5,4543.5,4543.5,0,0,,,
2021-12-02,4214.0,4214.0,4214.0,4214.0,143,0,,,
```

**`CME_Solana_futures__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2025-03-16,126.0,130.5,124.7,129.85,192,119,,,
2025-03-17,129.2,129.2,122.05,124.2,165,101,,,
```

**`COIN_coinbase_stock__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2021-04-14,381.0,429.54,310.0,328.28,81065746,,,,
2021-04-15,348.9,349.2,317.2701,322.75,39777858,,,,
```

**`CRCL_circle_stock__daily.csv`**

```csv
date,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,Open Interest (Low),... (+1 more)
2025-06-05,69.0,103.75,64.0,83.23,47784339,,,,
2025-06-06,96.39,123.515,92.95,107.7,60706262,,,,
```

_(15 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
