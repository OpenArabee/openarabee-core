# OpenArabee core: working rules

Derived from `docs/charter.md`. If this file and the charter disagree, the charter wins.
Read `docs/charter.md` and `docs/handoff.md` before starting; update `docs/handoff.md` before ending.

## What this repository is

The canonical dataset of OpenArabee (Arabic morphology, both the classical abwāb and the
Western Forms, every fact with source and verification status) plus the schema and the tools
that check it. Everything else (SQLite, CSV, website) is generated from the JSON here.

## Rules that must never be broken

1. **No value without a source.** Every fact is an object `{value, src, status}`. `src` names
   entries of `sources/register.json`, with the exact place (`loc`) wherever possible.
2. **AI output is never a source.** If you know something but have not seen it in a source,
   it does not go into `data/` or `reference/`. Look it up, or leave it out and note the gap.
3. **Only core-layer sources back core data.** Sources with layer `cross-check` or
   `quran-layer` must not appear in `src` here. Nothing is copied systematically from
   protected works or databases (charter §6).
4. **New values start as `draft`.** Only raise a status when its condition in charter §5 is
   met: `machine-checked` after rules and tool comparison pass, `source-verified` after two
   independent free sources agree, `expert-*` only on a human reviewer's decision.
5. **Record disagreement, do not resolve it silently.** When sources or schools classify a
   verb differently, add all classifications with their sources.
6. **Canonical JSON is edited deliberately; generated files are never edited by hand.**
7. **Ask the owner before anything public, irreversible, paid or licence-related**: merging
   to `main`, releases, licence or CLA changes, DNS, new external services, deleting data.
   Work on a branch and open a pull request; the owner merges.
8. **No claims we have not computed** (charter §9).

## How to work

- Run `python tools/validate.py` and `python -m pytest` before every commit. Both must pass.
- IDs, spelling of Arabic values and the validation rules are defined in `docs/data-model.md`.
  Generate root ids with `python tools/oa/ids.py كتب`; never invent them by hand.
- Changes to decisions go into the decision log (charter §12) in the same pull request, in
  `docs/charter.md` and `docs/charter.de.md`.
- After each session: `tools/backup.sh`, upload the bundle to Google Drive, update the handoff.

## Languages

Code, schema, docs: English. Content: Arabic and English; Arabic technical terms (باب، وزن،
مصدر) are kept, with transliteration. Conversation with the owner: German.

## Layout

| Path | Content | Licence |
|---|---|---|
| `data/roots/` | one JSON file per root (canonical data) | CC BY 4.0 |
| `reference/` | the 35 abwāb, the Forms | CC BY 4.0 |
| `sources/register.json` | every work that may be cited, with rights and layer | CC BY 4.0 |
| `schema/` | JSON Schema v0 | MIT |
| `tools/`, `tests/`, `.github/` | validation, ids, backup, CI | MIT |
| `docs/` | charter, handoff, data model | CC BY 4.0 |
