"""Run metadata-only eligibility probes for optional official sources."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from cqresearch.data.source_probes import run_source_probes

if __name__ == "__main__":
    results = run_source_probes(ROOT)
    print(results[["source_id", "gate_status", "enabled_analysis"]].to_string(index=False))
