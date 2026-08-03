---
date: 2026-08-03
title: "Welfare boundary enforcement — content-based detection vs ID-substring heuristic"
category: "testing-patterns"
language: "Python"
tags: [welfare-boundary, content-based-detection, false-positives, false-negatives, extraction-pipeline, gates]
root-cause: "ID-substring heuristic cannot detect welfare leakage through citation evidence"
severity: "P0"
---

# Welfare Boundary Enforcement — Content-Based Detection

## Problem

The extraction pipeline's welfare leakage detector (`check_no_welfare_leakage`
in `extraction_pipeline/reports.py`) used a simple ID-substring heuristic:
any inventory ID containing "CONS" was flagged as welfare leakage. This had
two failure modes:

1. **False negatives**: An inventory ID like `INV-UTL-014` (a utilities
   variable) whose cited evidence references `chapter8-CONS.qmd` was NOT
   flagged — the welfare content leaked through because the ID doesn't
   contain "CONS".

2. **False positives**: An inventory ID like `INV-CONSULTATION-001` was
   flagged as welfare leakage even though it has nothing to do with
   consumption — "CONS" appears as a substring of "CONSULTATION".

The G9 welfare gate (`g9_welfare_gate`) compounded the problem by accepting
a bare `bool` parameter with no guarantee that the caller actually ran the
detector. A caller could pass `True` without ever checking for leakage.

## Root Cause

The original detector was written as a quick heuristic without considering
the governance Decision 10 welfare boundary rules, which define welfare
content by **source file reference** (chapter 8), not by inventory ID
naming convention. The boundary is about **what evidence the candidate
cites**, not **what the candidate is named**.

## Solution

### 1. Content-based detector

Added `check_welfare_leakage_content()` in `reports.py` that inspects each
candidate's `evidence_ids` → `Citation.source_path`. If any citation points
to `chapter8-CONS.qmd`, the candidate is flagged — regardless of its
inventory ID.

```python
def check_welfare_leakage_content(
    candidates: list[dict[str, Any]],
    citations_by_id: dict[str, dict[str, Any]],
    excluded_source: str = WELFARE_EXCLUDED_SOURCE,
) -> dict[str, Any]:
    # Inspect each candidate's evidence_ids → Citation.source_path
    # Flag if any citation points to the welfare-excluded source file
```

### 2. Structured gate input

Changed `g9_welfare_gate` to accept a structured leakage report (dict with
`leaked`, `leaked_ids`, `detector_version`) instead of a bare `bool`. This
ensures the gate is wired to the detector and records the detector version
for audit traceability. Backward-compatible bare-bool path retained.

### 3. Orchestrator wiring

The orchestrator now passes the G9 gate result from `gate_results` into
`g9_welfare_gate`, ensuring the welfare gate is actually checked before
canonicalization.

## Prevention

### Anti-pattern: ID-substring heuristics for content classification

Never classify content by naming convention. Inventory IDs, variable names,
and file names are labels — they don't determine what evidence the content
references. Always inspect the actual content (citations, source paths,
evidence links) when enforcing boundaries.

### Pattern: Structured gate inputs

Gates should accept structured reports from detectors, not bare booleans.
A bare `bool` parameter carries no provenance — the caller could have
fabricated it. A structured report with `detector_version` and `leaked_ids`
provides audit trail and makes the wiring explicit.

### Pattern: Content-based boundary checks

When a governance decision defines a boundary by source reference (e.g.,
"chapter 8 is welfare"), the detector must inspect source references, not
proxy identifiers. The detector should consume candidates + citations, not
just ID strings.

### Testing: False-positive and false-negative cases

Always test both directions:
- A non-CONS ID citing chapter8 → must be flagged (false-negative prevention)
- A CONS-substring ID NOT citing chapter8 → must NOT be flagged (false-positive prevention)

## Related

- Governance Decision 10: `governance/decisions/Extraction-Preflight-2026-08.md`
- Review report P0.4/P0.5: `.cg-docs/reviews/2026-08-03-extract-universal-non-welfare-schema-review.md`
- `extraction_pipeline/reports.py` — `check_welfare_leakage_content()`
- `extraction_pipeline/gates.py` — `g9_welfare_gate()`
- `extraction_pipeline/orchestrator.py` — G9 wiring
