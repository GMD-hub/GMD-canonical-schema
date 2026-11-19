"""The gates a set of variable records must pass.

Shared by the tests of the promoted records (knowledge/variables/, in
tests/test_knowledge_variables.py) and of the drafts (extraction/20_drafts/,
in tests/extraction/test_drafts.py). They implement the plan's V5
(frontmatter validation), V5b (7 body sections), C4 (no duplicate
variable_id), derivation-graph acyclicity, and the grep-based
welfare-leakage content scan (V6 substitute).
"""

from pathlib import Path
from typing import Any

from schema.frontmatter import load_markdown
from schema.missing import MissingDefinition, global_missing_ids
from schema.parameter import ParameterDefinition
from schema.variable import VariableDefinition

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
DRAFTS = ROOT / "extraction" / "20_drafts"

REQUIRED_SECTIONS = [
    "## Definition",
    "## Conceptual intent",
    "## Construction notes",
    "## Consistency checks",
    "## Escalation triggers",
    "## Common mistakes",
    "## Change log",
]


def knowledge_variables() -> list[Path]:
    return sorted((KNOWLEDGE / "variables").glob("*/VAR-*.md"))


def draft_variables() -> list[Path]:
    return sorted(DRAFTS.glob("*/VAR-*.md"))


def _drafted(pattern: str) -> list[Path]:
    return [
        path
        for path in sorted(DRAFTS.rglob(pattern))
        if "runs" not in path.relative_to(DRAFTS).parts
    ]


def missing_definitions(paths: list[Path]) -> dict[str, MissingDefinition]:
    return {
        path.stem: MissingDefinition.model_validate(load_markdown(path)[0])
        for path in paths
    }


def registered_missing() -> dict[str, MissingDefinition]:
    return missing_definitions(sorted((KNOWLEDGE / "missing").glob("MISS-*.md")))


def drafted_missing() -> dict[str, MissingDefinition]:
    return missing_definitions(_drafted("MISS-*.md"))


def reference_context(*, with_drafts: bool) -> dict[str, Any]:
    """What a variable's references resolve against.

    The promoted records resolve against knowledge/ alone. A draft resolves
    against knowledge/ plus whatever is drafted beside it: a draft rule,
    parameter, missing value definition or variable is cited by draft
    variables before it is promoted, and takes the place of its promoted
    version.
    """
    variables = knowledge_variables()
    parameters = sorted((KNOWLEDGE / "parameters").glob("PARAM-*.md"))
    rules = sorted((KNOWLEDGE / "rules").rglob("RULE-*.md"))
    missing = registered_missing()
    if with_drafts:
        variables = [*variables, *draft_variables()]
        parameters = [*parameters, *_drafted("PARAM-*.md")]
        rules = [*rules, *_drafted("RULE-*.md")]
        missing = {**missing, **drafted_missing()}
    return {
        "allow_unresolved_draft": True,
        "variable_ids": {path.stem for path in variables},
        "parameter_ids": {
            ParameterDefinition.model_validate(load_markdown(path)[0]).parameter_id
            for path in parameters
        },
        "rule_ids": {path.stem for path in rules},
        "missing_ids": set(missing),
        "global_missing_ids": global_missing_ids(list(missing.values())),
    }


def validate(path: Path, context: dict[str, Any]) -> VariableDefinition:
    return VariableDefinition.model_validate(load_markdown(path)[0], context=context)


def frontmatter_failures(paths: list[Path], context: dict[str, Any]) -> list[str]:
    failures = []
    for path in paths:
        try:
            validate(path, context)
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{path}: {exc}")
    return failures


def missing_sections(paths: list[Path]) -> list[str]:
    missing = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                missing.append(f"{path}: missing {section}")
    return missing


def duplicate_ids(paths: list[Path]) -> list[str]:
    ids = [path.stem for path in paths]
    return sorted({i for i in ids if ids.count(i) > 1})


def welfare_leakage(paths: list[Path]) -> list[str]:
    """Grep-based welfare-leakage content scan (V6 substitute).

    The pipeline's check_welfare_leakage_content requires structured
    citation objects not present in Markdown records, so this grep-based scan
    is the concrete substitute. It requires human sign-off (weaker than the
    content-based detector).
    """
    hits = []
    for path in paths:
        text = path.read_text(encoding="utf-8").lower()
        for needle in ("chapter8-cons", "chapter-8", "cons.qmd"):
            if needle in text:
                hits.append(f"{path}: {needle}")
    return hits


def long_labels(paths: list[Path], limit: int = 80) -> dict[str, int]:
    too_long = {}
    for path in paths:
        label = load_markdown(path)[0]["canonical_label"]
        if len(label) > limit:
            too_long[path.name] = len(label)
    return too_long
