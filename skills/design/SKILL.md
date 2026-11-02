---
name: design
description: Build or refine interfaces using the project's design system, bundled Impeccable and complete screen states. Use for UI work, typography, layout, color, motion or an explicit Impeccable action. Not for backend-only work.
argument-hint: "[action or request] [target]"
---

# Design

Read [the shared workflow](references/workflow.md) before acting. It defines how to load the bundled Impeccable, preserve scope and check states.

## Proposal before implementation

For a UI creation/change request, load `design:mockup` before product edits. Create a reviewable artifact or a Figma/FigCraft proposal containing every applicable state from `design:states`, the relevant control variants and responsive compositions from `design:responsive`. Iterate on that proposal with the user.

Implement only after the user explicitly approves the current proposal and its scope. An approved idea is not an approved mockup. If an approval already exists for this exact proposal/scope, use it rather than asking again. Record the artifact/version and actual approval in the project. Substantial changes to the approved proposal require review of the affected changes before implementation.

Setup, diagnosis and review-only work can proceed without an implementation approval. Preparing the isolated mockup is authorized by the design request; changing production source is gated by the approval above. This gate also applies when an upstream playbook would otherwise proceed directly to code.

Resolve the target from the request and project. With no request, show the available actions and the relevant project context; do not edit automatically.

| Need | Load |
|---|---|
| Establish or document the system | `design:setup` |
| Explore an idea before implementation | `design:mockup` |
| Review without implementation | `design:review` |
| Visual-only iteration | `design:style` |
| Enumerate alternate states | `design:states` |
| Consolidate tokens/components | `design:system` |
| Connect a design tool | `design:connect` |
| Consistent interface patterns | `design:patterns` |
| Color, surface, theme or contrast changes | `design:colors` |
| Measure legibility and control contrast | `design:contrast` |
| Font, hierarchy or reading changes | `design:typography` |
| Transitions or interaction feedback | `design:motion` |

For an upstream action, load its playbook through the shared workflow and honor the proposal gate. For a new screen, include its state matrix in the mockup. For a narrow refinement, check the existing states affected by the proposal. After approval and implementation, run scoped visual verification and report evidence and remaining gaps.

Always load `design:responsive` for UI work and verify the project's breakpoint behavior in affected states.
