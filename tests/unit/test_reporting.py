from __future__ import annotations

from pathlib import Path

import fitz
import nbformat

ROOT = Path(__file__).resolve().parents[2]


def test_executed_notebook_has_outputs_and_no_errors() -> None:
    path = ROOT / "reports" / "crypto_market_dynamics_reproducibility.executed.ipynb"
    assert path.exists()
    assert b"\r\n" not in path.read_bytes()
    notebook = nbformat.read(path, as_version=4)
    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    assert all(cell.execution_count is not None for cell in code_cells)
    assert not [
        output for cell in code_cells for output in cell.outputs if output.output_type == "error"
    ]


def test_report_pdf_is_nonempty_and_multipage() -> None:
    path = ROOT / "reports" / "crypto_market_dynamics_research_report.pdf"
    assert path.exists() and path.stat().st_size > 100_000
    document = fitz.open(path)
    assert document.page_count >= 7
    assert all(len(page.get_text().strip()) > 100 for page in document)


def test_report_market_structure_formula_matches_implemented_estimands() -> None:
    text = (ROOT / "reports" / "crypto_market_dynamics_research_report.md").read_text(
        encoding="utf-8"
    )
    assert "entropy breadth `= exp(" in text
    assert "turnover `= (entries + exits) / size(union of adjacent memberships)`" in text
    assert "effective count `= 1 / HHI" not in text
