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

## Work in Progress
<!-- Modules, features, or migrations currently underway -->

## Workspace Notes
<!-- Related folders, dependencies on other projects in the VS Code workspace -->

## Wiki Configuration
<!-- folder: wiki -->
<!-- audience: developers | researchers | end-users -->
<!-- tone: technical | conversational | formal -->