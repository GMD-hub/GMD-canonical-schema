"""The missing value definitions registered under knowledge/missing/."""

from pathlib import Path

from schema.frontmatter import load_markdown
from schema.missing import MissingDefinition, validate_missing_set

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "knowledge" / "missing"


def test_registered_missing_definitions_validate() -> None:
    paths = sorted(REGISTRY.glob("MISS-*.md"))
    assert paths, "no missing value definitions found under knowledge/missing/"
    definitions = []
    for path in paths:
        definition = MissingDefinition.model_validate(load_markdown(path)[0])
        assert definition.missing_id == path.stem
        definitions.append(definition)
    validate_missing_set(definitions)


def test_every_registered_missing_file_is_a_definition() -> None:
    strays = sorted(
        path.name for path in REGISTRY.rglob("*.md") if not path.name.startswith("MISS-")
    )
    assert not strays, f"not a missing value definition: {strays}"
