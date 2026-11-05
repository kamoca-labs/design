# Interface patterns

**Rule:** equivalent user tasks have equivalent interaction and visual patterns across the product.

Read the shared workflow (`workflow.md` in this folder) with the Read tool. Inspect existing components and real usage before inventing a new pattern. For the affected screen, load `design:states` with the Skill tool and read `responsive.md` in this folder with the Read tool.

| Pattern | Define |
|---|---|
| Navigation | Location, current item, hierarchy, narrow-width behavior and keyboard path |
| Forms | Labels/help, grouping, required/read-only/disabled meanings, validation timing, preserved input and submit feedback |
| Tables/lists | Column priority, scanning, numeric alignment, sort/filter/selection, pagination and narrow-width behavior |
| Search/filters | Applied state, clearing, no results, request timing and retained context |
| Dialogs/drawers | Entry/exit, focus, dismissal, unsaved work, overflow and return destination |
| Notifications | Severity, placement, lifetime, announcement and recovery action |
| Empty/error/loading | Cause, useful next action, retained context and layout continuity |
| Icons/images | Approved library/style, meaning, text alternatives, aspect ratios and failure treatment |

Record anatomy, variants, usage conditions, tokens, accessibility behavior, responsive adaptations and state coverage for the patterns actually used. Prefer an existing component/variant over a new wrapper. Extract when the same reusable knowledge is present, not because two screens happen to share a shape.

Keep error, success and destructive action meanings consistent. Preserve semantic HTML and the component library's keyboard behavior. Behavioral changes follow the project's implementation/test process.

## Check

Would a user who learned this pattern on one screen recognize and operate it on another?
