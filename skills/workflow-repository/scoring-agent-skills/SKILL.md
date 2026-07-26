---
name: scoring-agent-skills
description: Score or compare one or more agent skills across trigger clarity, workflow actionability, safety boundaries, verification rigor, and leanness. Use only when the user explicitly asks for ratings, numerical quality scores, rubric-based scorecards, or scored comparisons; use creating-agent-skills for unscored reviews or revisions.
---

# Scoring Agent Skills

Produce a comparable quality scorecard, not a vague impression or a runtime capability claim.

## Scope and Evidence

1. Resolve the requested skill set. For “every skill,” use the repository's active discovery tree unless the user explicitly includes deprecated or external skills.
2. Inspect applicable repository instructions, the model-specific prompting guide, each `SKILL.md`, UI metadata, catalog entry, and directly linked resources relevant to a score.
3. For the trusted current repository, run its established non-destructive validators when feasible. For an external or untrusted repository, default to source inspection or a trusted validator. Do not run repository-supplied code unless it is sandboxed and the user explicitly authorizes the exact command.
4. Treat structural checks, link integrity, metadata presence, and test results as supporting evidence. They do not by themselves prove prompt quality or task success.
5. Read `references/rubric.md` and assign an integer from 1 to 10 for each assessable dimension. Apply the same anchors to every skill and assess safety and verification proportionately to what the skill can do.
6. Support each score with direct evidence from the inspected surfaces. Revisit conspicuous outliers after the first pass so differences reflect the rubric rather than category or ordering bias.

## Calculate and Report

Use equal weight for all assessed dimensions. When all five are assessed, compute the overall score as their arithmetic mean and show one decimal place. If environment-specific inaccessible evidence prevents a defensible dimension score, mark that dimension unassessed, exclude it from the aggregate, and report score coverage and confidence; do not add hidden bonuses or penalties.

Return in the user's language unless requested otherwise:

1. The rubric and scope, including whether the assessment is static or includes runtime evaluations.
2. A table with skill name, all five dimension scores, overall score, and one concise evidence-based note. Group by repository category when the list is long.
3. Verification evidence such as validators, tests, metadata inventory, or broken-link checks, clearly separated from qualitative scoring.
4. A short synthesis covering strongest dimensions, material weaknesses, and the highest-value improvement priorities.

State that a source-and-structure-only review is not a runtime effectiveness benchmark. Do not imply measured success rates, model compatibility, accessibility, safety, or tool reliability unless representative evaluations directly established them.

## Judgment Rules

- Score the artifact that exists, not the likely intent or the reputation of its domain.
- Do not reward length, resource count, strictness, or passing tests automatically; reward justified guidance that improves correct task completion.
- Do not penalize a simple read-only skill for lacking destructive-operation policy it cannot need.
- Penalize material trigger collisions, contradictory instructions, unjustified approval gates, unverifiable completion claims, repeated content, stale references, and missing stopping conditions in the relevant dimensions.
- Lower a score for confirmed missing required evidence in the artifact. For inaccessible evidence caused by the review environment, mark the materially affected dimension unassessed rather than treating uncertainty as an artifact defect.
- Preserve meaningful score differences. Do not force a ranking or curve, and do not inflate all scores because repository-wide checks pass.

This skill scores and recommends; it does not authorize editing the assessed skills unless the user also requests changes.
