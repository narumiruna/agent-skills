---
name: creating-agent-skills
description: Create, revise, or review agent skills for reliable triggering, lean instructions, justified resources, aligned UI metadata, repository discovery, and validation. Use for new skills, skill scaffolding, workflow-to-skill conversion, prompt optimization, or skill audits.
---

# Creating Agent Skills

Create a skill another agent can select and apply without unnecessary context.

## Workflow

1. Inspect the target repository's instructions, skill root, sibling skills, catalog, validators, and any model-specific prompting guide. Infer the destination and ask one question only when purpose, trigger, or location is materially ambiguous.
2. Choose a concise lowercase kebab-case name that preserves the skill's actual intent. Keep directory and frontmatter `name` identical.
3. Keep only justified contents:
   - `SKILL.md` for trigger metadata and post-trigger workflow.
   - `agents/openai.yaml` when the target ecosystem uses UI metadata.
   - `references/` for detail loaded only on demand.
   - `scripts/` for deterministic repeated operations.
   - `assets/` for material copied into or used by outputs.
   Do not add per-skill README, changelog, installation, or quick-reference files unless the target framework explicitly requires them.
4. Use an official scaffold when the target repository provides one, then edit the generated files. Keep changes within the skill and required discovery/catalog surfaces.
5. Write `SKILL.md`:
   - Put `name` and a what-and-when description in YAML frontmatter; use only supported optional fields.
   - Put trigger conditions in `description`, not a body “when to use” section.
   - State each instruction once. Prefer outcome, constraints, approval boundaries, evidence, and stopping criteria over prescribed routine steps.
   - Keep examples only when they encode a requirement or prevent a demonstrated error.
   - Link each resource directly and say when to load or run it; do not duplicate its detail in `SKILL.md`.
6. Write aligned UI metadata. For OpenAI metadata, quote strings; include `interface.display_name`, `short_description`, and a `default_prompt` that explicitly names `$skill-name`. Add policy, icons, colors, or dependencies only when needed.
7. Update the repository's catalog or installation surfaces only when its discovery model requires it.
8. Validate syntax and structure with the repository's documented validator, run representative bundled scripts, and forward-test subtle workflows. Run the repository gate when required and report unavailable checks honestly.

## Completion Criteria

- One clear purpose and discriminating trigger.
- Body content is useful only after the skill has triggered.
- No repeated instruction groups, generic background, decorative examples, or unjustified resources.
- Local edits and checks proceed when requested; external, destructive, costly, or scope-expanding actions retain explicit approval boundaries.
- Frontmatter, UI metadata, catalog text, and resource links agree.
- Validation evidence and material caveats are reported.
