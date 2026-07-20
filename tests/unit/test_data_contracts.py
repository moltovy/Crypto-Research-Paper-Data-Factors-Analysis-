from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from cqresearch.data.contracts import (
    SourceFamilyContract,
    assert_unique_plot_keys,
    load_sample_definitions,
    load_source_contracts,
    native_log_return,
    result_sample_summary,
)

ROOT = Path(__file__).resolve().parents[2]


def test_every_local_source_family_has_an_explicit_contract() -> None:
    contracts = load_source_contracts(ROOT)
    local = {path.name for path in (ROOT / "data_local" / "raw").iterdir() if path.is_dir()}
    assert local <= set(contracts)


def test_observation_contract_rejects_undeclared_dates() -> None:
    contract = SourceFamilyContract("demo", "date", (), None, "after close", "crypto_7", "UTC")
    assert contract.observation_field(["timestamp", "value"]) is None


def test_native_return_does_not_bridge_missing_session() -> None:
    index = pd.date_range("2024-01-02", periods=3, freq="D")
    levels = pd.Series([100.0, np.nan, 110.0], index=index, name="close")
    returns = native_log_return(levels, index)
    assert returns.isna().all()


def test_result_sample_uses_estimation_n_not_result_rows() -> None:
    table = pd.DataFrame(
        {
            "sample_start": ["2020-01-01", "2020-01-01"],
            "sample_end": ["2024-12-31", "2024-12-31"],
            "n": [900, 875],
        }
    )
    assert result_sample_summary(table) == "2020-01-01 to 2024-12-31, n=875-900"


def test_plot_keys_must_be_unique() -> None:
    frame = pd.DataFrame({"asset": ["BTC", "BTC"], "regime": ["era", "era"]})
    with pytest.raises(ValueError, match="duplicate plot keys"):
        assert_unique_plot_keys(frame, ["asset", "regime"])


def test_samples_s1_through_s5_are_locked() -> None:
    definitions = load_sample_definitions(ROOT)
    assert [definition.sample_id for definition in definitions] == ["S1", "S2", "S3", "S4", "S5"]
    assert "HYPE" in definitions[1].exclusion_rule
