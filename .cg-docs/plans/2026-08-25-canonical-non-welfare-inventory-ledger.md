---
date: 2026-08-25
title: "Canonical Non-Welfare Inventory Ledger"
status: completed
completed-date: 2026-08-26
failing-steps: []
completed-phases: [1, 2]
execution-report: "../work-reports/2026-08-25-canonical-non-welfare-inventory-ledger.md"
scope: "Standard"
brainstorm: "../brainstorms/2026-08-03-extract-universal-non-welfare-schema.md"
language: "Python"
estimated-effort: "medium"
deviation-policy: "ask"
artifact-schema-version: 1
phases: 2
tags: [extraction, inventory, ledger, provenance, validation, reproducibility]
---

# Plan: Canonical Non-Welfare Inventory Ledger

## Objective

Replace the contradictory prose inventory with one deterministic, row-level,
machine-readable ledger that proves the authoritative non-welfare denominator
is 267 and records every repeated, excluded, helper, inventory-only, and
disputed source occurrence needed to explain the denominator.

## Context

The completed draft corpus contains 267 canonical variable drafts across six
modules: 9 IDN, 14 GEO, 24 DEM, 90 LBR, 61 UTL, and 69 DWL. The current prose
inventory at `extraction/20_drafts/runs/inventory-2026-08-13.md` predates that
reconciliation and reports contradictory LBR and UTL totals. The approved
denominator decision explains the inferred 277 as 267 canonical outputs, five
LBR and four UTL occurrences of IDN-owned identifiers, and one unsupported UTL
phantom count.

The Task C guideline baseline is commit
`d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`. This is the current source
revision named by the task and verified in the read-only sibling checkout; it
is not represented as an approved source identity in the protected source
manifest. Relevant source tables include
Table 2.1 in `chapters/chapter2-IDN.qmd`, the identification table beginning in
`chapters/chapter5-LMR.qmd`, the utilities table beginning in
`chapters/chapter6-UTL.qmd`, and the Chapter 8 tables in
`chapters/chapter8-CONS.qmd`. Source paths, table identities, row locators, and
evidence references must be retained in the ledger.

This task is independent of Task B. The compiler records and verifies the
Task C baseline commit and chapter hashes supplied for generation, but it must
not edit `extraction/config/source-manifest.v1.yaml`, claim that the source-lock
gate is cleared, or modify `SOURCE_INVENTORY_FREEZE_PENDING`. Existing strict
Pydantic, PyYAML, pytest, loguru, path-containment, and deterministic-output
patterns are reused; no new dependency is needed.

On 2026-08-25, after `/cg-plan-review` identified the repository write-policy
ambiguity, the human project operator explicitly answered **Approve explicitly**
to the exact implementation paths, the two generated draft YAML files, the
workflow-managed plan/roadmap/work-report paths, and the Denominator Decision.
That external approval message, summarized in the Approval Record below, is the
task-specific supervision authority; the plan does not authorize itself. This
approval does not amend `AGENTS.md`, permit changes to any other implementation
path, or authorize protected semantic, review, approval, manifest, `knowledge/`,
or country-parameter artifacts.

## Denominator Decision

The human-approved Task C denominator decision, durably recorded by this plan,
is:

1. The canonical denominator is 267: 9 IDN, 14 GEO, 24 DEM, 90 LBR, 61 UTL,
   and 69 DWL.
2. The prior inferred total of 277 is explained by those 267 canonical outputs,
   five LBR and four UTL occurrences of IDN-owned identifiers, and one
   unsupported UTL phantom count.
3. The nine repeats are real guideline-table occurrences and remain row-level
   `shared_identifier_occurrence` records that do not count.
4. The phantom is not a guideline-table occurrence. It is one top-level
   `InventoryDiscrepancy` that cites the obsolete 66-variable claim in
   `extraction/20_drafts/runs/inventory-2026-08-13.md` and references this
   section as its resolution. It must never be given a fabricated source-table
   locator or canonical `variable_id`.
5. The generated v1 file is `status: draft_pending_human_inventory_review`.
   It becomes the authoritative denominator only after the required human
   inventory review and merge; Task B source-identity approval remains a
   separate later condition for clearing the global freeze.

## Approval Record

- **Status**: approved for supervised Task C implementation
- **Authority**: human project operator
- **Date**: 2026-08-25
- **External approval source**: explicit **Approve explicitly** response in the
  `/cg-plan-review` session after the exact scope was presented
- **Implementation paths approved**:
  `schema/extraction/inventory.py`, optional
  `schema/extraction/__init__.py`, `extraction_pipeline/inventory.py`,
  `tests/extraction/test_inventory.py`, optional
  `tests/extraction/test_completeness.py`,
  `extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml`, and
  `extraction/20_drafts/runs/non-welfare-inventory.v1.yaml`
- **Workflow-managed paths approved**:
  `.cg-docs/plans/2026-08-25-canonical-non-welfare-inventory-ledger.md`,
  `roadmap.json`, and
  `.cg-docs/work-reports/2026-08-25-canonical-non-welfare-inventory-ledger.md`
- **Decision approved**: the five numbered statements in the Denominator
  Decision section
- **Rationale**: implement the deterministic ledger without broadening the
  repository's general agent permissions or claiming Task B/human inventory
  approval
- **Durability rule**: the ledger stores the repository-relative plan path,
  exact Approval Record and Denominator Decision section excerpt hashes, and
  the decision date/authority. Final handoff includes this plan in the same
  reviewed change set; section-hash mismatch blocks generation.

## Source Reconciliation Baseline

The pre-implementation source/draft reconciliation is closed and has no
unresolved canonical mismatch. The source map must encode these exact facts;
`/cg-work` verifies them but does not choose alternatives.

| Chapter | Source rows | Canonical | Required non-counting treatment |
|---------|------------:|----------:|---------------------------------|
| 2 IDN | 10 | 9 | 1 `helper_or_metadata` placeholder |
| 3 GEO | 18 | 14 | 4 IDN-owned repeats as `inventory_only` |
| 4 DEM | 29 | 24 | 5 IDN-owned repeats as `inventory_only` |
| 5 LBR | 95 | 90 | 5 IDN-owned `shared_identifier_occurrence` rows |
| 6 UTL | 65 | 61 | 4 IDN-owned `shared_identifier_occurrence` rows |
| 7 DWL | 73 | 69 | 4 IDN-owned repeats as `inventory_only` |
| 8 CONS | 28 | 0 | 28 `welfare_excluded` rows |
| **Total** | **318** | **267** | **51 non-counting rows** |

The nine LBR/UTL shared rows are the repeats that explain the legacy 277
denominator inference. The additional 13 GEO/DEM/DWL identifier occurrences
are retained as contextual `inventory_only` rows so the exhaustive ledger
preserves them without changing the approved nine-repeat arithmetic. The UTL
phantom remains separate top-level discrepancy metadata, so it is not part of
the 318 source-row total.

Mechanical normalization is closed and ordered: trim cell padding; strip only
balanced Markdown emphasis; unescape `\_`; remove whitespace immediately around
underscores; lowercase; remove underscores; prefix `VAR-`. This explains
`marital -> VAR-marital`, `t_hours \_total -> VAR-thourstotal`,
`t_hours \_total_year -> VAR-thourstotalyear`, `LPG_exp -> VAR-lpgexp`, and
unemphasized cells such as `central_acc`; these are fixtures, not semantic
aliases. No arbitrary punctuation removal or spelling repair is allowed.

The complete semantic/corpus alias registry is:

| Raw source name | Source | Canonical draft ID |
|-----------------|--------|--------------------|
| `gual_adm2_code` | `chapter3-GEO.qmd:122` | `VAR-gauladm2code` |
| `eye_dsablty` | `chapter4-DEM.qmd:474` | `VAR-eyedisability` |
| `hear_dsablty` | `chapter4-DEM.qmd:476` | `VAR-heardisability` |
| `walk_dsablty` | `chapter4-DEM.qmd:478` | `VAR-walkdisability` |
| `conc_dsord` | `chapter4-DEM.qmd:480` | `VAR-concentrationdisorder` |
| `slfcre_dsablty` | `chapter4-DEM.qmd:482` | `VAR-selfcaredisability` |
| `comm_dsablty` | `chapter4-DEM.qmd:484` | `VAR-communicationdisability` |
| `wage_noc` | `chapter5-LMR.qmd:445` | `VAR-wagenc` |
| `t_wage_nc_total` | `chapter5-LMR.qmd:783` | `VAR-twagencotal` |
| `t_wage_nc_total_year` | `chapter5-LMR.qmd:1487` | `VAR-twagencototalyear` |
| `elec_exp` | `chapter6-UTL.qmd:740` | `VAR-elecxp` |
| `kerosene_exp` | `chapter6-UTL.qmd:752` | `VAR-kerosenexp` |

Ten UTL cells carry a cited terminal `\*` derived-variable annotation that is
not part of the name: `water_exp`, `waste_exp`, `gas_exp`, `liquid_exp`,
`solid_exp`, `utl_exp`, `othhousing_exp`, `tel_exp`, `comm_exp`, and
`tvintph_exp` at Chapter 6 lines 590, 596, 746, 756, 766, 774, 874, 882, 888,
and 892. The source map records each as an explicit annotation-removal mapping
and cites the explanatory footnotes at lines 601, 777, and 895. It must not use
a blanket punctuation-deletion rule. The sole module alias is source filename
`chapter5-LMR.qmd`/`LMR` to heading/module `MOD-LBR` (heading line 2).

The 28 source captions contain 27 inventory-bearing tables. Required
disambiguations are: Table 6.2 is one logical table with ordered physical
fragments of 5 and 4 rows; the two Table 7.7 captions become distinct
agricultural-land and legal-documentation-image keys, with the latter explicitly
non-inventory; Table 5.6 retains its incorrect raw 7-day caption but is keyed as
the 12-month table from row/section evidence; duplicate/skipped printed ordinals
never define occurrence identity; Table 6.3 uses positional column 3 as the raw
name despite duplicate headings; Table 7.7 accepts `Variable` as its configured
name header; and Markdown emphasis is optional presentation. Any new mismatch,
alias, table fragment, or ambiguity is a blocked source delta.

Relevant project lessons:

- Inventory facts come from authoritative source tables, while skills and
  prose summaries are secondary hints.
- Normalized IDs use `VAR-` plus the source name with underscores removed,
  except for already-governed corpus mappings such as `VAR-marital`.
- IDN owns shared identifiers and weights even when they occur in another
  module's source table.
- Chapter 8 scope must be enforced from source path/evidence, never from an ID
  substring heuristic.
- Volatile timestamps and environment details must not enter deterministic
  content artifacts.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Add strict Pydantic inventory contracts with forbidden extra fields, stable occurrence keys/IDs, normalized `variable_id`, complete source reference (`source_name`, path, table key, occurrence key), owner module, tier, derivation status, disposition, inline validated citation, draft path, and explicit denominator-count state. Model non-source count claims separately as `InventoryDiscrepancy`. | Invocation requirement 1; existing `schema/extraction/*.py` conventions; P1.4/P2.2 review |
| R2 | Define exactly the six approved row dispositions: `canonical_output`, `shared_identifier_occurrence`, `helper_or_metadata`, `welfare_excluded`, `inventory_only`, and `unresolved_source_discrepancy`; enforce the biconditional `counts_toward_denominator == (disposition == canonical_output)` and equality of canonical-row, true-count, and aggregate-denominator totals. | Invocation requirements 1, 4, 7, 8; P1.5 review |
| R3 | Compile occurrences deterministically from immutable Git object bytes at the Task C baseline and the current `extraction/20_drafts/{idn,geo,dem,lbr,utl,dwl}/VAR-*.md` paths. Verify all seven chapter SHA-256 values from the source-lock report; never read dirty working-tree QMD bytes. | Invocation requirements 2, 4; P1.2/P1.3 review |
| R4 | Enforce one canonical row per normalized variable ID, exactly 267 canonical rows, and exact owner-module counts of 9 IDN, 14 GEO, 24 DEM, 90 LBR, 61 UTL, and 69 DWL. | Governing facts; invocation requirement 5 |
| R5 | Preserve five LBR and four UTL source occurrences of IDN-owned identifiers as non-counting shared rows. Preserve the unsupported fifth UTL count as one non-counting top-level discrepancy citing the obsolete prose claim and this plan's denominator decision, not as a fabricated source occurrence. | Governing facts; invocation requirements 6-7; P1.4 review |
| R6 | Record source-grounded helper/metadata, inventory-only, and Chapter 8 welfare exclusions with byte-verifiable inline citations; no Chapter 8 row may enter the canonical set. | Governing facts; invocation requirement 8; welfare-boundary lesson; P2.2 review |
| R7 | Serialize a versioned, deterministic YAML ledger at `extraction/20_drafts/runs/non-welfare-inventory.v1.yaml` with stable row order, stable key order, no volatile fields, and byte-identical output for identical inputs. | Invocation requirements 3-4; validation and acceptance criteria |
| R8 | Add fixed-set and failure-mode tests covering duplicate normalized IDs, missing/extra/renamed drafts, wrong ownership, both directions of the counting invariant, welfare leakage, missing/tampered citations, dirty source files, hash mismatch, wrong counts, source-map coverage, locator semantics, lock contention, nondeterministic row order, and nondeterministic bytes. | Invocation requirement 9; failure modes; plan review |
| R9 | Keep Task B and all protected artifacts unchanged; completion produces a review-ready ledger without implementing Task B, clearing global blockers, or fabricating human inventory approval. | AGENTS.md; merge dependency; protected-path acceptance criterion |
| R10 | Add a versioned source-map draft at `extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml` that exhaustively enumerates the closed 28-caption/27-table/318-row baseline, expected occurrence keys/counts/classifications, all explicit aliases/annotations, ownership rules, chapter hashes, exact toolchain versions, and phantom claim/resolution references. | P1.6/P2.1/P2.8/P3.1 review |
| R11 | Make `/cg-work` verification executable by defining environment setup, exact candidate compiler/validation/promotion commands, immutable-source integration checks, the named work report, and a content-sensitive baseline allowlist audit. | P1.7/P2.6/P2.7 review |

## Implementation Steps

## Phase 1: Authorized Contracts and Deterministic Compiler

### 1. Establish the execution preflight and change baseline

- **Requirements**: R9, R11
- **Files**: reads `requirements.txt`; creates only the ignored local `.venv/`, temporary baseline files, and workflow-managed `.cg-docs/work-reports/2026-08-25-canonical-non-welfare-inventory-ledger.md`
- **Details**: Confirm the selected `/cg-work` run is executing this human-approved plan and therefore has task-specific supervision for only the allowed paths. Create the missing Python environment with `uv`, install the existing requirements without changing dependency files, smoke-test imports, and capture the complete staged/unstaged/untracked baseline before implementation:

  ```bash
  test -x .venv/bin/python || uv venv --python 3.11 .venv
  uv pip install --python .venv/bin/python -r requirements.txt
  .venv/bin/python -c "import loguru, pydantic, pytest, yaml"
  uv pip freeze --python .venv/bin/python > "${TMPDIR:-/tmp}/task-c-python.freeze"
  git rev-parse HEAD > "${TMPDIR:-/tmp}/task-c-head.before"
  git status --porcelain=v1 --untracked-files=all > "${TMPDIR:-/tmp}/task-c-status.before"
  ```

  Before any implementation edit, also capture content-sensitive baseline files
  for every path outside the approved implementation and workflow-managed
  allowlists: (1) `git diff --binary HEAD`, (2) `git diff --cached --binary
  HEAD`, and (3) a sorted `git hash-object` record for every untracked file.
  Apply exact Git `:(exclude)<path>` pathspecs for the seven implementation
  paths plus this plan, `roadmap.json`, and the named work report. Save the
  three results as `${TMPDIR:-/tmp}/task-c-worktree.before.diff`,
  `task-c-index.before.diff`, and `task-c-untracked.before.hashes`. This records
  content, staging, additions, removals, and status transitions rather than
  status labels alone. Record the HEAD, exact frozen package versions, full
  porcelain status, baseline artifact hashes, and command results in the named
  work report. Stop if `uv` cannot supply Python 3.10+, imports fail, or the
  baseline cannot be captured.
- **Test Scenarios**: happy path (environment and imports ready); edge case (existing compatible `.venv` reused); error path (missing `uv`, unsupported Python, install failure, or plan authorization/path mismatch).
- **Tests**: `.venv/bin/python --version`; `.venv/bin/python -m pytest --version`
- **Acceptance criteria**: every later verification command is executable and the pre-task change baseline is durably recorded.

### 2. Define strict row, discrepancy, citation, and ledger contracts

- **Requirements**: R1, R2
- **Files**: `schema/extraction/inventory.py`; `schema/extraction/__init__.py` only if a package export is required; `tests/extraction/test_inventory.py`
- **Details**: Add strict enums and models for source references, occurrence rows, aggregate module counts, top-level discrepancies, and the versioned ledger. Reuse `schema.extraction.evidence.Citation` inline for every source occurrence and validate its source path, line bounds, exact excerpt, and excerpt SHA-256 against immutable bytes. Give discrepancies a repository-local claim citation plus an exact decision reference. Derive occurrence IDs from inventory version plus the curated stable `occurrence_key` in the source map, never from line numbers or parser enumeration order. Validate normalized `variable_id` values and require them for canonical/shared rows. Enforce `counts_toward_denominator == (disposition == canonical_output)`, and require canonical-row count, true-count, and ledger denominator to match. Require a draft path and valid owner for canonical rows. Reject duplicate occurrence IDs/keys and duplicate canonical normalized IDs.
- **Test Scenarios**: happy path (valid canonical, noncanonical, and discrepancy records); edge case (helper row with no canonical draft); error path (extra field, malformed ID, canonical row marked false, noncanonical row marked true, missing/tampered citation, discrepancy without both references, duplicate occurrence key, or duplicate canonical ID).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q -k "model or citation or counting"`
- **Acceptance criteria**: invalid counting, evidence, discrepancy, identity, and uniqueness states cannot be represented by a validated ledger.

### 3. Add the exhaustive source map and pure compiler pipeline

- **Requirements**: R3, R5, R6, R10
- **Files**: `extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml`; `extraction_pipeline/inventory.py`; `tests/extraction/test_inventory.py`
- **Details**: Create one reviewable input contract that records the Task C baseline SHA, the seven chapter hashes from `source-lock-2026-08-13.md`, exact Python/Pydantic/PyYAML/loguru toolchain versions from Step 1, table order, unique table keys, duplicate-caption disambiguators, physical fragments, expected occurrence keys/raw names/counts, required dispositions, owner rules, and explicit exclusions. The compiler rejects a toolchain mismatch so later replay installs the recorded exact versions rather than silently accepting a new serializer/model stack. Encode the complete Source Reconciliation Baseline above: 28 captions, 27 inventory-bearing tables, 318 source rows, 267 canonical rows, and all 51 non-counting row dispositions. Include every mechanical fixture, all 12 semantic/corpus aliases, all 10 cited terminal-annotation removals, the LMR-to-LBR module alias, every table disambiguation, and the 13 GEO/DEM/DWL repeats classified as `inventory_only`. This list is closed; unknown aliases or mismatches block generation rather than being decided by `/cg-work`.

  Choose a bounded built-in parser, not Pandoc: derive grid-table column boundaries from separator rows, join continuation lines within each row band, parse pipe-table cells, strip only configured Markdown emphasis/escape syntax, and preserve raw cell text plus line spans. The parser supports only the exact grid/pipe constructs covered by real-source fixtures and fails on any unrecognized inventory-bearing construct. Split the implementation into pure functions that accept source bytes/draft records/source-map data and an orchestration wrapper that obtains each QMD with `git show <sha>:<path>`, verifies its configured SHA-256, then invokes the pure compiler. Never read source working-tree files. A dirty checkout at the same `HEAD` must therefore produce the same output as the immutable Git object; a missing object or hash mismatch must fail.

  Treat parser input enumeration order as irrelevant and normalize it through source-map order. Treat any source-row movement/content change as a source-byte/hash delta requiring a new source-map/ledger version; do not preserve identity across changed source bytes. Model five LBR and four UTL repeats as IDN-owned shared rows. Model the phantom only as top-level discrepancy metadata. Bind its obsolete-inventory citation to the current canonical-schema HEAD/blob plus exact line/excerpt hash, and bind its resolution to the repository-relative plan path plus exact Approval Record and Denominator Decision section excerpt hashes/date/authority. Section-hash mismatch or absence of the plan in the final reviewed change set blocks generation.
- **Test Scenarios**: happy path (pure fixture compiler and temporary-Git wrapper compile); edge case (split grid, duplicate caption, escaped/case/alias name, dirty checkout at correct HEAD, and shuffled in-memory enumeration); error path (missing table/fragment/row, unclassified inventory-bearing row, unknown alias, wrong Git object, hash mismatch, modified source bytes supplied to pure validation, extra draft, or wrong owner).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q -k "parser or source_map or compiler or git_object or alias"`
- **Acceptance criteria**: all configured source occurrences and exclusions are exhaustive, byte-grounded, and mapped bijectively to classified ledger rows or the explicit non-source discrepancy.

### 4. Enforce totals and write deterministic output safely

- **Requirements**: R4, R7, R8
- **Files**: `extraction_pipeline/inventory.py`; `tests/extraction/test_inventory.py`
- **Details**: Finalize only when canonical count, true-count, and denominator all equal 267; module counts equal `9/14/24/90/61/69`; shared rows are exactly the approved five LBR plus four UTL occurrences; discrepancies contain exactly the one non-counting UTL phantom; and no Chapter 8 row is canonical. Sort by explicit source-map table order and occurrence order, then stable occurrence ID; evidence line numbers do not define identity. Serialize validated model data with fixed PyYAML options, UTF-8, LF, trailing newline, and fixed key order. Acquire an exclusive sibling lock file, write through a unique same-directory temporary file, flush and `fsync`, commit with `os.replace`, and clean temporary/lock files on every failure. Fail clearly on lock contention; never reuse the existing predictable `.tmp` writer pattern.
- **Test Scenarios**: happy path (approved totals serialize); edge case (shuffled parser enumeration gives identical bytes); error path (canonical false-count, wrong module total, repeat/discrepancy/welfare counted, output escape, lock contention, stale temporary file, write failure, or second serialization differs).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q -k "totals or deterministic or writer or lock"`
- **Acceptance criteria**: finalization fails on every denominator/scope invariant, concurrent writers cannot corrupt output, and identical immutable inputs always produce identical bytes.

## Phase 2: Ledger Freeze and Regression Gates

### 5. Complete fixed-set, source-coverage, and adversarial tests

- **Requirements**: R8, R9, R10
- **Files**: `tests/extraction/test_inventory.py`; `tests/extraction/test_completeness.py` only for minimal ledger integration if required
- **Details**: Expand the tests created alongside Steps 2-4. Use `tmp_path` source snippets, temporary Git repositories, draft corpora, lock files, and output paths; unit tests remain network-independent and never mutate the sibling checkout. Add a committed-corpus test that loads the source map and v1 ledger and compares canonical draft paths, normalized IDs, and ownership to the exact repository glob. Parameterize every requested failure mode plus the critic cases: canonical false-count, dirty checkout, hash mismatch, omitted table/fragment/row, unknown alias, broken/tampered evidence, source-row mutation, parser-enumeration shuffle, lock contention, and stale-temp cleanup. Test welfare classification from source path in both directions.
- **Test Scenarios**: happy path (source map and committed ledger match all 267 drafts); edge case (noncanonical occurrence shares a normalized ID and remains non-counting); error path (each mutation independently fails validation or compilation).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q`; `.venv/bin/python -m pytest tests/extraction/test_completeness.py -q`
- **Acceptance criteria**: adding, removing, renaming, or re-owning a draft, or omitting/reclassifying a source occurrence, fails until an explicit versioned source-map and ledger update is reviewed.

### 6. Generate, validate, and atomically promote the review-ready v1 ledger

- **Requirements**: R3, R4, R5, R6, R7, R8, R9, R10, R11
- **Files**: `extraction/20_drafts/runs/non-welfare-inventory.v1.yaml`
- **Details**: Set `GMD_GUIDELINES_REPO` to the read-only sibling Git repository. Generate two candidates from immutable Git objects without touching the prior ledger, compare and validate them, run all required tests against candidate A through `INVENTORY_LEDGER_PATH`, and only then atomically promote candidate A through the lock-protected writer. Any pre-promotion failure leaves the prior ledger unchanged. Every command below must exit 0:

  ```bash
  : "${GMD_GUIDELINES_REPO:?set to the read-only GMD-guidelines Git repository}"
  SOURCE_SHA=d46dc03d253764ad7bdef53f625d54fd2a0a9ea1
  SOURCE_MAP=extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml
  LEDGER=extraction/20_drafts/runs/non-welfare-inventory.v1.yaml
  CANDIDATE_A="$(mktemp extraction/20_drafts/runs/.non-welfare-inventory.candidate-a.XXXXXX)"
  CANDIDATE_B="$(mktemp extraction/20_drafts/runs/.non-welfare-inventory.candidate-b.XXXXXX)"
  trap 'rm -f "$CANDIDATE_A" "$CANDIDATE_B"' EXIT
  .venv/bin/python -m extraction_pipeline.inventory compile --source-repo "$GMD_GUIDELINES_REPO" --source-commit "$SOURCE_SHA" --source-map "$SOURCE_MAP" --draft-root extraction/20_drafts --output "$CANDIDATE_A"
  .venv/bin/python -m extraction_pipeline.inventory compile --source-repo "$GMD_GUIDELINES_REPO" --source-commit "$SOURCE_SHA" --source-map "$SOURCE_MAP" --draft-root extraction/20_drafts --output "$CANDIDATE_B"
  cmp -s "$CANDIDATE_A" "$CANDIDATE_B"
  .venv/bin/python -m extraction_pipeline.inventory validate --source-repo "$GMD_GUIDELINES_REPO" --source-commit "$SOURCE_SHA" --source-map "$SOURCE_MAP" --draft-root extraction/20_drafts --ledger "$CANDIDATE_A"
  INVENTORY_LEDGER_PATH="$CANDIDATE_A" .venv/bin/python -m pytest tests/extraction/test_inventory.py -q
  INVENTORY_LEDGER_PATH="$CANDIDATE_A" .venv/bin/python -m pytest tests/extraction/test_completeness.py -q
  INVENTORY_LEDGER_PATH="$CANDIDATE_A" .venv/bin/python -m pytest tests/ -q
  .venv/bin/python -m extraction_pipeline.inventory promote --source-repo "$GMD_GUIDELINES_REPO" --source-commit "$SOURCE_SHA" --source-map "$SOURCE_MAP" --draft-root extraction/20_drafts --candidate "$CANDIDATE_A" --output "$LEDGER"
  cmp -s "$LEDGER" "$CANDIDATE_A"
  rm "$CANDIDATE_A" "$CANDIDATE_B"
  trap - EXIT
  ```

  Validate `status: draft_pending_human_inventory_review`, 267 and `9/14/24/90/61/69`, all 318 source rows, 51 non-counting rows, nine shared rows, one non-source discrepancy, complete source-map coverage/evidence, and zero Chapter 8 canonical rows before promotion.

  Implementation allowlist:

  ```text
  schema/extraction/inventory.py
  schema/extraction/__init__.py
  extraction_pipeline/inventory.py
  tests/extraction/test_inventory.py
  tests/extraction/test_completeness.py
  extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml
  extraction/20_drafts/runs/non-welfare-inventory.v1.yaml
  ```

  Recreate the Step 1 HEAD, full porcelain status, non-allowlisted worktree
  binary diff, non-allowlisted index binary diff, and non-allowlisted untracked
  `git hash-object` list with identical exclusion pathspecs. Require HEAD
  unchanged and `cmp -s` equality for all three content-sensitive baseline
  artifacts. This detects edits to paths already dirty at baseline, added or
  removed files, staging changes, and status transitions. Retain the full
  before/after porcelain reports to enumerate allowed Task C/workflow changes.
  Attach all commands, hashes, and comparison results to the named work report.
  Do not use status-set difference or `git diff --name-only` as the safety gate.
  Present the ledger and source map for human inventory review without writing
  a review decision or clearing a blocker.
- **Test Scenarios**: happy path (candidates match, all pre-promotion checks pass, and one candidate promotes atomically); edge case (pre-existing non-allowlisted dirty content is byte-identical and workflow-managed paths change as expected); error path (missing source object, hash/toolchain mismatch, generation/validation/test/cmp failure, non-allowlisted content/index/untracked change, HEAD change, or promotion failure preserves the prior ledger).
- **Tests**: exact candidate CLI/validation/test/promotion sequence above; content-sensitive baseline HEAD/diff/index/untracked-hash comparison
- **Acceptance criteria**: one review-ready, byte-stable v1 draft ledger and its exhaustive source map exist, all required evidence passes before promotion, no protected artifact changed, and the human review/Task B source-identity gates remain explicit.

## Testing Strategy

- Model-level tests validate strict fields, enums, normalization, cross-field
  invariants in both directions, inline citations, discrepancies, duplicate
  occurrence keys/IDs, and duplicate canonical IDs.
- Parser/compiler unit tests use real-syntax grid/pipe snippets, temporary Git
  repositories, and temporary draft sets; they remain network-independent and
  do not depend on the sibling checkout.
- Immutable-source integration invokes the CLI against `git show` objects at
  the Task C baseline and verifies all seven configured chapter hashes. Dirty
  working-tree source files are deliberately ignored; missing/tampered objects
  fail.
- Source-map coverage scans all captioned tables and requires every
  inventory-bearing table fragment and row to be selected or cited as excluded.
- Corpus tests load the committed source map and ledger and compare the
  canonical subset to the exact 267 draft paths and module ownership currently
  in the repository.
- Adversarial tests mutate one fact at a time: path, name, owner, disposition,
  either direction of count state, occurrence key, citation line/hash/excerpt,
  source hash, table selection, alias, source path, or source row.
- Reproducibility tests compile twice into separate temporary files and compare
  bytes, including newline and key/row order. Parser enumeration shuffle must
  normalize; source-row/content movement must fail as a source delta.
- Writer tests exercise unique temporary files, `fsync`/`os.replace`, lock
  contention, failure cleanup, and stale unrelated temporary files.
- Existing completeness tests run after focused inventory tests, followed by
  the complete repository suite.
- The final path audit requires unchanged HEAD and compares binary worktree and
  index diffs plus untracked-file content hashes outside the exact implementation
  and workflow allowlists. Full porcelain reports remain supplementary evidence;
  pre-existing dirty content cannot be edited invisibly.

## Documentation Checklist

- [ ] Ledger top-level metadata states inventory version, authoritative source
  repository, Task C baseline commit/hashes, normalization contract version,
  draft review status, and totals. Task B remains an independent gate.
- [ ] The source map enumerates every inventory-bearing table/fragment/row,
  explicit exclusion, known alias, ownership rule, and expected classification.
- [ ] Every occurrence row includes source name/path/table key/occurrence key
  and an inline citation validated against immutable source bytes.
- [ ] The top-level discrepancy cites the obsolete UTL 66-variable prose claim
  and this plan's Denominator Decision, and states that it is retired/non-counting
  without inventing a source occurrence or canonical variable.
- [ ] The nine shared occurrences identify IDN as owner and retain LBR/UTL as
  occurrence context.
- [ ] Chapter 8, helper/metadata, and inventory-only exclusions include a reason
  and citation.
- [ ] Known source aliases preserve raw spelling and cite their explicit
  reconciliation; unknown aliases remain blocking.
- [ ] Compiler public functions and CLI arguments have concise docstrings and
  typed signatures.
- [ ] Environment setup, exact generation/replay commands, and changed-path
  audit evidence are recorded in
  `.cg-docs/work-reports/2026-08-25-canonical-non-welfare-inventory-ledger.md`.
- [ ] The old prose inventory is left unchanged but is no longer used as an
  executable authority.
- [ ] Human inventory review is requested after generation; no review decision
  is fabricated or written by the implementation agent.

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Source tables contain irregular/split grid syntax or duplicate captions | Silent row loss or wrong denominator | Bounded parser over real-source fixtures plus exhaustive source-map table/fragment/row coverage; fail on unknown constructs |
| A duplicated source occurrence is mistaken for a canonical output | Denominator exceeds 267 | Encode counting as a schema invariant; assert exact shared-occurrence set and module totals |
| A prose or filename heuristic misclassifies Chapter 8 or ownership | Welfare leakage or wrong module totals | Classify from source path, source module code, explicit ownership contract, and evidence; test both false-positive and false-negative cases |
| Dirty source files are read at the expected Git `HEAD` | Ledger falsely claims baseline bytes | Read only `git show <sha>:<path>` objects and verify configured SHA-256 values; test dirty checkout and hash mismatch |
| Known malformed/case/alias names are silently normalized | Canonical IDs drift from reviewed drafts | Version all aliases in the source map with raw spelling/evidence; block unknown mismatches |
| Evidence fields accept arbitrary strings or stale lines | Unverifiable row grounding | Embed strict citations and revalidate source path, line bounds, excerpt, and hash against immutable bytes |
| YAML output changes across runs | No reproducible inventory freeze | Fix model dump, key/row order, encoding, newline, and serializer options; compare exact bytes from two runs |
| Draft corpus changes without ledger review | Stale denominator and hidden path drift | Fixed-set test compares exact ledger IDs/paths/owners to the current corpus and fails on any delta |
| Task C accidentally alters Task B or governed artifacts | Merge conflict or governance violation | Keep manifest/blocker changes out of scope and enforce final changed-path audit |
| UTL phantom is modeled as a nonexistent guideline row | Fabricated locator/evidence | Use top-level discrepancy metadata citing the obsolete prose claim and this plan's durable denominator decision |
| Concurrent generation corrupts the ledger | Partial or nondeterministic output | Exclusive lock, unique same-directory temporary file, flush/fsync, `os.replace`, and cleanup tests |
| Local verification environment is absent | `/cg-work` cannot satisfy required evidence | Step 1 creates `.venv` with `uv`, installs existing requirements, and smoke-tests imports before mutation |

## Out of Scope

- Modifying `extraction/config/source-manifest.v1.yaml` or implementing source
  identity enforcement owned by Task B.
- Clearing `SOURCE_INVENTORY_FREEZE_PENDING` or any other global blocker.
- Editing existing variable draft semantics, derivation graphs, source
  manifests, review records, approval records, `knowledge/`, or
  `country-parameters/`.
- Promoting the generated ledger to an approved or canonical knowledge path.
- Claiming that the Task C baseline commit is the human-approved Task B source
  identity, or marking the draft ledger human-approved.
- Resolving a newly discovered source discrepancy without a human denominator
  decision and an explicit new ledger version.
- Adding Pandoc or another dependency. The bounded parser supports only the
  configured grid/pipe table syntax needed for this fixed ledger.
- Replacing the broader extraction orchestrator or implementing a general QMD
  parser beyond the source-map table/locator contract.

## Completion Contract

### Outcome

A review-ready versioned YAML ledger and exhaustive source map deterministically
account for every configured source occurrence while identifying exactly 267
unique canonical non-welfare outputs with module counts `9/14/24/90/61/69`.
The nine LBR/UTL identifier repeats, top-level retired UTL phantom discrepancy,
helper/inventory-only rows, and Chapter 8 exclusions remain visible but cannot
enter the canonical denominator; the Task B gate and human inventory review
remain unresolved rather than being fabricated.

### Verification Surface

| ID | Phase | Evidence Required | Command/Artifact | Required |
|----|-------|-------------------|------------------|----------|
| V1 | 1 | Python 3.10+ environment and required imports/tests are executable; exact package versions and content-sensitive pre-task baseline are recorded | Step 1 `uv`/freeze/import/HEAD/diff/index/untracked-hash evidence in `.cg-docs/work-reports/2026-08-25-canonical-non-welfare-inventory-ledger.md` | yes |
| V2 | 1 | Strict models reject extra fields, invalid identities/dispositions, both illegal count directions, missing/tampered citations, and invalid discrepancies | `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q -k "model or citation or counting"` | yes |
| V3 | 1 | Versioned source map covers every inventory-bearing table/fragment/row, explicit exclusion, known alias, owner rule, and expected classification | `extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml`; `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q -k "source_map"` | yes |
| V4 | 1 | Compiler reads verified immutable Git objects, ignores dirty working files, validates chapter hashes/citations, and reconciles exact 267 drafts with `9/14/24/90/61/69` | `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q -k "source_map or compiler or git_object or alias"` | yes |
| V5 | 2 | Ledger contains exactly nine IDN-owned shared rows, one non-source UTL discrepancy, cited helper/inventory/welfare exclusions, pending approval statuses, and zero Chapter 8 canonical rows | `extraction/20_drafts/runs/non-welfare-inventory.v1.yaml` plus focused tests | yes |
| V6 | 2 | Two exact Step 6 candidates are byte-identical, validate, pass all candidate-directed tests, leave no stale temporary file, and promote only afterward | Step 6 compile/compile/`cmp`/validate/test/promote/cleanup sequence | yes |
| V7 | 2 | Draft/source add/remove/rename/reorder, duplicate normalized ID, wrong owner, omitted source row, unknown alias, hash/evidence tamper, lock contention, and forbidden counting all fail | `.venv/bin/python -m pytest tests/extraction/test_inventory.py -q` | yes |
| V8 | final | Existing completeness behavior remains green against the validated candidate | `INVENTORY_LEDGER_PATH="$CANDIDATE_A" .venv/bin/python -m pytest tests/extraction/test_completeness.py -q` | yes |
| V9 | final | Repository-wide regression suite passes against the validated candidate before promotion | `INVENTORY_LEDGER_PATH="$CANDIDATE_A" .venv/bin/python -m pytest tests/ -q` | yes |
| V10 | final | HEAD is unchanged; every non-allowlisted staged, unstaged, and untracked path retains its baseline content/index/hash state; only exact implementation/workflow paths may differ | Step 6 HEAD plus binary worktree/index diff and untracked `git hash-object` comparisons in the named work report | yes |

### Constraints

| ID | Phase | Constraint | Check |
|----|-------|------------|-------|
| C1 | all | External human approval covers only the exact implementation/workflow paths and Denominator Decision recorded in the Approval Record; it does not amend general repository governance | Approval Record plus V10 allowlist evidence |
| C2 | all | Do not modify `knowledge/`, review/approval records, source manifests, protected semantic fields, or country parameters | V10 baseline-aware path audit |
| C3 | all | `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` is the Task C baseline, not an approved Task B source identity | Ledger commit/hash fields, `git show` byte/hash validation, and no manifest change |
| C4 | 1-2 | Preserve source occurrences; deduplicate only canonical outputs by normalized `variable_id` | Occurrence/cardinality tests |
| C5 | 1-2 | Counting is biconditional: every and only `canonical_output` row counts; Chapter 8 and all noncanonical dispositions cannot count | Model, aggregate, and welfare tests |
| C6 | 2 | Any drift from 28 captions, 27 inventory tables, 318 source rows, 267 canonical rows, 51 non-counting rows, source bytes, drafts, owners, closed aliases, or classifications requires an explicit version update | Fixed-set/source-coverage tests |
| C7 | all | No new dependency and no dependency on Task B implementation | `requirements.txt` unchanged; path audit |
| C8 | 1-2 | Evidence resolves to immutable source bytes; the phantom remains discrepancy metadata with no fabricated source locator | Citation/hash and discrepancy tests |
| C9 | 1-2 | Output commits are lock-protected, unique-temp, flushed, atomically replaced, and cleaned on failure | Writer/lock tests |

### Boundaries

- Allowed by the external Approval Record: `schema/extraction/inventory.py`, minimal export wiring if required,
  `extraction_pipeline/inventory.py`, `tests/extraction/test_inventory.py`,
  focused completeness-test integration if needed, and
  `extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml` and
  `extraction/20_drafts/runs/non-welfare-inventory.v1.yaml`.
- Allowed: read-only Git-object access to the sibling guideline repository at
  the Task C baseline to generate and verify source locators/citations.
- Workflow-managed: this plan, `roadmap.json`, and
  `.cg-docs/work-reports/2026-08-25-canonical-non-welfare-inventory-ledger.md`.
- Out of scope: changing `extraction/config/source-manifest.v1.yaml`,
  implementing Task B, clearing `SOURCE_INVENTORY_FREEZE_PENDING`, editing any
  variable draft's semantic fields, changing review state, or promoting
  artifacts to `knowledge/`.
- Out of scope: resolving new source discrepancies beyond the approved retired
  UTL phantom decision, adding dependencies, or claiming source/human approval.

### Iteration Policy

1. Encode schema invariants before compiler behavior so invalid counting states
   are unrepresentable.
2. Freeze the exhaustive source map, aliases, and occurrence keys before
   compiling; unknown tables, rows, aliases, or discrepancies block rather than
   trigger inference.
3. Read immutable Git objects, verify chapter hashes and inline citations, and
   keep dirty working-tree bytes outside the evidence chain.
4. Reconcile against the exact committed draft path set; fail before writing on
   any missing, extra, duplicate, ownership, classification, or count mismatch.
5. Serialize through the lock-protected unique-temp writer, run the exact CLI
   twice, and compare bytes before accepting the generated ledger.
6. Run focused inventory tests, completeness tests, the full suite, and the
   baseline-aware path audit; fix only in-scope regressions.
7. Under `deviation-policy: ask`, pause before changing file boundaries, source
   map semantics, denominator counts, aliases, discrepancy dispositions, parser
   contract, or dependencies.

### Blocked-Stop Conditions

- The external human approval summarized in the Approval Record cannot be
  verified from the session, or implementation requires a path/decision outside
  its exact scope.
- The sibling guideline Git repository lacks the Task C baseline object, a
  chapter hash differs, or immutable bytes cannot be read with `git show`.
- An inventory-bearing table/fragment/row cannot be parsed, assigned a stable
  source-map occurrence key, or exhaustively classified.
- A citation cannot be verified against immutable bytes, or a known/unknown
  alias lacks an explicit source-map decision.
- Source rows reveal a discrepancy not covered by the approved denominator
  decision.
- Exact counts, ownership, or the fixed draft set cannot be reconciled without
  editing protected artifacts.
- The Python environment cannot be created from existing `requirements.txt`,
  or implementing the bounded parser would require a new dependency.
- Lock contention persists or atomic output cleanup cannot be guaranteed.
- Required tests or byte-reproducibility checks remain failing after in-scope
  recovery.
- HEAD changes, or the final content-sensitive baseline audit finds any
  non-allowlisted worktree/index/untracked hash difference.
- Continuing would require source-manifest, semantic-draft, review-record,
  approval-record, `knowledge/`, or country-parameter changes.

## Review Resolution Log

All findings from `/cg-plan-review` on 2026-08-25 were accepted for revision;
none were deferred or accepted as residual risk.

| Finding | Resolution |
|---------|------------|
| P1.1 | Obtained an external **Approve explicitly** response from the human operator and recorded its exact implementation/workflow scope, decision scope, authority, date, rationale, and blocked stops. |
| P1.2 | Reclassified `d46dc...` as the Task C baseline and removed claims of Task B approval. |
| P1.3 | Required `git show` immutable bytes, seven chapter hashes, dirty-checkout behavior, and mismatch tests. |
| P1.4 | Added the externally approved Denominator Decision; modeled the phantom as top-level discrepancy metadata bound to the obsolete-inventory HEAD/blob citation and exact approval/decision section hashes, not a source row. |
| P1.5 | Made the count invariant biconditional and equated canonical-row, true-count, and denominator totals. |
| P1.6 | Added an exhaustive versioned source map covering tables, fragments, rows, classifications, and exclusions. |
| P1.7 | Replaced status-set/path-only checks with unchanged-HEAD plus binary worktree/index diffs and untracked content hashes outside exact implementation/workflow allowlists. |
| P2.1 | Completed the source reconciliation: 12 semantic/corpus aliases, 10 cited annotation removals, one module alias, closed mechanical rules, and no unresolved canonical mismatch. |
| P2.2 | Reused inline strict citations with path/line/excerpt/hash validation and added tamper tests. |
| P2.3 | Chose a bounded built-in grid/pipe parser, specified its syntax contract, and prohibited new parser dependencies. |
| P2.4 | Created focused model/compiler tests alongside Phase 1 steps; Phase 2 only expands adversarial/corpus gates. |
| P2.5 | Split pure byte/data APIs from the Git-object orchestration wrapper and specified temporary-Git integration tests. |
| P2.6 | Added executable `uv` environment setup, exact version freeze, named work-report evidence, and source-map toolchain enforcement. |
| P2.7 | Added exact two-candidate compile/compare/validate/test/atomic-promote/cleanup commands; prior ledger remains untouched until every pre-promotion check passes. |
| P2.8 | Defined stable curated occurrence keys, enumeration-order normalization, and source-row movement as a blocking version delta. |
| P3.1 | Replaced fixed `.tmp` reuse with lock-protected unique temporary output, flush/fsync, `os.replace`, cleanup, and concurrency tests. |

The first verification pass surfaced six residual P1/P2 items and one P3 item.
They were also accepted and resolved: external human approval was obtained;
decision citations were content-bound; the path audit became content-sensitive;
the work-report path was explicitly authorized; source aliases were exhaustively
closed; promotion became fail-closed; and exact toolchain versions became part
of the v1 source-map/replay contract.
