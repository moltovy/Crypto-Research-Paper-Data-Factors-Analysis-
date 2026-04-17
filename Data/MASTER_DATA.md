# Master Data Inventory

This file is the single-page index of every CSV under `Data/`. It is intended for two audiences:

1. **Teammates** — to know what data exists, what dates it covers, and where to find it.
2. **Downstream AI / scripts** — paired with `MASTER_DATA.csv`, this is a machine-readable inventory.

Mission context (from `Manager_Outline.md`): comparative BTC/ETH factor-evolution research around post-ETF institutionalization, using macro, institutional, crypto-liquidity, and on-chain factor blocks.

All time-series CSVs have been normalized to:

- `date` as the first column (ISO `YYYY-MM-DD`, UTC calendar, ascending).
- Timestamped sources (CryptoQuant, TradingView) also keep a `timestamp_utc` column.
- UTF-8, LF line endings, no BOM.

## Sources

| Source | Files | Rows total | Date span | Primary kind |
| --- | ---: | ---: | --- | --- |
| `Artemis/` | 48 | 75,302 | 2010-01-01 .. 2026-04-30 | daily |
| `CryptoQuant/` | 345 | 1,181,712 | 2006-04-11 .. 2026-04-12 | daily |
| `DefiLlama/` | 37 | 327,830 | 2016-04-19 .. 2026-04-19 | daily |
| `Farside ETF Data/` | 3 | 1,032 | 2024-01-11 .. 2026-04-10 | daily |
| `Tradingview/` | 12 | 16,133 | 2017-12-17 .. 2026-04-16 | daily |

## Factor-block mapping (for quick teammate orientation)

| Factor block | Primary sources |
| --- | --- |
| Macro / cross-asset | `Tradingview/` (DVOL), and any future FRED/Yahoo pulls |
| Institutional (ETF / DAT) | `Farside ETF Data/`, `Artemis/` ETF AUMs, `DefiLlama/ETFs/`, `DefiLlama/DATs/` |
| Crypto-liquidity | `DefiLlama/TVL/`, `DefiLlama/Stablecoins/`, `DefiLlama/CEX/`, `DefiLlama/ChainMetrics/`, Artemis chain/DEX/lending metrics |
| BTC-native | `CryptoQuant/BTC/` (all subfolders), `Tradingview/` CME BTC futures |
| ETH-native | `CryptoQuant/ETH/` (all subfolders), `Tradingview/` CME ETH futures, Artemis chain metrics |

## Full file index

### Artemis

Cross-chain analytics platform. Exports here are manually downloaded dashboards covering ETF AUM, perpetuals, DEX activity, lending, stablecoins, and RWAs.

| Relative path | Topic | Date range | Rows | Freq | Missing days | Cols |
| --- | --- | --- | ---: | --- | ---: | ---: |
| `Artemis/Adjusted Stablecoin Transactions by Region (Ethereum and Solana).csv` | Stablecoin | 2020-01-31 .. 2026-03-31 | 75 | monthly | — | 8 |
| `Artemis/Artemis - Digital Asset Treasuries Overview.csv` | Artemis - Digital Asset Treasuries Overview | — | 20 | snapshot | — | 11 |
| `Artemis/Bitcoin ETFs AUM.csv` | ETF | 2024-01-11 .. 2026-04-14 | 825 | daily | 0 | 12 |
| `Artemis/BTC DATs - Bitcoin Count.csv` | BTC DATs - Bitcoin Count | 2020-08-10 .. 2026-04-15 | 1,483 | daily | 592 | 8 |
| `Artemis/BTC DATs- Fully Diluted EV NAV.csv` | BTC DATs- Fully Diluted EV NAV | 2020-08-10 .. 2026-04-15 | 1,483 | daily | 592 | 7 |
| `Artemis/Centralized Exchanges - Open Interest.csv` | Open interest | 2022-07-11 .. 2026-04-14 | 1,374 | daily | 0 | 8 |
| `Artemis/Centralized Exchanges - Perpetuals Volume.csv` | Centralized Exchanges - Perpetuals Volume | 2022-01-01 .. 2026-04-14 | 1,565 | daily | 0 | 8 |
| `Artemis/Centralized Exchanges - Spot Volume.csv` | Centralized Exchanges - Spot Volume | 2022-01-01 .. 2026-04-14 | 1,565 | daily | 0 | 9 |
| `Artemis/Chains - Chain MAU.csv` | Chains - Chain MAU | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 9 |
| `Artemis/Chains - Daily Active Addresses (New Wallets).csv` | Active addresses | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 7 |
| `Artemis/Chains - Daily Active Addresses (Returning Wallets).csv` | Active addresses | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 7 |
| `Artemis/Chains - Fees.csv` | Fees | 2015-08-07 .. 2026-04-14 | 3,904 | daily | 0 | 13 |
| `Artemis/Chains - Market Cap.csv` | Market cap | 2015-08-07 .. 2026-04-15 | 3,903 | daily | 2 | 13 |
| `Artemis/Chains - P2P Stablecoin Transaction Volume.csv` | Stablecoin | 2017-11-28 .. 2026-04-14 | 3,060 | daily | 0 | 9 |
| `Artemis/Chains - Revenue.csv` | Chains - Revenue | 2015-07-30 .. 2026-04-14 | 3,912 | daily | 0 | 13 |
| `Artemis/Chains - Stablecoin Supply.csv` | Stablecoin | 2017-11-28 .. 2026-04-14 | 3,060 | daily | 0 | 9 |
| `Artemis/Chains - Stablecoin Transaction Volume.csv` | Stablecoin | 2017-11-28 .. 2026-04-14 | 3,060 | daily | 0 | 9 |
| `Artemis/Crypto ETF AUM to Crypto Market Cap.csv` | Market cap | 2024-01-11 .. 2026-04-14 | 825 | daily | 0 | 5 |
| `Artemis/Crypto ETF Flows.csv` | ETF | 2024-01-14 .. 2026-04-12 | 118 | weekly | — | 5 |
| `Artemis/Crypto ETFs AUM.csv` | ETF | 2024-01-11 .. 2026-04-14 | 825 | daily | 0 | 5 |
| `Artemis/DEX - Spot DEX Daily Active Users.csv` | DEX - Spot DEX Daily Active Users | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 21 |
| `Artemis/DEX - Spot Fees.csv` | Fees | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 21 |
| `Artemis/DEX - Spot Volume.csv` | DEX - Spot Volume | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 24 |
| `Artemis/DEX - TVL.csv` | TVL | 2010-01-01 .. 2026-04-14 | 5,948 | daily | 0 | 19 |
| `Artemis/Ethereum ETFs AUM.csv` | ETF | 2024-07-23 .. 2026-04-14 | 631 | daily | 0 | 11 |
| `Artemis/Lending Borrows by Chain.csv` | Lending Borrows by Chain | 2019-11-17 .. 2026-04-12 | 335 | weekly | — | 9 |
| `Artemis/Lending Borrows by Protocol.csv` | Lending Borrows by Protocol | 2017-12-24 .. 2026-04-12 | 434 | weekly | — | 20 |
| `Artemis/Lending Deposits by Chain.csv` | Lending Deposits by Chain | 2019-11-17 .. 2026-04-12 | 335 | weekly | — | 9 |
| `Artemis/Lending Deposits by Protocol.csv` | Lending Deposits by Protocol | 2017-12-24 .. 2026-04-12 | 434 | weekly | — | 20 |
| `Artemis/Lending Interest Fees by Protocol.csv` | Fees | 2020-06-30 .. 2026-03-31 | 70 | monthly | — | 11 |
| `Artemis/Lending Protocol Revenue.csv` | Lending Protocol Revenue | 2020-06-21 .. 2026-04-12 | 304 | weekly | — | 8 |
| `Artemis/Liquid Restaking - LRT TVL (USD).csv` | TVL | 2022-09-30 .. 2026-04-14 | 1,293 | daily | 0 | 8 |
| `Artemis/Liquid Staking - LST TVL (USD).csv` | TVL | 2020-12-19 .. 2026-04-14 | 1,943 | daily | 0 | 12 |
| `Artemis/Monthly Bitcoin ETF flows.csv` | ETF | 2024-01-31 .. 2026-03-31 | 27 | monthly | — | 12 |
| `Artemis/Monthly Ethereum ETF flows.csv` | ETF | 2024-07-31 .. 2026-03-31 | 21 | monthly | — | 11 |
| `Artemis/Monthly Solana ETF flows.csv` | ETF | 2025-10-31 .. 2026-03-31 | 6 | monthly | — | 7 |
| `Artemis/Perpetuals Daily Active Users for Trading Platforms.csv` | Perpetuals Daily Active Users for Trading Platforms | 2021-04-11 .. 2026-04-12 | 262 | weekly | — | 12 |
| `Artemis/Perpetuals Open Interest for Trading Platforms.csv` | Open interest | 2023-06-18 .. 2026-04-12 | 148 | weekly | — | 12 |
| `Artemis/Perpetuals Volume for Protocols.csv` | Perpetuals Volume for Protocols | 2021-04-11 .. 2026-04-12 | 262 | weekly | — | 27 |
| `Artemis/Perpetuals Volume for Trading Platforms.csv` | Perpetuals Volume for Trading Platforms | 2021-04-11 .. 2026-04-12 | 262 | weekly | — | 20 |
| `Artemis/RWA - Tokenized Market Cap.csv` | Market cap | 2023-01-01 .. 2026-04-14 | 1,200 | daily | 0 | 8 |
| `Artemis/Solana ETFs AUM.csv` | ETF | 2025-10-31 .. 2026-04-14 | 166 | daily | 0 | 7 |
| `Artemis/Stablecoin Active Addresses by Chain.csv` | Active addresses | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 12 |
| `Artemis/Stablecoin Active Addresses by Token.csv` | Active addresses | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 12 |
| `Artemis/Stablecoin Market Share by Token.csv` | Stablecoin | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 12 |
| `Artemis/Stablecoin Supply by Chain.csv` | Stablecoin | 2017-11-30 .. 2026-04-30 | 102 | monthly | — | 12 |
| `Artemis/Stablecoin Supply by Currency.csv` | Stablecoin | 2017-11-30 .. 2026-03-31 | 101 | monthly | — | 17 |
| `Artemis/Stablecoin Supply by Token.csv` | Stablecoin | 2017-11-30 .. 2026-04-30 | 102 | monthly | — | 12 |

### CryptoQuant

On-chain, derivatives, exchange-flow, and market-indicator data for BTC, ETH, USDC, USDT (ERC20 / TRC20), and WBTC. Source files are per-metric daily CSVs exported from the CryptoQuant web UI.

| Relative path | Topic | Date range | Rows | Freq | Missing days | Cols |
| --- | --- | --- | ---: | --- | ---: | ---: |
| `CryptoQuant/BTC/Addresses/Bitcoin Active Addresses - Day.csv` | Active addresses | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Addresses/Bitcoin Active Receiving Addresses - Day.csv` | Bitcoin Active Receiving Addresses - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Addresses/Bitcoin Active Sending Addresses - Day.csv` | Bitcoin Active Sending Addresses - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Estimated Leverage Ratio - All Exchanges - Day.csv` | Estimated leverage ratio | 2019-03-30 .. 2026-04-10 | 2,569 | daily | 0 | 3 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Funding Rates - All Exchanges - Day.csv` | Funding rates | 2016-05-15 .. 2026-04-11 | 3,619 | daily | 0 | 3 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2019-01-13 .. 2026-04-11 | 2,646 | daily | 0 | 5 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Long Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 3 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Long Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 3 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Open Interest - All Exchanges, All Symbol - Day.csv` | Open interest | 2019-03-30 .. 2026-04-11 | 2,570 | daily | 0 | 3 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Short Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 3 |
| `CryptoQuant/BTC/Derivatives/Bitcoin Short Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-20 .. 2026-04-11 | 2,670 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Depositing Addresses - All Exchanges - Day.csv` | Bitcoin Exchange Depositing Addresses - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Depositing Transactions - All Exchanges - Day.csv` | Bitcoin Exchange Depositing Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day.csv` | Bitcoin Exchange In-House Flow (Mean) - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day.csv` | Bitcoin Exchange In-House Flow (Total) - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange In-House Transactions - All Exchanges - Day.csv` | Bitcoin Exchange In-House Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Inflow - Spent Output Age Bands - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 15 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Inflow - Spent Output Value Bands - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 10 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2012-04-02 .. 2026-04-11 | 5,123 | daily | 0 | 4 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Reserve USD - All Exchanges - Day.csv` | Exchange reserve | 2012-04-02 .. 2026-04-11 | 5,123 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Bitcoin Exchange Withdrawing Addresses - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Exchange Flows/Bitcoin Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Bitcoin Exchange Withdrawing Transactions - All Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Block Rewards - Day.csv` | Bitcoin Block Rewards - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Block Rewards USD - Day.csv` | Bitcoin Block Rewards USD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees (Total) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees per Block (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees per Block USD (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees per Transaction (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees per Transaction (Median) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees per Transaction USD (Mean) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees per Transaction USD (Median) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees to Reward Ratio - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fees And Revenue/Bitcoin Fees USD (Total) - Day.csv` | Fees | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Flow Indicator/Bitcoin Exchange Inflow CDD - All Exchanges - Day.csv` | Exchange inflow | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 3 |
| `CryptoQuant/BTC/Flow Indicator/Bitcoin Exchange Stablecoins Ratio - All Exchanges - Day.csv` | Stablecoin | 2023-07-16 .. 2026-04-10 | 1,000 | daily | 0 | 3 |
| `CryptoQuant/BTC/Flow Indicator/Bitcoin Exchange Stablecoins Ratio USD - All Exchanges - Day.csv` | Stablecoin | 2023-07-16 .. 2026-04-10 | 1,000 | daily | 0 | 3 |
| `CryptoQuant/BTC/Flow Indicator/Bitcoin Exchange Supply Ratio - All Exchanges - Day.csv` | Bitcoin Exchange Supply Ratio - All Exchanges - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Flow Indicator/Bitcoin Exchange Whale Ratio - All Exchanges - Day.csv` | Bitcoin Exchange Whale Ratio - All Exchanges - Day | 2012-04-02 .. 2026-04-10 | 5,122 | daily | 0 | 3 |
| `CryptoQuant/BTC/Flow Indicator/Bitcoin Fund Flow Ratio - All Exchanges - Day.csv` | Bitcoin Fund Flow Ratio - All Exchanges - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Flow Indicator/Bitcoin Stablecoin Supply Ratio (SSR) - Day.csv` | Stablecoin | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fund Data/Bitcoin Coinbase Premium Gap - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fund Data/Bitcoin Coinbase Premium Index - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fund Data/Bitcoin Fund Holdings - All Symbol - Day.csv` | Fund holdings | 2020-06-09 .. 2026-04-09 | 2,131 | daily | 0 | 3 |
| `CryptoQuant/BTC/Fund Data/Bitcoin Fund Market Premium - All Symbol - Day.csv` | Fund market premium | 2020-06-09 .. 2026-04-09 | 1,506 | daily | 625 | 3 |
| `CryptoQuant/BTC/Fund Data/Bitcoin Fund Price (USD) - GBTC - Day.csv` | Fund price | 2015-05-04 .. 2026-04-02 | 2,746 | daily | 1241 | 3 |
| `CryptoQuant/BTC/Fund Data/Bitcoin Fund Volume - All Symbol - Day.csv` | Fund volume | 2015-05-04 .. 2026-04-09 | 2,792 | daily | 1202 | 3 |
| `CryptoQuant/BTC/Fund Data/Bitcoin Korea Premium Index - Day.csv` | Korea premium | 2020-07-16 .. 2026-04-10 | 2,095 | daily | 0 | 3 |
| `CryptoQuant/BTC/Inter Entity Flows/Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Flow (Mean) - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Inter Entity Flows/Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Flow (Total) - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Inter Entity Flows/Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day.csv` | Bitcoin Exchange to Exchange Transactions - All Exchanges, Spot Exchanges - Day | 2009-01-01 .. 2026-04-11 | 6,310 | daily | 0 | 3 |
| `CryptoQuant/BTC/Inter Entity Flows/Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Flow (Mean) - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 3 |
| `CryptoQuant/BTC/Inter Entity Flows/Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Flow (Total) - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 3 |
| `CryptoQuant/BTC/Inter Entity Flows/Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day.csv` | Bitcoin Miner to Miner Transactions - All Miners, 1THash - Day | 2021-01-24 .. 2026-04-10 | 1,903 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Average Cap - Day.csv` | Bitcoin Average Cap - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Delta Cap - Day.csv` | Bitcoin Delta Cap - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Exchange Supply - Day.csv` | Bitcoin Exchange Supply - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 8 |
| `CryptoQuant/BTC/Market Data/Bitcoin Geographical Supply Distribution by Entities - Day.csv` | Bitcoin Geographical Supply Distribution by Entities - Day | 2006-04-11 .. 2026-04-10 | 7,305 | daily | 0 | 5 |
| `CryptoQuant/BTC/Market Data/Bitcoin Market Cap - Day.csv` | Market cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Price & Volume - Spot, All Exchanges, BTC-USD - Day.csv` | Price & volume | 2009-01-03 .. 2026-04-11 | 6,308 | daily | 0 | 7 |
| `CryptoQuant/BTC/Market Data/Bitcoin Price & Volume KRW - Spot - Day.csv` | Price & volume | 2013-09-03 .. 2026-04-10 | 4,594 | daily | 9 | 7 |
| `CryptoQuant/BTC/Market Data/Bitcoin Realized Cap - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Realized Cap - UTXO Age Bands (%) - Day.csv` | Realized cap | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Data/Bitcoin Realized Cap - UTXO Age Bands USD - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Data/Bitcoin Realized Cap - UTXO Value Bands (%) - Day.csv` | Realized cap | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 |
| `CryptoQuant/BTC/Market Data/Bitcoin Realized Cap - UTXO Value Bands USD - Day.csv` | Realized cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 10 |
| `CryptoQuant/BTC/Market Data/Bitcoin Taker Buy Ratio - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Taker Buy Sell Ratio - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Taker Buy Volume - All Exchanges - Day.csv` | Taker buy volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Taker Sell Ratio - All Exchanges - Day.csv` | Taker sell volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Taker Sell Volume - All Exchanges - Day.csv` | Taker sell volume | 2015-09-26 .. 2026-04-11 | 3,851 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Thermo Cap - Day.csv` | Thermo cap | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Data/Bitcoin Trading Volume (KYC VS. Non-KYC) - Day.csv` | Bitcoin Trading Volume (KYC VS. Non-KYC) - Day | 2013-10-21 .. 2026-04-10 | 4,555 | daily | 0 | 4 |
| `CryptoQuant/BTC/Market Data/Bitcoin Trading Volume (Spot VS. Derivative) - Day.csv` | Bitcoin Trading Volume (Spot VS. Derivative) - Day | 2013-10-21 .. 2026-04-10 | 4,555 | daily | 0 | 4 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Adjusted SOPR (aSOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Average Dormancy - Day.csv` | Bitcoin Average Dormancy - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Average Supply-Adjusted CDD - Day.csv` | Bitcoin Average Supply-Adjusted CDD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Binary CDD - Day.csv` | Bitcoin Binary CDD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Long Term Holder SOPR - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Mean Coin Age - Day.csv` | Bitcoin Mean Coin Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Mean Coin Dollar Age - Day.csv` | Bitcoin Mean Coin Dollar Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin MVRV Ratio - Day.csv` | MVRV ratio | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Net Unrealized Loss (NUL) - Day.csv` | Bitcoin Net Unrealized Loss (NUL) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Net Unrealized Profit (NUP) - Day.csv` | Bitcoin Net Unrealized Profit (NUP) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Net Unrealized Profit_Loss (NUPL) - Day.csv` | NUPL | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin NVM Ratio - Day.csv` | Bitcoin NVM Ratio - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin NVT Golden Cross - Day.csv` | NVT | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin NVT Ratio - Day.csv` | NVT | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Puell Multiple - Day.csv` | Puell multiple | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Realized Price - Day.csv` | Realized price | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Realized Price - UTXO Age Bands - Day.csv` | Realized price | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Short Term Holder SOPR - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin SOPR Ratio (LTH-SOPR_STH-SOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spent Output Age Bands (%) - Day.csv` | Bitcoin Spent Output Age Bands (%) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spent Output Age Bands - Day.csv` | Bitcoin Spent Output Age Bands - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spent Output Age Bands USD - Day.csv` | Bitcoin Spent Output Age Bands USD - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spent Output Profit Ratio (SOPR) - Day.csv` | SOPR | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spent Output Value Bands (%) - Day.csv` | Bitcoin Spent Output Value Bands (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spent Output Value Bands - Day.csv` | Bitcoin Spent Output Value Bands - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spent Output Value Bands USD - Day.csv` | Bitcoin Spent Output Value Bands USD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Spot Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2017-01-01 .. 2026-04-11 | 3,388 | daily | 0 | 5 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Stock-to-Flow Ratio - Day.csv` | Bitcoin Stock-to-Flow Ratio - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Stock-to-Flow Reversion - Day.csv` | Bitcoin Stock-to-Flow Reversion - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Sum Coin Age - Day.csv` | Bitcoin Sum Coin Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Sum Coin Age Distribution (%) - Day.csv` | Bitcoin Sum Coin Age Distribution (%) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Sum Coin Age Distribution - Day.csv` | Bitcoin Sum Coin Age Distribution - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 15 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Sum Coin Dollar Age - Day.csv` | Bitcoin Sum Coin Dollar Age - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Supply Adjusted Dormancy - Day.csv` | Bitcoin Supply Adjusted Dormancy - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Supply in Loss (%) - Day.csv` | Bitcoin Supply in Loss (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Supply in Loss - Day.csv` | Bitcoin Supply in Loss - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Supply in Profit (%) - Day.csv` | Bitcoin Supply in Profit (%) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Supply in Profit - Day.csv` | Bitcoin Supply in Profit - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Market Indicator/Bitcoin Supply-Adjusted CDD - Day.csv` | Bitcoin Supply-Adjusted CDD - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Flow (Mean) - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Flow (Total) - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day.csv` | Bitcoin Exchange to Miner Transactions - All Exchanges, All Miners - Day | 2012-07-11 .. 2026-04-11 | 5,023 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Depositing Addresses - All Miners - Day.csv` | Bitcoin Miner Depositing Addresses - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Depositing Transactions - All Miners - Day.csv` | Bitcoin Miner Depositing Transactions - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner In-House Flow (Mean) - All Miners - Day.csv` | Bitcoin Miner In-House Flow (Mean) - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner In-House Flow (Total) - All Miners - Day.csv` | Bitcoin Miner In-House Flow (Total) - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner In-House Transactions - All Miners - Day.csv` | Bitcoin Miner In-House Transactions - All Miners - Day | 2009-01-12 .. 2026-04-11 | 6,299 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Inflow (Mean) - All Miners - Day.csv` | Bitcoin Miner Inflow (Mean) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Inflow (Top10) - All Miners - Day.csv` | Bitcoin Miner Inflow (Top10) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Inflow (Total) - All Miners - Day.csv` | Bitcoin Miner Inflow (Total) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Netflow Total - All Miners - Day.csv` | Miner netflow | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Outflow (Mean) - All Miners - Day.csv` | Bitcoin Miner Outflow (Mean) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Outflow (Top10) - All Miners - Day.csv` | Bitcoin Miner Outflow (Top10) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Outflow (Total) - All Miners - Day.csv` | Bitcoin Miner Outflow (Total) - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Reserve - All Miners - Day.csv` | Miner reserve | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Reserve USD - All Miners - Day.csv` | Miner reserve | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Supply Ratio - All Miners - Day.csv` | Bitcoin Miner Supply Ratio - All Miners - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner to Exchange Flow (Mean) - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Flow (Mean) - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner to Exchange Flow (Total) - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Flow (Total) - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner to Exchange Transactions - All Miners, All Exchanges - Day.csv` | Bitcoin Miner to Exchange Transactions - All Miners, All Exchanges - Day | 2012-04-25 .. 2026-04-11 | 5,100 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Withdrawing Addresses - All Miners - Day.csv` | Bitcoin Miner Withdrawing Addresses - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miner Withdrawing Transactions - All Miners - Day.csv` | Bitcoin Miner Withdrawing Transactions - All Miners - Day | 2009-01-09 .. 2026-04-11 | 6,302 | daily | 0 | 3 |
| `CryptoQuant/BTC/Miner Flows/Bitcoin Miners' Position Index (MPI) - Day.csv` | Bitcoin Miners' Position Index (MPI) - Day | 2011-01-07 .. 2026-04-10 | 5,573 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin Coin Days Destroyed (CDD) - Day.csv` | Bitcoin Coin Days Destroyed (CDD) - Day | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Age Bands (%) - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Age Bands - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Age Bands USD - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Count - Age Bands (%) - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Count - Age Bands - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 15 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Count - Value Bands (%) - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 10 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Count - Value Bands - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Value Bands (%) - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXO Value Bands - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 10 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXOs in Loss (%) - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXOs in Loss - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXOs in Profit (%) - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Indicator/Bitcoin UTXOs in Profit - Day.csv` | UTXO metrics | 2020-12-31 .. 2026-04-10 | 1,927 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Stats/Bitcoin Block Interval (Mean) - Day.csv` | Bitcoin Block Interval (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Stats/Bitcoin Block Size (Mean) - Day.csv` | Bitcoin Block Size (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Stats/Bitcoin Blocks Mined - Day.csv` | Bitcoin Blocks Mined - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Stats/Bitcoin Difficulty - Day.csv` | Difficulty | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Stats/Bitcoin Hashrate - Day.csv` | Hashrate | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Stats/Bitcoin UTXO Count - Day.csv` | UTXO metrics | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Network Stats/Bitcoin Velocity - Day.csv` | Bitcoin Velocity - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Supply/Bitcoin New Supply - Day.csv` | Bitcoin New Supply - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Supply/Bitcoin Total Supply - Day.csv` | Bitcoin Total Supply - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Transactions/Bitcoin Tokens Transferred (Mean) - Day.csv` | Bitcoin Tokens Transferred (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Transactions/Bitcoin Tokens Transferred (Median) - Day.csv` | Bitcoin Tokens Transferred (Median) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Transactions/Bitcoin Tokens Transferred (Total) - Day.csv` | Bitcoin Tokens Transferred (Total) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Transactions/Bitcoin Transaction Count (Mean) - Day.csv` | Bitcoin Transaction Count (Mean) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/BTC/Transactions/Bitcoin Transaction Count (Total) - Day.csv` | Bitcoin Transaction Count (Total) - Day | 2009-01-03 .. 2026-04-10 | 6,307 | daily | 0 | 3 |
| `CryptoQuant/ETH/Addresses/Ethereum Active Addresses - Day.csv` | Active addresses | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Addresses/Ethereum Active Addresses - Internal, External, EOA - Day.csv` | Active addresses | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 |
| `CryptoQuant/ETH/Addresses/Ethereum Active Receiving Addresses - Day.csv` | Ethereum Active Receiving Addresses - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Addresses/Ethereum Active Receiving Addresses - Internal, External, EOA - Day.csv` | Ethereum Active Receiving Addresses - Internal, External, EOA - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 |
| `CryptoQuant/ETH/Addresses/Ethereum Active Sending Addresses - Day.csv` | Ethereum Active Sending Addresses - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Addresses/Ethereum Active Sending Addresses - Internal, External, EOA - Day.csv` | Ethereum Active Sending Addresses - Internal, External, EOA - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 |
| `CryptoQuant/ETH/Derivatives/Ethereum Estimated Leverage Ratio - All Exchanges - Day.csv` | Estimated leverage ratio | 2019-03-30 .. 2026-04-10 | 2,569 | daily | 0 | 3 |
| `CryptoQuant/ETH/Derivatives/Ethereum Funding Rates - All Exchanges - Day.csv` | Funding rates | 2018-08-02 .. 2026-04-11 | 2,810 | daily | 0 | 3 |
| `CryptoQuant/ETH/Derivatives/Ethereum Futures Taker CVD(Cumulative Volume Delta, 90-day) - Day.csv` | Taker CVD | 2019-01-13 .. 2026-04-11 | 2,646 | daily | 0 | 5 |
| `CryptoQuant/ETH/Derivatives/Ethereum Long Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 |
| `CryptoQuant/ETH/Derivatives/Ethereum Long Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 |
| `CryptoQuant/ETH/Derivatives/Ethereum Open Interest - All Exchanges, All Symbol - Day.csv` | Open interest | 2019-03-30 .. 2026-04-11 | 2,570 | daily | 0 | 3 |
| `CryptoQuant/ETH/Derivatives/Ethereum Short Liquidations - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 |
| `CryptoQuant/ETH/Derivatives/Ethereum Short Liquidations USD - All Exchanges, All Symbol - Day.csv` | Liquidations | 2018-12-28 .. 2026-04-11 | 2,662 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum Cumulative TXs to ETH 2.0 Contract - Day.csv` | Ethereum Cumulative TXs to ETH 2.0 Contract - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum ETH 2.0 Staking Rate (%) - Day.csv` | Ethereum ETH 2.0 Staking Rate (%) - Day | 2020-11-03 .. 2026-04-10 | 1,985 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum New Depositors - Day.csv` | Ethereum New Depositors - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum Number of ETH 2.0 Deposits - Day.csv` | Ethereum Number of ETH 2.0 Deposits - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum Number of Unique Depositors - Day.csv` | Ethereum Number of Unique Depositors - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum Phase 0 Success Rate (%) - Day.csv` | Ethereum Phase 0 Success Rate (%) - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum Staking Inflow Total - Day.csv` | Ethereum Staking Inflow Total - Day | 2020-11-03 .. 2026-04-06 | 1,981 | daily | 0 | 3 |
| `CryptoQuant/ETH/ETH 2.0/Ethereum Total Value Staked - Day.csv` | Ethereum Total Value Staked - Day | 2020-11-03 .. 2026-04-10 | 1,985 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Depositing Addresses - All Exchanges - Day.csv` | Ethereum Exchange Depositing Addresses - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Depositing Transactions - All Exchanges - Day.csv` | Ethereum Exchange Depositing Transactions - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2015-08-13 .. 2026-04-11 | 3,895 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Reserve USD - All Exchanges - Day.csv` | Exchange reserve | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Ethereum Exchange Withdrawing Addresses - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 |
| `CryptoQuant/ETH/Exchange Flows/Ethereum Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Ethereum Exchange Withdrawing Transactions - All Exchanges - Day | 2015-08-07 .. 2026-04-11 | 3,901 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees Burnt (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees Burnt per Transaction (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees Burnt per Transaction (Median) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees Burnt per Transaction USD (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees Burnt per Transaction USD (Median) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees Burnt USD (Total) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees per Transaction (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fees And Revenue/Ethereum Fees per Transaction USD (Mean) - Day.csv` | Fees | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Flow Indicator/Ethereum Exchange Supply Ratio - All Exchanges - Day.csv` | Ethereum Exchange Supply Ratio - All Exchanges - Day | 2015-07-30 .. 2026-04-10 | 3,908 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fund Data/Ethereum Coinbase Premium Gap - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fund Data/Ethereum Coinbase Premium Index - Day.csv` | Coinbase premium | 2017-08-17 .. 2026-04-10 | 3,159 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fund Data/Ethereum Fund Holdings - All Symbol - Day.csv` | Fund holdings | 2020-11-04 .. 2026-04-09 | 1,983 | daily | 0 | 3 |
| `CryptoQuant/ETH/Fund Data/Ethereum Fund Market Premium - All Symbol - Day.csv` | Fund market premium | 2020-11-04 .. 2026-04-09 | 1,379 | daily | 604 | 3 |
| `CryptoQuant/ETH/Fund Data/Ethereum Fund Price (USD) - ETHE - Day.csv` | Fund price | 2019-06-14 .. 2026-04-02 | 1,710 | daily | 775 | 3 |
| `CryptoQuant/ETH/Fund Data/Ethereum Fund Volume - All Symbol - Day.csv` | Fund volume | 2019-06-14 .. 2026-04-09 | 1,738 | daily | 754 | 3 |
| `CryptoQuant/ETH/Fund Data/Ethereum Korea Premium Index - Day.csv` | Korea premium | 2020-07-16 .. 2026-04-10 | 2,095 | daily | 0 | 3 |
| `CryptoQuant/ETH/Market Data/Ethereum Market Cap - Day.csv` | Market cap | 2015-08-07 .. 2026-04-10 | 3,900 | daily | 0 | 3 |
| `CryptoQuant/ETH/Market Data/Ethereum Price & Volume - Spot, All Exchanges, ETH-USD - Day.csv` | Price & volume | 2015-08-07 .. 2026-04-11 | 3,896 | daily | 5 | 7 |
| `CryptoQuant/ETH/Market Data/Ethereum Price & Volume KRW - Spot - Day.csv` | Price & volume | 2016-04-08 .. 2026-04-10 | 3,654 | daily | 1 | 7 |
| `CryptoQuant/ETH/Market Data/Ethereum Taker Buy Ratio - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 |
| `CryptoQuant/ETH/Market Data/Ethereum Taker Buy Sell Ratio - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 |
| `CryptoQuant/ETH/Market Data/Ethereum Taker Buy Volume - All Exchanges - Day.csv` | Taker buy volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 |
| `CryptoQuant/ETH/Market Data/Ethereum Taker Sell Ratio - All Exchanges - Day.csv` | Taker sell volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 |
| `CryptoQuant/ETH/Market Data/Ethereum Taker Sell Volume - All Exchanges - Day.csv` | Taker sell volume | 2018-09-01 .. 2026-04-11 | 2,780 | daily | 0 | 3 |
| `CryptoQuant/ETH/Network Stats/Ethereum Destroyed Contracts - Day.csv` | Ethereum Destroyed Contracts - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Network Stats/Ethereum New Contracts - Day.csv` | Ethereum New Contracts - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Network Stats/Ethereum Number of Contracts - Day.csv` | Ethereum Number of Contracts - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Contract Calls (Mean) - Day.csv` | Ethereum Contract Calls (Mean) - Day | 2015-07-30 .. 2026-04-10 | 3,908 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Contract Calls (Total) - Day.csv` | Ethereum Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum External Contract Calls (Mean) - Day.csv` | Ethereum External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum External Contract Calls (Total) - Day.csv` | Ethereum External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred (Mean) - Day.csv` | Ethereum Tokens Transferred (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred (Median) - Day.csv` | Ethereum Tokens Transferred (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred (Total) - Day.csv` | Ethereum Tokens Transferred (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day.csv` | Ethereum Tokens Transferred - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred Between EOA (Mean) - Day.csv` | Ethereum Tokens Transferred Between EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred Between EOA (Total) - Day.csv` | Ethereum Tokens Transferred Between EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred Between EOA USD (Mean) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred Between EOA USD (Median) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred Between EOA USD (Total) - Day.csv` | Ethereum Tokens Transferred Between EOA USD (Total) - Day | 2015-07-30 .. 2026-04-10 | 3,908 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by Contract Calls (Mean) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by Contract Calls (Median) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by Contract Calls (Total) - Day.csv` | Ethereum Tokens Transferred by Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by Contract Calls USD (Mean) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by Contract Calls USD (Median) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by Contract Calls USD (Total) - Day.csv` | Ethereum Tokens Transferred by Contract Calls USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by External Contract Calls (Mean) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by External Contract Calls (Median) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by External Contract Calls (Total) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by External Contract Calls USD (Mean) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by External Contract Calls USD (Median) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Median) - Day | 2024-09-22 .. 2026-04-10 | 566 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred by External Contract Calls USD (Total) - Day.csv` | Ethereum Tokens Transferred by External Contract Calls USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred USD (Mean) - Day.csv` | Ethereum Tokens Transferred USD (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred USD (Median) - Day.csv` | Ethereum Tokens Transferred USD (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred USD (Total) - Day.csv` | Ethereum Tokens Transferred USD (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred USD - Internal, External, EOA (Mean) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred USD - Internal, External, EOA (Median) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Median) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Tokens Transferred USD - Internal, External, EOA (Total) - Day.csv` | Ethereum Tokens Transferred USD - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Transaction Count (Mean) - Day.csv` | Ethereum Transaction Count (Mean) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transaction Count (Total) - Day.csv` | Ethereum Transaction Count (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transaction Count - Internal, External, EOA (Total) - Day.csv` | Ethereum Transaction Count - Internal, External, EOA (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Transactions Between EOA (Mean) - Day.csv` | Ethereum Transactions Between EOA (Mean) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transactions Between EOA (Total) - Day.csv` | Ethereum Transactions Between EOA (Total) - Day | 2020-11-02 .. 2026-04-10 | 1,986 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transfer Count - Internal, External, EOA (Mean) - Day.csv` | Ethereum Transfer Count - Internal, External, EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Transfer Count - Internal, External, EOA (Total) - Day.csv` | Ethereum Transfer Count - Internal, External, EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 5 |
| `CryptoQuant/ETH/Transactions/Ethereum Transfers Between EOA (Mean) - Day.csv` | Ethereum Transfers Between EOA (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transfers Between EOA (Total) - Day.csv` | Ethereum Transfers Between EOA (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transfers by Contract Calls (Mean) - Day.csv` | Ethereum Transfers by Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transfers by External Contract Calls (Mean) - Day.csv` | Ethereum Transfers by External Contract Calls (Mean) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/ETH/Transactions/Ethereum Transfers by External Contract Calls (Total) - Day.csv` | Ethereum Transfers by External Contract Calls (Total) - Day | 2025-04-11 .. 2026-04-10 | 365 | daily | 0 | 3 |
| `CryptoQuant/USDC/Addresses/USD Coin(ERC20) Active Addresses - Day.csv` | Active addresses | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDC/Addresses/USD Coin(ERC20) Active Receiving Addresses (%) - Day.csv` | USD Coin(ERC20) Active Receiving Addresses (%) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDC/Addresses/USD Coin(ERC20) Active Receiving Addresses - Day.csv` | USD Coin(ERC20) Active Receiving Addresses - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDC/Addresses/USD Coin(ERC20) Active Sending Addresses (%) - Day.csv` | USD Coin(ERC20) Active Sending Addresses (%) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDC/Addresses/USD Coin(ERC20) Active Sending Addresses - Day.csv` | USD Coin(ERC20) Active Sending Addresses - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Depositing Addresses - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Depositing Transactions - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2018-09-12 .. 2026-04-11 | 2,769 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Exchange Flows/USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2018-09-12 .. 2026-04-12 | 2,770 | daily | 0 | 3 |
| `CryptoQuant/USDC/Flow Indicator/USD Coin(ERC20) Exchange Supply Ratio - All Exchanges - Day.csv` | USD Coin(ERC20) Exchange Supply Ratio - All Exchanges - Day | 2018-09-10 .. 2026-04-11 | 2,771 | daily | 0 | 3 |
| `CryptoQuant/USDC/Transactions/USD Coin(ERC20) Tokens Transferred (Mean) - Day.csv` | USD Coin(ERC20) Tokens Transferred (Mean) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDC/Transactions/USD Coin(ERC20) Tokens Transferred (Total) - Day.csv` | USD Coin(ERC20) Tokens Transferred (Total) - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDC/Transactions/USD Coin(ERC20) Transfer Event Count - Day.csv` | USD Coin(ERC20) Transfer Event Count - Day | 2018-09-10 .. 2026-04-11 | 2,761 | daily | 10 | 3 |
| `CryptoQuant/USDT (TRX)/Addresses/Tether USD(TRC20) Active Addresses - Day.csv` | Active addresses | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Addresses/Tether USD(TRC20) Active Receiving Addresses (%) - Day.csv` | Tether USD(TRC20) Active Receiving Addresses (%) - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Addresses/Tether USD(TRC20) Active Receiving Addresses - Day.csv` | Tether USD(TRC20) Active Receiving Addresses - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Addresses/Tether USD(TRC20) Active Sending Addresses (%) - Day.csv` | Tether USD(TRC20) Active Sending Addresses (%) - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Addresses/Tether USD(TRC20) Active Sending Addresses - Day.csv` | Tether USD(TRC20) Active Sending Addresses - Day | 2019-07-01 .. 2026-04-08 | 2,474 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | Tether USD(TRC20) Exchange Depositing Transactions - All Exchanges - Day | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT (TRX)/Exchange Flows/Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Tether USD(TRC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2019-07-17 .. 2026-04-09 | 2,459 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Addresses/Tether USD(ERC20) Active Addresses - Day.csv` | Active addresses | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/USDT ETH/Addresses/Tether USD(ERC20) Active Receiving Addresses (%) - Day.csv` | Tether USD(ERC20) Active Receiving Addresses (%) - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/USDT ETH/Addresses/Tether USD(ERC20) Active Receiving Addresses - Day.csv` | Tether USD(ERC20) Active Receiving Addresses - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/USDT ETH/Addresses/Tether USD(ERC20) Active Sending Addresses (%) - Day.csv` | Tether USD(ERC20) Active Sending Addresses (%) - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/USDT ETH/Addresses/Tether USD(ERC20) Active Sending Addresses - Day.csv` | Tether USD(ERC20) Active Sending Addresses - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Depositing Addresses - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Depositing Transactions - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Inflow (Mean) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Inflow (Top10) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Inflow (Total) - All Exchanges - Day.csv` | Exchange inflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Netflow (Total) - All Exchanges - Day.csv` | Exchange netflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Outflow (Mean) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Outflow (Top10) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Outflow (Total) - All Exchanges - Day.csv` | Exchange outflow | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Reserve - All Exchanges - Day.csv` | Exchange reserve | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Withdrawing Addresses - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Exchange Flows/Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Withdrawing Transactions - All Exchanges - Day | 2017-12-28 .. 2026-04-11 | 3,027 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Flow Indicator/Tether USD(ERC20) Exchange Supply Ratio - All Exchanges - Day.csv` | Tether USD(ERC20) Exchange Supply Ratio - All Exchanges - Day | 2017-11-28 .. 2026-04-10 | 3,056 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Market Data/Tether USD(ERC20) Market Cap - Day.csv` | Market cap | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/USDT ETH/Supply/Tether USD(ERC20) Total Supply - Day.csv` | Tether USD(ERC20) Total Supply - Day | 2017-11-28 .. 2026-04-11 | 3,057 | daily | 0 | 3 |
| `CryptoQuant/USDT ETH/Transactions/Tether USD(ERC20) Tokens Transferred (Total) - Day.csv` | Tether USD(ERC20) Tokens Transferred (Total) - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/USDT ETH/Transactions/Tether USD(ERC20) Transfer Event Count - Day.csv` | Tether USD(ERC20) Transfer Event Count - Day | 2017-11-28 .. 2026-04-11 | 3,008 | daily | 49 | 3 |
| `CryptoQuant/WBTC/Addresses/Wrapped BTC Active Addresses - Day.csv` | Active addresses | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Addresses/Wrapped BTC Active Receiving Addresses - Day.csv` | Wrapped BTC Active Receiving Addresses - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Addresses/Wrapped BTC Active Sending Addresses - Day.csv` | Wrapped BTC Active Sending Addresses - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Transactions/Wrapped BTC Tokens Transferred (Mean) - Day.csv` | Wrapped BTC Tokens Transferred (Mean) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Transactions/Wrapped BTC Tokens Transferred (Median) - Day.csv` | Wrapped BTC Tokens Transferred (Median) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Transactions/Wrapped BTC Tokens Transferred (Total) - Day.csv` | Wrapped BTC Tokens Transferred (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Transactions/Wrapped BTC Transaction Count (Mean) - Day.csv` | Wrapped BTC Transaction Count (Mean) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Transactions/Wrapped BTC Transaction Count (Total) - Day.csv` | Wrapped BTC Transaction Count (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |
| `CryptoQuant/WBTC/Transactions/Wrapped BTC Transfer Count (Total) - Day.csv` | Wrapped BTC Transfer Count (Total) - Day | 2018-11-24 .. 2026-04-11 | 2,696 | daily | 0 | 3 |

### DefiLlama

All DefiLlama data — programmatic TVL panels plus manual website exports. Organised into topical subfolders: `TVL/` (all-chain / per-chain TVL daily and weekly panels), `Stablecoins/` (market cap time-series + entity lists), `ETFs/` (flow history + overview snapshot), `RWA/` (real-world-asset market-cap and TVL by category), `ChainMetrics/` (chain-level all-in-one dashboards: fees, revenue, volumes, TVL), `CEX/` (centralized-exchange net inflows by exchange), `DATs/` (public-company digital-asset-treasuries snapshot).

| Relative path | Topic | Date range | Rows | Freq | Missing days | Cols |
| --- | --- | --- | ---: | --- | ---: | ---: |
| `DefiLlama/_raw_parts/cex_inflows/cex-inflows-chart_combined_2026-04-17 part 1.csv` | cex-inflows-chart_combined_2026-04-17 part 1 | 2022-11-12 .. 2026-04-17 | 1,253 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/cex_inflows/cex-inflows-chart_combined_2026-04-17 part 2.csv` | cex-inflows-chart_combined_2026-04-17 part 2 | 2023-06-16 .. 2026-04-17 | 1,037 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/cex_inflows/cex-inflows-chart_combined_2026-04-17 part 3.csv` | cex-inflows-chart_combined_2026-04-17 part 3 | 2022-11-22 .. 2026-04-17 | 1,243 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17 (1) part 5.csv` | Stablecoin | 2020-11-14 .. 2026-04-17 | 1,981 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17 (1) part 6.csv` | Stablecoin | 2020-07-16 .. 2026-04-17 | 2,102 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17 (1) part 7.csv` | Stablecoin | 2020-12-31 .. 2026-04-17 | 1,934 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17 part 1.csv` | Stablecoin | 2017-11-29 .. 2026-04-17 | 3,062 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17 part 2.csv` | Stablecoin | 2020-12-02 .. 2026-04-17 | 1,963 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17 part 3.csv` | Stablecoin | 2020-01-04 .. 2026-04-17 | 2,296 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17 part 4.csv` | Stablecoin | 2018-09-11 .. 2026-04-17 | 2,776 | daily | 0 | 26 |
| `DefiLlama/_raw_parts/stablecoin_mcap/stablecoin-mcap-chart_combined_2026-04-17.csv` | Stablecoin | 2020-12-03 .. 2026-04-17 | 1,962 | daily | 0 | 26 |
| `DefiLlama/CEX/cex_net_inflows_by_exchange__daily.csv` | CEX net inflows | 2022-11-12 .. 2026-04-17 | 1,253 | daily | 0 | 76 |
| `DefiLlama/ChainMetrics/all_metrics_2026-04-17 (1) volume.csv` | all_metrics_2026-04-17 (1) volume | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 38 |
| `DefiLlama/ChainMetrics/all_metrics_2026-04-17.csv` | all_metrics_2026-04-17 | 2016-04-19 .. 2026-04-17 | 3,644 | daily | 7 | 40 |
| `DefiLlama/ChainMetrics/ethereum_metrics_2026-04-17 (1).csv` | ethereum_metrics_2026-04-17 (1) | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 |
| `DefiLlama/ChainMetrics/ethereum_metrics_2026-04-17 Fees and revenue.csv` | Fees | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 |
| `DefiLlama/ChainMetrics/ethereum_metrics_2026-04-17 volume.csv` | ethereum_metrics_2026-04-17 volume | 2017-09-27 .. 2026-04-17 | 3,125 | daily | 0 | 48 |
| `DefiLlama/ChainMetrics/solana_metrics_2026-04-17.csv` | Solana | 2021-03-18 .. 2026-04-17 | 1,857 | daily | 0 | 38 |
| `DefiLlama/DATs/dat-institutions.csv` | Public-company digital-asset treasuries | — | 86 | snapshot | — | 11 |
| `DefiLlama/ETFs/etf-history.csv` | ETF | 2024-01-11 .. 2026-04-14 | 565 | daily | 260 | 3 |
| `DefiLlama/ETFs/etf-overview.csv` | ETF | — | 25 | snapshot | — | 6 |
| `DefiLlama/RWA/rwa-category-chart_combined_2026-04-17.csv` | Real-world assets (RWA) | 2021-09-04 .. 2026-04-17 | 1,687 | daily | 0 | 13 |
| `DefiLlama/RWA/rwa-time-series-chart-active-mcap-all-2026-04-14.csv` | Real-world assets (RWA) | 2021-09-04 .. 2026-04-14 | 1,684 | daily | 0 | 19 |
| `DefiLlama/RWA/rwa-time-series-chart-defi-active-tvl-all-2026-04-14.csv` | TVL | 2021-10-25 .. 2026-04-14 | 1,633 | daily | 0 | 19 |
| `DefiLlama/RWA/rwa-time-series-chart-onchain-mcap-all-2026-04-14.csv` | Real-world assets (RWA) | 2021-09-04 .. 2026-04-14 | 1,684 | daily | 0 | 22 |
| `DefiLlama/Stablecoins/stablecoin_mcap_by_defillama_id__daily.csv` | Stablecoin | 2017-11-29 .. 2026-04-17 | 3,062 | daily | 0 | 201 |
| `DefiLlama/Stablecoins/stablecoin_mcap_id_to_name.csv` | Stablecoin | — | 200 | snapshot | — | 4 |
| `DefiLlama/Stablecoins/stablecoins-chains.csv` | Stablecoin | — | 175 | snapshot | — | 3 |
| `DefiLlama/Stablecoins/stablecoins.csv` | Stablecoin | — | 360 | snapshot | — | 10 |
| `DefiLlama/TVL/Daily/tvl_all_chains_daily.csv` | TVL | 2017-09-27 .. 2026-04-14 | 3,122 | daily | 0 | 2 |
| `DefiLlama/TVL/Daily/tvl_by_chain_long_daily.csv` | TVL | 2017-09-27 .. 2024-09-13 | 200,000 | daily | 0 | 3 |
| `DefiLlama/TVL/Daily/tvl_by_chain_wide_daily.csv` | TVL | 2017-09-27 .. 2026-04-14 | 3,122 | daily | 0 | 440 |
| `DefiLlama/TVL/Snapshot/tvl_chains_current.csv` | TVL | — | 440 | snapshot | — | 6 |
| `DefiLlama/TVL/Snapshot/tvl_protocols_current.csv` | TVL | — | 7,317 | snapshot | — | 56 |
| `DefiLlama/TVL/Weekly/tvl_all_chains_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 447 | weekly | — | 2 |
| `DefiLlama/TVL/Weekly/tvl_by_chain_long_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 60,392 | weekly | — | 3 |
| `DefiLlama/TVL/Weekly/tvl_by_chain_wide_weekly.csv` | TVL | 2017-10-01 .. 2026-04-19 | 447 | weekly | — | 440 |

### Farside ETF Data

Daily US$m net flows for US spot BTC, ETH, and SOL ETFs. See `Farside_ETF_Data_Summary.txt` for ticker list per asset.

| Relative path | Topic | Date range | Rows | Freq | Missing days | Cols |
| --- | --- | --- | ---: | --- | ---: | ---: |
| `Farside ETF Data/BTC/bitcoin_etf_flow_all_data.csv` | ETF | 2024-01-11 .. 2026-04-10 | 579 | daily | 242 | 14 |
| `Farside ETF Data/ETH/ethereum_etf_flow_all_data.csv` | ETF | 2024-07-23 .. 2026-04-10 | 441 | daily | 186 | 12 |
| `Farside ETF Data/SOL/solana_etf_flow_all_data.csv` | ETF | 2026-03-25 .. 2026-04-10 | 12 | daily | 5 | 8 |

### Tradingview

Manual chart-to-CSV exports from TradingView for CME futures (BTC, ETH, Micro BTC, Micro ETH, SOL), BlackRock ETF-vs-spot ratios (IBIT, ETHA), and Deribit's DVOL.

| Relative path | Topic | Date range | Rows | Freq | Missing days | Cols |
| --- | --- | --- | ---: | --- | ---: | ---: |
| `Tradingview/tradingview__CME_BTC_front_month_futures__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,096 | daily | 946 | 12 |
| `Tradingview/tradingview__CME_BTC_futures_minus_SPOT_BTC_basis__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,102 | daily | 940 | 12 |
| `Tradingview/tradingview__CME_BTC_futures_over_SPOT_BTC_ratio__daily.csv` | CME BTC futures | 2017-12-17 .. 2026-04-15 | 2,102 | daily | 940 | 12 |
| `Tradingview/tradingview__CME_ETH_front_month_futures__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,307 | daily | 590 | 12 |
| `Tradingview/tradingview__CME_ETH_futures_minus_SPOT_ETH_basis__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,308 | daily | 589 | 12 |
| `Tradingview/tradingview__CME_ETH_futures_over_SPOT_ETH_ratio__daily.csv` | CME ETH futures | 2021-02-04 .. 2026-04-15 | 1,308 | daily | 589 | 12 |
| `Tradingview/tradingview__CME_Micro_Bitcoin_futures__daily.csv` | CME Micro BTC futures | 2018-03-25 .. 2026-04-15 | 1,685 | daily | 1259 | 12 |
| `Tradingview/tradingview__CME_Micro_Ether_futures__daily.csv` | CME Micro ETH futures | 2021-12-01 .. 2026-04-15 | 1,099 | daily | 498 | 12 |
| `Tradingview/tradingview__CME_Solana_futures__daily.csv` | Solana | 2025-03-16 .. 2026-04-15 | 274 | daily | 122 | 12 |
| `Tradingview/tradingview__Deribit_BTC_volatility_index_DVOL__daily.csv` | Deribit volatility index | 2021-03-24 .. 2026-04-16 | 1,850 | daily | 0 | 6 |
| `Tradingview/tradingview__ETHA_ETF_over_SPOT_ETH__daily.csv` | ETF | 2024-07-23 .. 2026-04-16 | 435 | daily | 198 | 12 |
| `Tradingview/tradingview__IBIT_ETF_over_SPOT_BTC__daily.csv` | ETF | 2024-01-11 .. 2026-04-16 | 567 | daily | 260 | 12 |

## Machine-readable version

The same information (plus column lists and SHA-256) is in `Data/MASTER_DATA.csv` for programmatic consumption.

_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`._
