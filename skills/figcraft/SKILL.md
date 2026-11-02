---
name: figcraft
description: Use or configure the FigCraft editor's local MCP for frames, auto layout, components, variants, prototypes and rendered verification.
argument-hint: "[document or setup request]"
user-invocable: false
---

# FigCraft integration

Follow `design:connect`. This skill targets the standalone FigCraft editor documented at [FigCraft MCP](https://figcraft.run/mcp). There are other projects with the same name; inspect the supplied URL or installation and clarify only if the intended product is ambiguous.

Verify the installed app/CLI and current official commands before configuring. The documented modes are `figcraft-cli mcp` (headless) and `figcraft-cli mcp --attach 7979` for an app started with `figcraft --control 7979`. The browser editor is not the local MCP server. Use the actual executable path; do not invent a cross-machine absolute path in tracked configuration.

[The MCP example](assets/mcp.example.json) assumes the verified CLI is available on PATH. Merge the chosen server only; use a local override when an absolute executable path is required. Use attached mode only when the user wants the running editor controlled.

Inspect the document structure and available commands. Reuse variables, text styles and components. Use auto layout and component variants for responsive and state differences when supported. Create the applicable main, empty, loading, error and success frames, with the additional states required by the screen contract.

Map the tool's properties to DESIGN.md and runtime tokens. Inspect JSON and a rendered PNG after changes; confirm constraints and actual text layout. A fixed-size frame does not prove responsive behavior in the application. Verify implementation separately in the browser.

Keep edits inside the requested document. Preserve existing user work, record artifact paths and disclose unsupported imports/exports, font differences or missing prototype capabilities.
