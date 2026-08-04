---
date: 2026-08-03
title: "Extract the Universal Non-Welfare Schema"
status: decided
scope: "Deep"
chosen-approach: "Evidence-first corpus compiler"
tags: [extraction, non-welfare, provenance, validation, agents, python]
---
<!-- Valid status values: decided, in-progress, abandoned -->

# Extract the Universal Non-Welfare Schema

## Context

The roadmap milestone must convert every non-welfare output defined by the GMD
harmonization guidelines into structured, cited CVS drafts. The work is one
cross-cutting software/data effort rather than separate feature brainstorms.

The authoritative source is `GMD-hub/GMD-guidelines`. During this brainstorm,
its `main` branch resolved to commit
`d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`. That revision contains QMD module
chapters for IDN, GEO, DEM, LMR/LBR, UTL, DWL, and CONS. The source is not
perfectly regular: variable headings and summary tables can disagree in
spelling or formatting. The pipeline must detect these discrepancies instead
of selecting one representation silently.

The repository already has strict Pydantic models for variables, rules,
parameters, and country records; a Markdown front-matter loader; canonical
validation; a bundle compiler; and pytest coverage for the current country
layer. It does not yet have extraction agents, a source manifest, an inventory
model, a candidate model, draft-aware validators, or extraction tests.

## Requirements

- Treat the pinned GMD guideline content as the sole authority for extracted
  harmonization facts.
- Inventory canonical GMD outputs as the primary units. Record helper fields,
  intermediate concepts, repeated cross-module occurrences, and welfare
  references in a dependency/exclusion ledger rather than as equal artifacts.
- Exclude all outputs in chapter 8, CONS. Keep outputs from chapters 2 through
  7 in scope, including LBR income and UTL expenditure variables.
- Include referenced annexes as supporting evidence inputs, not as independent
  variable inventories.
- Require every generated CVS artifact to begin in `extraction/20_drafts/`.
  Human review and promotion may later move approved content to its governed
  destination. Extraction agents must never write to `knowledge/`, review, or
  approved staging.
- Allow supervised implementation work on Python orchestration, schemas,
  validators, tests, and documentation outside `extraction/20_drafts/`. Clarify
  the conflicting wording in `AGENTS.md` before implementation.
- Reuse Python 3.10+, Pydantic 2, PyYAML, pytest, the existing canonical
  schemas, the front-matter loader, validator patterns, and build conventions.
- Use a structured QMD parser. Pandoc JSON AST is the preferred basis because
  the source contains both pipe and grid tables, Quarto attributes, code
  blocks, footnotes, and cross-references.
- Fail loudly for unavailable or changed source bytes, missing artifacts,
  unsupported assumptions, unresolved required fields, invalid citations,
  welfare leakage, invalid references, and writes outside permitted paths.
- Preserve the existing rule that missing survey data and null weights cannot
  be silently repaired. This extraction repository cannot inspect raw survey
  observations, so it must encode and validate the non-null weight invariant in
  the extracted canon rather than claim to test survey values.
- Do not design the Shiny review application or Country Parameter Layer. Define
  only stable output and issue interfaces that those systems can consume later.

## Decisions From Clarification

1. The inventory contains canonical outputs plus a separate dependency and
   exclusion ledger.
2. Chapter 8, CONS, is the deterministic welfare exclusion boundary.
3. Source input uses a manifest plus a verified resolver. The resolver may use
   a local checkout or immutable raw URLs, but source hashes must match.
4. Missing evidence is represented in a nullable extraction candidate and an
   issue record. A strict canonical-shaped artifact is emitted only when all
   required fields pass validation.
5. Python owns source resolution, parsing, orchestration, state transitions,
   validation, and filesystem writes.
6. Agent specialization is hybrid: reusable role agents consume bounded
   evidence packets, while module skills capture source conventions and edge
   cases.
7. The initial agent set stays small: one extractor and one adversarial
   evidence reviewer. Additional agents require measured error evidence.

## Structural Field Classification

Every candidate field must be assigned one of these classes in the extraction
contract:

| Class | Examples | Rule |
|---|---|---|
| Source-explicit | variable name, label, tier, value codes, stated unit | Copy from cited evidence without reinterpretation. |
| Deterministically derived | `VAR-` ID, source order, normalized chapter path | Compute by a versioned Python rule and retain input citations. |
| Governed constant | schema version, GMD version, draft status, authority | Read from approved configuration; never infer from prose. |
| Agent interpreted | mapping role, derivation relation, prerequisite, rule candidate, normalized data type | Require direct citations, confidence, and critic review. |
| Generated metadata | run ID, tool versions, source-manifest hash, extraction method | Produce in the orchestration layer and keep volatile run metadata separate from content. |
| Unresolved | any required value lacking sufficient evidence | Store `null` only in the candidate, create a blocking issue, and do not emit a canonical artifact. |

The plan must map every current `VariableDefinition`, `RuleDefinition`, and
`ParameterDefinition` field to one class. Fields that lack an approved source,
such as rule priority, cannot be invented merely to satisfy Pydantic.

## Deterministic Extraction Contract

### Inputs

The source manifest must contain:

- source repository URL and immutable commit SHA;
- ordered chapter and annex paths;
- scope status for each path: included, supporting, or welfare-excluded;
- SHA-256 for every source file;
- parser and normalization contract versions;
- governed module registry and GMD/schema versions;
- approved output-root allowlist.

The resolver may read a local guidelines checkout or fetch immutable raw
content. It must reject branch names, hash mismatches, absent files, unexpected
files, redirects to unapproved origins, and partial downloads.

### Inventory Method

1. Parse every manifest file into a structured AST.
2. Collect variable candidates independently from module summary-table rows and
   explicit variable subsections.
3. Normalize names only through versioned, testable rules. Preserve the exact
   source spelling in evidence.
4. Reconcile the two signal sets. A name present in only one set, conflicting
   labels or tiers, malformed names, duplicate rows, and likely spelling
   variants are blocking inventory issues until resolved.
5. Deduplicate repeated ID variables into one canonical output while retaining
   every source occurrence.
6. Record helper placeholders and all chapter 8 outputs in the exclusion
   ledger with a reason and citation.
7. Compare the result with a small human-reviewed gold set and with expected
   module/table counts. The gold set tests the parser; it does not replace the
   source-derived inventory.

### Outputs

Logical outputs, with exact paths to be finalized by `/cg-plan`, are:

- source manifest and resolved-source report;
- normalized non-welfare inventory;
- dependency/exclusion ledger;
- one immutable evidence packet per inventory item;
- one nullable extraction candidate per attempted item;
- one machine-readable issue record per failure or governance block;
- strict variable, rule, parameter, and module Markdown drafts when eligible;
- run manifest containing versions, hashes, states, and aggregate counts;
- validation and completeness reports.

Content artifacts must be byte-stable for the same source manifest, contract,
and agent outputs. Timestamps, durations, and environment diagnostics belong in
a separate run ledger so they do not create false content diffs.

### Provenance and Citations

Every non-generated claim must cite one or more evidence spans containing:

- source repository and commit SHA;
- source path;
- AST node ID and nearest stable heading anchor;
- one-based start and end lines in the pinned source;
- exact excerpt and SHA-256 of that excerpt;
- evidence role, such as definition, allowed codes, derivation, prohibition,
  consistency check, or source conflict;
- extraction method and the versioned transform or agent configuration used.

The citation validator must re-read the pinned bytes, verify line bounds and
excerpt hashes, and reject citations that do not entail the associated claim.
Entailment review may be agent-assisted, but byte and locator checks are
deterministic Python checks.

## Responsibility Division

### Python Orchestration

- Resolve and hash source inputs.
- Parse QMD through the structured parser.
- Build and reconcile inventory signals.
- Create bounded evidence packets.
- Select the next state using an explicit state machine.
- Invoke agents with schemas and token-bounded evidence only.
- Validate returned structured data before accepting it.
- Assign stable IDs and detect duplicates.
- Write all files transactionally through an allowlisted path service.
- Resume idempotently from the run ledger.
- Produce completeness, failure, and reproducibility reports.

### Agents

- The extractor maps an evidence packet into the candidate schema. It may not
  browse, fetch additional sources, mutate files, choose scope, or fill an
  unsupported required field.
- The critic tries to disprove each interpreted field, checks citation
  entailment, finds omitted prohibitions and edge cases, and identifies source
  contradictions.
- Both agents return schema-constrained data to Python. They never write
  repository files directly.

### Skills

- Define the universal extraction rubric and prohibited assumptions.
- Define module-specific vocabulary, table patterns, known source anomalies,
  and interpretation checks for IDN, GEO, DEM, LBR, UTL, and DWL.
- Define citation, missing-evidence, rule-splitting, and provenance standards.
- Remain versioned instructions, not stores for run state or extracted facts.

### Validators

- Reuse canonical Pydantic models at the canonical-artifact gate.
- Add separate strict models for manifests, inventory records, citations,
  candidates, issues, run state, and modules.
- Add draft-aware repository checks that validate only staged output and never
  load staged drafts as approved canon.
- Keep deterministic structural validation separate from agent-assisted
  evidentiary review, and report which layer produced each result.

## Validation Gates and Failure States

| Gate | Required check | Blocking failures |
|---|---|---|
| G0 Source | Manifest, immutable revision, path allowlist, file and manifest hashes | Missing source, hash mismatch, unpinned branch, unapproved redirect |
| G1 Parse | Complete AST and recognized module tables/headings | Parser error, truncated AST, unsupported construct in an inventory-bearing region |
| G2 Inventory | Table/heading reconciliation, deduplication, counts, welfare exclusion | Orphan signal, conflicting name/label/tier, duplicate output, welfare leakage |
| G3 Candidate | Candidate Pydantic schema and field classifications | Malformed agent output, unknown field, missing candidate artifact |
| G4 Evidence | Citation bytes, locators, hashes, and claim entailment | Invalid span, unsupported claim, citation to excluded authority |
| G5 Governance | Governed constants and decisions are available | Unknown module ID, unresolved `basic`/tier policy, invented priority, missing approval evidence |
| G6 Semantics | Allowed codes, missing rules, prerequisites, derivations, prohibitions | Contradictory fields, unsupported assumption, null required field |
| G7 Graph | Reference targets, reciprocal derivations where required, cycles, scope | Unknown final target, cycle, out-of-scope dependency represented as canonical |
| G8 Canonical | Existing strict canonical Pydantic models and body-section contract | Any schema failure or required prose section absent |
| G9 Write | Transactional output and path containment | Write outside `extraction/20_drafts/`, overwrite without matching lineage, partial artifact set |
| G10 Reproducibility | Repeat run and compare content artifacts and counts | Semantic or byte diff under identical locked inputs |

Run-fatal failures stop the run: source integrity failures, parser truncation,
manifest incompleteness, path violations, and reproducibility failures.
Item-blocking failures preserve the candidate and issue but prevent canonical
emission: missing evidence, citation failure, contradiction, unresolved
governance, and malformed agent output. Cross-item references may be pending
only when their target exists in the locked inventory; they must resolve before
module completion.

After each item attempt, Python must execute G3 through G9 and persist the
result before scheduling another item. G0 through G2 run before extraction, and
G10 runs at pilot and release checkpoints. A failed gate never becomes a
warning-only success.

## Approaches Considered

### Approach 1: Evidence-First Corpus Compiler

Build a shared source resolver, AST inventory, candidate contract,
orchestrator, agent roles, skills, and validators before bulk extraction.

Pros: strongest completeness proof, replayability, uniform provenance, and
scope control. Cons: largest up-front contract and parser investment, including
a controlled Pandoc/Quarto dependency.

### Approach 2: Module-by-Module Vertical Slices

Complete inventory, extraction, and validation separately for each module,
allowing the contract to evolve during implementation.

Pros: early reviewable outputs and locally understandable failures. Cons:
schema drift, repeated infrastructure, late discovery of cross-module
requirements, and rework when UTL or LBR exceeds early assumptions.

### Approach 3: Human-Curated Inventory Manifest

Ask humans to define the complete inventory and disputed structural fields,
then constrain agents to that list.

Pros: smaller parser and ambiguity surface. Cons: manual transcription becomes
an unaudited second source of truth, update detection is weak, and recurring
human cost is high. A small curated manifest remains useful as a test oracle.

## Decision

Adopt Approach 1, the evidence-first corpus compiler. Use vertical slices as
the delivery sequence within the shared architecture, and use a small
human-reviewed inventory as a parser gold set.

Keep the first agent implementation intentionally lean: one extractor and one
critic with module skills. Add specialization only after measured pilot errors
show that a separate role improves quality.

The first proof point is not bulk Markdown generation. It is a complete,
source-derived, cited inventory plus a validated candidate contract and hard
failure gates. This limits false confidence and gives later extraction a stable
denominator.

## Practical Implementation Phases

### Phase 0: Governance and Existing Approval

Corresponds to the completed roadmap feature "Document the schema approval"
and prerequisites for the remaining work.

- Locate or create the human-authorized record supporting the 2026-07-29
  schema approval; do not rely only on roadmap status.
- Clarify `AGENTS.md`: generated CVS artifacts begin in `20_drafts`, while
  supervised coding agents may edit implementation code and tests.
- Decide whether `basic` is distinct from `tier` and whether it belongs in the
  canonical model, inventory metadata, or neither.
- Approve a module registry, including the source filename `chapter5-LMR.qmd`,
  the chapter title LBR, and canonical `MOD-LBR`; also resolve DEM chapter rows
  labeled Education and Disability.
- Define governed defaults for rule priority, schema/GMD versions, and required
  prose sections. No extraction may invent these values.

### Phase 1: Inventory All Non-Welfare Variables

Implements roadmap feature `inventory-non-welfare-variables`.

- Add the source manifest, resolver, AST parser, normalization rules, inventory
  models, exclusion ledger, issue model, and gold fixtures.
- Produce a complete inventory for chapters 2 through 7 and a complete excluded
  inventory for chapter 8.
- Resolve every table/heading discrepancy through evidence or governance.
- Freeze an inventory version and counts by module before extraction begins.

### Phase 2: Define the Extraction Contract

Implements roadmap feature `define-extraction-contract`.

- Add candidate, citation, run-manifest, and state-machine schemas.
- Map every canonical field to its structural class and evidence requirement.
- Define artifact body sections, stable naming, lineage, overwrite rules,
  failure codes, and machine-readable report contracts.
- Add contract fixtures for simple, derived, country-specific, contradictory,
  and missing-evidence cases.

### Phase 3: Build the Extraction System and Gates

Implements roadmap features `build-extraction-system` and the executable part
of `validate-every-extraction` before bulk extraction.

- Build orchestration, safe writes, resume behavior, extractor and critic
  adapters, universal extraction skill, module skills, and draft-aware
  validators.
- Pilot IDN and GEO because they exercise shared identifiers,
  country-specific fields, repeated occurrences, and null-weight prohibitions
  without the full LBR derivation graph.
- Require every G0-G10 test and a repeated-run comparison to pass.

### Phase 4: Extract in Controlled Waves

Implements roadmap feature `extract-non-welfare-variables`.

1. IDN and GEO pilot.
2. DEM, including Education and Disability rows.
3. DWL.
4. UTL, including access, affordability, and derived expenditure variables.
5. LBR last because it has the largest inventory, repeated-period families,
   dense derivations, external standards, and visible source inconsistencies.

Each wave requires an inventory reconciliation report, item-level gate results,
module graph validation, critic review, and a human checkpoint before the next
wave. No wave writes outside draft staging.

### Phase 5: Validate Completion

Completes roadmap feature `validate-every-extraction` at milestone level.

- Prove that every locked in-scope inventory item is emitted or has a blocking
  issue with owner and disposition.
- Require zero welfare leakage and zero uncited non-generated claims.
- Require all citations to resolve against the locked source revision.
- Require all canonical drafts to pass existing and new strict validators.
- Require graph integrity, unique IDs, stable naming, complete provenance,
  and byte-stable content under a repeated run.
- Produce a milestone report for human review; do not promote artifacts.

## Risks and Unresolved Decisions

- The roadmap marks schema approval documentation done, but no obvious approval
  artifact was found in the expected project-documentation draft folder.
- `AGENTS.md` currently expresses conflicting implementation-write rules.
- The relationship between `basic` and `tier` is unresolved.
- The canonical module taxonomy is incomplete, especially LMR/LBR and
  Education/Disability rows embedded in DEM.
- The source includes apparent typos and mismatches. Normalization cannot
  silently correct them; each needs a cited alias decision or upstream fix.
- The current schema has no strict module model and no candidate/citation
  models.
- Current rule priorities are governed fields but are not supplied by the
  source guidelines. A policy or human decision is required.
- Current canonical validation permits unresolved variable references in
  drafts. Extraction validation needs a stricter milestone-completion rule.
- Pandoc availability and version pinning in local and CI environments must be
  decided during planning.
- Agent/model version pinning may not guarantee identical language output.
  Canonicalization and replay rules must distinguish deterministic mechanics
  from reviewed agent output.
- Source changes after the locked commit require a new manifest version and
  explicit delta inventory; they must never mutate an existing run silently.
- Citation entailment is not fully mechanical. The critic reduces risk but
  does not replace human approval.
- The Shiny app will need stable candidate, issue, and validation report
  schemas, but its interface and workflow are outside this milestone.

## Acceptance Criteria

### Ready for `/cg-plan`

- This decision record is accepted as the architecture baseline.
- Inventory unit, welfare boundary, source strategy, missing-evidence model,
  and responsibility split are decided.
- The six roadmap features are mapped to phases and validation is positioned
  before and during bulk extraction rather than only afterward.
- Unresolved governance items are listed as explicit plan tasks with owners,
  decision authority, and blocking effect.
- The plan can define concrete files, commands, tests, checkpoints, and rollback
  boundaries without reopening the core architecture.

### Ready for `/cg-work`

- A reviewed implementation plan exists and names the first bounded phase.
- `AGENTS.md` write permissions are clarified by an authorized human change.
- The schema approval evidence is locatable and the approved schema version is
  known.
- The source commit, manifest format, QMD parser/version, and module registry
  are approved.
- `basic` versus `tier`, rule-priority ownership, and all other fields needed by
  the first phase are resolved or explicitly modeled as blockers.
- Output paths, safe-write rules, failure codes, and validation commands are
  specified.
- Gold fixtures include at least one normal table/heading match, one repeated
  cross-module variable, one source mismatch, one helper exclusion, one CONS
  exclusion, and one missing-evidence candidate.
- CI can run focused unit tests without network dependence after fixture setup.
- No unresolved decision is allowed to be converted into a default assumption.

### Ready for Bulk Extraction

- The locked inventory and exclusion ledger pass completeness review.
- Candidate and citation contracts are versioned and tested.
- IDN/GEO pilots pass all gates and a repeated-run content comparison.
- Every failure state produces a machine-readable issue and non-zero/blocking
  outcome as specified.
- Human reviewers approve proceeding from the pilot to module waves.

## Next Steps

1. Run `/cg-plan` for the full milestone using this Deep scope and phase order.
2. Put the governance preflight and inventory denominator first in the plan.
3. Define the smallest Phase 1 file and test set before designing agent prompts.
4. Treat the current pinned commit as brainstorm evidence only; the plan must
   resolve and approve the source revision again when implementation begins.