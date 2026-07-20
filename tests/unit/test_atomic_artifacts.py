from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from cqresearch.core.artifacts import write_csv


def test_failed_csv_write_preserves_existing_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "artifact.csv"
    target.write_text("stable\n", encoding="utf-8")

    def fail_write(self: pd.DataFrame, path: Path, **kwargs: object) -> None:
        Path(path).write_text("partial", encoding="utf-8")
        raise RuntimeError("injected write failure")

    monkeypatch.setattr(pd.DataFrame, "to_csv", fail_write)
    with pytest.raises(RuntimeError, match="injected"):
        write_csv(target, pd.DataFrame({"value": [1]}))

    assert target.read_text(encoding="utf-8") == "stable\n"
    assert not list(tmp_path.glob(".*.tmp"))


def test_csv_serialization_removes_sub_reporting_precision_noise(tmp_path: Path) -> None:
    first = tmp_path / "first.csv"
    second = tmp_path / "second.csv"
    write_csv(first, pd.DataFrame({"value": [0.0094997270842301]}))
    write_csv(second, pd.DataFrame({"value": [0.00949972708423019]}))
    assert first.read_bytes() == second.read_bytes()
    assert b"\r\n" not in first.read_bytes()
