"""Integration tests: full pipeline run against calibration drafts.

Validates agent output against known_answer_key.yml.
"""

import pytest
from pathlib import Path

import yaml

from extraction_pipeline.review_agents.consistency_derivation import check_drafts
from extraction_pipeline.review_agents.helpers import list_drafts, list_parameter_ids, write_findings
from extraction_pipeline.review_agents.models import AgentFindings
from extraction_pipeline.review_agents.rules_caveats import check_draft as rules_check
from extraction_pipeline.review_agents.run_all_agents import run
from extraction_pipeline.review_agents.schema_compliance import check_draft as schema_check
from extraction_pipeline.review_agents.source_grounding import check_draft as source_check

DRAFTS_DIR = Path("extraction/20_drafts")
REGISTRY_DIR = Path("knowledge/parameters")
ANSWER_KEY_PATH = Path(__file__).parent / "known_answer_key.yml"


@pytest.fixture
def answer_key():
    data = yaml.safe_load(ANSWER_KEY_PATH.read_text())
    return data or []


@pytest.fixture
def all_findings():
    draft_paths = list_drafts(DRAFTS_DIR)
    all_data = []
    for path in draft_paths:
        from extraction_pipeline.review_agents.helpers import load_draft
        data, _ = load_draft(path)
        all_data.append((path, data))

    variable_ids = {d.get("variable_id", "") for _, d in all_data if d.get("variable_id")}
    rule_ids = {r for _, d in all_data for r in d.get("rules", [])}
    parameter_ids, _ = list_parameter_ids(REGISTRY_DIR)

    findings: list[AgentFindings] = []
    for path, _ in all_data:
        findings.append(schema_check(path, variable_ids, parameter_ids=parameter_ids, rule_ids=rule_ids))
        findings.append(source_check(path))
        findings.append(rules_check(path))
    findings.extend(check_drafts(draft_paths))
    return findings


class TestKnownAnswerKey:
    def test_all_key_entries_matched(self, answer_key, all_findings):
        for entry in answer_key:
            artifact_id = entry["artifact_id"]
            agent = entry["agent"]
            field = entry["field"]
            severity = entry["severity"]
            message_contains = entry["message_contains"]

            matching_findings = [
                f
                for af in all_findings
                if af.artifact_id == artifact_id and af.agent == agent
                for f in af.findings
                if f.field == field
                and f.severity == severity
                and message_contains in f.message
            ]
            assert len(matching_findings) >= 1, (
                f"Known answer key entry not matched: "
                f"artifact={artifact_id}, agent={agent}, field={field}, "
                f"severity={severity}, message_contains={message_contains!r}"
            )


class TestFullPipeline:
    def test_runner_produces_summary(self, tmp_path):
        findings, exit_code = run(DRAFTS_DIR, tmp_path)
        summary_path = tmp_path / "SUMMARY.md"
        assert summary_path.exists()
        content = summary_path.read_text()
        assert "Agent Review Summary" in content
        assert "| " in content

    def test_runner_produces_yml_files(self, tmp_path):
        run(DRAFTS_DIR, tmp_path)
        yml_files = list(tmp_path.glob("*.yml"))
        assert len(yml_files) >= 6

    def test_runner_exit_code(self, tmp_path):
        _, exit_code = run(DRAFTS_DIR, tmp_path)
        assert exit_code == 1, "Expected exit code 1 due to known errors in non-variable calibration files"