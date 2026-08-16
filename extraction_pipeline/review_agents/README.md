# Review Agents

Deterministic Python agents that validate extraction drafts against schema
compliance, source grounding, rules/caveats quality, and cross-variable
consistency.

## Agents

| Agent | Module | What it checks |
|-------|--------|----------------|
| Schema Compliance | `schema_compliance.py` | Pydantic validation, ID formats, required section presence, placeholder text |
| Source Grounding | `source_grounding.py` | Provenance fields, derivation documentation, rule references in body |
| Rules & Caveats | `rules_caveats.py` | Section content quality (≥50 chars), actionable checks, vague text, list format |
| Consistency & Derivation | `consistency_derivation.py` | derived_from/derives_to symmetry, cycle detection, module consistency, value codes |

### Required Sections

All 7 sections must be present and have content:

1. Definition
2. Conceptual intent
3. Construction notes
4. Consistency checks
5. Escalation triggers
6. Common mistakes
7. Change log

## Usage

Run all agents against the default drafts directory:

```bash
.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents
```

Specify custom directories:

```bash
.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents extraction/20_drafts/ --output-dir extraction/25_agent_review/
```

## Output

### Per-artifact findings

Each agent writes a YAML file per artifact to the output directory:

```
extraction/25_agent_review/
├── VAR-male.schema_compliance.yml
├── VAR-male.source_grounding.yml
├── VAR-male.rules_caveats.yml
├── VAR-male.consistency_derivation.yml
├── ...
└── SUMMARY.md
```

### Finding schema

```yaml
agent: schema_compliance
artifact_id: VAR-male
checked_at: "2026-08-15T12:00:00+00:00"
findings:
  - field: country_parameters
    severity: error
    message: "Parameter reference not in registry: PARAM-EDU-YEARS-BY-LEVEL"
    line: null
summary:
  errors: 1
  warnings: 0
  passed: 0
```

### Exit codes

- `0`: No errors across all agents (warnings allowed)
- `1`: At least one error found

## Calibration Notes

- Thresholds are provisional and based on the 6 calibration drafts
- Vague text patterns (`verify`, `check that`, `ensure`, etc.) are heuristics
- The 50-char minimum section length is a starting point; adjust after calibration runs
- The `PARAM-*` and `RULE-*` registries are currently empty; parameter reference checks
  will flag errors until the registries are populated

## Known Answer Key

Integration tests validate against `tests/review_agents/known_answer_key.yml`.
Add new entries as new expected findings are discovered:

```yaml
- artifact_id: VAR-educy
  agent: schema_compliance
  field: country_parameters
  severity: error
  message_contains: "PARAM-EDU-YEARS-BY-LEVEL"
```

## Running Tests

```bash
.venv/bin/python -m pytest tests/review_agents/ -v
```