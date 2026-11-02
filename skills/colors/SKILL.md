---
name: colors
description: Define semantic background, surface, foreground, action and status tokens across supported themes. Use for palettes, nested containers, color roles or theme consistency.
argument-hint: "[scope]"
user-invocable: false
---

# Semantic color pairs

**Rule:** alternate two neutral background roles as containers nest: `bg-1 → bg-2 → bg-1 → bg-2`. Use the foreground paired with the chosen background. A semantic name is a contract, not proof of contrast.

Read [the shared workflow](../design/references/workflow.md). Use bundled Impeccable's colorize/extract playbook as relevant. Read `design:contrast` for measurement.

## Roles

| Background | Content partner | Purpose |
|---|---|---|
| `--bg-1` | `--fg-1` | First neutral background; reused at the third nesting level |
| `--bg-2` | `--fg-2` | Second neutral background; reused at the fourth nesting level |
| `--overlay` | `--overlay-foreground` | Popover or dialog, above a separate backdrop |
| `--field` | `--field-foreground` | Input/select interior |
| `--accent` | `--accent-foreground` | Primary emphasis/action |
| `--success`, `--warning`, `--danger`, `--info` | Corresponding `-foreground` | Status feedback |

Map these conceptual roles to existing tokens rather than renaming the project's system. Choose a visibly distinct pair in each supported theme. The two backgrounds separate adjacent neutral containers; their foregrounds ensure readable content. Do not introduce a third neutral background merely because nesting reaches a third level. Elevation may also use borders or shadows. This alternation does not require adding wrappers or nested cards where no grouping is needed.

1. Identify canvas, containers, controls, overlays, actions and feedback in the target.
2. Keep existing brand primitives; map them to semantic roles in the project's theme source. Components consume roles, not palette hex values. At each nested neutral container boundary, switch to the other background; the third level returns to the first. Count meaningful background-bearing containers, not every DOM wrapper. A reusable component must adapt to its parent background instead of always forcing bg-2.
3. Pair every colored content container with its text/icon color. Set background and foreground together, so nested content does not inherit an incompatible page color. Reset pairs inside inverse/colored containers.
4. Define hover, pressed, selected, focus and disabled treatments only where used. Recheck text on changed backgrounds. Add `-soft` and `-soft-foreground` together when a subtle status variant is needed.
5. Define muted text for each allowed surface context. A global muted token is valid only where measured; do not reduce the whole container's opacity to mute text.
6. Separate decorative `--separator` from `--control-border` when a boundary is required to identify a field. Define links, selection and focus explicitly. Status also needs text, an icon or another non-color cue.
7. Apply the same roles in supported themes, with values selected and verified per theme. Do not add a dark theme to a light-only project without a requirement.

Use [the starter theme](assets/theme.css) only for an explicitly new system or requested seed. It is a neutral example with local values, not a universal identity. Extend semantic action/status roles using current needs, then measure real rendered states.

```css
.page, .panel__group {
  background: var(--bg-1);
  color: var(--fg-1);
}
.panel {
  background: var(--bg-2);
  color: var(--fg-2);
}
.primary-action {
  background: var(--accent);
  color: var(--accent-foreground);
}
.primary-action:hover { background: var(--accent-hover); }
```

## Check

Can each content color be traced to an allowed surface pair, including nested containers, themes and interaction states? Does measured contrast support that pairing?

For the example hierarchy `.page > .panel > .panel__group`, the backgrounds are bg-1, bg-2 and bg-1 respectively. These selectors illustrate the hierarchy; they are not a context-independent component API. Verify visually that adjacent containers are distinguishable, and measure text contrast separately; text contrast does not prove background separation.
