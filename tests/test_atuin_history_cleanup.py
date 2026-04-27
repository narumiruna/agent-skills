from __future__ import annotations

import importlib.util
import sqlite3
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "atuin-history-cleanup"
    / "scripts"
    / "atuin_history_cleanup.py"
)

SPEC = importlib.util.spec_from_file_location(
    "atuin_history_cleanup_script", SCRIPT_PATH
)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def iso_at(offset_seconds: int) -> str:
    base = datetime(2026, 4, 1, 8, 0, 0, tzinfo=UTC)
    return (base + timedelta(seconds=offset_seconds)).isoformat()


def row(
    row_id: str,
    offset_seconds: int,
    exit_code: int,
    command: str,
    cwd: str = "/repo",
    session: str = "session-1",
    hostname: str = "host-1",
) -> tuple[str, str, int, str, str, str, str]:
    return (
        row_id,
        iso_at(offset_seconds),
        exit_code,
        command,
        cwd,
        session,
        hostname,
    )


def write_history_db(
    tmp_path: Path,
    rows: list[tuple[str, str, int, str, str, str, str]],
) -> Path:
    db_path = tmp_path / "history.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute(
            """
            CREATE TABLE history (
                id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                exit INTEGER,
                command TEXT NOT NULL,
                cwd TEXT NOT NULL,
                session TEXT,
                hostname TEXT
            )
            """
        )
        connection.executemany(
            """
            INSERT INTO history (id, timestamp, exit, command, cwd, session, hostname)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )
        connection.commit()
    finally:
        connection.close()
    return db_path


def run_audit(db_path: Path, **overrides: object) -> dict[str, Any]:
    kwargs: dict[str, object] = {
        "dupkeep": 3,
        "before": "now",
        "typo_window_seconds": 300,
        "max_typos": 20,
    }
    kwargs.update(overrides)
    return MODULE.audit_history(db_path, **kwargs)


def test_duplicate_groups_report_global_dedup_preview(tmp_path: Path) -> None:
    db_path = write_history_db(
        tmp_path,
        [
            row("dup-1", 0, 0, "git status"),
            row("dup-2", 30, 0, "git status"),
            row("dup-3", 60, 0, "git status"),
            row("dup-4", 90, 0, "git status"),
            row("dup-5", 120, 0, "git status"),
            row("other-1", 150, 0, "git pull"),
        ],
    )

    report = run_audit(db_path)

    duplicates = report["duplicates"]
    assert duplicates["group_count"] == 1
    assert duplicates["deletable_count"] == 2
    assert duplicates["groups"][0]["command"] == "git status"
    assert (
        duplicates["preview_command"]
        == "atuin history dedup --dry-run --before now --dupkeep 3"
    )
    assert duplicates["apply_command"] == "atuin history dedup --before now --dupkeep 3"


def test_typo_retry_candidate_is_detected(tmp_path: Path) -> None:
    db_path = write_history_db(
        tmp_path,
        [
            row("git-1", 0, 0, "git branch", session="freq-1"),
            row("git-2", 30, 0, "git status", session="freq-2"),
            row("git-3", 60, 0, "git add .", session="freq-3"),
            row("git-4", 90, 0, "git diff", session="freq-4"),
            row("git-5", 120, 0, "git log --oneline", session="freq-5"),
            row("git-6", 150, 0, "git fetch", session="freq-6"),
            row("typo-1", 300, 127, "gti status", session="repair"),
            row("typo-2", 320, 0, "git status", session="repair"),
        ],
    )

    report = run_audit(db_path)

    typos = report["typos"]
    assert typos["candidate_count"] == 1
    candidate = typos["candidates"][0]
    assert candidate["original_command"] == "gti status"
    assert candidate["suggested_command"] == "git status"
    assert candidate["time_delta_seconds"] == 20
    assert candidate["delete_command"] == "atuin search --delete 'gti status'"
    assert "previous exit 127" in candidate["reason"]


def test_non_typo_tool_switch_is_not_reported(tmp_path: Path) -> None:
    db_path = write_history_db(
        tmp_path,
        [
            row("eza-1", 0, 0, "eza .", session="freq-1"),
            row("eza-2", 30, 0, "eza -la", session="freq-2"),
            row("eza-3", 60, 0, "eza src", session="freq-3"),
            row("eza-4", 90, 0, "eza docs", session="freq-4"),
            row("eza-5", 120, 0, "eza tests", session="freq-5"),
            row("eza-6", 150, 0, "eza .git", session="freq-6"),
            row("switch-1", 300, 1, "exa .", session="repair"),
            row("switch-2", 315, 0, "eza .", session="repair"),
        ],
    )

    report = run_audit(db_path)

    assert report["typos"]["candidate_count"] == 0
    assert report["typos"]["candidates"] == []


def test_path_like_tokens_are_excluded(tmp_path: Path) -> None:
    db_path = write_history_db(
        tmp_path,
        [
            row("script-1", 0, 0, "./build.sh release", session="freq-1"),
            row("script-2", 30, 0, "./build.sh test", session="freq-2"),
            row("script-3", 60, 0, "./build.sh lint", session="freq-3"),
            row("script-4", 90, 0, "./build.sh docs", session="freq-4"),
            row("script-5", 120, 0, "./build.sh clean", session="freq-5"),
            row("script-6", 150, 0, "./build.sh package", session="freq-6"),
            row("repair-1", 300, 1, "./buid.sh release", session="repair"),
            row("repair-2", 320, 0, "./build.sh release", session="repair"),
        ],
    )

    report = run_audit(db_path)

    assert report["typos"]["candidate_count"] == 0
    assert report["typos"]["candidates"] == []


def test_shell_quoting_is_preserved_for_cwd_and_query(tmp_path: Path) -> None:
    weird_cwd = "/tmp/My Project/(draft)[$HOME]"
    db_path = write_history_db(
        tmp_path,
        [
            row("git-1", 0, 0, "git branch", cwd=weird_cwd, session="freq-1"),
            row("git-2", 30, 0, "git status", cwd=weird_cwd, session="freq-2"),
            row("git-3", 60, 0, "git add .", cwd=weird_cwd, session="freq-3"),
            row("git-4", 90, 0, "git diff", cwd=weird_cwd, session="freq-4"),
            row("git-5", 120, 0, "git log --oneline", cwd=weird_cwd, session="freq-5"),
            row("git-6", 150, 0, "git fetch", cwd=weird_cwd, session="freq-6"),
            row(
                "quote-1",
                300,
                1,
                "gti commit --amend --no-edit",
                cwd=weird_cwd,
                session="repair",
            ),
            row(
                "quote-2",
                315,
                0,
                "git commit --amend --no-edit",
                cwd=weird_cwd,
                session="repair",
            ),
        ],
    )

    report = run_audit(db_path)
    candidate = report["typos"]["candidates"][0]

    assert candidate["cwd_shell_quoted"] == "'/tmp/My Project/(draft)[$HOME]'"
    assert candidate["cd_command"] == "cd '/tmp/My Project/(draft)[$HOME]'"
    assert (
        candidate["preview_command"] == "atuin search -i 'gti commit --amend --no-edit'"
    )
    assert (
        candidate["delete_command"]
        == "atuin search --delete 'gti commit --amend --no-edit'"
    )
