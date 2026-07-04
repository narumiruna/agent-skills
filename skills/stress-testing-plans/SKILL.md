---
name: stress-testing-plans
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when the user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

# Stress Testing Plans

## Purpose

Stress-test a user's plan or design with a one-question-at-a-time interview until decisions, dependencies, assumptions, tradeoffs, and verification are explicit.

## Operating Loop

1. Build the current decision tree from the user's plan: goal, constraints, stakeholders, flows, dependencies, risks, and success criteria.
2. Before asking, answer anything discoverable from the repository by reading relevant files, searching callers/config/docs, and inspecting tests or commands.
3. Ask exactly one question at a time. Pick the highest-leverage unresolved decision whose answer unblocks later branches.
4. For each question, include:
   - `Question:` the single thing the user must answer next.
   - `Recommended answer:` the answer you would choose, with enough rationale to be useful.
5. After each user answer, update the shared understanding, resolve dependent branches, and ask the next question.
6. If an answer conflicts with repository evidence or an earlier decision, call out the conflict and ask the smallest clarifying question.

## Question Priority

Prefer questions that resolve, in order:

1. Goal and success criteria.
2. Constraints, non-goals, and hard requirements.
3. Existing architecture and codebase facts.
4. Interfaces, data model, state ownership, and control flow.
5. Failure modes, security, migration, rollout, and observability.
6. Test and verification criteria.

## Pairing With Writing Plans

Do not draft a plan while the interview is still resolving major branches. If the user asks to create or update a plan document after grilling, load `writing-plans` and follow its file/output rules using the agreed decisions.

## Stop Condition

Stop only when no major unresolved branch remains. End with the agreed decisions, remaining risks or unknowns, and the recommended next step.
