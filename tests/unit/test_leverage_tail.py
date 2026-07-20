from __future__ import annotations

import numpy as np
import pandas as pd

from cqresearch.modeling.leverage_tail import (
    leverage_horizon_sensitivity,
    leverage_tail_model,
    systemic_tail_associations,
)


def test_leverage_tail_curve_uses_lagged_states_and_observed_support() -> None:
    rng = np.random.default_rng(31)
    index = pd.date_range("2020-01-01", periods=900)
    leverage = pd.Series(rng.uniform(size=len(index)), index=index)
    returns = pd.Series(rng.normal(scale=0.02, size=len(index)), index=index)
    returns.iloc[1:] -= leverage.iloc[:-1].to_numpy() * 0.01
    daily = pd.DataFrame(
        {
            "btc_ret": returns,
            "btc_leverage_ratio_percentile_lag1": leverage,
            "btc_realized_vol_30d": returns.rolling(30, min_periods=20).std(),
        }
    )
    curve, diagnostics = leverage_tail_model(daily)
    assert curve["leverage"].between(0, 1).all()
    assert curve["predicted_tail_probability"].between(0, 1).all()
    assert diagnostics.loc[0, "converged"]
    assert diagnostics.loc[0, "brier_score"] >= 0

    horizon = leverage_horizon_sensitivity(daily)
    assert len(horizon) == 5
    assert horizon["tail_probability"].between(0, 1).all()


def test_systemic_tail_table_reports_delta_covar() -> None:
    rng = np.random.default_rng(83)
    returns = pd.DataFrame(
        rng.normal(size=(800, 4)),
        columns=["BTC", "ETH", "XRP", "ADA"],
        index=pd.date_range("2021-01-01", periods=800),
    )
    result = systemic_tail_associations(returns, reps=100)
    assert {"conditional_var_5pct", "unconditional_var_5pct", "delta_covar_5pct"}.issubset(result)
    assert np.allclose(
        result["delta_covar_5pct"],
        result["conditional_var_5pct"] - result["unconditional_var_5pct"],
    )
