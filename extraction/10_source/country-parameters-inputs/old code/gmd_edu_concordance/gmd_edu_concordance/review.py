"""
gmd_edu_concordance.review
==========================
Edits and approvals, as artefacts.

Two rules shape this, both from the design note, and both are about what
*cannot* happen:

**Nothing is overwritten.** An edit is a **patch on top of the extract**, kept
in its own file. The extracted instruction stays exactly as the workbook
produced it, so a re-extraction can always be compared against it and a
reviewer's change is always visible as a change rather than as a fact. Undoing
an edit is deleting a patch, not re-running anything.

**A blocked version cannot be approved.** Approval is a claim about one
country made by a person who can be asked to defend it, so it records who,
when, what fingerprint they were looking at, and -- in writing -- every warning
they acknowledged. A warning that was never acknowledged is not approved
silently.

Both files live beside the instruction they belong to:

    {ISO3}_{domain}_patches.json     every edit, in order, with who and why
    {ISO3}_{domain}_approval.json    the approval record
"""
from __future__ import annotations

import datetime as _dt
import json
import os
from typing import Any, Dict, List, Optional

PATCH_SUFFIX = "_patches.json"
APPROVAL_SUFFIX = "_approval.json"
SCHEMA = "gmd.concordance_review"

# Only these can be edited. A reviewer corrects the mapping; they do not get to
# rewrite what the workbook said, because the extract must stay comparable to
# the file it came from.
EDITABLE = {
    "rows": {"gmd", "note", "spans", "improved_note", "attainment_note",
             "excluded", "reason"},
    "eras": {"from", "to", "label", "description", "reason"},
    "instruction": {"note", "owner"},
}


def now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat()


def patch_path(outdir: str, stem: str) -> str:
    return os.path.join(outdir, stem + PATCH_SUFFIX)


def approval_path(outdir: str, stem: str) -> str:
    return os.path.join(outdir, stem + APPROVAL_SUFFIX)


def load_patches(outdir: str, stem: str) -> Dict[str, Any]:
    p = patch_path(outdir, stem)
    if not os.path.exists(p):
        return {"schema": SCHEMA, "stem": stem, "patches": []}
    with open(p, encoding="utf-8") as fh:
        d = json.load(fh)
    d.setdefault("patches", [])
    return d


def add_patch(outdir: str, stem: str, patch: Dict[str, Any]) -> Dict[str, Any]:
    """Append one edit.

    ``patch`` is ``{target, id, field, value, reason, by}`` where ``target`` is
    ``rows``, ``eras`` or ``instruction``. A field outside the editable set is
    refused rather than stored, because a patch nobody can apply is worse than
    no patch.
    """
    target = patch.get("target")
    field = patch.get("field")
    if target not in EDITABLE:
        raise ValueError(f"{target!r} is not an editable target")
    if field not in EDITABLE[target]:
        raise ValueError(
            f"{field!r} cannot be edited on {target}; editable: "
            + ", ".join(sorted(EDITABLE[target])))
    if not str(patch.get("reason") or "").strip():
        raise ValueError("every edit carries a reason")
    if not str(patch.get("by") or "").strip():
        raise ValueError("every edit records who made it")
    doc = load_patches(outdir, stem)
    rec = {
        "seq": len(doc["patches"]) + 1,
        "at": now(),
        "target": target,
        "id": patch.get("id"),
        "field": field,
        "value": patch.get("value"),
        "previous": patch.get("previous"),
        "reason": str(patch["reason"]).strip(),
        "by": str(patch["by"]).strip(),
    }
    doc["patches"].append(rec)
    doc["updated_at"] = rec["at"]
    os.makedirs(outdir, exist_ok=True)
    with open(patch_path(outdir, stem), "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return rec


def undo_patch(outdir: str, stem: str, seq: int) -> bool:
    doc = load_patches(outdir, stem)
    keep = [p for p in doc["patches"] if p.get("seq") != seq]
    if len(keep) == len(doc["patches"]):
        return False
    doc["patches"] = keep
    doc["updated_at"] = now()
    with open(patch_path(outdir, stem), "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return True


def apply_patches(doc: Dict[str, Any], patches: List[dict]) -> Dict[str, Any]:
    """Overlay the edits on a view bundle, in order.

    Applied to a *copy*: the caller keeps the extract. Every field an edit
    touched is also recorded in ``_edited`` so the viewer can mark it, because
    an edit that looks like an extraction is the thing to avoid.
    """
    import copy
    out = copy.deepcopy(doc)
    edited: Dict[str, List[str]] = {}
    rows = {str(r.get("code") or r.get("programme_id")): r
            for r in out.get("rows", [])}
    eras = {str(e.get("id")): e for e in out.get("eras", [])}
    for p in sorted(patches, key=lambda x: x.get("seq", 0)):
        t, i, f, v = (p.get("target"), str(p.get("id")), p.get("field"),
                      p.get("value"))
        if t == "rows" and i in rows:
            rows[i][f] = v
            edited.setdefault(i, []).append(f)
        elif t == "eras" and i in eras:
            eras[i][f] = v
            edited.setdefault("era:" + i, []).append(f)
        elif t == "instruction":
            out[f] = v
            edited.setdefault("instruction", []).append(f)
    out["_edited"] = edited
    out["_patches"] = len(patches)
    return out


# --------------------------------------------------------------------------
def load_approval(outdir: str, stem: str) -> Optional[Dict[str, Any]]:
    p = approval_path(outdir, stem)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def approve(outdir: str, stem: str, *, by: str, fingerprint: str,
            version: str, verdict: str, counts: Dict[str, int],
            acknowledged: Optional[List[dict]] = None,
            note: str = "", patches: int = 0) -> Dict[str, Any]:
    """Record an approval, or refuse to.

    Refused when the version is blocked, when no approver is named, or when a
    warning has not been acknowledged in writing. The last one is the point:
    approving a version with unacknowledged warnings is how a warning becomes
    invisible.
    """
    by = str(by or "").strip()
    if not by:
        raise ValueError("an approval names the person making it")
    if verdict == "blocked" or (counts or {}).get("BLOCK"):
        raise ValueError(
            "a blocked version cannot be approved; the BLOCK findings have to "
            "be resolved in the workbook, or waived by a schema decision")
    acknowledged = acknowledged or []
    want = (counts or {}).get("WARN", 0)
    got = len([a for a in acknowledged if str(a.get("text") or "").strip()])
    if got < want:
        raise ValueError(
            f"{want} warning(s) need acknowledgement in writing and {got} "
            f"were given; a warning nobody wrote against is not approved")
    rec = {
        "schema": SCHEMA,
        "stem": stem,
        "approved": True,
        "by": by,
        "at": now(),
        "version": version,
        "fingerprint": fingerprint,
        "verdict_at_approval": verdict,
        "counts_at_approval": counts,
        "patches_at_approval": patches,
        "acknowledged": acknowledged,
        "note": str(note or "").strip(),
    }
    os.makedirs(outdir, exist_ok=True)
    with open(approval_path(outdir, stem), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=1, ensure_ascii=False, default=str)
    return rec


def revoke(outdir: str, stem: str, by: str, reason: str) -> Dict[str, Any]:
    """Withdraw an approval. The record stays; it is marked withdrawn."""
    rec = load_approval(outdir, stem)
    if not rec:
        raise ValueError("there is no approval to withdraw")
    rec["approved"] = False
    rec["withdrawn"] = {"by": str(by or "").strip(),
                        "at": now(), "reason": str(reason or "").strip()}
    with open(approval_path(outdir, stem), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=1, ensure_ascii=False, default=str)
    return rec
