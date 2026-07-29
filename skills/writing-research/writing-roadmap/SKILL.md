---
name: writing-roadmap
description: Create, revise, or review outcome-oriented product and system roadmaps that connect vision and current state to measurable objectives, themes, phased milestones, technical health, risks, dependencies, success metrics, non-goals, and decision history. Use for strategic roadmap artifacts; use writing-plans for task-level implementation plans, checklists, or execution tracking.
---

# Writing Roadmaps

A roadmap expresses strategic direction and sequencing, not a promise of delivery dates or an implementation checklist. Creating or revising one authorizes changes to the roadmap artifact only, not implementation of its initiatives. For a review-only request, report findings without rewriting unless asked.

## Ground the Roadmap

Inspect provided material and relevant repository evidence before drafting. Establish the audience, scope, planning horizon, and current baseline. Ask at most one question when a missing answer would materially change the roadmap; otherwise proceed with explicit assumptions or unknowns.

Separate verified current state, approved commitments, and proposed direction. Do not invent capabilities, dates, targets, owners, capacity, dependencies, or certainty.

Save a created or revised roadmap to the repository unless the user requests chat-only output. Default to `docs/roadmaps/YYYY-MM-DD_<topic>-roadmap.md`; derive a concise lowercase kebab-case topic, create the directory when needed, and update an existing roadmap in place.

## Use the Required Structure

Keep these sections in order. When evidence is unavailable, state the gap and its consequence instead of filling it with generic claims.

1. **Vision** — One clear statement of the durable purpose and desired future state.
2. **Objectives** — A small set of near- to mid-term outcomes supporting the vision. Make them measurable when baselines, targets, and horizons are known.
3. **Current State** — Evidence-backed capabilities, constraints, limitations, and key challenges that explain why the roadmap is needed.
4. **Guiding Principles** — Decision rules that resolve likely prioritization or tradeoff questions; avoid generic values that change no decision.
5. **Roadmap Themes** — Outcome-oriented strategic pillars spanning related initiatives. Do not use teams, components, or feature lists as themes unless they genuinely express strategy.
6. **Phases and Milestones** — Sequential stages that move from the current state toward the objectives. Adapt the phase count and names to the evidence; use Foundation, Expansion, Maturity, and Evolution only when they accurately describe the progression.
7. **Technical Health** — Stability, performance, security, scalability, maintainability, observability, and technical-debt needs relevant to delivery.
8. **Risks and Dependencies** — Material uncertainties, blockers, sequencing constraints, and external or internal prerequisites, with mitigations or decisions needed when known.
9. **Success Metrics** — Quantifiable indicators tied to objectives. Include baseline, target, horizon, and measurement source only when grounded.
10. **Non-Goals** — Explicit exclusions that prevent scope drift or false expectations.
11. **Decisions and Changes** — Significant decisions and roadmap revisions with their rationale and impact. State that no prior record was supplied rather than inventing history.

Format every phase consistently:

```markdown
### Phase N: <outcome-focused name>

**Milestones:**

- <observable delivered capability, validated assumption, or consequential decision>

**Outcome:** <the state this phase establishes and what it unlocks>
```

Milestones describe verifiable results, not activities such as “work on,” “improve,” or “explore” without a decision criterion. Add dates or calendar ranges only when the user supplies them or evidence supports them.

## Check Strategic Coherence

Before handoff, verify that:

- Vision → objectives → themes → milestones → metrics form a traceable chain.
- Each phase has a distinct outcome, logical dependencies, and a credible transition to the next phase.
- Technical-health work appears in the phases that need it rather than becoming an unsequenced side list.
- Risks distinguish uncertainty from dependency and pair material items with mitigation, a decision, or a monitoring signal when possible.
- Metrics measure outcomes rather than output volume, and unsupported targets remain explicit unknowns.
- Non-goals draw meaningful boundaries, while the decision log preserves significant changes without rewriting history.

Lead with the completed roadmap or review verdict. Follow it only with material assumptions, evidence gaps, or decisions still required.

## Revise and Hand Off

When revising a roadmap, preserve prior significant decisions and append the change, rationale, and impact; update affected objectives, phases, risks, metrics, and non-goals so the document remains internally consistent.

If the user asks to turn an approved phase or milestone into executable work, use `writing-plans` for the implementation plan. Keep the roadmap strategic and do not replace its outcomes with task checkboxes.
