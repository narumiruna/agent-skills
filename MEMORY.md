## GOTCHA

- `skill-creator` 的 `quick_validate.py` 需要 `PyYAML`; 在這個 repo 用 `uv run --with pyyaml python /home/narumi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>` 比直接 `uv run python` 穩定。
- 這個 sandbox 對 `~/.cache/uv` 可能是唯讀；跑 `uv run --with ...` 類的一次性工具時，先設 `UV_CACHE_DIR=/tmp/uv-cache` 比較穩。
- Codex CLI 讀本地 skills 時對 symlink 不可靠；這個 repo 的 `just` 安裝流程改成 copy/rm，不再用 `stow`。
- IMRaD 現在只保留 `skills/imrad/`; repo 內已無 `imrad-*` 舊 skill 名稱可更新。
- Python 的 project setup、quality tooling、packaging 現在都整併進 `skills/python/`; repo 內已無 `python-uv-project-setup`、`python-quality-tooling`、`python-packaging-uv` 可更新。
- Standalone uv script guidance 現在也整併進 `skills/python/`; repo 內已無 `uv-scripts` 可更新。
- Root 文件分工現在固定為 `README.md` 對外、`AGENTS.md` 對內；安裝 recipe 以 `justfile` 為準，支持的是 `install-all`/`install <skill>` 與 `clean-all`/`clean <skill>`。
- 這個 repo 的 `skills/python/` 和 `~/.codex/skills/python/` 不是同一路徑綁定；改完 repo 後要再跑 `just install python` 才會同步到 Codex 實際載入版本。

## TASTE
- `git-commit` 應依賴 repo 級 `AGENTS.md` 的 git 基線；SKILL.md 只保留 diff 到 commit message 的流程與判斷，少見 Conventional Commits 細節放在 `references/`。
