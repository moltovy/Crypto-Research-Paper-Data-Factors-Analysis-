# CryptoQuant / ETH/Derivatives

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) and keeps the original as `timestamp_utc`.

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (8)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Estimated Leverage Ratio - All Exchanges - Day.csv` | Estimated leverage ratio | 2019-03-30 .. 2026-04-10 | 2,569 | daily | 0 | 3 | `c048f21427fa` |
| `Ethereum Funding Rates - All Exchanges - Day.csv` | Funding rates | 2018-08-02 .. 2026-04-11 | 2,810 | daily | 0 | 3 | `d2898e245bdf` |
| `Ethereum Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2019-01-13 .. 2026-04-11 | 2,646 | daily | 0 | 5 | `d0b6dbecf4f5` |
| `Ethereum Long Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 | `479206919dba` |
| `Ethereum Long Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 | `9cc830c98441` |
| `Ethereum Open Interest - All Exchanges, All Symbol - Day.csv` | Open interest | 2019-03-30 .. 2026-04-11 | 2,570 | daily | 0 | 3 | `cc4e62346b91` |
| `Ethereum Short Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 | `5d1d3e76c24e` |
| `Ethereum Short Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 | `95d3ac36c081` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Estimated Leverage Ratio - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Estimated Leverage Ratio
2019-03-30,2019-03-30T00:00:00Z,0.05260992
2019-03-31,2019-03-31T00:00:00Z,0.05610774
```

**`Ethereum Funding Rates - All Exchanges - Day.csv`**

```csv
date,timestamp_utc,Funding Rates
2018-08-02,2018-08-02T00:00:00Z,0.00527778
2018-08-03,2018-08-03T00:00:00Z,0.00295555
```

**`Ethereum Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv`**

```csv
date,timestamp_utc,Neutral,Taker Buy Dominant,Taker Sell Dominant
2019-01-13,2019-01-13,115.5,-,-
2019-01-14,2019-01-14,128.45,-,-
```

**`Ethereum Long Liquidations - All Exchanges, All Symbol - Day.csv`**

```csv
date,timestamp_utc,Long Liquidations
2018-12-28,2018-12-28T00:00:00Z,1.4462
2018-12-29,2018-12-29T00:00:00Z,121.671779
```

**`Ethereum Long Liquidations USD - All Exchanges, All Symbol - Day.csv`**

```csv
date,timestamp_utc,Long Liquidations USD
2018-12-28,2018-12-28T00:00:00Z,165.08373
2018-12-29,2018-12-29T00:00:00Z,16318.589260399996
```

**`Ethereum Open Interest - All Exchanges, All Symbol - Day.csv`**

```csv
date,timestamp_utc,Open Interest
2019-03-30,2019-03-30T00:00:00Z,102936575.0864352
2019-03-31,2019-03-31T00:00:00Z,109172772.8283936
```

**`Ethereum Short Liquidations - All Exchanges, All Symbol - Day.csv`**

```csv
date,timestamp_utc,Short Liquidations
2018-12-28,2018-12-28T00:00:00Z,110.481493
2018-12-29,2018-12-29T00:00:00Z,312.886518
```

**`Ethereum Short Liquidations USD - All Exchanges, All Symbol - Day.csv`**

```csv
date,timestamp_utc,Short Liquidations USD
2018-12-28,2018-12-28T00:00:00Z,13236.235005649924
2018-12-29,2018-12-29T00:00:00Z,44303.371859
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
