from __future__ import annotations

import numpy as np
import pandas as pd

from cqresearch.modeling.fevd_sensitivity import (
    run_fevd_order_sensitivity,
    summarize_fevd_sensitivity,
)
from cqresearch.modeling.var_fevd import fit_var_fevd


def test_fevd_order_sensitivity_records_successes_and_failures() -> None:
    rng = np.random.default_rng(7)
    idx = pd.date_range("2024-01-01", periods=140)
    df = pd.DataFrame(
        rng.normal(scale=0.01, size=(len(idx), 4)),
        index=idx,
        columns=["btc_ret", "eth_ret", "spy_ret", "VIXCLS_d1"],
    )

    out = run_fevd_order_sensitivity(
        df,
        {
            "crypto_first": ["btc_ret", "eth_ret", "spy_ret", "VIXCLS_d1"],
            "too_small": ["btc_ret", "eth_ret"],
        },
        horizon=3,
        maxlags=2,
    )
    summary = summarize_fevd_sensitivity(out)

    assert "fewer_than_3_available_columns" in set(out["error"].dropna())
    assert not summary.empty
    assert {"from", "to", "range"}.issubset(summary.columns)


def test_generalized_fevd_is_row_normalized_and_order_invariant() -> None:
    rng = np.random.default_rng(19)
    frame = pd.DataFrame(rng.normal(size=(400, 4)), columns=list("ABCD"))
    first = fit_var_fevd(frame, horizon=5, maxlags=2)
    reversed_result = fit_var_fevd(frame[list(reversed(frame.columns))], horizon=5, maxlags=2)
    aligned = reversed_result.table.reindex(index=frame.columns, columns=frame.columns)
    assert first.row_sum_max_error < 1e-10
    assert np.allclose(first.table, aligned, atol=1e-8)
    assert first.method == "Pesaran-Shin generalized FEVD"
