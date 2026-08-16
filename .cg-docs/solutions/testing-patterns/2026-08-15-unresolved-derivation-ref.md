---
date: 2026-08-15
title: "Derivation asymmetry check requires both variables in draft set"
category: "testing-patterns"
language: "Python"
tags: [graph-validation, asymmetry, derivation, cross-variable]
root-cause: "The symmetry check only fires when both source and target variables exist in the drafts; unresolved references need a separate check"
severity: "P3"
plan: ".cg-docs/plans/2026-08-14-build-agent-review.md"
---

# Derivation Asymmetry Check Requires Both Variables in Draft Set

## Problem

VAR-urban declares `derived_from: [VAR-rurality]` but VAR-rurality is not in
the draft set. The expected test for an asymmetry warning on VAR-urban failed
because the symmetry check only fires when `source_id in all_variables`.

## Root Cause

The symmetry check logic:

```python
for source_id in derived_from:
    if source_id in all_variables:
        # Only checks symmetry when both vars exist
        source_derives_to = all_variables[source_id].get("derives_to", [])
        if vid not in source_derives_to:
            # This never fires for VAR-rurality
```

When the source variable doesn't exist in the draft set, the check is skipped
entirely — it can't check `derives_to` of a non-existent variable.

## Solution

Add a separate `_check_unresolved_derivation_refs` function that flags
`derived_from` references to variables not in the draft set as warnings:

```python
def _check_unresolved_derivation_refs(data, all_variables):
    findings = []
    for dep in data.get("derived_from", []):
        if dep not in all_variables:
            findings.append(Finding(
                field="derived_from",
                severity="warning",
                message=f"Unresolved derivation reference: {dep} not found in extracted drafts",
            ))
    return findings
```

This distinction matters: asymmetry (both exist but derives_to is missing) is
an error, while unresolved (source doesn't exist yet) is a warning.

## Prevention

When building cross-variable checks:
1. Handle the "variable not in set" case explicitly — don't silently skip
2. Distinguish "completeness warnings" (extraction incomplete) from "integrity
   errors" (both exist but data is contradictory)
3. Test both cases: variable in set and variable not in set