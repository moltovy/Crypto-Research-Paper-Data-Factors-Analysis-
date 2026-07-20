"""Build the repository root README, research index, manifests, and figure specs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd
import yaml
from config.paths import PROJECT_ROOT

from cqresearch.core.artifacts import (
    artifact_record,
    sha256_file,
    write_csv,
    write_json,
    write_text,
)
from cqresearch.research.registry import MODULES

ROOT_FIGURE_SELECTION_COLUMNS = [
    "figure_id",
    "module",
    "finding",
    "empirical_strength",
    "robustness",
    "economic_relevance",
    "june_2026_relevance",
    "cross_asset_breadth",
    "visual_quality",
    "weighted_score",
    "hard_exclusion",
    "selected",
    "reason",
]


def build_root_research_surface(root: Path = PROJECT_ROOT) -> list[Path]:
    research_dir = root / "research"
    research_dir.mkdir(parents=True, exist_ok=True)

    module_rows = _module_rows(root)
    figure_specs = _figure_specs(root)
    selection = _root_figure_selection(figure_specs)
    usage_counts = _usage_counts(root)

    research_readme = _research_index(module_rows, figure_specs, usage_counts)
    root_readme = _root_readme(root, module_rows, figure_specs, selection, usage_counts)
    artifacts: list[Path] = [
        write_csv(research_dir / "figure_specs.csv", figure_specs),
        write_csv(research_dir / "root_figure_selection.csv", selection),
        write_text(research_dir / "README.md", research_readme),
        write_text(root / "README.md", root_readme),
    ]
    artifacts.append(
        _write_root_manifest(root, module_rows, figure_specs, selection, usage_counts, artifacts)
    )
    return artifacts


def _module_rows(root: Path) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for module in MODULES:
        module_dir = root / "research" / module.module_id
        manifest_path = module_dir / "manifest.json"
        manifest = _read_json(manifest_path)
        artifacts = manifest.get("artifacts", []) if isinstance(manifest, dict) else []
        tables = sorted(path.name for path in (module_dir / "tables").glob("*") if path.is_file())
        figures = sorted(
            path.name for path in (module_dir / "figures").glob("*.png") if path.is_file()
        )
        rows.append(
            {
                "module_id": module.module_id,
                "title": module.title,
                "question": module.research_question,
                "path": f"research/{module.module_id}",
                "manifest_path": f"research/{module.module_id}/manifest.json",
                "manifest_sha256": sha256_file(manifest_path) if manifest_path.exists() else "",
                "artifact_count": len(artifacts),
                "table_count": len(tables),
                "figure_count": len(figures),
            }
        )
    return pd.DataFrame(rows)


def _figure_specs(root: Path) -> pd.DataFrame:
    registry = _figure_registry(root)
    rows: list[dict[str, Any]] = []
    modules = {item.module_id: item for item in MODULES}
    for png_path in sorted((root / "research").glob("*/figures/*.png")):
        relpath = png_path.relative_to(root).as_posix()
        module_id = png_path.relative_to(root / "research").parts[0]
        if module_id not in modules:
            continue
        module = modules[module_id]
        registered = registry.get(relpath, {})
        source_tables = registered.get("source_tables") or _claim_source_tables(
            root, module_id, png_path.name
        )
        rows.append(
            {
                "figure_id": registered.get("figure_id", png_path.stem),
                "module": module_id,
                "research_question": registered.get("research_question", module.research_question),
                "model_ids": _model_ids_from_source_tables(source_tables),
                "source_tables": source_tables,
                "chart_type": registered.get("chart_type", _chart_type_from_name(png_path.stem)),
                "x": registered.get("x", "see source table"),
                "y": registered.get("y", "see source table"),
                "interval": registered.get(
                    "interval", "shown where source model reports uncertainty"
                ),
                "sample": registered.get("sample", "see source table"),
                "figure_path": relpath,
                "svg_path": png_path.with_suffix(".svg").relative_to(root).as_posix(),
                "title": registered.get("caption", png_path.stem.replace("_", " ").title()),
                "subtitle": registered.get("units", "derived analytical output"),
                "interpretation": registered.get(
                    "caption", "See module findings and interpretation."
                ),
                "limitation": registered.get("caveat", "See module limitations."),
                "root_readme": registered.get("status") == "public",
                "visual_qa_status": registered.get("visual_qa_status", "manual_review_required"),
                "root_order": int(registered.get("root_order", 999)),
            }
        )
    return (
        pd.DataFrame(rows).sort_values(["root_order", "module", "figure_id"]).reset_index(drop=True)
    )


def _figure_registry(root: Path) -> dict[str, dict[str, Any]]:
    path = root / "config" / "public_figures.yml"
    if not path.exists():
        return {}
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(item.get("filename", "")): item for item in payload.get("figures", [])}


def _claim_source_tables(root: Path, module_id: str, figure_name: str) -> str:
    claims_path = root / "research" / module_id / "tables" / "claims.csv"
    if not claims_path.exists():
        return f"research/{module_id}/tables/claims.csv"
    claims = pd.read_csv(claims_path)
    if "source_figure" in claims:
        matches = claims[
            claims["source_figure"].astype(str).str.contains(figure_name, regex=False, na=False)
        ]
        if not matches.empty:
            return "; ".join(matches["source_table"].dropna().astype(str).unique())
    return f"research/{module_id}/tables/claims.csv"


def _root_figure_selection(figure_specs: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if figure_specs.empty:
        return pd.DataFrame(columns=ROOT_FIGURE_SELECTION_COLUMNS)
    excluded_terms = {
        "mvrv": "measurement warning belongs in methodology/appendix, not default root slot",
        "selected_major_asset_risk": "basic volatility/drawdown scatter is excluded",
        "cumulative": "ETF cumulative-flow root figure is excluded",
    }
    for row in figure_specs.to_dict("records"):
        figure_id = str(row["figure_id"])
        figure_path = str(row["figure_path"])
        text = f"{figure_id} {figure_path} {row.get('chart_type', '')}".lower()
        hard_exclusion = ""
        for term, reason in excluded_terms.items():
            if term in text:
                hard_exclusion = reason
                break
        selected = bool(row.get("root_readme", False)) and not hard_exclusion
        empirical_strength = _score(row, "empirical")
        robustness = _score(row, "robustness")
        economic = _score(row, "economic")
        june = _score(row, "june")
        breadth = _score(row, "breadth")
        visual = _score(row, "visual")
        weighted = round(
            0.25 * empirical_strength
            + 0.20 * robustness
            + 0.20 * economic
            + 0.15 * june
            + 0.10 * breadth
            + 0.10 * visual,
            2,
        )
        rows.append(
            {
                "figure_id": figure_id,
                "module": row["module"],
                "finding": row.get("title", figure_id),
                "empirical_strength": empirical_strength,
                "robustness": robustness,
                "economic_relevance": economic,
                "june_2026_relevance": june,
                "cross_asset_breadth": breadth,
                "visual_quality": visual,
                "weighted_score": weighted,
                "hard_exclusion": hard_exclusion,
                "selected": selected,
                "reason": "selected root evidence map figure"
                if selected
                else hard_exclusion or "module/appendix figure retained outside root selection",
            }
        )
    return pd.DataFrame(rows)[ROOT_FIGURE_SELECTION_COLUMNS].reset_index(drop=True)


def _score(row: dict[str, Any], dimension: str) -> int:
    text = f"{row.get('figure_id', '')} {row.get('chart_type', '')} {row.get('source_tables', '')} {row.get('module', '')}".lower()
    if dimension == "empirical":
        return (
            5
            if any(
                term in text for term in ["pca", "lag_response", "tail", "delta", "decomposition"]
            )
            else 3
        )
    if dimension == "robustness":
        return (
            5
            if any(
                term in text
                for term in ["bootstrap", "ridge", "fdr", "same-support", "pca", "lag_response"]
            )
            else 3
        )
    if dimension == "economic":
        return (
            5
            if any(term in text for term in ["macro", "etf", "leverage", "risk", "dependence"])
            else 3
        )
    if dimension == "june":
        return (
            5
            if any(term in text for term in ["etf", "leverage", "macro", "cross_asset", "relative"])
            else 3
        )
    if dimension == "breadth":
        return 5 if any(term in text for term in ["cross_asset", "relative", "macro"]) else 3
    if dimension == "visual":
        return 5 if str(row.get("visual_qa_status", "")).startswith("pass") else 3
    return 3


def _usage_counts(root: Path) -> dict[str, int]:
    path = (
        root / "research" / "00_data_measurement_foundation" / "tables" / "feature_usage_matrix.csv"
    )
    if not path.exists():
        return {}
    usage = pd.read_csv(path)
    return {str(key): int(value) for key, value in usage["usage_status"].value_counts().items()}


def _usage_status_label(status: str) -> str:
    return {
        "diagnostic_only": "diagnostic only",
        "excluded_ambiguous_definition_or_unit": "excluded for ambiguous definition or unit",
        "excluded_duplicate": "excluded duplicate",
        "excluded_insufficient_coverage": "excluded for insufficient coverage",
        "excluded_release_risk": "excluded for release risk",
        "primary_analysis": "primary analysis",
        "robustness_or_sensitivity": "robustness or sensitivity",
    }.get(status, status.replace("_", " "))


def _root_readme(
    root: Path,
    module_rows: pd.DataFrame,
    figure_specs: pd.DataFrame,
    selection: pd.DataFrame,
    usage_counts: dict[str, int],
) -> str:
    selected = selection[selection["selected"].eq(True)] if not selection.empty else pd.DataFrame()
    fig_map = figure_specs.set_index("figure_id").to_dict("index") if not figure_specs.empty else {}
    figure_sections = []
    for item in selected.itertuples(index=False):
        spec = fig_map.get(item.figure_id, {})
        source = str(spec.get("source_tables", "")).split(";")[0].strip()
        figure_sections.append(
            f"### {spec.get('title', item.finding)}\n\n"
            f"![{item.finding}]({spec.get('figure_path', '')})\n\n"
            f"**Sample:** {spec.get('sample', 'see source table')}. "
            f"**Method:** {str(spec.get('chart_type', 'analytical result')).replace('_', ' ').replace('fevd', 'FEVD')}.\n\n"
            f"**Result:** {spec.get('interpretation', item.finding)} "
            f"**Boundary:** {spec.get('limitation', '')} [Source table]({source})."
        )
    figure_text = "\n\n".join(figure_sections)
    module_map = "\n".join(
        f"| [{str(row.module_id).split('_', 1)[0]}]({row.path}/README.md) | {row.title} | {row.question} |"
        for row in module_rows.itertuples(index=False)
    )
    findings = _headline_findings(root, module_rows)
    methods = "\n".join(
        [
            "| Method family | Used for | Key boundary |",
            "|---|---|---|",
            "| Leave-one-out PCA and moving-block tail inference | common variation and co-exceedance | realized dependence only |",
            "| Multivariate HAC exposure and era interactions | TradFi integration | contemporaneous period comparison |",
            "| Distributed lags with max-t bands | ETF market plumbing | timing and simultaneity remain unresolved |",
            "| Spline logit, quantile/ES, generalized FEVD | leverage and tail stress | descriptive state association |",
            "| PIT concentration, turnover, and exact decomposition | monthly market structure | no daily constituent-performance inference |",
        ]
    )
    status_list = ", ".join(
        f"{_usage_status_label(key)}: {value}" for key, value in sorted(usage_counts.items())
    )
    return f"""# Crypto Market Dynamics

## Project Overview

Crypto Market Dynamics is a reproducible empirical study of how crypto dependence, financial integration, institutional plumbing, leverage stress, liquidity state, and market structure evolved through the frozen 2026-06-30 acquisition cutoff.

The evidence is descriptive and associational. It does not forecast prices, propose trading rules, or identify causal effects.

## Evidence Map

| Question | Primary evidence | Sample boundary | Main limitation |
|---|---|---|---|
| How broad are common crypto variation, lower-tail dependence, and TradFi integration? | [Common-factor and tail tables](research/01_cross_asset_dependence_regimes/README.md); [dynamic TradFi exposures](research/02_macro_tradfi_integration/README.md) | S2 fixed stable core from 2021; XNYS-matched BTC/ETH from 2020 | Dependence and period comparisons are not causal or predictive. |
| How do institutional flows and positioning line up with market outcomes? | [ETF distributed lags and CFTC positioning](research/04_etf_institutional_flows/README.md) | Actual reporting lives; no pre-inception or holiday zero fill | Reporting time and simultaneity prevent price-impact interpretation. |
| Where do leverage states coincide with tails and connectedness? | [Leverage, expected shortfall, systemic-tail, and FEVD tables](research/03_derivatives_leverage_liquidations/README.md) | BTC state panel from 2020; S2 connectedness from 2021 | State associations are not forecasts, signals, or liquidation-cause estimates. |
| How did endogenous liquidity state and monthly market structure change? | [TVL residual and MVRV mechanics](research/05_stablecoin_defi_liquidity/README.md); [PIT structure and turnover](research/07_chain_fundamentals_sector_dynamics/README.md) | Daily liquidity panel; complete monthly PIT snapshots through May 2026 | USD TVL is valuation-sensitive; PIT data cannot recover daily constituent performance. |

## Data Universe and Asset Coverage

The [data-foundation module](research/00_data_measurement_foundation/README.md) inventories raw objects separately from logical series and records feature semantics, identity, timing, units, source eligibility, and release risk. Current data-usage counts are {status_list or "available in the data-foundation module"}.

S2 fixes PIT-eligible, identity-resolved assets using the January 2021 top-20 snapshot and requires at least 95% daily coverage. S4 uses monthly top-100 point-in-time snapshots only. S5 begins each institutional series at its actual reporting inception.

## Research Modules

| Module | Title | Scope |
|---|---|---|
{module_map}

## Qualified Findings

{findings}

## Evidence Figures

{figure_text}

## Methods Used

{methods}

## Important Limitations

- S2 is fixed from a January 2021 PIT snapshot; S3 current-cohort daily analysis remains survivorship-biased and cannot establish historical altseason behavior.
- ETF flows are market-plumbing associations with timing and simultaneity concerns.
- Stablecoin supply, DeFi TVL, and related balance-sheet measures are endogenous state proxies; raw USD TVL is valuation-sensitive.
- Same-day MVRV is a mechanically price-linked valuation-state diagnostic and is excluded from primary BTC/ETH models.
- Monthly point-in-time data supports composition, concentration, turnover, and state variables only, not daily constituent returns.

## Reproduce

```bash
uv sync --all-extras
uv run ruff check src/cqresearch scripts tests
uv run ruff format --check src/cqresearch scripts tests
uv run mypy src/cqresearch
uv run pytest -q
uv run python scripts/run_all.py --mode local
uv run python scripts/build_research_figures.py --module all
uv run python scripts/check_research_surface.py --module all
```

## Repository Structure

- [`research/`](research/README.md): canonical public research surface.
- [`src/cqresearch/`](src/cqresearch): contracts, samples, estimators, reporting, and visualization code.
- [`scripts/`](scripts): thin command-line entry points.
- [`config/`](config): data, sample, source, figure, and module registries.
- `data_local/`: local raw data, normalized panels, caches, and private QA evidence; intentionally untracked.

## Data Policy and Citation

Raw/provider data stays local under `data_local/` and outside Git. Public tables and figures are derived semantic outputs designed for review without redistributing provider exports.

This repository is independent research and is not affiliated with any data provider. See [`REFERENCES.md`](REFERENCES.md) for source and method attribution. Cite the commit, module, table, figure, sample definition, uncertainty statement, and limitation when referencing a result.
"""


def _research_index(
    module_rows: pd.DataFrame, figure_specs: pd.DataFrame, usage_counts: dict[str, int]
) -> str:
    module_map = "\n".join(
        "| [{module_id}]({relpath}/README.md) | {title} | {tables} | {figures} |".format(
            module_id=str(row.module_id).split("_", 1)[0],
            relpath=Path(row.path).relative_to("research").as_posix(),
            title=row.title,
            tables=row.table_count,
            figures=row.figure_count,
        )
        for row in module_rows.itertuples(index=False)
    )
    root_figures = figure_specs[figure_specs["root_readme"].eq(True)]
    figure_list = "\n\n".join(
        "![{title}]({path})\n\nSource: `{source}`. Boundary: {limitation}".format(
            title=str(row.title),
            path=Path(str(row.figure_path)).relative_to("research").as_posix(),
            source=str(row.source_tables),
            limitation=str(row.limitation),
        )
        for row in root_figures.itertuples(index=False)
    )
    status_list = "\n".join(
        f"- {_usage_status_label(key)}: {value}" for key, value in sorted(usage_counts.items())
    )
    return f"""# Research Surface

This directory is the canonical public research surface for Crypto Market Dynamics. It contains generated modules, tables, figures, manifests, and the root figure-selection audit.

## Module Map

| Module | Title | Tables | Figures |
|---|---|---:|---:|
{module_map}

## Root Figure Set

{figure_list}

## Data-Usage Status Counts

{status_list}

## Provenance

- Root manifest: [`manifest.json`](manifest.json)
- Figure specifications: [`figure_specs.csv`](figure_specs.csv)
- Root figure selection: [`root_figure_selection.csv`](root_figure_selection.csv)
- Cross-module evidence ledger: [`09_event_stress_cross_module_synthesis/tables/evidence_ledger.csv`](09_event_stress_cross_module_synthesis/tables/evidence_ledger.csv)

## Rebuild

```bash
uv run python scripts/run_research.py --module all
uv run python scripts/build_research_figures.py --module all
uv run python scripts/check_research_surface.py --module all
```
"""


def _headline_findings(root: Path, module_rows: pd.DataFrame) -> str:
    rows = []
    selected_modules = {
        "01_cross_asset_dependence_regimes",
        "02_macro_tradfi_integration",
        "03_derivatives_leverage_liquidations",
        "04_etf_institutional_flows",
        "07_chain_fundamentals_sector_dynamics",
    }
    for module_row in module_rows.itertuples(index=False):
        module = str(module_row.module_id)
        if module not in selected_modules:
            continue
        claims_path = root / "research" / str(module) / "tables" / "claims.csv"
        if not claims_path.exists():
            continue
        claims = pd.read_csv(claims_path)
        if claims.empty:
            continue
        claim = claims.iloc[0]
        rows.append(
            "| {module} | {finding} | {grade} | [{table}]({table}) | {limitation} |".format(
                module=str(module_row.title),
                finding=str(claim.get("claim_text", "")),
                grade=str(claim.get("evidence_grade", "")),
                table=str(claim.get("source_table", ""))
                .split(";")[0]
                .replace("tables/", f"research/{module}/tables/"),
                limitation=str(claim.get("limitation", "")),
            )
        )
    header = "| Module | Finding | Grade | Source | Limitation |\n|---|---|---|---|---|"
    return header + "\n" + "\n".join(rows[:5])


def _write_root_manifest(
    root: Path,
    module_rows: pd.DataFrame,
    figure_specs: pd.DataFrame,
    selection: pd.DataFrame,
    usage_counts: dict[str, int],
    artifacts: list[Path],
) -> Path:
    module_payload = module_rows.to_dict(orient="records")
    root_records = [artifact_record(path, root) for path in sorted(artifacts)]
    module_manifest_records = [
        artifact_record(root / str(row["manifest_path"]), root)
        for row in module_payload
        if (root / str(row["manifest_path"])).exists()
    ]
    registry_paths = sorted((root / "research").glob("*.csv"))
    provenance_path = root / "research" / "build_provenance.json"
    if provenance_path.exists():
        registry_paths.append(provenance_path)
    registry_records = [artifact_record(path, root) for path in registry_paths]
    artifact_records = root_records + module_manifest_records + registry_records
    deduplicated_records = {str(record["path"]): record for record in artifact_records}
    payload = {
        "schema_version": 1,
        "canonical_surface": "research",
        "build_timestamp_utc": "not_recorded_for_deterministic_rebuilds",
        "module_count": len(module_payload),
        "modules": module_payload,
        "public_figure_count": int(figure_specs["root_readme"].eq(True).sum())
        if not figure_specs.empty
        else 0,
        "figure_count": int(len(figure_specs)),
        "selected_root_figures": selection[selection["selected"].eq(True)]["figure_id"].tolist()
        if not selection.empty
        else [],
        "data_usage_status_counts": usage_counts,
        "artifacts": [deduplicated_records[path] for path in sorted(deduplicated_records)],
    }
    return write_json(root / "research" / "manifest.json", payload)


def _model_ids_from_source_tables(source_tables: str) -> str:
    ids: list[str] = []
    for item in str(source_tables).replace(",", ";").split(";"):
        item = item.strip()
        if item:
            ids.append(f"table:{Path(item).stem}")
    return "; ".join(ids) or "table:claims"


def _chart_type_from_name(name: str) -> str:
    if "correlation" in name:
        return "correlation_heatmap"
    if "pca" in name or "factor" in name:
        return "factor_decomposition"
    if "etf" in name:
        return "etf_lag_response"
    if "mvrv" in name:
        return "measurement_decomposition"
    if "event" in name:
        return "event_placebo_response"
    if "risk" in name or "tail" in name:
        return "risk_decomposition"
    return "analytical_result"


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))
