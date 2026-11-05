---
name: system
description: Consolidates design tokens, semantic surface pairs, typography and reusable UI patterns in an existing project and keeps DESIGN.md in sync. Use when tokens or components drift, repeat or need one source of truth.
argument-hint: "[scope]"
---

# Consolidate the system

Read [the shared workflow](../design/references/workflow.md) and bundled extract playbook. Use setup for a project that has not been inspected.

Before implementing a visual change, follow `design:mockup` and obtain approval for the current proposal. Documentation-only inventory can proceed; existing approval covers faithful consolidation without a new proposal.

1. Inventory repeated visual decisions in the requested scope and identify the existing sources of truth. Read [patterns.md](../design/references/patterns.md), [colors.md](../design/references/colors.md), [typography.md](../design/references/typography.md), [responsive.md](../design/references/responsive.md) and [motion.md](../design/references/motion.md) with the Read tool. Read only the references of the affected domains.
2. Distinguish intentional variants from drift. Consolidate shared knowledge into the existing token/theme/component system. Do not replace the styling stack or create a parallel token package by default.
3. Map background/foreground roles and verify their contrast with [contrast.md](../design/references/contrast.md). Preserve theme selectors and component APIs unless the requested change requires a migration.
4. Define reusable component anatomy and actual variants, including responsive adaptations and applicable control/screen states. Avoid speculative components or tokens without a current use.
5. Update relevant DESIGN.md sections and state matrices to match implemented decisions. Keep links relative and preserve unrelated content.
6. Inspect representative consumers after consolidation; run scoped existing checks and render affected themes, widths and states. Report migrations, retained exceptions and unresolved drift.
