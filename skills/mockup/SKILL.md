---
name: mockup
description: Creates an inspectable UI proposal with all applicable screen states and responsive variants before implementation. Use when a new screen or a UI change needs a mockup, a prototype or user approval. Implementation waits for explicit approval of the current proposal.
argument-hint: "[screen or idea]"
---

# Mock up, iterate, approve

**Rule:** build a reviewable proposal before changing the product implementation. Only the user's explicit approval of that proposal opens implementation for its approved scope.

Read [the shared workflow](../design/references/workflow.md) and [responsive.md](../design/references/responsive.md) with the Read tool. Load `design:states` with the Skill tool. Use bundled shape/new-work playbooks for ideation and existing project context for fidelity. Do not run their product implementation steps before approval.

1. Establish the idea, target screen/flow, user goal and existing design system. Enumerate every applicable state in the state contract, including control states, recovery and content extremes. Record non-applicable categories with reasons and unresolved product rules as open decisions.
2. Choose the available review medium: a Figma/FigCraft draft when connected and desired. Otherwise, use a self-contained local HTML artifact or another inspectable mockup. When relevant, use `design:connect` and the provider guidance in [figma.md](../design/references/figma.md) or [figcraft.md](../design/references/figcraft.md). A plain written description does not substitute for a visual proposal.
3. Keep local proposal files under `docs/design/mockups/<screen>/` or the project's established prototype directory, separate from production source/routes. Do not install a new app framework or change the running product merely to create a mockup. Use controlled fictional data without invented factual marketing claims.
4. Render the main state and every applicable alternate state. Use linked frames, component variants or an interactive state switcher so the user can inspect them. Include navigation between relevant screens and show recovery, focus/feedback and motion intent where it affects understanding. Label simulated actions and data clearly.
5. Show responsive compositions at the project's relevant breakpoints. For a local interactive artifact, support resizing and explicit state selection. For fixed frames, include the narrow/medium/wide variants that have meaningfully different behavior and specify intermediate adaptation. Check contrast, typography and surface pairings in the proposal.
6. Present the artifact path or design links, state/viewport coverage, outstanding decisions and a concise description of the proposed changes. Ask for approval of the current artifact. Stop before product implementation while the answer is pending; silence, elapsed time, approval of the idea alone or a previous artifact is not approval of this version.
7. Iterate in the artifact on feedback. Keep the state contract current. Once the user approves, record the approved artifact/version, scope, decisions and pending implementation verification in `docs/design/mockups/<screen>/APPROVAL.md` or the existing project equivalent. Record actual approval only; do not prefill it as granted.
8. Implement only the approved scope through the project's behavior/test workflow. New substantial visual, interaction or state changes return the affected proposal to review. Routine faithful implementation choices do not require another approval.

Prototype coverage is design evidence, not proof that the real application handles those states. Implementation still needs scoped behavior checks and rendered verification against the approved proposal.
