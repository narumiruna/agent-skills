# Skills

Reusable agent skills for coding, writing, research, and slide work. The collection is organized for Codex-first workflows, and it can also be installed as a standard skills repo with `npx skills add narumiruna/skills`.

## Install

### 1. Install with `npx`

Use this when you want the collection without linking a local checkout.

```shell
npx skills add narumiruna/skills
```

### 2. Local Codex development with `just`

Use this when you want repo-managed local copies in `~/.codex/skills`.

```shell
just install-all

# or install one skill
just install managing-python-projects
```

Each install replaces the target skill directory before copying. `just install-all`
installs active top-level skills only; it skips `skills/deprecated/`.

Remove copied skills when finished:

```shell
just clean-all

# or clean one skill
just clean managing-python-projects
```

`just` by itself only lists the available recipes.

### 3. Manual copy for Codex

Use this when you want a one-off local copy without `just`.

```shell
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/managing-python-projects
cp -R ./skills/managing-python-projects ~/.codex/skills/managing-python-projects
```

Repeat the same pattern for other skills as needed.

## How To Use In Codex

- Run `/skills` to inspect the installed collection.
- Type `$managing-python-projects`, `$writing-imrad`, or another skill name to invoke one explicitly.
- Or describe the task normally and let Codex choose a matching skill.

If Codex does not pick up a local skill change, restart Codex and try again.

## Skill Guide

### Python

- `managing-python-projects`: uv-based Python project setup and standalone scripts, including dependency add/remove/sync, `uv run`, `uv run --with`, `--no-project`, inline script metadata, quality gates with ruff, ty, pytest, coverage, prek or pre-commit, and package build or publishing workflows.
- `building-typer-clis`: focused Typer command structure, options, and multi-command apps.
- `configuring-python-logging`: focused stdlib logging or loguru configuration.
- `using-peewee-orm`: focused Peewee patterns such as `DatabaseProxy`, scoped transactions, and SQLite tests.

### Writing And Research

- `writing-plans`: lean implementation and work plans with executable task lists, optional architecture and tech-stack notes, finite completion checklists, and plan archiving rules.
- `writing-imrad`: deciding whether IMRaD fits, drafting new IMRaD outputs, and reviewing existing drafts.
- `researching-gourmet-venues`: evidence-based city dining research with structured scoring and audit files.

### Slides And Visuals

- `creating-slide-decks`: end-to-end Marp/Marpit slide creation, including color systems and SVG visuals.
- `authoring-marp-slides`: focused Marp/Marpit authoring rules, directives, and layouts.
- `designing-slide-colors`: slide palette selection and color-system workflows.
- `creating-svg-illustrations`: SVG diagram and illustration guidance for slide decks.
- `creating-mermaid-diagrams`: Mermaid diagrams for docs, architecture, sequence flows, ER diagrams, and Gantt charts.

### Workflow And Repository Maintenance

- `naming-agent-skills`: creating, reviewing, renaming, and standardizing agent skill names so they are predictable, searchable, and easy for agents to select.
- `checking-cli-help`: deciding whether to check `--help`, built-in `help`, or `man` before running a shell or CLI command.
- `using-jira-cli`: using ankitpokhrel/jira-cli for Jira setup, issue queries and mutations, epics, sprints, releases, projects, boards, and script-friendly output.
- `writing-git-commits`: reviewing diffs, choosing commit types, and writing focused Conventional Commits.
- `maintaining-memory-md`: deciding when to read or update repository `MEMORY.md` files and keeping `GOTCHA` / `TASTE` entries concise.
- `writing-agents-md`: creating or updating `AGENTS.md` guidance for this repository.

## Deprecated Skills

Deprecated skills remain in `skills/deprecated/<skill-name>/` for reference and
are not included in `just install-all`.

- `cleaning-atuin-history`: preview-first cleanup planning for noisy Atuin shell history.
- `building-codex-hooks`: designing or debugging Codex CLI hooks and `hooks.json` behavior.
- `writing-tests-first`: applying a red-green-refactor workflow to non-trivial code changes.
- `writing-work-logs`: explicitly invoked only; writing concise work logs from repository evidence.
