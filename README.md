# Skills

Reusable agent skills for coding, writing, research, and slide work. This repo is organized for Codex-first workflows and can also be installed as a standard skills repo.

## 🚀 Quick Start

Install the collection:

```shell
npx skills add narumiruna/skills
```

Then open Codex and run `/skills` to inspect what was installed. Invoke a skill explicitly with `$skill-name`, or describe the task normally and let Codex choose a match.

## 📦 Install

Choose the path that matches how you want to use the skills.

### 1. Standard install with `npx`

Use this when you want the collection without linking a local checkout:

```shell
npx skills add narumiruna/skills
```

Standard discovery exposes active skills only; deprecated skills live outside `skills/` and remain available solely for repository reference or explicit local use.

### 2. Local Codex development with `just`

Use this when you want repo-managed local copies in `~/.codex/skills`:

```shell
just install-all

# or install one skill
just install managing-python-with-uv
```

Each install replaces the target skill directory before copying. `just install-all` installs the top-level directories under `skills/`; deprecated skills live outside that tree.

Remove copied skills when finished:

```shell
just clean-all

# or clean one skill
just clean managing-python-with-uv
```

`just` by itself only lists the available recipes.

### 3. Manual copy for Codex

Use this when you want a one-off local copy without `just`:

```shell
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/managing-python-with-uv
cp -R ./skills/managing-python-with-uv ~/.codex/skills/managing-python-with-uv
```

Repeat the same pattern for other skills as needed.

## 🧭 How To Use In Codex

- Run `/skills` to inspect the installed collection.
- Type `$managing-python-with-uv`, `$applying-imrad`, or another skill name to invoke one explicitly.
- Describe the task normally and let Codex choose a matching skill.

If Codex does not pick up a local skill change, restart Codex and try again.

## 🧰 Skill Catalog

### Python

| Skill | Use it for |
| --- | --- |
| `managing-python-with-uv` | uv-based projects, scripts, dependencies, quality gates, and packaging. |
| `building-typer-clis` | Typer command structure, options, and multi-command apps. |
| `configuring-python-logging` | stdlib logging and loguru configuration choices. |
| `using-peewee-orm` | Peewee patterns, scoped transactions, and SQLite tests. |

### Writing & Research

| Skill | Use it for |
| --- | --- |
| `writing-plans` | Lean implementation plans with executable task lists and completion checks. |
| `grilling-designs` | One-question-at-a-time plan and design grilling. |
| `applying-imrad` | IMRaD fit checks, drafting, transformation, and review. |
| `researching-gourmet-venues` | Evidence-based dining research with scoring and audit files. |
| `creating-telegraph-pages` | Publishing structured public articles to Telegra.ph. |

### Learning & Explanation

| Skill | Use it for |
| --- | --- |
| `explaining-step-by-step` | Progressive, source-grounded explanations of concepts, issues, PRs, code, systems, and decisions. |

### UI/UX Design

| Skill | Use it for |
| --- | --- |
| `designing-user-interfaces` | HIG-informed, accessible interfaces that preserve agency and useful capability. |

### Slides & Visuals

| Skill | Use it for |
| --- | --- |
| `creating-slide-decks` | End-to-end Marp/Marpit slide creation. |
| `authoring-marp-slides` | Marp/Marpit directives, layouts, and authoring rules. |
| `designing-slide-colors` | Slide palettes and color-system workflows. |
| `creating-svg-illustrations` | SVG diagrams and illustrations for decks. |
| `creating-mermaid-diagrams` | Mermaid flowcharts, sequence diagrams, ER diagrams, and more. |

### Workflow & Repository Maintenance

| Skill | Use it for |
| --- | --- |
| `creating-agent-skills` | Creating concise, valid, discoverable agent skills. |
| `reviewing-code` | Code review for correctness, edge cases, tests, security, and integration risk. |
| `resolving-edge-cases` | Iteratively finding, fixing, and verifying plausible edge cases in code flows. |
| `naming-agent-skills` | Predictable, searchable skill names. |
| `using-jira-cli` | Jira setup, queries, mutations, epics, sprints, releases, projects, and boards. |
| `applying-tdd` | TDD red-green-refactor workflow for non-trivial code changes. |
| `writing-git-commits` | Focused Conventional Commits from real diffs. |
| `managing-git-worktrees` | Safe Git worktree creation, repair, removal, pruning, and branch cleanup. |
| `maintaining-memory-md` | Creates repository `MEMORY.md` on the first durable `GOTCHA` or `TASTE`, then keeps entries concise and current. |
| `writing-agents-md` | Creating or updating repository `AGENTS.md` guidance. |

## 🗄️ Deprecated Skills

Deprecated skills remain in `deprecated/<skill-name>/` for reference and are not included in `just install-all`.

| Skill | Notes |
| --- | --- |
| `checking-cli-help` | Deciding whether to inspect `--help`, built-in `help`, or `man`. |
| `cleaning-atuin-history` | Preview-first cleanup planning for noisy Atuin shell history. |
| `building-codex-hooks` | Codex CLI hooks and `hooks.json` behavior. |
| `writing-work-logs` | Explicitly invoked work logs from repository evidence. |
