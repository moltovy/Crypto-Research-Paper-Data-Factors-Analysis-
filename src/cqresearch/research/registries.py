"""Generate the canonical repository-level research registries."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yaml

from cqresearch.core.artifacts import write_csv
from cqresearch.data.contracts import (
    contract_record,
    load_source_contracts,
    logical_series_registry,
    sample_registry,
)
from cqresearch.pipelines.final_research import source_file_inventory


def build_foundation_registries(root: Path) -> list[Path]:
    research = root / "research"
    contracts = pd.DataFrame(
        contract_record(item) for item in load_source_contracts(root).values()
    ).sort_values("source_family")
    raw_objects = source_file_inventory(root).rename(columns={"source_group": "provider"})
    features = _feature_registry(root)
    estimands = _estimand_registry()
    decisions = _source_decision_registry(root)
    acceptance = _acceptance_registry(root)
    return [
        write_csv(research / "source_contracts.csv", contracts),
        write_csv(research / "raw_objects.csv", raw_objects),
        write_csv(research / "logical_series.csv", logical_series_registry(root)),
        write_csv(research / "feature_registry.csv", features),
        write_csv(research / "sample_manifest.csv", sample_registry(root)),
        write_csv(research / "estimand_registry.csv", estimands),
        write_csv(research / "source_decisions.csv", decisions),
        write_csv(research / "acceptance_ledger.csv", acceptance),
    ]


def _estimand_registry() -> pd.DataFrame:
    rows = [
        {
            "research_question": "RQ1",
            "estimand_id": "dependence_and_integration",
            "samples": "S1|S2|S3",
            "outcomes": "returns|tail indicators",
            "exposures": "leave-one-out common factor|TradFi returns and changes",
            "method": "PCA|HAC rolling exposure|tail co-exceedance|break tests",
            "uncertainty": "HAC and moving-block bootstrap",
            "claim_boundary": "descriptive dependence and conditional association",
        },
        {
            "research_question": "RQ2",
            "estimand_id": "institutional_market_plumbing",
            "samples": "S5",
            "outcomes": "crypto return|absolute return|realized volatility",
            "exposures": "ETF flow divided by lagged market capitalization",
            "method": "distributed-lag HAC regression and flow concentration",
            "uncertainty": "moving-block max-t simultaneous bands",
            "claim_boundary": "timing-sensitive association; no price-impact attribution",
        },
        {
            "research_question": "RQ3",
            "estimand_id": "leverage_tails_connectedness",
            "samples": "S1|S2",
            "outcomes": "tail indicator|quantile return|expected shortfall|FEVD share",
            "exposures": "lagged leverage|funding|open interest|liquidations",
            "method": "spline logit|quantile regression|CoVaR and MES|rolling generalized FEVD",
            "uncertainty": "HAC and moving-block bootstrap",
            "claim_boundary": "conditional association; no forecasting or trading rule",
        },
        {
            "research_question": "RQ4",
            "estimand_id": "liquidity_and_market_structure",
            "samples": "S1|S4",
            "outcomes": "concentration|turnover|liquidity residual|chain share",
            "exposures": "monthly membership|stablecoin supply|price-adjusted TVL|chain activity",
            "method": "PIT decomposition|HAC residualization|optional two-way fixed effects",
            "uncertainty": "descriptive bounds|HAC|clustered or Driscoll-Kraay",
            "claim_boundary": "state association; no exogenous-liquidity or daily PIT claim",
        },
    ]
    return pd.DataFrame(rows)


def _source_decision_registry(root: Path) -> pd.DataFrame:
    payload = yaml.safe_load(
        (root / "config" / "source_candidates.yml").read_text(encoding="utf-8")
    )
    rows = []
    for candidate in payload.get("candidates", []):
        rows.append(
            {
                **candidate,
                "gate_status": "pending_probe",
                "access": "",
                "authentication": "",
                "terms": "",
                "earliest_date": "",
                "latest_date": "",
                "cadence": "",
                "missingness": "",
                "duplicates": "",
                "staleness": "",
                "timezone": "",
                "checksum": "",
                "enabled_analysis": "none_until_pass",
                "evidence": "",
            }
        )
    fresh = pd.DataFrame(rows)
    existing_path = root / "research" / "source_decisions.csv"
    if not existing_path.exists():
        return fresh
    existing = pd.read_csv(existing_path).drop_duplicates("source_id", keep="last")
    preserved = existing.set_index("source_id")
    for column in fresh.columns:
        if column == "source_id" or column not in preserved:
            continue
        fresh[column] = fresh.apply(
            lambda row, column=column: (
                preserved.at[row["source_id"], column]
                if row["source_id"] in preserved.index
                and pd.notna(preserved.at[row["source_id"], column])
                else row[column]
            ),
            axis=1,
        )
    return fresh


def _acceptance_registry(root: Path) -> pd.DataFrame:
    payload = yaml.safe_load(
        (root / "config" / "acceptance_criteria.yml").read_text(encoding="utf-8")
    )
    fresh = pd.DataFrame(
        [
            {
                "criterion_id": criterion_id,
                "mandatory": mandatory,
                "name": name,
                "status": "pending",
                "evidence": "",
                "reason": "",
                "verified_at": "",
            }
            for criterion_id, mandatory, name in payload.get("criteria", [])
        ]
    )
    existing_path = root / "research" / "acceptance_ledger.csv"
    if not existing_path.exists():
        return fresh
    existing = pd.read_csv(existing_path).drop_duplicates("criterion_id", keep="last")
    preserved = existing.set_index("criterion_id")
    for column in ["status", "evidence", "reason", "verified_at"]:
        if column not in preserved:
            continue
        fresh[column] = fresh.apply(
            lambda row, column=column: (
                preserved.at[row["criterion_id"], column]
                if row["criterion_id"] in preserved.index
                and pd.notna(preserved.at[row["criterion_id"], column])
                else row[column]
            ),
            axis=1,
        )
    return fresh


def _feature_registry(root: Path) -> pd.DataFrame:
    payload = yaml.safe_load((root / "config" / "feature_registry.yml").read_text(encoding="utf-8"))
    units_payload = yaml.safe_load(
        (root / "config" / "feature_units.yml").read_text(encoding="utf-8")
    )
    units = units_payload.get("units", {})
    features = pd.DataFrame(payload.get("features", []))
    features["unit"] = features["feature_id"].map(units)
    missing_units = features.loc[features["unit"].isna(), "feature_id"].tolist()
    if missing_units:
        raise ValueError(f"feature units are undeclared: {missing_units}")

    daily_path = root / "data_local" / "processed" / "feature_store_daily.parquet"
    if daily_path.exists():
        daily = pd.read_parquet(daily_path)
        for row_index, feature_id in features["feature_id"].items():
            if feature_id not in daily:
                continue
            valid = pd.to_numeric(daily[feature_id], errors="coerce").notna()
            if valid.any():
                features.at[row_index, "first_valid_date"] = (
                    daily.index[valid].min().date().isoformat()
                )
                features.at[row_index, "last_valid_date"] = (
                    daily.index[valid].max().date().isoformat()
                )
    pit = features["feature_id"].eq("pit_hhi")
    features.loc[pit, "first_valid_date"] = "2020-01-31"
    features.loc[pit, "last_valid_date"] = "2026-05-31"
    return features
