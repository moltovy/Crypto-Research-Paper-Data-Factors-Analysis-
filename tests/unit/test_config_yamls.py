"""Assert that the YAML configs parse and contain the fields every agent depends on."""

from __future__ import annotations

import yaml
from config.paths import (
    CALENDARS_YML,
    CHAIN_TAXONOMY_YML,
    CONFIG_DIR,
    CURATION_SNAPSHOTS_YML,
    EVENTS_YML,
    FACTOR_BLOCKS_YML,
)


def _load(p):
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_calendars_yml_has_required_calendars() -> None:
    data = _load(CALENDARS_YML)
    assert "calendar_daily" in data
    assert data["calendar_daily"]["frequency"] == "D"


def test_factor_blocks_declares_five_blocks() -> None:
    data = _load(FACTOR_BLOCKS_YML)
    for block in ("macro", "institutional", "liquidity", "btc_native", "eth_native"):
        assert block in data, f"factor_blocks.yml missing block: {block}"
        assert "files" in data[block], f"{block} has no files list"


def test_events_yml_has_primary_breaks() -> None:
    data = _load(EVENTS_YML)
    ids = {e["id"] for e in data["primary_breaks"]}
    assert "btc_spot_etf_launch" in ids
    assert "eth_spot_etf_launch" in ids
    assert "bitcoin_halving_2024" in ids
    events = [*data["primary_breaks"], *data["secondary_candidates"]]
    assert all(event["source_url"].startswith("https://") for event in events)
    assert all(str(event["source_retrieved_at"]) == "2026-07-19" for event in events)


def test_every_feature_has_a_declared_unit() -> None:
    registry = _load(CONFIG_DIR / "feature_registry.yml")["features"]
    units = _load(CONFIG_DIR / "feature_units.yml")["units"]
    assert {item["feature_id"] for item in registry} == set(units)
    assert all(str(unit).strip() for unit in units.values())


def test_chain_taxonomy_blocks_summing_l1_and_l2() -> None:
    data = _load(CHAIN_TAXONOMY_YML)
    assert "ethereum_ecosystem" in data
    assert "l1" in data["ethereum_ecosystem"]
    assert "canonical_l2" in data["ethereum_ecosystem"]


def test_curation_snapshots_is_parsable() -> None:
    data = _load(CURATION_SNAPSHOTS_YML)
    assert "validate" in data


def test_research_modules_yml_declares_retained_modules() -> None:
    data = _load(CONFIG_DIR / "research_modules.yml")
    modules = data["modules"]
    assert [item["module_id"] for item in modules] == [
        "00_data_measurement_foundation",
        "01_cross_asset_dependence_regimes",
        "02_macro_tradfi_integration",
        "03_derivatives_leverage_liquidations",
        "04_etf_institutional_flows",
        "05_stablecoin_defi_liquidity",
        "07_chain_fundamentals_sector_dynamics",
        "09_event_stress_cross_module_synthesis",
    ]
