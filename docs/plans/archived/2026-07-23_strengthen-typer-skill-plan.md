## Goal

Strengthen `building-typer-clis` with current, official Typer guidance that protects command grammar, modern parameter declarations, callbacks and completion, runtime exits, testing behavior, and installed entry points without bloating the core skill.

## Context

- The existing trigger is useful, but the body mainly provides a basic greeting example and generic CLI advice.
- Official Typer documentation and release notes currently show Typer 0.27.0, recommend `Annotated`, require explicit `add_typer(..., name=...)` group names, dropped `typer-slim`/`typer-cli`, vendored Click in 0.26.0, and changed current testing compatibility surfaces.
- The official Typer repository also ships an agent skill whose current rules corroborate the installation, `Annotated`, explicit app, and vendored-Click guidance.

## Plan

- [x] Create branch `feat/strengthen-typer-skill` from clean, fast-forwarded `main`; verified at `f22e9e8` after PR #99 merged.
- [x] Research the official Typer tutorial, API reference, release notes, and official agent skill; verified current command-shape, parameter, callback/completion, packaging, testing, and compatibility behavior against `https://typer.tiangolo.com/` and `fastapi/typer`.
- [x] Add focused regression expectations for the strengthened trigger, lean routing workflow, command-grammar and modern-API safeguards, justified references, and aligned metadata/catalog; verified the focused test failed because the current basic skill had no Typer reference set.
- [x] Rewrite the core skill around Typer-specific decisions and add focused architecture, parameter/runtime, testing, and packaging/completion references with official source links; verified command shape, `Annotated`, `BadParameter`, current `CliRunner`, `[project.scripts]`, installed execution, help, and wheel build against Typer 0.27.0.
- [x] Run all repository validation gates, inspect the final diff and branch state, obtain independent review, and archive this completed plan with evidence; verified the changed skill passed `quick_validate.py`, 89/89 tests passed, all `prek run -a` hooks passed, `git diff --check` passed, and final independent re-review found no issue after its three correctness findings were fixed.

## Risks

- Typer evolves quickly; keep version-sensitive details in references, require inspection of the declared version, and link release notes rather than hard-coding latest behavior as universally compatible.
- Adding commands or callbacks can silently change `PROGRAM ...` into `PROGRAM COMMAND ...`; make public invocation grammar an explicit invariant and regression assertion.
- Typer 0.26 vendored Click and simplified `CliRunner`; avoid stale Click extension, `mix_stderr`, and filesystem-runner guidance.
- More documentation can recreate the prompt bloat this repository removed; keep only routing and invariants in `SKILL.md` and load detailed references on demand.

## Completion Checklist

- [x] `building-typer-clis` provides substantial Typer-specific value beyond a basic framework example while remaining lean and trigger-aligned; verified a 37-line routed core replaces the generic minimal pattern and aligns frontmatter, metadata, and README.
- [x] References cover application shape, typed parameters/runtime, current testing, and packaging/completion with official source URLs and no obsolete package/API advice; verified by focused assertions, link checks, and independent review.
- [x] Representative current-Typer examples and regression assertions prove the highest-risk guidance; verified live against Typer 0.27.0 for command promotion, `add_typer`, callbacks, `Annotated`, `default_factory`, `BadParameter`, no-command modes, current `CliRunner`, installed scripts, help, and wheel builds.
- [x] Skill validation, full pytest, `prek run -a`, and `git diff --check` pass on `feat/strengthen-typer-skill`; verified one valid changed skill, 89 passing tests, all hooks passing, and a clean diff check.
