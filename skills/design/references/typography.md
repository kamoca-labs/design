# Typography as a system

**Rule:** the same content role uses the same treatment across the product; hierarchy and readability follow the actual content and task.

With the Read tool, read the shared workflow (`workflow.md` in this folder) and the bundled typeset playbook. Inspect fonts, text styles and rendered content before selecting replacements.

1. Inventory the current family, available weights, licenses/source, fallback stack and loading behavior. Reuse the brand's choices. Do not assume a font is installed or add a remote font service without considering existing project constraints.
2. Map roles: display where needed, headings, body, labels, help text, captions, controls, code and numeric/tabular data. Record size, weight, line height and tracking in existing tokens.
3. Tune hierarchy and line lengths using representative content. Use responsive sizing only where it helps; a fixed universal scale is not required. Preserve semantic heading order rather than selecting a heading tag for its font size.
4. Check Portuguese accents and all supported scripts, punctuation, emoji and fallback. Check long translated labels, pluralization, dates and numbers. Use the project's localization system rather than embedding translated values in styles.
5. Let controls wrap or grow where the task allows. Check zoom, text enlargement, narrow viewports and late font loading. Truncation needs a reason and a way to access essential full content.
6. Use tabular numbers when comparison/alignment benefits from them. Do not impose the same expressive typography on a dashboard and a campaign page merely because they share a brand.
7. Check text/surface contrast with `contrast.md` in this folder. Read it with the Read tool. Verify primary, helper, placeholder, error and disabled treatments in applicable states. Record the roles and implementation links in DESIGN.md.

## Check

Can the user recognize hierarchy and read real content before and after fonts load, across supported languages and viewport sizes?
