---
name: naming-agent-skills
description: Choose, review, rename, and standardize agent skill names so they are predictable, searchable, and easy for agents to select correctly. Use when creating a new skill name, renaming an existing skill, reviewing whether a skill name is appropriate, standardizing multiple skill names, converting informal skill ideas into production-ready skill names, or designing naming conventions for an agent skill library.
---

# Naming Agent Skills

## Purpose

Name skills by the task and trigger condition they represent. Optimize for predictable agent selection, file-tree search, and low overlap with existing skills.

## Naming Rules

- Use lowercase letters only.
- Use digits only when they are meaningful.
- Use hyphens as word separators.
- Do not use spaces, underscores, camelCase, PascalCase, or dots.
- Keep names short but specific; prefer 2 to 4 words.
- Avoid names longer than 64 characters.
- Avoid product or organization names unless the skill is truly specific to that product.
- Avoid reserved or platform-specific names unless explicitly required.
- Avoid vague words such as `helper`, `utils`, `tools`, `assistant`, `magic`, `smart`, `general`, `data`, `files`, or `documents`.

## Preferred Patterns

Default to:

```text
<verb-ing>-<object>
```

Examples:

```text
reviewing-pull-requests
debugging-docker-compose
analyzing-otel-traces
writing-unit-tests
refactoring-python
summarizing-logs
```

Use command-style names only when the library already follows that pattern:

```text
<verb>-<object>
```

Examples:

```text
review-pull-requests
debug-docker-compose
analyze-otel-traces
write-unit-tests
refactor-python
summarize-logs
```

Use domain-first names only when the library is organized mainly by technology or domain:

```text
<domain>-<task>
```

Examples:

```text
python-refactoring
gitlab-mr-review
docker-compose-debugging
otel-trace-analysis
jira-ticket-polishing
```

## Selection Rules

When choosing between possible names:

1. Prefer the name that best describes when the agent should use the skill.
2. Prefer concrete task names over broad category names.
3. Prefer user-facing intent over implementation detail.
4. Prefer names that remain valid if the internal implementation changes.
5. Prefer names that are easy to search in a file tree.
6. Prefer names that do not overlap with existing skills.

## Renaming Existing Skills

When renaming an existing skill:

1. Identify the skill's actual trigger condition.
2. Identify the main object or domain.
3. Remove vague, decorative, or implementation-focused words.
4. Choose one naming pattern and apply it consistently.
5. Preserve compatibility notes if external references depend on the old name.

Examples:

```text
old: smart-code-helper
new: reviewing-code-changes

old: jira
new: polishing-jira-tickets

old: trace-tool
new: analyzing-otel-traces
```

## Examples

Prefer:

```text
reviewing-gitlab-mrs
debugging-ci-pipelines
writing-python-tests
refactoring-typescript
analyzing-otel-traces
summarizing-gmail-threads
polishing-jira-tickets
creating-release-notes
```

Avoid vague names:

```text
helper
utils
tools
smart-review
magic-agent
general-coding
documents
data
files
```

Avoid inconsistent formatting:

```text
ReviewPR
review_pr
review.pr
Review-Pull-Requests
review pull requests
```

Avoid implementation-oriented names:

```text
parse-json
call-api
read-yaml
run-python-script
```

Prefer purpose-oriented alternatives:

```text
analyzing-test-results
syncing-linear-issues
validating-skill-metadata
generating-project-summary
```

For a skill that adds timestamps to agent messages, prefer:

```text
adding-message-timestamps
```

Use `pi-message-timestamps` only if the skill is specific to Pi. Otherwise, use `adding-message-timestamps`.

## Output Formats

When asked to propose names, return:

```text
Recommended: <name>

Alternatives:
- <name>
- <name>
- <name>

Reason:
<brief explanation>
```

When asked to review a name, return:

```text
Verdict: good / acceptable / should rename

Issues:
- <issue>

Recommended replacement:
<name>
```

When asked to standardize multiple names, return a table:

```text
| Current name | Recommended name | Reason |
|---|---|---|
| old-name | new-name | reason |
```

## Default Decision Rule

If there is no strong reason to use another pattern, use `<verb-ing>-<object>`. This makes the skill name read like a capability and helps the agent understand when to use it.
