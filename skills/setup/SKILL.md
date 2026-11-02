---
name: setup
description: Inspect an existing or new UI project and establish DESIGN.md, token mappings, component conventions and state documentation without replacing its identity.
argument-hint: "[project or scope]"
---

# Set up the project design system

Read [the shared workflow](../design/references/workflow.md). Use bundled Impeccable's `init` and `document` playbooks for missing product context and visual documentation. Reuse existing PRODUCT.md rather than asking the same questions again.

1. Inspect manifests, global CSS/theme files, font loading, component libraries, stories, screenshots, routes and current documentation. Identify the actual stack; preserve the existing library by default.
2. Distinguish an existing system, a partial system and a new project. Preserve established choices. Infer facts from code and rendered evidence; ask only for missing decisions that materially affect the result.
3. Read `design:colors` and map the two alternating neutral backgrounds (bg-1 -> bg-2 -> bg-1), their foregrounds, and the control/action/status roles to real project tokens. Include supported themes and contrast evidence. Fill gaps only within the requested setup scope.
4. Read `design:typography`, `design:motion`, `design:patterns` and `design:responsive` to record existing conventions and unresolved gaps. Include spacing, layout, depth, shape, assets, shared breakpoints and content behavior between them.
5. Use [the DESIGN.md template](assets/DESIGN.md) as a section guide. Replace prompts with evidence, proposals or explicit unknowns. For an existing document, merge within the authorized setup request and preserve unrelated decisions; destructive replacement needs an explicit request. Honor upstream's document-update choice when it has not already been supplied.
6. Use `design:states` to document requested screens; link their matrices from Components. Record optional connector choices and the source of truth for design/code conflicts. Do not connect accounts as a side effect of documentation.
7. Verify relative paths, actual token/component names and consistency between documentation and implementation. Report extracted facts separately from proposed changes and pending validation.

Use uppercase `DESIGN.md` for upstream compatibility. In a monorepo, use the established app-level boundary and link shared rules rather than duplicating them.
