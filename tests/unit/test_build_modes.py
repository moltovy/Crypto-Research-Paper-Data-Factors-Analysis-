from __future__ import annotations

from pathlib import Path

from cqresearch.pipelines.build_modes import run_mode


def test_fixture_mode_is_deterministic_and_does_not_mutate_research(tmp_path: Path) -> None:
    first = run_mode("fixture", tmp_path)
    second = run_mode("fixture", tmp_path)

    assert first == second
    assert first["status"] == "pass"
    assert not (tmp_path / "research").exists()
