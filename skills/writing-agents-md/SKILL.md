---
name: writing-agents-md
description: Use when creating, auditing, or updating AGENTS.md files for a repository, package, or monorepo. This skill turns repository facts into concise agent-facing instructions: setup, build/test commands, code style, security gotchas, PR/commit rules, nested AGENTS.md scope, and conflict precedence.
---

# AGENTS.md Writer

Create or revise `AGENTS.md`: a standard Markdown "README for agents" that gives coding agents the project-specific context they need without cluttering the human README.

## Grounding workflow

Before writing, inspect the repository instead of guessing:

- Read existing guidance: `README.md`, `CONTRIBUTING.md`, current `AGENTS.md`, package-level docs, `.github/workflows/*`, config files, and obvious build manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `justfile`, `Makefile`, etc.).
- Check the tree for monorepos, generated directories, vendored code, large data, or subprojects that may need scoped instructions.
- Verify commands from scripts, task files, Make/Just recipes, or CI definitions. Do not invent commands from ecosystem habits.
- If sources conflict, prefer executable config and CI over prose; preserve uncertainty as a short note or ask one focused question rather than silently choosing.
- If updating an existing `AGENTS.md`, preserve correct project-specific rules and remove stale or unverifiable claims.
- Prefer repository evidence over generic best practices. Label uncertainty briefly or omit it rather than inventing commands.

## Review mode

When asked to review an existing `AGENTS.md` instead of drafting one:

- Check it against repository evidence and the principles below.
- Report concrete findings with severity, affected section/path, evidence, and a suggested replacement.
- Prioritize incorrect commands, stale paths, missing scoped guidance, unsafe instructions, and conflicts with closer `AGENTS.md` files or explicit user directions.
- Use this concise review shape when not directly editing: `Findings`, `Suggested edits`, `Verified evidence`, `Open questions`.
- If edits are requested or clearly beneficial, make a bounded revision and then verify that all listed commands/paths remain grounded.

## AGENTS.md principles

- `AGENTS.md` is plain Markdown; there are no required fields or frontmatter.
- Default to a root-level `AGENTS.md`; add package-level files only when scoped instructions differ.
- Keep it agent-focused: include details a coding agent needs to work safely and verify changes, not product marketing or broad README content.
- Treat it as living documentation. Make rules actionable, testable, and easy to update.
- User prompts override repository instructions. When multiple `AGENTS.md` files apply, the closest file to the edited path takes precedence.
- For large monorepos, prefer nested `AGENTS.md` files in packages/subprojects instead of one overloaded root file. Root files should describe global rules and point to scoped files.
- Avoid copying broad human-facing README content, long install walkthroughs, unverifiable "best practices", personal preferences, or rules that merely restate tool defaults.

## Output requirements

- Name the file exactly `AGENTS.md`.
- Use a clear title; `# Repository Guidelines` is a good default unless the repo already uses another title.
- Keep it concise: usually 200–500 words for a root file. Go longer only when the repository genuinely needs more operational detail.
- Use direct imperative bullets with concrete examples: commands, paths, naming patterns, and verification gates.
- Do not duplicate README installation walkthroughs unless agents specifically need those commands to run checks.
- Do not include secrets, credentials, private URLs, speculative claims, or instructions that encourage bypassing security checks.
- For review responses, prefer findings first; for file creation/update responses, summarize changed paths and verification.

## Recommended content

Choose sections that match the repository; omit empty or irrelevant sections. The core coverage from agents.md is: project overview, build and test commands, code style guidelines, testing instructions, security considerations, and extra teammate-like instructions such as commit/PR rules, deployment gotchas, large datasets, or migration steps.

### Project structure and scope

- Summarize key directories and what agents should edit or avoid.
- Mention generated/vendor/build artifacts that should not be hand-edited.
- In monorepos, state how to locate the relevant package and whether package-level `AGENTS.md` files override root guidance.
- Example split: root `AGENTS.md` owns repo-wide safety rules and CI gates; `packages/api/AGENTS.md` owns API migrations and schema tests; `packages/web/AGENTS.md` owns UI screenshots and browser checks.

### Build, test, and development commands

- List the smallest reliable commands for setup, local development, formatting, linting, typechecking, tests, and full CI-equivalent verification.
- Include targeted variants when useful, e.g. package filters or single-test patterns.
- State required working directory if commands must run from repo root or a package directory.
- Prefer commands proven by `package.json` scripts, `just --list`, `make help`, lockfiles, or CI jobs; if a command cannot be confirmed, leave it out or mark it as an example.

### Code style and conventions

- Capture formatting tools, language versions, strictness settings, naming patterns, architectural boundaries, and dependency rules.
- Prefer enforceable rules over taste statements.

### Testing and verification

- Explain where tests live, naming conventions, fixture practices, coverage expectations, and which checks agents should run after specific change types.
- Include relevant programmatic checks because agents may attempt listed commands and fix failures before finishing.
- Encourage adding or updating tests with behavior changes when that is true for the repo.

### Security, configuration, and data

- Call out secret handling, environment files, migrations, external services, large datasets, deployment steps, and destructive commands.
- Tell agents how to use safe examples (`.env.example`, local mocks, dry-run flags) when available.

### Commit and PR guidance

- Derive commit style from recent history if requested or relevant.
- Include PR expectations such as linked issues, screenshots for UI changes, migration notes, and verification summaries.

## Migration and compatibility notes

- If the repo has older agent instruction files, migrate by renaming to `AGENTS.md`; optionally leave a symlink for tools that still expect the old name, e.g. `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`.
- For tools that need explicit configuration, add minimal setup notes only when the repo uses them (for example Aider `read: AGENTS.md` or Gemini CLI `context.fileName`).

## Final checks

Before finishing:

- Verify every listed command/path exists or is clearly marked as an example.
- Ensure rules do not conflict with nearer scoped instructions or explicit user requirements.
- Check that review output uses the requested findings format when applicable.
- Keep one clear purpose per section; remove filler and generic advice.
- If you edited the file, summarize affected path(s), evidence used, and verification performed.
