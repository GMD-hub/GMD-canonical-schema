---
date: 2026-08-15
title: "Pydantic allow_unresolved_draft does not bypass rule_ids/parameter_ids validation"
category: "testing-patterns"
language: "Python"
tags: [pydantic, validation, context, rule-ids, extraction]
root-cause: "allow_unresolved_draft only bypasses unknown variable references, not rule_ids or parameter_ids in the validate_references model_validator"
severity: "P2"
plan: ".cg-docs/plans/2026-08-14-build-agent-review.md"
---

# Pydantic allow_unresolved_draft Does Not Bypass rule_ids Validation

## Problem

When validating extraction drafts against `VariableDefinition` with
`allow_unresolved_draft=True`, Pydantic raised `unknown rule IDs: ['RULE-SEX-001']`
even though the flag was set. The flag only bypasses `unknown_variables`, not
`unknown_rules` or `unknown_parameters`.

## Root Cause

In `schema/variable.py`, the `validate_references` model_validator has three
separate checks:

```python
# This one is bypassed by allow_unresolved_draft:
if unknown_variables and not allow_unresolved_draft:
    raise ValueError(...)

# These two are NOT bypassed:
if unknown_parameters:
    raise ValueError(...)
if unknown_rules:
    raise ValueError(...)
```

The `allow_unresolved_draft` flag was designed for incomplete extraction (~15%),
which affects variable references. But rule IDs and parameter IDs have separate
registries that are also incomplete.

## Solution

Collect `rule_ids` from all drafts (just like `variable_ids`) and pass them
in the Pydantic validation context:

```python
variable_ids = set()
rule_ids = set()
for path in draft_paths:
    data, _ = load_draft(path)
    vid = data.get("variable_id", "")
    if vid:
        variable_ids.add(vid)
    for rule_id in data.get("rules", []):
        rule_ids.add(rule_id)

# Pass both to schema_compliance.check_draft
check_draft(path, variable_ids, rule_ids=rule_ids)
```

## Prevention

When using Pydantic `model_validator` with context-dependent resolution:
1. Always check which fields are gated by the `allow_*` flag
2. Populate the context sets for ALL registries, not just the flagged one
3. Integration tests against real drafts will surface this immediately