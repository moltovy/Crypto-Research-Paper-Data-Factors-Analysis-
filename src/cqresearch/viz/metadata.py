"""Canonical metadata sidecars for public research figures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import yaml

from cqresearch.core.artifacts import write_json

FIGURE_METADATA_FIELDS = {
    "figure_id",
    "research_question",
    "sample",
    "date_range",
    "method",
    "units",
    "uncertainty",
    "limitation",
    "data_cutoff",
    "source_tables",
    "source_csv",
    "plot_key_column",
    "plot_keys_unique",
    "rows",
    "png",
    "svg",
    "visual_qa_status",
}


def write_figure_metadata(
    path: Path,
    source: pd.DataFrame,
    figure_id: str,
    source_tables: str | list[str],
) -> Path:
    """Write a contract-complete figure sidecar from the canonical figure registry."""

    root = _project_root(path)
    registry = _figure_registry(root)
    if figure_id not in registry:
        raise ValueError(f"figure {figure_id!r} is absent from config/public_figures.yml")
    spec = registry[figure_id]
    missing = [
        field
        for field in [
            "research_question",
            "sample",
            "date_range",
            "method",
            "units",
            "uncertainty",
            "caveat",
            "visual_qa_status",
        ]
        if not str(spec.get(field, "")).strip()
    ]
    if missing:
        raise ValueError(f"figure {figure_id!r} has incomplete registry metadata: {missing}")
    if "plot_key" not in source:
        raise ValueError(f"figure {figure_id!r} source is missing plot_key")
    if source["plot_key"].astype(str).duplicated().any():
        raise ValueError(f"figure {figure_id!r} source has duplicate plot keys")
    tables = _source_tables(source_tables)
    payload: dict[str, Any] = {
        "figure_id": figure_id,
        "research_question": spec["research_question"],
        "sample": spec["sample"],
        "date_range": spec["date_range"],
        "method": spec["method"],
        "units": spec["units"],
        "uncertainty": spec["uncertainty"],
        "limitation": spec["caveat"],
        "data_cutoff": "2026-06-30",
        "source_tables": tables,
        "source_csv": path.with_suffix(".source.csv").name,
        "plot_key_column": "plot_key",
        "plot_keys_unique": True,
        "rows": int(len(source)),
        "png": path.name,
        "svg": path.with_suffix(".svg").name,
        "visual_qa_status": spec["visual_qa_status"],
    }
    if set(payload) != FIGURE_METADATA_FIELDS:
        raise AssertionError("figure metadata schema drifted")
    return write_json(path.with_suffix(".metadata.json"), payload)


def _figure_registry(root: Path) -> dict[str, dict[str, Any]]:
    payload = yaml.safe_load((root / "config" / "public_figures.yml").read_text(encoding="utf-8"))
    return {str(row["figure_id"]): row for row in payload.get("figures", [])}


def _project_root(path: Path) -> Path:
    for parent in path.resolve().parents:
        if (parent / "config" / "public_figures.yml").exists():
            return parent
    raise ValueError(f"cannot locate project root for {path}")


def _source_tables(value: str | list[str]) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [item.strip() for item in value.replace(",", ";").split(";") if item.strip()]
