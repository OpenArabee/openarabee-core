# Data model v0

Schema version `0.1`. All of this is provisional (charter §12, D-015 to D-018).

## 1. Files

| File | Schema | Content |
|---|---|---|
| `data/roots/<root id>.json` | `schema/root.schema.json` | one root and all its lexemes |
| `reference/abwab.bina-35.json` | `schema/abwab.schema.json` | the 35 abwāb of *Matn al-Bināʾ* |
| `reference/forms.wright.json` | `schema/forms.schema.json` | Forms I-XV and QI-QIV after Wright |
| `sources/register.json` | `schema/source-register.schema.json` | every citable work |

UTF-8, Unicode NFC, two-space indentation, no tatweel.

## 2. Identifiers (open point O-2)

Identifiers are ASCII, lowercase letters and digits only. They are therefore safe in file
names and URLs and cannot collide on case-insensitive file systems (macOS, Windows), which
rules out plain Buckwalter (`D` ض against `d` د).

**Root letters: one character per radical.**

| ء | ب | ت | ث | ج | ح | خ | د | ذ | ر | ز | س | ش | ص |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | b | t | v | j | 7 | x | d | 4 | r | z | s | c | 9 |

| ض | ط | ظ | ع | غ | ف | ق | ك | ل | م | ن | ه | و | ي |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | 6 | 0 | 3 | g | f | q | k | l | m | n | h | w | y |

The 19 letters whose Buckwalter symbol is a lowercase letter keep it. Of the other nine,
`2 3 6 7 9` are the digits of the Arabic chat alphabet and `c` is Safe Buckwalter; `4 8 0`
(ذ ض ظ) are fixed by this table only. Hamza as a radical is always `ء`, whatever its seat.

| Thing | Pattern | Example |
|---|---|---|
| Root | `r-<letters>` | `r-ktb`, `r-3lm` (علم), `r-qr2` (قرأ), `r-8rb` (ضرب) |
| Lexeme | `<v\|n\|p>-<letters>-<n>` | `v-ktb-1` |
| Bāb | `bina-01` … `bina-35` | `bina-01` (نصر) |
| Form | `I` … `XV`, `QI` … `QIV` | `IV` |
| Source | lowercase slug | `mukhtar`, `wright-1896` |

`<n>` in a lexeme id is a running number per root. It is given once, never reused and says
nothing about the Form: حَسِبَ and حَسَبَ are two verbs of one root and one Form. Bāb ids use
the running number of the *Matn* (1-35) because readable names collide (احمرّ / احمارّ).
An id never changes once it has been published in a release.

`python tools/oa/ids.py كتب r-3lm` converts in both directions.

## 3. Provenance and status

Every factual field is an object:

```json
{ "value": "كَتَبَ", "src": [{ "id": "mukhtar", "loc": "s.v. كتب" }], "status": "draft" }
```

- `src` has at least one entry. An entry is a source id, or an object with `id` and the
  place `loc` (page, paragraph, headword) and an optional `note`. Give `loc` whenever you can.
- `status` is one of `draft`, `machine-checked`, `source-verified`, `expert-reviewed`,
  `expert-confirmed` (charter §5).
- `note` records anything a reader needs to judge the value, e.g. a misprint in the copy used.
- Fields that are *derived by rule* from other fields carry no source of their own and are
  recomputed by the validator. In v0 this is only `root.types`.

## 4. Spelling of Arabic values

So that values can be compared mechanically, citation forms are written one way:

- Verbs: 3rd person masculine singular, fully vowelled, with the final vowel (كَتَبَ، يَكْتُبُ).
- Maṣdars and nouns: no case ending and no tanwīn (كِتَابَة).
- Hamzat al-waṣl is written as plain alif with kasra (اِنْكَسَرَ); hamzat al-qaṭʿ with its
  hamza (أَكْرَمَ، إِكْرَام).
- Sukūn on every vowelless consonant, including the diphthongs (حَوْقَلَ), but not on the
  letters of the long vowels (قَاتَلَ، تَفْعِيل).
- Shadda with its vowel (فَرَّحَ).

Where the source prints something else, the value is normalised and a `note` says so.

## 5. Root types

Derived from the letters of a triliteral root (`tools/oa/arabic.py`, `root_types`):
`hamzated` (a radical is ء), `doubled` (second = third), `assimilated` / `hollow` /
`defective` (first / second / third radical is و or ي), `doubly-weak` (two weak radicals),
otherwise `sound`. A root can have several (أتى: hamzated and defective). Roots with four or
more letters have no types in v0. The Arabic terms and their sources will be added to the
reference tables in sub-phase 1a.

## 6. Reference tables

Each bāb records what the text says: the pattern (`wazn`), the model verb (`mawzun`), each
with past, imperfect and maṣdars; what the pattern is built for (`bina`, in the text's own
words, with an English reading aid); its examples; and its Western equivalent with the kind
of relation (`exact`, `vowel-class` for the six abwāb of Form I, `subsumed` for mulḥaq
patterns that Western grammars do not number, `model-verb` where the Western source lists
the bāb's model verb under a Form with a different pattern). A bāb can have several Western
equivalents; bāb 35 (اسلنقى) is the first case.

## 7. Validation rules

`python tools/validate.py` (add `--release` for the R rules):

| Code | Rule |
|---|---|
| F01-F04 | valid UTF-8 JSON; no duplicate keys; NFC; no tatweel |
| S01 | the file matches its JSON Schema |
| G01 | source ids are unique |
| P01 | every `src` exists in the register |
| P02 | only sources with layer `core` back core data |
| T01-T03 | reference tables are complete, numbered 1-35 and grouped as declared |
| T04 | every model verb and maṣdar is an instance of its pattern |
| T05 | Western equivalents exist; an `exact` one has the same pattern |
| D01 | file name = root id = id derived from the letters |
| D02 | root types as derived from the letters |
| D03 | lexeme ids are well-formed, unique and belong to the root |
| D04 | classifications exist and the two schemes agree |
| D05 | a verb of a sound root fits the pattern of its bāb |
| D06 | a Form VII verb is not transitive |
| R01 | release: all mandatory verb fields are present (charter §5) |
| R02 | release: no value is still `draft` |

D05 covers sound roots only; weak, doubled and hamzated verbs need the conjugation tools
(charter §7, item 2) and are checked from sub-phase 1b on.

## 8. Not in v0 yet

Senses beyond a short gloss, detailed transitivity, nouns and nominal features, rootless
lexemes (function words), attestations (Quran layer, separate repository), German.
