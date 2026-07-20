from __future__ import annotations

import numpy as np
import pandas as pd

from cqresearch.modeling.market_structure import pit_market_structure


def test_pit_hhi_decomposition_reconciles_exactly() -> None:
    rows = []
    for date, values in [
        ("2020-01-31", {"A": 60, "B": 40}),
        ("2020-02-29", {"A": 50, "C": 50}),
    ]:
        for rank, (asset, market_cap) in enumerate(values.items(), start=1):
            rows.append(
                {
                    "snapshot_date": date,
                    "rank_full_market": rank,
                    "asset_key": asset,
                    "market_cap_usd": market_cap,
                    "is_partial_month": False,
                }
            )
    source = pd.DataFrame(rows)
    concentration, turnover, decomposition = pit_market_structure(source)
    assert len(concentration) == 2
    assert turnover.loc[0, "entries"] == 1
    assert turnover.loc[0, "exits"] == 1
    assert np.isclose(decomposition.loc[0, "residual"], 0.0, atol=1e-12)
    shuffled = pit_market_structure(source.sample(frac=1, random_state=7))[2]
    pd.testing.assert_frame_equal(decomposition, shuffled)
