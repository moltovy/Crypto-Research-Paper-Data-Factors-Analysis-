from __future__ import annotations

import numpy as np
import pandas as pd

from cqresearch.modeling.etf_plumbing import distributed_lag_models, nonlinear_flow_sensitivity


def test_distributed_lag_recovers_known_lag_and_simultaneous_bands() -> None:
    rng = np.random.default_rng(15)
    index = pd.bdate_range("2022-01-03", periods=500)
    flow = pd.Series(rng.normal(scale=0.0001, size=len(index)), index=index)
    returns = 0.8 * flow.shift(1) + rng.normal(scale=0.00005, size=len(index))
    frame = pd.DataFrame(
        {
            "btc_etf_net_flow_usd": flow * 1e12,
            "btc_mcap_lag1": 1e12,
            "btc_ret": returns,
            "eth_etf_net_flow_usd": flow * 4e11,
            "eth_mcap_lag1": 4e11,
            "eth_ret": returns,
        },
        index=index,
    )
    coefficients, cumulative, timing = distributed_lag_models(frame, reps=100)
    btc = coefficients[(coefficients["asset"].eq("BTC")) & coefficients["response"].eq("return")]
    assert btc.loc[btc["lag_sessions"].eq(1), "coefficient_per_flow_bps"].iloc[0] > 0
    assert {"simultaneous_ci_low", "simultaneous_ci_high"}.issubset(coefficients)
    assert not cumulative.empty
    assert not timing.empty
    assert {
        "design_condition_number",
        "durbin_watson",
        "jarque_bera_pvalue",
        "breusch_pagan_pvalue",
    }.issubset(coefficients)

    nonlinear = nonlinear_flow_sensitivity(frame)
    assert set(nonlinear["term"]) == {
        "inflow_bps",
        "outflow_bps",
        "flow_x_high_volatility",
    }
    assert nonlinear["qvalue_bh"].between(0, 1).all()
