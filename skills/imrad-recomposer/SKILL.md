---
name: imrad-recomposer
description: Use when transforming non-IMRaD material into a clean IMRaD output with strict section boundaries and explicit assumption labeling.
---

# IMRaD Recomposer

## Purpose

Transform non-IMRaD material into IMRaD-structured output.

## When to use

Use this skill when the user provides:

- Notes, transcripts, explanations, or fragmented analysis
- Mixed reasoning that needs separation into IMRaD sections
- Research-style analytical content requiring a production-ready IMRaD draft

## When NOT to use

Do NOT use this skill when:

- The detector recommendation is "do not use IMRaD"
- The user requests only diagnosis or review
- The task is simple Q&A, tutorials, or ideation without meaningful analytical structure

## Input Assumptions

- Input may be partial or noisy
- Source evidence may be incomplete
- Assumptions are allowed only when explicitly stated

## Core Workflow

1. Extract the core question/problem.
2. Derive or identify method/approach.
3. Separate findings from interpretation.
4. Compose sections in exact IMRaD order.
5. Validate claim traceability and section boundaries.

## Handling Incomplete Inputs

If methods or results are missing, the agent MUST:

- Infer a reasonable method only for analytical or design-oriented tasks
- State assumptions explicitly in Methods
- Use non-empirical results only when empirical results are unavailable
- Label non-empirical results as inferred, hypothetical, expected, or simulated

## Truthfulness Constraints

- The agent MUST NOT fabricate empirical data, citations, experiments, measurements, or observations
- Every major claim in Results and Discussion MUST be traceable to explicit input evidence or explicit assumptions

## Output Requirements

The output MUST:

- Follow IMRaD order exactly: Introduction, Methods, Results, Discussion
- Use clear section headers
- Keep boundaries clean between reporting and interpretation
- Be concise, precise, and non-redundant
- Prefer bullets where helpful

## Section Specifications

### Introduction

- Define context and question
- State objective or hypothesis
- MUST NOT include methods, results, or conclusions

### Methods

- Describe approach, process, tools, and assumptions
- Include reproducibility details when available
- MUST NOT include interpretation or findings

### Results

- Report findings objectively
- Separate empirical from non-empirical outputs
- MUST NOT include interpretation, implication, or argument

### Discussion

- Interpret only what Results support
- Answer the question from Introduction
- Include limitations and concrete next steps when relevant

## Failure Modes

- Mixing Results with Discussion
- Introducing claims unsupported by evidence or assumptions
- Hiding assumptions used to infer missing components
- Producing generic prose instead of structured analytical transformation
