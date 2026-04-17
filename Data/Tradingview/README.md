# Tradingview

**Source**: https://www.tradingview.com/

Manual chart-to-CSV exports from TradingView for CME futures (BTC, ETH, Micro BTC, Micro ETH, SOL), BlackRock ETF-vs-spot ratios (IBIT, ETHA), and Deribit's DVOL.

**Date convention**: Originally `time` as Unix epoch seconds. After curation each file has `date` (ISO `YYYY-MM-DD`) plus `timestamp_utc` (full ISO-8601 UTC).

**Units**: OHLC in instrument quote currency; Volume in contracts; Open Interest in contracts.

> Note: These files explicitly cover CME BTC/ETH futures, which CryptoQuant aggregates away.

**Frequency hint**: Daily (1D) bars, trading-day cadence for CME (no weekends / holidays).

**Licensing**: TradingView chart data is for research use only; redistribution restricted.

## Files (12)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `tradingview__CME_BTC_front_month_futures__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,096 | daily | 946 | 12 | `07ce06acc033` |
| `tradingview__CME_BTC_futures_minus_SPOT_BTC_basis__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,102 | daily | 940 | 12 | `867ed3e5d679` |
| `tradingview__CME_BTC_futures_over_SPOT_BTC_ratio__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,102 | daily | 940 | 12 | `4cdbd7f5e3e4` |
| `tradingview__CME_ETH_front_month_futures__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,307 | daily | 590 | 12 | `387f5cbcda31` |
| `tradingview__CME_ETH_futures_minus_SPOT_ETH_basis__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,308 | daily | 589 | 12 | `fc9e2ff8bc47` |
| `tradingview__CME_ETH_futures_over_SPOT_ETH_ratio__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,308 | daily | 589 | 12 | `4971c5b6094b` |
| `tradingview__CME_Micro_Bitcoin_futures__daily.csv` | CME Micro BTC futures | 2018-03-25 .. 2026-04-15 | 1,685 | daily | 1259 | 12 | `e147bb5787c4` |
| `tradingview__CME_Micro_Ether_futures__daily.csv` | CME Micro ETH futures | 2021-12-01 .. 2026-04-15 | 1,099 | daily | 498 | 12 | `527b185a6914` |
| `tradingview__CME_Solana_futures__daily.csv` | Solana | 2025-03-16 .. 2026-04-15 | 274 | daily | 122 | 12 | `f6bdbd749a85` |
| `tradingview__Deribit_BTC_volatility_index_DVOL__daily.csv` | Deribit volatility index | 2021-03-24 .. 2026-04-16 | 1,850 | daily | 0 | 6 | `05b3fd315404` |
| `tradingview__ETHA_ETF_over_SPOT_ETH__daily.csv` | ETF | 2024-07-23 .. 2026-04-16 | 435 | daily | 198 | 12 | `630c8f2b8ae0` |
| `tradingview__IBIT_ETF_over_SPOT_BTC__daily.csv` | ETF | 2024-01-11 .. 2026-04-16 | 567 | daily | 260 | 12 | `b6bdde9855b5` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`tradingview__CME_BTC_front_month_futures__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2017-12-17,2017-12-17T23:00:00Z,20650,20650,18345,19100,1054,215,,
2017-12-18,2017-12-18T23:00:00Z,19135,19725,17180,18200,559,231,,
```

**`tradingview__CME_BTC_futures_minus_SPOT_BTC_basis__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2017-12-17,2017-12-17T23:00:00Z,1521.6775000000016,1521.6775000000016,151.08000000000175,151.08000000000175,53763.87804825,,,
2017-12-18,2017-12-18T23:00:00Z,186.1525000000001,660.8525000000009,186.1525000000001,505.1899999999987,71126.17363502,,,
```

**`tradingview__CME_BTC_futures_over_SPOT_BTC_ratio__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2017-12-17,2017-12-17T23:00:00Z,1.0795510165619595,1.0795510165619595,1.0079730137654284,1.0079730137654284,53763.87804825,,,
2017-12-18,2017-12-18T23:00:00Z,1.0098239483958062,1.0346646761938871,1.0098239483958062,1.028550179402887,71126.17363502,,,
```

**`tradingview__CME_ETH_front_month_futures__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2021-02-04,2021-02-04T23:00:00Z,1745.0,1745.0,1745.0,1745.0,280,0,,
2021-02-07,2021-02-07T23:00:00Z,1669.75,1793.25,1604.25,1751.75,303,171,,
```

**`tradingview__CME_ETH_futures_minus_SPOT_ETH_basis__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2021-02-04,2021-02-04T23:00:00Z,146.885,152.90249999999992,-19.36500000000001,23.762500000000045,666960.75824011,,,
2021-02-07,2021-02-07T23:00:00Z,54.382499999999936,54.382499999999936,-1.3424999999999727,-1.3424999999999727,742156.19297846,,,
```

**`tradingview__CME_ETH_futures_over_SPOT_ETH_ratio__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2021-02-04,2021-02-04T23:00:00Z,1.0919114081277004,1.0960384021707212,0.989024379876046,1.0138054742590723,666960.75824011,,,
2021-02-07,2021-02-07T23:00:00Z,1.0336657138391108,1.0336657138391108,0.9992342104024744,0.9992342104024744,742156.19297846,,,
```

**`tradingview__CME_Micro_Bitcoin_futures__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2018-03-25,2018-03-25T22:00:00Z,0.9,0.9,0.2,0.2,0,0,,
2018-03-26,2018-03-26T22:00:00Z,0.5,0.5,0.5,0.5,0,0,,
```

**`tradingview__CME_Micro_Ether_futures__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2021-12-01,2021-12-01T23:00:00Z,4543.5,4543.5,4543.5,4543.5,0,0,,
2021-12-02,2021-12-02T23:00:00Z,4214.0,4214.0,4214.0,4214.0,143,0,,
```

**`tradingview__CME_Solana_futures__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2025-03-16,2025-03-16T22:00:00Z,126.0,130.5,124.7,129.85,192,119,,
2025-03-17,2025-03-17T22:00:00Z,129.2,129.2,122.05,124.2,165,101,,
```

**`tradingview__Deribit_BTC_volatility_index_DVOL__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close
2021-03-24,2021-03-24T00:00:00Z,84.8,95.94,80.52,95.04
2021-03-25,2021-03-25T00:00:00Z,95.03,97.43,87.25,89.74
```

**`tradingview__ETHA_ETF_over_SPOT_ETH__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2024-07-23,2024-07-23T13:30:00Z,0.0077243294590645,0.0077243294590645,0.0075117291373791,0.0075318539440335,10022445.00101999,,,
2024-07-24,2024-07-24T13:30:00Z,0.0075509278658225,0.0077151191496708,0.0075427052329128,0.0076410217993857,10233426.44241432,,,
```

**`tradingview__IBIT_ETF_over_SPOT_BTC__daily.csv`**

```csv
date,timestamp_utc,open,high,low,close,Volume,Open Interest,Open Interest (Open),Open Interest (High,... (+2 more)
2024-01-11,2024-01-11T14:30:00Z,0.0005986438167849,0.0006125565517313,0.0005745846721609,0.0005745846721609,37763715.24955933,,,
2024-01-12,2024-01-12T14:30:00Z,0.0005696642153123,0.0005966372799704,0.0005678159510917,0.0005835471487166,23057050.88870057,,,
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
