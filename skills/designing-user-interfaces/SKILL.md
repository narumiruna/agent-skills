---
name: designing-user-interfaces
description: Design and review UI/UX that minimizes cognitive load without sacrificing functional completeness. Use when creating or evaluating screens, components, wireframes, navigation, workflows, dashboards, forms, or design systems; especially when deciding what stays visible, what uses progressive disclosure, how information should be prioritized, or whether an interface is cluttered or over-simplified.
---

# Designing User Interfaces

## Objective

Minimize cognitive load while preserving useful capability, agency, context, and recovery. Do not pursue visual simplicity by deleting necessary functions or moving complexity into harder navigation, memory, or repeated effort. As Apple’s HIG states, simplicity is not minimalism: keep the important things close and include what the task actually needs.

Before proposing a design, identify the primary user, current context, primary task, platform, input methods, constraints, and existing product conventions. Inspect available product evidence rather than inventing requirements or user research. Read `references/apple-hig.md` for the HIG-derived baseline; for material Apple-platform decisions, inspect the mapped source JSON in `docs/human-interface-guidelines` when it is available.

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

For each element, ask:

1. Is it necessary for the current task?
2. How often is it used, and by whom?
3. What is the consequence if it cannot be found quickly?
4. Must it remain visible, or can context reveal it at the right moment?
5. Can it be grouped with related controls or information?
6. Is the proposed entry point labeled and predictable?
7. Would hiding it increase memory, search, navigation, or recovery burden?
8. Does the design reduce complexity, or merely move it elsewhere?
9. Does the action apply to the object’s current lifecycle state, or should it appear only after a prerequisite such as saving?

When evidence is missing, state the assumption that drives the classification. Do not pretend frequency or user priority is known.

Never hide the current location, consequential system state, required input, destructive consequence, permission boundary, unsaved-work risk, error recovery, or the only accessible route to a core action. Never rely on an unlabeled icon, hidden gesture, hover, color, sound, or motion as the sole route or explanation.

## Information Hierarchy

Organize the interface in this order:

1. State the screen's purpose and preserve enough context for orientation.
2. Place the primary task and its status first.
3. Group related content and actions by user intent, not by implementation ownership.
4. Separate primary, secondary/supporting, contextual, and advanced layers.
5. Make scanning order and action priority clear through layout before decoration; account for right-to-left reading order.
6. Check narrow and wide layouts, large text, long localization, empty and dense data, loading, errors, offline behavior, permissions, and assistive-technology focus order; hierarchy must survive them all.
7. Make each title, status, badge, summary, and instruction answer a distinct question. Remove synonymous layers that repeat identity or state without helping the next decision.

Prefer the fewest visible elements that still support efficient, predictable use. Fewer elements are not automatically better.

## Design Workflow

1. **Frame the task.** Identify user, purpose, context, frequency, stakes, constraints, input methods, and success signal.
2. **Inventory capability, state, and ownership.** List actions, information, dependencies, current location, loading, empty, success, error, offline, disabled, permission-denied, and unsaved-work states before simplifying. Identify which surface owns selection and drafts so disclosure, responsive presentation, refreshes, and handoffs do not reset work.
3. **Classify visibility.** Apply the visibility table and explain uncertain classifications.
4. **Structure the hierarchy.** Define regions, groups, reading and focus order, primary action, and disclosure paths. Generally limit prominent actions to one or two per view.
5. **Protect discoverability.** Give every hidden capability a clear label, obvious entry point, predictable location, minimal depth, return path, and consistent interaction.
6. **Protect accessibility.** Check semantic labels, contrast, noncolor cues, text scaling and reflow, target size and spacing, keyboard and assistive operation, gesture alternatives, and reduced motion.
7. **Match feedback to stakes.** Put routine status and validation near the affected object. Use interruption only when the information is critical and actionable; make irreversible or unexpected consequences explicit.
8. **Audit overload and false simplicity.** Check competing emphasis, dense choices, decorative noise, extra steps, menu hunting, context loss, hidden status, recall, and repeated work.
9. **Test adaptation, transitions, and edge states.** Exercise the smallest and largest layouts, largest text, long translated and right-to-left content, empty and dense data, all supported inputs, errors, offline operation, permissions, cancellation, and recovery. Test stateful transitions — create, switch panel/item/workspace, refresh, reject or accept discard, save, fail, and retry — because static screenshots cannot prove draft preservation or recovery.
10. **Explain and validate tradeoffs.** Tie each choice to purpose, frequency, consequence, context, evidence, accessibility, or convention; name what user evidence or testing would change it.

## Required Output

For a proposal or review, include:

1. **Primary task and context** — who is doing what, where, and under which assumptions.
2. **Action priority** — primary, secondary/supporting, contextual, and advanced actions.
3. **Information hierarchy** — scan order, grouping, emphasis, and status placement.
4. **Always visible** — functions and information that must remain on the surface, with reasons.
5. **Progressively disclosed** — what is initially hidden and why.
6. **Discoverability path** — label, location, trigger, navigation depth, and return path for hidden functions.
7. **Cognitive-overload risks** — simultaneous choices, density, competing emphasis, or irrelevant content.
8. **Over-simplification risks** — buried capability, extra steps, hidden state, recall burden, or lost context.
9. **Tradeoffs and alternatives** — what improves, what worsens, and what evidence would change the decision.
10. **Accessibility, convention, and validation check** — supported inputs and assistive paths, adaptation and edge states, relevant platform/product patterns, applicable HIG topics for Apple work, and how the design should be tested.

Do not stop at adjectives such as “clean,” “simple,” or “modern.” Name the concrete structural decision and its effect on user effort.

## References

- Read `references/apple-hig.md` for the HIG-derived product, accessibility, layout, action, feedback, modality, writing, privacy, and motion baseline. For material Apple-platform decisions, inspect the mapped archived topic and exact component page.
- Read `references/preferences.md` before choosing visual density, shape, motion, color, or information amount. Project requirements, user evidence, platform conventions, and accessibility needs override its defaults.
- Read `references/cases.md` when a listed pattern resembles the current problem or when reviewing whether a proposal creates false simplicity.

Maintain this skill in three layers:

- Keep durable usability rules in this file.
- Put project-adjustable visual preferences in `references/preferences.md`.
- Add concrete liked and disliked patterns to `references/cases.md`, including the context and reason; do not turn isolated taste into a universal rule.
