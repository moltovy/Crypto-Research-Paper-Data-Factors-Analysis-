from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import yaml

from cqresearch.data.inventory import physical_column_inventory, source_file_inventory
from cqresearch.research.registries import _estimand_registry, _feature_registry
from cqresearch.research.samples import _s3_membership, _s4_membership
from cqresearch.viz.metadata import FIGURE_METADATA_FIELDS

ROOT = Path(__file__).resolve().parents[2]


def test_raw_objects_and_physical_columns_have_stable_unique_ids() -> None:
    objects = source_file_inventory(ROOT)
    columns = physical_column_inventory(ROOT)
    assert len(objects) == 1518
    assert objects["raw_object_id"].is_unique
    assert objects["sha256"].str.fullmatch(r"[0-9a-f]{64}").all()
    assert columns["physical_column_id"].is_unique
    assert columns["raw_object_id"].isin(objects["raw_object_id"]).all()


def test_sample_taxonomy_and_pit_dimensions_are_enforced() -> None:
    broad = pd.DataFrame(_s3_membership(ROOT))
    included = set(broad.loc[broad["included"], "asset"])
    assert not included.intersection({"CBBTC", "PAXG", "XAUT", "SUSDS", "USDT0", "BSC-USD"})

    pit = pd.DataFrame(_s4_membership(ROOT))
    assert len(pit) == 7700
    assert pit["period"].nunique() == 77
    assert pit.groupby("period").size().eq(100).all()


def test_feature_and_estimand_registries_expose_required_semantics() -> None:
    features = _feature_registry(ROOT)
    assert {
        "availability_rule",
        "timezone",
        "native_calendar",
        "sample_eligibility",
        "evidence_class",
    }.issubset(features.columns)
    assert (
        features[
            [
                "availability_rule",
                "timezone",
                "native_calendar",
                "sample_eligibility",
                "evidence_class",
            ]
        ]
        .notna()
        .all()
        .all()
    )

    estimands = _estimand_registry()
    assert set(estimands["research_question"]) == {"RQ1", "RQ2", "RQ3", "RQ4"}
    assert (
        estimands[
            [
                "question",
                "inputs",
                "estimand",
                "primary_specification",
                "assumptions",
                "diagnostics",
                "robustness",
                "decision_rule",
                "tables",
                "figures",
            ]
        ]
        .notna()
        .all()
        .all()
    )


def test_every_figure_registry_row_supports_complete_metadata() -> None:
    registry = yaml.safe_load((ROOT / "config" / "public_figures.yml").read_text(encoding="utf-8"))
    for row in registry["figures"]:
        metadata_path = (ROOT / row["filename"]).with_suffix(".metadata.json")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        assert set(metadata) == FIGURE_METADATA_FIELDS
        assert metadata["figure_id"] == row["figure_id"]
        assert metadata["plot_key_column"] == "plot_key"
        assert metadata["plot_keys_unique"] is True
