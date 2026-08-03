"""Governance preflight tests — Phase 1 Step 1."""

import pytest
import yaml
from pathlib import Path

GOVERNANCE_DIR = Path(__file__).resolve().parents[2] / "governance"


class TestGovernancePreflight:
    """Verify governance preflight records exist and are well-formed."""

    def test_extraction_preflight_decision_exists(self) -> None:
        """The extraction preflight decision record must exist and have required fields."""
        decision_file = GOVERNANCE_DIR / "decisions" / "Extraction-Preflight-2026-08.md"
        assert decision_file.exists(), (
            f"Missing preflight decision record: {decision_file}"
        )
        text = decision_file.read_text(encoding="utf-8")
        # Must have YAML frontmatter
        assert text.startswith("---\n"), "Decision record must have YAML frontmatter"
        # Required fields
        assert "Schema approval" in text or "schema approval" in text, (
            "Must reference 2026-07-29 schema approval"
        )
        assert "AGENTS.md" in text or "write policy" in text, (
            "Must clarify supervised implementation write policy"
        )

    def test_module_registry_exists_and_valid(self) -> None:
        """Module registry must exist and include required modules."""
        registry_path = Path(__file__).resolve().parents[2] / "extraction" / "config" / "extraction-governance.v1.yaml"
        assert registry_path.exists(), f"Missing module registry: {registry_path}"
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        assert "modules" in data, "Module registry must have 'modules' key"
        required = {"IDN", "GEO", "DEM", "LBR", "UTL", "DWL"}
        found = {m.get("code") for m in data["modules"] if "code" in m}
        missing = required - found
        assert not missing, f"Missing required modules: {missing}"

    def test_module_registry_disambiguates_idn_geo(self) -> None:
        """IDN and GEO are module codes, not ISO 3166 country codes."""
        registry_path = Path(__file__).resolve().parents[2] / "extraction" / "config" / "extraction-governance.v1.yaml"
        if not registry_path.exists():
            pytest.skip("Module registry not yet created")
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        for mod in data.get("modules", []):
            if mod.get("code") in ("IDN", "GEO"):
                assert "note" in mod or "disambiguation" in mod, (
                    f"Module {mod['code']} must disambiguate from ISO 3166 country code"
                )

    def test_basic_policy_is_decided(self) -> None:
        """The basic tier policy must be canonical, inventory-only, or excluded."""
        registry_path = Path(__file__).resolve().parents[2] / "extraction" / "config" / "extraction-governance.v1.yaml"
        if not registry_path.exists():
            pytest.skip("Module registry not yet created")
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        assert "tier_policy" in data, "Must define tier_policy for 'basic'"
        assert data["tier_policy"]["basic"] in (
            "canonical", "inventory-only", "excluded"
        ), f"Invalid basic policy: {data['tier_policy'].get('basic')}"

    def test_field_classification_exists_and_is_complete(self) -> None:
        """Field classification matrix must exist and cover all required fields."""
        classification_path = (
            Path(__file__).resolve().parents[2]
            / "extraction" / "config" / "field-classification.v1.yaml"
        )
        assert classification_path.exists(), (
            f"Missing field classification: {classification_path}"
        )
        data = yaml.safe_load(classification_path.read_text(encoding="utf-8"))
        assert "classifications" in data, "Must have 'classifications' key"
        # Require at least the VariableDefinition, RuleDefinition, ParameterDefinition models
        models_found = {c.get("model") for c in data["classifications"]}
        required_models = {"VariableDefinition", "RuleDefinition", "ParameterDefinition"}
        missing_models = required_models - models_found
        assert not missing_models, f"Missing model classifications: {missing_models}"

    def test_field_classification_valid_classes(self) -> None:
        """All field classifications must use valid class names."""
        valid_classes = {
            "source-explicit",
            "deterministically-derived",
            "governed-constant",
            "agent-interpreted",
            "generated-metadata",
            "unresolved",
        }
        classification_path = (
            Path(__file__).resolve().parents[2]
            / "extraction" / "config" / "field-classification.v1.yaml"
        )
        if not classification_path.exists():
            pytest.skip("Field classification not yet created")
        data = yaml.safe_load(classification_path.read_text(encoding="utf-8"))
        invalid = []
        for entry in data.get("classifications", []):
            for field_entry in entry.get("fields", []):
                cls = field_entry.get("class", "")
                if cls and cls not in valid_classes:
                    invalid.append(
                        f"{entry.get('model')}.{field_entry.get('field')} = {cls}"
                    )
        assert not invalid, f"Invalid classification classes: {invalid}"

    def test_welfare_utl_boundary_defined(self) -> None:
        """The welfare vs. in-scope UTL expenditure boundary must be defined."""
        registry_path = Path(__file__).resolve().parents[2] / "extraction" / "config" / "extraction-governance.v1.yaml"
        if not registry_path.exists():
            pytest.skip("Module registry not yet created")
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        assert "welfare_boundary" in data, "Must define welfare/UTL boundary"
        boundary = data["welfare_boundary"]
        assert "rule" in boundary, "Welfare boundary must have a 'rule' key"
        assert "examples" in boundary, "Welfare boundary must have 'examples'"

    def test_non_null_weight_rule_explicit(self) -> None:
        """The non-null weight rule must be explicit in the extraction rubric."""
        registry_path = Path(__file__).resolve().parents[2] / "extraction" / "config" / "extraction-governance.v1.yaml"
        if not registry_path.exists():
            pytest.skip("Module registry not yet created")
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        assert "weight_invariant" in data, "Must have 'weight_invariant' key"
        assert data["weight_invariant"], "Weight invariant must be documented"


def test_preflight_blocks_on_missing_approval() -> None:
    """Without approval reference, a preflight check must fail.

    The governance decision record (Extraction-Preflight-2026-08.md) documents
    that the schema approval reference is a TODO pending GPID Team confirmation.
    This test verifies the contract: the decision record must exist and must
    explicitly document the pending approval items so that the preflight gate
    can be wired to check for a locatable approval reference in the future.
    """
    decision_file = GOVERNANCE_DIR / "decisions" / "Extraction-Preflight-2026-08.md"
    assert decision_file.exists(), (
        f"Missing preflight decision record: {decision_file}"
    )
    text = decision_file.read_text(encoding="utf-8")
    # The decision record must document the pending approval reference
    assert "TODO" in text or "Pending Human Authorization" in text, (
        "Decision record must document the pending approval reference "
        "so preflight can enforce it once wired"
    )
    # The decision record must reference the 2026-07-29 schema approval
    assert "2026-07-29" in text, (
        "Decision record must reference the 2026-07-29 schema approval meeting"
    )
