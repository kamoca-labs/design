---
name: connect
description: Inspect and configure optional design-tool MCP integrations for a project, routing to Figma, FigCraft or another available provider.
argument-hint: "[figma | figcraft | tool]"
---

# Connect a design tool

Read [the shared workflow](../design/references/workflow.md).

1. Discover the current session's design tools and inspect the project's existing MCP configuration and documented design links. Do not assume a connector exists because a tool name was mentioned.
2. Load `design:figma` or `design:figcraft` for the selected provider. For another tool, check its official integration documentation and use the same capability contract below. Clarify the provider only when it cannot be inferred.
3. Record supported operations: read structure, read/export tokens and assets, inspect rendered output, create/update components/variants and prototype transitions. State capability gaps; providers are not interchangeable.
4. For a requested setup, merge only the chosen server into the existing project configuration using verified current official settings. Check local binaries and account requirements first. Preserve other servers; keep credentials out of tracked files. Hand off interactive authentication only when it cannot be performed by the agent.
5. Verify discovery and a relevant read operation. A requested create/edit workflow can verify with a clearly scoped draft; configuring a connection alone does not authorize changing arbitrary design files.
6. Record provider, project/file links, component/token mappings and design-vs-code authority in DESIGN.md. Use portable commands/paths where possible and keep machine-local paths in local configuration.

If no provider is available, continue with local components, browser evidence and supplied references. Report the missing integration rather than pretending a screenshot contains editable component/token data.
