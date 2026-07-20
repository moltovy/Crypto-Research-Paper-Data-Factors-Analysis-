"""Build the Markdown, self-contained HTML, and PDF research report."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from cqresearch.reporting.research_report import build_report

if __name__ == "__main__":
    artifacts = build_report(ROOT)
    print(f"wrote {len(artifacts)} report and QA artifacts")
