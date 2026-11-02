---
name: review
description: Review rendered UI for system consistency, contrast, typography, responsiveness, motion and complete states. Reports findings without changing implementation unless fixes are requested.
argument-hint: "[scope]"
---

# Review the interface

Read [the shared workflow](../design/references/workflow.md). Load bundled critique for UX/hierarchy and audit for technical checks as needed; do not run every upstream action automatically.

1. Resolve the target and read its system and state contract. Establish the routes, supported themes, viewport ranges and available evidence.
2. Assess each domain below. Read only the skills with a relevant signal; state and responsiveness assessment always applies to UI.

| Domain | Skill | Signal |
|---|---|---|
| Color roles | `design:colors` | Ad hoc shades, mismatched surface/text, inconsistent themes |
| Contrast | `design:contrast` | Faint text, ambiguous controls, unknown contrast evidence |
| Typography | `design:typography` | Unclear hierarchy, clipping, inconsistent roles or fallback |
| Patterns | `design:patterns` | Equivalent tasks use inconsistent components or interactions |
| Responsive | `design:responsive` | Broken layouts, unsupported width ranges or missing breakpoint checks |
| Motion | `design:motion` | Abrupt/confusing transitions, interrupted state bugs or missing reduced motion |
| States | `design:states` | Main screen is the only demonstrated variant |

3. Inspect the rendered result and keyboard path; check labels, semantic structure, focus, content alternatives and announcements. Use available tooling for computed contrast and accessibility checks. A screenshot cannot prove interaction semantics.
4. Report findings by priority with route/component, theme/viewport/state, evidence, user impact and a concrete correction. Distinguish verified defects, suspected issues and checks that could not run. Do not produce a numeric quality score without a defined rubric and supporting evidence.
5. For review-only requests, stop with the report. When fixes were requested, apply the scoped batch and perform one confirmation pass. Do not expand into an unrequested redesign.
