"""Tests for review_agents.consistency_derivation agent."""

import pytest
from pathlib import Path

from extraction_pipeline.review_agents.consistency_derivation import check_drafts


DRAFTS_DIR = Path("extraction/20_drafts")


class TestConsistencyDerivation:
    def test_all_drafts(self):
        draft_paths = sorted(DRAFTS_DIR.rglob("*.md"))
        results = check_drafts(draft_paths)
        by_id = {r.artifact_id: r for r in results}
        assert "VAR-educy" in by_id
        assert "VAR-male" in by_id

    def test_educy_no_asymmetry_error(self):
        draft_paths = sorted(DRAFTS_DIR.rglob("*.md"))
        results = check_drafts(draft_paths)
        by_id = {r.artifact_id: r for r in results}
        educy = by_id["VAR-educy"]
        asymmetry = [f for f in educy.findings if "Asymmetry" in f.message]
        assert asymmetry == [], (
            "VAR-educy should have no asymmetry errors after the derivation "
            f"graph repair; found: {[f.message for f in asymmetry]}"
        )

    def test_male_no_derivation_issues(self):
        draft_paths = sorted(DRAFTS_DIR.rglob("*.md"))
        results = check_drafts(draft_paths)
        by_id = {r.artifact_id: r for r in results}
        male = by_id["VAR-male"]
        errors = [f for f in male.findings if f.severity == "error"]
        assert errors == [], f"Unexpected errors: {[f.message for f in errors]}"

    def test_educy_value_codes_null_no_warning(self):
        draft_paths = sorted(DRAFTS_DIR.rglob("*.md"))
        results = check_drafts(draft_paths)
        by_id = {r.artifact_id: r for r in results}
        educy = by_id["VAR-educy"]
        value_code_warnings = [f for f in educy.findings if "Value codes" in f.message]
        assert value_code_warnings == [], "educy has value_codes: null, should not trigger subset check"

    def test_urban_unresolved_derivation_ref(self):
        draft_paths = sorted(DRAFTS_DIR.rglob("*.md"))
        results = check_drafts(draft_paths)
        by_id = {r.artifact_id: r for r in results}
        urban = by_id["VAR-urban"]
        unresolved = [f for f in urban.findings if "VAR-rurality" in f.message and "not found" in f.message]
        assert len(unresolved) >= 1
        assert unresolved[0].severity == "warning"