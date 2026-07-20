from __future__ import annotations

import pandas as pd


def test_absolute_return_correlation_is_not_absolute_signed_correlation() -> None:
    returns = pd.Series([-3.0, -1.0, 1.0, 3.0])
    flow = pd.Series([-3.0, -1.0, 1.0, 3.0])
    signed = returns.corr(flow)
    volatility = returns.abs().corr(flow)
    assert signed == 1.0
    assert pd.isna(volatility) or volatility != abs(signed)
