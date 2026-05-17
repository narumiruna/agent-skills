## GOTCHA

- `skill-creator`'s `quick_validate.py` requires `PyYAML`; in this repo, `uv run --with pyyaml python /home/narumi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>` is more reliable than plain `uv run python`.
- `skill-creator`'s `init_skill.py` creates the target skill directory and `SKILL.md` before it validates `agents/openai.yaml` metadata, so a bad `--interface short_description` can leave a partially initialized skill directory behind.
- In this sandbox, `~/.cache/uv` may be read-only; when running one-off `uv run --with ...` tools, set `UV_CACHE_DIR=/tmp/uv-cache` first for more reliable behavior.
- In this sandbox, the first run of skill metadata tools like `uv run --with pyyaml` may still need temporary network access if the local cache does not already contain the package, so `uv` can fetch `PyYAML`.
- Codex CLI is unreliable with symlinks when loading local skills; this repo's `just` install flow now uses copy/rm instead of `stow`.
- IMRaD now only lives under `skills/imrad/`; there are no remaining `imrad-*` legacy skill names in the repo to update.
- Root document ownership is now fixed as `README.md` for external-facing docs and `AGENTS.md` for maintainer-facing docs; treat `justfile` as the source of truth for install recipes, with `install-all`/`install <skill>` and `clean-all`/`clean <skill>` as the supported commands.
- `atuin search --delete` deletes every history row matching the query under the active search semantics; do not treat preview uniqueness or local substring counts as proof of single-row safety.
- `atuin search -i` can panic inside Codex's filesystem sandbox because Atuin fails to create its log file on a read-only path; run interactive inspector deletions with escalated permissions.
- For Atuin cleanup automation, snapshot `history.db` with SQLite's backup API instead of a raw file copy so live-database state and WAL pages stay consistent.

## TASTE
- `git-commit` should rely on the repo-level `AGENTS.md` for the Git baseline; `SKILL.md` should keep only the flow and judgment from diff to commit message, while less common Conventional Commits details belong in `references/`.
- `memory-md` should trigger at the start of repository conversations, record repeatable mistakes as `GOTCHA`, correct wrong or stale memory entries in place, and store durable user preferences under `TASTE`.
