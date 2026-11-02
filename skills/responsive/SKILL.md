---
name: responsive
description: Design and verify responsive screens using project breakpoints, content constraints and container sizes. Applies to every UI change and its relevant states.
argument-hint: "[screen or component]"
user-invocable: false
---

# Responsive at every state

**Rule:** every interface works across its supported widths; alternate states follow the same responsive contract as the main screen.

Read [the shared workflow](../design/references/workflow.md) and bundled adapt/layout playbooks. Inspect existing breakpoint tokens, utilities, media/container queries and supported platform constraints before adding new values.

1. Start from the narrow usable layout, then add space and structure at content-driven breakpoints. Reuse the project's existing breakpoint names/values; do not scatter arbitrary pixel thresholds through components. If none exist, propose a small shared scale and validate it against the real layouts before documenting it.
2. Record width ranges, container limits, grid columns, gutters and changes in navigation, tables, forms and overlays in DESIGN.md. Use container queries for reusable components when their own available width, rather than viewport width, determines layout and the project supports them.
3. At a breakpoint, preserve information, task completion, reading order, focus order and available actions. A smaller screen is not permission to hide essential controls. Choose wrapping, stacking, alternative composition or purposeful scrolling by content.
4. Check narrow, medium and wide widths, plus just below/at/above each breakpoint used by the changed layout. Test intermediate widths, not only device presets. Width values come from the project; there is no mandatory framework or universal phone/tablet/desktop scale.
5. Verify applicable empty, loading, error, success and content-extreme states at representative widths. Include long translations, zoom/text enlargement, orientation, touch/keyboard input and the on-screen keyboard when relevant. Avoid hover-only access to essential actions.
6. Check for clipped actions, accidental page-level horizontal scrolling, fixed-height text containers, overlapping sticky areas and dialogs extending outside the viewport. Wide data tables may have intentional accessible horizontal scrolling without making the entire page scroll sideways.
7. Record route, actual viewport/container size, theme/state and evidence. A media query existing in source is not proof that the layout works.

## Check

Does the same user goal remain achievable between breakpoints and in alternate states, with enlarged or localized content?
