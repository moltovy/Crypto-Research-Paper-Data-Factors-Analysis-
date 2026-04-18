# Artemis

**Source**: https://app.artemis.xyz/

Cross-chain analytics platform. Exports here are manually downloaded dashboards covering ETF AUM, perpetuals, DEX activity, lending, stablecoins, and RWAs.

**Date convention**: Each file originally had a quoted `"DateTime"` column as `YYYY-MM-DD 00:00:00`. After curation it is `date` (ISO `YYYY-MM-DD`, UTC, ascending).

**Units**: Mixed — USD for AUM / mcap / volumes / TVL, count for addresses, see per-file headers.

**Frequency hint**: Mostly daily, some monthly aggregates (ETF flows).

**Licensing**: Artemis Terms of Use; for internal research use.

## Files (48)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `Adjusted Stablecoin Transactions by Region (Ethereum and Solana).csv` | Stablecoin | 2020-01-31 .. 2026-03-31 | 75 | monthly | — | 8 | `f5cde0a34c0e` |
| `Artemis - Digital Asset Treasuries Overview.csv` | Artemis - Digital Asset Treasuries Overview | — | 20 | snapshot | — | 11 | `9f47ae804e5c` |
| `Bitcoin ETFs AUM.csv` | ETF | 2024-01-11 .. 2026-04-14 | 825 | daily | 0 | 12 | `f505ff9eb3df` |
| `BTC DATs - Bitcoin Count.csv` | BTC DATs - Bitcoin Count | 2020-08-10 .. 2026-04-15 | 1,483 | daily | 592 | 8 | `5427169a4ceb` |
| `BTC DATs- Fully Diluted EV NAV.csv` | BTC DATs- Fully Diluted EV NAV | 2020-08-10 .. 2026-04-15 | 1,483 | daily | 592 | 7 | `72f50e7a1671` |
| `Centralized Exchanges - Open Interest.csv` | Open interest | 2022-07-11 .. 2026-04-14 | 1,374 | daily | 0 | 8 | `02deb89ee71e` |
| `Centralized Exchanges - Perpetuals Volume.csv` | Centralized Exchanges - Perpetuals Volume | 2022-01-01 .. 2026-04-14 | 1,565 | daily | 0 | 8 | `cbfa126a910d` |
| `Centralized Exchanges - Spot Volume.csv` | Centralized Exchanges - Spot Volume | 2022-01-01 .. 2026-04-14 | 1,565 | daily | 0 | 9 | `8e14988f40ba` |
| `Chains - Chain MAU.csv` | Chains - Chain MAU | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 9 | `7486e3773061` |
| `Chains - Daily Active Addresses (New Wallets).csv` | Active addresses | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 7 | `aa9b7eaf8401` |
| `Chains - Daily Active Addresses (Returning Wallets).csv` | Active addresses | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 7 | `1a7d8c3691fd` |
| `Chains - Fees.csv` | Fees | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 13 | `fb78e6a59d48` |
| `Chains - Market Cap.csv` | Market cap | 2015-08-07 .. 2026-04-15 | 3,903 | daily | 2 | 13 | `eff62b25b9f8` |
| `Chains - P2P Stablecoin Transaction Volume.csv` | Stablecoin | 2017-11-28 .. 2026-04-14 | 3,060 | daily | 0 | 9 | `3f42eafbcbea` |
| `Chains - Revenue.csv` | Chains - Revenue | 2015-07-30 .. 2026-04-14 | 3,912 | daily | 0 | 13 | `b8a684912a9a` |
| `Chains - Stablecoin Supply.csv` | Stablecoin | 2017-11-28 .. 2026-04-14 | 3,060 | daily | 0 | 9 | `39c6472000dd` |
| `Chains - Stablecoin Transaction Volume.csv` | Stablecoin | 2017-11-28 .. 2026-04-14 | 3,060 | daily | 0 | 9 | `05faa710f8d7` |
| `Crypto ETF AUM to Crypto Market Cap.csv` | Market cap | 2024-01-11 .. 2026-04-14 | 825 | daily | 0 | 5 | `174f6759e95c` |
| `Crypto ETF Flows.csv` | ETF | 2024-01-14 .. 2026-04-12 | 118 | weekly | — | 5 | `98a9cdc54999` |
| `Crypto ETFs AUM.csv` | ETF | 2024-01-11 .. 2026-04-14 | 825 | daily | 0 | 5 | `f99a1231f14d` |
| `DEX - Spot DEX Daily Active Users.csv` | DEX - Spot DEX Daily Active Users | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 21 | `b1e45c20ec51` |
| `DEX - Spot Fees.csv` | Fees | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 21 | `4d33ed246bdb` |
| `DEX - Spot Volume.csv` | DEX - Spot Volume | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 24 | `eae1a49b49e2` |
| `DEX - TVL.csv` | TVL | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 19 | `323e552931f5` |
| `Ethereum ETFs AUM.csv` | ETF | 2024-07-23 .. 2026-04-14 | 631 | daily | 0 | 11 | `11bc631b52ab` |
| `Lending Borrows by Chain.csv` | Lending Borrows by Chain | 2019-11-17 .. 2026-04-12 | 335 | weekly | — | 9 | `cded37602cec` |
| `Lending Borrows by Protocol.csv` | Lending Borrows by Protocol | 2017-12-24 .. 2026-04-12 | 434 | weekly | — | 20 | `ea5eaee272a6` |
| `Lending Deposits by Chain.csv` | Lending Deposits by Chain | 2019-11-17 .. 2026-04-12 | 335 | weekly | — | 9 | `0ff0b357b68a` |
| `Lending Deposits by Protocol.csv` | Lending Deposits by Protocol | 2017-12-24 .. 2026-04-12 | 434 | weekly | — | 20 | `1c0a6ec1b531` |
| `Lending Interest Fees by Protocol.csv` | Fees | 2020-06-30 .. 2026-03-31 | 70 | monthly | — | 11 | `554ff4217db2` |
| `Lending Protocol Revenue.csv` | Lending Protocol Revenue | 2020-06-21 .. 2026-04-12 | 304 | weekly | — | 8 | `55423e75d575` |
| `Liquid Restaking - LRT TVL (USD).csv` | TVL | 2022-09-30 .. 2026-04-14 | 1,293 | daily | 0 | 8 | `b324d5c7a5c3` |
| `Liquid Staking - LST TVL (USD).csv` | TVL | 2020-12-19 .. 2026-04-14 | 1,943 | daily | 0 | 12 | `9831c858b874` |
| `Monthly Bitcoin ETF flows.csv` | ETF | 2024-01-31 .. 2026-03-31 | 27 | monthly | — | 12 | `5cc7da839f0b` |
| `Monthly Ethereum ETF flows.csv` | ETF | 2024-07-31 .. 2026-03-31 | 21 | monthly | — | 11 | `645fc2f90668` |
| `Monthly Solana ETF flows.csv` | ETF | 2025-10-31 .. 2026-03-31 | 6 | monthly | — | 7 | `2bb4e87fb6ba` |
| `Perpetuals Daily Active Users for Trading Platforms.csv` | Perpetuals Daily Active Users for Trading Platforms | 2021-04-11 .. 2026-04-12 | 262 | weekly | — | 12 | `ddea4ed2899b` |
| `Perpetuals Open Interest for Trading Platforms.csv` | Open interest | 2023-06-18 .. 2026-04-12 | 148 | weekly | — | 12 | `c5eb6a0dfeda` |
| `Perpetuals Volume for Protocols.csv` | Perpetuals Volume for Protocols | 2021-04-11 .. 2026-04-12 | 262 | weekly | — | 27 | `b1b7c33cda5e` |
| `Perpetuals Volume for Trading Platforms.csv` | Perpetuals Volume for Trading Platforms | 2021-04-11 .. 2026-04-12 | 262 | weekly | — | 20 | `cc162dbf7134` |
| `RWA - Tokenized Market Cap.csv` | Market cap | 2023-01-01 .. 2026-04-14 | 1,200 | daily | 0 | 8 | `da195b457cbf` |
| `Solana ETFs AUM.csv` | ETF | 2025-10-31 .. 2026-04-14 | 166 | daily | 0 | 7 | `ae8e608f1848` |
| `Stablecoin Active Addresses by Chain.csv` | Active addresses | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 12 | `d2f6f71647b2` |
| `Stablecoin Active Addresses by Token.csv` | Active addresses | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 12 | `9c0f965351ba` |
| `Stablecoin Market Share by Token.csv` | Stablecoin | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 12 | `a05d8f0fa380` |
| `Stablecoin Supply by Chain.csv` | Stablecoin | 2017-11-30 .. 2026-04-30 | 102 | monthly | — | 12 | `8f1e0a9a86cb` |
| `Stablecoin Supply by Currency.csv` | Stablecoin | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 17 | `1e9d8ce8b71e` |
| `Stablecoin Supply by Token.csv` | Stablecoin | 2017-11-30 .. 2026-04-30 | 102 | monthly | — | 12 | `42b682ddcdb1` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`Adjusted Stablecoin Transactions by Region (Ethereum and Solana).csv`**

```csv
date,Africa,Asia,Europe,Latin America,North America,Oceania,Southeast Asia
2020-01-31,0,469027,1169,11486,129885,55,10738
2020-02-29,0,776224,3133,17282,209172,66,12742
```

**`Artemis - Digital Asset Treasuries Overview.csv`**

```csv
symbol,EQ_SHARE_VOLUME,MC,EQ_FULLY_DILUTED_MARKET_CAP,EQ_NAV,EQ_M_NAV,EQ_FDM_NAV,EQ_EV_MNAV,EQ_FD_EV_MNAV,TICKER,... (+1 more)
eq-mstr,752697892.128,,51129485904.0,57651282819.0,0.8084061069433877,0.886875077255859,0.9118556697002888,0.9903246400127602,MSTR
eq-mtplf,14511400.0,,3065218503.299033,2591475354.0,1.182808278908692,1.182808278908692,1.2908548399411222,1.2908548399411222,MTPLF
```

**`Bitcoin ETFs AUM.csv`**

```csv
date,ARKB,BITB,BRRR,Bitcoin,BTCO,BTCW,EZBC,FBTC,GBTC,... (+2 more)
2024-01-11,65299999.99999999,237900000.0,29400000.000000004,0.0,17400000.0,1000000.0,50100000.0,227000000.0,26847704354.03643
2024-01-12,100277438.80886866,237730515.9667665,47428739.67811238,0.0,44514968.38092366,926147.6080990608,46399995.16576294,405535507.0384867,24380837170.44157
```

**`BTC DATs - Bitcoin Count.csv`**

```csv
date,American Bitcoin - Number of Tokens Held,Strive Asset Management - Number of Tokens Held,Bitcoin Standard Treasury Company - Number of Tokens Held,Metaplanet - Number of Tokens Held,Strategy - Number of Tokens Held,Nakamoto Holdings - Number of Tokens Held,Twenty One Capital - Number of Tokens Held
2020-08-10,,,,,21454,,
2020-08-11,,,,,21454,,
```

**`BTC DATs- Fully Diluted EV NAV.csv`**

```csv
date,American Bitcoin - Fully Diluted EV / Nav,Strive Asset Management - Fully Diluted EV / Nav,Metaplanet - Fully Diluted EV / Nav,Strategy - Fully Diluted EV / Nav,Nakamoto Holdings - Fully Diluted EV / Nav,Twenty One Capital - Fully Diluted EV / Nav
2020-08-10,,,,5.042842747548336,,
2020-08-11,,,,5.746786952520501,,
```

**`Centralized Exchanges - Open Interest.csv`**

```csv
date,Binance,Bitget,Bybit,Crypto.com,Gate.io,Kraken,OKX
2022-07-11,6525534281.76741,,,,,,3779741678.31529
2022-07-12,6389563370.43266,,,,,,3712362784.26242
```

**`Centralized Exchanges - Perpetuals Volume.csv`**

```csv
date,Binance,Bitget,Bybit,Crypto.com,Gate.io,Kraken,OKX
2022-01-01,30486139526.77748,,,,,,
2022-01-02,32089549821.25571,,,,,,
```

**`Centralized Exchanges - Spot Volume.csv`**

```csv
date,Binance,Bitget,Bitstamp,Bybit,Crypto.com,Gate.io,HTX,Kraken
2022-01-01,9206823508.004118,,82108288.75607626,,3033273880.7320814,40009459.42980464,455280325.70613855,324492376.657262
2022-01-02,9913789090.851809,,94428533.56189372,,2672977856.352208,48009236.43883676,499147390.5051552,314717167.0162022
```

**`Chains - Chain MAU.csv`**

```csv
date,Aptos,Avalanche C-Chain,Ethereum,Near,Sui,Polygon PoS,Solana,Acala
2015-08-07,,,784,,,,,
2015-08-08,,,1214,,,,,
```

**`Chains - Daily Active Addresses (New Wallets).csv`**

```csv
date,Avalanche C-Chain,Ethereum,Near,Sui,Polygon PoS,Solana
2015-08-07,,784,,,,
2015-08-08,,430,,,,
```

**`Chains - Daily Active Addresses (Returning Wallets).csv`**

```csv
date,Avalanche C-Chain,Ethereum,Near,Sui,Polygon PoS,Solana
2015-08-07,,0,,,,
2015-08-08,,175,,,,
```

**`Chains - Fees.csv`**

```csv
date,Aptos,Avalanche C-Chain,Ethereum,Near,Sui,Polygon PoS,Solana,TON,Abstract,... (+3 more)
2015-08-07,,,49.661478780134935,,,,,,
2015-08-08,,,0.0,,,,,,
```

_(36 more files in this folder — see the table above or the master inventory.)_

---
_Auto-generated on 2026-04-18 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
