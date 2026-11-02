# Project design system

## Overview

Describe the audience, primary tasks, identity, supported platforms and evidence used. Separate confirmed decisions, observed implementation and proposals. Link PRODUCT.md if present. Record optional design-tool files and which source wins when design and code disagree.

## Colors

Link the authoritative token/theme files. Fill this role map using existing names; add roles only for current needs.

| Role | Background token | Foreground token | Intended use | Themes | Evidence |
|---|---|---|---|---|---|
| bg-1 | To inspect | To inspect | First and third neutral nesting levels | To inspect | Pending |
| bg-2 | To inspect | To inspect | Second and fourth neutral nesting levels | To inspect | Pending |
| Overlay | To inspect | To inspect | Dialog or popover | To inspect | Pending |
| Field | To inspect | To inspect | Input and select | To inspect | Pending |
| Accent | To inspect | To inspect | Primary action | To inspect | Pending |
| Status | To inspect | To inspect | Success, warning, danger and info as needed | To inspect | Pending |

Document muted text, links, separators, control boundaries and focus rings. Record allowable background/foreground pairings, interaction states and measurement evidence. Do not infer passing contrast from token names. Keep decorative separator requirements separate from control boundaries.

Neutral containers alternate bg-1 -> bg-2 -> bg-1 as they nest. Map the roles to existing tokens and pair each with its foreground. Do not introduce a third shade just for the third level. Apply the alternation at meaningful background-bearing groups, not every DOM wrapper.

## Typography

Link font sources and text styles. Record family/fallback, role, size, weight, line height, tracking and readable line lengths. Include numeric content, localization, text expansion, zoom and font-loading behavior. Mark unresolved font availability explicitly.

## Layout

Link spacing and layout definitions. Describe grid, alignment, density, content widths and content-driven breakpoints. Map the project's breakpoint names to actual thresholds and document what changes at each one. Include intermediate widths, small screens, large text, long content, orientation and bidirectional layout when supported. Record viewport sizes verified in representative states.

## Elevation & Depth

Describe the alternating neutral backgrounds, overlay/backdrop relationships, shadows, stacking and focus visibility. Link the corresponding tokens. Nesting reuses bg-1 and bg-2; overlays and semantic status containers keep their distinct purpose.

## Shapes

Record radii, borders, icon/illustration language and image treatment, with implementation links.

## Components

Link reusable components and their variants. Define composition, intended usage and visible control states. Link screen matrices under docs/design/states/. Record motion tokens, interruption behavior, reduced-motion alternatives, focus movement and recovery rules here. Name the actual connector and component mapping if one is in use.

## Do's and Don'ts

Record the project's specific approved constraints, exceptions and open decisions. Include scoped verification commands and remaining gaps. Avoid generic style bans or claiming validation that has not run.
