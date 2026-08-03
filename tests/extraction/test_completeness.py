"""Tests for completeness and reproducibility — Phase 6."""

from pathlib import Path

from extraction_pipeline.reports import (
    build_completeness_report,
    check_no_duplicate_ids,
    check_no_welfare_leakage,
    check_welfare_leakage_content,
    compare_runs,
)
from extraction_pipeline.state import ExtractionState, ItemState, RunState


class TestCompleteness:
    def test_all_disposed(self) -> None:
        run_state = RunState(
            execution_id="exec-001",
            items={
                "INV-001": ItemState(inventory_id="INV-001", state=ExtractionState.CANONICAL),
                "INV-002": ItemState(inventory_id="INV-002", state=ExtractionState.BLOCKED, issue_ids=["ISS-001"]),
            },
        )
        report = build_completeness_report(["INV-001", "INV-002"], run_state)
        assert report.complete
        assert report.canonical_count == 1
        assert report.blocked_count == 1
        assert report.undisposed_count == 0

    def test_undisposed_item(self) -> None:
        run_state = RunState(
            execution_id="exec-001",
            items={
                "INV-001": ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED),
            },
        )
        report = build_completeness_report(["INV-001", "INV-002"], run_state)
        assert not report.complete
        assert "INV-002" in report.undisposed_ids


class TestWelfareLeakage:
    def test_no_leakage(self) -> None:
        ids = ["INV-IDN-001", "INV-GEO-002", "INV-DEM-003"]
        assert check_no_welfare_leakage(ids)

    def test_leakage_detected(self) -> None:
        ids = ["INV-IDN-001", "INV-CONS-002"]
        assert not check_no_welfare_leakage(ids)


class TestWelfareLeakageContent:
    """Content-based welfare leakage detector (P0.4 fix)."""

    def test_no_leakage_when_no_cons_citations(self) -> None:
        """Candidates citing only non-CONS sources must not be flagged."""
        candidates = [
            {
                "inventory_id": "INV-IDN-001",
                "evidence_ids": {"canonical_label": ["CIT-001"]},
            },
            {
                "inventory_id": "INV-UTL-014",
                "evidence_ids": {"canonical_label": ["CIT-002"]},
            },
        ]
        citations_by_id = {
            "CIT-001": {"source_path": "chapter2-IDN.qmd"},
            "CIT-002": {"source_path": "chapter6-UTL.qmd"},
        }
        report = check_welfare_leakage_content(candidates, citations_by_id)
        assert not report["leaked"]
        assert report["leaked_ids"] == []
        assert report["detector_version"] == "v1-content"

    def test_leakage_detected_via_cons_citation(self) -> None:
        """A non-CONS ID citing chapter8-CONS.qmd must be flagged (content-based)."""
        candidates = [
            {
                "inventory_id": "INV-UTL-014",
                "evidence_ids": {"canonical_label": ["CIT-001", "CIT-002"]},
            },
        ]
        citations_by_id = {
            "CIT-001": {"source_path": "chapter6-UTL.qmd"},
            "CIT-002": {"source_path": "chapter8-CONS.qmd"},
        }
        report = check_welfare_leakage_content(candidates, citations_by_id)
        assert report["leaked"]
        assert "INV-UTL-014" in report["leaked_ids"]

    def test_leakage_detected_for_cons_id(self) -> None:
        """A CONS-ID candidate citing chapter8 must also be flagged."""
        candidates = [
            {
                "inventory_id": "INV-CONS-002",
                "evidence_ids": {"canonical_label": ["CIT-001"]},
            },
        ]
        citations_by_id = {
            "CIT-001": {"source_path": "chapter8-CONS.qmd"},
        }
        report = check_welfare_leakage_content(candidates, citations_by_id)
        assert report["leaked"]
        assert "INV-CONS-002" in report["leaked_ids"]

    def test_no_false_positive_on_cons_substring_in_id(self) -> None:
        """An ID containing 'CONS' as substring but citing non-CONS must NOT be flagged."""
        candidates = [
            {
                "inventory_id": "INV-CONSULTATION-001",
                "evidence_ids": {"canonical_label": ["CIT-001"]},
            },
        ]
        citations_by_id = {
            "CIT-001": {"source_path": "chapter2-IDN.qmd"},
        }
        report = check_welfare_leakage_content(candidates, citations_by_id)
        assert not report["leaked"]
        assert report["leaked_ids"] == []

    def test_missing_citation_id_skipped(self) -> None:
        """A citation ID not in citations_by_id is skipped, not treated as leakage."""
        candidates = [
            {
                "inventory_id": "INV-IDN-001",
                "evidence_ids": {"canonical_label": ["CIT-UNKNOWN"]},
            },
        ]
        citations_by_id = {}
        report = check_welfare_leakage_content(candidates, citations_by_id)
        assert not report["leaked"]

    def test_multiple_leaked_ids(self) -> None:
        """Multiple candidates citing CONS must all be flagged."""
        candidates = [
            {
                "inventory_id": "INV-UTL-014",
                "evidence_ids": {"canonical_label": ["CIT-001"]},
            },
            {
                "inventory_id": "INV-DWL-007",
                "evidence_ids": {"canonical_label": ["CIT-002"]},
            },
        ]
        citations_by_id = {
            "CIT-001": {"source_path": "chapter8-CONS.qmd"},
            "CIT-002": {"source_path": "chapter8-CONS.qmd"},
        }
        report = check_welfare_leakage_content(candidates, citations_by_id)
        assert report["leaked"]
        assert set(report["leaked_ids"]) == {"INV-UTL-014", "INV-DWL-007"}


class TestDuplicateIds:
    def test_no_duplicates(self) -> None:
        assert check_no_duplicate_ids(["INV-001", "INV-002", "INV-003"])

    def test_duplicates_detected(self) -> None:
        assert not check_no_duplicate_ids(["INV-001", "INV-002", "INV-001"])


class TestCompareRuns:
    def test_identical(self, tmp_path: Path) -> None:
        ref = tmp_path / "ref"
        cur = tmp_path / "cur"
        (ref / "data.json").parent.mkdir(parents=True, exist_ok=True)
        (cur / "data.json").parent.mkdir(parents=True, exist_ok=True)
        (ref / "data.json").write_text('{"x":1}', encoding="utf-8")
        (cur / "data.json").write_text('{"x":1}', encoding="utf-8")
        assert compare_runs(ref, cur)

    def test_different_content(self, tmp_path: Path) -> None:
        ref = tmp_path / "ref"
        cur = tmp_path / "cur"
        (ref / "data.json").parent.mkdir(parents=True, exist_ok=True)
        (cur / "data.json").parent.mkdir(parents=True, exist_ok=True)
        (ref / "data.json").write_text('{"x":1}', encoding="utf-8")
        (cur / "data.json").write_text('{"x":2}', encoding="utf-8")
        assert not compare_runs(ref, cur)

    def test_missing_reference_dir_returns_false(self, tmp_path: Path) -> None:
        cur = tmp_path / "cur"
        (cur / "data.json").parent.mkdir(parents=True, exist_ok=True)
        (cur / "data.json").write_text('{"x":1}', encoding="utf-8")
        assert not compare_runs(tmp_path / "nonexistent-ref", cur)

    def test_missing_current_dir_returns_false(self, tmp_path: Path) -> None:
        ref = tmp_path / "ref"
        (ref / "data.json").parent.mkdir(parents=True, exist_ok=True)
        (ref / "data.json").write_text('{"x":1}', encoding="utf-8")
        assert not compare_runs(ref, tmp_path / "nonexistent-cur")

    def test_different_file_sets_return_false(self, tmp_path: Path) -> None:
        ref = tmp_path / "ref"
        cur = tmp_path / "cur"
        (ref / "a.json").parent.mkdir(parents=True, exist_ok=True)
        (cur / "b.json").parent.mkdir(parents=True, exist_ok=True)
        (ref / "a.json").write_text('{"x":1}', encoding="utf-8")
        (cur / "b.json").write_text('{"x":1}', encoding="utf-8")
        assert not compare_runs(ref, cur)

    def test_run_ledger_excluded_from_comparison(self, tmp_path: Path) -> None:
        """Volatile run-ledger files must not participate in byte comparison."""
        ref = tmp_path / "ref"
        cur = tmp_path / "cur"
        (ref / "content.json").parent.mkdir(parents=True, exist_ok=True)
        (cur / "content.json").parent.mkdir(parents=True, exist_ok=True)
        (ref / "content.json").write_text('{"x":1}', encoding="utf-8")
        (cur / "content.json").write_text('{"x":1}', encoding="utf-8")
        # Differing run-ledger files must NOT cause comparison to fail.
        (ref / "run-ledger.json").write_text('{"ts":"ref"}', encoding="utf-8")
        (cur / "run-ledger.json").write_text('{"ts":"cur"}', encoding="utf-8")
        assert compare_runs(ref, cur)
