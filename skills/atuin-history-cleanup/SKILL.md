---
name: atuin-history-cleanup
description: Use when auditing Atuin shell history for noisy duplicates or high-confidence typo/retry pairs and when preparing safe preview-first cleanup steps without editing the SQLite database directly.
---

# Atuin History Cleanup

## Overview

Audit first, delete second. Use the bundled script to summarize duplicate pressure and high-confidence typo-like retries. For typo cleanup, prefer the transactional `cleanup-typos` command so the flow snapshots `history.db`, uploads the current host history store, deletes candidates, verifies the result, and rolls back automatically if verification fails.

Read `references/atuin-cli.md` when you need the exact delete, dedup, or prune behavior.

## Use When

- Reviewing a noisy Atuin `history.db` before removing anything.
- Estimating how much `atuin history dedup` would remove while still keeping the newest repeated entries.
- Looking for typo-like retries such as `gti status` followed by `git status`.
- Running a transactional typo cleanup with backup, verification, and rollback.
- Rechecking an Atuin cleanup plan without mutating the database directly.

## Guardrails

- Always run `atuin info` and the audit script before any destructive step.
- Treat duplicate cleanup as global. `atuin history dedup` is not a single-command delete tool.
- `atuin search --delete` is query-wide and follows Atuin's active search semantics. Do not use it manually for typo cleanup.
- `cleanup-typos` is the only approved automation path for typo deletion. It may use `atuin search --delete` only after a strict uniqueness gate; any ambiguous match must fall back to the interactive inspector path.
- `cleanup-typos` must snapshot `history.db` before deletion and delay the final remote sync until verification passes.
- Rollback is whole-database restore, not selective row restore.
- Re-confirm every destructive command immediately before running it.
- Do not delete rows directly from SQLite.
- Do not edit Atuin config as part of this skill. `history_filter` and `cwd_filter` tuning is out of scope for v1.

## Workflow

1. Resolve the active database:

```bash
atuin info
```

2. Run the audit:

```bash
uv run python skills/atuin-history-cleanup/scripts/atuin_history_cleanup.py audit
```

Useful flags:

```bash
uv run python skills/atuin-history-cleanup/scripts/atuin_history_cleanup.py audit --db-path ~/.local/share/atuin/history.db --dupkeep 3 --before now --typo-window-seconds 300 --max-typos 20
```

3. Review the `duplicates` section first.
   Use the reported `atuin history dedup --dry-run ...` command. If the dry run matches expectations, rerun the same command without `--dry-run`.

4. Review the `typos` section second and choose one path:
   Preferred transactional path:

```bash
uv run python skills/atuin-history-cleanup/scripts/atuin_history_cleanup.py cleanup-typos
```

   Useful flags:

```bash
uv run python skills/atuin-history-cleanup/scripts/atuin_history_cleanup.py cleanup-typos --db-path ~/.local/share/atuin/history.db --before now --typo-window-seconds 300 --max-typos 20 --backup-dir ~/.local/share/atuin/cleanup-backups/manual-run
```

   Manual review path:
   Start with the suggested `atuin search -i --search-mode prefix ...` preview command. The audit will also add `--cwd <cwd>` when it knows the original working directory, so review stays narrow even if your default Atuin config uses `skim` or another fuzzy mode. In the TUI inspector, use `Ctrl+O`, confirm the exact entry, then `Ctrl+D` to delete that one row.

5. Stop after the cleanup you actually verified. Do not keep expanding the scope.

## What The Audit Does

- Resolves the database path from `atuin info` unless `--db-path` is provided.
- Opens the SQLite database in read-only mode and inspects only `id`, `timestamp`, `exit`, `command`, `cwd`, `session`, and `hostname`.
- Groups duplicates by `(command, cwd, hostname)` and reports how many rows exceed `--dupkeep`.
- Emits typo review commands with an explicit `--search-mode prefix` override and never emits `atuin search --delete`.
- `cleanup-typos` first runs the same typo audit, then creates a snapshot, writes `pre_audit.json`, `plan.json`, and `post_verify.json`, and only commits the deletion to remote sync after verification succeeds.
- Detects typo candidates only when all of these are true:
  - same session
  - within the configured window
  - arguments after the first token are identical
  - previous command exited non-zero
  - the first token looks rare
  - the corrected token is much more common
  - the token change is a single-edit or adjacent-transposition typo
- Excludes path- or script-like first tokens from typo suggestions.

## Output Expectations

- `duplicates` gives one global preview/apply pair for `history dedup`.
- `typos` gives per-row review data: id, time, cwd, original command, suggested correction, reason, and shell-safe preview commands for inspector review only.
- `--format json` is preferable when another tool needs to post-process the audit.
- `cleanup-typos` prints a text summary and leaves its backup and verification artifacts in the chosen backup directory.
