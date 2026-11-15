<p align="center"><img src="assets/logo.svg" alt="OpenArabee" width="420"></p>

**Open, source-referenced data on Arabic morphology: roots, abwāb and Forms I–XV.**

Every verb is described in both grammatical traditions, the classical *abwāb* and the Western
numbered Forms, and every single value names its source and its verification status.

**Status: Phase 0 (setup).** The schema, the source register, the two reference tables and
the validation are in place; there are no root entries yet. All values in the reference
tables are still `draft`. Project charter: [English](docs/charter.md) · [Deutsch](docs/charter.de.md).

## What is here

| Path | Content |
|---|---|
| `reference/abwab.bina-35.json` | the 35 abwāb of *Matn al-Bināʾ*: pattern, model verb, maṣdars, examples, Western equivalent |
| `reference/forms.wright.json` | Forms I–XV and QI–QIV after Wright's *Grammar* (3rd ed.) |
| `sources/register.json` | every work that may be cited, with rights and permitted use |
| `data/roots/` | one file per root (empty until Phase 1) |
| `schema/` | JSON Schema v0 |
| `tools/`, `tests/` | validation, identifiers, backup |
| `docs/data-model.md` | identifiers, provenance, spelling, validation rules |

## Check the data

```
pip install -r requirements.txt
python tools/validate.py
python -m pytest
```

## Corrections

Found a mistake? Open an issue with the form **Suggest a correction** and name a source where
it can be checked. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licences

Code and schema (`tools/`, `tests/`, `schema/`, `.github/`): [MIT](LICENSE).
Data, reference tables, source register and documentation: [CC BY 4.0](LICENSE-DATA),
suggested attribution: "OpenArabee (openarabee.com)". For the logo see `assets/README.md`.
