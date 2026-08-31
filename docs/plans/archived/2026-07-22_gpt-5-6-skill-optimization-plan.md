## Goal

Optimize every active and deprecated skill against `./skills/writing-research/prompting-gpt/references/gpt-5.6.md`: remove repeated or low-value prompt content, keep domain-critical constraints, state approval and evidence boundaries precisely, and align each skill's metadata and catalog entry.

## Assumptions

- “All skills” includes the 28 active skills under `skills/` and the 4 deprecated skills under `deprecated/`.
- Optimization applies to `SKILL.md`, metadata, and bundled references where they duplicate guidance or contain correctness/safety defects; scripts and assets change only if verification exposes a defect.
- Shorter text counts as an improvement only when trigger quality, safety, domain invariants, and verifiability are preserved.

## Plan

- [x] Establish a guide-derived audit baseline for all 32 skills and inspect repository ownership, tests, metadata, and relevant references; verified by `find skills deprecated -name SKILL.md` (28 active, 4 deprecated), frontmatter/metadata extraction, repository tests and instructions, and a four-stream per-skill audit against `./skills/writing-research/prompting-gpt/references/gpt-5.6.md`.
- [x] Optimize Python and learning skills (`explaining-step-by-step`, `building-typer-clis`, `configuring-python-logging`, `managing-python-with-uv`, `using-peewee-orm`) and align their metadata/catalog wording; verified by diff review, a live Peewee lifecycle example, and the final repository suite (67 passed).
- [x] Optimize slide, visual, and UI skills (`authoring-marp-slides`, `creating-mermaid-diagrams`, `creating-slide-decks`, `creating-svg-illustrations`, `designing-slide-colors`, `designing-user-interfaces`) and duplicated or misleading bundled guidance; verified by diff review and final tests covering trigger alignment, inline images, false validation claims, commit authority, and resource links (67 passed).
- [x] Optimize workflow and repository skills (`applying-tdd`, `creating-agent-skills`, `hardening-code-paths`, `maintaining-memory-md`, `managing-git-worktrees`, `naming-agent-skills`, `resolving-pr-review-comments`, `reviewing-code`, `syncing-main-branch`, `using-jira-cli`, `writing-agents-md`, `writing-git-commits`) while preserving explicit-invocation and destructive/external-action boundaries; verified by diff review, 32-skill metadata validation, targeted authorization tests, and independent review. `hardening-code-paths` required no body reduction after audit.
- [x] Optimize writing and research skills (`applying-imrad`, `creating-telegraph-pages`, `grilling-designs`, `researching-gourmet-venues`, `writing-plans`) and keep evidence, publication, and completion criteria explicit; verified by diff review, catalog/metadata inventory validation, and targeted repository tests (22 passed).
- [x] Optimize deprecated skills (`building-codex-hooks`, `checking-cli-help`, `cleaning-atuin-history`, `writing-work-logs`) as concise reference skills without reactivating discovery; verified all four remain under `deprecated/`, carry `metadata.internal: true`, preserve explicit-only policy where required, and pass exact-operation boundary tests.
- [x] Add or update regression checks that enforce repository-wide prompt invariants introduced by this optimization; verified `tests/test_skill_repository.py` covers the 32-skill inventory, key semantic trigger surfaces, metadata/catalog presence, lean body headings, external/destructive authorization, logging/Peewee semantics, truthful slide validation, visual commit boundaries, and relative resource links (25 targeted tests; 67 in the full suite).
- [x] Run every documented validation gate and audit every skill against the guide-derived criteria; verified `just` listed only the non-mutating default recipes, the skill-creator validator passed all 32 directories, `UV_CACHE_DIR=/tmp/uv-cache uv run --no-project --with pytest pytest` passed 67 tests, `prek run -a` passed every hook, `git diff --check` passed, all relative Markdown links resolved, and final independent review found no remaining issue.

## Risks

- Mitigated: aggressive shortening could remove a domain invariant, approval boundary, or recovery step; canonical constraints were retained, tests cover high-risk boundaries, and an independent review rechecked its findings after fixes.
- Mitigated: metadata edits could change triggers unintentionally; all 32 frontmatter/metadata/catalog entries were compared, key semantic surfaces have regression assertions, and every skill passed validation.
- Mitigated: deprecated skills may describe version-sensitive tools; all remain internal under `deprecated/`, Codex hooks are labeled version-sensitive, and unsafe Atuin transactional automation is explicitly disabled.

## Completion Checklist

- [x] All 32 skill directories have an explicit audited disposition, verified by the 28-active/4-deprecated inventory, per-skill diff review, and independent final review.
- [x] Repetition and unnecessary prompt scaffolding are reduced without losing required constraints, verified against `./skills/writing-research/prompting-gpt/references/gpt-5.6.md`, zero generic trigger/cleanup headings, a 43.4% aggregate `SKILL.md` word reduction, and 67 passing tests.
- [x] External, destructive, public, or costly actions require precise authorization where applicable, verified by targeted assertions and independent review of PR, Jira, uv publish, Telegraph, worktree, database, and deprecated Atuin paths.
- [x] Frontmatter and README catalog descriptions remain aligned, verified by all-skill validation, inventory tests, semantic trigger assertions, and manual 32-skill comparison.
- [x] All documented validation gates pass, verified by `just`, 32/32 skill validation, 67/67 tests, all `prek` hooks, `git diff --check`, relative-link checks, and a passing independent review.
