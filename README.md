<p align="center">
  <img src="./assets/icon.png" alt="Multicolored chameleon with design construction guides" width="180">
</p>

# Plugin `design`

Design systems and complete interfaces, powered by a pinned Impeccable distribution. Install this plugin once; a separate Impeccable plugin is not required. No marketplace registration or publication is included in this draft.

For local review, start Claude Code with `claude --plugin-dir ./design` from this workspace. The plugin follows the same `skills/<name>/SKILL.md` layout as craft and docker.

CLAUDE.md at the plugin root is for maintaining this repository; Claude Code does not inject it as runtime plugin context. Runtime rules are carried by the skills and their shared workflow.

## Commands

| Command | Purpose |
|---|---|
| `/design:setup [scope]` | Inspect the project and create or update DESIGN.md from evidence |
| `/design:design [request]` | Build/refine UI, or pass an Impeccable action such as `typeset`, `animate`, `shape`, `harden` or `polish` |
| `/design:style <change>` | Iterate on visual-only changes; migrated from craft:style |
| `/design:mockup [idea]` | Produce a state-complete responsive proposal and iterate before implementation approval |
| `/design:states [screen]` | Define applicable screen/control states and their verification |
| `/design:system [scope]` | Consolidate existing tokens and reusable component patterns |
| `/design:connect [tool]` | Inspect or set up an optional Figma/FigCraft MCP integration |
| `/design:review [scope]` | Report visual, accessibility and state coverage findings; fix only when requested |

The entry points load the shared workflow and relevant domain skills: colors, contrast, typography, patterns, motion, responsiveness, Figma and FigCraft. Those domain skills stay out of the command menu. Every UI workflow assesses states and responsive behavior using the project's shared breakpoints, including intermediate widths; an isolated typography edit does not authorize building unrelated error screens.

## Proposal gate

UI creation and changes start with an isolated reviewable artifact or a Figma/FigCraft draft, containing every applicable screen/control state and relevant responsive composition. The user iterates on that proposal and explicitly approves its current version before product implementation begins. Approval and scope are recorded in the project. Substantial proposal changes return to review; documentation and review-only tasks can proceed without this gate.

## Testing boundary

Functional automated tests (unit, component, integration and E2E) verify behavior, meaningful visibility and accessibility semantics. They never lock decorative UI to a particular color, exact size, CSS class, spacing or animation time. Appearance is reviewed in the rendered result. A dedicated visual-regression suite requires an explicit request and stays separate from behavioral assertions.

## Color contract

Nested neutral containers alternate two background roles: `bg-1 → bg-2 → bg-1 → bg-2`. A third nesting level reuses the first background instead of introducing a third shade. Each background has its foreground partner (`fg-1` or `fg-2`). Action, status, field and overlay colors retain their own semantic roles. Names do not guarantee contrast: measure the actual text/background pair in each supported theme and interaction state.

The framework-neutral starter is `skills/colors/assets/theme.css`. It is an example, not an automatic palette replacement. Existing projects keep their token names through a mapping in DESIGN.md.

## Project artifacts

- `DESIGN.md`: system overview, semantic roles, typography, layout, components and decisions, with relative links to implementation.
- `docs/design/states/<screen>.md`: state matrix and evidence for screens in scope.
- Existing token/theme/component files: authoritative runtime values.
- Optional Impeccable PRODUCT.md and `.impeccable/` artifacts: retain upstream compatibility; do not create competing product briefs.

Templates are bundled with setup and states. They are filled from the target project, not copied as an invented identity. Connector configuration belongs to the target project's existing MCP configuration, not this plugin's global configuration.

## Upstream and runtime

Impeccable 4.8.0 is bundled under `upstream/impeccable/`; the exact commit and Git blob hashes are in `upstream.lock.json`. The files are not registered as a second discoverable skill: our entry points read its SKILL.md and selected playbooks directly, resolving every launcher path to the bundled directory.

The upstream launcher may download a checksum-verified native engine on first use. Engine, interactive login and network-dependent tools were not exercised in this draft. If the engine is unavailable, its documented manual workflow remains usable. There are no automatic hooks in this first version; do not claim the upstream detector hook is installed.

The migrated style flow needs craft 0.16.0 or later when craft's `atdd-first` hook is enabled. Older versions recognize only the retired craft:style name. The mockup approval gate is expressed in the design workflow instructions; the craft hook recognizes the loaded style flow and does not independently validate approval records.

To update, use the procedure in `UPSTREAM.md`. Run `python3 scripts/verify.py` to check packaging, upstream integrity, local Markdown links and the sample palette's contrast. This does not prove live Claude loading, visual correctness or WCAG conformance of a consuming application.

## Sources and licensing

- [Impeccable](https://github.com/pbakaus/impeccable): bundled skill, playbooks and runtime support, Apache-2.0; original license and third-party notices retained in its directory.
- [WCAG text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html): measurement criteria.

Local extensions are MIT licensed. Neither upstream affiliation nor upstream review is implied.
