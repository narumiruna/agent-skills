---
name: git-commit
description: Use when inspecting local git changes, drafting or validating commit messages, converting ad hoc messages to Conventional Commits, choosing an appropriate commit type or scope, explaining whether a change is breaking, or creating focused commits that match the actual diff.
---

# Git Commit

## Overview

Inspect the actual diff before writing the message. Prefer one coherent commit per intent, then map that intent to a Conventional Commits title, optional body, and optional footers.

Read `references/conventional-commits.md` when the type is ambiguous, when footers are needed, or when the change may be breaking.

## Workflow

1. Inspect the working tree first.
   Start with `git status --short` to see staged, unstaged, and untracked paths. If the user asks for a commit, inspect `git diff --cached` first; inspect `git diff` too when unstaged changes might affect the requested commit.
2. Define the commit boundary.
   Group files by one user-visible intent. If the diff mixes unrelated work, recommend splitting it into multiple commits instead of forcing one summary over several intents.
3. Choose the type from behavior, not file extension.
   Use `feat` for a new capability, `fix` for a bug fix, and other common lowercase types such as `docs`, `refactor`, `test`, `perf`, `build`, `ci`, `style`, `chore`, or `revert` when they describe the dominant change more accurately.
4. Add a scope only when it clarifies the change.
   Keep scopes short, noun-like, and stable, such as `api`, `auth`, `parser`, or `docs`. Omit the scope when it adds little signal.
5. Write the title in the required format.
   Use `<type>[optional scope][!]: <description>`. Keep the description short, specific, and grounded in the diff. Prefer imperative phrasing such as `fix(parser): handle empty array input`.
6. Add body and footers only when they add concrete value.
   Use the body to explain why the change exists, important constraints, or notable tradeoffs. Add footers after a blank line for trailers such as `Refs: #123` or `Reviewed-by: Name`.
7. Mark breaking changes explicitly.
   Use `!` before the colon, a `BREAKING CHANGE:` footer, or both. When the change is breaking, describe the user impact or migration requirement clearly.
8. Keep the message aligned with the exact commit contents.
   Do not describe unstaged changes, planned follow-up work, or unrelated cleanup that is not part of the commit.

## Decision Rules

- Prefer `feat` when the diff introduces new behavior that users or integrators can rely on.
- Prefer `fix` when the diff corrects incorrect behavior, a regression, or an edge-case failure.
- Prefer `refactor` when behavior should stay the same and the change mainly restructures code.
- Prefer `docs` when the commit only changes documentation.
- Prefer multiple commits when a single diff contains more than one independent reason to exist.
- Prefer no body when the title fully explains the change.
- Prefer no footer unless a trailer or breaking-change notice is actually needed.

## Commit Execution

- Stage only the paths intended for this commit.
- If the repo has staged and unstaged changes, ensure the commit message matches only the staged diff.
- If the user asks for a suggested message instead of an actual commit, return one or more candidate messages grounded in the inspected diff.
- If the user asks whether an existing message is valid, check the structure, the type choice, and whether the wording matches the actual change.

## Reference

- `references/conventional-commits.md`: format, type guidance, breaking-change rules, footers, and examples.
