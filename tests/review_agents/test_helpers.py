"""Tests for review_agents.helpers."""

import pytest
from pathlib import Path

from extraction_pipeline.review_agents.helpers import (
    REQUIRED_SECTIONS,
    load_draft,
    list_drafts,
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