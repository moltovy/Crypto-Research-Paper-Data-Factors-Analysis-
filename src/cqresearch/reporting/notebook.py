"""Execute the public semantic-output reproducibility notebook."""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient


def execute_reproducibility_notebook(root: Path) -> Path:
    source = root / "notebooks" / "crypto_market_dynamics_reproducibility.ipynb"
    output = root / "reports" / "crypto_market_dynamics_reproducibility.executed.ipynb"
    notebook = nbformat.read(source, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=300,
        kernel_name="python3",
        resources={"metadata": {"path": str(root)}},
        record_timing=False,
    )
    executed = client.execute()
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".ipynb.tmp")
    try:
        nbformat.write(executed, temporary)
        temporary.replace(output)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return output


__all__ = ["execute_reproducibility_notebook"]
