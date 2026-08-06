## Goal

Refine `using-codebase-memory-cli` into a lean, accurate, and operationally safe skill whose trigger, workflow, command reference, catalog entry, and validation evidence agree with the installed CLI and current repository guidance.

## Plan

- [x] Audit the current skill, command reference, catalog, repository conventions, GPT-5.6 prompt guidance, installed `codebase-memory-mcp` help, and upstream documentation; verified against v0.9.0 help/release docs and live `skills`/`pi` output, exposing cache-vs-artifact ambiguity, contradictory temporary-index cleanup, unreported mode/freshness limits, broad semantic-result behavior, and an over-eager installer path.
- [x] Revise `SKILL.md` so graph-first routing, index freshness, evidence escalation, fallbacks, mutation boundaries, and completion reporting are discriminating and non-duplicative; verified by direct diff audit against the trigger, safety, and completion criteria.
- [x] Revise `references/commands.md` with version-qualified, help-verified command shapes and only the operational details worth loading on demand; verified every documented flag against v0.9.0 help or live output, while the existing README catalog remains accurately aligned without an edit.
- [x] Forward-test representative index, search, trace/snippet, literal-search, architecture/schema, and change-impact paths without starting an MCP server; verified on `~/workspace/pi` and a task-scoped fast index of this repository, then deleted `skills-refine-cbm-cli-20260806` and confirmed it was absent from `list_projects`.
- [x] Validate frontmatter, links, formatting, repository gates, diff scope, and instruction consistency; verified the target with `quick_validate.py`, `just`, relative-link validation, `prek run -a`, `git diff --check`, final file/diff audit, catalog comparison, and temporary-index absence.

## Risks

- Version-sensitive flags or schemas may drift; mitigate by distinguishing installed-help evidence from upstream guidance and requiring runtime help checks.
- Aggressive shortening may remove a safety or evidence invariant; mitigate with a requirement-by-requirement final audit and representative CLI execution.
- Indexing creates local tool state; use a clearly task-scoped project identity and delete it after validation.

## Completion Checklist

- [x] Trigger metadata clearly distinguishes graph discovery from literal/configuration search and from unavailable-CLI fallback.
- [x] Every command and behavioral claim is supported by installed help, representative output, or explicitly qualified upstream evidence.
- [x] Local indexing and external/destructive/persistent operations have precise autonomy and approval boundaries.
- [x] `SKILL.md`, its reference, and README catalog are aligned, lean, and free of stale or duplicate guidance.
- [x] `prek run -a`, `git diff --check`, relative-link validation, and representative CLI checks pass with no task-only index left behind.
