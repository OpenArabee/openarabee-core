# OpenArabee — Project Charter

| | |
|---|---|
| **Version** | 0.2 (draft) — 2026-11-15 (Phase 0: D‑015 to D‑019, O‑2, O‑6, O‑8, O‑9) |
| **Owner** | Obada Obaid (GitHub: `obadaobaid`, organisation: `OpenArabee`) |
| **Status** | **All decisions in this document are provisional.** They can be changed at any time through the decision log (section 12). |
| **Domain / brand** | openarabee.com · logo: `assets/logo.png` · colours (sampled from the logo): navy ≈ `#0A2A45`, gold ≈ `#C29A52` |

This charter is the single reference for every working session, human or AI. `CLAUDE.md` in each repository is derived from it. If a session and the charter disagree, the charter wins until it is changed on purpose.

---

## 1. Purpose

OpenArabee builds an **open, verified, source-referenced dataset of Arabic morphology**, starting from the Quran's most frequent roots, and turns it into learning tools.

Its distinctive idea: every verb is described in **both** grammatical traditions at once — the classical Arabic system of *abwāb* (أبواب التصريف) and the Western system of numbered Forms (I–XV, QI–QIV) — and **every single fact carries its source and its verification status**.

### Goals
1. Make the language of the Quran, and Arabic generally, easier to learn and understand.
2. Provide clean, openly licensed, verified morphological data that software and AI systems can rely on.
3. Serve as the data foundation for products: first a website, later the book «الجذور المئة», apps, and datasets.

### Non-goals
- Not a complete dictionary and not a *tafsīr*; no religious rulings.
- Not a copy or re-packaging of copyrighted dictionaries or databases.
- Not a new morphological analyser; existing open tools are used, not rebuilt.

---

## 2. Principles

1. **Small and useful first.** Grow root by root; each phase ends with something people can use.
2. **Provenance per fact.** No value without a source reference. AI output alone is never a source.
3. **Visible reliability.** Each entry shows its verification status publicly.
4. **Clean rights.** The core contains only material that permits commercial reuse. Anything else lives in a separate layer.
5. **Honest claims.** No marketing numbers we have not computed ourselves (see section 9).
6. **Both traditions, neutrally.** Where sources or schools classify differently, record all classifications with their sources instead of picking silently.
7. **Reversible decisions.** Everything is versioned; plans change through the decision log.

---

## 3. The two systems and how they relate

Finding from the preparation work: the two systems describe the same verbs at different levels of detail. They are not rivals.

- The **Western Forms I–X** are identical to «الأوزان العشرة». The numbering is a European convention dating back to Erpenius (1613); the Arabic tradition names each pattern by its shape (وزن أَفْعَلَ …).
- The **35 abwāb** are the count given in *Matn al-Bināʾ* (متن البناء). Other classical authors count differently, so "35" is one scheme, not *the* official number. The data model therefore stores a `scheme` with every classification.
- The classical system is finer in four places: Form I splits into six abwāb by vowel; rare Forms XI–XV; quadriliteral verbs; and the *mulḥaq* group (verbs with a triliteral root that conjugate like quadriliterals).
- **The bāb belongs to the verb, not to the root** (حَسِبَ vs. حَسَبَ). It cannot be computed; it must be looked up per verb.

### Correspondence (after *Matn al-Bināʾ* and Wright; all 35 abwāb transcribed on 2026‑11‑15 from a reading copy into `reference/abwab.bina-35.json`; collation against a printed edition is still open, see O‑6)

| Classical group | Count | Patterns | Western |
|---|---|---|---|
| ثلاثي مجرد | 6 | فعَل‑يفعُل (نصر), فعَل‑يفعِل (ضرب), فعَل‑يفعَل (فتح), فعِل‑يفعَل (علم), فعُل‑يفعُل (حسن), فعِل‑يفعِل (حسب) | Form I + vowel class |
| ثلاثي مزيد بحرف | 3 | أفعل، فعّل، فاعل | IV, II, III |
| ثلاثي مزيد بحرفين | 5 | انفعل، افتعل، افعلّ، تفعّل، تفاعل | VII, VIII, IX, V, VI |
| ثلاثي مزيد بثلاثة | 4 | استفعل، افعوعل، افعوّل، افعالّ | X, XII, XIII, XI |
| رباعي مجرد | 1 | فعلل | QI |
| ملحق بالرباعي المجرد | 6 | فوعل، فيعل، فعول، فعيل، فعلل، فعلى | usually treated as QI |
| رباعي مزيد بحرف | 1 | تفعلل | QII |
| ملحق بـ«تفعلل» | 5 | تفعلل، تفوعل، تفيعل، تفعول، تفعلى | usually treated as QII |
| رباعي مزيد بحرفين | 2 | افعنلل، افعللّ | QIII, QIV |
| ملحق بـ«افعنلل» | 2 | افعنلل (اقعنسس), افعنلى (اسلنقى) | XIV, XV |
| **Total** | **35** | | |

---

## 4. Scope and phases

Only Phase 1 is planned in detail. Later phases are a direction, not a commitment. Each phase is split into sub-phases when it starts; plan changes are recorded in the decision log.

| Phase | Content | Result |
|---|---|---|
| **0 — Setup** | Repositories, licences, `CLAUDE.md`, schema v0, source register, reference tables (abwāb, Forms) transcribed from the reference works, validation scripts, backup routine, domain + GitHub Pages | A working, empty but validated project |
| **1 — The 100 roots** | The 100 most frequent Quranic roots plus the few additions needed to cover every Form, bāb and root type | Dataset v0.1 + website v1 |
| **2 — Growth** | 300–500 roots, nouns and nominal patterns, feedback process with reviewer roles, contributor agreement | Dataset v0.5, review workflow |
| **3 — Products** | Book «الجذور المئة», Anki decks, apps, German as a third language | First products |
| **4 — Data for AI** | Benchmark for Arabic morphology in language models, training-ready datasets, API, OntoLex-Lemon export | Research and developer offering |

### Phase 1 in detail

| Sub-phase | Work |
|---|---|
| 1a | Fix the root list. Build the coverage matrix **Form/bāb × root type** (sound, hamzated, doubled, assimilated, hollow, defective, doubly weak). Add roots until every cell that exists in the language has at least one example; mark cells that need non-Quranic examples (Forms XIII–XV). |
| 1b | Create verb entries with the mandatory fields (section 5). |
| 1c | Quran layer: occurrence counts and 1–3 example verses per verb. |
| 1d | Website v1: one page per root, provenance on hover/tap, "Suggest a correction" button that opens a pre-filled GitHub issue. |
| 1e | First expert review round, release v0.1 archived with a DOI (Zenodo). |

**Exit criteria for Phase 1:** all mandatory fields filled for all selected roots; every value has at least one non-AI source; 100 % of entries machine-checked; at least the gold set (section 7) expert-reviewed; website live on openarabee.com.

---

## 5. Data model (sketch)

**Canonical format:** UTF-8 JSON files with stable IDs, one file per root, validated by a JSON Schema. Everything else (SQLite, CSV, graph, website, OntoLex) is **generated** from it — never edited by hand.

### Entities
- **Root** — letters, root type, optional (function words and loanwords have no root).
- **Lexeme** — a verb, noun or particle. Has a `type` (verb / derived noun / primitive noun / particle / proper noun / loanword).
- **Classification** — links a verb to a bāb and/or Form, always with `scheme` (e.g. `bina-35`, `wright`) and source. Several classifications per verb are allowed.
- **Sense** — meaning in Arabic and English (later German).
- **Attestation** — Quranic occurrences (lives in the Quran layer).
- **Source** — one entry per work in the source register: title, author, edition, licence, link.

### Mandatory fields for a verb in Phase 1
root + root type · Form (I–XV/QI–QIV) · bāb (for Form I: which of the six) · past and imperfect, fully vowelled · maṣdar(s) · transitive yes/no · short meaning (ar + en) · Quran: count and 1–3 examples · **source and status for every field**.

Prepared in the schema but filled later: detailed transitivity, conjugation restrictions, nominal features (plural, gender, diptote), further derived nouns, long explanations, German, images, audio.

### Provenance pattern
Every factual field is an object, not a bare value:

```json
{
  "id": "v-ktb-1",
  "root": "r-ktb",
  "type": "verb",
  "past":      { "value": "كَتَبَ",   "src": ["mukhtar"], "status": "draft" },
  "imperfect": { "value": "يَكْتُبُ", "src": ["mukhtar"], "status": "draft" },
  "classification": [
    { "scheme": "bina-35", "value": "bab-1-nasara", "src": ["mukhtar"], "status": "draft" },
    { "scheme": "wright",  "value": "I",            "src": ["wright-1896"], "status": "draft" }
  ],
  "masdar": [ { "value": "كِتَابَة", "src": ["lane"], "status": "draft" } ],
  "transitive": { "value": true, "src": ["lane"], "status": "draft" }
}
```
*(Illustrative only — values and source assignments are not yet verified.)*

### Verification status (shown on the website)
`draft` (AI or unchecked) → `machine-checked` (passes rules and tool comparison) → `source-verified` (matches at least two independent free sources) → `expert-reviewed` (one qualified reviewer) → `expert-confirmed` (two reviewers).

---

## 6. Sources

Rule: **the core is built only from sources that allow commercial reuse.** Protected works are consulted by a human for single entries when sources disagree; nothing is extracted from them systematically.

### A. Reference works (define the two systems)

| Role | Work | Rights |
|---|---|---|
| Classical framework: the 35 abwāb | **متن البناء** (بناء الأفعال), attributed to al‑Danqazī; printed in Cairo collections since at least 1911 | public domain |
| Classical explanation and terminology | **شذا العرف في فن الصرف**, Aḥmad al‑Ḥamalāwī (d. 1932), first printed 1894 | public domain |
| Classical authority for disputes | **شرح الشافية**, al‑Raḍī al‑Astarābādhī on Ibn al‑Ḥājib | public domain (work); check edition |
| Western framework: Forms I–XV, QI–QIV | **Wright, *A Grammar of the Arabic Language***, 3rd ed. 1896–98 | public domain |

### B. Evidence per verb (bāb, vowels, maṣdar, meaning)

| Work | Why | Rights |
|---|---|---|
| **مختار الصحاح** (al‑Rāzī) | names the bāb of triliteral verbs by model verbs | public domain |
| **المصباح المنير** (al‑Fayyūmī) | states the bāb explicitly («من باب ضرب») | public domain |
| **Lane, *Arabic–English Lexicon*** (1863–93) | imperfect vowel, maṣdars, English meanings | work is public domain; the Perseus digital text is CC BY‑SA → cite the printed volume, do not paste its text into the core |
| لسان العرب، القاموس المحيط، تاج العروس | fallback evidence | public domain (works) |
| **مقاييس اللغة** (Ibn Fāris), **مفردات ألفاظ القرآن** (al‑Rāghib) | core meaning of roots; Quranic usage | public domain (works) |

### C. Machine-readable free data

| Source | Licence | Use |
|---|---|---|
| Wikidata lexemes | CC0 | core; verify before import |
| Camel Morph data | CC BY 4.0 | core, with attribution |
| CAMeL Tools (code) | MIT | tooling |
| Tanzil Quran text (Uthmani, Ḥafṣ) | CC BY 3.0, verbatim only | Quran layer |
| Quranic Arabic Corpus v0.4 | research / non-commercial, attribution | **Quran layer only** |

### D. Cross-check only (never copied into the core)
Qutrub, Arramooz (GPL) · Hans Wehr, Doha Historical Dictionary, Fischer and other modern works (copyrighted) · OpenITI and Shamela digitisations (reading copies; OpenITI is non-commercial).

### Notes on rights (not legal advice)
- In Germany a work enters the public domain 70 years after the author's death; critical editions of public-domain texts can carry a separate 25-year right. Prefer old printings and cite work + edition + page.
- Single facts are not protected; systematically extracting a substantial part of someone else's database can violate EU database right.
- Before any commercial use: one consultation with a lawyer.

---

## 7. Quality assurance

1. **Gold set:** 200–500 verbs reviewed by hand by a qualified person; used to measure every tool and every AI draft.
2. **Two independent tools** (e.g. CAMeL vs. Qutrub) for conjugation; agreement passes, disagreement goes to manual review.
3. **Automated rules** in CI: schema validity, vowel pattern matches the declared bāb, Form VII has no object, every `src` exists in the source register, no value without source.
4. **Cross-model review:** an entry drafted by one AI model is checked by a different one.
5. **Public correction channel:** GitHub issue form now; reviewer roles and weighting (teacher / verified expert) when there are enough contributors. No own account system at the start.
6. **Owner spot checks** of a random sample in every release.

---

## 8. Licences and repositories

| Item | Decision |
|---|---|
| Code | MIT |
| Core data and own texts | CC BY 4.0 |
| Contributions | Contributor agreement (CLA) from the first external contribution, so the owner keeps full rights of use |
| Quran layer | Separate repository; terms of its sources apply (non-commercial where the Quranic Arabic Corpus is used) |

**GitHub organisation `OpenArabee`** (all repositories public):
- `openarabee-core` — schema, core data, build and validation code, docs (this charter in `docs/charter.md`)
- `openarabee-quran` — Quran layer
- `openarabee-web` — website (GitHub Pages → openarabee.com), from Phase 1d

**Protection against loss:** GitHub + a `git bundle` in Google Drive after every working session + release archives on Zenodo. Two-factor authentication on the owner account.

---

## 9. Verified numbers and claims policy

Computed by us from the Quranic Arabic Corpus v0.4 (77,429 words):

| Statement | Value |
|---|---|
| Distinct roots | 1,642 |
| Words without a root (particles, pronouns, names) | 35.5 % of all words, only 175 distinct lemmas |
| The 100 most frequent roots cover | 39.0 % of all words (60.5 % of words that have a root) |
| 100 roots + 50 most frequent function words | 73.4 % of all words |
| Verses fully covered by that | 9.9 % |
| Verb roots / average Forms per root | 943 / 1.56 (63 % occur in one Form only) |

**Policy:** "Recognising a word" is not "understanding the text". Allowed wording: *"With 100 roots and 50 small function words you recognise about three out of four words in the Quran."* Claims such as "80 % understanding" are not used.

Consequence for the product: function words are taught alongside roots — they are the largest lever.

---

## 10. Working mode and roles

| Who | Does |
|---|---|
| **Owner** | Strategy and priorities; approvals for releases, licences, spending and anything public; native-speaker judgement; recruiting reviewers; spot checks |
| **AI (Claude)** | Execution: research, schema, code, drafts, validation, documentation, backups. Asks the owner before irreversible or public steps |
| **Expert reviewers** | Verify linguistic content; their decision outranks tools and AI |

**Model use:** the strongest model (Fable 5.2) for architecture, the charter and hard linguistic questions · Opus 5.5 / Sonnet for implementation · Sonnet / Haiku in batch mode for bulk drafts · a different model for review than for drafting.

**Languages:** code, schema, docs: English. Content: Arabic and English; Arabic technical terms (باب، وزن، مصدر) are kept with transliteration. German from Phase 3. Conversation with the owner: German.

**Continuity:** sessions do not remember each other. Charter, `CLAUDE.md` and the decision log carry the context; each phase starts in a fresh session that reads them first.

---

## 11. Open points

| # | Question | Who |
|---|---|---|
| O‑1 | Recruit at least one qualified reviewer (Arabic linguistics / Quranic studies) for the gold set | Owner |
| O‑2 | ID and transliteration scheme for roots and abwāb. Proposed in Phase 0: D‑015, `docs/data-model.md` §2 | Owner confirms |
| O‑3 | Ask the maintainers of the Quranic Arabic Corpus about terms for non-research use | Owner, later |
| O‑4 | Does the root list itself (derived from frequency counts) belong in the core or the Quran layer? Default: list in core, counts in Quran layer; confirm in the legal consultation | Owner |
| O‑5 | Logo: generated by the owner with Google Gemini (2026‑11‑15). AI-generated images usually carry no copyright of their own, so others could reuse the bitmap; protection of the name/logo would come from a trademark (see O‑7). Redraw as a clean SVG in Phase 0 and record provenance in `assets/README.md` | AI (redraw), Owner (approve) |
| O‑6 | Choose citable printings (edition + page) of the reference works. Done for Wright (Cambridge 1896–98). Open for all Arabic works; until a printing of *Matn al-Bināʾ* is chosen, the abwāb table cites a typed reading copy and stays `draft` | AI proposes, owner approves |
| O‑7 | Trademark: exact-name searches at DPMA, EUIPO, WIPO were empty on 2026‑11‑15; similar names exist ("OpenArabic" app, "arabee" platform). Decide later whether to register | Owner |
| O‑8 | Collate Wright's table of Forms (§35) and his quadriliteral examples (§§67–72) against the page images; the text layer of the scan is illegible for Arabic. To check there: §71 seems to list a verb "to lie on one's back" under the third quadriliteral Form, while *Matn al-Bināʾ* has اسلنقى as mulḥaq (bāb 35, Form XV) | AI |
| O‑9 | `CLA.md` is a draft without legal review and not in force; review it in the legal consultation before the first external contribution | Owner |

---

## 12. Decision log

All entries are provisional.

| ID | Date | Decision |
|---|---|---|
| D‑001 | 2026‑11‑15 | Name **OpenArabee**; domain openarabee.com; GitHub organisation `OpenArabee` |
| D‑002 | 2026‑11‑15 | Licences: code MIT, core data CC BY 4.0, CLA for contributors |
| D‑003 | 2026‑11‑15 | Two layers: commercially usable core / separate Quran layer |
| D‑004 | 2026‑11‑15 | Free sources only in the core; protected works for single-entry checks only |
| D‑005 | 2026‑11‑15 | Reference works: *Matn al-Bināʾ* + *Shadhā al-ʿArf* (classical), Wright 3rd ed. (Western); per-verb evidence from *Mukhtār al-Ṣiḥāḥ*, *al-Miṣbāḥ al-Munīr*, Lane |
| D‑006 | 2026‑11‑15 | Phase 1 = 100 most frequent Quranic roots + additions for full coverage; the book «الجذور المئة» grows out of it |
| D‑007 | 2026‑11‑15 | Canonical format: JSON with stable IDs and per-field provenance; all other formats generated |
| D‑008 | 2026‑11‑15 | First product: static website on GitHub Pages with provenance display and correction button |
| D‑009 | 2026‑11‑15 | Languages: project in English; content Arabic + English; German later |
| D‑010 | 2026‑11‑15 | Quran text: Tanzil Uthmani (Ḥafṣ), unmodified |
| D‑011 | 2026‑11‑15 | Backups: `git bundle` to Google Drive after each session |
| D‑012 | 2026‑11‑15 | Phases 0–4 as in section 4; only Phase 1 detailed |
| D‑013 | 2026‑11‑15 | All repositories public from the start; names `openarabee-core`, `openarabee-quran`, later `openarabee-web` |
| D‑014 | 2026‑11‑15 | Charter kept in English (`charter.md`, authoritative) with a German version (`charter.de.md`) |
| D‑015 | 2026‑11‑15 | Identifiers: ASCII, lowercase letters and digits; one character per root letter (table in `docs/data-model.md` §2); roots `r-ktb`, lexemes `v-ktb-1` with a running number per root, abwāb `bina-01`…`bina-35`, Forms `I`…`XV`, `QI`…`QIV`. Published ids never change |
| D‑016 | 2026‑11‑15 | Schema v0 (`0.1`): one file per root holding the root and its lexemes; a source reference may carry the exact place (`loc`); root types are derived from the letters by rule and checked, not sourced |
| D‑017 | 2026‑11‑15 | Arabic citation forms are spelled one normalised way (`docs/data-model.md` §4); deviations of the source are recorded in a note |
| D‑018 | 2026‑11‑15 | Licence split inside `openarabee-core`: code and schema MIT; data, reference tables, source register and docs CC BY 4.0 |
| D‑019 | 2026‑11‑15 | Work happens on branches; the owner approves by merging the pull request into `main` |

---

## Appendix — links

- Matn al-Bināʾ (text): https://takw.in/files/البناء%20والأساس.pdf
- Shadhā al-ʿArf (1901 printing, Qatar National Library): https://ediscovery.qnl.qa/islandora/object/QNL:00002470
- Wright's Grammar (Internet Archive): https://archive.org/details/grammarofarabicl01caspuoft
- Mukhtār al-Ṣiḥāḥ (Arabic Wikisource, author's preface): https://ar.wikisource.org/wiki/مختار_الصحاح/مقدمة
- al-Miṣbāḥ al-Munīr (Arabic Wikisource, index): https://ar.wikisource.org/wiki/المصباح_المنير/فهرس
- Lane's Lexicon (scans): https://archive.org/details/ArabicEnglishLexicon.CopiousEasternSources.EnlargedSuppl.Kamoos.Lane.Poole.1863
- Wikidata licensing: https://www.wikidata.org/wiki/Wikidata:Licensing
- Camel Morph: https://pypi.org/project/camel-morph/
- CAMeL Tools: https://camel-tools.readthedocs.io/
- Tanzil: https://tanzil.net/download
- Quranic Arabic Corpus FAQ: https://corpus.quran.com/faq.jsp
- Origin of the Form numbers (Arabic-L): https://listserv.linguistlist.org/pipermail/arabic-l/2000-September/000805.html
