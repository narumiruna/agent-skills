---
name: applying-imrad
description: Use when deciding whether IMRaD fits, drafting a fresh IMRaD output, transforming mixed material into IMRaD, or reviewing an IMRaD draft for structure, evidence, and section-boundary correctness.
---

# Applying IMRaD

## Overview

Single entry skill for IMRaD work. First choose one mode, then apply the shared IMRaD rules and the mode-specific workflow. Do not ask the user to name a mode unless the prompt is genuinely ambiguous and the choice would materially change the deliverable.

## Use IMRaD Only When

Use IMRaD only if ALL are true:

- A clear question or problem exists
- A method exists or can be responsibly inferred
- Results exist or can be responsibly scoped as non-empirical
- Interpretation is needed

Do NOT use IMRaD for:

- Simple Q&A or plain explanations
- Tutorials or step-by-step guides
- Brainstorming or ideation without a meaningful method-result path
- Purely stylistic editing with no structural IMRaD objective

## Mode Selection

Choose exactly one mode:

1. **Reviewer**: The input is already an IMRaD draft and the user wants review, audit, diagnosis, or structural quality checks.
2. **Detector**: The user asks whether IMRaD should be used, which IMRaD parts are present, or what assumptions would be needed to proceed.
3. **Recomposer**: The user provides notes, transcripts, mixed reasoning, or non-IMRaD material and wants it reorganized into IMRaD.
4. **Writer**: The user wants a fresh research-style output in IMRaD and there is no existing draft to review.

Tie-breakers:

- Existing IMRaD draft plus review language means **Reviewer**, not Recomposer.
- Applicability or readiness questions mean **Detector**, not Writer.
- Non-IMRaD source material plus "turn this into IMRaD" means **Recomposer**.
- If the user wants a complete IMRaD output and does not explicitly ask for applicability diagnosis first, proceed with **Writer** or **Recomposer** and surface assumptions in Methods.

## Shared Rules

- Keep IMRaD section boundaries strict.
- Never fabricate empirical data, citations, experiments, measurements, or observations.
- If the input is incomplete, state assumptions explicitly.
- Non-empirical results MUST be labeled as `inferred`, `hypothetical`, `expected`, or `simulated`.
- Every major claim in Results or Discussion MUST trace back to explicit input evidence or explicit assumptions.
- Be concise, precise, and non-redundant.
- Prefer bullets over long narrative paragraphs when they improve clarity.

## Section Rules

Apply these rules whenever producing a full IMRaD document.

### Introduction

- Define background and context
- Identify the question, problem, or objective
- State the objective or hypothesis
- Do NOT include methods, results, or conclusions

### Methods

- Describe the approach, process, tools, data sources, and assumptions
- Include reproducibility details when applicable
- Put inferred assumptions here when the input is incomplete
- Do NOT include findings or interpretation

### Results

- Present findings, outputs, or observations objectively
- Separate empirical from non-empirical outputs when both appear
- Do NOT include interpretation, implication, or argument

### Discussion

- Interpret only what Results support
- Answer the question from Introduction
- Include limitations and concrete next steps when relevant

## Mode Workflows

### Detector

Use when the user needs an IMRaD go/no-go decision or a gap analysis.

Workflow:

1. Evaluate IMRaD applicability.
2. Classify Introduction, Methods, Results, and Discussion as `explicit`, `partial`, `inferable`, or `unavailable`.
3. Identify the assumptions required to proceed responsibly.
4. Recommend `use full IMRaD`, `use partial IMRaD`, or `do not use IMRaD`.

Output MUST include:

- IMRaD applicability: `high`, `medium`, or `low`
- Section availability for Introduction, Methods, Results, Discussion
- Inferred components
- Key assumptions required
- Recommendation

Constraints:

- Diagnose only
- Do NOT output a full IMRaD article by default
- Do NOT treat missing evidence as observed results

### Reviewer

Use when the input is an IMRaD draft and the task is review rather than rewriting.

Workflow:

1. Validate section presence and order.
2. Check section-boundary purity.
3. Trace major claims to Results evidence or explicit assumptions.
4. Flag unsupported claims, over-interpretation, and weak question-method-result linkage.
5. Produce actionable fixes with severity.

Output MUST include:

- Overall assessment
- Strengths
- Issues list with:
  - `severity`: `high`, `medium`, or `low`
  - `section`
  - `problem`
  - `why it matters`
  - `suggested fix`
- Optional verdict: `structurally sound`, `needs revision`, or `unsuitable as IMRaD`

Constraints:

- Review the draft; do NOT rewrite the full document unless the user explicitly asks
- Do NOT invent missing evidence
- Distinguish empirical vs non-empirical results when reviewing claims

### Recomposer

Use when non-IMRaD or mixed material needs to become a clean IMRaD draft.

Workflow:

1. Extract the core question or problem.
2. Derive or identify the method or approach.
3. Separate findings from interpretation.
4. Compose Introduction, Methods, Results, and Discussion in exact order.
5. Validate claim traceability and section boundaries before finalizing.

Output MUST:

- Produce a full IMRaD document in exact section order
- Use the Section Rules above
- Make assumptions explicit in Methods
- Label non-empirical results explicitly

Constraints:

- Do NOT hide inferred assumptions
- Do NOT introduce claims unsupported by source material or explicit assumptions
- Do NOT collapse reporting and interpretation into the same section

### Writer

Use when the user wants a fresh research-style IMRaD output from a question, topic, or task brief.

Workflow:

1. Define the question, objective, or hypothesis.
2. Describe the method or analytical approach.
3. Present results objectively.
4. Interpret the results in Discussion.

Output MUST:

- Produce a full IMRaD document in exact section order
- Use the Section Rules above
- Keep results objective and discussion interpretive
- Mark any non-empirical results explicitly

Constraints:

- If methods or results are missing, infer them only for analytical or design-oriented tasks
- Put assumptions in Methods
- Optional `Abstract` or `Conclusion` sections are allowed only when the user explicitly asks for them

## Common Failures

- Over-triggering IMRaD for simple explanatory tasks
- Mixing Results with Discussion
- Rewriting a draft when the user only asked for review
- Presenting inferred content as observed evidence
- Skipping assumptions that were necessary to build Methods or Results
