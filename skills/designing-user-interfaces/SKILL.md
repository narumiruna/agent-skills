---
name: designing-user-interfaces
description: Design, implement, and review UI/UX that minimizes cognitive load without sacrificing functional completeness, using Apple-derived design philosophy adapted to the target platform. Use when creating or evaluating screens, components, wireframes, navigation, workflows, dashboards, forms, or design systems; especially when deciding what stays visible, what uses progressive disclosure, how information should be prioritized, or whether an interface is cluttered or over-simplified.
---

# Designing User Interfaces

## Objective

Minimize cognitive load while preserving useful capability, agency, context, and recovery. Apply Apple-derived principles of purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, and delight across platforms, translating them into the target platform's conventions instead of copying Apple-specific components. Simplicity is not minimalism: keep important things close and include what the task actually needs.

Before designing, reviewing, or changing an interface, identify the primary user, current context, primary task, platform, input methods, constraints, and existing product conventions. Inspect available product evidence rather than inventing requirements or user research.

## Operating Mode

Choose the mode from the request and do not substitute a design report for requested implementation work.

- **Proposal:** Recommend the smallest coherent structure that satisfies the task, then explain material hierarchy, disclosure, accessibility, and tradeoff decisions.
- **Review:** Lead with concrete findings or a direct recommendation. Tie each issue to user effort, risk, evidence, or a violated convention.
- **Implementation:** Inspect the existing interface, design system, content, behavior, and repository conventions; make the bounded requested change and verify the directly affected states and interactions.

During implementation, preserve existing product behavior, content meaning, data semantics, validation contracts, permissions, persistence, and destructive consequences unless the request or product evidence authorizes a change. Treat current code and copy as evidence, not as an invitation to complete a speculative production flow. A destructive label alone does not establish reversibility, timing, scope, reauthentication, or recovery policy. Do not invent business rules, limits, defaults, system capabilities, success claims, consequences, or unsupported states.

If a missing product decision materially blocks safe implementation, ask at most one question. Until it is answered, leave the uncertain behavior unchanged and make only improvements that do not depend on that decision. In a proposal or review, frame unsupported behavior as a decision or open question, not an assumed fact.

Keep the effort and code change proportional to the requested surface and risk. Prefer the smallest coherent change that uses the existing design system. Do not turn a small implementation into a full redesign or exhaustive audit, and do not redesign unrelated regions. Stop when the requested task, directly affected states, accessibility paths, and recovery behavior are addressed; report unsupported or unverified scenarios instead of inventing them.

## Stable Principles

1. **Serve a clear purpose.** Prioritize the job people came to do and get them to content or action without unnecessary setup, ceremony, or lock-in.
2. **Preserve agency and recovery.** Let people explore, exit, cancel, undo, and recover without losing work. Guided or modal flows need obvious escape and safe dismissal.
3. **Prioritize clarity over simultaneous visibility.** Guide attention to the most important task in the current state instead of showing every action and datum at once.
4. **Preserve functionality.** Reorganize useful capabilities through hierarchy, grouping, contextual presentation, progressive disclosure, secondary menus, or dedicated detail views before considering removal.
5. **Keep critical paths apparent.** Make primary, frequent, essential, time-sensitive, and contextually important actions directly visible. Give destructive actions an explicit, predictable entry point, but never style one as the primary/default action.
6. **Hide complexity, not capability.** Disclose advanced or infrequent functions from a clearly labeled, predictable entry point with shallow navigation, visible cues that more exists, and consistent behavior.
7. **Build hierarchy structurally.** Use grouping, reading order, spacing, typography, alignment, and contrast before adding borders, colors, buttons, or containers.
8. **Optimize for recognition and familiarity.** Prefer clear labels, visible cues, standard controls, platform patterns, and persistent context over recall, abstract icons, hidden gestures, or unexplained state.
9. **Design accessibly from the start.** Never make color, sound, motion, gesture, pointer, or spatial position the sole carrier of essential meaning or functionality. Support text scaling, assistive technology, alternative inputs, adequate targets, contrast, and reduced motion.
10. **Match feedback and interruption to consequence.** Keep routine status near the affected object; reserve alerts and confirmations for critical, actionable, unexpected, or hard-to-reverse situations.
11. **Avoid false simplicity.** A cleaner surface is worse if it increases search time, navigation depth, repeated effort, uncertainty, hidden dependencies, context loss, or inaccessible interaction.
12. **Adapt without losing identity.** Preserve recognizable structure and priority across viewport sizes, text sizes, localization, right-to-left layout, input methods, permissions, and content states.
13. **Follow conventions deliberately.** Prefer established platform and product patterns unless deviation produces a specific, testable usability gain. On Apple platforms, consult the relevant HIG platform and component topics.
14. **Give each workspace a distinct responsibility.** When multiple surfaces handle the same objects, assign one canonical owner for each workflow instead of duplicating full editors. Keep cross-workspace handoffs shallow, predictable, and context preserving.

## Visibility Decision

Classify every action or information element before styling it.

| Classification | Use when | Presentation |
| --- | --- | --- |
| Primary | Required for the main task or next likely step | Directly visible, clearly labeled, visually prominent |
| Secondary/supporting | Frequently needed to understand or complete the task | Visible but lower emphasis or grouped near its object |
| Contextual | Relevant only for a selected item, state, role, or step | Reveal in that context without requiring recall |
| Advanced | Useful but infrequent, specialized, or configuration-heavy | Progressive disclosure through a labeled control or dedicated view |
| Safety/status | Needed to understand system state, consequences, permissions, errors, progress, or recovery | Visible at the relevant time and near the affected object; interrupt only when necessary |
| Redundant or irrelevant | Duplicates another path or does not support the current context | Remove only after confirming no capability, status, recovery path, or learning cue is lost |

For each element, determine its necessity for the current task, evidence of frequency and audience, consequence if missed, applicable lifecycle state, possible grouping, disclosure entry point, and the memory, search, navigation, or recovery burden of hiding it. Label missing evidence as unknown; do not convert unknown frequency, priority, or behavior into product requirements.

Never hide the current location, consequential system state, required input, destructive consequence, permission boundary, unsaved-work risk, error recovery, or the only accessible route to a core action. Never rely on an unlabeled icon, hidden gesture, hover, color, sound, or motion as the sole route or explanation.

## Information Hierarchy

Organize the interface in this order:

1. State the screen's purpose and preserve enough context for orientation.
2. Place the primary task and its status first.
3. Group related content and actions by user intent, not by implementation ownership.
4. Separate primary, secondary/supporting, contextual, and advanced layers.
5. Make scanning order and action priority clear through layout before decoration; account for right-to-left reading order.
6. Check the relevant narrow and wide layouts, text sizes, localization, content density, system states, supported inputs, and assistive-technology focus order; hierarchy must survive the conditions the product supports.
7. Make each title, status, badge, summary, and instruction answer a distinct question. Remove synonymous layers that repeat identity or state without helping the next decision.

Prefer the fewest visible elements that still support efficient, predictable use. Fewer elements are not automatically better.

## Design Workflow

1. **Frame the task.** Identify user, purpose, context, frequency, stakes, constraints, input methods, and success signal.
2. **Inventory relevant capability, state, and ownership.** List the actions, information, dependencies, and reachable states needed by the requested flow before simplifying. Identify which surface owns selection and drafts so disclosure, responsive presentation, refreshes, and handoffs do not reset work.
3. **Classify visibility.** Apply the visibility table and explain uncertain classifications.
4. **Structure the hierarchy.** Define regions, groups, reading and focus order, primary action, and disclosure paths. Generally limit prominent actions to one or two per view.
5. **Protect discoverability.** Give every hidden capability a clear label, obvious entry point, predictable location, minimal depth, return path, and consistent interaction.
6. **Protect accessibility.** Check semantic labels, contrast, noncolor cues, text scaling and reflow, target size and spacing, keyboard and assistive operation, gesture alternatives, and reduced motion.
7. **Match feedback to stakes.** Put routine status and validation near the affected object. Use interruption only when the information is critical and actionable; make irreversible or unexpected consequences explicit.
8. **Audit overload and false simplicity.** Check competing emphasis, dense choices, decorative noise, extra steps, menu hunting, context loss, hidden status, recall, and repeated work.
9. **Test relevant adaptation, transitions, and edge states.** Exercise the supported layouts, text and localization extremes, content densities, inputs, failures, permissions, cancellation, and recovery that the requested change can affect. Test relevant stateful transitions because static screenshots cannot prove preservation or recovery. Do not invent unsupported behavior to complete a checklist.
10. **Explain and validate tradeoffs.** Tie each choice to purpose, frequency, consequence, context, evidence, accessibility, or convention; name what user evidence or testing would change it.

## Output

Lead with the result appropriate to the mode: the recommended structure for a proposal, prioritized findings for a review, or the implemented changes and verification for implementation. Do not return only rationale when the user asked for working UI changes.

For a material proposal or review, cover only the dimensions that affect the decision:

1. **Task, context, and assumptions** — who is doing what and under which evidence or constraints.
2. **Action priority and information hierarchy** — scan order, grouping, emphasis, status placement, and primary versus secondary actions.
3. **Visibility and discoverability** — what stays visible, what is disclosed, and the labeled path to hidden capability.
4. **Overload and over-simplification risks** — competing emphasis, density, extra steps, hidden state, recall burden, or lost context.
5. **Tradeoffs and alternatives** — what improves, what worsens, and what evidence would change the decision.
6. **Accessibility, conventions, and validation** — supported inputs and assistive paths, relevant adaptation and edge states, target-platform patterns, and how the design should be tested.

Omit inapplicable or repetitive sections. A small component decision may need only a recommendation, the key consequence, and a verification note.

Do not stop at adjectives such as “clean,” “simple,” or “modern.” Name the concrete structural decision and its effect on user effort.

## References

- Apply the Apple-derived philosophy in this file to every platform. Read `references/apple-hig.md` when the task benefits from deeper HIG-derived reasoning or exact accessibility, layout, action, feedback, modality, writing, privacy, or motion guidance. For material Apple-platform decisions, inspect the mapped archived topic and exact platform or component page; do not apply Apple-specific metrics or controls to other platforms by default.
- Read `references/preferences.md` before choosing visual density, shape, motion, color, or information amount. Project requirements, user evidence, platform conventions, and accessibility needs override its defaults.
- Read `references/cases.md` when a listed pattern resembles the current problem or when reviewing whether a proposal creates false simplicity.

Maintain this skill in three layers:

- Keep durable usability rules in this file.
- Put project-adjustable visual preferences in `references/preferences.md`.
- Add concrete liked and disliked patterns to `references/cases.md`, including the context and reason; do not turn isolated taste into a universal rule.
