# FigCraft integration

## Contents

- [Setup](#setup)
- [State board](#state-board)
- [Editing mechanics](#editing-mechanics)
- [Offline coverage audit](#offline-coverage-audit)

## Setup

Follow `design:connect`. This reference targets the standalone FigCraft editor documented at [FigCraft MCP](https://figcraft.run/mcp). There are other projects with the same name. Inspect the supplied URL or installation and clarify only if the intended product is ambiguous.

Verify the installed app/CLI and current official commands before configuring. The documented modes are `figcraft-cli mcp` (headless) and `figcraft-cli mcp --attach 7979` for an app started with `figcraft --control 7979`. The browser editor is not the local MCP server. Use the actual executable path; do not invent a cross-machine absolute path in tracked configuration. A `figcraft://join` link carries a session token: never write it to a file.

[The MCP example](../assets/figcraft.mcp.example.json) assumes the verified CLI is available on PATH. Merge the chosen server only. Use a local override when an absolute executable path is required. Use attached mode only when the user wants the running editor controlled.

Inspect the document structure and available commands. Reuse variables, text styles and components. Every color, radius and spacing comes from a variable; no raw values. Use auto layout and component variants for responsive and state differences when supported.

Map the tool's properties to DESIGN.md and runtime tokens. Inspect JSON and a rendered PNG after changes; confirm constraints and actual text layout. A fixed-size frame does not prove responsive behavior in the application. Verify implementation separately in the browser.

Keep edits inside the requested document. Preserve existing user work, record artifact paths and disclose unsupported imports/exports, font differences or missing prototype capabilities.

## State board

A screen proposal is a full grid: **every applicable state, at every width of the project's breakpoint scale, in every supported theme**. This is the review artifact; representative sampling belongs to implementation verification, not to the board.

- **One page per screen.** Proposals that lost the vote may stay on a separate page as history; the final screen page holds only the chosen direction.
- **Theme blocks.** The light block comes first, with a heading such as "Light mode"; the dark block repeats it below in the same order. Themes switch through the variable collection mode (for example `Colors` in `dark`), never through copied colors.
- **One row per width, ascending.** Include a base width below the first breakpoint (for example 390, then 640, 768, 1024, 1280 and 1536 for the Tailwind scale). The row label is only the width and its token (`768 px · md`), plus at most a short layout hint.
- **Every state in every row, in the same order.** Number the states and keep the numbering across rows and themes, so a column means the same state everywhere. Extra states go to the right of the main ones.
- **Frame name** `<width> / <theme> / <n> <state>`, for example `1024 / dark / 7 Offline`. Width-only states (such as wizard steps that replace an overview on narrow widths) appear only in the rows that have them and are recorded as such in the state matrix.
- **Fixed frame height per width** within a page, so rows line up. Keep heights consistent across pages unless the content needs more, and record them in DESIGN.md.
- **Shell pages** (navigation, account menu) use the same grid. Below the navigation switch: bottom bar, navigation menu open, account menu open. From the switch up: sidebar open, open with the account menu, collapsed rail, rail with the account menu. The rail shows a tooltip on hover and focus in both themes.
- **Overlays per width.** Overlay states appear at every width and in every theme, in the form the project uses at that width (for example a bottom drawer on narrow widths and a modal above). The switch width is one project rule, applied the same on every page.
- **Loose parts** (repeated cards and blocks not yet componentized) sit outside the grid, named `Part / <name>`, and never count as states.
- **Prototype flows** (`afterDelay`, smart animate) only on representative rows, for example the primary desktop and mobile widths in each theme. Write the remaining motion as a spec table in DESIGN.md.
- **Stress test** with content extremes at every width (long names, large counts, high prices). Fix what breaks; record accepted truncations as open decisions. A width that cannot fit its layout gets a different composition (for example the sidebar becomes a rail at the narrowest desktop width), recorded in DESIGN.md.
- **Coverage note in DESIGN.md**: states, widths, themes and frame count per page. Update it whenever the grid changes.

## Editing mechanics

- Save with `file.save` after each adjustment and check a screenshot. The app keeps changes in memory until saved.
- Generate a repeated set (a row of states, a theme block) in one `batch`, naming created nodes with `as` and referencing them with `$ref`.
- Find node ids with `edit.findReplace` using `layerNames` and `select: false`.
- Text clipped inside auto layout: set the text to `textAutoResize: widthAndHeight` and the parent frame to `sizingH: hug`. Text that must wrap uses `fill` width with `textAutoResize: height`; single-line labels that must truncate use an ellipsis.
- Parents of an element with a focus ring do not clip (`clip` off), or the ring is cut.
- Derive every new modal or sheet by duplicating the project's standard one and changing only icon, text and action color. Building one from scratch drifts in header size, close button and action layout. Compare a screenshot against the standard before calling it done.

## Offline coverage audit

When the MCP is not connected, audit the saved file. A `.figcraft` file is a zip with `document.json` (`pages`, `nodes` by id, each with `name`, `type`, `width`, `height`, `children`). Unzip it into a scratch directory, list each page's top-level frames, split the names on ` / ` and count states per width and theme. Report missing cells, height mismatches between pages and elements present in one theme but not the other. This reads the last save only; say so, and that unsaved in-app changes are not covered.
