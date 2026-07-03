---
name: writing-work-logs
description: Use only when the user explicitly names the writing-work-logs skill; never auto-activate from generic work log, daily log, EOD summary, status update, or date-range summary requests.
---

# Work Log Writer

## Scope

Write concise work logs for a specified date range in the current git repository. Do not use this skill unless the user explicitly invokes `$writing-work-logs` or names `writing-work-logs`.

Operate on one git repository at a time. Do not write files unless the user explicitly asks for a saved note or file update.

## Date Range

Resolve the requested range before collecting evidence.

- If the user uses a relative range such as today, yesterday, or last week, check the current local date first.
- Interpret "last week" as the previous calendar week by default. If context suggests the user might mean the last 7 days, ask one concise clarification question before proceeding.
- If the user gives explicit dates or a start/end range, use them directly.
- If no date range is provided, ask which date or period to summarize.

Use concrete dates in the final title, not relative labels.

Example commands:

```bash
date +%F
git config user.name
git config user.email
git log --since="2026-05-01 00:00" --until="2026-05-05 23:59:59" --date=iso --pretty=format:"%h%x09%ad%x09%an <%ae>%x09%s"
```

## Evidence Collection

Start from commits in the resolved range.

1. Gather commit hashes, authors, dates, and messages.
2. If commits include multiple authors, prefer commits from the current git user when `git config user.name` or `git config user.email` identifies them. If the current author cannot be determined, ask whether to summarize only the user's own commits.
3. If commit messages are too vague, inspect relevant diffs with `git show --stat <sha>` or `git show --name-only <sha>` before summarizing.
4. If the range includes today, optionally inspect uncommitted changes with `git status --short` and `git diff --stat`.
5. Use user notes or pasted context when provided, but do not invent completed work.

## Output Rules

Required format:

```markdown
# Work Log - <resolved date range>

- ...
- ...
- ...
```

Use a title that includes the resolved date range. Keep the body as a single flat bullet list with no sections or subheadings. Each bullet should describe one high-level work item, progress point, blocker, or follow-up. Prefer concise summaries over implementation details, and order bullets from highest to lowest team impact. If team impact is unclear, use the evidence to prioritize likely cross-team/customer impact, risk reduction, unblockers, and follow-ups before lower-impact implementation details.

## Uncertainty

Do not guess what the user completed. If evidence is insufficient, either mark the uncertainty in a bullet or ask for the minimum missing context needed to proceed.
