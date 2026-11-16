"""Tests for tools/validate.py. Run with: python -m pytest"""
import copy
import json
import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

import validate as v  # noqa: E402
from oa.arabic import match_pattern, root_types  # noqa: E402
from oa.ids import root_id, root_letters  # noqa: E402

FIXTURE = json.loads((REPO / "tests/fixtures/r-ktb.json").read_text(encoding="utf-8"))


@pytest.fixture
def repo(tmp_path):
    for name in ("schema", "sources", "reference"):
        shutil.copytree(REPO / name, tmp_path / name)
    (tmp_path / "data/roots").mkdir(parents=True)
    return tmp_path


def write_root(repo, data, name=None):
    path = repo / "data/roots" / (name or data["root"]["id"] + ".json")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def codes(repo, release=False):
    return sorted({line.split()[0] for line in v.validate(repo, release).errors})


def verb(data):
    return data["lexemes"][0]


def test_repository_as_committed_is_valid():
    assert v.validate(REPO).errors == []


def test_fixture_is_valid(repo):
    write_root(repo, FIXTURE)
    assert codes(repo) == []


def test_release_rejects_drafts(repo):
    write_root(repo, FIXTURE)
    assert codes(repo, release=True) == ["R02"]


def mutations():
    def unknown_source(d): verb(d)["past"]["src"] = ["nowhere"]
    def cross_check_source(d): verb(d)["masdar"][0]["src"] = ["wehr"]
    def quran_layer_source(d): verb(d)["transitive"]["src"] = ["qac"]
    def no_source(d): verb(d)["past"]["src"] = []
    def bare_value(d): verb(d)["past"] = "كَتَبَ"
    def wrong_root_id(d): d["root"]["letters"] = ["ك", "ت", "م"]
    def wrong_types(d): d["root"]["types"] = ["hollow"]
    def foreign_lexeme(d): verb(d)["id"] = "v-drb-1"
    def unknown_status(d): verb(d)["past"]["status"] = "checked"
    def schemes_disagree(d): verb(d)["classification"][1]["value"] = "IV"
    def vowel_against_bab(d): verb(d)["imperfect"]["value"] = "يَكْتِبُ"
    def tatweel(d): verb(d)["gloss"]["en"]["value"] = "to wriـte"
    def verified_without_check(d): verb(d)["past"]["status"] = "source-verified"
    def expert_without_person(d):
        verb(d)["past"]["status"] = "expert-reviewed"
        verb(d)["past"]["checks"] = [{"by": "ai:some-model", "date": "2026-11-16", "method": "compared with the source"}]
    def form_seven_transitive(d):
        verb(d)["classification"] = [{"scheme": "wright", "value": "VII", "src": ["wright-1896"], "status": "draft"}]
    return [
        (unknown_source, "P01"), (cross_check_source, "P02"), (quran_layer_source, "P02"),
        (no_source, "S01"), (bare_value, "S01"), (wrong_root_id, "D01"), (wrong_types, "D02"),
        (foreign_lexeme, "D03"), (unknown_status, "S01"), (schemes_disagree, "D04"),
        (vowel_against_bab, "D05"), (tatweel, "F04"), (form_seven_transitive, "D06"),
        (verified_without_check, "P03"), (expert_without_person, "P03"),
    ]


@pytest.mark.parametrize("mutate,code", mutations(), ids=lambda x: x.__name__ if callable(x) else x)
def test_rule_catches(repo, mutate, code):
    data = copy.deepcopy(FIXTURE)
    mutate(data)
    write_root(repo, data, "r-ktb.json")
    assert code in codes(repo)


def test_release_requires_mandatory_fields(repo):
    data = copy.deepcopy(FIXTURE)
    del verb(data)["masdar"]
    write_root(repo, data)
    assert "R01" in codes(repo, release=True)
    assert codes(repo) == []


def test_duplicate_keys_are_rejected(repo):
    (repo / "data/roots/r-ktb.json").write_text('{"schema_version": "0.1", "schema_version": "0.1"}', encoding="utf-8")
    assert codes(repo) == ["F02"]


def test_a_wrong_model_verb_is_caught(repo):
    path = repo / "reference/abwab.bina-35.json"
    table = json.loads(path.read_text(encoding="utf-8"))
    table["abwab"][0]["mawzun"]["imperfect"]["value"] = "يَنْصِرُ"
    path.write_text(json.dumps(table, ensure_ascii=False), encoding="utf-8")
    assert codes(repo) == ["T04"]


def test_match_pattern():
    assert match_pattern("اِفْعَلَلَّ", "اِقْشَعَرَّ") is None
    assert match_pattern("اِفْعَوْعَلَ", "اِعْشَوْشَبَ") is None
    assert match_pattern("فَعَّلَ", "فَرَّحَ") is None
    assert match_pattern("اِفْعَوْعَلَ", "اِعْشَوْسَبَ") is not None  # ع must repeat
    assert match_pattern("فَعَلَ", "عَلِمَ") is not None


def test_ids_round_trip():
    assert root_id(["ك", "ت", "ب"]) == "r-ktb"
    assert root_id(["ض", "ر", "ب"]) != root_id(["د", "ر", "ب"])
    for rid in ("r-ktb", "r-3lm", "r-qr2", "r-9br", "r-0lm"):
        assert root_id(root_letters(rid)) == rid
    with pytest.raises(ValueError):
        root_id(["ق", "ر", "أ"])


def test_root_types():
    assert root_types(["ك", "ت", "ب"]) == ["sound"]
    assert root_types(["ق", "و", "ل"]) == ["hollow"]
    assert root_types(["و", "ع", "د"]) == ["assimilated"]
    assert root_types(["ر", "م", "ي"]) == ["defective"]
    assert root_types(["م", "د", "د"]) == ["doubled"]
    assert root_types(["و", "ق", "ي"]) == ["doubly-weak"]
    assert root_types(["ء", "ت", "ي"]) == ["hamzated", "defective"]
    assert root_types(["ز", "ل", "ز", "ل"]) == []


def test_a_check_by_a_person_allows_expert_reviewed(repo):
    data = copy.deepcopy(FIXTURE)
    verb(data)["past"]["status"] = "expert-reviewed"
    verb(data)["past"]["checks"] = [{"by": "person:some-reviewer", "date": "2026-11-16", "method": "compared with the printed dictionary"}]
    write_root(repo, data)
    assert codes(repo) == []


def test_generated_tables_are_current():
    import render_tables
    assert render_tables.render(REPO) == (REPO / "docs/tables.md").read_text(encoding="utf-8"), "run: python tools/render_tables.py"
