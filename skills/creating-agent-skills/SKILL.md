---
name: creating-agent-skills
description: Create, update, or review agent skills with correct structure, triggering metadata, bundled resources, UI metadata, repository integration, and validation. Use when the user asks to create a new skill, improve an existing skill, turn a workflow into a reusable skill, scaffold skill files, or check whether a skill is concise, discoverable, and valid.
---

# Creating Agent Skills

## Purpose

Create skills that another agent can reliably select and use. Keep each skill concise, task-focused, and grounded in the workflow it teaches.

## Workflow

1. Clarify the target only when needed.
   - Infer the destination from the current repo or explicit path when possible.
   - Ask at most one question if the skill's trigger condition or destination is genuinely ambiguous.
   - Treat user-provided requirements, naming rules, and examples as authoritative.

2. Choose the name.
   - Use lowercase letters, meaningful digits, and hyphens.
   - Avoid leading, trailing, or consecutive hyphens.
   - Prefer short, action-oriented names such as `<verb-ing>-<object>`.
   - Avoid vague names like `helper`, `utils`, `tools`, `assistant`, `general`, `data`, `files`, and `documents`.
   - Keep the folder name exactly equal to the frontmatter `name`.

3. Plan reusable contents.
   - Default to `SKILL.md` and `agents/openai.yaml` for judgment or workflow skills when no bundled resources are needed.
   - Add `scripts/` only when deterministic repeated code is useful.
   - Add `references/` only for detail that should be loaded on demand.
   - Add `assets/` only for files that should be copied or used in outputs.
   - Do not create README, changelog, quick-reference, or installation documents inside a skill.

4. Create or update the skill files.
   - Use the target repo's documented skill root.
   - In this repo, new active skills belong in `skills/<skill-name>/SKILL.md`.
   - In this repo, deprecated skills belong in `skills/deprecated/<skill-name>/SKILL.md`.
   - If the target repo, skill framework, or active instructions document or expose a scaffold tool, use it before editing manually.
   - Keep edits bounded to the skill directory and required catalog files.

5. Write `SKILL.md`.
   - Include required `name` and `description` in YAML frontmatter.
   - Add official optional frontmatter fields only when the target repo or skill use case needs them.
   - Put all trigger conditions in `description`; do not rely on a body "when to use" section.
   - Write imperative, reusable instructions for the agent using the skill.
   - Prefer concise checklists, decision rules, and examples over broad explanations.
   - Reference bundled resources directly from `SKILL.md` and explain when to read or use them.
   - Avoid duplicating detailed reference content in both `SKILL.md` and `references/`.

6. Write `agents/openai.yaml`.
   - Include `interface.display_name`, `interface.short_description`, and `interface.default_prompt`.
   - Quote all string values.
   - Make `default_prompt` explicitly mention `$skill-name`.
   - Add icons, colors, dependencies, or policy fields only when explicitly needed.

7. Integrate repository discovery.
   - Add active skills to the relevant `README.md` catalog section when this repo maintains one.
   - Do not duplicate README product messaging in `AGENTS.md`.
   - Update install or clean recipes only when supported paths or install behavior changes.

8. Validate.
   - Prefer documented validation commands from README, AGENTS.md, Makefile, package scripts, or existing CI config.
   - When `skills-ref` is available, run `skills-ref validate <skill-dir>`.
   - Run the available skill validator for the changed skill.
   - Run the repository verification gate when preparing a PR.
   - Test added scripts by executing a representative path.
   - Forward-test complex skills when the workflow is subtle enough that metadata and syntax validation are not enough.

## Review Checklist

- The skill has one clear purpose and trigger condition.
- The frontmatter description says both what the skill does and when to use it.
- Optional frontmatter fields are official and justified by the skill or repo.
- The body contains instructions that are useful after the skill has already triggered.
- Optional resources are justified by repeated use or context savings.
- `agents/openai.yaml` matches the skill and includes a `$skill-name` default prompt.
- The README catalog entry is present when the repo maintains a skill catalog.
- Validation commands passed or failures are explicitly reported.
