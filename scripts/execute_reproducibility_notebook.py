"""Execute the semantic-output reproducibility notebook with nbclient."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from cqresearch.reporting.notebook import execute_reproducibility_notebook

if __name__ == "__main__":
    print(execute_reproducibility_notebook(ROOT))
