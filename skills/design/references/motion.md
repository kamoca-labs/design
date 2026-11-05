# Purposeful motion

**Rule:** motion explains a change, maintains continuity or gives feedback. Record its purpose and reduced-motion behavior.

With the Read tool, read the shared workflow (`workflow.md` in this folder) and the bundled animate playbook. Inspect existing tokens and component transitions.

1. Identify the trigger, start/end states, animated properties, duration, easing, interruption behavior and semantic/focus outcome. Cover entry, exit, expansion, progress and validation where applicable.
2. Reuse shared motion tokens. Choose timing by distance, complexity and task; do not impose one duration or curve on every interaction.
3. Prefer transform/opacity when they express the change. For intrinsic size, use a technique supported by the project's browser targets and verify layout behavior. Reserve space for loading content when needed.
4. Handle repeated input, cancellation and rapid open/close without stale visibility, trapped focus or invisible interactive elements. Animation completion must not be the only path to saving data or restoring controls.
5. Respect `prefers-reduced-motion` with an immediate state change or restrained alternative. Loading and feedback remain understandable. Avoid flashing and unnecessary perpetual motion; provide controls for nonessential moving content when applicable.
6. Test actual states with keyboard, reduced motion, slow responses and representative devices. Record the conventions in DESIGN.md and relevant state matrices.

If craft:style imposes a conflicting motion rule, follow the active project's instructions and report the conflict. Do not bypass hooks or silently claim both policies were satisfied.

## Check

Does the interface remain understandable and usable when motion is reduced, interrupted or skipped?
