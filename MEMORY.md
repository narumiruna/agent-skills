## GOTCHA

- `skill-creator` 的 `quick_validate.py` 需要 `PyYAML`; 在這個 repo 用 `uv run --with pyyaml python /home/narumi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>` 比直接 `uv run python` 穩定。
- 這個 sandbox 對 `~/.cache/uv` 可能是唯讀；跑 `uv run --with ...` 類的一次性工具時，先設 `UV_CACHE_DIR=/tmp/uv-cache` 比較穩。
- IMRaD 現在只保留 `skills/imrad/`; repo 內已無 `imrad-*` 舊 skill 名稱可更新。
- Python 的 project setup、quality tooling、packaging 現在都整併進 `skills/python/`; repo 內已無 `python-uv-project-setup`、`python-quality-tooling`、`python-packaging-uv` 可更新。
- Standalone uv script guidance 現在也整併進 `skills/python/`; repo 內已無 `uv-scripts` 可更新。

## TASTE
