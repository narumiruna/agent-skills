## GOTCHA

- `skill-creator`'s `quick_validate.py` requires `PyYAML`; in this repo, `uv run --with pyyaml python /home/narumi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>` is more reliable than plain `uv run python`.
- In this sandbox, `~/.cache/uv` may be read-only; when running one-off `uv run --with ...` tools, set `UV_CACHE_DIR=/tmp/uv-cache` first for more reliable behavior.
- In this sandbox, the first run of skill metadata tools like `uv run --with pyyaml` may still need temporary network access if the local cache does not already contain the package, so `uv` can fetch `PyYAML`.
- Codex CLI is unreliable with symlinks when loading local skills; this repo's `just` install flow now uses copy/rm instead of `stow`.
- IMRaD now only lives under `skills/imrad/`; there are no remaining `imrad-*` legacy skill names in the repo to update.
- Python project setup, quality tooling, and packaging are now consolidated into `skills/python/`; there are no remaining `python-uv-project-setup`, `python-quality-tooling`, or `python-packaging-uv` skills in the repo to update.
- Typer CLI guidance now lives under `skills/python-typer/`; use that name consistently across repo docs and prompts.
- Standalone uv script guidance is also consolidated into `skills/python/`; there is no remaining `uv-scripts` skill in the repo to update.
- Root document ownership is now fixed as `README.md` for external-facing docs and `AGENTS.md` for maintainer-facing docs; treat `justfile` as the source of truth for install recipes, with `install-all`/`install <skill>` and `clean-all`/`clean <skill>` as the supported commands.
- `skills/python/` in this repo and `~/.codex/skills/python/` are not the same bound path; after changing the repo copy, run `just install python` again to sync the version Codex actually loads.
- `atuin search --delete` deletes every history row matching the query under the active search semantics; do not treat preview uniqueness or local substring counts as proof of single-row safety.

## TASTE
- `git-commit` should rely on the repo-level `AGENTS.md` for the Git baseline; `SKILL.md` should keep only the flow and judgment from diff to commit message, while less common Conventional Commits details belong in `references/`.
