from pathlib import Path

import yaml

from extraction_pipeline.country_inputs import cli


def _write_markdown_parameter(path: Path, parameter_id: str) -> None:
    front_matter = {
        "parameter_id": parameter_id,
        "parameter_name": "Legacy placeholder",
        "module_id": "MOD-DEM",
        "schema_version": "0.1",
        "status": "draft",
        "authority": "GPID Team",
        "kind": "construction",
        "value_type": "mapping",
        "value_schema": {"x": "integer"},
        "applies_to_variables": ["VAR-age"],
        "fallback_policy": "undecided",
        "global_default": None,
        "provenance": {
            "source_document": "x",
            "extraction_method": "manual",
            "extracted_on": "2026-09-04",
            "human_reviewed": False,
            "reviewer": None,
            "notes": "x",
        },
    }
    text = yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=False)
    path.write_text(f"---\n{text}---\n\nbody\n", encoding="utf-8")


def _write_contract(path: Path) -> None:
    contract = {
        "parameter_id": "PARAM-EDU-LEVEL-CROSSWALK",
        "parameter_name": "Education crosswalk",
        "module_id": "MOD-EDU",
        "schema_version": "0.2",
        "status": "draft",
        "authority": "GPID Team",
        "kind": "construction",
        "value_type": "table",
        "row_schema": {
            "country_entry_id": "string",
            "national_label_en": "string",
            "national_label_local": "string",
            "entry_age": "integer",
            "duration_years": "integer",
            "isced_level": "string",
            "isced_label": "string",
            "gmd_educat4_target": "string",
            "gmd_educat5_target": "string",
            "gmd_educat7_target": "string",
            "source_row": "integer",
        },
        "applies_to_variables": ["VAR-educat4"],
        "fallback_policy": "block_and_escalate",
        "global_default": None,
        "provenance": {
            "source_document": "GMD_household_survey_harmonization.md",
            "extraction_method": "manual",
            "extracted_on": "2026-09-04",
            "human_reviewed": False,
            "reviewer": None,
            "notes": "draft",
        },
    }
    path.write_text(yaml.safe_dump(contract, sort_keys=False, allow_unicode=False), encoding="utf-8")


def _write_valid_draft(path: Path) -> None:
    payload = {
        "country_id": "CTY-VNM",
        "country_name": "Viet Nam",
        "iso3": "VNM",
        "schema_version": "0.2",
        "status": "draft",
        "parameters": [
            {
                "parameter_id": "PARAM-EDU-LEVEL-CROSSWALK",
                "effective_from": 2023,
                "effective_to": None,
                "selectors": None,
                "value": [
                    {
                        "country_entry_id": "VNM-EDU-01",
                        "national_label_en": "Primary",
                        "national_label_local": "Tieu hoc",
                        "entry_age": 6,
                        "duration_years": 5,
                        "isced_level": "1",
                        "isced_label": "ISCED 1 Primary",
                        "gmd_educat4_target": "primary",
                        "gmd_educat5_target": "primary_complete",
                        "gmd_educat7_target": "primary_complete",
                        "source_row": 9,
                    }
                ],
                "provenance": {
                    "source": "x.xlsx",
                    "verified_on": None,
                    "human_reviewed": False,
                    "reviewer": None,
                },
            }
        ],
    }
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=False), encoding="utf-8")


def _setup_layout(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    (root / "knowledge" / "parameters").mkdir(parents=True)
    (root / "extraction" / "20_drafts" / "runs" / "country-parameters" / "contracts").mkdir(
        parents=True
    )
    (root / "extraction" / "20_drafts" / "runs" / "country-parameters" / "VNM").mkdir(
        parents=True
    )
    _write_markdown_parameter(
        root / "knowledge" / "parameters" / "PARAM-DEM-MIN-MARRIAGE-AGE.md",
        "PARAM-DEM-MIN-MARRIAGE-AGE",
    )
    return root


def test_run_check_validates_schema_using_draft_contracts(tmp_path: Path, monkeypatch) -> None:
    root = _setup_layout(tmp_path)
    _write_contract(
        root
        / "extraction"
        / "20_drafts"
        / "runs"
        / "country-parameters"
        / "contracts"
        / "PARAM-EDU-LEVEL-CROSSWALK.yaml"
    )
    _write_valid_draft(
        root
        / "extraction"
        / "20_drafts"
        / "runs"
        / "country-parameters"
        / "VNM"
        / "PARAM-EDU-LEVEL-CROSSWALK.yaml"
    )

    monkeypatch.setattr(cli, "ROOT", root)
    monkeypatch.setattr(
        cli,
        "DRAFT_ROOT",
        root / "extraction" / "20_drafts" / "runs" / "country-parameters",
    )
    monkeypatch.setattr(cli, "CONTRACT_ROOT", cli.DRAFT_ROOT / "contracts")

    result = cli.run_check()
    assert result["ok"] is True
    assert result["count"] == 1
    assert result["errors"] == []


def test_run_check_fails_on_unknown_parameter(tmp_path: Path, monkeypatch) -> None:
    root = _setup_layout(tmp_path)
    _write_valid_draft(
        root
        / "extraction"
        / "20_drafts"
        / "runs"
        / "country-parameters"
        / "VNM"
        / "PARAM-EDU-LEVEL-CROSSWALK.yaml"
    )

    monkeypatch.setattr(cli, "ROOT", root)
    monkeypatch.setattr(
        cli,
        "DRAFT_ROOT",
        root / "extraction" / "20_drafts" / "runs" / "country-parameters",
    )
    monkeypatch.setattr(cli, "CONTRACT_ROOT", cli.DRAFT_ROOT / "contracts")

    result = cli.run_check()
    assert result["ok"] is False
    assert result["count"] == 1
    assert any("unknown parameter_id" in item["error"] for item in result["errors"])
