from __future__ import annotations

from pathlib import Path

from cqresearch.pipelines.build_modes import build_fingerprint, run_mode


def test_fixture_mode_is_deterministic_and_does_not_mutate_research(tmp_path: Path) -> None:
    first = run_mode("fixture", tmp_path)
    second = run_mode("fixture", tmp_path)

    assert first == second
    assert first["status"] == "pass"
    assert not (tmp_path / "research").exists()


def test_build_fingerprint_ignores_text_checkout_line_endings(tmp_path: Path) -> None:
    paths = [
        tmp_path / "config" / "settings.yml",
        tmp_path / "src" / "cqresearch" / "module.py",
        tmp_path / "scripts" / "run.py",
        tmp_path / "pyproject.toml",
        tmp_path / "uv.lock",
        tmp_path / "data_local" / "raw" / "provider" / "input.csv",
    ]
    for path in paths:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"first\nsecond\n")
    first = build_fingerprint(tmp_path)
    for path in paths:
        path.write_bytes(b"first\r\nsecond\r\n")
    assert build_fingerprint(tmp_path) == first
