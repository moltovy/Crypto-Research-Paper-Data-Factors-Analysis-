"""Portable raw-object and physical-column inventories."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import zipfile
from functools import lru_cache
from pathlib import Path
from typing import Any

import pandas as pd
from config.paths import PROJECT_ROOT

from cqresearch.data.contracts import load_source_contracts, resolve_raw_data_root

PROVIDER_DISPLAY_NAMES = {
    "cryptoquant": "CryptoQuant",
    "artemis": "Artemis",
    "tradingview": "Tradingview",
    "defillama": "DefiLlama",
    "farside": "Farside ETF Data",
    "fred": "FRED",
    "alternativeme": "AlternativeMe",
    "market_structure": "MarketStructure",
    "binance": "Binance Vision",
    "cftc": "CFTC",
}

BINANCE_KLINE_COLUMNS = (
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "quote_asset_volume",
    "number_of_trades",
    "taker_buy_base_asset_volume",
    "taker_buy_quote_asset_volume",
    "ignore",
)

RAW_OBJECT_COLUMNS = (
    "raw_object_id",
    "relpath",
    "source_group",
    "size_bytes",
    "sha256",
    "suffix",
    "rows",
    "columns",
    "start_date",
    "end_date",
    "lineage_observed_at",
    "lineage_note",
    "status",
)

PHYSICAL_COLUMN_COLUMNS = (
    "physical_column_id",
    "raw_object_id",
    "provider",
    "relpath",
    "column_name",
    "observed_dtype",
    "non_null_count",
    "null_count",
    "profile_status",
)


def source_file_inventory(root: Path = PROJECT_ROOT) -> pd.DataFrame:
    """Return one portable, content-addressed row per local raw object."""

    objects, _ = _inventory_bundle(str(root.resolve()))
    return objects.copy()


def physical_column_inventory(root: Path = PROJECT_ROOT) -> pd.DataFrame:
    """Return the observed physical fields for readable raw objects."""

    _, columns = _inventory_bundle(str(root.resolve()))
    return columns.copy()


@lru_cache(maxsize=4)
def _inventory_bundle(root_text: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    root = Path(root_text)
    raw_root = resolve_raw_data_root(root)
    contracts = load_source_contracts(root)
    object_rows: list[dict[str, Any]] = []
    column_rows: list[dict[str, Any]] = []
    if not raw_root.exists():
        return (
            pd.DataFrame(columns=RAW_OBJECT_COLUMNS),
            pd.DataFrame(columns=PHYSICAL_COLUMN_COLUMNS),
        )

    for path in sorted(raw_root.rglob("*")):
        if not path.is_file():
            continue
        data_rel = path.relative_to(raw_root).as_posix()
        if data_rel in {"MASTER_DATA.csv", "MASTER_DATA.md", "MASTER_DATA.txt"}:
            continue
        provider_key = path.relative_to(raw_root).parts[0].lower()
        provider = PROVIDER_DISPLAY_NAMES.get(provider_key, provider_key)
        relpath = f"data_local/raw/{data_rel}"
        digest = _sha256(path)
        raw_object_id = _stable_id("raw", relpath, digest)
        profile = _profile_object(path, provider_key, contracts.get(provider_key))
        object_rows.append(
            {
                "raw_object_id": raw_object_id,
                "relpath": relpath,
                "source_group": provider,
                "size_bytes": path.stat().st_size,
                "sha256": digest,
                "suffix": path.suffix.lower(),
                "rows": profile["rows"],
                "columns": len(profile["fields"]),
                "start_date": profile["start_date"],
                "end_date": profile["end_date"],
                "lineage_observed_at": "2026-07-19",
                "lineage_note": (
                    "first repository inventory observation; provider retrieval time is "
                    "available only where a source manifest records it"
                ),
                "status": profile["status"],
            }
        )
        for field in profile["fields"]:
            name = str(field["column_name"])
            column_rows.append(
                {
                    "physical_column_id": _stable_id("col", raw_object_id, name),
                    "raw_object_id": raw_object_id,
                    "provider": provider,
                    "relpath": relpath,
                    **field,
                }
            )

    objects = pd.DataFrame(object_rows, columns=RAW_OBJECT_COLUMNS)
    columns = pd.DataFrame(column_rows, columns=PHYSICAL_COLUMN_COLUMNS)
    return objects, columns


def _profile_object(path: Path, provider_key: str, contract: Any) -> dict[str, Any]:
    suffix = path.suffix.lower()
    try:
        if suffix == ".csv":
            frame = pd.read_csv(path, low_memory=False)
            return _frame_profile(frame, contract)
        if suffix == ".json":
            return _json_profile(path)
        if suffix == ".zip":
            return _zip_profile(path, provider_key, contract)
        return _empty_profile("indexed:non_tabular")
    except Exception as exc:
        return _empty_profile(f"read_error:{type(exc).__name__}")


def _frame_profile(frame: pd.DataFrame, contract: Any) -> dict[str, Any]:
    fields = []
    for column in frame.columns:
        values = frame[column]
        fields.append(
            {
                "column_name": str(column),
                "observed_dtype": str(values.dtype),
                "non_null_count": int(values.notna().sum()),
                "null_count": int(values.isna().sum()),
                "profile_status": "observed",
            }
        )
    start, end, status = _date_bounds(frame, contract)
    return {
        "rows": int(len(frame)),
        "fields": fields,
        "start_date": start,
        "end_date": end,
        "status": status,
    }


def _json_profile(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload if isinstance(payload, list) else [payload]
    records = [item for item in records if isinstance(item, dict)]
    frame = pd.DataFrame(records)
    result = _frame_profile(frame, None)
    result["status"] = "indexed:json_fields"
    return result


def _zip_profile(path: Path, provider_key: str, contract: Any) -> dict[str, Any]:
    with zipfile.ZipFile(path) as archive:
        members = [name for name in archive.namelist() if not name.endswith("/")]
        if not members:
            return _empty_profile("indexed:empty_archive")
        member = members[0]
        with archive.open(member) as binary:
            text_stream = io.TextIOWrapper(binary, encoding="utf-8-sig", errors="replace")
            if provider_key == "binance":
                archive_records = [
                    row for row in csv.reader(text_stream) if row and row[0].isdigit()
                ]
                rows = len(archive_records)
                non_null = [
                    sum(
                        index < len(row) and str(row[index]).strip() != ""
                        for row in archive_records
                    )
                    for index in range(len(BINANCE_KLINE_COLUMNS))
                ]
                fields = [
                    {
                        "column_name": name,
                        "observed_dtype": (
                            "int64_epoch"
                            if name in {"open_time", "close_time"}
                            else "int64"
                            if name == "number_of_trades"
                            else "float64"
                        ),
                        "non_null_count": non_null[index],
                        "null_count": rows - non_null[index],
                        "profile_status": "declared_headerless_schema",
                    }
                    for index, name in enumerate(BINANCE_KLINE_COLUMNS)
                ]
                timestamps = [int(row[0]) for row in archive_records]
                unit = "us" if timestamps and max(timestamps) >= 100_000_000_000_000 else "ms"
                dates = pd.to_datetime(timestamps, unit=unit, errors="coerce", utc=True)
                return {
                    "rows": rows,
                    "fields": fields,
                    "start_date": dates.min().date().isoformat() if len(dates) else "",
                    "end_date": dates.max().date().isoformat() if len(dates) else "",
                    "status": "indexed:headerless_zip",
                }
            dict_reader = csv.DictReader(text_stream)
            dict_records = list(dict_reader)
            frame = pd.DataFrame(dict_records, columns=dict_reader.fieldnames or [])
            result = _frame_profile(frame, contract)
            result["status"] = "indexed:zip_csv"
            return result


def _date_bounds(frame: pd.DataFrame, contract: Any) -> tuple[str, str, str]:
    if contract is None:
        return "", "", "indexed"
    observation_field = contract.observation_field(frame.columns)
    if observation_field is None:
        return "", "", "indexed:no_declared_observation_column"
    dates = pd.to_datetime(frame[observation_field], errors="coerce", utc=True).dropna()
    if dates.empty:
        return "", "", "indexed:no_valid_observation_date"
    return dates.min().date().isoformat(), dates.max().date().isoformat(), "indexed"


def _empty_profile(status: str) -> dict[str, Any]:
    return {"rows": "", "fields": [], "start_date": "", "end_date": "", "status": status}


def _sha256(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def _stable_id(prefix: str, *parts: str) -> str:
    payload = "|".join(parts).encode("utf-8")
    return f"{prefix}_{hashlib.sha256(payload).hexdigest()[:16]}"
