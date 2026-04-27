# Atuin CLI Notes

## Single-entry delete in the TUI

- Run `atuin search -i <query>` to open the interactive search view.
- Open the entry inspector with `Ctrl+O`.
- After confirming the exact row, press `Ctrl+D` to delete that one history item.

## Batch delete after preview

- Start with `atuin search -i <query>` so you can preview what the query matches.
- If the preview is clearly scoped, rerun it as `atuin search --delete <query>`.
- Keep the preview and apply commands adjacent so deletion stays review-first.

## Global duplicate cleanup

- Preview with `atuin history dedup --dry-run --before "<before>" --dupkeep <n>`.
- If the dry run matches expectations, rerun the same command without `--dry-run`.
- `history dedup` is global across the selected history window, not a single-command delete.

## Retroactive filter cleanup

- Use `atuin history prune` only when you already have `history_filter` or `cwd_filter` rules and need to retroactively remove matching entries.
- Do not use `history prune` as a general typo or duplicate cleanup substitute.
