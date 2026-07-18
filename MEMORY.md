## GOTCHA

- Symptom: recursively downloading Apple HIG HTML misses the navigator and article source. Cause: the site is a DocC SPA whose complete tree and content live under `/tutorials/data/`. Fix: enumerate `/tutorials/data/index/design--human-interface-guidelines`, then download each indexed page JSON and its resource references.
- Symptom: `skill-creator`'s `quick_validate.py` raises `ModuleNotFoundError: yaml` even with `uv run --with pyyaml` under the default Python 3.14. Cause: that one-off environment did not inject PyYAML. Fix: run `UV_CACHE_DIR=/tmp/uv-cache uv run --no-project --python 3.13 --with pyyaml python "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" <skill-dir>`.
- `skill-creator`'s `init_skill.py` creates the target skill directory and `SKILL.md` before it validates `agents/openai.yaml` metadata, so a bad `--interface short_description` can leave a partially initialized skill directory behind.
- In this sandbox, `~/.cache/uv` may be read-only; when running one-off `uv run --with ...` tools, set `UV_CACHE_DIR=/tmp/uv-cache` first for more reliable behavior.
- In this sandbox, the first run of skill metadata tools like `uv run --with pyyaml` may still need temporary network access if the local cache does not already contain the package, so `uv` can fetch `PyYAML`.
- Codex CLI is unreliable with symlinks when loading local skills; this repo's `just` install flow now uses copy/rm instead of `stow`.
- IMRaD now only lives under `skills/writing-research/applying-imrad/`; there are no remaining `imrad-*` legacy skill names in the repo to update.
- Root document ownership is now fixed as `README.md` for external-facing docs and `AGENTS.md` for maintainer-facing docs; treat `justfile` as the source of truth for install recipes, with `install-all`/`install <skill>` and `clean-all`/`clean <skill>` as the supported commands.
- `atuin search --delete` deletes every history row matching the query under the active search semantics; do not treat preview uniqueness or local substring counts as proof of single-row safety.
- `atuin search -i` can panic inside Codex's filesystem sandbox because Atuin fails to create its log file on a read-only path; run interactive inspector deletions with escalated permissions.
- For Atuin cleanup automation, snapshot `history.db` with SQLite's backup API instead of a raw file copy so live-database state and WAL pages stay consistent.

## TASTE
- Prefer applying Apple-derived design philosophy across platforms while translating platform-specific metrics and controls to target conventions; minimize cognitive load without sacrificing functional completeness, keep critical actions and state visible, and use predictable progressive disclosure for secondary complexity.
- Prefer preserving a skill's original user intent when naming or renaming skills; do not force `<verb-ing>-<object>` if it changes the meaning.
- `writing-git-commits` should rely on the repo-level `AGENTS.md` for the Git baseline; `SKILL.md` should keep only the flow and judgment from diff to commit message, while less common Conventional Commits details belong in `references/`.
- `maintaining-memory-md` should check at conversation start without creating `MEMORY.md` merely because it is missing; when the first qualifying `GOTCHA` or durable `TASTE` emerges, it should create the repository-root file without extra confirmation and revise stale or similar entries in place.
