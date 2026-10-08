"""
Tests for gmd_wash_concordance.

The workbook-dependent tests are skipped unless a JMP country file is present.
Point GMD_JMP_DIR at a directory of them, or drop them in ./samples/.

    python3 tests/test_wash.py
    GMD_JMP_DIR=/path/to/files python3 tests/test_wash.py
"""
import glob
import json
import shutil
import urllib.error
import urllib.request
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from gmd_wash_concordance import check, extract, master          # noqa: E402
from gmd_wash_concordance.validate import validate as run_rules  # noqa: E402
from gmd_wash_concordance.reader import load_profile, read, slug  # noqa: E402
from gmd_wash_concordance import benchmark as BM
from gmd_wash_concordance import countries as CO
from gmd_wash_concordance import registry as REG
from gmd_wash_concordance import review as RV
from gmd_wash_concordance import translate as TR
from gmd_wash_concordance import viewer as V
from gmd_wash_concordance.viewer import build as build_viewer    # noqa: E402
from gmd_wash_concordance.schema import (                          # noqa: E402
    GMD_SANITATION_TYPES, GMD_WATER_SOURCES, SAN_LADDER, WATER_LADDER,
)

SAMPLE_DIRS = [os.environ.get("GMD_JMP_DIR"),
               os.path.join(os.path.dirname(__file__), "..", "samples"),
               os.path.dirname(__file__)]


def find_all(d):
    out = []
    for root, _dirs, files in os.walk(d):
        out += [os.path.join(root, f) for f in files]
    return out


def find_workbooks():
    for d in SAMPLE_DIRS:
        if not d or not os.path.isdir(d):
            continue
        hits = sorted(glob.glob(os.path.join(d, "JMP_*.xlsx")))
        if hits:
            return hits
    return []


WB = find_workbooks()
needs_wb = unittest.skipUnless(WB, "no JMP workbook found; set GMD_JMP_DIR")


class TestMaster(unittest.TestCase):
    def test_tree_sizes(self):
        self.assertEqual(len(master.water()), 73)
        self.assertEqual(len(master.sanitation()), 80)

    def test_every_improved_class_feeds_a_facility_type(self):
        """The chain classification -> subgroup -> facility type must close for
        anything JMP counts as improved."""
        for tree in (master.water(), master.sanitation()):
            for n in tree.nodes:
                if n.improved is True:
                    self.assertIn("Improved", n.rolls_up_to,
                                  f"{n.path} is improved but feeds nothing")

    def test_nothing_unimproved_rolls_into_improved(self):
        for tree in (master.water(), master.sanitation()):
            for n in tree.nodes:
                if n.improved is not True:
                    self.assertNotIn("Improved", n.rolls_up_to, n.path)

    def test_rollups_name_only_declared_facility_types(self):
        for tree in (master.water(), master.sanitation()):
            declared = set(tree.facility_types)
            for n in tree.nodes:
                self.assertLessEqual(set(n.rolls_up_to), declared, n.path)

    def test_water_improved_is_all_piped_plus_non_piped(self):
        w = master.water()
        imp = {n.id for n in w.nodes if "Improved" in n.rolls_up_to}
        split = {n.id for n in w.nodes
                 if "All piped" in n.rolls_up_to or "Non-piped" in n.rolls_up_to}
        self.assertEqual(imp, split)

    def test_piped_on_premises_is_inside_all_piped(self):
        w = master.water()
        for n in w.nodes:
            if "Piped on premises" in n.rolls_up_to:
                self.assertIn("All piped", n.rolls_up_to, n.path)

    def test_every_node_has_a_target_or_spans_or_is_structural(self):
        for tree in (master.water(), master.sanitation()):
            for n in tree.nodes:
                self.assertTrue(n.gmd or n.spans or n.structural,
                                f"{n.path} has neither target nor spans")

    def test_targets_are_in_the_controlled_lists(self):
        self.assertLessEqual(set(master.water().gmd_targets()),
                             set(GMD_WATER_SOURCES))
        self.assertLessEqual(set(master.sanitation().gmd_targets()),
                             set(GMD_SANITATION_TYPES))

    def test_node_ids_are_unique(self):
        for tree in (master.water(), master.sanitation()):
            ids = [n.id for n in tree.nodes]
            self.assertEqual(len(ids), len(set(ids)))

    def test_improvement_is_pinned_not_guessed(self):
        w = master.water()
        self.assertIs(w.by_id("ground_water.protected_well").improved, True)
        self.assertIs(w.by_id("ground_water.unprotected_well").improved, False)
        self.assertIsNone(w.by_id("ground_water.all_wells").improved)

    def test_alignment_catches_a_changed_template(self):
        w = master.water()
        labels = [n.label for n in w.nodes]
        self.assertEqual(master.check_alignment(w, labels), [])
        labels[5] = "Something else"
        self.assertEqual(len(master.check_alignment(w, labels)), 1)


class TestLadders(unittest.TestCase):
    def test_five_rungs_each(self):
        self.assertEqual(len(WATER_LADDER), 5)
        self.assertEqual(len(SAN_LADDER), 5)

    def test_ladders_are_jmp_s(self):
        self.assertEqual([r["rung"] for r in WATER_LADDER][-1], "Surface water")
        self.assertEqual([r["rung"] for r in SAN_LADDER][-1], "Open defecation")


class TestProfile(unittest.TestCase):
    def test_profile_loads_and_names_both_domains(self):
        p = load_profile()
        self.assertIn("water", p["domains"])
        self.assertIn("sanitation", p["domains"])
        self.assertEqual(p["block"]["width"], 6)

    def test_slug_is_stable(self):
        self.assertEqual(slug("Tubewell/handpump"), "tubewell_handpump")
        self.assertEqual(slug("  Piped  water "), "piped_water")


@needs_wb
class TestRealWorkbooks(unittest.TestCase):
    """Reading a JMP country file takes a few seconds, so the first workbook is
    read once for the whole class."""

    @classmethod
    def setUpClass(cls):
        cls.ex, cls.binding = read(WB[0])
        cls.inst = cls.ex.water

    def test_identity_and_tree(self):
        ex, b = self.ex, self.binding
        self.assertEqual(len(ex.iso3), 3)
        self.assertEqual(b.tree_alignment.get("water"), [])
        self.assertEqual(b.tree_alignment.get("sanitation"), [])

    def test_water_and_sanitation_are_separate_instructions(self):
        ex = self.ex
        self.assertIsNotNone(ex.water)
        self.assertIsNotNone(ex.sanitation)
        self.assertIsNot(ex.water, ex.sanitation)
        self.assertNotEqual(ex.water.filename(), ex.sanitation.filename())
        self.assertNotEqual(ex.water.schema, ex.sanitation.schema)
        self.assertNotEqual(ex.water.content_fingerprint(),
                            ex.sanitation.content_fingerprint())

    def test_one_domain_can_be_read_alone(self):
        ex, _ = read(WB[0], domains="water")
        self.assertIsNotNone(ex.water)
        self.assertIsNone(ex.sanitation)

    def test_each_domain_carries_its_own_ladder(self):
        self.assertEqual(self.ex.water.ladder[-1]["rung"], "Surface water")
        self.assertEqual(self.ex.sanitation.ladder[-1]["rung"],
                         "Open defecation")

    def test_the_chain_is_carried_on_every_row(self):
        for inst in self.ex.instructions():
            for r in inst.rows:
                self.assertTrue(r.classification, r.label)
                self.assertLessEqual(set(r.rolls_up_to),
                                     {f["name"] for f in inst.facility_types})

    def test_facility_types_come_from_the_workbook(self):
        for inst in self.ex.instructions():
            self.assertTrue(inst.facility_types)
            self.assertTrue(all(f["in_workbook"] for f in inst.facility_types),
                            [f["name"] for f in inst.facility_types
                             if not f["in_workbook"]])

    def test_classifications_carry_their_subgroups_and_usage(self):
        for inst in self.ex.instructions():
            self.assertTrue(inst.classifications)
            total = sum(c["n_national_categories"] for c in inst.classifications)
            self.assertEqual(total, len(inst.rows))

    def test_language_is_kept(self):
        for inst in self.ex.instructions():
            self.assertTrue(inst.language)
            for r in inst.rows:
                self.assertTrue(r.jmp_label_local, r.label)

    def test_data_used_flags_are_captured_per_source(self):
        sc = self.ex.water.per_source[0]
        self.assertTrue(sc.data_used)
        self.assertIn("label", sc.data_used[0])

    def test_microdata_is_the_default_and_is_a_subset_of_all(self):
        f = WB[0]
        md, _ = read(f, sources="microdata", domains="water")
        al, _ = read(f, sources="all", domains="water")
        self.assertLess(len(md.water.sources), len(al.water.sources))
        self.assertTrue(all("microdata" in s.type.lower()
                            for s in md.water.sources))

    def test_no_survey_level_data_reaches_the_instruction(self):
        """The instruction must not carry frequencies -- spec S9, MUST NOT."""
        for inst in self.ex.instructions():
            for r in inst.rows:
                for v in r.__dict__.values():
                    self.assertNotIsInstance(v, float)

    def test_improvement_is_never_asserted_by_the_country(self):
        inst, b = self.inst, self.binding
        for f in run_rules(inst, b):
            self.assertNotEqual((f.rule, f.level), ("W-02", "BLOCK"))

    def test_no_row_carries_a_ladder_rung(self):
        for inst in self.ex.instructions():
            for r in inst.rows:
                self.assertFalse(hasattr(r, "rung"))

    def test_vintage_trail_is_populated(self):
        inst = self.ex.water
        self.assertTrue(inst.vintage["from"])
        self.assertTrue(any(len(r.observed_in) > 1 for r in inst.rows))

    def test_fingerprint_is_stable_across_reads(self):
        again, _ = read(WB[0])
        self.assertEqual(self.ex.water.content_fingerprint(),
                         again.water.content_fingerprint())

    def test_extract_writes_seven_artifacts_per_domain_plus_shared(self):
        with tempfile.TemporaryDirectory() as d:
            res = extract(WB[0], out=d)
            # 7 per domain, plus the binding report and the registry
            self.assertEqual(len(res["artifacts"]), 7 * 2 + 2)
            for p in res["artifacts"]:
                self.assertTrue(os.path.getsize(p) > 0, p)
            names = {os.path.basename(p) for p in res["artifacts"]}
            iso = res["extract"].iso3
            for dom in ("water", "sanitation"):
                self.assertIn(f"{iso}_{dom}_v1.0.yaml", names)
                self.assertIn(f"{iso}_{dom}_view.json", names)

    def test_standalone_check_reproduces_the_extraction_verdict(self):
        """A hand-edited instruction must be checkable without the workbook."""
        with tempfile.TemporaryDirectory() as d:
            res = extract(WB[0], out=d)
            again = check(d)
            self.assertEqual(len(again), 2)
            by_dom = {r["instruction"].domain: r for r in again}
            for dom, first in res["domains"].items():
                self.assertEqual(by_dom[dom]["verdict"], first["verdict"], dom)

    def test_the_check_catches_an_edit_that_breaks_a_rule(self):
        with tempfile.TemporaryDirectory() as d:
            extract(WB[0], out=d)
            path = [p for p in find_all(d)
                    if p.endswith("_water_v1.0.yaml")][0]
            txt = open(path, encoding="utf-8").read()
            self.assertIn("improved: true", txt)
            open(path, "w", encoding="utf-8").write(
                txt.replace("improved: true", "improved: false", 1))
            res = [r for r in check(d) if r["instruction"].domain == "water"][0]
            self.assertEqual(res["verdict"], "blocked")
            self.assertTrue(any(f.rule == "W-02" and f.level == "BLOCK"
                                for f in res["findings"]))

    def test_viewer_is_one_self_contained_file(self):
        with tempfile.TemporaryDirectory() as d:
            extract(WB[0], out=d)
            html = build_viewer(d, os.path.join(d, "v.html"))
            body = open(html, encoding="utf-8").read()
            self.assertTrue(os.path.getsize(html) > 20000)
            self.assertIn("__BUNDLES__", body)
            for bad in ("http://", "https://", "<script src", "<link rel"):
                self.assertNotIn(bad, body, f"viewer reaches for {bad}")

    def test_unknown_source_selector_is_an_error_not_a_silent_default(self):
        with self.assertRaises(ValueError):
            read(WB[0], sources="nonsense")

    def test_a_second_country_reads_with_the_same_pinned_tree(self):
        if len(WB) < 2:
            self.skipTest("only one workbook available")
        inst, b = read(WB[1])
        self.assertEqual(len(inst.iso3), 3)
        self.assertEqual(b.tree_alignment.get("water"), [])
        self.assertNotEqual(inst.iso3, self.inst.iso3)



# ==========================================================================
# the review app
# ==========================================================================
MINIMAL_BUNDLE = {
    "kind": "wash", "domain": "water",
    "country": {"iso3": "ZZZ", "name": "Testland"},
    "version": "v1.0", "status": "draft", "verdict": "clean",
    "counts": {"BLOCK": 0, "WARN": 0, "INFO": 1},
    "rows": [], "classifications": [], "facility_types": [], "sources": [],
    "findings": [], "source": {"file": "x.xlsx"},
}


def _fake_out(root):
    """An output tree with no workbook behind it."""
    d = os.path.join(root, "ZZZ")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "ZZZ_water_view.json"), "w") as fh:
        json.dump(MINIMAL_BUNDLE, fh)
    with open(os.path.join(d, "ZZZ_water_v1.0.yaml"), "w") as fh:
        fh.write("schema: gmd.country_instruction.wash.water\n")
    with open(os.path.join(d, "ZZZ_secret.env"), "w") as fh:
        fh.write("TOKEN=hunter2\n")
    return d


class TestViewerPage(unittest.TestCase):
    def test_picker_page_carries_no_data(self):
        with tempfile.TemporaryDirectory() as d:
            p = V.build(None, os.path.join(d, "v.html"))
            body = open(p, encoding="utf-8").read()
            self.assertIn('window.__MODE__ = "picker"', body)
            self.assertIn("window.__BUNDLES__ = [];", body)

    def test_embed_page_carries_the_bundles(self):
        with tempfile.TemporaryDirectory() as d:
            _fake_out(d)
            p = V.build(d, os.path.join(d, "v.html"), embed=True)
            body = open(p, encoding="utf-8").read()
            self.assertIn('window.__MODE__ = "embed"', body)
            self.assertIn("Testland", body)

    def test_mode_placeholder_does_not_eat_the_variable_name(self):
        """`__MODE__` used to substitute into `window.__MODE__` itself."""
        with tempfile.TemporaryDirectory() as d:
            body = open(V.build(None, os.path.join(d, "v.html")),
                        encoding="utf-8").read()
            self.assertIn("window.__MODE__", body)

    def test_page_never_reaches_for_the_network(self):
        with tempfile.TemporaryDirectory() as d:
            _fake_out(d)
            for embed in (False, True):
                body = open(V.build(d, os.path.join(d, "v.html"), embed=embed),
                            encoding="utf-8").read()
                for bad in ("http://", "https://", "<script src", "<link rel"):
                    self.assertNotIn(bad, body, f"embed={embed} pulls {bad}")


class TestViewerScan(unittest.TestCase):
    def test_scan_finds_a_country_folder(self):
        with tempfile.TemporaryDirectory() as d:
            _fake_out(d)
            sc = V.scan(d)
            self.assertEqual(len(sc["countries"]), 1)
            c = sc["countries"][0]
            self.assertEqual((c["iso3"], c["dir"]), ("ZZZ", "ZZZ"))
            self.assertIn("water", [x["domain"] for x in c["domains"]])

    def test_two_folders_for_one_country_are_two_entries(self):
        """A country is a folder. Keying by ISO3 silently dropped the second."""
        with tempfile.TemporaryDirectory() as d:
            _fake_out(d)
            shutil.copytree(os.path.join(d, "ZZZ"), os.path.join(d, "ZZZ_v2"))
            self.assertEqual(len(V.scan(d)["countries"]), 2)

    def test_scan_lists_only_readable_artefacts(self):
        with tempfile.TemporaryDirectory() as d:
            _fake_out(d)
            names = {f["name"] for f in V.scan(d)["countries"][0]["files"]}
            self.assertIn("ZZZ_water_v1.0.yaml", names)
            self.assertNotIn("ZZZ_secret.env", names)

    def test_scan_is_reread_not_cached(self):
        with tempfile.TemporaryDirectory() as d:
            _fake_out(d)
            self.assertEqual(len(V.scan(d)["countries"]), 1)
            shutil.copytree(os.path.join(d, "ZZZ"), os.path.join(d, "YYY"))
            self.assertEqual(len(V.scan(d)["countries"]), 2)


class TestViewerPaths(unittest.TestCase):
    def test_traversal_is_refused_not_normalised(self):
        with tempfile.TemporaryDirectory() as d:
            root = os.path.abspath(d)
            for bad in ("../x", "../../etc/passwd", "/etc/passwd", "a/../../b",
                        "..", "ZZZ/../../x"):
                self.assertIsNone(V._safe_join(root, bad), bad)

    def test_ordinary_paths_resolve(self):
        with tempfile.TemporaryDirectory() as d:
            root = os.path.abspath(d)
            self.assertEqual(V._safe_join(root, "ZZZ/a.yaml"),
                             os.path.join(root, "ZZZ", "a.yaml"))
            self.assertEqual(V._safe_join(root, ""), root)


class TestViewerServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = tempfile.mkdtemp()
        _fake_out(cls.dir)
        cls.httpd, cls.url = V.serve(cls.dir, port=0, block=False)

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        shutil.rmtree(cls.dir, ignore_errors=True)

    def get(self, path):
        with urllib.request.urlopen(self.url.rstrip("/") + path, timeout=10) as r:
            return r.read().decode()

    def test_index_is_the_page_in_server_mode(self):
        body = self.get("/")
        self.assertIn('window.__MODE__ = "server"', body)
        self.assertIn("window.__BUNDLES__ = [];", body)

    def test_scan_and_bundles(self):
        sc = json.loads(self.get("/api/scan"))
        self.assertEqual(sc["countries"][0]["iso3"], "ZZZ")
        b = json.loads(self.get("/api/bundles?dir=ZZZ"))
        self.assertEqual(b[0]["country"]["iso3"], "ZZZ")

    def test_empty_dir_means_every_folder(self):
        b = json.loads(self.get("/api/bundles?dir="))
        self.assertTrue(b)

    def test_raw_reads_an_artefact(self):
        d = json.loads(self.get("/api/raw?rel=ZZZ/ZZZ_water_v1.0.yaml"))
        self.assertIn("gmd.country_instruction.wash.water", d["text"])

    def test_a_new_folder_appears_without_a_restart(self):
        """The entire point: rerun the extractor, hit reload, see it."""
        before = len(json.loads(self.get("/api/scan"))["countries"])
        shutil.copytree(os.path.join(self.dir, "ZZZ"),
                        os.path.join(self.dir, "QQQ"))
        try:
            after = len(json.loads(self.get("/api/scan"))["countries"])
            self.assertEqual(after, before + 1)
        finally:
            shutil.rmtree(os.path.join(self.dir, "QQQ"))

    def test_it_refuses_to_leave_the_served_root(self):
        for bad in ("/api/raw?rel=../../etc/passwd", "/api/raw?rel=/etc/passwd",
                    "/api/bundles?dir=../..", "/api/bundles?dir=/tmp"):
            with self.assertRaises(urllib.error.HTTPError, msg=bad):
                self.get(bad)

    def test_it_refuses_extensions_that_are_not_artefacts(self):
        with self.assertRaises(urllib.error.HTTPError):
            self.get("/api/raw?rel=ZZZ/ZZZ_secret.env")

    def test_it_binds_loopback_only(self):
        self.assertEqual(self.httpd.server_address[0], "127.0.0.1")


# ==========================================================================
# language
# ==========================================================================
class TestPhraseIndex(unittest.TestCase):
    """The formula, not the rendered string, identifies a phrase."""

    def test_both_spellings_of_the_lookup(self):
        self.assertEqual(TR.phrase_index(
            "=HLOOKUP(Introduction!$G$4,nametranslations,183,FALSE)"), 183)
        self.assertEqual(TR.phrase_index(
            "=HLOOKUP(Introduction!$G$4,Key!$A$1:$G$395,248,FALSE)"), 248)

    def test_a_nested_lookup_is_still_found(self):
        self.assertEqual(TR.phrase_index(
            '=IF(A1="","",HLOOKUP(Introduction!$G$4,nametranslations,42,FALSE))'),
            42)

    def test_anything_else_is_none(self):
        for v in (None, "", "plain text", "=SUM(A1:A2)", 17):
            self.assertIsNone(TR.phrase_index(v), repr(v))


class TestCountries(unittest.TestCase):
    def test_a_country_named_in_its_own_language(self):
        for name, iso in (("España", "ESP"), ("Sénégal", "SEN"),
                          ("Российская Федерация", "RUS"),
                          ("Federación Rusa", "RUS"), ("Viet Nam", "VNM")):
            self.assertEqual(CO.to_iso3(name), iso, name)

    def test_a_country_named_inside_a_banner(self):
        self.assertEqual(CO.resolve("Sri Lanka - ISCED 2011 Mapping")[0], "LKA")
        self.assertEqual(
            CO.resolve("Cartographie de la CITE 2011 de Sénégal")[0], "SEN")

    def test_the_longest_country_wins(self):
        self.assertEqual(CO.to_iso3("Papua New Guinea"), "PNG")

    def test_the_banner_keeps_the_country_s_own_spelling(self):
        self.assertEqual(CO.resolve("España")[1], "España")

    def test_the_filename_is_the_fallback(self):
        iso, name = CO.resolve("", "JMP_2025_RUS_Russian_Federation_0.xlsx")
        self.assertEqual((iso, name), ("RUS", "Russian Federation"))

    def test_english_name_is_canonical_not_first_alphabetically(self):
        self.assertEqual(CO.english_name("RUS"), "Russian Federation")

    def test_an_unknown_name_is_none_never_a_guess(self):
        self.assertIsNone(CO.to_iso3("Nowhereland"))
        self.assertEqual(CO.resolve("Nowhereland")[0], "")


@needs_wb
class TestTranslatedWorkbooks(unittest.TestCase):
    """A workbook in Russian or Spanish must read exactly like an English one."""

    @classmethod
    def setUpClass(cls):
        cls.cases = {}
        for f in WB:
            ex, b = read(f)
            cls.cases[ex.iso3] = (ex, b, f)

    def _non_english(self):
        return {k: v for k, v in self.cases.items()
                if not (v[1].translation or {}).get("resolved_by",
                                                    "").startswith("already")}

    def test_the_dictionary_is_the_workbook_s_own(self):
        for iso, (ex, b, f) in self.cases.items():
            t = b.translation or {}
            self.assertTrue(t.get("available"), iso)
            self.assertEqual(t.get("languages", [""])[0], "English", iso)

    def test_the_matrix_stops_where_the_named_range_stops(self):
        """Folding the Key sheet's second table in mapped "Census" to a ladder
        rung and stopped English files binding."""
        for iso, (ex, b, f) in self.cases.items():
            self.assertLessEqual(len(b.translation.get("languages", [])), 8, iso)

    def test_a_translated_workbook_binds_its_concordance(self):
        for iso, (ex, b, f) in self._non_english().items():
            for inst in ex.instructions():
                self.assertTrue(b.tree_header_row.get(inst.domain), iso)
                self.assertTrue(inst.rows, f"{iso} {inst.domain}")

    def test_a_translated_workbook_matches_the_pinned_tree(self):
        for iso, (ex, b, f) in self.cases.items():
            for inst in ex.instructions():
                self.assertIn(inst.domain, b.tree_alignment, iso)
                self.assertEqual(b.tree_alignment[inst.domain], [],
                                 f"{iso} {inst.domain}")

    def test_source_types_resolve_so_microdata_is_selectable(self):
        for iso, (ex, b, f) in self.cases.items():
            for inst in ex.instructions():
                self.assertTrue(inst.sources, f"{iso} {inst.domain}")
                self.assertTrue(all("microdata" in s.type.lower()
                                    for s in inst.sources), iso)

    def test_facility_types_are_found_in_every_language(self):
        for iso, (ex, b, f) in self.cases.items():
            for inst in ex.instructions():
                missing = [x["name"] for x in inst.facility_types
                           if not x["in_workbook"]]
                self.assertEqual(missing, [], f"{iso} {inst.domain}")

    def test_the_local_wording_is_kept(self):
        for iso, (ex, b, f) in self._non_english().items():
            for inst in ex.instructions():
                self.assertTrue(any(r.jmp_label_local for r in inst.rows), iso)
                self.assertTrue(all(r.language for r in inst.rows), iso)

    def test_national_denominations_are_never_translated(self):
        """A country's own words are not JMP phrases and must survive intact."""
        for iso, (ex, b, f) in self._non_english().items():
            for inst in ex.instructions():
                for r in inst.rows:
                    self.assertTrue(r.label.strip(), iso)

    def test_nothing_blocks_on_a_translated_workbook(self):
        for iso, (ex, b, f) in self.cases.items():
            for inst in ex.instructions():
                blocks = [x for x in run_rules(inst, b) if x.level == "BLOCK"]
                self.assertEqual(blocks, [],
                                 f"{iso} {inst.domain}: "
                                 f"{[x.message for x in blocks]}")



# ==========================================================================
# benchmark, registry, review
# ==========================================================================
class TestBenchmarkHelpers(unittest.TestCase):
    def test_text_is_never_a_number(self):
        for v in ("No", "-", "m", "", None, True, False):
            self.assertIsNone(BM.num(v), repr(v))

    def test_a_number_is_a_number(self):
        self.assertEqual(BM.num(31.5), 31.5)
        self.assertEqual(BM.num(18), 18.0)


class TestRegistry(unittest.TestCase):
    def _e(self, **kw):
        base = dict(iso3="ZZZ", domain="water", country="Testland",
                    file="a.xlsx", fingerprint="aaa", era="2025",
                    era_from=2000, era_to=2020, signature={"gmd": "x"})
        base.update(kw)
        return base

    def test_first_ingest_is_v1_0(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(REG.record(d, self._e())["version"], "v1.0")

    def test_an_unchanged_re_ingest_mints_no_version(self):
        with tempfile.TemporaryDirectory() as d:
            REG.record(d, self._e())
            again = REG.record(d, self._e())
            self.assertEqual(again["version"], "v1.0")
            self.assertEqual(again["change"]["kind"], "identical")

    def test_a_cosmetic_change_is_minor(self):
        with tempfile.TemporaryDirectory() as d:
            REG.record(d, self._e())
            got = REG.record(d, self._e(fingerprint="bbb",
                                        signature={"gmd": "x", "note": "n"}))
            self.assertEqual((got["version"], got["change"]["kind"]),
                             ("v1.1", "cosmetic"))

    def test_a_change_that_moves_people_is_major(self):
        with tempfile.TemporaryDirectory() as d:
            REG.record(d, self._e())
            got = REG.record(d, self._e(fingerprint="ccc",
                                        signature={"gmd": "y"}))
            self.assertEqual((got["version"], got["change"]["kind"]),
                             ("v2.0", "breaking"))
            self.assertEqual(got["change"]["changed"], ["gmd"])

    def test_a_new_era_starts_its_own_version(self):
        with tempfile.TemporaryDirectory() as d:
            REG.record(d, self._e(era="2014", era_from=2014))
            got = REG.record(d, self._e(era="2023", era_from=2023,
                                        fingerprint="ddd"))
            self.assertEqual(got["version"], "v1.0")

    def test_two_eras_close_the_window_between_them(self):
        with tempfile.TemporaryDirectory() as d:
            REG.record(d, self._e(domain="education", cohort_era=True,
                                  era="2014", era_from=2014, era_to=2035))
            REG.record(d, self._e(domain="education", cohort_era=True,
                                  era="2023", era_from=2023, era_to=2035,
                                  fingerprint="ddd"))
            c = [x for x in REG.load(d)["countries"]
                 if x["domain"] == "education"][0]
            self.assertEqual(c["n_eras"], 2)
            self.assertEqual(c["eras"][0]["to"], 2022)
            self.assertEqual(c["eras"][1]["to"], 2035)

    def test_only_a_schooling_era_leaves_a_cohort_gap(self):
        with tempfile.TemporaryDirectory() as d:
            REG.record(d, self._e(cohort_era=False))
            c = REG.load(d)["countries"][0]
            self.assertNotIn("gap_before", c["eras"][0])


class TestReview(unittest.TestCase):
    def _patch(self, **kw):
        base = dict(target="rows", id="x", field="gmd", value="piped",
                    reason="because", by="A. Reviewer")
        base.update(kw)
        return base

    def test_an_edit_needs_a_reason_and_a_name(self):
        with tempfile.TemporaryDirectory() as d:
            for bad in (self._patch(reason=""), self._patch(by="")):
                with self.assertRaises(ValueError):
                    RV.add_patch(d, "ZZZ_water", bad)

    def test_only_declared_fields_are_editable(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                RV.add_patch(d, "ZZZ_water", self._patch(field="label"))
            with self.assertRaises(ValueError):
                RV.add_patch(d, "ZZZ_water", self._patch(target="nope"))

    def test_an_edit_is_a_patch_beside_the_extract(self):
        with tempfile.TemporaryDirectory() as d:
            RV.add_patch(d, "ZZZ_water", self._patch())
            doc = RV.load_patches(d, "ZZZ_water")
            self.assertEqual(len(doc["patches"]), 1)
            self.assertEqual(doc["patches"][0]["seq"], 1)

    def test_patches_overlay_a_copy_and_mark_what_changed(self):
        bundle = {"rows": [{"code": "x", "gmd": "surface"}]}
        out = RV.apply_patches(bundle, [self._patch(seq=1)])
        self.assertEqual(out["rows"][0]["gmd"], "piped")
        self.assertEqual(bundle["rows"][0]["gmd"], "surface")   # untouched
        self.assertIn("gmd", out["_edited"]["x"])

    def test_undo_removes_one_edit(self):
        with tempfile.TemporaryDirectory() as d:
            RV.add_patch(d, "ZZZ_water", self._patch())
            self.assertTrue(RV.undo_patch(d, "ZZZ_water", 1))
            self.assertEqual(RV.load_patches(d, "ZZZ_water")["patches"], [])

    def test_a_blocked_version_cannot_be_approved(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                RV.approve(d, "ZZZ_water", by="A", fingerprint="f",
                           version="v1.0", verdict="blocked",
                           counts={"BLOCK": 1, "WARN": 0})

    def test_every_warning_needs_an_acknowledgement(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                RV.approve(d, "ZZZ_water", by="A", fingerprint="f",
                           version="v1.0", verdict="awaiting_review",
                           counts={"BLOCK": 0, "WARN": 2},
                           acknowledged=[{"rule": "W-09", "text": "ok"}])

    def test_an_approval_names_a_person_and_pins_the_fingerprint(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                RV.approve(d, "ZZZ_water", by="  ", fingerprint="f",
                           version="v1.0", verdict="clean", counts={})
            rec = RV.approve(d, "ZZZ_water", by="L. Mbeki", fingerprint="abc",
                             version="v1.0", verdict="awaiting_review",
                             counts={"BLOCK": 0, "WARN": 1},
                             acknowledged=[{"rule": "W-09", "text": "agreed"}])
            self.assertTrue(rec["approved"])
            self.assertEqual(rec["fingerprint"], "abc")

    def test_withdrawing_keeps_the_record(self):
        with tempfile.TemporaryDirectory() as d:
            RV.approve(d, "ZZZ_water", by="L", fingerprint="f", version="v1.0",
                       verdict="clean", counts={})
            rec = RV.revoke(d, "ZZZ_water", "L", "changed my mind")
            self.assertFalse(rec["approved"])
            self.assertIn("withdrawn", rec)


@needs_wb
class TestBenchmarkOnRealWorkbooks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ex, cls.b = read(WB[0])

    def test_estimates_are_captured(self):
        for inst in self.ex.instructions():
            sm = (inst.benchmark or {}).get("summary") or {}
            self.assertTrue(sm.get("categories_with_estimates"), inst.domain)
            self.assertTrue(sm.get("sources_with_estimates"), inst.domain)

    def test_the_country_ladder_is_captured(self):
        inst = self.ex.water
        rungs = (inst.benchmark.get("ladder") or {}).get("rungs") or []
        self.assertGreaterEqual(len(rungs), 4)

    def test_the_three_aggregate_blocks_are_captured(self):
        ps = self.ex.water.benchmark["per_source"][0]
        for k in ("facility_type_estimates", "service_level_estimate",
                  "data_used_for_estimates"):
            self.assertIn(k, ps["blocks"])

    def test_the_benchmark_never_reaches_the_instruction(self):
        for inst in self.ex.instructions():
            self.assertNotIn("benchmark", inst.to_dict())
            for f in run_rules(inst, self.b):
                self.assertFalse(f.rule == "W-17" and f.level == "BLOCK",
                                 f.message)

    def test_the_benchmark_is_written_as_its_own_artefact(self):
        with tempfile.TemporaryDirectory() as d:
            res = extract(WB[0], out=d, domains="water")
            names = {os.path.basename(p) for p in res["artifacts"]}
            iso = res["extract"].iso3
            self.assertIn(f"{iso}_water_benchmark.json", names)
            self.assertIn(f"{iso}_water_benchmark.csv", names)


if __name__ == "__main__":
    if not WB:
        print("note: no JMP workbook found -- workbook tests will be skipped.\n"
              "      set GMD_JMP_DIR=/path/to/files to run them.\n")
    unittest.main(verbosity=2)
