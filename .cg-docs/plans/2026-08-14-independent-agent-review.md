---
date: 2026-08-14
title: "Independent Agent Review"
status: active
scope: "Deep"
language: "both"
estimated-effort: "large"
deviation-policy: "ask"
tags: [agent-review, validation, extraction, schema, provenance]
---

# Plan: Independent Agent Review

## Objective

Build 4 specialized review agents that validate extraction drafts before human
review. Each agent checks a different dimension of quality: source grounding,
schema compliance, rules/caveats completeness, and cross-variable consistency.
Agents run automatically against `extraction/20_drafts/` and produce structured
findings that human reviewers can act on.

## Context

The calibration milestone is complete. The review-app is production-ready. The
next bottleneck is extraction quality at scale. Manual human review of every
draft is expensive; agent review provides a first pass that catches
systematic errors before humans invest time.

The 4 agents correspond to the 4 review dimensions identified in the
measurement framework (`.cg-docs/calibration/measurement-framework.md`):

1. **Source-grounding**: Every rule, value code, and derivation path must
   trace back to the GMD guidelines document.
2. **Schema-compliance**: YAML front matter must validate against the
   Pydantic model (`schema/variable.py`) with correct types and references.
3. **Rules-caveats**: IF/THEN logic must be complete, edge cases covered,
   no vague statements.
4. **Consistency-derivation**: Cross-variable references must be consistent,
   derivation graph must be acyclic, derived_from/derives_to must be symmetric.

## Phase 1: Build schema-compliance agent

### Step 1: Define the agent contract

- **Input**: A directory of extraction drafts (`extraction/20_drafts/`)
- **Output**: A YAML findings file per draft (`extraction/25_agent_review/<artifact_id>.schema-compliance.yml`)
- **Findings format**:
  ```yaml
  agent: schema-compliance
  artifact_id: VAR-male
  checked_at: 2026-08-14T16:30:00Z
  schema_version: "0.1"
  findings:
    - field: "rules[0]"
      severity: error
      message: "RULE-EDU-999 does not exist in the rule registry"
      line: 53
    - field: "derived_from"
      severity: warning
      message: "References VAR-educat7 which is not yet extracted"
  summary:
    errors: 1
    warnings: 1
    passed: true  # false if any errors
  ```

### Step 2: Implement the validator

- Use `schema/variable.py` Pydantic model for structural validation
- Check all field references (variable_id, rule_id, parameter_id) against
  the registry
- Validate YAML front matter is byte-identical to the loaded draft (C1)
- Check required Markdown sections are present and non-stub
- File: `review-app/R/agent_schema_compliance.R` or Python script
  `extraction/agents/schema_compliance.py`

### Step 3: Run against existing drafts

- Run against the 6 calibration drafts
- Compare findings against known-answer key (seeded defects in VAR-educat7,
  VAR-urban, VAR-marital)
- Verify the agent catches the known defects

## Phase 2: Build source-grounding agent

### Step 4: Define source-grounding checks

- Every `rules` reference must point to a rule that exists in `knowledge/rules/`
  or `extraction/20_drafts/` with a corresponding guideline section
- Every `value_codes` entry must have a guideline source citation in the
  Markdown body
- Every `derived_from` / `derives_to` must be grounded in the guidelines
  (not invented)
- The `provenance.source_document` and `provenance.source_section` must be
  non-empty and plausible

### Step 5: Implement and run

- File: `extraction/agents/source_grounding.py`
- Run against all drafts
- Report findings in the same YAML format

## Phase 3: Build rules-caveats agent

### Step 6: Define rules-caveats checks

- Each required Markdown section must contain substantive content:
  - `## Construction notes`: must document derivation paths, not just "TBD"
  - `## Consistency checks`: must have specific, actionable checks
  - `## Escalation triggers`: must have concrete conditions
  - `## Common mistakes`: must have real pitfalls, not generic text
- IF/THEN logic in Construction notes must be complete (no dangling conditions)
- No placeholder text ("TODO", "TBD", "placeholder", " lorem ipsum")

### Step 7: Implement and run

- File: `extraction/agents/rules_caveats.py`
- Run against all drafts
- Report findings

## Phase 4: Build consistency-derivation agent

### Step 8: Define consistency checks

- `derived_from` and `derives_to` must be symmetric across all variables
  (if A derives_from B, then B must derive_to A)
- Derivation graph must be acyclic (use `validate_acyclic_derivation_graph`)
- Module consistency: all variables in a derivation chain should be in the
  same module or have an explicit cross-module derivation path
- Value code consistency: if A derives_from B, A's value codes must be a
  subset or mapping of B's value codes

### Step 9: Implement and run

- File: `extraction/agents/consistency_derivation.py`
- Run against all drafts
- Report findings

## Phase 5: Integration and reporting

### Step 10: Build the agent-review runner

- Single entry point: `python extraction/agents/run_all_agents.py`
- Runs all 4 agents against all drafts
- Produces a summary report: `extraction/25_agent_review/SUMMARY.md`
- Exit code 0 if no errors, 1 if any agent found errors

### Step 11: Integrate with extraction workflow

- After extraction of each batch of variables, run the agent-review runner
- Findings in `extraction/25_agent_review/` are available to human reviewers
  in the review-app (optional: surface agent findings in the detail view)
- Artifacts with agent-review errors are flagged in the dashboard

### Step 12: Validate against calibration sample

- Run all 4 agents against the 6 calibration drafts
- Verify the agents catch the known defects:
  - VAR-educat7: hallucinated rule reference (RULE-EDU-999) -> schema-compliance
  - VAR-urban: module_id/directory mismatch -> schema-compliance + consistency
  - VAR-marital: stub Construction notes -> rules-caveats
- Measure catch rate vs known-answer key

## Verification

| ID | Evidence | Required |
|----|----------|----------|
| A1 | schema-compliance agent catches RULE-EDU-999 in VAR-educat7 | yes |
| A2 | source-grounding agent catches missing guideline citations | yes |
| A3 | rules-caveats agent catches stub sections in VAR-marital | yes |
| A4 | consistency-derivation agent catches module mismatch in VAR-urban | yes |
| A5 | All 4 agents run without errors on the 6 calibration drafts | yes |
| A6 | Summary report generated with findings per artifact | yes |

## Files to create

| File | Purpose |
|------|---------|
| `extraction/agents/schema_compliance.py` | Schema compliance validator |
| `extraction/agents/source_grounding.py` | Source grounding checker |
| `extraction/agents/rules_caveats.py` | Rules and caveats completeness |
| `extraction/agents/consistency_derivation.py` | Cross-variable consistency |
| `extraction/agents/run_all_agents.py` | Runner that executes all 4 |
| `extraction/25_agent_review/` | Output directory for findings |
| `.cg-docs/plans/2026-08-14-independent-agent-review.md` | This plan |

## Out of Scope

- Real-time agent review in the review-app UI (deferred to a later iteration)
- Agent review of welfare variables (out of scope for this project)
- Automatic fixes based on agent findings (agents report, humans decide)
