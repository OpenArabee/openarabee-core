#!/usr/bin/env python3
"""Validate the OpenArabee core data (charter §7, item 3).

    python tools/validate.py              # everything that must always hold
    python tools/validate.py --release    # plus the release criteria of charter §4

Exit code 0 means no errors. Each rule has a short code so that CI output,
issues and docs/data-model.md can refer to it.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oa.arabic import TATWEEL, is_nfc, match_pattern, root_types  # noqa: E402
from oa.ids import LEXEME_ID, root_id  # noqa: E402

SCHEMA_BASE = "https://openarabee.com/schema/v0/"
MANDATORY_VERB_FIELDS = ("past", "imperfect", "classification", "masdar", "transitive", "gloss")
STATUS_ORDER = ["draft", "machine-checked", "source-verified", "expert-reviewed", "expert-confirmed"]
INTRANSITIVE_FORMS = {"VII"}  # charter §7: a Form VII verb takes no object


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, code: str, where: str, message: str) -> None:
        self.errors.append(f"{code}  {where}: {message}")


class _DuplicateKey(ValueError):
    pass


def _no_duplicates(pairs):
    seen = {}
    for key, value in pairs:
        if key in seen:
            raise _DuplicateKey(key)
        seen[key] = value
    return seen


def load_json(path: Path, rel: str, report: Report):
    """F01 valid UTF-8 JSON, F02 no duplicate keys, F03 NFC, F04 no tatweel."""
    try:
        text = path.read_text(encoding="utf-8")
        data = json.loads(text, object_pairs_hook=_no_duplicates)
    except _DuplicateKey as exc:
        report.error("F02", rel, f"duplicate key {exc}")
        return None
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        report.error("F01", rel, f"cannot read as UTF-8 JSON: {exc}")
        return None
    if not is_nfc(text):
        report.error("F03", rel, "text is not in Unicode normal form NFC")
    if TATWEEL in text:
        report.error("F04", rel, "contains tatweel (U+0640)")
    return data


def schema_validators(repo: Path) -> dict[str, Draft202012Validator]:
    schemas = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in sorted((repo / "schema").glob("*.schema.json"))}
    registry = Registry().with_resources((s["$id"], Resource.from_contents(s)) for s in schemas.values())
    out = {}
    for name, schema in schemas.items():
        Draft202012Validator.check_schema(schema)
        out[name] = Draft202012Validator(schema, registry=registry)
    return out


def check_schema(validator: Draft202012Validator, data, rel: str, report: Report) -> bool:
    """S01 the file matches its JSON Schema."""
    ok = True
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        ok = False
        at = "/".join(str(p) for p in err.absolute_path) or "(top level)"
        report.error("S01", rel, f"{at}: {err.message[:200]}")
    return ok


def iter_facts(node, path=""):
    """Yield (path, object) for every object that carries provenance."""
    if isinstance(node, dict):
        if "src" in node and "status" in node:
            yield path, node
        for key, value in node.items():
            yield from iter_facts(value, f"{path}/{key}")
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from iter_facts(value, f"{path}/{i}")


def check_provenance(data, rel: str, sources: dict[str, dict], report: Report, release: bool) -> None:
    """P01 every src exists in the register. P02 only core-layer sources in core data.
    P03 a status from source-verified upwards names who checked the value. R02 (release) no value is still a draft."""
    for path, fact in iter_facts(data):
        for ref in fact["src"]:
            sid = ref if isinstance(ref, str) else ref.get("id")
            if sid not in sources:
                report.error("P01", rel, f"{path}: source '{sid}' is not in sources/register.json")
            elif sources[sid]["layer"] != "core":
                report.error("P02", rel, f"{path}: source '{sid}' is {sources[sid]['layer']}-only and cannot back core data")
        level = STATUS_ORDER.index(fact["status"])
        checks = fact.get("checks", [])
        persons = {c["by"] for c in checks if c["by"].startswith("person:")}
        if level >= 2 and not checks:
            report.error("P03", rel, f"{path}: status {fact['status']} needs at least one entry in checks")
        if level >= 3 and len(persons) < level - 2:
            report.error("P03", rel, f"{path}: status {fact['status']} needs checks by {level - 2} different person(s)")
        if release and fact["status"] == "draft":
            report.error("R02", rel, f"{path}: still has status draft")


def check_register(reg: dict, rel: str, report: Report) -> dict[str, dict]:
    """G01 source ids are unique."""
    sources: dict[str, dict] = {}
    for s in reg.get("sources", []):
        if s["id"] in sources:
            report.error("G01", rel, f"source id '{s['id']}' appears twice")
        sources[s["id"]] = s
    return sources


def check_forms(forms: dict, rel: str, report: Report) -> dict[str, dict]:
    """T01 form ids are unique."""
    out: dict[str, dict] = {}
    for f in forms.get("forms", []):
        if f["id"] in out:
            report.error("T01", rel, f"Form '{f['id']}' appears twice")
        out[f["id"]] = f
    return out


def check_abwab(table: dict, forms: dict[str, dict], rel: str, report: Report) -> dict[str, dict]:
    """T02 numbering 1..35 in order with matching ids. T03 group sizes as declared.
    T04 each model verb is an instance of its pattern. T05 Western equivalents exist;
    an 'exact' equivalent has the same past pattern."""
    abwab = table.get("abwab", [])
    out: dict[str, dict] = {}
    if [b["number"] for b in abwab] != list(range(1, 36)):
        report.error("T02", rel, "abwāb must be numbered 1 to 35 in order")
    groups = {g["id"]: g for g in table.get("groups", [])}
    seen: dict[str, int] = {}
    for b in abwab:
        where = f"{rel} {b['id']}"
        if b["id"] != f"bina-{b['number']:02d}":
            report.error("T02", where, f"id does not match number {b['number']}")
        out[b["id"]] = b
        if b["group"] not in groups:
            report.error("T03", where, f"unknown group '{b['group']}'")
        seen[b["group"]] = seen.get(b["group"], 0) + 1
        if b["number_in_group"] != seen[b["group"]]:
            report.error("T03", where, f"number_in_group should be {seen[b['group']]}")
        for key in ("past", "imperfect"):
            msg = match_pattern(b["wazn"][key]["value"], b["mawzun"][key]["value"])
            if msg:
                report.error("T04", where, msg)
        wm, mm = b["wazn"].get("masdar", []), b["mawzun"].get("masdar", [])
        if len(wm) != len(mm):
            report.error("T04", where, "different number of maṣdar patterns and model maṣdars")
        for w, m in zip(wm, mm):
            msg = match_pattern(w["value"], m["value"])
            if msg:
                report.error("T04", where, msg)
        for w in b["western"]:
            form = forms.get(w["value"])
            if form is None:
                report.error("T05", where, f"Form '{w['value']}' is not in the forms table")
            elif w["relation"] == "exact" and form["pattern"]["value"] != b["wazn"]["past"]["value"]:
                report.error("T05", where, f"marked exact, but Form {w['value']} has pattern {form['pattern']['value']}")
    for gid, g in groups.items():
        if seen.get(gid, 0) != g["count"]:
            report.error("T03", rel, f"group '{gid}' declares {g['count']} abwāb, has {seen.get(gid, 0)}")
    return out


def check_root_file(data: dict, path: Path, rel: str, abwab: dict, forms: dict,
                    lexeme_ids: dict[str, str], report: Report, release: bool) -> None:
    """D01 file name = root id = id derived from the letters. D02 root types as derived.
    D03 lexeme ids well-formed, unique, and under this root. D04 classifications exist and
    agree across schemes. D05 a sound verb fits the pattern of its bāb. D06 Form VII is
    intransitive. R01 (release) mandatory verb fields are present."""
    root = data["root"]
    expected = root_id(root["letters"])
    if root["id"] != expected:
        report.error("D01", rel, f"root id is {root['id']}, letters give {expected}")
    if path.stem != root["id"]:
        report.error("D01", rel, f"file must be named {root['id']}.json")
    derived = root_types(root["letters"])
    if sorted(root["types"]) != sorted(derived):
        report.error("D02", rel, f"root types {root['types']} should be {derived}")
    key = root["id"][2:]
    for lex in data["lexemes"]:
        where = f"{rel} {lex['id']}"
        m = LEXEME_ID.match(lex["id"])
        if not m or m.group(2) != key or lex["root"] != root["id"]:
            report.error("D03", where, f"lexeme must belong to {root['id']} and be named <v|n|p>-{key}-<n>")
        if (lex["type"] == "verb") != lex["id"].startswith("v-"):
            report.error("D03", where, "the prefix v- is for verbs and only for verbs")
        if lex["id"] in lexeme_ids:
            report.error("D03", where, f"id already used in {lexeme_ids[lex['id']]}")
        lexeme_ids[lex["id"]] = rel
        if lex["type"] != "verb":
            continue
        classes = lex.get("classification", [])
        babs = [c["value"] for c in classes if c["scheme"] == "bina-35"]
        wforms = [c["value"] for c in classes if c["scheme"] == "wright"]
        for b in babs:
            if b not in abwab:
                report.error("D04", where, f"unknown bāb '{b}'")
        for f in wforms:
            if f not in forms:
                report.error("D04", where, f"unknown Form '{f}'")
        allowed = {w["value"] for b in babs if b in abwab for w in abwab[b]["western"]}
        if babs and wforms and not allowed & set(wforms):
            report.error("D04", where, f"bāb {babs} corresponds to Form {sorted(allowed)}, entry says {wforms}")
        if derived == ["sound"] and len(babs) == 1 and babs[0] in abwab:
            bab = abwab[babs[0]]
            for field in ("past", "imperfect"):
                if field in lex:
                    msg = match_pattern(bab["wazn"][field]["value"], lex[field]["value"])
                    if msg:
                        report.error("D05", where, f"{field} does not fit {babs[0]}: {msg}")
        if INTRANSITIVE_FORMS & set(wforms) and lex.get("transitive", {}).get("value") is True:
            report.error("D06", where, "a Form VII verb cannot be transitive")
        if release:
            for field in MANDATORY_VERB_FIELDS:
                if not lex.get(field):
                    report.error("R01", where, f"mandatory field '{field}' is missing")
            gloss = lex.get("gloss", {})
            for lang in ("ar", "en"):
                if gloss and lang not in gloss:
                    report.error("R01", where, f"gloss.{lang} is missing")
            for scheme, found in (("bina-35", babs), ("wright", wforms)):
                if classes and not found:
                    report.error("R01", where, f"no classification in scheme '{scheme}'")


def validate(repo: Path, release: bool = False) -> Report:
    report = Report()
    validators = schema_validators(repo)

    def load(rel: str, schema: str):
        data = load_json(repo / rel, rel, report)
        if data is None or not check_schema(validators[schema], data, rel, report):
            return None
        return data

    reg = load("sources/register.json", "source-register.schema.json")
    forms_doc = load("reference/forms.wright.json", "forms.schema.json")
    abwab_doc = load("reference/abwab.bina-35.json", "abwab.schema.json")
    if reg is None or forms_doc is None or abwab_doc is None:
        return report
    sources = check_register(reg, "sources/register.json", report)
    forms = check_forms(forms_doc, "reference/forms.wright.json", report)
    abwab = check_abwab(abwab_doc, forms, "reference/abwab.bina-35.json", report)
    # Reference tables are checked for provenance but are not held to R02:
    # their collation is tracked in the handoff, not by the release flag.
    check_provenance(forms_doc, "reference/forms.wright.json", sources, report, False)
    check_provenance(abwab_doc, "reference/abwab.bina-35.json", sources, report, False)

    lexeme_ids: dict[str, str] = {}
    for path in sorted((repo / "data" / "roots").glob("*.json")):
        rel = str(path.relative_to(repo))
        data = load(rel, "root.schema.json")
        if data is None:
            continue
        check_root_file(data, path, rel, abwab, forms, lexeme_ids, report, release)
        check_provenance(data, rel, sources, report, release)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--release", action="store_true", help="also apply the release criteria (R rules)")
    args = parser.parse_args(argv)
    report = validate(args.repo, args.release)
    roots = len(list((args.repo / "data" / "roots").glob("*.json")))
    for line in report.errors:
        print(line)
    print(f"{'FAILED' if report.errors else 'OK'}: {len(report.errors)} error(s); "
          f"register, 2 reference tables and {roots} root file(s) checked"
          f"{' with release criteria' if args.release else ''}.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
