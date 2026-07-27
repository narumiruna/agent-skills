---
name: designing-user-experiences
description: Design or redesign end-to-end user experiences for new or existing digital products through an approval-gated workflow. Use for substantial work on user goals, information architecture, navigation, workflows, system states, or interaction behavior that requires a proposal before implementation.
---

# Designing User Experiences

Ground the experience in the product's actual users, workflows, platform, design system, and constraints. Do not transplant another product's labels, visual patterns, or information architecture. Treat unsupported claims about users, frequency, risk, or platform behavior as assumptions rather than facts.

## Establish the Experience Context

Choose the applicable context, then gather enough evidence to support the proposal.

### New Product

1. Inspect available product briefs, user research, requirements, domain rules, platform conventions, technical constraints, and accessibility requirements.
2. Identify the intended user groups, the jobs they need to complete, and the evidence or assumptions behind those choices.
3. Inventory proposed capabilities and classify them as primary, secondary, advanced, destructive, or deferred. Do not invent research, business rules, or implementation constraints.
4. Evaluate proposed flows by expected frequency, importance, complexity, risk, and reversibility. Mark unvalidated expectations for later testing.
5. Define the intended state model, dependencies, cancellation and recovery paths, and measurable outcomes without implying that unbuilt behavior already exists.

### Existing Product

1. Inspect the relevant interface, code, tests, user-facing documentation, stored formats, supported screen sizes and inputs, and accessibility conventions.
2. Identify the primary user groups, the jobs they are trying to complete, and the current paths to those outcomes.
3. Inventory features and classify them as primary, secondary, advanced, destructive, or compatibility-only. Preserve unknown capabilities until their ownership and use are understood.
4. Evaluate affected flows by evidence-backed frequency, importance, complexity, risk, and reversibility.
5. Map current state, transitions, dependencies, cancellation and recovery paths, then identify avoidable steps, inconsistent behavior, unclear state, and usability failures.

Label assumptions, unknowns, and product decisions that require confirmation. For existing products, preserve current behavior where evidence is incomplete.

## Shape the Proposal

Organize the experience around user goals rather than internal settings or data structures. Prioritize a small set of frequent and important actions while applying these constraints. Treat primary, secondary, advanced, destructive, and similar classifications as analysis and prioritization inputs, not as required sections, menus, pages, or navigation levels.

- Keep consequential current or proposed state visible where it informs a decision.
- Keep seven or fewer options from the same related group together at one information-architecture level by default. Express differences in frequency through ordering, labels, or visual hierarchy rather than an extra advanced section, page, menu, or navigation level.
- Starting with the eighth option, quantity may justify grouping or another level but does not require it. Split only when the workflow and scanability improve, and explain the improvement.
- Use labeled, predictable progressive disclosure when secondary or advanced complexity warrants it; do not infer disclosure from classification alone or hide critical information or the only route to a capability.
- Keep navigation shallow with clear return, cancel, and exit paths.
- Offer a small set of meaningful defaults or presets when supported, while retaining expert customization.
- Preview the concrete effect of consequential choices. Distinguish previewing, confirming, cancelling, saving, and applying through labels, state, and feedback.
- Reduce steps without removing safeguards for destructive or hard-to-reverse actions. The option-count threshold limits unnecessary information-architecture depth, not confirmation dialogs, risk warnings, or other required safety flows.
- Maintain consistent terminology, navigation, confirmations, and cancellation behavior.
- Adapt hierarchy and interaction to supported widths, content sizes, localization, inputs, and assistive technology. Avoid ambiguous truncation, inaccessible overflow, hidden critical information, and disruptive layout shifts.

Present:

1. The evidence-backed findings, assumptions, and capability classification.
2. The proposed information architecture and primary, secondary, advanced, destructive, and recovery flows.
3. Intended loading, empty, success, error, disabled, and partial states, including where status and actionable feedback appear.
4. Concrete acceptance criteria for behavior, responsiveness, keyboard and focus operation, screen readers, contrast, compatibility when applicable, tests, and documentation.
5. The main decisions, trade-offs, risks, validation needs, unresolved questions, and—when changing an existing product—compatibility and migration requirements.

Do not edit product files, tests, stored data, or user-facing documentation during this proposal phase. Wait for explicit approval of the proposal before implementation; requested revisions update the proposal and do not imply approval.

## Implement After Approval

Implement only the approved scope and preserve unrelated behavior.

- For existing products, keep backward compatibility, existing workflows, stored user data, and unknown configuration fields unless the approved proposal includes a verified migration path.
- Apply confirmed changes atomically and provide immediate success feedback. Cancellation must have no side effects.
- On failure, retain the previous valid state and show an actionable error that explains what failed and how to recover or retry.
- Keep primary actions, consequential status, validation, unsaved-work risk, and recovery paths visible at the relevant time.
- Preserve capability through stable progressive disclosure rather than deletion or ambiguous hiding.
- Verify responsive layouts without overflow or harmful shifts across supported sizes, inputs, content extremes, and text scaling.
- Support keyboard navigation, logical focus order and restoration, screen-reader semantics and announcements, non-color cues, appropriate contrast, and reduced motion where relevant.
- Add or update tests for affected primary flows, previews, confirmations, cancellations, navigation, failures, responsive behavior, accessibility, and compatibility where applicable. Test only states and environments the product supports.
- Update user-facing documentation to describe the final behavior and any approved migration.

Exercise the affected loading, empty, success, error, disabled, and partial states. Report what changed, validation evidence, approved deviations, and any scenarios that could not be verified; for existing products, also report preserved compatibility.
