# Project Context

Additional context for Copilot and the Compound GPID plugin. Edit freely --
this file is committed to git and shared with the team.

## Data Sources
<!-- Where does data come from? File paths, databases, APIs, vintage conventions -->

## Domain Rules
<!-- Project-specific rules that Copilot should always follow -->

### Extraction pipeline conventions

- **Promotion recomputes rather than trusts candidates**: Resolve evidence from
  pinned Git commits/blobs, verify hashes, deterministically recompile, derive
  aggregates from canonical rows, and require exact candidate-byte equality
  before atomic replacement. Any mismatch must leave the prior artifact intact.
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
- **Variable-name normalization**: GMD snake_case names map to CVS
  `variable_id` by dropping underscores and prefixing `VAR-` (e.g.
  `relationship_to_head`→`VAR-relationshiptohead`), with one grandfathered
  exception (`VAR-marital`, never `VAR-maritalstatus`). Keep the original
  snake_case as `variable_name`.
- **Module ownership**: DEM owns core person demographics (male, age,
  marital, relationshiptohead); IDN owns household identifiers and weights.
  Each `variable_id` belongs to exactly one module (no cross-module dupes).
- **Registered-reference discipline**: reference only registered RULE/PARAM
  ids (RULE-EDU-001/002/003, RULE-SEX-001; PARAM-DEM-MIN-MARRIAGE-AGE,
  PARAM-EDU-YEARS-BY-LEVEL) or leave `rules: []`. Governance concepts (e.g.
  Non-Null Weight Invariant) go in `provenance.notes`, never in `rules:`.
- **Pydantic v2 context validation**: validate drafts with
  `VariableDefinition.model_validate(data, context={...})`, NOT
  `VariableDefinition(**data, context=...)` — under `extra="forbid"` the
  constructor rejects `context` as an extra kwarg.
- **Corpus gate is committed**: `tests/extraction/test_drafts.py` globs the
  real drafts and enforces frontmatter validation, 7 body sections, no
  duplicate ids, acyclic derivation, and welfare-leakage scan under `pytest`.
- **Draft enumerators must use `EXCLUDE_DIRS`**:
  `extraction_pipeline/review_agents/helpers.py` defines
  `EXCLUDE_DIRS = {"project-documentation", "runs"}`. The `runs/` and
  `project-documentation/` dirs under `extraction/20_drafts/` hold run-tracking
  metadata and process docs (not variable definitions). Any code that
  enumerates `20_drafts/` should reuse this constant/set; matching is
  case-sensitive exact, lowercase convention. The review runner also purges
  stale findings yml for artifacts no longer in the corpus
  (`_purge_stale_findings` in `run_all_agents.py`).

## Work in Progress
<!-- Modules, features, or migrations currently underway -->

- Release A production cutover completed on 2026-09-03. Connect runs the
  reviewed app from `main/review-app@f064987357fec71c67df909380ad039450f42eb4`
  and reads `review-production@1399f12fe04c33370f77fee13eff69768c90a769`.
  The descriptor is schema 1.1, all 267 initial review-record blobs are
  preserved, and approval remains disabled. The unchanged
  `review@983d7d9503fbf5c2c911ac9d85a37b88accfe4ac` branch is the data rollback.
- Next review-app work is human content review. The first genuine reviewer and
  distinct approver interaction serves as the production role smoke. Enable
  approval with one governed descriptor-only commit before the first approval.

## Workspace Notes
<!-- Related folders, dependencies on other projects in the VS Code workspace -->

- `review-app/` is a `{golem}` Shiny R package. Golem module tests must capture
  `moduleServer()` return lists and drive namespaced inputs; unexported helpers
  break under R CMD check. See
  `.cg-docs/solutions/testing-patterns/2026-08-10-golem-module-testserver-capture.md`.
- The review app uses Git-backed Connect deployment from repository `main`,
  directory `review-app`. Current deployment and queue identities are recorded
  in `.cg-docs/work-reports/2026-08-26-complete-release-a-production-queue-cutover.md`;
  do not rely on old Publisher bundle metadata.
## Wiki Configuration
<!-- folder: wiki -->
<!-- audience: developers | researchers | end-users -->
<!-- tone: technical | conversational | formal -->
