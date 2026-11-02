Skill names, arguments, documentation, scripts and code are in English. Replies follow the user's language.

Keep project decisions in the target repository with relative paths. DESIGN.md describes the system; token files and components define its implementation. Do not put project facts in user-local memory.

The user requests the work; the agent performs implementation, setup and verification. Hand off only actions the agent cannot perform, such as an interactive login. Existing authorization applies to routine configuration within scope.

Files under upstream/impeccable are an unmodified, pinned third-party distribution. Put extensions in skills/. Preserve LICENSE and NOTICE.md. Update upstream.lock.json only with a verified upstream snapshot. Never run an upstream self-update against the bundled copy.

Always assess the applicable screen and control states for UI work. Cover only the requested scope; an unrelated defect is a finding, not permission to redesign the product.
