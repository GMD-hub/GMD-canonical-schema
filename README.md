# GMD Canonical Variable Schema

This repository contains the Canonical Variable Schema (CVS) for the GMD
AI-Assisted Harmonization project. The CVS is the authoritative,
machine-readable representation of the rules governing how each GMD variable
must be harmonized across all household surveys processed by the GPID Team.

## What is in this repository

The `knowledge/` folder contains one Markdown file per GMD variable, one
Markdown file per decision rule, and one Markdown file per GMD module. Each
file has YAML front matter (structured, machine-readable metadata) and a
Markdown body (human-readable guidance). These files are the rulebook that
the AI harmonization agent reads before drafting a Harmonization Specification
for any new survey.

The `extraction/` folder contains the staged pipeline used to produce CVS
artifacts from the GMD harmonization guidelines. The `lookup-tables/` folder
contains country-specific parameter tables referenced by CVS records. The
`schema/` folder contains Pydantic models that validate every CVS artifact.

See `knowledge/index.md` for a complete list of all artifacts and their paths.
See `AGENTS.md` for the operating rules that govern any agent working here.

## This repository is part of a three-schema pipeline

| Schema | Repo | Purpose |
|--------|------|---------|
| Schema 1: Survey Profile | GMD-hub/survey-scribe | Captures what is in a raw household survey |
| Schema 2: Canonical Variable Schema | This repo | Defines the GMD harmonization rules |
| Schema 3: Harmonization Specification | GMD-hub/harmonization-specs | Maps survey to GMD standard for one variable/survey pair |
