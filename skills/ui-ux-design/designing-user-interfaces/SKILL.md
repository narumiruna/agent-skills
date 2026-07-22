---
name: designing-user-interfaces
description: Design, implement, or review screens, components, navigation, workflows, forms, dashboards, and design systems for clear hierarchy, low cognitive load, accessibility, and preserved capability, using Apple-derived philosophy adapted to the target platform. Use especially for visibility, progressive-disclosure, clutter, or over-simplification decisions.
---

# Designing User Interfaces

Minimize cognitive load without sacrificing capability, agency, context, or recovery. Apply Apple-derived principles through the target platform's conventions; do not copy platform-specific components or metrics blindly.

## Choose the Mode

- **Proposal:** Recommend the smallest coherent structure and explain material hierarchy, disclosure, accessibility, and tradeoffs.
- **Review:** Lead with prioritized findings tied to user effort, risk, evidence, or convention.
- **Implementation:** Inspect the current interface and design system, make the bounded requested change, and verify affected states and interactions.

Identify the primary user, task, context, platform, inputs, constraints, and product conventions from available evidence. Do not invent research, business rules, capabilities, defaults, success claims, or destructive consequences. Preserve behavior, content meaning, data semantics, permissions, persistence, and recovery unless authorized evidence requires a change. Ask one question only when a missing product decision blocks safe work; otherwise leave uncertain behavior unchanged and label the unknown.

## Design Principles

1. **Purpose and agency:** Put the job people came to do first. Preserve exit, cancel, undo, and recovery paths.
2. **Clarity with capability:** Reorganize useful functions through hierarchy, grouping, context, and progressive disclosure before removing them.
3. **Visible critical paths:** Keep primary, frequent, consequential, time-sensitive, and safety/status information apparent. Never style a destructive action as the default.
4. **Predictable disclosure:** Give advanced or infrequent capability a labeled, stable, shallow path with visible cues and a clear return.
5. **Structural hierarchy:** Use reading order, grouping, spacing, typography, alignment, and contrast before decorative containers or color.
6. **Recognition over recall:** Prefer clear labels, standard controls, persistent context, and familiar patterns over hidden gestures, hover-only actions, or unexplained icons.
7. **Accessible operation:** Never make color, sound, motion, gesture, pointer, or position the sole carrier of meaning or access. Support relevant text scaling, reflow, assistive technology, alternative input, target size, contrast, and reduced motion.
8. **Proportionate feedback:** Keep routine status near its object; reserve interruptions and confirmations for critical, actionable, unexpected, or hard-to-reverse events.
9. **No false simplicity:** Reject cleanup that increases search, navigation depth, repeated effort, uncertainty, context loss, hidden dependencies, or inaccessible interaction.
10. **Adaptive identity:** Preserve recognizable structure and priority across supported widths, content states, text sizes, localization, right-to-left layout, permissions, and inputs.
11. **Clear ownership:** Give each workspace or surface a distinct responsibility; keep handoffs shallow and preserve selection, drafts, and context.

## Visibility Classification

| Class | Presentation |
| --- | --- |
| Primary | Direct, labeled, prominent |
| Supporting | Visible with lower emphasis near its object |
| Contextual | Revealed for the relevant item, role, state, or step |
| Advanced | Labeled progressive disclosure or dedicated view |
| Safety/status | Visible at the relevant time; interrupt only when needed |
| Redundant/irrelevant | Remove only after proving no capability, cue, status, or recovery path is lost |

Classify by task necessity, audience/frequency evidence, consequence if missed, lifecycle state, and the search, memory, navigation, or recovery cost of hiding it. Never hide location, consequential state, required input, destructive consequences, permission boundaries, unsaved-work risk, error recovery, or the only accessible route to a core action.

## Workflow

1. Inventory the relevant capabilities, information, states, dependencies, and ownership before simplifying.
2. Classify visibility, then structure regions, reading/focus order, action priority, status placement, and disclosure paths.
3. Protect accessibility and discoverability using the principles above.
4. Exercise directly affected layouts, content densities, inputs, failures, permissions, cancellation, transitions, and recovery states that the product supports. Do not invent unsupported states to complete a checklist.
5. Audit both overload and false simplicity; tie decisions to purpose, evidence, consequence, accessibility, or convention.
6. Stop when the requested surface and its affected states are addressed. Report the result first, checks performed, material tradeoffs, and unverified scenarios.

Use `references/apple-hig.md` for deeper HIG-derived or Apple-platform decisions, `references/preferences.md` for adjustable visual defaults, and `references/cases.md` for comparable patterns. Product evidence, platform conventions, and accessibility override preferences.
