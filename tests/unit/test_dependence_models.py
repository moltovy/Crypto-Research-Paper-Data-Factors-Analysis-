from __future__ import annotations

import numpy as np
import pandas as pd

from cqresearch.modeling.dependence import leave_one_out_factor, tail_dependence


def test_leave_one_out_factor_never_contains_target() -> None:
    rng = np.random.default_rng(4)
    common = rng.normal(size=300)
    frame = pd.DataFrame(
        {asset: common + rng.normal(scale=0.4, size=300) for asset in ["A", "B", "C", "D"]},
        index=pd.date_range("2020-01-01", periods=300),
    )
    overview, decomposition = leave_one_out_factor(frame)
    assert overview.loc[0, "variance_share"] > 0.5
    assert not decomposition["self_included"].any()
    for row in decomposition.itertuples(index=False):
        assert row.asset not in row.factor_assets.split("|")


def test_independent_tail_excess_is_near_zero() -> None:
    rng = np.random.default_rng(8)
    frame = pd.DataFrame(
        rng.normal(size=(2000, 3)),
        columns=["A", "B", "C"],
        index=pd.date_range("2020-01-01", periods=2000),
    )
    result = tail_dependence(
        frame, quantiles=(0.05,), reps=100, block_length=10, sensitivity_blocks=()
    )
    assert result["excess_probability"].abs().max() < 0.02
