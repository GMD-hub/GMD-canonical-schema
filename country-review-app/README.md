# Country Input Review App

This app is a dedicated review workspace for country-input artifacts:

- parameter drafts under `extraction/20_drafts/runs/country-parameters/<ISO3>/`
- exception drafts under `extraction/20_drafts/runs/country-parameters/<ISO3>/`
- benchmark references under `governance/benchmarks/` (read-only)

## Current implementation status

Phase 1 to Phase 5 core workflow is implemented:

- app shell (`app.R`, `R/run.R`, `R/app_ui.R`, `R/app_server.R`)
- country artifact model validators (`R/models.R`)
- country queue discovery/index (`R/country_queue.R`)
- role authorization (`R/authorization.R`)
- review state transitions (`R/state_machine.R`)
- local review record/body persistence and staged approvals (`R/actions.R`)
- detail pane with YAML editor and action buttons (save/submit/revision/approve/reopen)

This app intentionally does not write to canonical `country-parameters/countries/`.
Approved outputs will be staged under `extraction/40_approved/country-parameters/`.

Review records are persisted under `extraction/30_review/country-inputs/`.

## Local run (development)

```r
source("R/run.R")
run_app()
```
