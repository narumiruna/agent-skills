---
name: imrad-structure-detector
description: Use when deciding whether IMRaD is appropriate and diagnosing which IMRaD components are explicit, partial, inferable, or missing.
---

# IMRaD Structure Detector

## Purpose

Determine whether a task or source material is suitable for IMRaD treatment.

## When to use

Use this skill when the user:

- Asks whether IMRaD should be applied
- Provides fragmented material and needs structure diagnostics
- Needs a go/no-go decision before IMRaD generation

## When NOT to use

Do NOT use this skill when:

- The user explicitly asks for full IMRaD writing now
- The task is purely stylistic editing
- The task is unrelated to research-style analytical structure

## Core Tasks

- Evaluate IMRaD applicability
- Detect section availability for Introduction, Methods, Results, Discussion
- Classify each section as explicit, partial, inferable, or unavailable
- Identify assumptions required to proceed
- Recommend full IMRaD, partial IMRaD, or no IMRaD

## Decision Rules

Use IMRaD only when ALL are true:

- A clear question or problem exists
- A method exists or can be reasonably inferred
- Results exist or can be responsibly scoped as non-empirical
- Interpretation is needed

Lower applicability when the task is simple Q&A, tutorial content, or brainstorming without a meaningful method-result path.

## Output Requirements

The output MUST include:

- IMRaD applicability: high, medium, or low
- Section availability:
  - Introduction
  - Methods
  - Results
  - Discussion
- Inferred components
- Key assumptions required
- Recommendation:
  - use full IMRaD
  - use partial IMRaD
  - do not use IMRaD

## Truthfulness Constraints

- The agent MUST NOT claim missing empirical evidence exists
- Non-empirical results MUST be labeled as inferred, hypothetical, expected, or simulated
- The detector MUST diagnose only; it MUST NOT output a full IMRaD article

## Failure Modes

- Over-triggering on simple explanatory tasks
- Treating unavailable evidence as observed results
- Giving a recommendation without assumptions
- Collapsing diagnosis into full drafting
