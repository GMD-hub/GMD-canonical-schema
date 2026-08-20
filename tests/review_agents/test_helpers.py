"""Tests for review_agents.helpers."""

import pytest
from pathlib import Path

from extraction_pipeline.review_agents.helpers import (
    EXCLUDE_DIRS,
    REQUIRED_SECTIONS,
    load_draft,
    list_drafts,
    list_parameter_ids,
    write_findings,
    make_findings,
)
from extraction_pipeline.review_agents.models import Finding


class TestLoadDraft:
    def test_loads_valid_frontmatter(self, tmp_path):
        p = tmp_path / "test.md"
        p.write_text("---\nvariable_id: VAR-male\nstatus: draft\n---\n\nBody text\n")
        data, body = load_draft(p)
        assert data["variable_id"] == "VAR-male"
        assert "Body text" in body

    def test_missing_frontmatter_raises(self, tmp_path):
        p = tmp_path / "test.md"
        p.write_text("# No front matter\n")
        with pytest.raises(ValueError, match="does not start"):
            load_draft(p)

    def test_unterminated_frontmatter_raises(self, tmp_path):
        p = tmp_path / "test.md"
        p.write_text("---\nvariable_id: VAR-male\n")
        with pytest.raises(ValueError, match="unterminated"):
            load_draft(p)

    def test_yaml_comments_handled(self, tmp_path):
        p = tmp_path / "test.md"
        p.write_text("---\n# comment\nvariable_id: VAR-test\n---\n\nBody\n")
        data, body = load_draft(p)
        assert data["variable_id"] == "VAR-test"


class TestListDrafts:
    def test_finds_md_files(self, tmp_path):
        (tmp_path / "a.md").write_text("a")
        (tmp_path / "b.txt").write_text("b")
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "c.md").write_text("c")
        results = list_drafts(tmp_path)
        assert len(results) == 2
        assert all(p.suffix == ".md" for p in results)

    def test_empty_dir(self, tmp_path):
        assert list_drafts(tmp_path) == []

    def test_excludes_runs_and_project_documentation(self, tmp_path):
        (tmp_path / "VAR-x.md").write_text("x")
        runs_dir = tmp_path / "runs"
        runs_dir.mkdir()
        (runs_dir / "inventory.md").write_text("inv")
        proj_dir = tmp_path / "project-documentation"
        proj_dir.mkdir()
        (proj_dir / "wiki.md").write_text("wiki")
        results = list_drafts(tmp_path)
        assert [p.name for p in results] == ["VAR-x.md"]

    def test_excludes_nested_excluded_dirs(self, tmp_path):
        (tmp_path / "VAR-x.md").write_text("x")
        nested = tmp_path / "dem" / "runs"
        nested.mkdir(parents=True)
        (nested / "tracking.md").write_text("tracking")
        (tmp_path / "dem" / "VAR-y.md").write_text("y")
        results = list_drafts(tmp_path)
        assert sorted(p.name for p in results) == ["VAR-x.md", "VAR-y.md"]

    def test_excludes_nested_project_documentation(self, tmp_path):
        (tmp_path / "VAR-x.md").write_text("x")
        nested = tmp_path / "dem" / "project-documentation"
        nested.mkdir(parents=True)
        (nested / "process.md").write_text("process")
        (tmp_path / "dem" / "VAR-y.md").write_text("y")
        results = list_drafts(tmp_path)
        assert sorted(p.name for p in results) == ["VAR-x.md", "VAR-y.md"]

    def test_case_variant_not_excluded_is_documented_behavior(self, tmp_path):
        (tmp_path / "VAR-x.md").write_text("x")
        case_dir = tmp_path / "Runs"
        case_dir.mkdir()
        (case_dir / "tracking.md").write_text("tracking")
        results = list_drafts(tmp_path)
        assert sorted(p.name for p in results) == ["VAR-x.md", "tracking.md"], (
            "EXCLUDE_DIRS matching is case-sensitive exact; a case variant "
            "(e.g. Runs/) is retained by documented convention"
        )

    def test_exclude_set_matches_asymmetry_tool(self):
        assert EXCLUDE_DIRS == {"project-documentation", "runs"}


class TestWriteFindings:
    def test_creates_yaml_file(self, tmp_path):
        af = make_findings(
            "test_agent", "VAR-male",
            [Finding(field="x", severity="error", message="bad")],
        )
        path = write_findings(af, tmp_path)
        assert path.exists()
        assert path.name == "VAR-male.test_agent.yml"


class TestMakeFindings:
    def test_summary_computed(self):
        findings = [
            Finding(field="a", severity="error", message="e"),
            Finding(field="b", severity="warning", message="w"),
            Finding(field="c", severity="warning", message="w2"),
        ]
        af = make_findings("agent", "VAR-x", findings)
        assert af.summary.errors == 1
        assert af.summary.warnings == 2
        assert af.summary.passed == 0

    def test_no_findings_is_passed(self):
        af = make_findings("agent", "VAR-x", [])
        assert af.summary.errors == 0
        assert af.summary.warnings == 0
        assert af.summary.passed == 1


class TestRequiredSections:
    def test_seven_sections(self):
        assert len(REQUIRED_SECTIONS) == 7
        assert "Definition" in REQUIRED_SECTIONS
        assert "Change log" in REQUIRED_SECTIONS


class TestListParameterIds:
    def test_nonexistent_dir(self, tmp_path):
        ids, skipped = list_parameter_ids(tmp_path / "nonexistent")
        assert ids == set()
        assert skipped == []

    def test_empty_dir(self, tmp_path):
        ids, skipped = list_parameter_ids(tmp_path)
        assert ids == set()
        assert skipped == []

    def test_valid_registry(self, tmp_path):
        (tmp_path / "PARAM-X-TEST.md").write_text(
            "---\nparameter_id: PARAM-X-TEST\n---\n\nBody\n"
        )
        ids, skipped = list_parameter_ids(tmp_path)
        assert "PARAM-X-TEST" in ids
        assert skipped == []

    def test_file_without_parameter_id(self, tmp_path):
        (tmp_path / "bad.md").write_text(
            "---\nvariable_id: VAR-x\n---\n\nBody\n"
        )
        ids, skipped = list_parameter_ids(tmp_path)
        assert ids == set()
        assert len(skipped) == 1
        assert "bad.md" in skipped[0]

    def test_malformed_yaml(self, tmp_path):
        (tmp_path / "broken.md").write_text("not valid yaml\n---\n")
        ids, skipped = list_parameter_ids(tmp_path)
        assert ids == set()
        assert len(skipped) == 1
        assert "broken.md" in skipped[0]