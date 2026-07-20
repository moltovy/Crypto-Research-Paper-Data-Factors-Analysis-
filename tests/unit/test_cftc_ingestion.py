from __future__ import annotations

import pandas as pd
from tools.data_collection.fetch_cftc_positioning import _normalize


def test_cftc_normalization_keeps_contracts_separate_and_sets_availability() -> None:
    raw = pd.DataFrame(
        {
            "Report_Date_as_YYYY-MM-DD": ["2025-01-07", "2025-01-07", "2025-01-07"],
            "CFTC_Contract_Market_Code": ["133741", "133742", "999999"],
            "Open_Interest_All": [100, 50, 10],
            "Dealer_Positions_Long_All": [20, 5, 1],
            "Dealer_Positions_Short_All": [30, 2, 1],
            "Asset_Mgr_Positions_Long_All": [40, 10, 1],
            "Asset_Mgr_Positions_Short_All": [10, 8, 1],
            "Lev_Money_Positions_Long_All": [15, 4, 1],
            "Lev_Money_Positions_Short_All": [25, 6, 1],
        }
    )

    result = _normalize(raw)

    assert result["contract_code"].tolist() == ["133741", "133742"]
    assert result["available_date"].dt.strftime("%Y-%m-%d").unique().tolist() == ["2025-01-10"]
    assert result.loc[result["contract_code"].eq("133741"), "dealer_net_share_oi"].iat[0] == -0.1
    assert result["is_micro"].tolist() == [False, True]
