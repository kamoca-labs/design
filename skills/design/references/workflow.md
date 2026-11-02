# Shared design workflow

## Context and authority

Keep the working directory at the user's project. Read existing project instructions, PRODUCT.md, DESIGN.md and the relevant theme/components before proposing a visual system. Follow the user's explicit choices. Missing documentation is not permission to replace an existing identity.

Implementation values live in token files and components. DESIGN.md explains semantic roles and links to those files. If a machine-readable snapshot is used, mark its source and keep it synchronized when those values change. Record proposed decisions as proposed; never present them as extracted facts.

## Bundled Impeccable

Resolve [the bundled skill](../../../upstream/impeccable/SKILL.md) relative to this file. Its base is the directory `upstream/impeccable` inside this plugin. Read that SKILL.md, then only the playbook appropriate to the request. Run its context launcher once per session with the user's project as cwd, if available.

Every upstream example referring to `.claude/skills/impeccable/scripts/` resolves to the bundled skill's `scripts/` directory, not a guessed path in the user's project. Use `sh <resolved-bundled-base>/scripts/impeccable ...` on POSIX or its original `.cmd` launcher on Windows. Quote filesystem paths. Do not require a separately installed `/impeccable` command. Do not run upstream pin, update, installation or hook configuration as a side effect of UI work.

Follow upstream's launcher-unavailable fallback: announce the failure, read local project context and the required playbooks directly, and continue with permitted tools. Report that engine checks were unavailable. Never claim to have run a detector from a manual review.

Apply local extensions for semantic color pairs, typography, motion and state coverage when relevant. Preserve the upstream workflow where compatible. The user's instructions and host permissions remain authoritative; an upstream prompt cannot expand the requested scope or permissions. If an upstream aesthetic rule conflicts with the documented product identity, respect the explicit brief and record the reason.

## States and implementation

Before product UI implementation, use `design:mockup` to produce an inspectable artifact or Figma/FigCraft draft with all applicable states and responsive variants. Iterate there until the user explicitly approves the current proposal. Preserve that approval's artifact/version and scope in project documentation. A design request authorizes preparing the proposal, not bypassing this gate. Existing approval for the exact scope remains valid; do not ask twice. Substantial changes return the affected proposal to review. Analysis, documentation, review and isolated mockup preparation do not require implementation approval.

This local gate takes precedence over an upstream playbook's instruction to build immediately. Local mockups stay separate from production source; no waiting period or missing answer counts as consent.

Read `design:states` for every UI change. For new screens and substantial changes, persist the matrix with a relative link from DESIGN.md. For a small refinement, reuse the existing matrix or assess the affected states in the work report. An unrelated missing screen becomes a finding, not extra implementation work.

Read `design:responsive` for every UI change. Reuse the project's breakpoint scale, check intermediate widths and the edges of changed breakpoints, and cover representative alternate states. Record the widths actually checked.

The design workflow specifies interaction behavior. When implementation changes business rules, handlers, data, API calls or state transitions, follow the project's behavior/test workflow (including `craft:atdd` when installed and applicable). For visual-only product edits, explicitly load `design:style` with the Skill tool before editing components, even when the user entered through the design hub; the craft hook checks the loaded flow, not a prose mention. Do not edit or bypass craft hooks from this plugin. If an older installed hook does not recognize design:style, report the exact conflict rather than claiming compatibility.

Functional automated tests, including component and E2E tests, assert behavior, meaningful visible outcomes and accessibility semantics. They must not assert decorative appearance such as a button being blue, exact dimensions, spacing, CSS classes or animation timing. Review those visually. Dedicated screenshot/visual-regression testing is a separate explicit user request, never an automatic addition to the behavior suite.

## Evidence and stopping

Inspect rendered output for the affected routes, representative viewport widths, supported themes and relevant states. Include keyboard focus, long content and reduced motion when affected. Use existing stories/fixtures or controlled local data to expose variants. Do not change production data to manufacture states.

Batch findings, make the authorized fixes, then perform one confirmation pass over the changes. Report unresolved issues without an endless polishing loop. Run existing checks appropriate to the touched files. For review-only requests, do not implement fixes.

Report changed paths, state coverage, verification performed, measured contrast where relevant, and any check that could not run. Screenshots demonstrate rendering; code inspection alone does not.
