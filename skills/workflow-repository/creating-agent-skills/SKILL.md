---
name: creating-agent-skills
description: Create, name, rename, revise, or review agent skills for reliable triggering, lean instructions, justified resources, repository discovery, and validation. Use for new skills, naming decisions, authorized repository renames, skill scaffolding, workflow-to-skill conversion, prompt optimization, or skill audits.
---

# Creating Agent Skills

Create a skill another agent can select and apply without unnecessary context.

## Name and Rename

Name the task and trigger the skill represents, not its implementation.

- Read the skill's actual description and workflow, then identify the triggering action, object or domain, and any necessary product qualifier.
- Use lowercase kebab-case with meaningful digits and single hyphens; use no leading or trailing hyphen. Keep the directory and frontmatter `name` identical and respect the target framework's length limit.
- Prefer two to four specific words. Avoid vague terms such as `helper`, `utils`, `tools`, `assistant`, `magic`, `smart`, or `general`, and avoid product or organization names unless the trigger is genuinely product-specific.
- Preserve the original user intent rather than forcing `<verb-ing>-<object>` when another pattern better expresses the meaning or matches the repository's established convention.
- Inspect sibling names and exact-name references. Compare a small candidate set for specificity, searchability, future stability, and collision risk, then lead with one recommendation and its deciding reason.

A naming recommendation does not authorize a repository rename. Do not edit files when the user asked only for names or review. For an authorized rename, update the directory, frontmatter `name`, catalog, links, examples, tests, and other exact-name references as one bounded change; preserve a compatibility note when external consumers depend on the old name.

For naming-only output, lead with the recommendation and deciding reason. For multiple skills, use a current/recommended/reason table and include only conflicts or compatibility work that affects adoption.

## Workflow

1. Inspect the target repository's instructions, skill root, sibling skills, catalog, validators, and any model-specific prompting guide. Infer the destination and ask one question only when purpose, trigger, or location is materially ambiguous.
2. Choose or review the name with the naming criteria above.
3. Keep only justified contents:
   - `SKILL.md` for trigger metadata and post-trigger workflow.
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
6. Update the repository's catalog or installation surfaces only when its discovery model requires it.
7. Validate syntax and structure with the repository's documented validator, run representative bundled scripts, and forward-test subtle workflows. Run the repository gate when required and report unavailable checks honestly.

## Completion Criteria

- One clear purpose, discriminating trigger, and specific collision-resistant name that preserves the intended meaning.
- Body content is useful only after the skill has triggered.
- No repeated instruction groups, generic background, decorative examples, or unjustified resources.
- Local edits and checks proceed when requested; external, destructive, costly, or scope-expanding actions retain explicit approval boundaries.
- Frontmatter, catalog text, and resource links agree.
- Validation evidence and material caveats are reported.
