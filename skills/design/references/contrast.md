# Contrast on the rendered surface

**Rule:** measure the actual foreground against the background it is displayed on. A pair of variables does not ensure a passing ratio.

Read the shared workflow (`workflow.md` in this folder) with the Read tool. When tokens change, also read `colors.md` in this folder. Apply bundled Impeccable's audit playbook to the affected scope.

1. Identify text, placeholder, link, icon, control boundary, selected-state indicator and focus indicator pairs. Resolve computed colors after inheritance, alpha compositing, overlays and theme changes.
2. Use WCAG 2.2 AA as the baseline unless the project requires more: normal text at least 4.5:1; large text at least 3:1 (24 CSS px regular, or approximately 18.67 CSS px bold). Do not round a failing ratio up. Thin fonts can need additional margin for readability.
3. Required control/state cues and meaningful graphical elements need 3:1 against adjacent colors. Decorative separators and inactive controls have different requirements; do not incorrectly label every low-contrast divider a violation. An error message remains ordinary readable text.
4. Measure every supported theme and changed hover/pressed/selected state. A hover color need not differ from the default by 3:1; its required content and cues must remain distinguishable from their actual adjacent colors.
5. Check focus visibility, clipping and obscuration separately. Contrast alone does not prove keyboard accessibility. Do not encode success, errors or selection with color alone.
6. For text over an image/gradient/video, measure the relevant worst-case region and states. Add a suitable surface/scrim or reposition content when contrast is unstable; a single sampled pixel is not sufficient.
7. Report route/component, theme/state, foreground, background, measured ratio, target, evidence and proposed correction. Mark unmeasured pairs as pending. Prefer fixing the semantic pair rather than one-off component overrides.

Sources: [WCAG text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [WCAG non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
