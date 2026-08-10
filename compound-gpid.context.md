# Project Context

Additional context for Copilot and the Compound GPID plugin. Edit freely --
this file is committed to git and shared with the team.

## Data Sources
<!-- Where does data come from? File paths, databases, APIs, vintage conventions -->

## Domain Rules
<!-- Project-specific rules that Copilot should always follow -->

### Extraction pipeline conventions

- **Welfare boundary is content-based, not ID-based**: Welfare leakage is
  detected by inspecting candidate citations' `source_path` for
  `chapter8-CONS.qmd`, not by substring-matching inventory IDs. Never use
  ID-substring heuristics for content classification.
- **Every new public function needs at least one integration test**: "Thin
  sequencer" modules that wire together tested modules still need end-to-end
  tests. Zero-tested public functions are a P0 gap.
- **Verify attribute names across model boundaries**: When code in module A
  accesses attributes on a model defined in module B, verify the field name
  against the model definition — don't infer from related models with similar
  fields.
- **Run `/cg-review mode:verify` after fix-triage**: The verify pass catches
  cross-file breakage introduced by fixes, which the original review cannot
  see because the code didn't exist yet.
- **Cross-platform test conventions**: When writing Python tests that depend
  on exact byte content (excerpt matching, hash verification), use
  `write_bytes` instead of `write_text` to avoid Windows line ending
  translation (`\n` → `\r\n`). Skip symlink tests on Windows with
  `@pytest.mark.skipif(sys.platform == "win32")`. Compare path components
  (`path.parts[-N:]`) instead of full paths to handle Windows drive letters.

## Work in Progress
<!-- Modules, features, or migrations currently underway -->

## Workspace Notes
<!-- Related folders, dependencies on other projects in the VS Code workspace -->

- `review-app/` is a `{golem}` Shiny R package. Golem module tests must capture
  `moduleServer()` return lists and drive namespaced inputs; unexported helpers
  break under R CMD check. See
  `.cg-docs/solutions/testing-patterns/2026-08-10-golem-module-testserver-capture.md`.
- Deployed bundle IDs: the Posit Publisher record
  `review-app/.posit/publish/deployments/deployment-U42S.toml` is the
  authoritative source; hand-maintained audit refs (defect-log, active-state,
  work-report) must be re-reconciled after each deploy (latest: bundle 88147 @
  2026-08-10T22:52:40Z; DEF-001 fixed, boot smoke pending).
## Wiki Configuration
<!-- folder: wiki -->
<!-- audience: developers | researchers | end-users -->
<!-- tone: technical | conversational | formal -->