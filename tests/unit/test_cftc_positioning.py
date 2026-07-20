from __future__ import annotations

import numpy as np
import pandas as pd

from cqresearch.modeling.etf_plumbing import cftc_positioning_associations


def test_cftc_associations_exclude_micro_contracts() -> None:
    report_dates = pd.date_range("2022-01-04", periods=80, freq="W-TUE")
    rows = []
    for micro, name in [(False, "CME Bitcoin"), (True, "CME Micro Bitcoin")]:
        for index, date in enumerate(report_dates):
            rows.append(
                {
                    "report_date": date,
                    "available_date": date + pd.Timedelta(days=3),
                    "asset": "BTC",
                    "contract_name": name,
                    "is_micro": micro,
                    "open_interest": 1000 + index,
                    "dealer_net_share_oi": index / 1000,
                    "asset_manager_net_share_oi": index / 800,
                    "leveraged_money_net_share_oi": -index / 900,
                }
            )
    daily_index = pd.date_range("2021-12-20", report_dates.max(), freq="D")
    daily = pd.DataFrame(
        {
            "btc_ret": np.sin(np.arange(len(daily_index)) / 13) / 100,
            "eth_ret": np.cos(np.arange(len(daily_index)) / 11) / 100,
        },
        index=daily_index,
    )

    associations, eras, points = cftc_positioning_associations(pd.DataFrame(rows), daily)

    assert set(associations["contract_name"]) == {"CME Bitcoin"}
    assert set(points["contract_name"]) == {"CME Bitcoin"}
    assert set(eras["era"]) == {"pre_us_spot_etf"}
    assert associations["n"].min() >= 70
