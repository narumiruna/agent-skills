# Atuin CLI Notes

## Single-entry delete in the TUI

- Run `atuin search -i --search-mode prefix <query>` to open the interactive search view.
- Add `--cwd <cwd>` when you know the original working directory and want a narrower review.
- Open the entry inspector with `Ctrl+O`.
- After confirming the exact row, press `Ctrl+D` to delete that one history item.

## Why this skill avoids `search --delete` for typos

- `atuin search --help` defines `--delete` as deleting anything that matches the query.
- Matching behavior depends on the selected `--search-mode` or your configured default.
- Even under `--search-mode prefix`, `search --delete` still deletes every matching row, not one chosen id.
- For typo cleanup, stay in the interactive inspector and delete the confirmed row with `Ctrl+D`.

## Global duplicate cleanup

- Preview with `atuin history dedup --dry-run --before "<before>" --dupkeep <n>`.
- If the dry run matches expectations, rerun the same command without `--dry-run`.
- `history dedup` is global across the selected history window, not a single-command delete.

## Retroactive filter cleanup

- Use `atuin history prune` only when you already have `history_filter` or `cwd_filter` rules and need to retroactively remove matching entries.
- Do not use `history prune` as a general typo or duplicate cleanup substitute.
