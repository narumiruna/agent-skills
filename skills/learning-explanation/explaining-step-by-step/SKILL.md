---
name: explaining-step-by-step
description: Use when the user asks for a detailed, beginner-friendly, or step-by-step explanation; wants to understand how or why something works; asks to unpack a concept, issue, PR, code change, system, error, document, or technical decision; or says to explain it like teaching a child.
---

# Explaining Step by Step

Build understanding progressively: establish the big picture first, then add only the background, mechanics, evidence, and detail needed to answer the user's real question.

## Establish the Target

1. Identify what the user wants to understand and which question they are actually asking about it.
2. Infer their starting point from the request and conversation. Use their language. If their level is unknown, assume little prerequisite knowledge; ask about it only when the answer would materially change.
3. For an issue, PR, code path, error, or document, inspect the available source, diff, discussion, logs, and tests before explaining. If the referenced artifact cannot be identified or accessed, ask only for the minimum missing identifier or content.
4. Separate:
   - **Known:** directly supported by the available material.
   - **Inferred:** a reasoned interpretation that is not explicitly confirmed.
   - **Unknown:** information the material does not establish.

Do not present a plausible cause as the confirmed cause or an inferred motivation as the author's intent.

## Explain in Progressive Layers

Use the layers that help; merge or skip layers for simple material rather than forcing a long template.

1. **Orient:** In a few sentences, state what this is and why it matters to the user's question.
2. **Prepare:** Define only the terms and background needed for the next layer. Define jargon in plain language on first use.
3. **Decompose:** Break the subject into parts, events, or changes in a natural order.
4. **Connect:** Explain causality, data flow, control flow, state changes, or before/after relationships step by step.
5. **Demonstrate:** Add a concrete, traceable example, analogy, minimal code fragment, diff excerpt, or small calculation when it improves understanding.
6. **Qualify:** Cover practical effects, limitations, risks, exceptions, or tradeoffs that materially affect the mental model.
7. **Reinforce:** End with a short restatement of the mental model or the few points worth remembering.

Prefer a clear causal chain over a list of disconnected facts. Keep detail proportional to the request: detailed does not mean exhaustive.

## Adapt to the Subject

Do not force every subject into the same headings. Emphasize the sequence that fits:

- **Concept or system:** intuition → essential terms → exact mechanism → limitations.
- **Issue or error:** symptom → expected versus actual behavior → evidence → confirmed or possible cause → impact and handling direction.
- **PR or code change:** goal → before and after → important diff and execution flow → tests, effects, risks, and tradeoffs.
- **Document or decision:** context → decision or claim → reasoning → consequences.

Point to relevant files, sections, hunks, logs, or tests when that helps the user connect the explanation to its evidence.

## Use Examples Carefully

- Choose the smallest familiar example that exposes the mechanism; do not add examples merely to decorate the answer.
- Walk through meaningful state changes instead of showing code, math, a diff, or a data flow without explaining it.
- When using an analogy, state what maps to the real system and where the analogy stops matching.
- Simplify vocabulary and prerequisites, not the truth. Never create a false mental model for the sake of sounding easy.
- Treat “explain it like teaching a child” as a request for low assumed knowledge, not for childish or patronizing language.

## Control the Teaching Pace

- By default, complete the useful simple-to-deep explanation in one response.
- For a genuinely complex or multi-stage subject, or when the user appears stuck, pause at a natural boundary and ask one concrete comprehension or next-depth question before continuing.
- If the user asks for the complete explanation in one response, do not interrupt it with checkpoints.
- On follow-up questions, continue from the current layer instead of repeating the whole introduction.
- If the user explicitly asks for a brief answer, raw result, code only, or no explanation, follow that instruction instead of producing a tutorial.

## Keep the Boundary Clear

This skill explains material. It does not by itself approve a PR, perform a code review, diagnose and fix an issue, or modify code. When the user also requests one of those outcomes, combine this explanatory approach with the skill or workflow responsible for that work.
