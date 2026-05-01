from __future__ import annotations

import importlib.util
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "atuin_history_cleanup.py"
)
SPEC = importlib.util.spec_from_file_location("atuin_history_cleanup", MODULE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def make_entry(
    entry_id: str,
    *,
    offset_seconds: int,
    exit_code: int | None,
    command: str,
    cwd: str,
    session: str,
    hostname: str = "host",
) -> object:
    return MODULE.HistoryEntry(
        id=entry_id,
        timestamp=datetime(2026, 1, 1, tzinfo=UTC) + timedelta(seconds=offset_seconds),
        exit_code=exit_code,
        command=command,
        cwd=cwd,
        session=session,
        hostname=hostname,
    )


def test_typo_preview_uses_prefix_mode_and_cwd() -> None:
    entries = [
        make_entry(
            "1",
            offset_seconds=0,
            exit_code=127,
            command="mkdit test-ctx7",
            cwd="/tmp/project dir",
            session="session-1",
        ),
        make_entry(
            "2",
            offset_seconds=2,
            exit_code=0,
            command="mkdir test-ctx7",
            cwd="/tmp/project dir",
            session="session-1",
        ),
        make_entry(
            "3",
            offset_seconds=10,
            exit_code=0,
            command="mkdir alpha",
            cwd="/tmp/project dir",
            session="session-2",
        ),
        make_entry(
            "4",
            offset_seconds=11,
            exit_code=0,
            command="mkdir beta",
            cwd="/tmp/project dir",
            session="session-3",
        ),
        make_entry(
            "5",
            offset_seconds=12,
            exit_code=0,
            command="mkdir gamma",
            cwd="/tmp/project dir",
            session="session-4",
        ),
        make_entry(
            "6",
            offset_seconds=13,
            exit_code=0,
            command="mkdir delta",
            cwd="/tmp/project dir",
            session="session-5",
        ),
    ]

    report = MODULE.analyze_typos(entries, typo_window_seconds=300, max_typos=10)

    candidate = report["candidates"][0]
    assert (
        candidate["preview_command"]
        == "atuin search -i --search-mode prefix --cwd '/tmp/project dir' 'mkdit test-ctx7'"
    )
    assert candidate["preview_query"] == "mkdit test-ctx7"
    assert "delete_command" not in candidate
    assert "unique_preview" not in candidate
    assert "preview_match_count" not in candidate


def test_typo_preview_skips_unknown_cwd_and_text_output_has_no_apply() -> None:
    entries = [
        make_entry(
            "1",
            offset_seconds=0,
            exit_code=127,
            command="gbst",
            cwd="unknown",
            session="session-1",
        ),
        make_entry(
            "2",
            offset_seconds=1,
            exit_code=0,
            command="gst",
            cwd="unknown",
            session="session-1",
        ),
        make_entry(
            "3",
            offset_seconds=10,
            exit_code=0,
            command="gst status",
            cwd="unknown",
            session="session-2",
        ),
        make_entry(
            "4",
            offset_seconds=11,
            exit_code=0,
            command="gst diff",
            cwd="unknown",
            session="session-3",
        ),
        make_entry(
            "5",
            offset_seconds=12,
            exit_code=0,
            command="gst log",
            cwd="unknown",
            session="session-4",
        ),
        make_entry(
            "6",
            offset_seconds=13,
            exit_code=0,
            command="gst push",
            cwd="unknown",
            session="session-5",
        ),
    ]

    report = MODULE.analyze_typos(entries, typo_window_seconds=300, max_typos=10)

    candidate = report["candidates"][0]
    assert candidate["preview_command"] == "atuin search -i --search-mode prefix gbst"
    assert "--cwd" not in candidate["preview_command"]

    text = "\n".join(MODULE.format_typos_section(report))
    assert "apply:" not in text


def test_duplicates_section_keeps_dedup_apply_command() -> None:
    entries = [
        make_entry(
            str(index),
            offset_seconds=index,
            exit_code=0,
            command="gst",
            cwd="/tmp/repo",
            session=f"session-{index}",
        )
        for index in range(4)
    ]

    duplicates = MODULE.analyze_duplicates(entries, before_value="now", dupkeep=3)
    lines = MODULE.format_duplicates_section(duplicates)

    assert "- Preview: atuin history dedup --dry-run --before now --dupkeep 3" in lines
    assert "- Apply: atuin history dedup --before now --dupkeep 3" in lines
