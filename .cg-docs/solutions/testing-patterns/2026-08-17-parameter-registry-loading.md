---
date: 2026-08-17
title: "Parameter registry loading pattern for review agents"
tags: [parameter-registry, schema-compliance, testing-pattern, regression-guard]
---

# Parameter Registry Loading Pattern

## Problem

Review agents that validate `country_parameters` references need access to the
parameter ID registry (`knowledge/parameters/*.md`). Without it, every
`country_parameters` reference is flagged as "not in registry" — a false
positive when the registry simply wasn't loaded.

## Solution

1. **Loader in helpers**: `list_parameter_ids(registry_dir)` globs `*.md`,
   parses each with `load_markdown`, extracts `parameter_id`, returns
   `tuple[set[str], list[str]]` (IDs + skipped filenames).

2. **Hard-stop guard in runner**: If the registry yields zero IDs but any
   draft declares non-empty `country_parameters`, abort with a clear error
   instead of proceeding with an empty set. This prevents silent false
   positives from wrong worktrees or shallow clones.

3. **Regression guard tests**: Keep existing tests that assert errors when
   `parameter_ids` is NOT passed (unloaded case). Add separate tests that
   pass `parameter_ids` and assert zero errors (loaded case). This tests
   both directions without overwriting the regression guard.

## Key Files

- `extraction_pipeline/review_agents/helpers.py` — `list_parameter_ids`
- `extraction_pipeline/review_agents/run_all_agents.py` — loader + hard-stop
- `tests/review_agents/test_schema_compliance.py` — loaded/unloaded test pairs
- `tests/review_agents/test_helpers.py` — unit tests for the loader

## Gotchas

- Do NOT import from `build/compile_bundle` — mirror the minimal
  glob+`load_markdown`+read pattern in `helpers.py` instead (C7).
- Resolve registry dir relative to `__file__`, not CWD, for portability.
- Include exception messages in skipped files for debugging.
- Keep the `test_runner_exit_code` assertion at `exit_code == 1` even after
  removing parameter errors — it's sustained by an unrelated stub defect.
