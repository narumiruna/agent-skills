---
name: imrad-reviewer
description: Use when reviewing an IMRaD draft for structural integrity, evidentiary support, and section-boundary correctness.
---

# IMRaD Reviewer

## Purpose

Review an existing IMRaD draft for structural, logical, and evidentiary quality.

## When to use

Use this skill when the user asks to:

- Audit IMRaD structure quality
- Find section-boundary violations
- Identify unsupported or over-interpreted claims
- Decide whether a draft is structurally publishable

## When NOT to use

Do NOT use this skill when:

- The user asks for first-pass drafting from raw notes
- The user asks for full document rewrite by default
- The input is not an IMRaD draft and no review target exists

## Review Criteria

- Introduction defines a concrete question/problem
- Methods are sufficient for the document scope
- Results are objective and non-interpretive
- Discussion interprets only what Results support
- Linkage is intact: question -> method -> result -> interpretation
- Limitations and assumptions are present where needed

## Review Workflow

1. Validate section presence and order.
2. Check section-boundary purity.
3. Trace major claims to Results evidence or explicit assumptions.
4. Flag unsupported claims and over-interpretation.
5. Produce actionable fixes with severity.

## Output Requirements

The output MUST include:

- Overall assessment
- Strengths
- Issues list, where each issue includes:
  - severity: high, medium, or low
  - section
  - problem
  - why it matters
  - suggested fix
- Optional final verdict:
  - structurally sound
  - needs revision
  - unsuitable as IMRaD

## Severity Model

- High: structural breakage, fabricated or unsupported core claims, major section mixing
- Medium: weak linkage, under-specified methods, incomplete limitations
- Low: clarity, concision, or minor organization issues

## Truthfulness Constraints

- The reviewer MUST NOT invent missing evidence
- The reviewer MUST distinguish empirical vs non-empirical results
- Non-empirical results MUST be explicitly labeled as inferred, hypothetical, expected, or simulated

## Failure Modes

- Rewriting the full draft instead of reviewing
- Mixing structural critique with factual speculation
- Missing contradictions between Results and Discussion
- Providing non-actionable feedback
