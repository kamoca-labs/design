---
name: review
description: Reviews rendered UI for system consistency, contrast, typography, responsive layout, motion and complete states. Reports findings and changes code only when the user asks for fixes. Use when asked to review, audit or check an interface.
argument-hint: "[scope]"
---

# Review the interface

Read [the shared workflow](../design/references/workflow.md). Load bundled critique for UX/hierarchy and audit for technical checks as needed; do not run every upstream action automatically.

1. Resolve the target and read its system and state contract. Establish the routes, supported themes, viewport ranges and available evidence.
2. Assess each domain below. Read only the references with a relevant signal. Read a reference with the Read tool. Load `design:states` with the Skill tool. The state and responsive assessment always applies to UI.

| Domain | Reference or skill | Signal |
|---|---|---|
| Color roles | [colors.md](../design/references/colors.md) | Ad hoc shades, mismatched surface/text, inconsistent themes |
| Contrast | [contrast.md](../design/references/contrast.md) | Faint text, ambiguous controls, unknown contrast evidence |
| Typography | [typography.md](../design/references/typography.md) | Unclear hierarchy, clipping, inconsistent roles or fallback |
| Patterns | [patterns.md](../design/references/patterns.md) | Equivalent tasks use inconsistent components or interactions |
| Responsive | [responsive.md](../design/references/responsive.md) | Broken layouts, unsupported width ranges or missing breakpoint checks |
| Motion | [motion.md](../design/references/motion.md) | Abrupt/confusing transitions, interrupted state bugs or missing reduced motion |
| States | `design:states` | Main screen is the only demonstrated variant |

3. Inspect the rendered result and keyboard path; check labels, semantic structure, focus, content alternatives and announcements. Use available tooling for computed contrast and accessibility checks. A screenshot cannot prove interaction semantics.
4. Report findings by priority with route/component, theme/viewport/state, evidence, user impact and a concrete correction. Distinguish verified defects, suspected issues and checks that could not run. Do not produce a numeric quality score without a defined rubric and supporting evidence.
5. For review-only requests, stop with the report. When fixes were requested, apply the scoped batch and perform one confirmation pass. Do not expand into an unrequested redesign.
