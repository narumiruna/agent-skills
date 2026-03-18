---
name: imrad-writer
description: Use when producing research-style outputs that should follow IMRaD (Introduction, Methods, Results, Discussion).
---

# IMRaD Skill

## Purpose

Generate outputs strictly following the IMRaD structure:

- Introduction
- Methods
- Results
- Discussion

IMRaD is a standardized structure widely used in scientific writing to present research logically and clearly.

## When to use

Use this skill when the user:

- Asks for research-style writing
- Needs structured analysis or reports
- Wants systematic reasoning (problem -> method -> result -> interpretation)
- Requests academic, technical, or experimental explanations

## When NOT to use

Do NOT use this skill when:

- The task is simple explanation or Q&A
- The user asks for tutorials or step-by-step guides
- The task is brainstorming or ideation
- No clear "method -> result" structure exists

## Heuristic (quick decision rule)

Use IMRaD only if ALL are present:

- A clearly defined question or problem
- A describable method or approach
- Observable or derivable results
- A need to interpret those results

## Handling Incomplete Inputs

If the input lacks explicit methods or results, the agent MUST:

- Infer a reasonable method
- State assumptions explicitly in Methods
- Generate logically consistent Results

## Output Requirements

The output MUST:

- Follow IMRaD section order exactly
- Use clear section headers
- Be concise, precise, and non-redundant
- Avoid mixing content across sections
- Maintain logical flow

## Section Specifications

### 1. Introduction

- Define background and context
- Identify the problem or research question
- State objective or hypothesis

Constraint:

- No methods, results, or conclusions here

### 2. Methods

- Describe approach, methodology, or process
- Include assumptions, tools, or data sources
- Ensure reproducibility when applicable

Constraint:

- No interpretation or results

### 3. Results

- Present findings, outputs, or observations
- Use structured bullet points if helpful
- Stay objective and factual

Constraint:

- No interpretation, explanation, or implication
- Only describe observations or outputs

### 4. Discussion

- Interpret results
- Explain implications and significance
- Compare with expectations or prior knowledge
- Explicitly answer the research question from Introduction
- Mention limitations and possible next steps

## Style Constraints

- Language MUST be concise and precise
- Avoid narrative storytelling
- Prefer structured bullets over long paragraphs
- No filler or meta commentary
- No repetition across sections

## Optional Extensions

Include ONLY if explicitly requested:

- Abstract (summary of all sections)
- Conclusion (can be merged into Discussion)

## Example Invocation

User input:
"Analyze why async does not solve race conditions in file writes"

Expected structure:

## Introduction

...

## Methods

...

## Results

...

## Discussion

...

## Failure Modes (MUST avoid)

- Mixing Results with Discussion
- Introducing conclusions before Results
- Writing unstructured essays
- Skipping sections
