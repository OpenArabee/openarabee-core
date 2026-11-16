# OpenArabee — Session handoff

Read this together with `docs/charter.md` at the start of every new session. Update it at the end of every session.

## State on 2026-11-16 (end of the Phase 0 session)

**Phase 0 is closed.** All Phase 0 pull requests are merged (`openarabee-core` #1 and #2, `openarabee-quran`, `openarabee-web`). The website is live at https://openarabee.com with HTTPS. Two small branches wait for the owner: `checks` in `openarabee-core` and `legal` in `openarabee-web` (see to-dos).

**In `openarabee-core`**
- Project files, licences, schema v0, `docs/data-model.md`, source register (24 works), validator with CI: merged.
- `reference/forms.wright.json`: all 19 patterns collated with the page images of Wright vol. I (§35 p. 29, §68 p. 48).
- `reference/abwab.bina-35.json`: all 35 abwāb collated entry by entry against *Majmūʿ muhimmāt al-mutūn*, 4th printing, Cairo, Muṣṭafā al-Bābī al-Ḥalabī, 1369/1949, pp. 557–568; every `loc` gives the page of that printing.
- Branch `checks` (D-020, D-021): new field `checks` (who verified a value: `ai:<model>` or `person:<name>`, date, method), rule P03, and 297 Arabic values of the abwāb table raised to `source-verified` with a check by `ai:claude-fable-5.2`. Also `tools/render_tables.py` and the generated page `docs/tables.md` (the reference tables in readable form), a reading guide in the README, 26 tests. Charter 0.5.

**Finding:** the two traditions classify اسلنقى differently. *Matn*: bāb 35, mulḥaq, pattern اِفْعَنْلَى (= Wright's Form XV). Wright §71 (p. 49): example of the third quadriliteral Form. Both are recorded in bāb 35.

**In `openarabee-quran`:** README, `LICENSING.md`, `CLAUDE.md`, `LICENSE` on `main`. No data.

**In `openarabee-web`:** the start page is live (`index.html`, `404.html`, `CNAME`). Branch `legal` holds a draft `impressum.html` (legal notice and privacy notice in German) **with placeholders; it must not be merged before the owner's details are filled in**.

**What is not verified (do not present it as more than it is)**
- The `source-verified` values of the abwāb table were checked only by the AI model that also made the first transcription. An independent check (the owner as native speaker, or another model) is still missing; `docs/tables.md` is made for that.
- Still `draft`: the whole Forms table (only one witness), the group labels, English readings and Western equivalents of the abwāb table, the maṣdar pattern of bāb 18 (witnesses differ), the statements of use of abwāb 9 and 18.
- Wright: §§36–62 (Forms I–XI) and §§91–93 (imperfect vowel) are known only from the text layer of the scan.
- Authorship of the Matn is uncertain (al-Danqazī in the 1949 printing, al-Kafawī in a library record of an 1899 collection).
- Bibliographic details of the dictionaries in the register are `draft`; printings are chosen in sub-phase 1b.
- The end of the Matn (p. 568 ff.: sālim / non-sālim, ṣaḥīḥ, mithāl, ajwaf, nāqiṣ, lafīf …) is not transcribed; the root types in `tools/oa/arabic.py` follow the charter's list and still need their Arabic terms with sources. First task of 1a.
- The legal texts in the branch `legal` are drafts by the AI, not legal advice (O-11).

**Owner to-dos**
1. `openarabee-core`: open and merge the pull request `checks` → `main` (wait for the green check).
2. Spot check as native speaker: read `docs/tables.md` and report anything that looks wrong; the AI then adds a `person:` check for the rows he confirms.
3. O-11: decide who is named in the legal notice and with which address, send name, address, e-mail and a second contact channel; the AI fills `impressum.html`, then merge `legal`.
4. Still open from the founding session: repository descriptions under *About*; two-factor authentication.
5. O-1 (reviewer), O-9 (legal review of the CLA draft).

**Next: Phase 1a, in a new session**
1. Transcribe the end of the Matn (pp. 568 ff.) and add the Arabic terms for root types with sources (also Shadhā al-ʿArf).
2. Root list from the Quranic Arabic Corpus counts (in `openarabee-quran`, see O-4).
3. Coverage matrix Form/bāb × root type; add roots until every existing cell has an example.

## Domain and website
DNS at Namecheap (set by the owner on 2026-11-16): four `A` records for `@` (`185.199.108.153`, `.109.153`, `.110.153`, `.111.153`) and `CNAME www → openarabee.github.io.`; mail forwarding untouched. GitHub Pages: `openarabee-web`, branch `main`, root; custom domain `openarabee.com`; DNS check successful; *Enforce HTTPS* on. A push to `main` of `openarabee-web` publishes within a minute or two.

## Backup to Google Drive
`tools/backup.sh` writes a verified `git bundle` (restore: `git clone <file>.bundle`). Upload it to the Drive folder «OpenArabee-Backups» (id `1rcwM0TS1l1f9szQKrLzIhfPwZMYJlphl`, created by the connector, so Claude can write there). The owner's folder «OpenArabee» is read-only for Claude. If an upload fails with a missing-permission error, the owner has to reconnect Google Drive in the Claude settings. The owner keeps a copy of the typed reading copy of the Matn in the same folder.

## Working agreements with the owner
- Conversation in **German**; project files in English; content Arabic + English.
- Claude does the work; the owner decides strategy and approves anything public, irreversible, paid or licence-related. Work on branches; the owner merges (D-019).
- The owner is a native Arabic speaker with a CS background (Python); wants to learn effective AI use — explain choices briefly.
- Mark decisions as provisional; record changes in the charter's decision log.
- No access to the owner's Namecheap account needed; the owner enters DNS values himself.
- Pull requests: `gh` is not authenticated, so Claude pushes a branch and gives the owner the link `https://github.com/OpenArabee/<repo>/compare/main...<branch>`; the owner clicks *Create pull request* twice, then *Merge* and *Confirm*.
- Model use: Fable 5.2 for architecture/schema and hard linguistic questions, Opus 5.5 for implementation.

## Practical notes for AI sessions
- The workspace shell reaches only GitHub and the package registries. Sources are read with web fetch or the cloud browser.
- Web fetch does not return long verbatim text and garbles vowelled Arabic from PDFs. For transcription, read page images in the cloud browser.
- Internet Archive page images open directly: `https://archive.org/download/<item>/page/n<leaf>_w1000.jpg`. Wright vol. I (`grammarofarabicl01caspuoft`): printed page p is leaf n(p+17). The Matn (`1369_20220720`): printed page p is leaf n(p-1). Take region screenshots at scale 1.4 to 2.
- PDFs in the cloud browser: `#page=N&view=Fit`, then PageDown.
- The QNL page viewer (ediscovery.qnl.qa) shows no images, neither in the cloud browser nor for the owner.
- `google-chrome --headless=new --no-sandbox --screenshot=…` renders local HTML for a visual check.
- To update a project doc with `project_write` from a file, the file must have been read in full and then changed only with the Edit or Write tool.
