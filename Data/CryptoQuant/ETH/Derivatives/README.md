# CryptoQuant / ETH/Derivatives

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (8)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Estimated Leverage Ratio - All Exchanges - Day.csv` | Estimated leverage ratio | 2019-03-30 .. 2026-04-10 | 2,569 | daily | 0 | 2 | `fdd150dff64e` |
| `Ethereum Funding Rates - All Exchanges - Day.csv` | Funding rates | 2018-08-02 .. 2026-04-11 | 2,810 | daily | 0 | 2 | `32bf6c33e8c5` |
| `Ethereum Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2019-01-13 .. 2026-04-11 | 2,646 | daily | 0 | 4 | `08849fe36d7a` |
| `Ethereum Long Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 2 | `f0b5efc64f1f` |
| `Ethereum Long Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 2 | `12b59d9104db` |
| `Ethereum Open Interest - All Exchanges, All Symbol - Day.csv` | Open interest | 2019-03-30 .. 2026-04-11 | 2,570 | daily | 0 | 2 | `69bd0435e1de` |
| `Ethereum Short Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 2 | `ab3a4233f58c` |
| `Ethereum Short Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 2 | `91c71b3bbd7a` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Estimated Leverage Ratio - All Exchanges - Day.csv`**

```csv
date,Estimated Leverage Ratio
2019-03-30,0.05260992
2019-03-31,0.05610774
```

**`Ethereum Funding Rates - All Exchanges - Day.csv`**

```csv
date,Funding Rates
2018-08-02,0.00527778
2018-08-03,0.00295555
```

**`Ethereum Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv`**

```csv
date,Neutral,Taker Buy Dominant,Taker Sell Dominant
2019-01-13,115.5,-,-
2019-01-14,128.45,-,-
```

**`Ethereum Long Liquidations - All Exchanges, All Symbol - Day.csv`**

```csv
date,Long Liquidations
2018-12-28,1.4462
2018-12-29,121.671779
```

**`Ethereum Long Liquidations USD - All Exchanges, All Symbol - Day.csv`**

```csv
date,Long Liquidations USD
2018-12-28,165.08373
2018-12-29,16318.589260399996
```

**`Ethereum Open Interest - All Exchanges, All Symbol - Day.csv`**

```csv
date,Open Interest
2019-03-30,102936575.0864352
2019-03-31,109172772.8283936
```

**`Ethereum Short Liquidations - All Exchanges, All Symbol - Day.csv`**

```csv
date,Short Liquidations
2018-12-28,110.481493
2018-12-29,312.886518
```

**`Ethereum Short Liquidations USD - All Exchanges, All Symbol - Day.csv`**

```csv
date,Short Liquidations USD
2018-12-28,13236.235005649924
2018-12-29,44303.371859
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
