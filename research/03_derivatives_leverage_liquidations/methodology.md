# Methodology

Tail-state model: fit a spline logistic model using lagged OI-to-market-cap, funding, liquidation, and volatility states.

Tail severity: estimate 5% and 10% quantile associations, expected shortfall, CoVaR, delta-CoVaR, and MES.

Connectedness: estimate rolling generalized FEVD on S2 using 252 observations, BIC lag at most five, and horizon 10.
