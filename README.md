# Agent Skills

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
just install python
```

Each install replaces the target skill directory before copying.

Remove copied skills when finished:

```shell
just clean-all

# or clean one skill
just clean python
```

`just` by itself only lists the available recipes.

### 3. Manual copy for Codex

Use this when you want a one-off local copy without `just`.

```shell
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/python
cp -R ./skills/python ~/.codex/skills/python
```

Repeat the same pattern for other skills as needed.

## How To Use In Codex

- Run `/skills` to inspect the installed collection.
- Type `$python`, `$imrad`, or another skill name to invoke one explicitly.
- Or describe the task normally and let Codex choose a matching skill.

If Codex does not pick up a local skill change, restart Codex and try again.

## Skill Guide

### Python

- `python`: default entry for uv project setup, dependencies, quality gates, packaging, and standalone scripts.
- `python-typer`: Typer command structure, options, and multi-command apps.
- `python-logging`: choosing and configuring stdlib logging or loguru.
- `python-peewee`: Peewee patterns such as `DatabaseProxy`, scoped transactions, and SQLite tests.

### Writing And Research

- `imrad`: deciding whether IMRaD fits, drafting new IMRaD outputs, and reviewing existing drafts.
- `gourmet-research`: evidence-based city dining research with structured scoring and audit files.

### Slides And Visuals

- `slide-creator`: end-to-end Marp/Marpit slide creation, including color systems and SVG visuals.
- `marp-authoring`: focused Marp/Marpit authoring rules, directives, and layouts.
- `slide-color-design`: slide palette selection and color-system workflows.
- `svg-illustration`: SVG diagram and illustration guidance for slide decks.
- `mermaid-creator`: Mermaid diagrams for docs, architecture, sequence flows, ER diagrams, and Gantt charts.

### Workflow And Repository Maintenance

- `help-me`: deciding whether to check `--help`, built-in `help`, or `man` before running a shell or CLI command.
- `git-commit`: reviewing diffs, choosing commit types, and writing focused Conventional Commits.
- `work-log-writer`: explicitly invoked only; writing concise work logs from repository evidence.
- `agents-writer`: creating or updating `AGENTS.md` guidance for this repository.
- `codex-cli-hooks`: designing or debugging Codex CLI hooks and `hooks.json` behavior.
- `test-driven-development`: applying a red-green-refactor workflow to non-trivial code changes.

### Utilities

- `atuin-history-cleanup`: preview-first cleanup planning for noisy Atuin shell history.
