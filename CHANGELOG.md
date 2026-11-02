# Changelog

## 0.1.0 — 2026-11-02

Initial version. Repository history begins with this system; no earlier bug-fix release is recorded.

### New features

- Eight public workflows: design, setup, style, mockup, states, system, connect and review.
- Project setup with an evidence-based DESIGN.md template and links to existing tokens and components.
- Reviewable local artifacts or Figma/FigCraft drafts before product implementation, with explicit approval of the current proposal and scope.
- State contracts for main, empty, loading, success, error, offline, access and other applicable variants, including recovery and preserved input.
- Responsive guidance using shared project breakpoints, intermediate widths, content extremes, zoom and relevant alternate states.
- Two alternating neutral backgrounds (`bg-1 → bg-2 → bg-1`) with paired foregrounds and separate semantic action/status/control colors.
- Focused guidance for contrast, typography, interface patterns and purposeful reduced-motion-aware animation.
- Optional Figma and standalone FigCraft MCP guidance and configuration examples.
- Bundled Impeccable 4.8.0 pinned to an exact commit, with intact licenses/notices and an update procedure.
- Static verification for packaging, links, 60 upstream Git blobs and 56 opaque sample contrast pairs.

### Compatibility and limits

- Use craft 0.16.0 or later when its component edit gate is enabled. Visual-only work now uses `/design:style`.
- Functional tests verify behavior and semantics rather than decorative appearance. Dedicated visual-regression testing requires an explicit request.
- Mockup approval is enforced by workflow instructions, not a new mechanical hook. Optional connectors and the native engine require separate runtime access; static verification does not establish their end-to-end behavior.
- Existing tokens, libraries and identities are preserved by default. The palette is an example, not an automatic theme replacement.

### Documentation

- Match the sibling plugins' README structure: contents, installation, overview, command arguments, sub-skills, rules, artifacts and files.
- Add a usage guide for setup, mockup iteration, states, background alternation, review and connections before creating the version tag.

Evidence: [initial implementation](https://github.com/kamoca-labs/design/commit/48ec336), [installation documentation](https://github.com/kamoca-labs/design/commit/6663eaf). The README alignment and these release notes are added before the first tag.
