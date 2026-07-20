"""Explicit data, calendar, sample, and result-table contracts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

DATA_CUTOFF = pd.Timestamp("2026-06-30")


@dataclass(frozen=True)
class SourceFamilyContract:
    source_family: str
    observation_column: str
    alternate_observation_columns: tuple[str, ...]
    period_column: str | None
    availability_rule: str
    native_calendar: str
    timezone: str

    def observation_field(self, columns: pd.Index | list[str]) -> str | None:
        available = {str(column) for column in columns}
        for candidate in (self.observation_column, *self.alternate_observation_columns):
            if candidate in available:
                return candidate
        return None


@dataclass(frozen=True)
class SampleDefinition:
    sample_id: str
    name: str
    frequency: str
    start_rule: str
    end_rule: str
    inclusion_rule: str
    exclusion_rule: str


def load_source_contracts(root: Path) -> dict[str, SourceFamilyContract]:
    payload = yaml.safe_load((root / "config" / "data_contracts.yml").read_text(encoding="utf-8"))
    rows = payload.get("source_families", {})
    return {
        key: SourceFamilyContract(
            source_family=key,
            observation_column=str(value["observation_column"]),
            alternate_observation_columns=tuple(value.get("alternate_observation_columns", [])),
            period_column=value.get("period_column"),
            availability_rule=str(value["availability_rule"]),
            native_calendar=str(value["native_calendar"]),
            timezone=str(value["timezone"]),
        )
        for key, value in rows.items()
    }


def load_sample_definitions(root: Path) -> list[SampleDefinition]:
    payload = yaml.safe_load(
        (root / "config" / "sample_definitions.yml").read_text(encoding="utf-8")
    )
    return [SampleDefinition(**row) for row in payload.get("samples", [])]


def require_observation_index(
    frame: pd.DataFrame, contract: SourceFamilyContract
) -> pd.DatetimeIndex:
    field = contract.observation_field(frame.columns)
    if field is None:
        expected = ", ".join((contract.observation_column, *contract.alternate_observation_columns))
        raise ValueError(
            f"{contract.source_family}: missing declared observation field: {expected}"
        )
    parsed = pd.to_datetime(frame[field], errors="coerce", utc=True)
    if parsed.isna().all():
        raise ValueError(
            f"{contract.source_family}: observation field {field!r} has no valid dates"
        )
    return pd.DatetimeIndex(parsed.dt.tz_convert("UTC").dt.tz_localize(None)).normalize()


def native_log_return(
    levels: pd.Series, expected_index: pd.DatetimeIndex | None = None
) -> pd.Series:
    """Compute one-period log returns on a native calendar before cross-calendar joins."""

    import numpy as np

    clean = pd.to_numeric(levels, errors="coerce").where(lambda value: value > 0).sort_index()
    if expected_index is not None:
        clean = clean.reindex(pd.DatetimeIndex(expected_index))
    result = np.log(clean).diff()
    result.name = levels.name
    return result


def result_sample_summary(frame: pd.DataFrame) -> str:
    """Describe the observation sample represented by a result table."""

    if frame.empty:
        return "no rows"
    starts = _date_values(frame, ("sample_start", "first_date", "first_valid_date", "date"))
    ends = _date_values(frame, ("sample_end", "last_date", "last_valid_date", "date"))
    n_values = pd.to_numeric(frame.get("n", pd.Series(dtype=float)), errors="coerce").dropna()
    parts: list[str] = []
    if not starts.empty and not ends.empty:
        parts.append(f"{starts.min().date()} to {ends.max().date()}")
    elif not ends.empty:
        parts.append(f"through {ends.max().date()}")
    if not n_values.empty:
        n_min, n_max = int(n_values.min()), int(n_values.max())
        parts.append(f"n={n_min}" if n_min == n_max else f"n={n_min}-{n_max}")
    else:
        parts.append(f"result rows={len(frame)}")
    return ", ".join(parts)


def assert_unique_plot_keys(frame: pd.DataFrame, keys: list[str]) -> None:
    missing = [key for key in keys if key not in frame]
    if missing:
        raise ValueError(f"missing plot-key columns: {missing}")
    duplicates = frame.duplicated(keys, keep=False)
    if duplicates.any():
        values = frame.loc[duplicates, keys].drop_duplicates().to_dict("records")
        raise ValueError(f"duplicate plot keys for {keys}: {values[:5]}")


def logical_series_registry(root: Path) -> pd.DataFrame:
    payload = yaml.safe_load((root / "config" / "data_contracts.yml").read_text(encoding="utf-8"))
    frame = pd.DataFrame(payload.get("logical_series", []))
    required = [
        "series_id",
        "provider",
        "raw_field",
        "unit",
        "frequency",
        "observation_time",
        "availability_time",
        "valid_start",
        "missing_policy",
    ]
    return frame.reindex(columns=required).sort_values("series_id").reset_index(drop=True)


def sample_registry(root: Path) -> pd.DataFrame:
    return pd.DataFrame([definition.__dict__ for definition in load_sample_definitions(root)])


def contract_record(contract: SourceFamilyContract) -> dict[str, Any]:
    return {
        "source_family": contract.source_family,
        "observation_column": contract.observation_column,
        "alternate_observation_columns": "|".join(contract.alternate_observation_columns),
        "period_column": contract.period_column or "",
        "availability_rule": contract.availability_rule,
        "native_calendar": contract.native_calendar,
        "timezone": contract.timezone,
    }


def _date_values(frame: pd.DataFrame, candidates: tuple[str, ...]) -> pd.Series:
    for column in candidates:
        if column in frame:
            values = pd.to_datetime(frame[column], errors="coerce").dropna()
            if not values.empty:
                return values
    return pd.Series(dtype="datetime64[ns]")
