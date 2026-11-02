---
name: style
description: Iterate on visual-only UI changes using bundled Impeccable and the project design system, without a behavior specification or prior red test. Behavior changes follow craft:atdd when available.
argument-hint: "<what must change on the screen>"
---

# Style mode

A visual-only change is reviewed on the rendered screen. Use the project system, iterate with the user and check for behavioral regressions at the end.

Read [the shared workflow](../design/references/workflow.md), including bundled Impeccable loading. A separately installed Impeccable plugin is not required.

1. Resolve the visual scope and read DESIGN.md plus affected components/tokens. Load the appropriate bundled playbook and the relevant color, contrast, typography, pattern or motion skills.
2. Read `design:states`, `design:responsive` and `design:mockup`. Prepare the proposed change in an isolated artifact or Figma/FigCraft draft, including affected states and breakpoint ranges. Iterate there until the user explicitly approves the current proposal; then apply the approved change to the product and inspect the rendered result. Reuse valid approval already supplied for the same proposal/scope.
3. Iterate on feedback within the approved scope; substantial proposal changes return to mockup review. Do not write Given/When/Then or a red test for a purely visual preference. Do not use automated assertions to lock in a font, color, exact size, spacing, radius, shadow, animation duration or CSS class.
4. When the user accepts the screen, run the existing filtered behavior/component/E2E checks relevant to the touched files, following project execution rules. Fix confirmed behavioral regressions within scope and perform at most one confirmation pass. Report visual evidence and any remaining gaps.

## Boundary with behavior

Changing a handler, state/data flow, API call, business rule or rule-driven visibility is behavior. It follows the existing test-first process (`craft:atdd` when installed), even when the visible result is part of the same screen. The design specification can describe those interactions; style mode does not exempt their implementation from tests.

For mixed features, use the order the user requested. If the choice materially changes the work and no preference exists, clarify backend-first, screen-first with explicit mock data, or vertical slices. Keep mock behavior visible as such and replace it through the behavior workflow.

## Motion and loading

Read `design:motion` for transitions. Entry/exit, expansion, modal opacity/transform and loading feedback use the shared tokens and the project's supported techniques. Preserve useful content and reserve space to avoid load shifts. A skeleton is an option, not the default. Respect reduced motion and keep focus and actions usable when animation is skipped or interrupted.

## Verification boundary

Automated tests prove behavior, meaningful visibility, accessible state and user outcomes. Visual review proves the approved appearance at the relevant sizes/states. Do not turn a visual preference into a brittle functional test. A dedicated visual-regression suite is created or changed only when the user explicitly requests that kind of testing; it does not belong in normal component/E2E assertions.
