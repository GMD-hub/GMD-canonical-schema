"""Completeness and reproducibility reports — Phase 6 Step 15."""

from pathlib import Path
from typing import Any

from extraction_pipeline.state import RunState
from schema.extraction.run import CompletenessReport


# The welfare-excluded source file per source-manifest.v1.yaml and
# governance Decision 10. Any candidate whose cited evidence references
# this file has welfare leakage (unless recorded in the exclusion ledger
# as a welfare-reference, not a leaked canonical output).
WELFARE_EXCLUDED_SOURCE = "chapter8-CONS.qmd"

# Detector version — recorded in gate reports for audit traceability.
WELFARE_LEAKAGE_DETECTOR_VERSION = "v1-content"

# Volatile files excluded from byte-identical run comparison (P2.13/P2.19).
# These are orchestration state, not canonical content.
_VOLATILE_FILENAMES = frozenset({
    "run-ledger.json",
    "run-ledger.jsonl",
    "run-state.json",
    "content-run-manifest.json",
})


def _is_volatile(rel_path: Path) -> bool:
    """Check if a file is volatile (excluded from byte comparison) by exact name."""
    return rel_path.name in _VOLATILE_FILENAMES


def build_completeness_report(
    inventory_ids: list[str],
    run_state: RunState,
) -> CompletenessReport:
    """Produce a machine-readable completeness report.

    Every inventory item must have a disposition (canonical or blocked).
    """
    canonical: list[str] = []
    blocked: list[str] = []
    undisposed: list[str] = []

    for inv_id in inventory_ids:
        item = run_state.items.get(inv_id)
        if item is None:
            undisposed.append(inv_id)
        elif item.state.value == "canonical":
            canonical.append(inv_id)
        elif item.state.value == "blocked":
            blocked.append(inv_id)
        else:
            undisposed.append(inv_id)

    complete = len(undisposed) == 0

    return CompletenessReport(
        complete=complete,
        total_items=len(inventory_ids),
        canonical_count=len(canonical),
        blocked_count=len(blocked),
        undisposed_count=len(undisposed),
        undisposed_ids=undisposed,
        canonical_ids=canonical,
        blocked_ids=blocked,
    )


def check_no_welfare_leakage(inventory_ids: list[str], excluded_module: str = "CONS") -> bool:
    """Verify no welfare content leaked into non-welfare inventory.

    .. deprecated::
        This ID-substring heuristic is too narrow (misses content-based
        leakage where a non-CONS ID cites chapter8-CONS.qmd) and too broad
        (false positives on IDs containing "CONS" as a substring).
        Prefer :func:`check_welfare_leakage_content` for content-based
        detection. Retained for backward compatibility with existing callers.
    """
    for inv_id in inventory_ids:
        if excluded_module.upper() in inv_id.upper():
            return False
    return True


def check_welfare_leakage_content(
    candidates: list[dict[str, Any]],
    citations_by_id: dict[str, dict[str, Any]],
    excluded_source: str = WELFARE_EXCLUDED_SOURCE,
) -> dict[str, Any]:
    """Content-based welfare leakage detector.

    Inspects each candidate's ``evidence_ids`` to resolve the cited
    ``Citation.source_path`` values. If any citation points to the
    welfare-excluded source file (``chapter8-CONS.qmd`` by default), the
    candidate is flagged as leaked — regardless of its inventory ID.

    This replaces the ID-substring heuristic (:func:`check_no_welfare_leakage`)
    which missed candidates whose ID does not contain "CONS" but whose
    evidence cites chapter 8.

    Args:
        candidates: List of candidate dicts, each with ``inventory_id`` and
            ``evidence_ids`` (field → list of citation IDs).
        citations_by_id: Mapping of citation ID → citation dict (must
            contain ``source_path``).
        excluded_source: The welfare-excluded source filename.

    Returns:
        A structured leakage report::

            {
                "detector_version": "v1-content",
                "leaked": bool,
                "leaked_ids": ["INV-UTL-014", ...],
                "excluded_source": "chapter8-CONS.qmd",
            }
    """
    leaked_ids: list[str] = []
    for candidate in candidates:
        inv_id = candidate.get("inventory_id", "")
        evidence_ids: dict[str, list[str]] = candidate.get("evidence_ids", {})
        for _field, citation_ids in evidence_ids.items():
            for cit_id in citation_ids:
                citation = citations_by_id.get(cit_id)
                if citation is None:
                    continue
                source_path = citation.get("source_path", "")
                if source_path == excluded_source:
                    if inv_id not in leaked_ids:
                        leaked_ids.append(inv_id)
                    break

    return {
        "detector_version": WELFARE_LEAKAGE_DETECTOR_VERSION,
        "leaked": len(leaked_ids) > 0,
        "leaked_ids": leaked_ids,
        "excluded_source": excluded_source,
    }


def check_no_duplicate_ids(inventory_ids: list[str]) -> bool:
    """Verify all inventory IDs are unique."""
    return len(inventory_ids) == len(set(inventory_ids))


def compare_runs(reference_dir: Path, current_dir: Path) -> bool:
    """Compare two run directories for byte-identical content.

    Returns True if all content files match. Volatile files (run-ledger,
    run-state, content-run-manifest) are excluded by exact filename —
    they are orchestration state, not canonical content (P2.13/P2.19).
    """
    if not reference_dir.exists() or not current_dir.exists():
        return False

    # Collect relative paths, excluding volatile files by exact name
    ref_files = {
        p.relative_to(reference_dir): p
        for p in reference_dir.rglob("*")
        if p.is_file() and not _is_volatile(p.relative_to(reference_dir))
    }
    cur_files = {
        p.relative_to(current_dir): p
        for p in current_dir.rglob("*")
        if p.is_file() and not _is_volatile(p.relative_to(current_dir))
    }

    # Compare file sets first (early-exit, no bytes loaded)
    if ref_files.keys() != cur_files.keys():
        return False

    # Stream-compare each file pair with early-exit (P2.12)
    for key in ref_files:
        if ref_files[key].read_bytes() != cur_files[key].read_bytes():
            return False

    return True
