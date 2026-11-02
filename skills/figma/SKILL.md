---
name: figma
description: Use or configure Figma MCP to inspect design context, variables, assets and component mappings, and perform requested canvas edits.
argument-hint: "[Figma URL or setup request]"
user-invocable: false
---

# Figma integration

Follow `design:connect` and consult the [official MCP documentation](https://developers.figma.com/docs/figma-mcp-server/) and [tool reference](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/) for current configuration, authentication, permissions and tool support.

The documented remote endpoint is `https://mcp.figma.com/mcp`; verify it and the client's configuration schema before editing MCP settings. Use existing session tools when connected instead of adding a duplicate server.

[The MCP example](assets/mcp.example.json) is a merge fragment for Claude Code, not an instruction to replace the existing config. Verify the endpoint/schema and authenticate through the client's supported flow; no credentials are bundled.

For a design URL, resolve the exact file/node. Obtain structured context and a visual reference; inspect variables, layout, component variants and Code Connect mappings when available. Reuse real project components and tokens rather than blindly pasting framework-specific generated output.

Map page backgrounds, surface levels and foreground pairs to project roles. Compare typography, breakpoint adaptations and screen states with DESIGN.md. A single desktop frame does not define mobile, empty, loading or error behavior; record gaps and design the in-scope variants.

For requested canvas work, verify actual write capabilities and target permissions, work in the requested file/draft, and read/render back the result. Do not claim the connector can write merely because it can fetch context. Record node links and unresolved fidelity differences.
