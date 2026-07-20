"""Explicit local, fixture, and committed-artifact build modes."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Literal

import numpy as np
import pandas as pd
from tools.data_collection.fetch_binance_stable_core import normalize_existing_archives
from tools.data_collection.fetch_cftc_positioning import fetch_archives as normalize_cftc

from cqresearch.core.artifacts import sha256_file, write_json
from cqresearch.data.contracts import DATA_CUTOFF
from cqresearch.modeling.dependence import leave_one_out_factor, tail_dependence
from cqresearch.pipelines.final_research import build_feature_store, raw_data_root
from cqresearch.pipelines.research import check_research, run_research
from cqresearch.reporting.notebook import execute_reproducibility_notebook
from cqresearch.reporting.research_report import build_report
from cqresearch.research.root_surface import build_root_research_surface

BuildMode = Literal["local", "fixture", "artifact"]
SEED = 20260713


def run_mode(mode: BuildMode, root: Path) -> dict[str, Any]:
    if mode == "local":
        return _run_local(root)
    if mode == "fixture":
        return _run_fixture(root)
    if mode == "artifact":
        result = check_research(module="all", root=root)
        required = [
            root / "reports" / "crypto_market_dynamics_research_report.md",
            root / "reports" / "crypto_market_dynamics_research_report.html",
            root / "reports" / "crypto_market_dynamics_research_report.pdf",
            root / "reports" / "crypto_market_dynamics_reproducibility.executed.ipynb",
        ]
        missing = [path.relative_to(root).as_posix() for path in required if not path.exists()]
        if missing:
            raise FileNotFoundError(f"missing committed reporting artifacts: {missing}")
        return {"mode": mode, "checks": len(result), "status": "pass"}
    raise ValueError(f"unknown build mode: {mode}")


def _run_local(root: Path) -> dict[str, Any]:
    raw_root = raw_data_root(root)
    if not raw_root.exists() or not any(path.is_file() for path in raw_root.rglob("*")):
        raise FileNotFoundError(f"local mode requires provider data under {raw_root}")
    fingerprint = build_fingerprint(root)
    checkpoint = root / "data_local" / "cache" / "checkpoints" / f"{fingerprint}.json"
    write_json(
        checkpoint,
        {
            "status": "started",
            "mode": "local",
            "fingerprint": fingerprint,
            "seed": SEED,
            "data_cutoff": DATA_CUTOFF.date().isoformat(),
        },
    )
    normalize_existing_archives(root, raw_root / "binance")
    normalize_cftc(root, download_missing=False)
    daily, weekly, monthly = build_feature_store(root, rebuild_master=True)
    artifacts = run_research(module="all", root=root)
    notebook = execute_reproducibility_notebook(root)
    report_artifacts = build_report(root)
    provenance = {
        "schema_version": 1,
        "mode": "local",
        "fingerprint": fingerprint,
        "seed": SEED,
        "data_cutoff": DATA_CUTOFF.date().isoformat(),
        "daily_rows": len(daily),
        "weekly_rows": len(weekly),
        "monthly_rows": len(monthly),
        "research_artifacts": len(artifacts),
        "report_artifacts": len(report_artifacts),
        "executed_notebook": notebook.relative_to(root).as_posix(),
        "timestamps_excluded_from_determinism": [
            "reports/crypto_market_dynamics_research_report.pdf"
        ],
        "status": "complete",
    }
    write_json(root / "research" / "build_provenance.json", provenance)
    build_root_research_surface(root)
    write_json(checkpoint, provenance)
    return provenance


def _run_fixture(root: Path) -> dict[str, Any]:
    rng = np.random.default_rng(SEED)
    dates = pd.date_range("2021-01-01", periods=500, freq="D")
    factor = rng.normal(0, 0.02, len(dates))
    returns = pd.DataFrame(
        {
            asset: loading * factor + rng.normal(0, 0.01, len(dates))
            for asset, loading in {"BTC": 1.0, "ETH": 1.1, "XRP": 0.8, "ADA": 0.9}.items()
        },
        index=dates,
    )
    overview, loadings = leave_one_out_factor(returns)
    tails = tail_dependence(returns, quantiles=(0.05,), reps=100, sensitivity_blocks=())
    payload = {
        "mode": "fixture",
        "seed": SEED,
        "status": "pass",
        "rows": len(returns),
        "assets": returns.shape[1],
        "pc1_share": float(overview.loc[overview["component"].eq("PC1"), "variance_share"].iat[0]),
        "leave_one_out_rows": len(loadings),
        "tail_rows": len(tails),
    }
    write_json(root / "data_local" / "cache" / "fixture_smoke.json", payload)
    return payload


def build_fingerprint(root: Path) -> str:
    digest = hashlib.sha256()
    digest.update(f"seed={SEED};cutoff={DATA_CUTOFF.date().isoformat()}".encode())
    raw_root = raw_data_root(root)
    for path in sorted(item for item in raw_root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(raw_root).as_posix().encode())
        digest.update(sha256_file(path).encode())
    for base in [root / "config", root / "src" / "cqresearch", root / "scripts"]:
        for path in sorted(item for item in base.rglob("*") if item.is_file()):
            digest.update(path.relative_to(root).as_posix().encode())
            digest.update(sha256_file(path).encode())
    for path in [root / "pyproject.toml", root / "uv.lock"]:
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(sha256_file(path).encode())
    return digest.hexdigest()


__all__ = ["BuildMode", "build_fingerprint", "run_mode"]
