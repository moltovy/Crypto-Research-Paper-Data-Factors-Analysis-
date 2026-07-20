"""Scientific and release contracts for the rebuilt public research surface."""

from __future__ import annotations

import json
import re
import subprocess
import tomllib
from pathlib import Path

import numpy as np
import pandas as pd

from cqresearch.pipelines.final_research import classify_pit_asset

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research"
EXPECTED_MODULES = [
    "00_data_measurement_foundation",
    "01_cross_asset_dependence_regimes",
    "02_macro_tradfi_integration",
    "03_derivatives_leverage_liquidations",
    "04_etf_institutional_flows",
    "05_stablecoin_defi_liquidity",
    "07_chain_fundamentals_sector_dynamics",
    "09_event_stress_cross_module_synthesis",
]


def test_final_module_architecture_is_exact() -> None:
    module_dirs = sorted(path.name for path in RESEARCH.iterdir() if path.is_dir())
    assert module_dirs == EXPECTED_MODULES
    assert not (RESEARCH / "06_onchain_valuation_holder_behavior").exists()
    assert not (RESEARCH / "08_relative_asset_risk_factor_structure").exists()


def test_root_readme_is_four_question_evidence_surface() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_order = [
        "## Project Overview",
        "## Evidence Map",
        "## Data Universe and Asset Coverage",
        "## Research Modules",
        "## Qualified Findings",
        "## Evidence Figures",
        "## Methods Used",
        "## Important Limitations",
        "## Reproduce",
    ]
    positions = [readme.index(heading) for heading in required_order]
    assert positions == sorted(positions)
    evidence_map = readme.split("## Evidence Map", 1)[1].split(
        "## Data Universe and Asset Coverage", 1
    )[0]
    evidence_rows = [line for line in evidence_map.splitlines() if line.startswith("| ")]
    assert len(evidence_rows) == 5  # header plus four registered questions
    assert len(re.findall(r"!\[[^\]]*\]\(([^)]+)\)", readme)) == 5
    assert "Results At A Glance" not in readme
    assert "outputs/" not in readme


def test_module_readmes_and_claim_lineage_are_complete() -> None:
    required_claim_fields = {
        "sample",
        "method",
        "uncertainty",
        "evidence_grade",
        "source_table",
        "source_figure",
        "limitation",
    }
    for module_id in EXPECTED_MODULES:
        module = RESEARCH / module_id
        content = (module / "README.md").read_text(encoding="utf-8")
        assert "## Methodologies and Calculations" in content
        assert "## Summary of Results" in content
        claims = pd.read_csv(module / "tables" / "claims.csv")
        assert required_claim_fields <= set(claims.columns)
        assert claims[list(required_claim_fields)].notna().all().all()
        if module_id != "00_data_measurement_foundation":
            images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", content)
            assert 1 <= len(images) <= 3


def test_dependence_outputs_use_fixed_core_and_leave_one_out_factors() -> None:
    base = RESEARCH / "01_cross_asset_dependence_regimes" / "tables"
    factors = pd.read_csv(base / "common_factor_results.csv")
    tails = pd.read_csv(base / "tail_dependence.csv")
    coverage = pd.read_csv(base / "asset_return_coverage.csv")
    assert len(factors) == 14
    assert not factors["self_included"].astype(bool).any()
    assert factors["n"].eq(2006).all()
    assert coverage["coverage"].min() >= 0.99
    assert set(tails["quantile"]) == {0.01, 0.025, 0.05, 0.1}
    primary = tails[tails["primary_specification"].astype(bool)]
    assert primary["bootstrap_reps"].eq(2000).all()
    np.testing.assert_allclose(primary["independence_probability"], primary["quantile"] ** 2)


def test_tradfi_outputs_use_native_sessions_and_report_weak_interactions() -> None:
    base = RESEARCH / "02_macro_tradfi_integration" / "tables"
    rolling = pd.read_csv(base / "dynamic_tradfi_exposures.csv")
    breaks = pd.read_csv(base / "break_tests.csv")
    assert rolling["window"].eq(252).all()
    assert rolling["n"].eq(252).all()
    assert set(breaks["asset"]) == {"BTC", "ETH"}
    assert not breaks["feature_id"].str.contains("mvrv", case=False).any()
    qqq = breaks[breaks["feature_id"].eq("qqq_ret")]
    assert (qqq["era_beta_change_pvalue"] > 0.05).all()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "formal ETF-era interaction estimates are weak" in readme


def test_etf_outputs_preserve_inception_and_simultaneous_inference() -> None:
    base = RESEARCH / "04_etf_institutional_flows" / "tables"
    lags = pd.read_csv(base / "etf_distributed_lags.csv")
    timing = pd.read_csv(base / "etf_timing_sensitivity.csv")
    assert set(lags["asset"]) == {"BTC", "ETH"}
    assert set(lags["lag_sessions"]) == set(range(6))
    assert lags["bootstrap_reps"].eq(2000).all()
    assert pd.to_datetime(lags.loc[lags["asset"].eq("BTC"), "sample_start"]).min() >= pd.Timestamp(
        "2024-01-11"
    )
    assert pd.to_datetime(lags.loc[lags["asset"].eq("ETH"), "sample_start"]).min() >= pd.Timestamp(
        "2024-07-23"
    )
    assert {"return_correlation", "absolute_return_correlation"} <= set(timing.columns)
    corporate = pd.read_csv(base / "corporate_exposure_eras.csv")
    assert corporate.loc[0, "status"] == "not_run"


def test_leverage_and_connectedness_diagnostics_are_bounded() -> None:
    base = RESEARCH / "03_derivatives_leverage_liquidations" / "tables"
    curve = pd.read_csv(base / "leverage_tail_model.csv")
    connectedness = pd.read_csv(base / "connectedness.csv")
    assert curve["predicted_tail_probability"].between(0, 1).all()
    assert (curve["ci_low"] <= curve["predicted_tail_probability"]).all()
    assert (curve["ci_high"] >= curve["predicted_tail_probability"]).all()
    successful = connectedness[connectedness["error"].fillna("").eq("")]
    assert successful["stable"].astype(bool).all()
    assert successful["row_sum_max_error"].max() < 1e-10
    assert successful["connectedness_pct"].between(0, 100).all()


def test_liquidity_and_mvrv_guardrails_are_explicit() -> None:
    base = RESEARCH / "05_stablecoin_defi_liquidity" / "tables"
    coefficients = pd.read_csv(base / "liquidity_state_coefficients.csv")
    mechanics = pd.read_csv(base / "measurement_mechanics.csv")
    assert coefficients["r_squared"].max() < 0.05
    mvrv = mechanics.loc[mechanics["metric"].eq("correlation__btc_ret__d_log_mvrv")]
    assert mvrv["value"].iat[0] > 0.95
    assert mechanics["interpretation"].str.contains("measurement", case=False).all()
    assert (
        "MVRV"
        not in (ROOT / "config" / "public_figures.yml")
        .read_text(encoding="utf-8")
        .split("status: public")[0]
    )


def test_pit_outputs_exclude_partial_months_and_decompose_exactly() -> None:
    base = RESEARCH / "07_chain_fundamentals_sector_dynamics" / "tables"
    concentration = pd.read_csv(base / "pit_concentration.csv")
    decomposition = pd.read_csv(base / "pit_concentration_decomposition.csv")
    transitions = pd.read_csv(base / "pit_membership_transitions.csv")
    assert pd.to_datetime(concentration["snapshot_date"]).max() == pd.Timestamp("2026-05-31")
    np.testing.assert_allclose(decomposition["residual"], 0, atol=1e-12)
    assert transitions["turnover_rate"].between(0, 1).all()
    assert (concentration["effective_asset_count"] > 1).all()


def test_event_synthesis_contains_only_current_claims() -> None:
    base = RESEARCH / "09_event_stress_cross_module_synthesis" / "tables"
    ledger = pd.read_csv(base / "evidence_ledger.csv")
    responses = pd.read_csv(base / "event_response_matrix.csv")
    assert set(ledger["module_id"]) <= set(EXPECTED_MODULES)
    assert (
        not ledger["module_id"]
        .isin({"06_onchain_valuation_holder_behavior", "08_relative_asset_risk_factor_structure"})
        .any()
    )
    assert set(responses["window_days"]) == {1, 5, 10}
    assert responses["timing"].str.contains("event day excluded").all()


def test_figure_sidecars_have_unique_plot_keys_and_metadata() -> None:
    for png in RESEARCH.glob("*/figures/*.png"):
        source = png.with_suffix(".source.csv")
        metadata = png.with_suffix(".metadata.json")
        if source.exists():
            frame = pd.read_csv(source)
            assert frame["plot_key"].is_unique, source
            payload = json.loads(metadata.read_text(encoding="utf-8"))
            assert payload["rows"] == len(frame)
            assert payload["source_tables"]


def test_public_claims_avoid_prohibited_language() -> None:
    claims = pd.concat(
        [pd.read_csv(path) for path in sorted(RESEARCH.glob("*/tables/claims.csv"))],
        ignore_index=True,
    )
    text = " ".join(claims["claim_text"].str.lower())
    for phrase in ["will outperform", "trading signal", "causes returns", "price forecast"]:
        assert phrase not in text


def test_canonical_id_collision_handling_is_not_symbol_first() -> None:
    wrapped = pd.Series(
        {
            "symbol": "SOL",
            "asset_name": "Wrapped SOL",
            "coingecko_id": "coingecko:wrapped-sol",
            "asset_key": "coingecko:wrapped-sol",
        }
    )
    ton = pd.Series(
        {
            "symbol": "GRAM",
            "asset_name": "Toncoin",
            "coingecko_id": "coingecko:the-open-network",
            "asset_key": "coingecko:the-open-network",
        }
    )
    assert classify_pit_asset(wrapped) == "productized/wrapped assets"
    assert classify_pit_asset(ton) == "selected majors ex BTC/ETH"


def test_package_ci_and_raw_data_policy() -> None:
    metadata = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    assert metadata["name"] == "crypto-market-dynamics"
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "scripts/run_all.py --mode fixture" in workflow
    assert "scripts/run_all.py --mode artifact" in workflow
    result = subprocess.run(
        ["git", "ls-files", "--", "data_local", "data_cache", "reports/panels"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == ""
