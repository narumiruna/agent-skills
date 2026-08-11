# Skills

Reusable agent skills for coding, writing, research, and slide work. This repo is organized for Codex-first workflows and can also be installed as a standard skills repo.

## 🚀 Quick Start

Install the collection:

```shell
npx skills add narumiruna/skills
```

Then open Codex and run `/skills` to inspect what was installed. Invoke a skill explicitly with `$skill-name`, or describe the task normally and let Codex choose a match.

## 📦 Install

### Standard install with `npx skills`

Use this when you want the collection without linking a local checkout:

```shell
npx skills add narumiruna/skills
```

Standard discovery exposes active skills only; deprecated skills live outside `skills/` and remain available solely for repository reference or explicit local use.

## 🧭 How To Use In Codex

- Run `/skills` to inspect the installed collection.
- Type `$managing-python-with-uv`, `$applying-imrad`, or another skill name to invoke one explicitly.
- Describe the task normally and let Codex choose a matching skill.

If Codex does not pick up a local skill change, restart Codex and try again.

## 🧰 Skill Catalog

### Python

Repository path: `skills/python/`

| Skill | Use it for |
| --- | --- |
| `managing-python-with-uv` | uv projects, scripts, dependencies, checks, builds, and authorized publishing. |

### Writing & Research

Repository path: `skills/writing-research/`

| Skill | Use it for |
| --- | --- |
| `writing-roadmap` | Creating, revising, reviewing, and archiving evidence-grounded strategic roadmaps. |
| `writing-plans` | Drafting, executing, and tracking lean implementation plans with acceptance evidence. |
| `grilling-designs` | Evidence-informed, one-decision-at-a-time design grilling. |
| `applying-imrad` | Evidence-traceable IMRaD fit checks, reviews, transformations, and drafts. |
| `creating-telegraph-pages` | Preparing and publishing one explicitly authorized Telegra.ph article. |
| `grounding-with-google-genai` | Grounded Google Search, Maps, and specific-URL research with Gemini. |

### Learning & Explanation

Repository path: `skills/learning-explanation/`

| Skill | Use it for |
| --- | --- |
| `explaining-step-by-step` | Progressive, evidence-grounded mental models for complex material. |

### UI/UX Design

Repository path: `skills/ui-ux-design/`

| Skill | Use it for |
| --- | --- |
| `designing-user-experiences` | Design, review, or implement bounded interfaces and approval-gated end-to-end digital experiences. |

### Slides & Visuals

Repository path: `skills/slides-visuals/`

| Skill | Use it for |
| --- | --- |
| `creating-slide-decks` | Complete Marp decks with coordinated narrative, colors, visuals, and rendering. |
| `authoring-marp-slides` | Focused Marp/Marpit authoring, templates, themes, and rendered checks. |
| `designing-slide-colors` | Semantic slide palettes with usage rules and measured contrast evidence. |
| `creating-svg-illustrations` | Accessible, portable SVG diagrams and illustrations for target artifacts. |
| `creating-mermaid-diagrams` | Editable Mermaid diagrams with optional consumer-ready SVG rendering. |

### Workflow & Repository Maintenance

Repository path: `skills/workflow-repository/`

| Skill | Use it for |
| --- | --- |
| `creating-agent-skills` | Creating, naming, reviewing, revising, and explicitly scoring lean, discoverable agent skills. |
| `herdr` | Explicitly requested control of Herdr panes, tabs, workspaces, commands, and coding agents. |
| `improving-codebase-architecture` | Evidence-led codebase architecture assessment and behavior-preserving refactoring. |
| `auditing-code-security` | Evidence-led, security-first, read-only code audits with verified findings and bounded tool use. |
| `reviewing-code` | Evidence-led ordinary code review with baseline security checks and authorized hardening handoff. |
| `running-panel-review-loops` | Iterative multi-reviewer code review, verified fixes, and evidence-based acceptance. |
| `hardening-code-paths` | Confirming and fixing code-path failure modes or verified security findings. |
| `using-jira-cli` | Read-only Jira inspection and precisely authorized CLI mutations. |
| `applying-tdd` | Scoping red-green-refactor with explicit production-path, test-data, and observable-behavior boundaries. |
| `writing-git-commits` | Drafting, validating, or creating focused Conventional Commits from diffs. |
| `writing-agents-md` | Creating, reviewing, and automatically maintaining lean, evidence-backed `AGENTS.md` guidance at the narrowest applicable scope. |

## 🗄️ Deprecated Skills

Deprecated skills remain in `deprecated/<skill-name>/` for reference and are excluded from standard discovery.

| Skill | Notes |
| --- | --- |
| `checking-cli-help` | Legacy decision rule for focused command-help inspection. |
| `cleaning-atuin-history` | Legacy Atuin audit and exact-approval cleanup preparation. |
| `building-codex-hooks` | Version-sensitive legacy Codex CLI hook reference. |
| `writing-work-logs` | Legacy explicit-only Git-evidence work logs. |
| `naming-agent-skills` | Merged into `creating-agent-skills`; retained as a compatibility reference. |
| `scoring-agent-skills` | Merged into `creating-agent-skills`; retained as a compatibility reference. |
| `designing-user-interfaces` | Merged into `designing-user-experiences`; retained as a compatibility reference. |
| `researching-gourmet-venues` | Rarely used city dining workflow retained as a compatibility reference. |
| `syncing-main-branch` | Legacy explicit-only main-branch synchronization workflow. |
| `iterating-ui-improvements` | Legacy explicit-only DevTools audit-fix-commit loop. |
| `building-typer-clis` | Legacy Typer-specific CLI workflow retained as a compatibility reference. |
| `configuring-python-logging` | Legacy Python logging configuration workflow retained as a compatibility reference. |
| `using-peewee-orm` | Legacy Peewee lifecycle workflow retained as a compatibility reference. |
| `managing-git-worktrees` | Legacy loss-aware Git worktree lifecycle workflow retained as a compatibility reference. |
| `maintaining-memory-md` | Legacy repository memory curation workflow retained as a compatibility reference. |
| `resolving-pr-review-comments` | Legacy explicit PR feedback workflow retained as a compatibility reference. |
| `using-codebase-memory-cli` | Legacy CLI-only codebase graph workflow retained as a compatibility reference. |
