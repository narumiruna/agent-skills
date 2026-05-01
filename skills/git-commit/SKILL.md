---
name: git-commit
description: Use when inspecting local git changes, drafting or validating Conventional Commit messages, checking type or scope choices, explaining breaking changes, or creating a focused commit from the actual diff.
---

# Git Commit

Inspect the actual diff before writing the message. Prefer one coherent commit per intent, then map that intent to a Conventional Commits title and only add extra sections when they carry concrete information.

Read `references/conventional-commits.md` when the type is ambiguous, when you need trailers or breaking-change wording, or when the user asks for exact format details.

## Workflow

1. Inspect the exact commit contents.
   Start with `git status --short`. If the user asks for a commit, inspect `git diff --cached` first; inspect `git diff` too when unstaged changes might affect the commit boundary.
2. Define the commit boundary.
   Group files by one user-visible intent. If the diff mixes unrelated work, recommend splitting it into multiple commits instead of forcing one vague summary over several intents.
3. Choose the type and scope from behavior.
   Pick the lowercase Conventional Commits type that best matches the dominant behavior. Add a short noun-like scope only when it adds signal.
4. Write the title in the required format.
   Use `<type>[optional scope][!]: <description>`. Keep the description short, specific, and grounded in the diff.
5. Add body and footers only when they add concrete value.
   Use the body for why, constraints, or tradeoffs. Add footers only for real trailers or `BREAKING CHANGE:`.
6. Keep the message aligned with the selected diff.
   Do not describe unstaged changes, planned follow-up work, or unrelated cleanup that is not part of the commit.

## Decision Rules

- Prefer `feat` for a new capability and `fix` for incorrect behavior or regressions.
- Prefer `refactor` when behavior should stay the same, and `docs` when only documentation changes.
- Prefer no scope, body, or footer unless each one adds concrete signal.
- Prefer multiple commits over one vague summary when the diff contains unrelated work.
- If the user asks for validation, check both the structure and whether the wording matches the inspected diff.
- Follow repo git rules for staging and commit structure; this skill focuses on mapping the diff to the right message.

## Reference

- `references/conventional-commits.md`: exact format, common types, footer rules, breaking-change wording, and examples.
