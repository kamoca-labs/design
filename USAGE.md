# Design use cases

Installation and commands are in [README.md](README.md).

## Set up an existing project

```text
/design:setup
```

Inspect existing themes, fonts, components, breakpoints and documentation. Record observed facts, approved decisions and proposals separately in DESIGN.md. Keep runtime values in their implementation files. Preserve the existing identity and libraries.

## Explore a new screen

```text
/design:design an attachments screen with search and upload
```

1. Establish the user goal and data/interaction lifecycle.
2. Assess every state category. Include applicable empty, no-results, loading, uploading, success, error and access variants; explain non-applicable categories.
3. Prepare an inspectable local artifact or a draft in the selected connected tool. Include responsive compositions and a way to inspect alternate states.
4. Iterate on that artifact. Product implementation waits for explicit approval of its current version and scope.
5. Implement the approved proposal through the project's behavior/test process. Verify the actual application against the proposal at relevant states and widths.

## Refine visual appearance

```text
/design:style improve the spacing and hierarchy of the settings panel
```

Prepare the visual proposal using the existing system. Review affected states and breakpoints, obtain approval and implement it. Reuse existing approval for the same proposal/scope. Functional tests verify behavior; rendered review verifies appearance.

## Alternate nested backgrounds

For a page, its panel and a group inside that panel, use bg-1, bg-2 and bg-1. Pair each with its foreground. Count meaningful groups rather than every wrapper. The third level reuses the first shade. Measure content contrast separately from background separation.

## Review without changing code

```text
/design:review the checkout flow
```

Report findings with the route/component, state, viewport/theme, evidence and user impact. Include missing recovery, variants, contrast and responsive problems. Implement fixes only when requested and disclose checks that could not run.

## Connect a design tool

```text
/design:connect figma
/design:connect figcraft
```

Inspect session tools, local binaries and existing project MCP settings. Configure only the selected provider, preserve other servers and verify an actual read. For FigCraft, identify the intended standalone editor. Requested canvas changes stay in the chosen document and are checked structurally and visually.

## Verify the plugin

```bash
python3 scripts/verify.py
claude plugin validate .
```

The checks cover packaging, local links, exact upstream blobs, opaque sample color pairs and the plugin manifest. They do not establish that a consuming application's UI, connectors or native engine work end to end.
