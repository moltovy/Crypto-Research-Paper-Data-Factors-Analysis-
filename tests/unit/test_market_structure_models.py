from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from cqresearch.modeling.market_structure import chain_panel_model, pit_market_structure


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


def test_chain_panel_reads_external_raw_root(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    external = tmp_path / "provider-data"
    artemis = external / "raw" / "artemis"
    artemis.mkdir(parents=True)
    dates = pd.date_range("2022-01-31", periods=40, freq="ME")
    chains = ["Ethereum", "Solana", "Avalanche C-Chain", "Near"]
    rng = np.random.default_rng(20260713)
    for filename, scale in [
        ("Chains - Market Cap.csv", 1_000_000.0),
        ("Chains - Fees.csv", 10_000.0),
        ("Chains - Revenue.csv", 5_000.0),
    ]:
        frame = pd.DataFrame({"date": dates})
        for index, chain in enumerate(chains, start=1):
            trend = np.arange(len(dates), dtype=float) * index
            frame[chain] = (
                scale * index + scale * 0.01 * trend + rng.uniform(1.0, scale * 0.02, len(dates))
            )
        frame.to_csv(artemis / filename, index=False)
    monkeypatch.setenv("CMD_DATA_ROOT", str(external))
    estimates, coverage = chain_panel_model(tmp_path / "clean-worktree")
    assert len(estimates) == 2
    assert estimates["entities"].eq(4).all()
    assert coverage["gate_status"].eq("pass").all()
