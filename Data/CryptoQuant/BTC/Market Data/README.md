# CryptoQuant / BTC/Market Data

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (20)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Bitcoin Average Cap - Day.csv` | Bitcoin Average Cap - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `09734072bbb2` |
| `Bitcoin Delta Cap - Day.csv` | Bitcoin Delta Cap - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `fc550ed632a2` |
| `Bitcoin Exchange Supply - Day.csv` | Bitcoin Exchange Supply - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 7 | `7efdfd9ac730` |
| `Bitcoin Geographical Supply Distribution by Entities - Day.csv` | Bitcoin Geographical Supply Distribution by Entities - Day | 2006-04-11 .. 2026-04-10 | 7,305 | daily | 0 | 4 | `33caa2427b1e` |
| `Bitcoin Market Cap - Day.csv` | Market cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `7586ee348a32` |
| `Bitcoin Price & Volume - Spot, All Exchanges, BTC-USD - Day.csv` | Price & volume | 2009-01-03 .. 2026-04-11 | 6,308 | daily | 0 | 6 | `ee60291bea50` |
| `Bitcoin Price & Volume KRW - Spot - Day.csv` | Price & volume | 2013-09-03 .. 2026-04-10 | 4,594 | daily | 9 | 6 | `3a41302e1fee` |
| `Bitcoin Realized Cap - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `eafd2faaf3e6` |
| `Bitcoin Realized Cap - UTXO Age Bands (%) - Day.csv` | Realized cap | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 14 | `84dc5d0da4ce` |
| `Bitcoin Realized Cap - UTXO Age Bands USD - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 14 | `1f1b9152cf7e` |
| `Bitcoin Realized Cap - UTXO Value Bands (%) - Day.csv` | Realized cap | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 9 | `0cf02f8d4e41` |
| `Bitcoin Realized Cap - UTXO Value Bands USD - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 9 | `c66123fa9037` |
| `Bitcoin Taker Buy Ratio - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 2 | `a3658a4b5ebd` |
| `Bitcoin Taker Buy Sell Ratio - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 2 | `66f22aafcd3a` |
| `Bitcoin Taker Buy Volume - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 2 | `b6e6b47eb09e` |
| `Bitcoin Taker Sell Ratio - All Exchanges - Day.csv` | Taker sell volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 2 | `78955c2cb023` |
| `Bitcoin Taker Sell Volume - All Exchanges - Day.csv` | Taker sell volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 2 | `b921adee734a` |
| `Bitcoin Thermo Cap - Day.csv` | Thermo cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 2 | `c438cfcc54ea` |
| `Bitcoin Trading Volume (KYC VS. Non-KYC) - Day.csv` | Bitcoin Trading Volume (KYC VS. Non-KYC) - Day | 2013-10-21 .. 2026-04-10 | 4,555 | daily | 0 | 3 | `b91a0b0e0dc7` |
| `Bitcoin Trading Volume (Spot VS. Derivative) - Day.csv` | Bitcoin Trading Volume (Spot VS. Derivative) - Day | 2013-10-21 .. 2026-04-10 | 4,555 | daily | 0 | 3 | `44e342fd6040` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Bitcoin Average Cap - Day.csv`**

```csv
date,Average Cap
2009-01-03,0.0
2009-01-04,0.0
```

**`Bitcoin Delta Cap - Day.csv`**

```csv
date,Delta Cap
2009-01-03,0.0
2009-01-04,0.0
```

**`Bitcoin Exchange Supply - Day.csv`**

```csv
date,Total Left,KYC'd US Exchange,KYC'd US Alliance Exchange,KYC'd Off-shore Chinese-controlled Exchange,International,International.1
2009-01-03,1.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,1.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Geographical Supply Distribution by Entities - Day.csv`**

```csv
date,US,US Alliance,International
2006-04-11,0.0,0.0,0.0
2006-04-12,0.0,0.0,0.0
```

**`Bitcoin Market Cap - Day.csv`**

```csv
date,Market Cap
2009-01-03,0.0
2009-01-04,0.0
```

**`Bitcoin Price & Volume - Spot, All Exchanges, BTC-USD - Day.csv`**

```csv
date,Open,High,Low,Close,Volume
2009-01-03,,,,,0.0
2009-01-04,,,,,0.0
```

**`Bitcoin Price & Volume KRW - Spot - Day.csv`**

```csv
date,Open,High,Low,Close,Volume
2013-09-03,160000.0,160000.0,150000.0,150000.0,0.3
2013-09-04,180000.0,180000.0,180000.0,180000.0,3.44
```

**`Bitcoin Realized Cap - Day.csv`**

```csv
date,Realized Cap
2009-01-03,0.0
2009-01-04,0.0
```

**`Bitcoin Realized Cap - UTXO Age Bands (%) - Day.csv`**

```csv
date,0d ~ 1d (%),1d ~ 1w (%),1w ~ 1m (%),1m ~ 3m (%),3m ~ 6m (%),6m ~ 12m (%),12m ~ 18m (%),18m ~ 2y (%),2y ~ 3y (%),... (+4 more)
2020-12-31,5.88579612,14.33929276,20.50143208,17.46726301,7.61240894,7.57555927,6.20640016,3.9612323,9.82089209
2021-01-01,5.85587557,15.45617226,20.06734484,17.58761428,7.29711877,7.45943723,6.11565038,3.92526775,9.55835347
```

**`Bitcoin Realized Cap - UTXO Age Bands USD - Day.csv`**

```csv
date,0d ~ 1d,1d ~ 1w,1w ~ 1m,1m ~ 3m,3m ~ 6m,6m ~ 12m,12m ~ 18m,18m ~ 2y,2y ~ 3y,... (+4 more)
2009-01-03,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

**`Bitcoin Realized Cap - UTXO Value Bands (%) - Day.csv`**

```csv
date,0 ~ 1 USD (%),1 ~ 10 USD (%),10 ~ 100 USD (%),100 ~ 1K USD (%),1K ~ 10K USD (%),10K ~ 100K USD (%),100K ~ 1M USD (%),1M USD ~ (%)
2020-12-31,0.00309417,0.0279158,0.29787104,1.21660687,4.52600618,10.6478678,18.05543977,65.22519837
2021-01-01,0.00305595,0.02746418,0.29247539,1.195549,4.48314854,10.60176277,17.95495945,65.44158471
```

**`Bitcoin Realized Cap - UTXO Value Bands USD - Day.csv`**

```csv
date,0 ~ 1 USD,1 ~ 10 USD,10 ~ 100 USD,100 ~ 1K USD,1K ~ 10K USD,10K ~ 100K USD,100K ~ 1M USD,1M ~ USD
2009-01-03,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2009-01-04,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
```

_(8 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
