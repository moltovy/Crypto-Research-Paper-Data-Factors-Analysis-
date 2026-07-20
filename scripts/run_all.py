"""Run the canonical local build, fixture smoke, or artifact validation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from cqresearch.pipelines.build_modes import run_mode


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["local", "fixture", "artifact"], default="artifact")
    args = parser.parse_args()
    result = run_mode(args.mode, ROOT)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
