from __future__ import annotations

import importlib.util
import sqlite3
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
import subprocess

import pytest

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
    offset_seconds: float,
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


def make_candidate(
    entry: object, *, suggested_command: str = "git status"
) -> dict[str, object]:
    return {
        "id": entry.id,
        "timestamp": entry.timestamp.isoformat(),
        "cwd": entry.cwd,
        "original_command": entry.command,
        "previous_exit_code": entry.exit_code,
        "suggested_command": suggested_command,
    }


def create_history_db(path: Path, ids: list[str]) -> None:
    connection = sqlite3.connect(path)
    try:
        connection.execute("CREATE TABLE history (id TEXT PRIMARY KEY)")
        connection.executemany(
            "INSERT INTO history (id) VALUES (?)", [(entry_id,) for entry_id in ids]
        )
        connection.commit()
    finally:
        connection.close()


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


def test_parse_cli_args_supports_cleanup_typos() -> None:
    args = MODULE.parse_cli_args(
        [
            "cleanup-typos",
            "--before",
            "now",
            "--max-typos",
            "5",
            "--backup-dir",
            "/tmp/backup",
        ]
    )

    assert args.command == "cleanup-typos"
    assert args.before == "now"
    assert args.max_typos == 5
    assert args.backup_dir == "/tmp/backup"


def test_cleanup_plan_uses_fast_path_for_unique_match() -> None:
    typo_entry = make_entry(
        "1",
        offset_seconds=0,
        exit_code=127,
        command="mkdit test-ctx7",
        cwd="/tmp/project",
        session="session-1",
    )
    corrected_entry = make_entry(
        "2",
        offset_seconds=2,
        exit_code=0,
        command="mkdir test-ctx7",
        cwd="/tmp/project",
        session="session-1",
    )

    plan = MODULE.build_cleanup_plan(
        [make_candidate(typo_entry, suggested_command=corrected_entry.command)],
        [typo_entry, corrected_entry],
    )

    item = plan[0]
    assert item["route"] == "fast"
    assert item["match_ids"] == ["1"]
    assert item["move_up"] == 0
    assert item["command_parts"][:6] == [
        "atuin",
        "search",
        "--delete",
        "--filter-mode",
        "global",
        "--search-mode",
    ]
    assert "--cwd" in item["command_parts"]
    assert "--exit" in item["command_parts"]


def test_cleanup_plan_falls_back_to_interactive_for_prefix_collision() -> None:
    typo_entry = make_entry(
        "1",
        offset_seconds=0,
        exit_code=-1,
        command="fishb",
        cwd="unknown",
        session="session-1",
    )
    colliding_entry = make_entry(
        "2",
        offset_seconds=0.5,
        exit_code=-1,
        command="fishbg",
        cwd="unknown",
        session="session-2",
    )
    corrected_entry = make_entry(
        "3",
        offset_seconds=1,
        exit_code=0,
        command="fish",
        cwd="unknown",
        session="session-1",
    )

    plan = MODULE.build_cleanup_plan(
        [make_candidate(typo_entry, suggested_command=corrected_entry.command)],
        [typo_entry, colliding_entry, corrected_entry],
    )

    item = plan[0]
    assert item["route"] == "interactive"
    assert item["match_ids"] == ["1", "2"]
    assert item["move_up"] == 1
    assert item["command_parts"][2:7] == [
        "-i",
        "--filter-mode",
        "global",
        "--search-mode",
        "prefix",
    ]


def test_verify_cleanup_result_rejects_unexpected_removed_ids(tmp_path: Path) -> None:
    snapshot_db = tmp_path / "history-before.db"
    live_db = tmp_path / "history-live.db"
    create_history_db(snapshot_db, ["1", "2", "3"])
    create_history_db(live_db, ["3"])

    with pytest.raises(MODULE.AuditError) as excinfo:
        MODULE.verify_cleanup_result(
            snapshot_db,
            live_db,
            target_ids=["1"],
            post_audit={"typos": {"candidate_count": 0}},
        )

    assert "unexpected_removed_ids=['2']" in str(excinfo.value)


def test_verify_cleanup_result_allows_concurrent_added_ids(tmp_path: Path) -> None:
    snapshot_db = tmp_path / "history-before.db"
    live_db = tmp_path / "history-live.db"
    create_history_db(snapshot_db, ["target", "existing"])
    create_history_db(live_db, ["existing", "concurrent"])

    result = MODULE.verify_cleanup_result(
        snapshot_db,
        live_db,
        target_ids=["target"],
        post_audit={"typos": {"candidate_count": 0}},
    )

    assert result == {
        "removed_ids": ["target"],
        "added_ids": ["concurrent"],
        "target_ids": ["target"],
    }


def test_rollback_preserves_live_database_without_concurrent_rows(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    snapshot_db = tmp_path / "history-before.db"
    live_db = tmp_path / "history-live.db"
    create_history_db(snapshot_db, ["deleted", "existing"])
    create_history_db(live_db, ["existing"])

    commands: list[list[str]] = []
    monkeypatch.setattr(
        MODULE.transactional,
        "run_cli_command",
        lambda parts, **kwargs: commands.append(parts),
    )

    warnings = MODULE.rollback_cleanup(snapshot_db, live_db)

    assert MODULE.read_history_ids(live_db) == {"existing"}
    assert commands == []
    assert warnings == [
        "Skipped automatic whole-database rollback to avoid racing with concurrent "
        "history writes; the live database and backup were preserved for manual "
        "recovery."
    ]


def test_rollback_preserves_concurrent_history_rows(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    snapshot_db = tmp_path / "history-before.db"
    live_db = tmp_path / "history-live.db"
    create_history_db(snapshot_db, ["existing"])
    create_history_db(live_db, ["existing", "concurrent"])

    commands: list[list[str]] = []
    monkeypatch.setattr(
        MODULE.transactional,
        "run_cli_command",
        lambda parts, **kwargs: commands.append(parts),
    )

    warnings = MODULE.rollback_cleanup(snapshot_db, live_db)

    assert MODULE.read_history_ids(live_db) == {"existing", "concurrent"}
    assert commands == []
    assert warnings == [
        "Skipped automatic whole-database rollback to avoid racing with concurrent "
        "history writes; the live database and backup were preserved for manual "
        "recovery."
    ]


def test_cleanup_typos_runs_transactional_flow(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    history_db = tmp_path / "history.db"
    create_history_db(history_db, ["1", "2"])
    backup_dir = tmp_path / "backup"

    pre_audit = {
        "db_path": str(history_db),
        "typos": {
            "candidate_count": 2,
            "returned_count": 2,
            "candidates": [
                {
                    "id": "1",
                    "timestamp": "2026-01-01T00:00:00+00:00",
                    "cwd": "unknown",
                    "original_command": "cdoex",
                    "previous_exit_code": 127,
                },
                {
                    "id": "2",
                    "timestamp": "2026-01-01T00:00:01+00:00",
                    "cwd": "unknown",
                    "original_command": "gbst",
                    "previous_exit_code": 127,
                },
            ],
        },
    }
    post_audit = {
        "db_path": str(history_db),
        "typos": {"candidate_count": 0, "returned_count": 0, "candidates": []},
    }
    audit_reports = [pre_audit, post_audit]

    monkeypatch.setattr(
        MODULE, "audit_history", lambda *args, **kwargs: audit_reports.pop(0)
    )
    monkeypatch.setattr(
        MODULE,
        "get_remote_sync_status",
        lambda: {"address": "https://api.atuin.sh", "username": "narumi"},
    )
    monkeypatch.setattr(MODULE, "get_current_host_uuid", lambda: "host-uuid")
    monkeypatch.setattr(
        MODULE, "load_history_entries", lambda *args, **kwargs: ([], {})
    )
    monkeypatch.setattr(
        MODULE,
        "build_cleanup_plan",
        lambda candidates, entries: [
            {
                "id": "1",
                "route": "fast",
                "command_parts": ["atuin", "search", "--delete", "cdoex"],
            },
            {
                "id": "2",
                "route": "interactive",
                "command_parts": ["atuin", "search", "-i", "gbst"],
            },
        ],
    )
    monkeypatch.setattr(
        MODULE,
        "execute_cleanup_plan",
        lambda plan: {"fast_count": 1, "interactive_count": 1},
    )
    monkeypatch.setattr(
        MODULE,
        "verify_cleanup_result",
        lambda *args, **kwargs: {
            "removed_ids": ["1", "2"],
            "added_ids": [],
            "target_ids": ["1", "2"],
        },
    )

    commands: list[list[str]] = []

    def fake_run(
        parts: list[str], **kwargs: object
    ) -> subprocess.CompletedProcess[str]:
        commands.append(parts)
        return subprocess.CompletedProcess(parts, 0, stdout="", stderr="")

    monkeypatch.setattr(MODULE, "run_cli_command", fake_run)

    result = MODULE.cleanup_typos(
        None,
        before="now",
        typo_window_seconds=300,
        max_typos=20,
        backup_dir=str(backup_dir),
    )

    assert result["status"] == "success"
    assert result["fast_count"] == 1
    assert result["interactive_count"] == 1
    assert commands == [
        ["atuin", "store", "push", "--tag", "history", "--host", "host-uuid"],
        ["atuin", "sync"],
    ]
    assert (backup_dir / "history.db.before").exists()
    assert (backup_dir / "pre_audit.json").exists()
    assert (backup_dir / "plan.json").exists()
    assert (backup_dir / "post_verify.json").exists()


def test_cleanup_typos_rolls_back_after_verification_failure(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    history_db = tmp_path / "history.db"
    create_history_db(history_db, ["1"])
    backup_dir = tmp_path / "backup"

    pre_audit = {
        "db_path": str(history_db),
        "typos": {
            "candidate_count": 1,
            "returned_count": 1,
            "candidates": [
                {
                    "id": "1",
                    "timestamp": "2026-01-01T00:00:00+00:00",
                    "cwd": "unknown",
                    "original_command": "cdoex",
                    "previous_exit_code": 127,
                },
            ],
        },
    }
    post_audit = {
        "db_path": str(history_db),
        "typos": {
            "candidate_count": 1,
            "returned_count": 1,
            "candidates": pre_audit["typos"]["candidates"],
        },
    }
    audit_reports = [pre_audit, post_audit]

    monkeypatch.setattr(
        MODULE, "audit_history", lambda *args, **kwargs: audit_reports.pop(0)
    )
    monkeypatch.setattr(
        MODULE,
        "get_remote_sync_status",
        lambda: {"address": "https://api.atuin.sh", "username": "narumi"},
    )
    monkeypatch.setattr(MODULE, "get_current_host_uuid", lambda: "host-uuid")
    monkeypatch.setattr(
        MODULE, "load_history_entries", lambda *args, **kwargs: ([], {})
    )
    monkeypatch.setattr(
        MODULE,
        "build_cleanup_plan",
        lambda candidates, entries: [
            {
                "id": "1",
                "route": "fast",
                "command_parts": ["atuin", "search", "--delete", "cdoex"],
            },
        ],
    )
    monkeypatch.setattr(
        MODULE,
        "execute_cleanup_plan",
        lambda plan: {"fast_count": 1, "interactive_count": 0},
    )
    monkeypatch.setattr(
        MODULE,
        "verify_cleanup_result",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            MODULE.AuditError("verification failed")
        ),
    )
    monkeypatch.setattr(
        MODULE,
        "run_cli_command",
        lambda parts, **kwargs: subprocess.CompletedProcess(
            parts, 0, stdout="", stderr=""
        ),
    )

    rollback_calls: list[tuple[Path, Path]] = []

    def fake_rollback(snapshot: Path, live: Path) -> list[str]:
        rollback_calls.append((snapshot, live))
        return []

    monkeypatch.setattr(MODULE, "rollback_cleanup", fake_rollback)

    with pytest.raises(MODULE.AuditError) as excinfo:
        MODULE.cleanup_typos(
            None,
            before="now",
            typo_window_seconds=300,
            max_typos=20,
            backup_dir=str(backup_dir),
        )

    assert "verification failed" in str(excinfo.value)
    assert f"Backup dir: {backup_dir}" in str(excinfo.value)
    assert rollback_calls == [(backup_dir / "history.db.before", history_db)]
