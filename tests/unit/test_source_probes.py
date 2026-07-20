from __future__ import annotations

from cqresearch.data.source_probes import _result


def test_probe_cannot_pass_when_full_history_is_forced_failed() -> None:
    result = _result(
        "demo",
        True,
        "200",
        "2020-01-01",
        "2026-06-30",
        "daily",
        "checked",
        "checked",
        "current",
        "UTC",
        "abc",
        "none_until_full_history",
        "access only",
        force_fail=True,
    )
    assert result.gate_status == "fail"


def test_failed_probe_disables_dependent_analysis() -> None:
    result = _result(
        "demo",
        False,
        "404",
        "",
        "",
        "",
        "not evaluated",
        "not evaluated",
        "not evaluated",
        "",
        "",
        "none",
        "not eligible",
    )
    assert result.gate_status == "fail"
    assert result.enabled_analysis == "none"
