---
name: scoring-agent-skills
description: Score or compare one or more agent skills across trigger clarity, workflow actionability, safety boundaries, verification rigor, incremental knowledge value, and leanness. Use only when the user explicitly asks for ratings, numerical quality scores, rubric-based scorecards, or scored comparisons; use creating-agent-skills for unscored reviews or revisions.
---

# Scoring Agent Skills

Produce a comparable quality scorecard, not a vague impression or a runtime capability claim.

## Scope and Evidence

1. Resolve the requested skill set. For “every skill,” use the repository's active discovery tree unless the user explicitly includes deprecated or external skills.
2. Establish the target-model baseline from the user's request, the repository's model-specific guide, or the execution environment, in that order. If none identifies one, use a “general capable model” baseline and disclose that low-confidence assumption.
3. Inspect applicable repository instructions, the model-specific prompting guide, each `SKILL.md`, catalog entry, and directly linked resources relevant to a score.
4. For the trusted current repository, run its established non-destructive validators when feasible. For an external or untrusted repository, default to source inspection or a trusted validator. Do not run repository-supplied code unless it is sandboxed and the user explicitly authorizes the exact command.
5. Treat structural checks, link integrity, metadata presence, and test results as supporting evidence. They do not by themselves prove prompt quality, incremental value, or task success.
6. Before scoring, read [the rubric](references/rubric.md) and assign an integer from 1 to 10 for each assessable dimension. Apply the same anchors to every skill and assess each dimension proportionately to what the skill can do.
7. Support each score with direct evidence. For incremental knowledge value, label representative content as domain delta, justified activation, or redundancy candidate without inventing precise ratios. Revisit conspicuous outliers after the first pass so differences reflect the rubric rather than category or ordering bias.

## Calculate and Report

Use equal weight for all assessed dimensions. When all six are assessed, compute the overall score as their arithmetic mean and show one decimal place. If inaccessible evidence prevents a defensible dimension score, mark that dimension unassessed, exclude it from the aggregate, and report score coverage and confidence; do not add hidden bonuses or penalties.

Return in the user's language unless requested otherwise:

1. The rubric, scope, target-model baseline, assumptions, and whether the assessment is static or includes a representative baseline-versus-skill runtime comparison.
2. A table with skill name, all six dimension scores, overall score, and one concise evidence-based note. Group by repository category when the list is long.
3. Verification evidence such as validators, tests, metadata inventory, or broken-link checks, clearly separated from qualitative scoring.
4. A short synthesis covering the highest-value content, safely removable redundancy candidates, material weaknesses, and improvement priorities.

State that a source-and-structure-only review estimates incremental value and is not a runtime effectiveness benchmark. Only representative baseline-versus-skill evaluations can establish observed gains. Do not imply measured success rates, model compatibility, accessibility, safety, or tool reliability without direct evidence. Also state that this six-dimension aggregate is not directly comparable with historical five-dimension scores.

## Judgment Rules

- Score the artifact that exists, not the likely intent or the reputation of its domain.
- Do not reward length, resource count, strictness, passing tests, or unfamiliarity automatically; reward justified guidance that improves correct task completion.
- Do not call content redundant merely because a capable model may know it. Preserve concise disambiguation, current facts, safety and authorization boundaries, output contracts, stopping conditions, and reminders backed by observed failures.
- Do not penalize a simple read-only skill for lacking destructive-operation policy it cannot need.
- Penalize material trigger collisions, contradictory instructions, unjustified approval gates, unverifiable completion claims, repeated content, stale references, and missing stopping conditions in the relevant dimensions.
- Lower a score for confirmed missing required evidence in the artifact. For inaccessible evidence caused by the review environment, mark the materially affected dimension unassessed rather than treating uncertainty as an artifact defect.
- Preserve meaningful score differences. Do not force a ranking or curve, and do not inflate all scores because repository-wide checks pass.

This skill scores and recommends; it does not authorize editing the assessed skills unless the user also requests changes.
