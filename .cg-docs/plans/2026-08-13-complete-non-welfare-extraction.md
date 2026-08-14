---
date: 2026-08-13
title: "Complete Non-Welfare Variable Extraction Across All Modules"
status: completed
completed-date: 2026-08-14
scope: "Deep"
brainstorm: "../brainstorms/2026-08-03-extract-universal-non-welfare-schema.md"
follows: "2026-08-03-extract-universal-non-welfare-schema.md"
language: "Python"
estimated-effort: "large"
deviation-policy: "ask"
artifact-schema-version: 1
phases: 4
completed-phases: [0, 1, 2, 3]
tags: [extraction, non-welfare, variables, validation, provenance, idn, geo, dem, lbr, utl, dwl]
---

# Plan: Complete Non-Welfare Variable Extraction Across All Modules

## Objective

Produce schema-valid, source-grounded draft specifications for **every**
non-welfare variable defined in the GMD harmonization guidelines chapters 2-7,
across the six non-welfare modules (IDN, GEO, DEM, LBR, UTL, DWL). The
extraction infrastructure (pipeline, agents, skills, validators, manifest
contract) was built by the completed predecessor plan
(`2026-08-03-extract-universal-non-welfare-schema.md`). This follow-up
**hand-drafts** the remaining variables directly (the pipeline orchestrator is
a thin sequencer that accepts caller-provided candidates; it does not draft;
and preflight is blocked by the supervised manifest lock). The plan therefore
reads the source chapters, builds an authoritative per-module inventory from
each chapter's summary table, drafts every missing variable by hand, validates
against the Pydantic `VariableDefinition` schema, and emits a completeness
report with no chapter-8 (welfare) leakage.

The end state is a full set of drafts in `extraction/20_drafts/<module>/`
ready for the next calibration run of the human review app.

## Context

### What exists (predecessor plan, completed)
- Python pipeline at `extraction_pipeline/` (orchestrator, gates, writers,
  agents, evidence, state, reports, source, hashing, preflight, pandoc_ast).
  **Note**: the orchestrator (`run_item_pipeline`) is a thin sequencer that
  accepts caller-provided `evidence_packet`, `candidate`,
  `critic_disposition`, and `gate_results` — it does not draft. Preflight
  (`run_preflight`) hard-fails because the manifest `commit_sha` and
  `parser_contract.version` are `null` (supervised lock). This plan
  **hand-drafts** variables directly and does not invoke the pipeline
  orchestrator, gates, or preflight. Pipeline report functions requiring
  structured inputs are substituted with grep-based checks (see Step 12).
- Extraction agents and skills: `extraction/agents/{extractor,evidence-critic}.md`,
  `extraction/skills/universal-extraction.md`, `extraction/skills/modules/{idn,geo,dem,lbr,utl,dwl}.md`.
- Source manifest contract: `extraction/config/source-manifest.v1.yaml`
  (commit_sha and per-file sha256 currently `null`).
- Pydantic schema: `schema/variable.py` (`VariableDefinition`, strict,
  `extra="forbid"`), `schema/frontmatter.py` (`load_markdown`).
  **Note**: `VariableDefinition` validates frontmatter only; the body string
  from `load_markdown` is not inspected.
- Completeness/welfare-leakage checks: `extraction_pipeline/reports.py`
  (`build_completeness_report`, `check_no_welfare_leakage`, ...), tested in
  `tests/extraction/test_completeness.py`. **Note**: these require structured
  `RunState`/citation objects, not Markdown drafts — see Step 12 for the
  grep-based substitute.
- Tests under `tests/extraction/`. Dependencies: `pydantic>=2`, `PyYAML>=6`,
  `pytest>=8`, `loguru`.

### Current draft / approval state (fresher than project memory)
- Drafts in `extraction/20_drafts/` (6): `dem/{educat4,educat7,educy,male,marital}`, `geo/urban`.
- Approved in `knowledge/variables/` (3): `dem/{educat4,educy,male}` only.
- Modules IDN, LBR, UTL, DWL have **zero** drafts; GEO has only `urban`;
  DEM is missing `age`, `relationship_to_head` (→`VAR-relationshiptohead`
  per normalization), `marital_status` (→`VAR-marital` already exists —
  keep canonical, grandfathered exception), `educat5`, `literacy`,
  `disability_status` (→`VAR-disabilitystatus` per normalization) (per module skill; confirm against chapter 4 table).

### Source availability (NOT resolved — Phase 0 prerequisite)
- The authoritative source is the GitHub repository
  **https://github.com/GMD-hub/GMD-guidelines** (per AGENTS.md source-of-truth:
  `GMD_household_survey_harmonization.md (GMD-hub/GMD-guidelines, main branch)`).
  It is **not** inside this worktree (`extraction/10_source/` contains only
  `.gitkeep`).
- The source is available as a **local sibling repo** at
  `~/Documents/projects_WBG/GMD/GMD-guidelines/` (verified: commit
  `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` on `main`, chapters 2-8 present
  at `chapters/chapter{2..8}-*.qmd`). If the sibling repo is absent, clone
  from the GitHub URL above at commit `d46dc03`.
- The approved revision is `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` on
  branch `main` (matches the predecessor brainstorm and source-manifest
  comment). **This must be verified and the source obtained in Phase 0
  before any drafting begins.** If the sibling repo is absent or on a
  different commit, Phase 0 acquires or corrects it; if it cannot be
  obtained, this is a blocked-stop condition.

### Key constraints discovered during planning
- **Module skills are abbreviated hints, not the authoritative inventory.**
  The GEO chapter summary table lists `subnatid1..4`, `subnatidsurvey`,
  `subnatid1_prev..4_prev`, `urban` (15+ rows) — far more than the skill's
  `urban, subnatid1, subnatid2`. The per-chapter summary table is
  authoritative for the variable inventory.
- **`VariableDefinition` hard-fails on unknown RULE-*/PARAM-* IDs** with no
  draft exemption (only variable references honor `allow_unresolved_draft`).
  Registered rule IDs today: `RULE-EDU-001/002/003`, `RULE-SEX-001`
  (module/dem only). Existing draft `VAR-educat7` references `RULE-EDU-999`
  (unregistered) and will fail validation — must be fixed.
- **`variable_id` pattern rejects underscores** (`schema/variable.py:9`:
  `^VAR-[a-z][a-z0-9]*$`). GMD snake_case names (e.g. `marital_status`,
  `relationship_to_head`, `disability_status`) must be normalized to the
  CVS convention before drafting. The normalization rule is deterministic:
  **drop underscores** from the GMD name and prefix with `VAR-` (e.g.
  `marital_status`→`VAR-maritalstatus`, `relationship_to_head`→`VAR-relationshiptohead`,
  `disability_status`→`VAR-disabilitystatus`). There is exactly one
  grandfathered exception: `VAR-marital` (already exists as an approved
  artifact in `knowledge/variables/dem/` and must not be duplicated as
  `VAR-maritalstatus`). All other variables use the literal underscore-drop
  rule with no alternatives. The original snake_case is kept as
  `variable_name` in frontmatter. Every mapping is recorded in the Phase 1
  inventory before any draft is created. Existing approved artifact
  `VAR-male` and existing drafts `VAR-educat7`/`VAR-marital` all follow this
  no-underscore convention.
- **Body-section contract**: existing drafts and approved artifacts use a
  7-section body format (`Definition`, `Conceptual intent`, `Construction
  notes`, `Consistency checks`, `Escalation triggers`, `Common mistakes`,
  `Change log`). However, `extraction/skills/universal-extraction.md` and
  `extraction-governance.v1.yaml` define an **8-section** body contract
  (`Summary`, `Value codes`, `Derivation`, `Source note`, `Prerequisites`,
  `Country parameters`, `External standards`, `Provenance`). This plan
  **adopts the 7-section format** that existing drafts and approved
  `knowledge/` artifacts use, because they are the de facto standard and
  are already approved by the GPID Team. The 8-section contract is a
  governance-level contradiction tracked as a roadmap feature
  (`resolve-body-section-contract` under `complete-universal-records`).
  **V5 validates frontmatter only** (`load_markdown` + `VariableDefinition`
  does not inspect the body); a separate grep-based body-section check
  (V5b) enforces the 7-section presence.
- **Non-Null Weight Invariant is a governance concept, not a registered
  rule.** It is defined in `extraction-governance.v1.yaml:weight_invariant`
  as a concept with a citation — there is no `RULE-WGT-*` in
  `knowledge/rules/`. Weight-variable drafts must document the invariant
  in `provenance.notes`, never in `rules:`. The `rules:` list stays `[]`
  until a `RULE-WGT-*` is registered (tracked as roadmap feature
  `register-weight-invariant-rule`).
- **IDN ↔ DEM overlap**: both modules list `age`, `male`, `marital_status`,
  `relationship_to_head`. Each `variable_id` belongs to exactly one module.
  Ownership rule: **DEM owns core person demographics** (`age`, `male`,
  `marital_status`, `relationship_to_head`) per the approved `VAR-male`
  precedent (MOD-DEM, in `knowledge/variables/dem/`). **IDN owns household
  identifiers and survey-weight variables.** Overlap variables resolve to
  DEM; IDN drafts only its non-overlap variables. Record each decision.
- **AGENTS.md write boundary**: agents write only to `extraction/20_drafts/`
  (including `runs/`). The `extraction/config/source-manifest.v1.yaml`
  commit_sha/sha256 lock is a **supervised/human** step — this plan proposes
  values and records them in the run report; it does not write to `config/`.
- **`mineducatage` is an unregistered prerequisite** referenced in
  `extraction/20_drafts/dem/VAR-educat7.md` (`prerequisites: [{variable_id:
  VAR-mineducatage}]`). It is not in the DEM inventory and not a registered
  PARAM. Phase 1 inventory must classify it (variable to draft vs. parameter
  to register vs. out of scope) and record the decision. Tracked as roadmap
  feature `classify-mineducatage`.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R0 | Acquire the approved guideline source at commit `d46dc03` from GitHub repo `https://github.com/GMD-hub/GMD-guidelines` — use the local sibling repo at `~/Documents/projects_WBG/GMD/GMD-guidelines/` read-only if available, or propose a supervised clone into `extraction/10_source/` (outside `20_drafts/` write boundary; agent does not execute the clone); confirm chapters 2-7 present. This is a Phase 0 prerequisite — no drafting may begin until the source is verified. | AGENTS.md source-of-truth; P1.1/P2.6 findings |
| R1 | Verify the source commit, compute per-file sha256 for chapters 2-7, and propose the source-manifest lock (supervised — agent does not write to `extraction/config/`). | AGENTS.md source-of-truth; source-manifest.v1.yaml; predecessor brainstorm |
| R2 | Build an authoritative per-module non-welfare inventory from each chapter's summary table (ch2 IDN, ch3 GEO, ch4 DEM, ch5 LMR→LBR, ch6 UTL, ch7 DWL) with citations; reconcile against module skills (subsets); exclude ch8 CONS (welfare). Resolve IDN↔DEM ownership de-duplication (DEM owns core person demographics). Record variable-name normalization mappings (snake_case → `variable_id`). | universal-extraction.md Welfare Boundary; module skills; chapter tables; P1.2 finding |
| R3 | Draft every missing non-welfare variable as `extraction/20_drafts/<module>/VAR-<name>.md`: `VariableDefinition`-conformant YAML frontmatter + 7 body sections (7-section format adopted; see Key Constraints); apply field-classification discipline; cite provenance; null + blocking issue on missing evidence. | AGENTS.md; universal-extraction.md; extractor.md; existing drafts |
| R4 | Fix existing drafts that violate the schema or rubric (notably `VAR-educat7` → unregistered `RULE-EDU-999`; verify `VAR-marital`, `VAR-urban` conformance). Keep `VAR-marital` as the canonical name — do not rename to `marital_status` (fails `variable_id` pattern). | schema/variable.py reference validation; P2.3 finding |
| R5 | Validate every draft's **frontmatter** against `schema.variable.VariableDefinition` via `schema.frontmatter.load_markdown` (context `allow_unresolved_draft=True` for variable refs; hard rule/param checks). All drafts must pass frontmatter validation. | schema/variable.py, schema/frontmatter.py |
| R5b | Validate every draft's **body** has the 7 required sections (`## Definition`, `## Conceptual intent`, `## Construction notes`, `## Consistency checks`, `## Escalation triggers`, `## Common mistakes`, `## Change log`) via a grep-based header check (V5 only validates frontmatter). | P1.3/P2.4 findings |
| R6 | Produce an extraction inventory/completeness report under `extraction/20_drafts/runs/` mapping every inventoried variable to status (drafted/blocked) with content-error log entries. Welfare-leakage check: grep all drafts for `chapter8-CONS`/`chapter-8` references (the pipeline's `check_welfare_leakage_content` requires structured citation objects not present in Markdown drafts; a grep-based scan is the concrete substitute, documented as requiring human sign-off). | universal-extraction.md; P1.4 finding |

## Implementation Steps

## Phase 0: Acquire the source

### 1. Acquire and verify the approved guideline source
- **Requirements**: R0
- **Files**: `extraction/20_drafts/runs/source-acquisition-2026-08-13.md` (write)
- **Details**: The authoritative source is the GitHub repository
  **https://github.com/GMD-hub/GMD-guidelines** (per AGENTS.md). It is
  **not** inside this worktree (`extraction/10_source/` contains only
  `.gitkeep`). Before any drafting, acquire the source. **Note**:
  `extraction/10_source/` is **not** under `extraction/20_drafts/` — agents
  may not write there (C1). The acquisition strategy is:
  1. Check if the local sibling repo exists at
     `~/Documents/projects_WBG/GMD/GMD-guidelines/` and is at commit
     `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` on `main`. If present and
     at the correct commit, **use it read-only** at its existing path — no
     clone or copy needed. The chapter files are at
     `chapters/chapter{2..8}-*.qmd` and the full guidelines at
     `docs/GMD_household_survey_harmonization.md`.
  2. If the sibling repo is absent or on a different commit, the agent
     **proposes** (in the run report) a `git clone
     https://github.com/GMD-hub/GMD-guidelines.git` (and/or `git fetch &&
     git checkout d46dc03`) command to populate `extraction/10_source/`, but
     **does not execute it** — populating `10_source/` is a
     **supervised/human** step (like the manifest lock in Step 2), because
     it is outside the `extraction/20_drafts/` write boundary.
  3. Verify chapters `chapter2-IDN.qmd` through `chapter7-DWL.qmd` and
     `chapter8-CONS.qmd` exist at the resolved source path. Record any
     missing chapters.
  4. Write a source-acquisition report recording the resolved path, commit
     SHA, file-existence check results, and (if needed) the proposed clone
     command for a human to execute.
- **Test Scenarios**: happy path (sibling repo at `d46dc03`, used read-only);
  edge case (sibling repo on a different commit → propose checkout command);
  error path (repo missing → blocked-stop).
- **Tests**: `tests/extraction/test_source.py`
- **Acceptance criteria**: source is present at `d46dc03` (read-only sibling
  or human-populated `10_source/`); chapters 2-7 confirmed; source-acquisition
  report written. **No subsequent phase may begin until this is satisfied.**

## Phase 1: Source lock and authoritative inventory

### 2. Resolve and lock the approved source
- **Requirements**: R1
- **Files**: `extraction/config/source-manifest.v1.yaml` (propose only; do not
  write — supervised), `extraction/20_drafts/runs/source-lock-2026-08-13.md` (write)
- **Details**: Using the source acquired in Phase 0, confirm the commit is
  `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` on `main`. Verify chapters
  `chapter2-IDN.qmd` ... `chapter7-DWL.qmd` and `chapter8-CONS.qmd` exist.
  Compute sha256 for each included chapter (2-7) and record the welfare-excluded
  chapter 8 in the exclusion ledger. Write the resolved SHA + sha256 values into
  the run report and flag them for a human to apply to `source-manifest.v1.yaml`.
  Do **not** write to `extraction/config/`.
- **Test Scenarios**: happy path (SHA matches pinned); edge case (repo on a
  different commit); error path (repo missing).
- **Tests**: `tests/extraction/test_source.py`, `test_manifest.py`
- **Acceptance criteria**: run report records `commit_sha=d46dc03...` and a
  sha256 for each chapter 2-7; chapter 8 recorded as welfare-excluded.

### 3. Build per-module non-welfare inventory from chapter summary tables
- **Requirements**: R2
- **Files**: `extraction/20_drafts/runs/inventory-2026-08-13.md` (write);
  reads `chapters/chapter{2..7}-*.qmd` and `extraction/skills/modules/*.md`
- **Details**: For each non-welfare chapter, extract its variable summary
  table to a canonical inventory list (variable name, label, module code,
  tier, allowed codes, source section citation). Reconcile each list against
  the matching module skill (note that skills are subsets; the table wins).
  Apply the Welfare Boundary rule: chapter 8 CONS excluded (exclusion ledger
  entry only); chapter 6 UTL expenditure variables included; chapter 7 DWL
  included. Resolve IDN↔DEM overlap using the ownership rule (DEM owns core
  person demographics per `VAR-male` precedent; IDN owns household identifiers
  and survey-weight variables); record each decision. **Apply the
  variable-name normalization rule**: map every GMD snake_case name to a
  CVS `variable_id` by dropping underscores and prefixing with `VAR-`
  (e.g. `marital_status`→`VAR-maritalstatus`,
  `relationship_to_head`→`VAR-relationshiptohead`,
  `disability_status`→`VAR-disabilitystatus`). The single grandfathered
  exception is `VAR-marital` (already exists; must not be duplicated as
  `VAR-maritalstatus`). There are no alternatives — each GMD name maps to
  exactly one `variable_id`. Keep the original snake_case as `variable_name`.
  Record every mapping in the inventory. **Classify
  `mineducatage`**: determine whether it is a variable to draft, a country
  parameter to register, or out of scope; record the decision. Cross-check
  against existing drafts/approved variables to mark which are already done.
  Emit the inventory as a tracked table with one row per variable and a status
  column (`done`/`missing`/`blocked`).
- **Test Scenarios**: happy path (all 6 tables parsed); edge case (a chapter
  with tier-2 variables); error path (unparseable table → blocking issue).
- **Tests**: `tests/extraction/test_completeness.py`
- **Acceptance criteria**: inventory file lists every non-welfare variable
  with module, tier, citation, normalized `variable_id`, `variable_name`,
  and status; chapter 8 only in exclusion ledger; no duplicate `variable_id`
  across modules; `mineducatage` classified.

## Phase 2: Draft all missing variables

### 4. Draft IDN module variables
- **Requirements**: R3
- **Files**: `extraction/20_drafts/idn/VAR-<name>.md` (create); reads
  `chapter2-IDN.qmd`, `extraction/skills/modules/idn.md`
- **Details**: For each IDN inventory variable (e.g. household/person
  identifiers, weight variables), draft a spec following the established
  `VAR-male.md` shape. Frontmatter must satisfy `VariableDefinition` (strict).
  Reference only registered rule IDs or leave `rules: []`. **The Non-Null
  Weight Invariant is a governance concept, not a registered rule** — document
  it in `provenance.notes`, never in `rules:` (no `RULE-WGT-*` exists; tracked
  as roadmap feature). Body = 7 required sections (7-section format adopted;
  see Key Constraints). `provenance.source_section` must cite the chapter
  subsection. Use `extraction_method: manual`, `human_reviewed: false`. Set
  null + blocking issue where evidence is insufficient. Apply the
  variable-name normalization rule from Phase 1.
- **Test Scenarios**: happy path; edge case (top-coded age); error path
  (non-standard sex codes).
- **Tests**: V5 validation snippet per draft; V5b body-section check per draft.
- **Acceptance criteria**: one valid draft per IDN inventory variable.

### 5. Draft GEO module variables
- **Requirements**: R3
- **Files**: `extraction/20_drafts/geo/VAR-<name>.md` (create incl.
  `subnatid1..4`, `subnatidsurvey`, `*_prev`, and confirm/refine existing
  `urban`); reads `chapter3-GEO.qmd`, `extraction/skills/modules/geo.md`
- **Details**: Draft each GEO inventory variable. `urban` already exists as a
  draft — verify/reconcile rather than duplicate. Subnational variables are
  country-categorical strings; document country-parameter dependence
  (`country_parameters` list may be empty if no PARAM registered; do not
  fabricate PARAM IDs). Apply the variable-name normalization rule from Phase 1.
- **Test Scenarios**: happy path; edge case (country-specific coding); error
  path (sample stratum vs administrative geography ambiguity).
- **Tests**: V5 validation snippet per draft; V5b body-section check per draft.
- **Acceptance criteria**: one valid draft per GEO inventory variable; no
  duplicate `VAR-urban`.

### 6. Complete DEM module + fix existing DEM drafts
- **Requirements**: R3, R4
- **Files**: `extraction/20_drafts/dem/VAR-<name>.md` (create missing:
  `age`, `relationshiptohead` (from `relationship_to_head`), `educat5`,
  `literacy`, `disabilitystatus` (from `disability_status`) per Phase 1
  normalization — confirm against chapter 4 table); fix
  `extraction/20_drafts/dem/VAR-educat7.md`
- **Details**: Draft remaining DEM variables using the normalized `variable_id`
  names from Phase 1. **Fix `VAR-educat7`**: it references `RULE-EDU-999` which
  is not registered and will fail strict validation — replace with a registered
  rule ID or drop the reference and record a blocking issue. **Keep
  `VAR-marital` as the canonical name** — do not rename to `marital_status`
  (the `variable_id` pattern `^VAR-[a-z][a-z0-9]*$` rejects underscores;
  `VAR-marital` is already the approved convention). Use `variable_name:
  marital_status` in frontmatter to preserve the original GMD name. Verify
  `VAR-marital` frontmatter conformance. Preserve `educy` derivation graph
  (`derived_from`/`derives_to`) consistency with `educat7`.
- **Test Scenarios**: happy path; edge case (education age restrictions);
  error path (unregistered rule ref).
- **Tests**: V5 validation snippet per draft; V5b body-section check per draft;
  V4 grep for unregistered refs.
- **Acceptance criteria**: DEM inventory fully drafted; `VAR-educat7` passes
  validation; no unregistered RULE-/PARAM- refs in any DEM draft; `VAR-marital`
  not renamed.

### 7. Draft LBR module variables (chapter5-LMR alias)
- **Requirements**: R2, R3
- **Files**: `extraction/20_drafts/lbr/VAR-<name>.md` (create); reads
  `chapter5-LMR.qmd`, `extraction/skills/modules/lbr.md`
- **Details**: Resolve the `LMR`→`LBR` module-code alias through the approved
  normalization (cite it; never silently repair spelling). Draft employment
  status, occupation (ISCO), industry (ISIC), labor income, hours worked,
  employment sector, and any other chapter-5 inventory variables. Labor income
  is **in scope** (non-welfare); classify any chapter-8 consumption
  cross-reference as an exclusion-ledger entry, not a draft. External standards
  (ISCO/ISIC) go in `external_standards` with real URLs.
- **Test Scenarios**: happy path; edge case (repeated-period 7-day vs
  12-month); error path (informal classification ambiguity).
- **Tests**: V5 validation snippet per draft; V5b body-section check per draft.
- **Acceptance criteria**: one valid draft per LBR inventory variable; alias
  resolution cited.

### 8. Draft UTL module variables
- **Requirements**: R2, R3
- **Files**: `extraction/20_drafts/utl/VAR-<name>.md` (create); reads
  `chapter6-UTL.qmd`, `extraction/skills/modules/utl.md`
- **Details**: Draft access variables (electricity, water, sanitation,
  telecom) and derived utility expenditure variables. Apply Welfare Boundary:
  chapter-6 expenditure variables are non-welfare (included); chapter-8
  consumption references are excluded (ledger entry only). Flag access
  definitions that vary by country as country-parameter-dependent (no
  fabricated PARAM IDs).
- **Test Scenarios**: happy path; edge case (improved vs unimproved source);
  error path (composite index ambiguity).
- **Tests**: V5 validation snippet per draft; V5b body-section check per draft.
- **Acceptance criteria**: one valid draft per UTL inventory variable.

### 9. Draft DWL module variables
- **Requirements**: R2, R3
- **Files**: `extraction/20_drafts/dwl/VAR-<name>.md` (create); reads
  `chapter7-DWL.qmd`, `extraction/skills/modules/dwl.md`
- **Details**: Draft durable-goods ownership, asset-count, and
  housing-characteristic variables. These are non-welfare (chapter 7,
  included). Distinguish binary ownership vs count coding; document
  country-specific valuation dependence where relevant.
- **Test Scenarios**: happy path; edge case (binary vs count); error path
  (housing-characteristic coding ambiguity).
- **Tests**: V5 validation snippet per draft; V5b body-section check per draft.
- **Acceptance criteria**: one valid draft per DWL inventory variable.

## Phase 3: Validation and completion

### 10. Validate all drafts against the VariableDefinition schema (frontmatter)
- **Requirements**: R5, R4
- **Files**: all `extraction/20_drafts/<module>/VAR-*.md`; uses
  `schema/frontmatter.py`, `schema/variable.py`
- **Details**: For every draft, run `load_markdown(path)` then construct
  `VariableDefinition.model_validate(data, context={"allow_unresolved_draft": True,
  "variable_ids": <all known>, "parameter_ids": <registered PARAMs>,
  "rule_ids": <registered RULEs>})`. This validates **frontmatter only** —
  the body string returned by `load_markdown` is not inspected by
  `VariableDefinition`. Hard failures on unknown rule/param IDs must be fixed
  (drop the ref or record a blocking issue) — never weaken the model. Confirm
  frontmatter has no extra fields (`extra="forbid"`). Re-run until every draft
  passes frontmatter validation.
- **Test Scenarios**: happy path (all pass); edge case (draft referencing a
  not-yet-drafted variable — allowed via context); error path (unknown rule
  ID — fix).
- **Tests**: V5 snippet across all drafts; `tests/extraction/`
- **Acceptance criteria**: 0 frontmatter validation failures across all drafts.

### 11. Validate all drafts for 7 body sections (body)
- **Requirements**: R5b
- **Files**: all `extraction/20_drafts/<module>/VAR-*.md`
- **Details**: V5 (Step 10) validates frontmatter only. This step enforces the
  body-section contract via a grep-based header check. For every draft, grep
  for the 7 required `## ` headers: `## Definition`, `## Conceptual intent`,
  `## Construction notes`, `## Consistency checks`, `## Escalation triggers`,
  `## Common mistakes`, `## Change log`. Every draft must contain all 7. Any
  draft missing a section must be fixed and re-checked. This is a separate
  verification from V5 because `VariableDefinition` does not inspect the body.
- **Test Scenarios**: happy path (all 7 present); edge case (section present
  but empty stub — flag as content-error, not a structural failure); error
  path (missing section → fix).
- **Tests**: V5b grep snippet across all drafts.
- **Acceptance criteria**: every draft has all 7 required `## ` headers.

### 12. Produce completeness report and content-error log
- **Requirements**: R6
- **Files**: `extraction/20_drafts/runs/completeness-2026-08-13.md` (write)
- **Details**: Build a completeness report mapping every Phase-2 inventory
  item to `drafted` or `blocked` (with issue IDs). Record content-error log
  entries for any blocking issues (variable, missing field, reason, citation).
  Confirm `undisposed_count == 0` (every inventory item is either drafted or
  has a recorded blocking issue).

  **Welfare-leakage check**: The pipeline's `check_welfare_leakage_content`
  requires structured citation objects with a `source_path` field — Markdown
  drafts carry `provenance.source_section` as free text, not structured
  citations, so the function cannot run directly on draft outputs. Instead,
  use a **grep-based content scan**: search all files under
  `extraction/20_drafts/` for references to `chapter8-CONS`, `chapter-8`,
  `CONS.qmd`, or welfare-variable names from chapter 8. Any hit is a potential
  welfare-leakage finding that must be resolved (remove the cross-reference
  or move it to the exclusion ledger) before the report is finalized. Document
  that this grep-based scan is a substitute for the pipeline function and
  requires **human sign-off** (it is weaker than the content-based detector
  but is the only executable method against Markdown drafts). The deprecated
  `check_no_welfare_leakage` (ID-substring) is explicitly insufficient and is
  not used.

  The completeness report itself is hand-written (not generated by
  `build_completeness_report`, which requires a `RunState` of structured
  `ItemState` objects not produced by hand-drafting). The report's inventory
  table mirrors the Phase 1 inventory with a status column updated to
  `drafted`/`blocked`.
- **Test Scenarios**: happy path (complete); edge case (blocked item with
  issue); error path (welfare leakage detected → fix).
- **Tests**: `tests/extraction/test_completeness.py` (existing pipeline tests
  remain green; the hand-written report is verified by content review).
- **Acceptance criteria**: report shows all inventory items disposed; no
  welfare leakage (grep-based scan clean); content-error log complete.

## Testing Strategy

- **Per-draft frontmatter validation** (V5): a small Python snippet using
  `schema.frontmatter.load_markdown` + `schema.variable.VariableDefinition`
  with `allow_unresolved_draft=True`. This validates frontmatter only — the
  body is not inspected. Primary frontmatter gate.
- **Per-draft body-section check** (V5b): a grep-based header check verifying
  all 7 required `## ` headers are present. This is a separate gate because
  `VariableDefinition` does not inspect the body. Primary body gate.
- **Existing extraction tests**: `pytest tests/extraction/` covers contracts,
  governance, preflight, writers, completeness, source, manifest, state,
  orchestrator, manifest models, evidence, pandoc_ast, gates, agents.
- **Completeness**: the hand-written completeness report is verified by
  content review (the pipeline's `build_completeness_report` requires a
  structured `RunState` not produced by hand-drafting).
- **Welfare-leakage**: grep-based content scan for `chapter8-CONS`/`chapter-8`/
  `CONS.qmd` references across `extraction/20_drafts/` (the pipeline's
  `check_welfare_leakage_content` requires structured citation objects not
  present in Markdown drafts; grep is the concrete substitute, requiring
  human sign-off).
- **Reference integrity**: grep all drafts for `RULE-`/`PARAM-` references and
  confirm each is registered (no `RULE-EDU-999`-style violations).

## Documentation Checklist

- [ ] `extraction/20_drafts/runs/source-acquisition-2026-08-13.md` — source acquired and verified (Phase 0).
- [ ] `extraction/20_drafts/runs/source-lock-2026-08-13.md` — resolved SHA + sha256 (Phase 1).
- [ ] `extraction/20_drafts/runs/inventory-2026-08-13.md` — authoritative per-module inventory with naming mappings.
- [ ] `extraction/20_drafts/runs/completeness-2026-08-13.md` — completeness + content-error log + welfare scan results.
- [ ] Each draft's `provenance.source_section` cites its chapter subsection.
- [ ] No changes to `knowledge/`, `country-parameters/`, or `extraction/config/` by the agent.

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Source repo absent or at wrong commit | Medium | High | Phase 0 uses sibling repo read-only if available; proposes supervised clone if not; blocked-stop if neither works. |
| Source population of `10_source/` is supervised (agent cannot write outside `20_drafts/`) | Medium | High | Agent proposes clone command in run report; human executes; blocked-stop if human unavailable. |
| Module skills under-list variables vs chapter tables | High | Medium | Inventory from chapter summary tables (authoritative); skills are hints only. |
| Underscore variable names fail `variable_id` pattern | High | High | Phase 1 deterministic normalization: literal underscore-drop (one grandfathered exception: `VAR-marital`); record each mapping; keep original as `variable_name`. |
| 7-vs-8 body-section contract contradiction | Medium | High | Plan adopts 7-section format (matches approved `knowledge/` artifacts); 8-section contradiction tracked as roadmap feature; V5b grep enforces 7 sections. |
| Unknown RULE-/PARAM- IDs fail strict validation | High | High | Reference only registered IDs or leave empty + blocking issue; fix VAR-educat7. Non-Null Weight Invariant goes in `provenance.notes`, not `rules:`. |
| IDN↔DEM variable ownership ambiguity / duplicates | Medium | Medium | Phase 1 assigns single owner per variable_id using DEM-owns-demographics rule; record decision. |
| Source sibling repo drifts off `d46dc03` | Low | High | Lock and verify SHA at Phase 0/1; re-check before completion. |
| LBR/UTL/DWL canonical names not obvious | Medium | Medium | Resolve exact names from chapter tables in Phase 1 before drafting. |
| Large variable count extends beyond one session | Medium | Medium | Phased plan; each module is independently completable. |
| Welfare leakage from chapter-8 cross-references | Medium | High | Grep-based content scan for `chapter8-CONS`/`chapter-8` references; human sign-off required. |
| AGENTS.md write-boundary violation (config/) | Low | High | Manifest lock is supervised; agent writes only under `20_drafts/`. |
| `VAR-marital` rename breaks cross-references | Medium | High | Keep `VAR-marital` canonical; use `variable_name: marital_status` in frontmatter; do not rename. |
| Pipeline bypassed (hand-drafting) | — | Low | Plan explicitly states hand-drafting; pipeline functions requiring structured inputs are substituted with grep-based checks. |

## Out of Scope

- Chapter-8 (CONS) welfare variables.
- Promoting drafts to `knowledge/` (human-only approval).
- Country-parameter value authoring (`country-parameters/`).
- New pipeline infrastructure (already built by predecessor plan).
- The human review-app calibration run (separate plan:
  `2026-08-07-calibrate-human-review.md`).
- Stress-testing against legacy do-files (roadmap `idea`-stage feature).
- Resolving the 7-vs-8 body-section contract at the governance level (roadmap
  feature `resolve-body-section-contract` under `complete-universal-records`).
- Registering `RULE-WGT-*` for the Non-Null Weight Invariant (roadmap feature
  `register-weight-invariant-rule` under `universal-non-welfare-schema`).
- Classifying `mineducatage` as a variable vs. parameter beyond recording the
  decision in the inventory (roadmap feature `classify-mineducatage`).
- Formalizing the variable naming convention beyond this plan's Phase 1
  mappings (roadmap feature `standardize-variable-naming-convention`).

## Completion Contract

### Outcome
All non-welfare variables across the six modules (IDN, GEO, DEM, LBR, UTL, DWL)
exist as `VariableDefinition`-valid drafts in
`extraction/20_drafts/<module>/VAR-<name>.md`, each grounded in the locked
GMD-guidelines revision `d46dc03`, accompanied by an authoritative per-module
inventory and a completeness report confirming every inventoried variable is
drafted or has a recorded blocking issue, with no chapter-8 welfare leakage.

### Verification Surface
| ID | Evidence Required | Command/Artifact | Phase | Required |
|----|-------------------|------------------|-------|----------|
| V0 | Source acquired: commit `d46dc03` verified, chapters 2-7 present | `extraction/20_drafts/runs/source-acquisition-2026-08-13.md` | 0 | yes |
| V1 | Source locked: commit `d46dc03` + per-file sha256 proposed | `extraction/20_drafts/runs/source-lock-2026-08-13.md` + manifest (human-applied) | 1 | yes |
| V2 | Authoritative per-module inventory with citations, ch8 excluded, naming mappings, mineducatage classified | `extraction/20_drafts/runs/inventory-2026-08-13.md` | 1 | yes |
| V3 | Each missing variable drafted: frontmatter + 7 body sections | `extraction/20_drafts/<module>/VAR-<name>.md` count ≥ inventory | 2 | yes |
| V4 | No unregistered RULE-/PARAM- refs in drafts (VAR-educat7 fixed; VAR-marital not renamed) | `grep -rhE "RULE-\|PARAM-" extraction/20_drafts` vs registered set | 2 | yes |
| V5 | Every draft's **frontmatter** passes `VariableDefinition` validation | `python` snippet: `load_markdown` + `VariableDefinition(context={allow_unresolved_draft:True,...})` | 3 | yes |
| V5b | Every draft's **body** has all 7 required `## ` headers | `grep -rhE "^## " extraction/20_drafts` per draft vs required set | 3 | yes |
| V6 | Completeness report: all items drafted/blocked; no welfare leakage (grep-based scan) | `extraction/20_drafts/runs/completeness-2026-08-13.md`; grep scan for `chapter8-CONS` | final | yes |

### Constraints
| ID | Constraint | Check | Phase |
|----|------------|-------|-------|
| C1 | Agents write only to `extraction/20_drafts/` (incl. `runs/`) | path audit | all |
| C2 | Source = GMD guidelines at `d46dc03`; source wins on conflict | `provenance.source_section` cites chapter | all |
| C3 | `VariableDefinition` hard-fails on unknown RULE-/PARAM- IDs | V5 | 3 |
| C4 | Each `variable_id` belongs to exactly one module | inventory de-dup | 1 |
| C5 | Missing evidence → null + blocking issue; never invent | blocking-issue entries | 2 |
| C6 | Draft = VariableDefinition frontmatter + exactly 7 body sections (7-section format adopted) | V3, V5b | 2 |
| C7 | `variable_id` matches `^VAR-[a-z][a-z0-9]*$` (no underscores); snake_case names normalized via literal underscore-drop (one grandfathered exception: `VAR-marital`) | V5 + inventory naming column | 1 |
| C8 | Non-Null Weight Invariant documented in `provenance.notes`, not `rules:` | grep drafts for `RULE-WGT` (must be empty) | 2 |
| C9 | `VAR-marital` kept as canonical name (no rename to `marital_status`) | `VAR-marital` file exists, no `VAR-marital_status` file | 2 |

### Boundaries
- **Allowed**: using the sibling repo read-only at its existing path (Phase
  0); drafting variables for IDN, GEO, DEM, LBR (ch5-LMR), UTL, DWL; fixing
  existing non-conformant drafts; writing inventory/completeness reports
  under `extraction/20_drafts/runs/`.
- **Supervised/human**: populating `extraction/10_source/` (outside
  `20_drafts/` write boundary; agent proposes the clone command but does
  not execute it); applying the source-manifest lock to
  `extraction/config/source-manifest.v1.yaml`.
- **Out of scope**: chapter-8 CONS/welfare variables; promotion to
  `knowledge/`; country-parameter values; new pipeline infrastructure; the
  review-app calibration run; resolving the 7-vs-8 body-section contract at
  the governance level (roadmap feature `resolve-body-section-contract`);
  registering `RULE-WGT-*` (roadmap feature `register-weight-invariant-rule`).

### Iteration Policy
1. Phase 0 (source acquisition) must complete before any other phase begins.
2. On a draft failing `VariableDefinition` frontmatter validation, fix
   frontmatter and re-validate in-step; do not skip.
3. On a draft missing a body section, add it and re-check via V5b; do not skip.
4. On missing evidence for a field, set `null` + record a blocking issue
   rather than guessing; proceed to the next variable.
5. On a chapter summary-table ambiguity (e.g., IDN↔DEM ownership), resolve by
   the ownership rule (DEM owns core person demographics) and record it.
6. Unregistered RULE-/PARAM- references → drop the reference (leave empty) or
   record a blocking issue; never fabricate IDs. The Non-Null Weight Invariant
   is documented in `provenance.notes`, never `rules:`.
7. Variable names with underscores → normalize via literal underscore-drop
   to `^VAR-[a-z][a-z0-9]*$` (one grandfathered exception: `VAR-marital`);
   record the mapping in the inventory. No alternatives.

### Blocked-Stop Conditions
- The `GMD-guidelines` source at `d46dc03` cannot be acquired — neither the
  local sibling repo (`~/Documents/projects_WBG/GMD/GMD-guidelines/`) is
  available read-only nor a human has cloned
  `https://github.com/GMD-hub/GMD-guidelines` into `extraction/10_source/`
  (Phase 0).
- The sibling `GMD-guidelines` source is hash-mismatched.
- A chapter summary table cannot be parsed to a variable inventory (escalate;
  do not improvise).
- `VariableDefinition` schema is incompatible with a required legitimate field
  (escalate to schema owner; do not weaken the model).
