# Agent Skill Scoring Rubric

Assign an integer score from 1 to 10 for every dimension. Use these shared anchors:

| Score | Meaning |
| --- | --- |
| 10 | Exemplary: no material weakness found in the inspected scope |
| 9 | Excellent: only minor, non-material improvement remains |
| 8 | Strong: reliable with one or more localized limitations |
| 7 | Adequate: usable, but notable improvement is warranted |
| 6 | Workable: a material gap limits reliability or completeness |
| 5 | Inconsistent: useful elements exist, but substantial correction is needed |
| 4 | Weak: defects regularly interfere with correct application |
| 3 | Severe: only a small portion of the dimension is reliable |
| 2 | Effectively absent or materially misleading |
| 1 | Actively harmful or incompatible with the intended task |

Use the full range when evidence supports it. Intermediate differences must reflect inspected evidence rather than a preference for round numbers.

## Trigger clarity

Assess whether frontmatter states both what the skill does and when it should activate. Check specificity, collision risk with sibling skills, explicit-invocation requirements where needed, and alignment among name, description, UI metadata, and catalog text.

Lower the score for vague domain labels, trigger rules hidden only in the body, materially overlapping descriptions without routing, or mismatched discovery surfaces.

## Workflow actionability

Assess whether the post-trigger body lets another agent complete the task. Look for clear outcomes, relevant context gathering, executable decisions, justified sequencing, scope control, stopping conditions, and a defined deliverable.

Lower the score for generic advice, over-prescribed routine steps, missing decisions, plans that cannot be executed, or workflows that stop before the requested outcome.

## Safety boundaries

Assess authorization and risk controls proportionately to the skill's actual effects. Local read-only work may need only a concise boundary; external writes, destructive actions, credentials, costs, publication, and remote mutations require explicit approval and verification rules.

Lower the score for overbroad authority, missing target/content approval, secret exposure, unsafe recovery, or blanket confirmation gates that unnecessarily block safe local work.

## Verification rigor

Assess whether important claims and outcomes require direct, relevant evidence. Look for focused checks, representative validation, current-snapshot verification, honest handling of unavailable checks, and separation between source inspection, structural validation, rendering, runtime behavior, and external state.

Apply this proportionately: an explanatory skill need not require a test suite, but it should ground claims in available sources and distinguish evidence from inference. Lower the score for unverified completion claims, stale evidence, vague “test it” language, or checks that cannot prove the stated outcome.

## Leanness and maintainability

Assess whether every instruction earns its context cost. Look for one clear purpose, low repetition, outcome-focused constraints, direct on-demand resource routing, aligned metadata, bounded examples, and stable guidance rather than incidental implementation detail.

Lower the score for duplicated trigger sections, generic background, decorative examples, unjustified files, repeated approval language, oversized unstructured bodies, or version-sensitive facts without a verification path. Do not penalize necessary complexity merely because a high-risk workflow is longer.

## Overall score

Use equal weighting:

```text
overall = (trigger + workflow + safety + verification + leanness) / 5
```

Display the result to one decimal place. Do not round or normalize individual dimension scores, apply a curve, or convert repository test results into bonus points.
