# CryptoQuant / ETH/Addresses

**Source**: https://cryptoquant.com/

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

**Date convention**: Original column was `Datetime` (ISO `YYYY-MM-DDThh:mm:ssZ`, descending). After curation each file has `date` (ISO `YYYY-MM-DD`, ascending) as its first column; the original timestamp column has been dropped (everything is daily granularity).

**Units**: Varies per metric; see the existing `<ASSET>_Metrics.txt` inventories.

> Note: Derivatives metrics are aggregated across 'All Exchanges, All Symbol'. Whether CME BTC / ETH futures are included is NOT exposed in the export. For explicit CME coverage, see `Data/Tradingview/` CME files.

**Frequency hint**: All daily.

**Licensing**: CryptoQuant Terms of Service; for internal research use.

## Files (6)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Ethereum Active Addresses - Day.csv` | Active addresses | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `4ba4ada463bd` |
| `Ethereum Active Addresses - Internal, External, EOA - Day.csv` | Active addresses | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 4 | `1319ae9de53f` |
| `Ethereum Active Receiving Addresses - Day.csv` | Ethereum Active Receiving Addresses - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `184d935336e2` |
| `Ethereum Active Receiving Addresses - Internal, External, EOA - Day.csv` | Ethereum Active Receiving Addresses - Internal, External, EOA - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 4 | `e614f044c208` |
| `Ethereum Active Sending Addresses - Day.csv` | Ethereum Active Sending Addresses - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 2 | `c9688a91d88e` |
| `Ethereum Active Sending Addresses - Internal, External, EOA - Day.csv` | Ethereum Active Sending Addresses - Internal, External, EOA - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 4 | `c1a837ed61fa` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Ethereum Active Addresses - Day.csv`**

```csv
date,Active Addresses
2020-11-02,316567
2020-11-03,307180
```

**`Ethereum Active Addresses - Internal, External, EOA - Day.csv`**

```csv
date,Active Addresses -  Internal, External, EOA
2020-11-02,473277,,
2020-11-03,449977,,
```

**`Ethereum Active Receiving Addresses - Day.csv`**

```csv
date,Active Receiving Addresses
2020-11-02,228147
2020-11-03,221136
```

**`Ethereum Active Receiving Addresses - Internal, External, EOA - Day.csv`**

```csv
date,Active Receiving Addresses - Internal, External, EOA
2020-11-02,322570,,
2020-11-03,298324,,
```

**`Ethereum Active Sending Addresses - Day.csv`**

```csv
date,Active Sending Addresses
2020-11-02,180350
2020-11-03,177858
```

**`Ethereum Active Sending Addresses - Internal, External, EOA - Day.csv`**

```csv
date,Active Sending Addresses - Internal, External, EOA
2020-11-02,357277,,
2020-11-03,350898,,
```

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
