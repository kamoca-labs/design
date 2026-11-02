# Updating the bundled Impeccable

The local extension files do not modify upstream. `upstream.lock.json` records the repository, exact commit and Git blob identity of every imported file.

1. Resolve a candidate release to a full commit SHA. Inspect its changelog, Claude distribution, runtime launcher, license and notices.
2. Fetch `.claude/skills/impeccable/`, the root LICENSE and NOTICE.md from that commit into a separate staging directory. Check that large files are complete; an empty content response is not a valid file download.
3. Compare the candidate with the pinned files. Inspect command names, paths, engine checksums, documentation schema, connector behavior and extension conflicts. Preserve the upstream directory structure and executable modes. Do not rewrite upstream prompts to fit our conventions.
4. Replace only the tracked bundled snapshot after reviewing the diff. Preserve unrelated user changes. Refresh the lock's commit, version and complete file inventory with the upstream Git blob SHA and mode for each file. Remove retired files only when they were part of the previous inventory.
5. Run `python3 scripts/verify.py`. In a permitted test project, verify context loading, one narrow design operation, DESIGN.md setup/merge and an applicable error/empty state through the plugin. Check that the engine's paths resolve to this bundled distribution.
6. Record results and unresolved compatibility issues before releasing a new plugin version. Do not use `npx impeccable update` or the upstream self-updater on this directory: those tools do not manage this wrapper or its lock.

The engine binary is not vendored. Its version and release hashes are pinned by the original launcher's VERSION and engine-checksums.txt files. Runtime downloads need network and a writable cache. No new engine has been downloaded as part of this draft.
