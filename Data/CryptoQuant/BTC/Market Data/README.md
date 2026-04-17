# CryptoQuant / BTC/Market Data

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (20)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Average Cap - Day.csv` | Bitcoin Average Cap - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `178ba9df5ac8` |
| `Bitcoin Delta Cap - Day.csv` | Bitcoin Delta Cap - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `5508817bdfe8` |
| `Bitcoin Exchange Supply - Day.csv` | Bitcoin Exchange Supply - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 8 | `f7762c598c15` |
| `Bitcoin Geographical Supply Distribution by Entities - Day.csv` | Bitcoin Geographical Supply Distribution by Entities - Day | 2006-04-11 .. 2026-04-10 | 7,305 | daily | 0 | 5 | `f80a85faf704` |
| `Bitcoin Market Cap - Day.csv` | Market cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `416d9a56d361` |
| `Bitcoin Price & Volume - Spot, All Exchanges, BTC-USD - Day.csv` | Price & volume | 2009-01-03 .. 2026-04-11 | 6,308 | daily | 0 | 7 | `bc5e5e4fee98` |
| `Bitcoin Price & Volume KRW - Spot - Day.csv` | Price & volume | 2013-09-03 .. 2026-04-10 | 4,594 | daily | 9 | 7 | `1f16d6a3182b` |
| `Bitcoin Realized Cap - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `3bc718c49bcd` |
| `Bitcoin Realized Cap - UTXO Age Bands (%) - Day.csv` | Realized cap | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 15 | `6fe6c4ee5eb9` |
| `Bitcoin Realized Cap - UTXO Age Bands USD - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 | `7a1cffd71f43` |
| `Bitcoin Realized Cap - UTXO Value Bands (%) - Day.csv` | Realized cap | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 | `8fcc013f314c` |
| `Bitcoin Realized Cap - UTXO Value Bands USD - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 10 | `ee0e9ad9244f` |
| `Bitcoin Taker Buy Ratio - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 | `235501c370bd` |
| `Bitcoin Taker Buy Sell Ratio - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 | `76c95353e3ef` |
| `Bitcoin Taker Buy Volume - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 | `e6f50626ef5a` |
| `Bitcoin Taker Sell Ratio - All Exchanges - Day.csv` | Taker sell volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 | `7529134f05d7` |
| `Bitcoin Taker Sell Volume - All Exchanges - Day.csv` | Taker sell volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 | `ff2389551495` |
| `Bitcoin Thermo Cap - Day.csv` | Thermo cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 | `e8411e62e15a` |
| `Bitcoin Trading Volume (KYC VS. Non-KYC) - Day.csv` | Bitcoin Trading Volume (KYC VS. Non-KYC) - Day | 2013-10-21 .. 2026-04-10 | 4,555 | daily | 0 | 4 | `10ef7f3df4c5` |
| `Bitcoin Trading Volume (Spot VS. Derivative) - Day.csv` | Bitcoin Trading Volume (Spot VS. Derivative) - Day | 2013-10-21 .. 2026-04-10 | 4,555 | daily | 0 | 4 | `fff50006bb4f` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Average Cap - Day.csv`**

```csv
date,timestamp_utc,Average Cap
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Delta Cap - Day.csv`**

```csv
date,timestamp_utc,Delta Cap
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Exchange Supply - Day.csv`**

```csv
date,timestamp_utc,Total Left,KYC'd US Exchange,KYC'd US Alliance Exchange,KYC'd Off-shore Chinese-controlled Exchange,International,International.1
2009-01-03,2009-01-03T00:00:00Z,1.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,2009-01-04T00:00:00Z,1.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Geographical Supply Distribution by Entities - Day.csv`**

```csv
date,timestamp_utc,US,US Alliance,International
2006-04-11,2006-04-11T00:00:00Z,0.0,0.0,0.0
2006-04-12,2006-04-12T00:00:00Z,0.0,0.0,0.0
```

**`Bitcoin Market Cap - Day.csv`**

```csv
date,timestamp_utc,Market Cap
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Price & Volume - Spot, All Exchanges, BTC-USD - Day.csv`**

```csv
date,timestamp_utc,Open,High,Low,Close,Volume
2009-01-03,2009-01-03T00:00:00Z,,,,,0.0
2009-01-04,2009-01-04T00:00:00Z,,,,,0.0
```

**`Bitcoin Price & Volume KRW - Spot - Day.csv`**

```csv
date,timestamp_utc,Open,High,Low,Close,Volume
2013-09-03,2013-09-03T00:00:00Z,160000.0,160000.0,150000.0,150000.0,0.3
2013-09-04,2013-09-04T00:00:00Z,180000.0,180000.0,180000.0,180000.0,3.44
```

**`Bitcoin Realized Cap - Day.csv`**

```csv
date,timestamp_utc,Realized Cap
2009-01-03,2009-01-03T00:00:00Z,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0
```

**`Bitcoin Realized Cap - UTXO Age Bands (%) - Day.csv`**

```csv
date,timestamp_utc,0d ~ 1d (%),1d ~ 1w (%),1w ~ 1m (%),1m ~ 3m (%),3m ~ 6m (%),6m ~ 12m (%),12m ~ 18m (%),18m ~ 2y (%),... (+5 more)
2020-12-31,2020-12-31T00:00:00Z,5.88579612,14.33929276,20.50143208,17.46726301,7.61240894,7.57555927,6.20640016,3.9612323
2021-01-01,2021-01-01T00:00:00Z,5.85587557,15.45617226,20.06734484,17.58761428,7.29711877,7.45943723,6.11565038,3.92526775
```

**`Bitcoin Realized Cap - UTXO Age Bands USD - Day.csv`**

```csv
date,timestamp_utc,0d ~ 1d,1d ~ 1w,1w ~ 1m,1m ~ 3m,3m ~ 6m,6m ~ 12m,12m ~ 18m,18m ~ 2y,... (+5 more)
2009-01-03,2009-01-03T00:00:00Z,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Realized Cap - UTXO Value Bands (%) - Day.csv`**

```csv
date,timestamp_utc,0 ~ 1 USD (%),1 ~ 10 USD (%),10 ~ 100 USD (%),100 ~ 1K USD (%),1K ~ 10K USD (%),10K ~ 100K USD (%),100K ~ 1M USD (%),1M USD ~ (%)
2020-12-31,2020-12-31T00:00:00Z,0.00309417,0.0279158,0.29787104,1.21660687,4.52600618,10.6478678,18.05543977,65.22519837
2021-01-01,2021-01-01T00:00:00Z,0.00305595,0.02746418,0.29247539,1.195549,4.48314854,10.60176277,17.95495945,65.44158471
```

**`Bitcoin Realized Cap - UTXO Value Bands USD - Day.csv`**

```csv
date,timestamp_utc,0 ~ 1 USD,1 ~ 10 USD,10 ~ 100 USD,100 ~ 1K USD,1K ~ 10K USD,10K ~ 100K USD,100K ~ 1M USD,1M ~ USD
2009-01-03,2009-01-03T00:00:00Z,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,2009-01-04T00:00:00Z,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

_(8 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
