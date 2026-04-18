# CryptoQuant / USDC/Transactions

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (3)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `USD Coin(ERC20) Tokens Transferred (Mean) - Day.csv` | USD Coin(ERC20) Tokens Transferred (Mean) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 2 | `4e02a859afe1` |
| `USD Coin(ERC20) Tokens Transferred (Total) - Day.csv` | USD Coin(ERC20) Tokens Transferred (Total) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 2 | `974fedb1cba7` |
| `USD Coin(ERC20) Transfer Event Count - Day.csv` | USD Coin(ERC20) Transfer Event Count - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 2 | `428a420fb419` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`USD Coin(ERC20) Tokens Transferred (Mean) - Day.csv`**

```csv
date,Tokens Transferred (Mean)
2018-09-10,5.55
2018-09-12,0.625
```

**`USD Coin(ERC20) Tokens Transferred (Total) - Day.csv`**

```csv
date,Tokens Transferred (Total)
2018-09-10,22.2
2018-09-12,2.5
```

**`USD Coin(ERC20) Transfer Event Count - Day.csv`**

```csv
date,Transfer Event Count
2018-09-10,4
2018-09-12,4
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
