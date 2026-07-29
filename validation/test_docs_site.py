from pathlib import Path
import unittest

from mkdocs.config import load_config


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SITE = ROOT / "site"


def flatten_nav(items: list[object]) -> set[str]:
    pages: set[str] = set()
    for item in items:
        if isinstance(item, str):
            pages.add(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    pages.add(value)
                else:
                    pages.update(flatten_nav(value))
    return pages


class DocumentationSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = load_config(config_file=str(ROOT / "mkdocs.yml"))

    def test_every_wiki_page_is_in_navigation(self) -> None:
        source_pages = {
            path.relative_to(WIKI).as_posix() for path in WIKI.rglob("*.md")
        }
        self.assertEqual(source_pages, flatten_nav(self.config.nav))

    def test_homepage_has_no_case_variant_aliases(self) -> None:
        wiki_entries = {path.name for path in WIKI.iterdir()}
        self.assertIn("index.md", wiki_entries)
        self.assertNotIn("Home.md", wiki_entries)
        self.assertNotIn("Index.md", wiki_entries)

    def test_concept_guides_include_examples(self) -> None:
        concept_guides = {
            "index.md",
            "Architecture.md",
            "Repository-Map.md",
            "Artifact-Model.md",
            "Artifact-Lifecycle.md",
            "Country-Parameter-Layer.md",
            "Validation-and-Builds.md",
            "Governance-and-Contributing.md",
            "Glossary.md",
        }
        for filename in concept_guides:
            with self.subTest(filename=filename):
                content = (WIKI / filename).read_text(encoding="utf-8").lower()
                self.assertIn("example", content)

    def test_hypothetical_country_exception_is_unambiguous(self) -> None:
        content = (WIKI / "Country-Parameter-Layer.md").read_text(encoding="utf-8")
        self.assertIn("Hypothetical only", content)
        self.assertIn("not facts about any country or survey", content)
        self.assertIn("human_reviewed: false", content)

    def test_build_has_pages_search_and_diagrams(self) -> None:
        self.assertTrue((SITE / "index.html").is_file())
        self.assertTrue((SITE / "search" / "search_index.json").is_file())
        architecture = (SITE / "Architecture" / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertEqual(architecture.count('class="gmd-diagram"'), 3)
        diagram_assets = SITE / "assets" / "diagrams"
        self.assertEqual(len(list(diagram_assets.glob("*.svg"))), 4)

    def test_card_icons_render_without_leaking_shortcodes(self) -> None:
        card_pages = {
            "home": SITE / "index.html",
            "learning paths": SITE / "Learning-Paths" / "index.html",
        }
        for page_name, page_path in card_pages.items():
            with self.subTest(page=page_name):
                content = page_path.read_text(encoding="utf-8")
                self.assertNotIn(":material-", content)
                self.assertNotIn("{ .lg .middle }", content)
                self.assertIn('class="twemoji', content)


if __name__ == "__main__":
    unittest.main()