# References

## Data Sources

- Alternative.me. [Crypto Fear and Greed Index API](https://alternative.me/crypto/fear-and-greed-index/).
- Artemis. [Crypto fundamentals data](https://www.artemisanalytics.com/). Local provider exports are not redistributed.
- Binance. [Binance Public Data archive](https://data.binance.vision/). Monthly spot-kline ZIP files are checksum verified.
- CFTC. [Commitments of Traders historical compressed files](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm).
- CryptoQuant. [CryptoQuant data](https://cryptoquant.com/). Local provider exports are not redistributed.
- DefiLlama. [API documentation](https://defillama.com/docs/api).
- Federal Reserve Bank of St. Louis. [FRED](https://fred.stlouisfed.org/).
- Farside Investors. [Bitcoin ETF flow data](https://farside.co.uk/btc/) and [Ethereum ETF flow data](https://farside.co.uk/eth/).
- SEC. [EDGAR application programming interfaces](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).
- TradingView. [Market data](https://www.tradingview.com/). Local exports are not redistributed.

The contract, access, history, timing, and analysis-enablement decision for each proposed public source is recorded in [`research/source_decisions.csv`](research/source_decisions.csv). Raw objects remain local; their portable paths and SHA-256 hashes are recorded in [`research/raw_objects.csv`](research/raw_objects.csv).

## Event Sources

Event dates and retrieval dates are registered in [`config/events.yml`](config/events.yml). Sources include the SEC spot-Bitcoin ETP statement and Ether ETP order, the Ethereum Foundation Dencun announcement, FDIC's SVB receivership record, BIS's August 2024 carry-unwind review, SEC case records for Terra and FTX, and the on-chain record for Bitcoin block 840000.

## Methods

- Benjamini, Y., and Hochberg, Y. (1995). Controlling the false discovery rate. *Journal of the Royal Statistical Society, Series B*, 57(1), 289-300.
- Diebold, F. X., and Yilmaz, K. (2014). On the network topology of variance decompositions: Measuring the connectedness of financial firms. *Journal of Econometrics*, 182(1), 119-134.
- Driscoll, J. C., and Kraay, A. C. (1998). Consistent covariance matrix estimation with spatially dependent panel data. *Review of Economics and Statistics*, 80(4), 549-560.
- Kunsch, H. R. (1989). The jackknife and the bootstrap for general stationary observations. *Annals of Statistics*, 17(3), 1217-1241.
- Newey, W. K., and West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica*, 55(3), 703-708.
- Pesaran, H. H., and Shin, Y. (1998). Generalized impulse response analysis in linear multivariate models. *Economics Letters*, 58(1), 17-29.

Software versions and deterministic build inputs are pinned in [`pyproject.toml`](pyproject.toml), [`uv.lock`](uv.lock), and generated [`research/build_provenance.json`](research/build_provenance.json).
