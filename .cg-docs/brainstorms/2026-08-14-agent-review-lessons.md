# Lessons Learned: Independent Agent Review (Prototyping Session 2026-08-14)

## What was built (prototype, reverted)

A prototype of all 4 review agents was built and run against the 6 calibration
drafts. The prototype was reverted because it was built in Ask mode (read-only)
without using the Compound GPID workflow. These lessons should inform the proper
implementation via `/cg-plan` + `/cg-work`.

## Architecture discovered

### Agent contract
- Each agent is a standalone Python script in `extraction/agents/`
- Input: directory of extraction drafts (default `extraction/20_drafts/`)
- Output: per-artifact YAML findings file in `extraction/25_agent_review/<artifact-id>.<agent-name>.yml`
- A runner script (`run_all_agents.py`) executes all 4 agents and generates `extraction/25_agent_review/SUMMARY.md`

### Finding schema
```yaml
agent: <agent-name>
artifact_id: VAR-xxx
checked_at: <ISO-8601>
findings:
  - field: <field-path>
    severity: error|warning
    message: <human-readable>
    line: <int|null>
summary:
  errors: <int>
  warnings: <int>
  passed: bool  # false if errors > 0
```

### Python environment
- Project has `.venv/` with all required packages (pyyaml, pydantic)
- **Must use `.venv/bin/python`** — system Python 3.14.4 does not have pyyaml
- Schema imports require adding project root to sys.path

### Frontmatter parsing
- YAML frontmatter is between `---` markers on lines 0 and ~78
- Content between markers includes YAML comments (lines starting with `#`)
- `yaml.safe_load()` handles comments correctly, returns `dict`
- **Do NOT use `split('---', 2)`** — must find all `---` markers and extract between first two
- The `parse_frontmatter()` function must scan lines for `---` markers

### Pydantic validation
- `schema/variable.py::VariableDefinition` is the authoritative model
- Validation requires context: `variable_ids`, `rule_ids`, `allow_unresolved_draft=True`
- Without `allow_unresolved_draft=True`, any reference to a not-yet-extracted variable causes a validation error
- Parameter references (`country_parameters`) are validated against a parameter registry that may be empty

## Agent-specific findings

### Agent 1: schema-compliance (331 lines)
**What it checks:**
- YAML frontmatter parses and validates against Pydantic model
- variable_id, module_id, rule references match ID format patterns
- All 7 required Markdown sections present and non-stub (>= 50 chars)
- No placeholder text (TODO, TBD, FIXME, lorem ipsum)
- Variable references (derived_from, derives_to, prerequisites) exist or are noted as not yet extracted

**Prototype results on 6 calibration drafts:**
- 4/6 passed, 2 errors, 13 warnings
- Errors: VAR-educy and VAR-marital reference parameters that don't exist in the registry (PARAM-EDU-YEARS-BY-LEVEL, PARAM-DEM-MIN-MARRIAGE-AGE)
- Warnings: unresolved variable references (expected at 15% extraction), placeholder text in VAR-male

**Key design decisions:**
- `allow_unresolved_draft=True` because extraction is incomplete
- Parameter registry validation is strict (errors, not warnings) because parameters are defined separately from extraction
- Stub threshold: 50 chars per section (provisional, to be calibrated)

### Agent 2: source-grounding (250 lines)
**What it checks:**
- provenance.source_document is non-empty and references GMD guidelines
- provenance.source_section is non-empty
- Derived variable dependencies are documented in Construction notes
- Rules declared in frontmatter are referenced in the Markdown body

**Prototype results:**
- 6/6 passed, 0 errors, 18 warnings
- Warnings: rules declared but not referenced in body (RULE-EDU-001, RULE-EDU-002, RULE-SEX-001, etc.), derivation dependencies not mentioned in Construction notes

**Key design decisions:**
- "Rule not referenced in body" is a warning, not an error — rules may be implicit
- "Derivation dependency not mentioned" is a warning — the Construction notes may use different terminology

### Agent 3: rules-caveats (370 lines)
**What it checks:**
- All 7 required sections present and non-empty
- Construction notes: derivation paths documented, IF/THEN logic for derived variables, ordering for multiple paths
- Consistency checks: specific and actionable (not vague), in list format
- Escalation triggers: concrete IF conditions, not vague
- Common mistakes: real pitfalls, no placeholders
- Vague text patterns: "verify", "check that", "ensure", "appropriate", "valid", "correct", "reasonable"

**Prototype results:**
- 6/6 passed, 0 errors, 20 warnings
- Warnings: vague text in Consistency checks ("verify", "correct", "valid"), missing IF conditions in Escalation triggers, placeholder text

**Key design decisions:**
- Vague text detection uses regex patterns — these are heuristics, not definitive
- "Should have IF/THEN logic" is a warning for derived variables
- List format check (bullet points or numbered) for Consistency checks and Common mistakes

### Agent 4: consistency-derivation (277 lines)
**What it checks:**
- derived_from/derives_to symmetry (if A derives_from B, then B must derive_to A)
- Derivation graph is acyclic (cycle detection via DFS)
- Module consistency (cross-module derivations flagged as warnings)
- Value code consistency (derived variable's codes should be subset of source codes)
- Prerequisites exist or are noted as not yet extracted

**Prototype results:**
- 5/6 passed, 1 error, 7 warnings
- Error: VAR-educy derives_from VAR-educat4, but VAR-educat4 does not derive_to VAR-educy (asymmetry)
- Warnings: unresolved references (expected at 15% extraction)

**Key design decisions:**
- Symmetry errors are hard errors — these represent data integrity issues
- Cycle detection is critical for derivation graphs
- Cross-module derivations are warnings (may be intentional)
- Value code subset check is a warning (derived variables may have different codes via mapping)

### Runner: run_all_agents.py (158 lines)
**What it does:**
- Runs all 4 agents sequentially via subprocess
- Generates `SUMMARY.md` with aggregated results table and per-artifact findings
- Exit code 0 if no errors across all agents, 1 otherwise

## Implementation notes for /cg-plan

### File structure
```
extraction/
  agents/
    __init__.py
    schema_compliance.py      # Agent 1
    source_grounding.py       # Agent 2
    rules_caveats.py          # Agent 3
    consistency_derivation.py # Agent 4
    run_all_agents.py         # Runner
  25_agent_review/            # Output directory
    <artifact-id>.<agent>.yml # Per-artifact findings
    <agent>-summary.yml       # Per-agent summary
    SUMMARY.md                # Combined summary
```

### Dependencies
- pyyaml (already in .venv)
- pydantic (already in .venv, used by schema/variable.py)
- No new dependencies needed

### Test strategy
- Unit tests for each agent's check functions
- Integration tests running agents against the 6 calibration drafts
- Verify agents catch the known seeded defects:
  - VAR-educat7: RULE-EDU-999 (hallucinated rule) → source-grounding should warn
  - VAR-urban: module_id/directory mismatch → schema-compliance should error
  - VAR-marital: stub Construction notes → rules-caveats should error/warn
- Verify VAR-educy asymmetry is caught by consistency-derivation

### Calibration-vs-production thresholds
- Stub threshold (50 chars) needs calibration with real data
- Vague text patterns may produce false positives — needs review
- Parameter registry validation strictness should be configurable
- "not yet extracted" warnings should be filtered when running against incomplete extraction

### Integration with review-app
- Future: surface agent findings in the detail view of the review-app
- Future: flag artifacts with agent-review errors in the dashboard
- Future: agent findings could gate submission (Layer 1 extension)

### AGENTS.md compliance
- Agents write only to `extraction/25_agent_review/` (new directory, not in the restricted list)
- Agents read from `extraction/20_drafts/` and `schema/`
- Agents do NOT write to `knowledge/`, `extraction/30_review/`, or `extraction/40_approved/`
- The plan and any test files go through the normal Compound GPID workflow
