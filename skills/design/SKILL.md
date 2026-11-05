---
name: design
description: Builds or refines interfaces with the project design system, the bundled Impeccable and complete screen states. Use when a task creates or changes UI, typography, layout, color or motion, or names an Impeccable action. Not for backend-only work.
argument-hint: "[action or request] [target]"
---

# Design

Read [the shared workflow](references/workflow.md) before acting. It defines how to load the bundled Impeccable, preserve scope and check states.

## Proposal before implementation

For a UI creation/change request, load `design:mockup` before product edits. Create a reviewable artifact or a Figma/FigCraft proposal containing every applicable state from `design:states`, the relevant control variants and the responsive compositions from [responsive.md](references/responsive.md). Iterate on that proposal with the user.

Implement only after the user explicitly approves the current proposal and its scope. An approved idea is not an approved mockup. If an approval already exists for this exact proposal/scope, use it rather than asking again. Record the artifact/version and actual approval in the project. Substantial changes to the approved proposal require review of the affected changes before implementation.

Setup, diagnosis and review-only work can proceed without an implementation approval. Preparing the isolated mockup is authorized by the design request; changing production source is gated by the approval above. This gate also applies when an upstream playbook would otherwise proceed directly to code.

Resolve the target from the request and project. With no request, show the available actions and the relevant project context; do not edit automatically.

Load an entry skill with the Skill tool. Read a reference with the Read tool. The references are in the `references/` folder of this skill.

| Need | Load or read |
|---|---|
| Establish or document the system | `design:setup` |
| Explore an idea before implementation | `design:mockup` |
| Review without implementation | `design:review` |
| Visual-only iteration | `design:style` |
| Enumerate alternate states | `design:states` |
| Consolidate tokens/components | `design:system` |
| Connect a design tool | `design:connect` |
| Consistent interface patterns | [references/patterns.md](references/patterns.md) |
| Color, surface, theme or contrast changes | [references/colors.md](references/colors.md) |
| Measure legibility and control contrast | [references/contrast.md](references/contrast.md) |
| Font, hierarchy or reading changes | [references/typography.md](references/typography.md) |
| Transitions or interaction feedback | [references/motion.md](references/motion.md) |
| Breakpoints and layout across widths | [references/responsive.md](references/responsive.md) |
| Figma context or canvas work | [references/figma.md](references/figma.md) |
| FigCraft frames, components or prototypes | [references/figcraft.md](references/figcraft.md) |

For an upstream action, load its playbook through the shared workflow and honor the proposal gate. For a new screen, include its state matrix in the mockup. For a narrow refinement, check the existing states affected by the proposal. After approval and implementation, run scoped visual verification and report evidence and remaining gaps.

For UI work, always read [references/responsive.md](references/responsive.md) with the Read tool. Verify the breakpoint behavior of the project in the affected states.
