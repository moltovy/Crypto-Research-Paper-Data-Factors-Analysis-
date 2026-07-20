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
from cqresearch.data.inventory import physical_column_inventory, source_file_inventory


def build_foundation_registries(root: Path) -> list[Path]:
    research = root / "research"
    contracts = pd.DataFrame(
        contract_record(item) for item in load_source_contracts(root).values()
    ).sort_values("source_family")
    raw_objects = source_file_inventory(root).rename(columns={"source_group": "provider"})
    physical_columns = physical_column_inventory(root)
    features = _feature_registry(root)
    estimands = _estimand_registry()
    decisions = _source_decision_registry(root)
    acceptance = _acceptance_registry(root)
    return [
        write_csv(research / "source_contracts.csv", contracts),
        write_csv(research / "raw_objects.csv", raw_objects),
        write_csv(research / "physical_columns.csv", physical_columns),
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
            "question": "How broad are common crypto variation, lower-tail dependence, and conditional TradFi integration?",
            "inputs": "S2/S3 returns|BTC/ETH returns|SPY|QQQ|IWM|DXY|GLD|VIX|real and nominal yields",
            "samples": "S1|S2|S3",
            "outcomes": "returns|tail indicators",
            "exposures": "leave-one-out common factor|TradFi returns and changes",
            "estimand": "leave-one-out common variance share|conditional beta|joint, conditional, and excess co-exceedance|era interaction",
            "primary_specification": "leave-one-out PCA; 252-session HAC exposure with 126 minimum; q=1%,2.5%,5%,10%; formal interaction",
            "method": "PCA|HAC rolling exposure|tail co-exceedance|break tests",
            "uncertainty": "HAC and moving-block bootstrap",
            "assumptions": "matched contract-valid observations; descriptive dependence; stable fixed-core composition",
            "diagnostics": "coverage|self-inclusion|condition number|residual dependence|heteroskedasticity|break stability",
            "robustness": "moving-block bootstrap 2000 replications; block lengths 5/10/20; factor-composition sensitivity",
            "decision_rule": "report point estimates and intervals; qualify as weak when intervals or adjusted tests include the null",
            "tables": "common_factor_results.csv|tail_dependence.csv|dynamic_tradfi_exposures.csv|break_tests.csv",
            "figures": "01_common_factor_tail_dependence|02_dynamic_tradfi_integration",
            "claim_boundary": "descriptive dependence and conditional association",
        },
        {
            "research_question": "RQ2",
            "estimand_id": "institutional_market_plumbing",
            "question": "How do institutional flow intensity and regulated positioning line up with market outcomes?",
            "inputs": "Farside BTC/ETH ETF flows|lagged market capitalization|CFTC positioning|contract-valid derivatives",
            "samples": "S5",
            "outcomes": "crypto return|absolute return|realized volatility",
            "exposures": "ETF flow divided by lagged market capitalization",
            "estimand": "lag-0 through lag-5 flow-intensity coefficients|cumulative lag association|flow concentration|positioning share",
            "primary_specification": "distributed-lag HAC model on actual report dates; lagged market-cap denominator; no zero fill",
            "method": "distributed-lag HAC regression and flow concentration",
            "uncertainty": "moving-block max-t simultaneous bands",
            "assumptions": "reported-date convention is an imperfect timing proxy; denominator is known at t-1",
            "diagnostics": "pre-inception missingness|exchange-calendar support|timing shift|lag collinearity|issuer coverage",
            "robustness": "2000-replication block max-t; lag-zero and one-session-shift conventions; inflow/outflow and volatility-state splits",
            "decision_rule": "simultaneous interval must exclude zero for supported lag evidence; otherwise report weak",
            "tables": "etf_distributed_lags.csv|etf_flow_concentration.csv|institutional_positioning.csv",
            "figures": "04_institutional_market_plumbing",
            "claim_boundary": "timing-sensitive association; no price-impact attribution",
        },
        {
            "research_question": "RQ3",
            "estimand_id": "leverage_tails_connectedness",
            "question": "Where do lagged leverage states coincide with tails, expected shortfall, and connectedness?",
            "inputs": "BTC/ETH OI-to-market-cap|funding|liquidations|returns|volatility|S2 returns",
            "samples": "S1|S2",
            "outcomes": "tail indicator|quantile return|expected shortfall|FEVD share",
            "exposures": "lagged leverage|funding|open interest|liquidations",
            "estimand": "conditional tail probability curve|5% and 10% quantile association|ES|CoVaR|delta-CoVaR|MES|generalized FEVD connectedness",
            "primary_specification": "lagged-state spline logit; 5% quantile/ES; 252-observation stable-core VAR; BIC lag <=5; horizon 10",
            "method": "spline logit|quantile regression|CoVaR and MES|rolling generalized FEVD",
            "uncertainty": "HAC and moving-block bootstrap",
            "assumptions": "lagged state is observable before outcome; VAR is stable within each rolling window",
            "diagnostics": "support|collinearity|influence|calibration|stationarity|VAR stability|FEVD row sums",
            "robustness": "five-day non-overlapping outcomes; 10% quantile; windows 180/365; horizons 5/20; variable-order permutations",
            "decision_rule": "state differences require supported intervals and observed support; unstable VAR windows are excluded",
            "tables": "leverage_tail_model.csv|quantile_es.csv|systemic_tail_association.csv|connectedness.csv",
            "figures": "03_leverage_tail_connectedness",
            "claim_boundary": "conditional association; no forecasting or trading rule",
        },
        {
            "research_question": "RQ4",
            "estimand_id": "liquidity_and_market_structure",
            "question": "How did endogenous liquidity state and monthly point-in-time market structure change?",
            "inputs": "monthly PIT top 100|DefiLlama stablecoin and TVL|BTC/ETH/TOTAL3 controls|Artemis chain activity|MVRV and realized cap",
            "samples": "S1|S4",
            "outcomes": "concentration|turnover|liquidity residual|chain share",
            "exposures": "monthly membership|stablecoin supply|price-adjusted TVL|chain activity",
            "estimand": "HHI|entropy/effective count|turnover/entry/exit/survival|exact concentration decomposition|TVL residual state|chain-panel association|MVRV identity residual",
            "primary_specification": "complete monthly PIT top-100 census; HAC TVL residualization on crypto-market controls; diagnostic MVRV identity",
            "method": "PIT decomposition|HAC residualization|optional two-way fixed effects",
            "uncertainty": "descriptive bounds|HAC|clustered or Driscoll-Kraay",
            "assumptions": "PIT snapshots are monthly censuses; USD TVL remains valuation-sensitive and endogenous",
            "diagnostics": "partial-month exclusion|decomposition identity|panel support|residual dependence|MVRV identity fit",
            "robustness": "alternative concentration measures; turnover components; chain panel only with >=4 chains and >=36 common months",
            "decision_rule": "optional chain model runs only when support gate passes; MVRV remains appendix-only",
            "tables": "pit_concentration.csv|pit_membership_transitions.csv|pit_concentration_decomposition.csv|liquidity_state.csv|chain_panel.csv|measurement_mechanics.csv",
            "figures": "07_pit_concentration_turnover|05_liquidity_measurement_diagnostics",
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

    contracts = load_source_contracts(root)
    provider_keys = {
        "CryptoQuant": ("cryptoquant",),
        "DefiLlama": ("defillama",),
        "FRED": ("fred",),
        "Farside": ("farside",),
        "TradingView": ("tradingview",),
        "TradingView/FRED": ("tradingview", "fred"),
    }

    def contract_text(source: str, field: str) -> str:
        values = [str(getattr(contracts[key], field)) for key in provider_keys[str(source)]]
        return " | ".join(dict.fromkeys(values))

    features["availability_rule"] = features["raw_source"].map(
        lambda source: contract_text(str(source), "availability_rule")
    )
    features["timezone"] = features["raw_source"].map(
        lambda source: contract_text(str(source), "timezone")
    )
    features["native_calendar"] = features["raw_source"].map(
        lambda source: contract_text(str(source), "native_calendar")
    )
    features["sample_eligibility"] = features.apply(_feature_sample_eligibility, axis=1)
    features["evidence_class"] = features["research_block"].map(
        {
            "target": "outcome",
            "macro_risk": "contemporaneous_external_market_association",
            "etf_institutional": "timing_sensitive_market_plumbing",
            "leverage": "endogenous_lagged_state",
            "liquidity": "endogenous_state_proxy",
            "onchain_state": "endogenous_state_proxy",
            "market_structure": "monthly_point_in_time_census",
        }
    )

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


def _feature_sample_eligibility(row: pd.Series) -> str:
    block = str(row["research_block"])
    if block == "etf_institutional":
        return "S5 actual reporting life only"
    if block == "market_structure":
        return "S4 complete monthly PIT snapshots only"
    if block in {"target", "macro_risk", "leverage", "liquidity", "onchain_state"}:
        return "S1 contract-valid daily support; S2 only where fixed-core returns are required"
    return "not eligible until an explicit sample contract is assigned"
