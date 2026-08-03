---
date: 2026-08-03
title: "Extract the Universal Non-Welfare Schema"
status: active
scope: "Deep"
brainstorm: "../brainstorms/2026-08-03-extract-universal-non-welfare-schema.md"
language: "Python"
estimated-effort: "large"
deviation-policy: "ask"
phases: 6
tags: [extraction, non-welfare, provenance, validation, agents, python]
---

# Plan: Extract the Universal Non-Welfare Schema

## Objective

Build an evidence-first corpus compiler that locks the authoritative GMD
guideline revision, inventories every non-welfare output in chapters 2 through
7, preserves chapter 8 and helper exclusions in a ledger, and emits only
fully supported, cited CVS drafts under `extraction/20_drafts/`. Every locked
inventory item must end in either a gate-passing draft set or a
machine-readable blocking issue.

## Context

The architecture baseline is the decided Deep brainstorm linked in
frontmatter. Its pinned source SHA is evidence from planning, not an approved
implementation input; Phase 1 must resolve and approve the revision again.

The repository already has strict Pydantic models for variables, rules, and
parameters; a Markdown front-matter loader; a canon-oriented validator; a
bundle compiler; and pytest fixtures based on disposable repositories. It has
no extraction manifest, AST parser, inventory/citation/candidate contracts,
module model, orchestrator, extraction agents, or draft-aware gate runner.
The current canonical validator also permits unresolved variable references in
drafts, which is unsuitable for milestone completion.

Pandoc is not currently installed in the development environment. The exact
Pandoc version and installation method must therefore be approved and enforced
locally and in CI before parser implementation. The roadmap marks schema
approval complete and a strategy record states that approval occurred on
2026-07-29, but no meeting record or source reference currently provides the
required human-authorized evidence.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Record human-authorized schema approval and clarify that supervised coding agents may modify implementation, tests, configuration, and documentation while generated CVS artifacts remain restricted to `extraction/20_drafts/`. | `AGENTS.md`; brainstorm Phase 0 |
| R2 | Approve the module registry, `basic` versus `tier`, canonical schema/GMD versions, rule priority ownership, effective dates, provenance date semantics, required body sections, and module schema before extraction. | Brainstorm governance risks; current Pydantic models |
| R3 | Lock repository URL, immutable commit SHA, ordered source paths, scope classes, per-file SHA-256 values, parser/normalization versions, governed registries, and output allowlist in a source manifest. | Deterministic Extraction Contract |
| R4 | Resolve source only from a verified local checkout or immutable approved URL; reject branches, redirects, absent/unexpected files, partial content, and hash mismatches. | G0 Source gate |
| R5 | Parse QMD through a pinned Pandoc JSON AST and fail on truncation or unsupported inventory-bearing constructs. | G1 Parse gate |
| R6 | Reconcile summary-table and subsection signals, preserve exact spellings, deduplicate repeated canonical outputs, and freeze chapter 2-7 inventory plus chapter 8/helper/dependency exclusions. | Inventory Method; G2 gate |
| R7 | Represent every claim with byte-verifiable evidence spans and reject invalid locators, hashes, authority, or claim entailment. | Provenance and Citations; G4 gate |
| R8 | Provide strict models for manifests, modules, inventory, evidence, nullable candidates, issues, run state, gate results, and reports without weakening canonical schemas. | Validator responsibilities |
| R9 | Classify every current canonical variable, rule, and parameter field as source-explicit, deterministically derived, governed constant, agent interpreted, generated metadata, or unresolved. | Structural Field Classification |
| R10 | Emit canonical-shaped Markdown only when every required field, body section, citation, reference, and governance value passes; otherwise preserve a candidate and blocking issue. | G3-G8 gates |
| R11 | Use a deterministic state machine, transactional allowlisted writer, stable IDs, lineage checks, and idempotent resume; run G3-G9 after each item before scheduling the next. | Python Orchestration; G9 gate |
| R12 | Constrain one extractor and one adversarial evidence critic to bounded packets and schema-constrained returns; neither may browse, choose scope, or write files. | Agent decisions |
| R13 | Encode and validate the guideline's explicit non-null weight invariant without claiming to inspect survey observations. | Essential rules; brainstorm requirements |
| R14 | Pilot IDN and GEO through G0-G10, including identical-input replay, before controlled DEM, DWL, UTL, and LBR waves with human checkpoints. | Practical Implementation Phases |
| R15 | Prove final completeness: every locked item is emitted or blocked with owner/disposition, with zero welfare leakage, invalid citations, uncited claims, unresolved final references, cycles, or duplicate IDs. | Ready for Bulk Extraction; Phase 5 |
| R16 | Keep content artifacts byte-stable and place timestamps, durations, environment facts, and other volatile execution data in a separate run ledger. | Deterministic outputs |
| R17 | Keep unit tests network-independent after fixture setup and integrate the extraction checks into the existing Python 3.11 CI workflow. | Acceptance criteria; existing CI |

## Implementation Steps

## Phase 1: Governance and Locked Inputs

### 1. Clear the governance preflight

- **Requirements**: R1, R2, R9, R13
- **Files**: `AGENTS.md` (human-authorized clarification),
  `governance/decisions/Extraction-Preflight-2026-08.md` (human-owned decision
  record), `extraction/config/extraction-governance.v1.yaml`,
  `schema/variable.py`, `schema/rule.py`, `schema/parameter.py`,
  `schema/module.py`
- **Details**:
  - Require a locatable source reference for the 2026-07-29 schema approval;
    the roadmap status and strategy summary are not sufficient alone.
  - Obtain explicit human authorization before changing `AGENTS.md`. Clarify
    that generated CVS content starts in `extraction/20_drafts/`, while
    supervised implementation work may touch approved code, tests, config,
    workflows, and docs.
  - Record the canonical module mapping for IDN, GEO, DEM, LBR (including the
    `chapter5-LMR.qmd` source alias), UTL, and DWL; resolve Education and
    Disability rows embedded in DEM. Note in the module registry that `IDN`
    and `GEO` are *module* codes (identification, geography), not ISO 3166-1
    alpha-3 country codes, to disambiguate from `country-parameters/countries/IDN/`
    (Indonesia) (addresses review finding P3.1).
  - Decide whether `basic` is canonical, inventory-only, or excluded; approve
    schema/GMD versions, rule priorities, authority/effective dates, body
    section contracts, module fields, and the stable meaning of
    `provenance.extracted_on`.
  - Approve the field-classification matrix required by R9 here, not in
    Phase 3. Attach the baseline classification table (every current canonical
    variable, rule, and parameter field mapped to one of: source-explicit,
    deterministically derived, governed constant, agent interpreted, generated
    metadata, unresolved) as a Phase 1 deliverable. Phase 3 Step 6 only
    *encodes* the approved table into `field-classification.v1.yaml` and
    validates against it; it does not invent or revise classifications
    (addresses review finding P2.5).
  - Define the welfare vs. in-scope UTL expenditure boundary with examples:
    which expenditure mentions inside chapters 2-7 are in-scope UTL outputs
    versus referenced chapter 8 welfare outputs. Record the rule in the
    exclusion-ledger contract so Step 5 can classify each expenditure mention
    deterministically rather than by agent judgment (addresses review finding
    P2.4).
  - Make the non-null weight rule explicit in the extraction rubric and
    validator contract. It is a sourced invariant, not a runtime survey-data
    assertion.
  - Modify existing canonical models only where a recorded governance decision
    requires it; do not loosen `extra="forbid"`, identifier validation, or
    graph checks.
- **Test Scenarios**: approved preflight loads; unknown module/basic policy is
  rejected; absent approval reference blocks all later commands.
- **Tests**: `python3 -m pytest tests/extraction/test_governance.py -v`
- **Acceptance criteria**: every governed value required by the first pilot is
  explicit, cited to an approval record, and validated; no implementation
  phase can run while the preflight is incomplete.

### 2. Pin the source and parser contracts

- **Requirements**: R2, R3, R5, R16, R17
- **Files**: `extraction/config/source-manifest.v1.yaml`, `requirements.txt`,
  `.github/workflows/validate.yml`, `README.md`
- **Details**:
  - Resolve and approve a fresh immutable GMD-guidelines commit. Populate the
    exact ordered chapter and supporting-annex paths from that commit and
    classify each as `included`, `supporting`, or `welfare-excluded`.
  - `requirements.txt` is listed because the pinned Pandoc version and any
    new Python dependency required for AST normalization or JSON-schema
    validation must be recorded here. If no Python package is added (Pandoc is
    an external executable and JSON parsing uses the stdlib), state that
    explicitly and keep the file only for the Pandoc version pin note
    (addresses review finding P3.2).
  - Record SHA-256 for every source file, governed module and version values,
    parser/normalization contract versions, approved URL origins, and the
    resolved output-root allowlist.
  - Select one exact Pandoc release and one reproducible installation method
    for local macOS and Ubuntu CI. The preflight must compare the executable's
    full version to the manifest and fail on absence or mismatch.
  - Add a CI step that regenerates the Pandoc AST from the pinned QMD fixtures
    and diffs it against the committed gold JSON. Same-version Pandoc can emit
    subtly different JSON across platforms (table column defaults, attribute
    ordering, wrapper differences); if divergence is observed, either commit
    platform-specific gold or normalize the AST deterministically before
    locator extraction and pin the normalizer version (addresses review
    finding P2.2).
  - Decide and record the agent provider/model/config version used for
    extraction. Replayed reviewed agent responses remain valid only for the
    exact contract lineage recorded in the run manifest.
  - Keep volatile execution metadata out of both identifiers. Define two
    separate identifiers:
    - `execution-id` (created at run start) is a deterministic digest of
      source manifest, governance contract, parser/normalizer versions, and
      prompt/skill bytes only. It is the resume/persistence key for
      intermediate state and the run ledger; it is known before any agent
      runs.
    - `content-run-id` (computed at finalization) extends the `execution-id`
      digest with the hashes of all accepted structured agent outputs. It is
      written into `run-manifest.json` at finalization as the content-lineage
      digest and is the replay-comparison key for byte-identical output.
    - Resume is always keyed by `execution-id`. A crashed run therefore always
      has a resumable directory regardless of agent-output availability
      (addresses review finding P1.1).
- **Test Scenarios**: exact source/parser contract passes; branch name or wrong
  Pandoc version fails; source-path reordering changes the manifest digest.
- **Tests**: `python3 -m pytest tests/extraction/test_manifest.py tests/extraction/test_preflight.py -v`
- **Acceptance criteria**: a clean checkout can install the pinned dependencies
  and produce the same manifest digest locally and in CI without network use in
  unit tests.

## Phase 2: Complete Source-Derived Inventory

### 3. Implement manifest models and verified source resolution

- **Requirements**: R3, R4, R8, R16
- **Files**: `schema/extraction/manifest.py`,
  `extraction_pipeline/source.py`, `extraction_pipeline/hashing.py`,
  `tests/extraction/test_manifest.py`, `tests/extraction/test_source.py`,
  `tests/extraction/fixtures/source-repository/`
- **Details**:
  - Model repository identity, immutable SHA, ordered files, scope status,
    hashes, tool contracts, registries, origins, and write allowlists with
    Pydantic `extra="forbid"` models.
  - Resolve a local checkout by commit-object bytes, not working-tree state.
    For remote fallback, disable automatic redirects, allow only approved HTTPS
    origins, cap response size, stream to a temporary file, verify SHA-256, and
    atomically promote only a complete download.
  - Reject symbolic revisions, duplicate or unexpected paths, missing annexes,
    unapproved redirects/origins, and any byte mismatch before parsing.
  - Emit `resolved-source.json` with deterministic source facts; send download
    timing and environment diagnostics only to the separate run ledger.
- **Test Scenarios**: local pinned commit and immutable URL resolve to the same
  bytes; sibling-path escape and redirect are rejected; truncated content and
  hash mismatch are run-fatal.
- **Tests**: `python3 -m pytest tests/extraction/test_manifest.py tests/extraction/test_source.py -v`
- **Acceptance criteria**: G0 succeeds only for a complete, approved, byte-exact
  source set and never leaves partial output.

### 4. Parse QMD into stable, located AST nodes

- **Requirements**: R5, R7, R17
- **Files**: `extraction_pipeline/pandoc_ast.py`,
  `schema/extraction/evidence.py`, `tests/extraction/test_pandoc_ast.py`,
  `tests/extraction/fixtures/qmd/`
- **Details**:
  - Invoke the exact Pandoc executable with explicit reader/writer arguments
    and parse JSON through structured APIs. Preserve headings, pipe/grid table
    cells, attributes, code blocks, notes, cross-references, and source order.
  - Assign deterministic node IDs from source path, AST position, node type,
    and normalized anchor. Recover one-based line bounds by matching exact
    excerpts against pinned bytes; reject ambiguous or missing matches.
  - Mark inventory-bearing regions and fail G1 if Pandoc drops, merges, or
    represents one through an unsupported construct.
  - Build gold fixtures for a normal table/heading match, grid table, repeated
    variable, spelling mismatch, helper exclusion, CONS exclusion, annex
    citation, and missing-evidence case.
- **Test Scenarios**: pipe and grid tables preserve cells/locators; duplicate
  excerpts remain distinguishable; malformed QMD or unsupported inventory
  region is run-fatal.
- **Tests**: `python3 -m pytest tests/extraction/test_pandoc_ast.py -v`
- **Acceptance criteria**: every gold AST node has a stable ID, exact excerpt,
  line bounds, anchor, and excerpt hash under repeated parsing.

### 5. Reconcile and freeze the inventory denominator

- **Requirements**: R6, R8, R15, R16
- **Files**: `schema/extraction/inventory.py`,
  `extraction_pipeline/inventory.py`,
  `extraction/config/name-normalization.v1.yaml`,
  `tests/extraction/test_inventory.py`, `tests/extraction/gold/inventory.v1.yaml`
- **Details**:
  - Collect table rows and explicit variable subsections independently. Apply
    only versioned normalization rules while preserving each original spelling
    and occurrence.
  - Reconcile names, labels, tiers, module assignments, and source order.
    Orphan signals, conflicting labels/tiers, malformed names, duplicate rows,
    and probable aliases are blocking issues, never silent preferences.
  - Deduplicate repeated canonical identifiers while retaining all occurrences.
    Record helper/intermediate fields, dependencies, welfare references,
    supporting annex concepts, and every chapter 8 output in the exclusion
    ledger with reason and citation.
  - Compare source-derived results to the human-reviewed gold sample and
    approved module/table counts. The gold sample detects parser regressions;
    it never supplies missing source facts.
  - The human-reviewed gold inventory sample (`gold/inventory.v1.yaml`) and
    approved module/table counts are non-trivial human-authored inputs on the
    Phase 2 critical path. List them as explicit Phase 1/2 human deliverables
    with an owner and a checkpoint before inventory freeze (addresses review
    finding P3.3).
  - Freeze the denominator only after all G2 blocking issues have an approved
    disposition. Version any later source delta as a new inventory.
- **Test Scenarios**: matching dual signals emit one item; repeated ID retains
  all occurrences; table-only, heading-only, alias, tier conflict, and welfare
  leakage block inventory completion.
- **Tests**: `python3 -m pytest tests/extraction/test_inventory.py -v`
- **Acceptance criteria**: chapters 2-7 have one complete frozen canonical
  inventory and chapter 8/helpers have one complete cited exclusion ledger,
  with approved counts by module and signal source.

## Phase 3: Extraction and Evidence Contracts

### 6. Add strict contracts and the field-classification matrix

- **Requirements**: R7, R8, R9, R10, R13, R16
- **Files**: `schema/extraction/evidence.py`,
  `schema/extraction/candidate.py`, `schema/extraction/issues.py`,
  `schema/extraction/run.py`, `schema/module.py`,
  `extraction/config/field-classification.v1.yaml`,
  `tests/extraction/test_contracts.py`
- **Details**:
  - Add strict models for citations, claim-evidence links, nullable field
    candidates, issues, modules, state transitions, gate results, content run
    manifests, validation/completeness reports, and volatile run-ledger events.
  - Require each candidate field to carry its structural class, value or null,
    evidence IDs where applicable, confidence for interpreted fields, critic
    disposition, and blocking issue IDs.
  - Treat the following as the baseline classification. This table is the
    Phase 1 governance deliverable (R2/R9) referenced in Step 1; Step 6 only
    encodes it into `field-classification.v1.yaml` and validates against it.
    Phase 1 governance may change a classification only through an explicit
    recorded decision.

| Canonical model | Field | Classification |
|---|---|---|
| VariableDefinition | `variable_id` | deterministically derived |
| VariableDefinition | `canonical_label`, `variable_name`, `tier` | source-explicit |
| VariableDefinition | `module_id`, `gmd_version`, `schema_version`, `status` | governed constant |
| VariableDefinition | `unit_of_analysis`, `mapping_role`, `data_type` | agent interpreted |
| VariableDefinition | `value_codes`, `allowed_range`, `missing_codes`, `external_standards` | source-explicit |
| VariableDefinition | `derived_from`, `derives_to`, `country_parameters`, `prerequisites`, `rules`, `exceptions`, `source_hints` | agent interpreted |
| ValueCode | `value`, `label` | source-explicit |
| AllowedRange | `min`, `max` | source-explicit |
| MissingCode | `code`, `label` | source-explicit |
| Prerequisite | `variable_id`, `condition` | agent interpreted |
| ExternalStandard | `name`, `url` | source-explicit |
| SourceHints | `question_keywords`, `typical_section_names` | agent interpreted |
| VariableProvenance | `source_document`, `source_section` | deterministically derived from validated citations |
| VariableProvenance | `extraction_method`, `extracted_on` | generated metadata; stable canonical semantics require the Phase 1 decision |
| VariableProvenance | `human_reviewed`, `reviewer` | governed constant (`false`, `null`) for drafts |
| VariableProvenance | `notes` | agent interpreted or unresolved |
| RuleDefinition | `rule_id` | deterministically derived |
| RuleDefinition | `rule_name`, `applies_to_variables` | agent interpreted |
| RuleDefinition | `scope`, `module_id`, `priority`, `version`, `status`, `authority`, `effective_from`, `effective_to` | governed constant |
| ParameterDefinition | `parameter_id` | deterministically derived |
| ParameterDefinition | `parameter_name` | source-explicit when directly named; otherwise unresolved |
| ParameterDefinition | `module_id`, `schema_version`, `status`, `authority`, `fallback_policy`, `global_default` | governed constant |
| ParameterDefinition | `kind`, `value_type`, `value_schema`, `applies_to_variables` | agent interpreted |
| ParameterProvenance | `source_document` | deterministically derived from validated citations |
| ParameterProvenance | `extraction_method`, `extracted_on` | generated metadata; stable canonical semantics require the Phase 1 decision |
| ParameterProvenance | `human_reviewed`, `reviewer` | governed constant (`false`, `null`) for drafts |
| ParameterProvenance | `notes` | agent interpreted or unresolved |

- **Test Scenarios**: all current canonical fields occur exactly once in the
  classification matrix; unknown/duplicate fields fail; null candidate values
  create issues and cannot cross the canonical gate.
- **Tests**: `python3 -m pytest tests/extraction/test_contracts.py tests/extraction/test_field_classification.py -v`
- **Acceptance criteria**: schema introspection proves complete field coverage,
  and candidate models can represent missing evidence without making canonical
  models nullable.

### 7. Validate citations, claims, and canonical Markdown

- **Requirements**: R7, R10, R13, R15
- **Files**: `extraction_pipeline/evidence.py`,
  `extraction_pipeline/canonicalize.py`,
  `extraction_pipeline/validators.py`,
  `tests/extraction/test_evidence.py`,
  `tests/extraction/test_canonicalize.py`
- **Details**:
  - Re-read pinned bytes for every citation and verify source identity, path,
    node ID, heading anchor, one-based lines, exact excerpt, excerpt SHA-256,
    evidence role, extraction method, and transform/agent version.
  - Require every non-generated field and every factual body claim to link to
    evidence. Keep deterministic byte checks separate from critic/human
    entailment dispositions and report which layer made each finding.
  - Define stable file names, YAML ordering, serialization, body sections,
    rule splitting, module layout, identifier allocation, lineage, and
    overwrite policy. Canonicalization must reject unresolved values rather
    than omit keys or invent prose.
  - Validate the explicit non-null weight instruction as a cited prohibition in
    applicable canon; do not report that survey weights themselves were tested.
  - Validate staged drafts only. Never merge staged IDs into the approved canon
    registry or load staged content as effective harmonization rules.
- **Test Scenarios**: exact citation and supported claim pass; shifted lines,
  altered excerpt, excluded authority, uncited prose claim, invented rule, and
  missing body section fail.
- **Tests**: `python3 -m pytest tests/extraction/test_evidence.py tests/extraction/test_canonicalize.py -v`
- **Acceptance criteria**: G4-G8 deterministically prevent canonical emission
  for any invalid citation, unsupported claim, missing field/section, or
  governance block.

### 8. Build contract fixtures and compatibility checks

- **Requirements**: R8, R10, R15, R17
- **Files**: `tests/extraction/fixtures/contracts/`,
  `tests/extraction/test_contract_fixtures.py`,
  `tests/extraction/test_canonical_compatibility.py`
- **Details**:
  - Add simple atomic, derived, country-parameter declaration,
    contradictory-source, missing-evidence, invalid-citation, and
    null-weight-prohibition candidates.
  - Verify eligible outputs against the existing `VariableDefinition`,
    `RuleDefinition`, and `ParameterDefinition` models plus the new module
    model and body contract.
  - Verify final graph rules independently: all targets exist in the frozen
    inventory, required reciprocal relationships agree, IDs are unique, and
    cycles/out-of-scope canonical dependencies fail.
- **Test Scenarios**: each fixture reaches its expected state and gate; a model
  change that omits classification or compatibility coverage fails tests.
- **Tests**: `python3 -m pytest tests/extraction/test_contract_fixtures.py tests/extraction/test_canonical_compatibility.py -v`
- **Acceptance criteria**: fixtures cover every candidate outcome and prove the
  extraction contract remains a strict precursor to, not a replacement for,
  canonical validation.

## Phase 4: Orchestration, Agents, and Pilot

### 9. Implement the state machine and transactional writer

- **Requirements**: R10, R11, R16, R17
- **Files**: `extraction_pipeline/orchestrator.py`,
  `extraction_pipeline/state.py`, `extraction_pipeline/writers.py`,
  `extraction_pipeline/cli.py`, `tests/extraction/test_state.py`,
  `tests/extraction/test_writers.py`, `tests/extraction/test_resume.py`
- **Details**:
  - Implement explicit transitions from inventory item to evidence packet,
    candidate, critic result, gate results, canonical set or blocked issue.
    Persist G3-G9 atomically after every attempt before selecting another item.
  - Key all intermediate persisted state and the run ledger by `execution-id`
    (known at run start), not `content-run-id` (known only at finalization).
    Resume loads `runs/<execution-id>/` state; the final `content-run-id` is
    written into `run-manifest.json` at finalization (addresses review finding
    P1.1).
  - Resolve all targets and use `Path.relative_to()`/`is_relative_to()` for
    containment. Stage complete artifact sets in a temporary sibling and
    atomically rename only after all files validate.
  - Reject overwrite unless content-run lineage and existing hashes match.
    Resume from validated persisted state and reject skipped, reversed, or
    incompatible transitions.
  - Finalize the deterministic output layout:

```text
extraction/20_drafts/runs/<execution-id>/
  resolved-source.json
  run-manifest.json   # includes final content-run-id at finalization
  inventory/non-welfare-inventory.json
  inventory/dependency-exclusion-ledger.json
  evidence/<inventory-id>.json
  candidates/<inventory-id>.json
  issues/<issue-id>.json
  canonical/variables/<module>/<variable-id>.md
  canonical/rules/<module>/<rule-id>.md
  canonical/parameters/<parameter-id>.md
  canonical/modules/<module-id>.md
  reports/gate-results.json
  reports/completeness.json
  reports/reproducibility.json

extraction/20_drafts/run-ledgers/<execution-id>.jsonl
```

- **Test Scenarios**: complete item commits atomically; crash resumes without
  duplicate work; symlink/sibling traversal and partial-set overwrite fail;
  volatile ledger changes do not alter content hashes.
- **Tests**: `python3 -m pytest tests/extraction/test_state.py tests/extraction/test_writers.py tests/extraction/test_resume.py -v`
- **Acceptance criteria**: no failure can leave a partial content set or write
  outside the allowlist, and repeat execution resumes idempotently.

### 10. Add bounded extractor and critic roles

- **Requirements**: R7, R10, R12, R16
- **Files**: `extraction/agents/extractor.md`,
  `extraction/agents/evidence-critic.md`,
  `extraction/skills/universal-extraction.md`,
  `extraction/skills/modules/{idn,geo}.md`,
  `extraction_pipeline/agents.py`, `tests/extraction/test_agents.py`
- **Details**:
  - Define a provider-neutral typed adapter whose only input is the immutable
    evidence packet, candidate schema, governed constants, and versioned role
    and module instructions. Require schema-constrained JSON output.
  - The extractor copies explicit facts, proposes interpreted fields with
    citations/confidence, and returns null plus a blocking issue when evidence
    is insufficient. It cannot browse, change inventory, or write files.
  - The critic independently challenges every interpreted field, citation
    entailment, omitted prohibition, contradiction, and edge case. It cannot
    repair the candidate silently; it returns findings and dispositions.
  - Author only the universal rubric and the `idn.md` and `geo.md` module
    skills in this step. Defer `dem.md`, `dwl.md`, `utl.md`, and `lbr.md` to
    the start of their corresponding waves (Steps 12-14), after the IDN/GEO
    pilot has stabilized the skill template. This avoids front-loading work
    the pilot is meant to de-risk (addresses review finding P2.1).
  - Define an explicit `agent_output_invalid` transition for malformed JSON,
    schema-invalid output, or valid-but-empty results: zero retries (every
    response is terminal under the replay contract), each raw response is
    hashed into the run ledger, and exhaustion emits a machine-readable
    blocking issue rather than a silent skip (addresses review finding P2.3).
  - Version the universal rubric and the two pilot module skill files. Keep
    extracted facts and run state out of role/skill instructions.
  - Use fake and recorded adapters in tests. Network/model access is confined
    to explicitly requested extraction runs and every accepted response hash is
    part of content lineage.
- **Test Scenarios**: schema-valid supported output passes; browsing/write
  request, unknown field, unsupported filled value, malformed JSON, timeout,
  critic rejection, and `agent_output_invalid` terminal blocking issue all
  become blocking issues.
- **Tests**: `python3 -m pytest tests/extraction/test_agents.py -v`
- **Acceptance criteria**: agents cannot affect scope, files, IDs, or state
  directly, and no interpreted field reaches canonicalization without critic
  review.

### 11. Implement G0-G10 and complete the IDN/GEO pilot

- **Requirements**: R3-R17
- **Files**: `extraction_pipeline/gates.py`,
  `tests/extraction/test_gates.py`, `tests/extraction/test_pilot.py`,
  `extraction/20_drafts/runs/<pilot-execution-id>/`
- **Details**:
  - Implement G0-G2 as run-level prerequisites, G3-G9 per item, and G10 at
    pilot/release checkpoints. Distinguish run-fatal, item-blocking,
    cross-item-pending, and informational results in machine-readable output.
  - Run IDN and GEO first. Exercise repeated identifiers, country-specific
    source mentions represented without country leakage, null-weight
    prohibitions, and final graph resolution.
  - Repeat the pilot from clean temporary state with identical locked source,
    contracts, skills, and accepted agent responses. Compare aggregate counts,
    semantic JSON, and every content byte; ignore only the separate run ledger.
  - Require a human checkpoint on the inventory reconciliation, representative
    candidates, critic findings, and gate reports before Phase 5.
- **Test Scenarios**: successful replay is byte-identical; source mismatch and
  parser truncation stop the run; one missing-evidence item blocks only itself;
  path/reproducibility failures stop the run.
- **Tests**: `python3 -m pytest tests/extraction/test_gates.py tests/extraction/test_pilot.py -v`
- **Acceptance criteria**: IDN/GEO pass all required gates and reproducibility
  checks, every failure has the specified nonzero/blocking outcome, and the
  human checkpoint authorizes controlled waves.

## Phase 5: Controlled Extraction Waves

### 12. Extract and review DEM and DWL

- **Requirements**: R6-R16
- **Files**: `extraction/20_drafts/runs/<execution-id>/`, module-specific
  gold/regression fixtures under `tests/extraction/fixtures/modules/`
- **Details**:
  - Extract DEM after applying the approved Education/Disability module
    decision, then DWL. Author `dem.md` and `dwl.md` module skills at the start
    of this wave using the stabilized pilot template (deferred from Step 10 per
    review finding P2.1). Reconcile each module against its frozen denominator.
  - Validate module graphs, parameter declarations, prohibitions, missing-code
    semantics, critic findings, and all G3-G9 outcomes per item.
  - Stop before the next wave until the module report and representative
    artifacts receive a recorded human checkpoint.
- **Test Scenarios**: normal fields emit; embedded subdomain and cross-module
  references resolve per registry; unsupported parameter/default remains
  blocked.
- **Tests**: `python3 -m pytest tests/extraction -k "dem or dwl or graph" -v`
- **Acceptance criteria**: every DEM/DWL inventory item is emitted or has an
  owned blocking issue, module graphs pass, and the checkpoint is recorded.

### 13. Extract and review UTL

- **Requirements**: R6-R16
- **Files**: `extraction/20_drafts/runs/<execution-id>/`, UTL fixtures under
  `tests/extraction/fixtures/modules/utl/`
- **Details**:
  - Cover access, affordability, and derived expenditure variables without
    treating expenditure references as chapter 8 welfare outputs. Author
    `utl.md` at the start of this wave using the stabilized pilot template
    (deferred from Step 10 per review finding P2.1). Classify each expenditure
    mention using the Phase 1 welfare/UTL boundary rule (P2.4).
  - Validate units, allowed values/ranges, derivation direction, prerequisites,
    and cross-module targets against direct evidence and the frozen inventory.
  - Require the same per-item gates, module report, critic review, and human
    checkpoint before LBR.
- **Test Scenarios**: allowed UTL expenditure emits; CONS output is excluded;
  ambiguous derivation/unit blocks the item.
- **Tests**: `python3 -m pytest tests/extraction -k "utl or welfare or graph" -v`
- **Acceptance criteria**: UTL has complete disposition, zero welfare leakage,
  valid graph edges, and checkpoint approval.

### 14. Extract and review LBR last

- **Requirements**: R6-R16
- **Files**: `extraction/20_drafts/runs/<execution-id>/`, LBR fixtures under
  `tests/extraction/fixtures/modules/lbr/`
- **Details**:
  - Apply the approved LMR/LBR alias and cover repeated-period families, labor
    income outputs, dense derivations, external standards, and all documented
    source inconsistencies. Author `lbr.md` at the start of this wave using the
    stabilized pilot template (deferred from Step 10 per review finding P2.1).
  - Resolve aliases only through approved normalization records with citations;
    never silently repair source spelling or table/heading disagreements.
  - Complete final LBR graph validation and the wave checkpoint.
- **Test Scenarios**: repeated families receive stable unique IDs; labor income
  remains in scope; spelling conflict, unresolved external standard, duplicate
  output, and graph cycle block completion.
- **Tests**: `python3 -m pytest tests/extraction -k "lbr or alias or graph" -v`
- **Acceptance criteria**: every LBR inventory item is emitted or has an owned
  blocking issue, source discrepancies retain evidence/disposition, and the
  final wave checkpoint is recorded.

## Phase 6: Milestone Completion

### 15. Prove completeness, reproducibility, and CI integration

- **Requirements**: R14, R15, R16, R17
- **Files**: `extraction_pipeline/reports.py`,
  `tests/extraction/test_completeness.py`,
  `tests/extraction/test_reproducibility.py`, `.github/workflows/validate.yml`,
  `README.md`, `docs/the-schema.md`,
  `extraction/20_drafts/runs/<execution-id>/reports/`
- **Details**:
  - Produce machine-readable and human-readable reports proving a one-to-one
    disposition for every locked inventory item, with blocker owner and
    disposition where no canonical set exists.
  - Require zero welfare leakage, invalid locators/hashes, uncited
    non-generated claims, unknown final references, cycles, duplicate IDs,
    source-count drift, path violations, partial artifact sets, and
    unclassified canonical fields.
  - Run existing canonical/country validation and bundle smoke tests to prove
    no regression. Add extraction preflight/unit/integration checks to CI with
    network-independent pinned fixtures; keep live-source verification an
    explicit locked-input job or release command.
  - Repeat the full content build from clean state and compare bytes and
    semantic counts. Do not promote any artifact into `knowledge/`.
  - Document manifest updates, local source setup, parser installation, CLI
    commands, gate meanings, issue disposition, replay, and the boundary
    between deterministic and agent-assisted evidence review.
- **Test Scenarios**: complete run passes; one undisposed item, welfare leak,
  uncited claim, unresolved graph target, or byte difference prevents milestone
  completion and returns nonzero.
- **Tests**: `python3 validation/validate_country_layer.py`; `python3 build/compile_bundle.py PER 2019`; `python3 -m pytest tests/ -v`; `python3 -m extraction_pipeline.cli reproduce --manifest extraction/config/source-manifest.v1.yaml --compare <execution-id>`
- **Acceptance criteria**: all required verification evidence is persisted,
  CI-equivalent commands pass, repeated content is byte-identical, and the
  milestone report is ready for human review without promoting drafts.

## Testing Strategy

- Use Pydantic unit tests for every strict contract, forbidden extra field,
  state transition, and canonical compatibility boundary.
- Use small pinned QMD fixtures and a local fixture Git repository for source,
  parser, locator, hash, and inventory tests. No unit test may depend on GitHub
  or a model endpoint.
- Use `tmp_path` for resolver caches, transactional writes, crash injection,
  path escapes, and clean-state replay. Assert both return codes and
  machine-readable issue/gate content.
- Maintain a human-reviewed parser gold set spanning normal, repeated,
  conflicting, helper, welfare-excluded, annex, and missing-evidence cases.
- Use fake and recorded agent adapters to test schema failures, critic
  rejection, replay, and deterministic orchestration.
- Run focused tests after each step, the full extraction suite at each phase,
  existing repository tests after shared-model changes, and a full clean replay
  at pilot and milestone completion.

## Documentation Checklist

- [ ] Human-authorized schema approval and extraction preflight decisions are locatable.
- [ ] `AGENTS.md` clearly separates generated artifact paths from supervised implementation paths.
- [ ] Source manifest fields, source update/delta procedure, and approved origins are documented.
- [ ] Exact Pandoc installation/version checks are documented for macOS and CI.
- [ ] Module registry, normalization rules, field classes, body contracts, and stable ID rules are documented.
- [ ] Candidate, issue, gate, report, state, and output-layout schemas are documented for later review-app consumers.
- [ ] CLI usage, resume/replay, live-source verification, and failure exit codes are documented.
- [ ] Deterministic checks are distinguished from agent-assisted entailment and human approval.
- [ ] No documentation implies that extraction validates raw survey observations or promotes staged drafts.

## Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Approval or governance decisions remain unlocatable | Implementation invents required canonical values | Make Phase 1 a hard preflight with human-owned evidence and nonzero failure |
| Pandoc absence/version drift changes AST output | Inventory and citation locators become irreproducible | Pin one exact release, verify it before parsing, and test gold AST fixtures in CI |
| QMD tables/headings disagree | Silent output loss or incorrect normalization | Collect signals independently and block every orphan/conflict until disposition |
| Remote source changes or redirects | Wrong authority bytes enter extraction | Resolve immutable commit bytes, reject redirects/origins, and verify every hash |
| Agent output varies or invents values | Unsupported canon or false reproducibility | Constrain schemas/packets, require critic review, hash accepted responses, and support replay |
| Current provenance dates are volatile | Identical runs produce false diffs | Resolve stable canonical semantics in Phase 1 and keep runtime timing in a separate ledger |
| Staged IDs contaminate approved canon | Drafts become effective prematurely | Use draft-aware validators and never load staged output as approved registry content |
| Path traversal, symlinks, or crashes escape staging | Protected artifacts change or partial sets remain | Resolve/contain every path and atomically promote complete validated sets only |
| LBR graph and repeated families expose late contract gaps | Large rework near completion | Freeze shared contracts through IDN/GEO, process LBR last, and pause for wave checkpoints |
| Full extraction exceeds review capacity | Low-confidence bulk drafts accumulate | Require module-level reports and human authorization before each next wave |

## Out of Scope

- Designing or implementing the Shiny review application.
- Populating or redesigning the Country Parameter Layer.
- Promoting drafts into `extraction/30_review/`, `extraction/40_approved/`,
  `knowledge/`, or `country-parameters/`.
- Editing or correcting the upstream GMD guideline source.
- Inspecting raw survey observations or claiming runtime validation of their
  values or weights.
- Adding more agent roles before pilot error evidence justifies specialization.
- Treating supporting annexes as independent canonical variable inventories.

## Completion Contract

### Outcome

A reproducible, evidence-first compiler inventories every canonical
non-welfare output in guideline chapters 2-7, records helpers/dependencies and
chapter 8 outputs separately, and emits only fully supported CVS drafts under
`extraction/20_drafts/`. Every locked item ends with either a gate-passing
draft set or a machine-readable blocking issue, with citations validated
against pinned source bytes.

### Verification Surface

| ID | Phase | Evidence Required | Command/Artifact | Required |
|----|-------|-------------------|------------------|----------|
| V1 | 1 | Human-authorized schema approval record, write-policy clarification, module registry, field-governance decisions, source revision, and exact Pandoc contract are recorded | Governance records plus preflight validator | yes |
| V2 | 2 | Manifest hashes resolve; AST parsing and dual-signal reconciliation produce frozen in-scope inventory and complete exclusion ledger | Inventory reports and focused pytest suite | yes |
| V3 | 3 | All variable/rule/parameter fields are classified; citation, candidate, issue, run-state, module, and report contracts reject unresolved or unsupported canonical emission | Contract matrix, fixtures, schema tests | yes |
| V4 | 4 | Orchestrator, safe writes, state machine, extractor/critic adapters, and G0-G10 gates pass IDN/GEO pilots and identical-input replay | Pilot reports, full gate tests, byte comparison | yes |
| V5 | 5 | DEM, DWL, UTL, and LBR waves reconcile inventory, pass graph/critic checks, and receive required human checkpoints | Module manifests and checkpoint records | yes |
| V6 | 6 | Every locked item is emitted or blocked with owner/disposition; zero welfare leakage, invalid citations, unknown references, and uncited claims | Milestone completeness report and full pytest/validator run | yes |
| V7 | final | Clean CI-equivalent run and repeated build produce identical content artifacts under locked inputs | Validation workflow commands and reproducibility report | yes |

### Constraints

| ID | Phase | Constraint | Check |
|----|-------|------------|-------|
| C1 | all | Pinned GMD guideline bytes are the sole authority for extracted facts | Manifest/citation hash validation |
| C2 | all | Generated CVS content is written only under `extraction/20_drafts/`; protected review, approved, knowledge, and country paths remain human-owned | Resolved-path allowlist tests |
| C3 | 1-6 | No unresolved governance value or missing evidence is converted into a default | Candidate-to-canonical gate tests |
| C4 | 2-6 | Chapter 8 CONS never enters canonical inventory or drafts | Scope and leakage tests |
| C5 | 2-6 | Content outputs are byte-stable; timestamps, durations, and environment facts stay in a separate run ledger | Identical-input replay |
| C6 | 3-6 | Existing strict canonical and country-layer invariants are preserved, including null-weight prohibitions and final graph integrity | Existing plus extraction validator suites |
| C7 | 4-6 | Writes are transactional, lineage-aware, and contained using resolved paths | Failure-injection and path-escape tests |
| C8 | 4-6 | Each item passes G3-G9 before another item is scheduled; run-fatal failures stop immediately | State-machine transition tests |

### Boundaries

- Allowed: supervised Python schemas/orchestration/validators, extraction
  agents and skills, fixtures/tests, dependency and CI updates, documentation,
  and generated artifacts under `extraction/20_drafts/`.
- Allowed only after human authorization is recorded: governance changes
  needed to clarify `AGENTS.md` and approve schema/module/default decisions.
- Out of scope: Shiny review application, Country Parameter Layer
  population/design, promotion into `knowledge/`, changes to source guidelines,
  and extra agent roles without measured pilot evidence.

### Iteration Policy

1. Execute phases sequentially and satisfy each phase's required evidence
   before advancing.
2. Under `ask`, pause before changing scope, contracts, dependencies, source
   revision, module taxonomy, governed constants, or output locations.
3. Repair local gate failures and rerun the same focused check before widening
   scope.
4. Preserve item-blocking failures as candidates/issues; stop on run-fatal
   integrity, parser, path, or reproducibility failures.
5. Require the planned human checkpoint before each extraction wave; source
   changes create a new manifest version and delta inventory.

### Blocked-Stop Conditions

- Required approval evidence or Phase 1 governance decisions are absent.
- The pinned source is unavailable, incomplete, redirected unexpectedly, or
  hash-mismatched.
- The approved Pandoc version is unavailable or an inventory-bearing construct
  cannot be parsed completely.
- Continuing would write outside an allowed path or alter a human-owned
  artifact without approval.
- A required canonical field is unsupported, a required citation fails, or a
  cross-item reference cannot resolve by module completion.
- Identical locked inputs produce a semantic or byte difference.
- Any required verification cannot be executed or remains failed after focused
  recovery.

## Revision Log

### 2026-08-03 — Plan review revisions (`/cg-plan-review`)

All nine findings from `@cg-plan-critic` were addressed inline. Summary:

| ID | Priority | Finding | Resolution location |
|----|----------|---------|---------------------|
| P1.1 | P1 | `content-run-id` self-referential resume target | Step 2 (two-identifier definition), Step 9 (resume keyed by `execution-id`), output layout, Step 11/15 path references |
| P2.1 | P2 | Six module skill files authored before pilot evidence | Step 10 (author only `idn.md`/`geo.md`), Steps 12-14 (deferred skill authoring per wave) |
| P2.2 | P2 | Pandoc AST cross-platform stability unaddressed | Step 2 (CI AST-regeneration diff step, deterministic normalization) |
| P2.3 | P2 | No recovery policy for malformed/invalid agent output | Step 10 (`agent_output_invalid` transition, zero retries, blocking issue) |
| P2.4 | P2 | Welfare vs. in-scope UTL expenditure boundary unspecified | Step 1 (Phase 1 governance decision with examples), Step 13 (classification by rule) |
| P2.5 | P2 | Field-classification matrix under-scoped | Step 1 (R9 approval moved to Phase 1 with baseline table), Step 6 (encodes approved table only) |
| P3.1 | P3 | `IDN`/`GEO` dual meaning (module vs. country) | Step 1 (module-registry disambiguation note) |
| P3.2 | P3 | `requirements.txt` listed but no new Python dependency identified | Step 2 (clarification: Pandoc version pin and any normalization/validation package) |
| P3.3 | P3 | Gold inventory sample not accounted as a deliverable | Step 5 (explicit Phase 1/2 human deliverable with owner and checkpoint) |