# Agent Review Summary

- **Run at**: 2026-08-14T20:28:47.676948+00:00
- **Agents**: 4

## Results

| Agent | Artifacts | Passed | Failed | Errors | Warnings |
|-------|-----------|--------|--------|--------|----------|
| schema-compliance | 6 | 4 | 2 | 2 | 13 |
| source-grounding | 6 | 6 | 0 | 0 | 18 |
| rules-caveats | 6 | 6 | 0 | 0 | 20 |
| consistency-derivation | 6 | 5 | 1 | 1 | 7 |

**Overall**: FAILURES DETECTED
- Total errors: 3
- Total warnings: 58

## Per-Artifact Findings

### VAR-educat4 (schema-compliance) - PASS
- [warning] References VAR-educat5 which is not yet extracted
- [warning] Prerequisite references VAR-mineducatage which is not yet extracted

### VAR-educat7 (schema-compliance) - PASS
- [warning] Prerequisite references VAR-mineducatage which is not yet extracted
- [warning] Section '## Escalation triggers' may be a stub (43 chars < 50 threshold)
- [warning] Section '## Escalation triggers' contains placeholder text: 'TODO'

### VAR-educy (schema-compliance) - FAIL
- [error] Pydantic validation failed: 1 validation error for VariableDefinition
  Value error, unknown parameter IDs: ['PARAM-EDU-YEARS-BY-LEVEL'] [type=value_error, input_value={'variable_id': 'VAR-educ...ountry record exists.'}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error
- [warning] References VAR-educat5 which is not yet extracted
- [warning] Prerequisite references VAR-mineducatage which is not yet extracted
- [warning] Prerequisite references VAR-school which is not yet extracted

### VAR-male (schema-compliance) - PASS
- [warning] Section '## Construction notes' contains placeholder text: 'placeholder'
- [warning] Section '## Common mistakes' contains placeholder text: 'placeholder'

### VAR-marital (schema-compliance) - FAIL
- [error] Pydantic validation failed: 1 validation error for VariableDefinition
  Value error, unknown parameter IDs: ['PARAM-DEM-MIN-MARRIAGE-AGE'] [type=value_error, input_value={'variable_id': 'VAR-mari... known-answer-key.md.'}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error
- [warning] Section '## Construction notes' may be a stub (5 chars < 50 threshold)
- [warning] Section '## Construction notes' contains placeholder text: 'TODO'

### VAR-urban (schema-compliance) - PASS
- [warning] References VAR-rurality which is not yet extracted

### VAR-educat4 (source-grounding) - PASS
- [warning] Definition does not reference source section 'Demography (DEM), Mapping and Description of Variables, educat4'
- [warning] Derivation dependency 'VAR-educat7' not mentioned in Construction notes
- [warning] Derivation dependency 'VAR-educat5' not mentioned in Construction notes
- [warning] Rule 'RULE-EDU-001' is declared but not referenced in the Markdown body
- [warning] Rule 'RULE-EDU-002' is declared but not referenced in the Markdown body

### VAR-educat7 (source-grounding) - PASS
- [warning] Definition does not reference source section 'Demography (DEM), Mapping and Description of Variables, educat7 (calibration fixture)'
- [warning] Rule 'RULE-EDU-999' is declared but not referenced in the Markdown body

### VAR-educy (source-grounding) - PASS
- [warning] Definition does not reference source section 'Demography (DEM), Mapping and Description of Variables, educy'
- [warning] Derivation dependency 'VAR-educat7' not mentioned in Construction notes
- [warning] Derivation dependency 'VAR-educat5' not mentioned in Construction notes
- [warning] Derivation dependency 'VAR-educat4' not mentioned in Construction notes
- [warning] Rule 'RULE-EDU-001' is declared but not referenced in the Markdown body
- [warning] Rule 'RULE-EDU-003' is declared but not referenced in the Markdown body

### VAR-male (source-grounding) - PASS
- [warning] Definition does not reference source section 'Demography (DEM), Mapping and Description of Variables, male'
- [warning] Rule 'RULE-SEX-001' is declared but not referenced in the Markdown body

### VAR-marital (source-grounding) - PASS
- [warning] Definition does not reference source section 'Demography (DEM), Mapping and Description of Variables, marital (calibration fixture)'

### VAR-urban (source-grounding) - PASS
- [warning] Definition does not reference source section 'Geography (GEO), Mapping and Description of Variables, urban (calibration fixture)'
- [warning] Derivation dependency 'VAR-rurality' not mentioned in Construction notes

### VAR-educat4 (rules-caveats) - PASS
- [warning] Derivation dependency 'VAR-educat7' not documented in Construction notes
- [warning] Derivation dependency 'VAR-educat5' not documented in Construction notes
- [warning] Consistency checks: vague 'verify' - specify what to check
- [warning] Consistency checks: vague 'correct' - specify correctness criteria
- [warning] Escalation triggers should have concrete IF conditions
- [warning] Escalation triggers: vague 'reasonable' - specify reasonableness criteria

### VAR-educat7 (rules-caveats) - PASS
- [warning] Derived variable should have IF/THEN logic in Construction notes
- [warning] Escalation triggers should have concrete IF conditions

### VAR-educy (rules-caveats) - PASS
- [warning] Derivation dependency 'VAR-educat7' not documented in Construction notes
- [warning] Derivation dependency 'VAR-educat5' not documented in Construction notes
- [warning] Derivation dependency 'VAR-educat4' not documented in Construction notes
- [warning] Escalation triggers: vague 'valid' - specify validity criteria

### VAR-male (rules-caveats) - PASS
- [warning] Consistency checks: vague 'check that' - specify the check
- [warning] Consistency checks: vague 'valid' - specify validity criteria
- [warning] Common mistakes contains placeholder text: '\bplaceholder\b'

### VAR-marital (rules-caveats) - PASS
- [warning] Consistency checks: vague 'valid' - specify validity criteria
- [warning] Escalation triggers should have concrete IF conditions
- [warning] Escalation triggers: vague 'valid' - specify validity criteria

### VAR-urban (rules-caveats) - PASS
- [warning] Derivation dependency 'VAR-rurality' not documented in Construction notes
- [warning] Consistency checks: vague 'verify' - specify what to check

### VAR-educat4 (consistency-derivation) - PASS
- [warning] VAR-educat4 derives_from VAR-educat5 which is not yet extracted
- [warning] Prerequisite VAR-mineducatage is not yet extracted

### VAR-educat7 (consistency-derivation) - PASS
- [warning] Prerequisite VAR-mineducatage is not yet extracted

### VAR-educy (consistency-derivation) - FAIL
- [warning] VAR-educy derives_from VAR-educat5 which is not yet extracted
- [error] VAR-educy derives_from VAR-educat4, but VAR-educat4 does not derive_to VAR-educy
- [warning] Prerequisite VAR-mineducatage is not yet extracted
- [warning] Prerequisite VAR-school is not yet extracted

### VAR-male (consistency-derivation) - PASS

### VAR-marital (consistency-derivation) - PASS

### VAR-urban (consistency-derivation) - PASS
- [warning] VAR-urban derives_from VAR-rurality which is not yet extracted
