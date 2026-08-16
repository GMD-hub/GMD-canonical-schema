---
date: 2026-08-15
title: "Build Independent Agent Review System"
status: active
scope: "Standard"
brainstorm: ".cg-docs/brainstorms/2026-08-14-agent-review-lessons.md"
language: "Python"
estimated-effort: "medium"
deviation-policy: "ask"
artifact-schema-version: 1
tags: [extraction, agents, review, validation, python]
phases: 2
---

# Plan: Build Independent Agent Review System

## Objective

Build four deterministic Python review agents and a runner that validate every
extraction draft in `extraction/20_drafts/` against schema compliance, source
grounding, rules/caveats completeness, and cross-variable consistency. Each
agent writes structured YAML findings to `extraction/25_agent_review/`. A
runner script executes all agents and generates an aggregated `SUMMARY.md`.

## Context

A prototype of all 4 agents was built and tested against 6 calibration drafts
on 2026-08-14, then reverted because it bypassed the Compound GPID workflow.
The prototype confirmed the architecture, finding schema, and agent logic.
This plan re-implements the same design through `/cg-plan` + `/cg-work` with
proper tests and documentation.

Key constraints from the brainstorm:
- Must use `.venv/bin/python` (system Python 3.14.4 lacks pyyaml)
- Pydantic validation needs `allow_unresolved_draft=True` (extraction ~15% complete)
- Frontmatter parsing: reuse `schema/frontmatter.py::load_markdown()` which
  uses `split("\n---\n", 1)` — safe because `\n` anchors match actual delimiter
  lines. The brainstorm's warning "Do NOT use `split('---', 2)`" refers to an
  incorrect approach without `\n`, not to the existing parser.
- No new dependencies required (pyyaml, pydantic already in .venv)

### Package location rationale

The review agents are deterministic Python scripts, not LLM role definitions.
They belong in `extraction_pipeline/review_agents/` (the established Python
package) rather than `extraction/review_agents/` (which is a data directory
without `__init__.py`). The existing `extraction/agents/` directory contains
LLM role definitions (`.md` files) and is a different concern.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Update AGENTS.md to allow agent writes to `extraction/25_agent_review/` | AGENTS.md §Where agents write (P1.2 fix) |
| R2 | Finding schema: YAML with agent, artifact_id, checked_at, findings[], summary{} | Brainstorm §Finding schema |
| R3 | Agent 1: schema-compliance validates Pydantic model, ID formats, structural section presence, placeholders | Brainstorm §Agent 1 |
| R4 | Agent 2: source-grounding checks provenance, derivation docs, rule references | Brainstorm §Agent 2 |
| R5 | Agent 3: rules-caveats checks content quality (50-char threshold, actionable content, vague text, formatting) | Brainstorm §Agent 3 |
| R6 | Agent 4: consistency-derivation checks symmetry, cycles, module consistency, value codes | Brainstorm §Agent 4 |
| R7 | Runner executes all agents sequentially, generates SUMMARY.md, exits 0/1 | Brainstorm §Runner |
| R8 | Write output to `extraction/25_agent_review/` (AGENTS.md updated in R1) | AGENTS.md §Where agents write |
| R9 | Unit tests for each agent's check functions | Brainstorm §Test strategy |
| R10 | Integration tests against 6 calibration drafts with known-answer-key fixture | Brainstorm §Test strategy |

### Required sections constant

The 7 required Markdown sections (shared by Agents 1 and 3):

1. Definition
2. Conceptual intent
3. Construction notes
4. Consistency checks
5. Escalation triggers
6. Common mistakes
7. Change log

## Phase 1: Core Implementation

### 1. Update AGENTS.md to allow review agent output

- **Requirements**: R1, R8
- **Files**: `AGENTS.md`
- **Details**:
  - Add a row to the "Where agents allowed to write" table:
    `| extraction/25_agent_review/ | Agent review findings (YAML) | Agent |`
  - This is a governance change requiring human approval before agents can
    write findings. If implementing via `/cg-work`, the AGENTS.md edit must
    be the first commit.
  - Also add `extraction/review_agents/` row for the runner's own artifacts:
    `| extraction/review_agents/ | Review agent code and runner | Agent |`
- **Test Scenarios**: N/A (governance documentation)
- **Tests**: N/A
- **Acceptance criteria**: AGENTS.md table includes `extraction/25_agent_review/` as agent-writeable

### 2. Create shared finding schema and helpers

- **Requirements**: R2, R8
- **Files**: `extraction_pipeline/review_agents/__init__.py`, `extraction_pipeline/review_agents/models.py`, `extraction_pipeline/review_agents/helpers.py`
- **Details**:
  - Define Pydantic models for the finding schema: `Finding` (field, severity, message, line), `AgentSummary` (errors, warnings, passed), `AgentFindings` (agent, artifact_id, checked_at, findings, summary)
  - Create `load_draft(path)` that calls `schema.frontmatter.load_markdown(path)` — reuse the existing parser, do not reimplement frontmatter parsing
  - Create `write_findings(findings: AgentFindings, output_dir: Path)` that serializes to YAML
  - Create `list_drafts(drafts_dir: Path)` that yields all `.md` files recursively
  - Define `REQUIRED_SECTIONS` constant: `["Definition", "Conceptual intent", "Construction notes", "Consistency checks", "Escalation triggers", "Common mistakes", "Change log"]`
- **Test Scenarios**:
  - Happy path: valid frontmatter parses correctly via `load_draft`
  - Edge case: frontmatter with YAML comments (lines starting with `#`)
  - Error path: missing `---` markers raises ValueError
- **Tests**: `tests/review_agents/test_models.py`, `tests/review_agents/test_helpers.py`
- **Acceptance criteria**: `AgentFindings` model validates against the brainstorm YAML spec; `load_draft` handles the 6 calibration drafts

### 3. Build schema-compliance agent

- **Requirements**: R3
- **Files**: `extraction_pipeline/review_agents/schema_compliance.py`
- **Details**:
  - **Structural checks only** (content quality is Agent 3's responsibility):
    - Check YAML frontmatter parses via `load_markdown` and validates against `VariableDefinition` with context:
      - `variable_ids` = set of all `variable_id` values from all draft files
      - `parameter_ids` = `set()` (empty — registry not yet populated)
      - `rule_ids` = `set()` (empty — registry not yet populated)
      - `allow_unresolved_draft = True`
    - Validate `variable_id`, `module_id`, rule references match ID format patterns from `schema/variable.py`
    - Check all 7 required Markdown section headings present (heading exists, has any content after it)
    - Detect placeholder text in body: TODO, TBD, FIXME, lorem ipsum
    - Check variable references (derived_from, derives_to, prerequisites) exist or note as not yet extracted
    - Parameter reference validation is strict (errors) because parameters are defined separately from extraction
  - **Does NOT check** section content quality (50-char threshold, vague text) — that is Agent 3
- **Test Scenarios**:
  - Happy path: VAR-male passes all checks
  - Error path: VAR-educy references PARAM-EDU-YEARS-BY-LEVEL not in empty registry → error
  - Error path: VAR-marital references PARAM-DEM-MIN-MARRIAGE-AGE not in empty registry → error
  - Warning path: unresolved variable references → warning (extraction incomplete)
  - Edge case: placeholder text (TODO) detected in VAR-educat7 escalation triggers
- **Tests**: `tests/review_agents/test_schema_compliance.py`
- **Acceptance criteria**: Agent produces correct findings for all 6 calibration drafts

### 4. Build source-grounding agent

- **Requirements**: R4
- **Files**: `extraction_pipeline/review_agents/source_grounding.py`
- **Details**:
  - Check `provenance.source_document` is non-empty and references GMD guidelines
  - Check `provenance.source_section` is non-empty
  - Check derived variable dependencies are documented in Construction notes
  - Check rules declared in frontmatter are referenced in the Markdown body
  - "Rule not referenced in body" is a warning (rules may be implicit)
  - "Derivation dependency not mentioned" is a warning (Construction notes may use different terminology)
- **Test Scenarios**:
  - Happy path: VAR-male passes all checks
  - Warning path: rules declared but not referenced in body → warning (e.g., RULE-EDU-001 in VAR-educat4)
  - Warning path: derivation dependencies not mentioned in Construction notes → warning
  - Error path: empty provenance.source_document → error
- **Tests**: `tests/review_agents/test_source_grounding.py`
- **Acceptance criteria**: Agent produces correct findings for all 6 drafts

### 5. Build rules-caveats agent

- **Requirements**: R5
- **Files**: `extraction_pipeline/review_agents/rules_caveats.py`
- **Details**:
  - **Content quality checks** (section heading presence is Agent 1's responsibility):
    - Check each of the 7 required sections has substantive content (>= 50 chars of body text after heading)
    - Construction notes: derivation paths documented, IF/THEN logic for derived variables, ordering for multiple paths
    - Consistency checks: specific and actionable (not vague), in list format (bullet points or numbered)
    - Escalation triggers: concrete IF conditions, not vague
    - Common mistakes: real pitfalls, no placeholders
    - Vague text detection via regex patterns: "verify", "check that", "ensure", "appropriate", "valid", "correct", "reasonable"
    - List format check (bullet points or numbered) for Consistency checks and Common mistakes
  - **Does NOT check** section heading existence — that is Agent 1
- **Test Scenarios**:
  - Happy path: VAR-male passes all checks
  - Warning path: vague text in Consistency checks → warning
  - Warning path: missing IF conditions in Escalation triggers → warning
  - Error path: stub Construction notes (< 50 chars) → error (VAR-marital has "TODO.")
- **Tests**: `tests/review_agents/test_rules_caveats.py`
- **Acceptance criteria**: Agent produces correct findings for all 6 drafts

### 6. Build consistency-derivation agent

- **Requirements**: R6
- **Files**: `extraction_pipeline/review_agents/consistency_derivation.py`
- **Details**:
  - Check `derived_from`/`derives_to` symmetry: if A derives_from B, then B must derive_to A
  - Derivation graph is acyclic (cycle detection via DFS)
  - Module consistency: cross-module derivations flagged as warnings
  - Value code consistency: derived variable's codes should be subset of source codes (warning). Handle `value_codes: null` gracefully (continuous variable, no codes to subset-check)
  - Prerequisites exist or are noted as not yet extracted
  - Symmetry errors are hard errors (data integrity issues)
  - Requires loading all drafts to build the full derivation graph
- **Test Scenarios**:
  - Happy path: VAR-male (no derivations) passes
  - Error path: VAR-educy derives_from VAR-educat4, but VAR-educat4 derives_to only [] (not VAR-educy) → asymmetry error
  - Warning path: cross-module derivation → warning
  - Edge case: cycle detection with hypothetical cycle → error
  - Edge case: derived variable with `value_codes: null` (VAR-educy) vs. source with explicit codes (VAR-educat7) → no value_code warning (null means continuous)
- **Tests**: `tests/review_agents/test_consistency_derivation.py`
- **Acceptance criteria**: Agent catches VAR-educy asymmetry error

## Phase 2: Runner, Tests, and Documentation

### 7. Build runner script

- **Requirements**: R7
- **Files**: `extraction_pipeline/review_agents/run_all_agents.py`
- **Details**:
  - Execute all 4 agents sequentially against a drafts directory (default `extraction/20_drafts/`)
  - Write per-artifact findings to `extraction/25_agent_review/<artifact-id>.<agent-name>.yml`
  - Generate `extraction/25_agent_review/SUMMARY.md` with aggregated results table and per-artifact findings
  - Exit code 0 if no errors across all agents, 1 otherwise
  - Accept `--drafts-dir` argument (default `extraction/20_drafts/`)
  - Accept `--output-dir` argument (default `extraction/25_agent_review/`)
  - Use `argparse` for CLI interface
  - Importable as module: `python -m extraction_pipeline.review_agents.run_all_agents`
- **Test Scenarios**:
  - Happy path: runs against calibration drafts, produces SUMMARY.md, exit 0 or 1 based on errors
  - Edge case: empty drafts directory → exit 0 with empty summary
  - Error path: invalid drafts directory → exit with error message
- **Tests**: `tests/review_agents/test_runner.py`
- **Acceptance criteria**: Runner produces SUMMARY.md with results table; exit code reflects error state

### 8. Create known-answer-key and write integration tests

- **Requirements**: R9, R10
- **Files**: `tests/review_agents/known_answer_key.yml`, `tests/review_agents/test_integration.py`
- **Details**:
  - Create `known_answer_key.yml` listing expected findings for each agent × artifact combination:
    ```yaml
    - artifact_id: VAR-educy
      agent: schema_compliance
      field: country_parameters
      severity: error
      message_contains: "PARAM-EDU-YEARS-BY-LEVEL"
    - artifact_id: VAR-educy
      agent: consistency_derivation
      field: derived_from
      severity: error
      message_contains: "asymmetry"
    - artifact_id: VAR-educat7
      agent: schema_compliance
      field: body
      severity: warning
      message_contains: "TODO"
    - artifact_id: VAR-marital
      agent: rules_caveats
      field: construction_notes
      severity: error
      message_contains: "stub"
    - artifact_id: VAR-marital
      agent: schema_compliance
      field: country_parameters
      severity: error
      message_contains: "PARAM-DEM-MIN-MARRIAGE-AGE"
    ```
  - Integration tests load the key and verify each expected finding is present in agent output
  - Test the full pipeline: runner executes all agents and produces SUMMARY.md
  - Note: VAR-urban `module_id`/directory mismatch is NOT in the known-answer-key because no directory-to-module mapping convention exists in the codebase. Mark as future calibratable check.
- **Test Scenarios**:
  - Full pipeline run against calibration drafts
  - Verify each known-answer-key entry matches an actual finding
  - Verify SUMMARY.md format and content
- **Tests**: `tests/review_agents/test_integration.py`
- **Acceptance criteria**: All known-answer-key entries matched; SUMMARY.md matches expected format

### 9. Write documentation

- **Requirements**: R8
- **Files**: `extraction_pipeline/review_agents/README.md`
- **Details**:
  - Create README documenting:
    - What each agent checks (with the 7 required sections listed)
    - How to run the runner: `.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents`
    - Finding schema specification
    - Output directory structure (`extraction/25_agent_review/`)
    - Calibration notes (thresholds are provisional, vague text patterns are heuristics)
    - Known-answer-key format for adding new expected findings
  - Note: AGENTS.md was updated in Step 1 to authorize writes to `extraction/25_agent_review/`
- **Test Scenarios**: N/A (documentation)
- **Tests**: N/A
- **Acceptance criteria**: README.md exists with complete usage documentation

## Testing Strategy

- **Unit tests**: Each agent's check functions tested in isolation with synthetic draft content
- **Integration tests**: Full pipeline run against the 6 calibration drafts, validated against `known_answer_key.yml`
- **Test runner**: `.venv/bin/python -m pytest tests/review_agents/ -v`
- **Test data**: Use the existing 6 calibration drafts in `extraction/20_drafts/dem/` and `extraction/20_drafts/geo/`
- **Known defects to verify** (from `known_answer_key.yml`):
  - VAR-educy: parameter reference error (PARAM-EDU-YEARS-BY-LEVEL) + derivation asymmetry with VAR-educat4
  - VAR-educat7: placeholder text (TODO) in escalation triggers + hallucinated rule (RULE-EDU-999)
  - VAR-marital: stub construction notes ("TODO.") + parameter reference error (PARAM-DEM-MIN-MARRIAGE-AGE)
  - VAR-urban: unresolved derivation reference (VAR-rurality)

## Documentation Checklist

- [ ] `extraction_pipeline/review_agents/README.md` with usage docs
- [ ] Docstrings on all public functions and classes
- [ ] Finding schema documented in README and in `models.py` docstrings
- [ ] `known_answer_key.yml` documented with format spec

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Pydantic validation changes incompatibly | Low | High | Pin to `>=2.0,<3.0` (already in requirements.txt); test against current `schema/variable.py` |
| False positives from vague text regex patterns | Medium | Medium | Patterns are heuristics; document as warnings not errors; if warnings exceed 5 per draft after initial run, refactor the regex patterns |
| Stub threshold (50 chars) too strict or too lenient | Medium | Low | Provisional value; adjust after calibration run |
| Parameter registry empty during validation | High | Low | Expected at 15% extraction; use `allow_unresolved_draft=True` with empty `parameter_ids`/`rule_ids` context |
| AGENTS.md change requires human approval | High | Low | Step 1 is a governance change; must be committed before any agent writes |

## Out of Scope

- Integration with review-app Shiny UI
- Gating submission on agent findings (Layer 1 extension)
- Calibrating thresholds beyond prototype values
- Running agents against non-calibration drafts
- Directory-to-module mapping check (no convention exists; future calibratable check)

## Completion Contract

### Outcome

Four deterministic Python review agents and a runner script exist in
`extraction_pipeline/review_agents/`, validated by unit and integration tests
in `tests/review_agents/`. AGENTS.md authorizes agent writes to
`extraction/25_agent_review/`. Running the runner against the 6 calibration
drafts produces structured YAML findings and a `SUMMARY.md` with an aggregated
results table, validated against a formal `known_answer_key.yml` fixture.

### Verification Surface

| ID | Evidence Required | Command/Artifact | Required |
|----|-------------------|------------------|----------|
| V1 | All 4 agents run against 6 calibration drafts without crash | `.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents extraction/20_drafts/` | yes |
| V2 | Schema-compliance catches VAR-educy parameter reference error | `extraction/25_agent_review/VAR-educy.schema_compliance.yml` contains error for PARAM-EDU-YEARS-BY-LEVEL | yes |
| V3 | Consistency-derivation catches VAR-educy→VAR-educat4 asymmetry | `extraction/25_agent_review/VAR-educy.consistency_derivation.yml` contains asymmetry error | yes |
| V4 | All unit tests pass | `.venv/bin/python -m pytest tests/review_agents/ -v` | yes |
| V5 | Runner produces SUMMARY.md with aggregated table | `extraction/25_agent_review/SUMMARY.md` exists and contains results table | yes |
| V6 | AGENTS.md authorizes `extraction/25_agent_review/` writes | AGENTS.md write-targets table includes the directory | yes |
| V7 | Integration tests pass against known-answer-key | `.venv/bin/python -m pytest tests/review_agents/test_integration.py -v` | yes |

### Constraints

| ID | Constraint | Check |
|----|------------|-------|
| C1 | Agents write only to AGENTS.md-authorized directories | `extraction/25_agent_review/` listed in AGENTS.md write-targets table |
| C2 | Use `.venv/bin/python` | All test/run commands use venv Python |
| C3 | No new dependencies | Only pyyaml, pydantic (already in .venv) |
| C4 | Finding schema is YAML with agent, artifact_id, checked_at, findings[], summary{} | Matches brainstorm spec |
| C5 | `allow_unresolved_draft=True` for Pydantic validation | Extraction is ~15% complete |
| C6 | Reuse `schema/frontmatter.py::load_markdown()` | No duplicate frontmatter parsing code |

### Boundaries
- **Allowed**: Read from `extraction/20_drafts/`, `schema/`, `knowledge/`; write to `extraction/25_agent_review/`, `extraction_pipeline/review_agents/`, `tests/review_agents/`
- **Out of scope**: Integration with review-app UI, gating submission on agent findings, calibrating thresholds beyond prototype values, running agents against non-calibration drafts, directory-to-module mapping check

### Iteration Policy
1. If an agent check produces excessive false positives on calibration drafts, adjust the threshold/pattern and document the calibration decision
2. If vague-text warnings exceed 5 per draft after initial run, refactor the regex patterns instead of accepting the noise
3. If Pydantic validation fails due to missing parameter registry entries, treat as expected (extraction incomplete) and use `allow_unresolved_draft=True`
4. If a finding schema field is ambiguous, follow the brainstorm's YAML spec exactly

### Blocked-Stop Conditions
- `.venv` missing or pyyaml/pydantic not installed
- `extraction/20_drafts/` directory empty or missing
- `schema/variable.py::VariableDefinition` model changed incompatibly since brainstorm
- AGENTS.md update (Step 1) rejected by human reviewer
