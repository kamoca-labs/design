---
name: states
description: Defines and verifies complete screen and control variants, such as normal, first use, empty, no results, loading, success, error, offline and permission. Use when a screen or flow needs a state contract or a state is missing.
argument-hint: "[screen or flow]"
---

# Complete screen states

**Rule:** every UI task assesses applicable states. New screens need a state contract, not just a screenshot of the successful path.

Read [the shared workflow](../design/references/workflow.md). Use bundled harden/onboard playbooks when implementing recovery or first-use experiences.

## Required assessment

| State | Questions |
|---|---|
| Main/content | What is the user's goal and primary action? |
| First use | What explains the next useful step? |
| Empty | Why is there no data, and can the user create/import it? |
| No results | Which query/filters caused this, and how can they reset them? |
| Initial loading | What is pending and what can still be used? |
| Refresh/background loading | Can existing data, focus and position remain stable? |
| Submitting/pending | How are progress and repeated input handled? |
| Success | What changed and what is the next step? |
| Recoverable error | What failed, what was preserved and how can the user retry? |
| Partial error | Which sections still work? |
| Offline/reconnecting | What is available, pending or unsafe to repeat? |
| Unauthorized/expired session | How can access resume without losing work? |
| Forbidden | What access is required and what valid alternative exists? |
| Not found/unavailable | Where can the user go next? |
| Destructive/unsaved work | What consequence, confirmation or undo is appropriate? |
| Content extremes | What happens with long text, many items, missing values or broken assets? |

For controls, assess default, hover, focus-visible, pressed, selected/checked, disabled, read-only, invalid and processing. Keep read-only, disabled and loading meanings distinct.

1. Identify the screen's actual data and interaction lifecycle. Fill [the matrix template](assets/surface.md) before implementing a new screen. Each category is applicable, not applicable with a reason, or unresolved. Applicable states remain planned until implemented and verified.
2. Specify trigger, visible content, available actions, recovery, preserved user input and focus/announcement behavior. A spinner or generic error message is not a complete specification.
3. Persist new/substantial screen matrices at `docs/design/states/<screen>.md` and link from DESIGN.md. Small scoped changes reuse existing matrices and report only affected coverage.
4. Add a reproducible story, fixture, local mocked response or test path for applicable states. Do not manufacture new product rules or modify real accounts/data just to expose a variant.
5. Verify representative combinations: narrow screen, long/localized text, supported themes, keyboard and reduced motion where relevant. Avoid exhaustive Cartesian products with no distinct risk.
6. Implement in-scope states; report unrelated gaps. Mark evidence precisely as planned, implemented, verified or blocked. Never call a screen complete while an applicable in-scope state is unexplained or unverified without disclosing it.

Loading need not mean a skeleton. Choose progress feedback by context and preserve useful content. Error/empty screens reuse the same system, color pairs and hierarchy as the main screen.
