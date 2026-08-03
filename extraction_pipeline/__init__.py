"""extraction_pipeline — Deterministic guideline extraction pipeline.

This package provides:
- Preflight validation (source manifest, parser version)
- Source resolution (local checkout, hash verification)
- Pandoc AST parsing and normalization
- Strict extraction contracts (citations, candidates, issues)
- State machine with transactional writes
- Orchestrator that drives the per-item state machine through phases
- Bounded extractor and evidence critic agent adapters
"""
