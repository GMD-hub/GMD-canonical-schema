"""
gmd_wash_concordance.master
===========================
The fixed JMP master category trees.

The JMP country file lays its categories out as a fixed tree, identical in
every country file of a release.  The tree carries no indentation and no ids
in the workbook -- the labels come from a language lookup -- so the hierarchy,
the improvement status and the GMD target are pinned here and matched to the
workbook **by position**, with the English label used as a check.

That ordering matters.  Binding by label would silently mis-bind a French or
Spanish country file; binding by position and *checking* the label turns a
template change into a stop with a message, which is what the design note
asks for.
"""
from __future__ import annotations

import os
import unicodedata
from typing import Dict, List, Optional

import yaml

DATA = os.path.join(os.path.dirname(__file__), "data")


class Node(dict):
    """One JMP master category."""
    @property
    def id(self):        return self["id"]
    @property
    def label(self):     return self["label_en"]
    @property
    def path(self):      return self["path"]
    @property
    def level(self):     return self["level"]
    @property
    def gmd(self):       return self["gmd"]
    @property
    def improved(self):  return self["improved"]
    @property
    def shared(self):    return self["shared"]
    @property
    def spans(self):     return self.get("spans", [])
    @property
    def rolls_up_to(self): return self.get("rolls_up_to", [])
    @property
    def aliases(self):   return self.get("aliases", [])
    @property
    def structural(self): return self["structural"]


class MasterTree:
    def __init__(self, doc: dict):
        self.domain = doc["domain"]
        self.frame = doc["frame"]
        self.first_row = doc["tree_first_row"]
        self.facility_types = doc.get("facility_types", [])
        self.nodes: List[Node] = [Node(n) for n in doc["nodes"]]
        self._by_id = {n.id: n for n in self.nodes}

    def __len__(self):
        return len(self.nodes)

    def by_id(self, jid) -> Optional[Node]:
        return self._by_id.get(jid)

    def at_ordinal(self, i) -> Optional[Node]:
        return self.nodes[i] if 0 <= i < len(self.nodes) else None

    def gmd_targets(self):
        return sorted({n.gmd for n in self.nodes if n.gmd})

    def spans(self, jid) -> List[str]:
        """The GMD targets a node covers when it has no single target of its
        own.  A node with several targets below it is not a defect: it is a
        category that needs a splitting rule, not a target.  Rule W-09 uses
        this to tell that case from a genuinely missing target."""
        node = self._by_id.get(jid)
        return list(node.spans) if node else []


def _norm(s) -> str:
    s = "" if s is None else str(s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(s.lower().replace("’", "'").split())


_CACHE: Dict[str, MasterTree] = {}


def load(name: str) -> MasterTree:
    if name not in _CACHE:
        with open(os.path.join(DATA, name), encoding="utf-8") as fh:
            _CACHE[name] = MasterTree(yaml.safe_load(fh))
    return _CACHE[name]


def water() -> MasterTree:
    return load("jmp_water_master.yaml")


def sanitation() -> MasterTree:
    return load("jmp_sanitation_master.yaml")


def check_alignment(tree: MasterTree, labels: List[str]) -> List[dict]:
    """Compare the workbook's tree labels, in order, against the master.

    Returns one entry per position that does not agree.  An empty list means
    the workbook is laid out exactly as the release this package pins.
    """
    out = []
    for i, node in enumerate(tree.nodes):
        got = labels[i] if i < len(labels) else None
        if got is None:
            out.append({"ordinal": i, "row": node["row"], "expected": node.label,
                        "found": None, "reason": "tree ends early"})
        elif _norm(got) != _norm(node.label):
            if _norm(got) in {_norm(a) for a in node.aliases}:
                continue          # a wording JMP uses for the same node
            out.append({"ordinal": i, "row": node["row"], "expected": node.label,
                        "found": got, "reason": "label differs"})
    if len(labels) > len(tree.nodes):
        out.append({"ordinal": len(tree.nodes), "row": None,
                    "expected": None, "found": labels[len(tree.nodes)],
                    "reason": "tree is longer than the master"})
    return out
