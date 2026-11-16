# OpenArabee — Session handoff

Read this together with `docs/charter.md` at the start of every new session. Update it at the end of every session.

## State on 2026-11-16 (end of the Phase 0 session)

**Phase 0 is closed apart from the owner's merges listed below.** `openarabee-core`: pull request #1 (`phase-0`) is merged into `main`; the branch `phase-0-collation` carries the collation and waits for a second pull request.

**In `openarabee-core`**
- Project files, licences, schema v0, `docs/data-model.md`, source register (24 works), validator with 22 tests and green CI: merged.
- `reference/forms.wright.json`: all 19 patterns collated with the page images of Wright vol. I (§35 p. 29, §68 p. 48).
- `reference/abwab.bina-35.json` (branch `phase-0-collation`): **all 35 abwāb collated entry by entry against the printed edition** *Majmūʿ muhimmāt al-mutūn*, 4th printing, Cairo, Muṣṭafā al-Bābī al-Ḥalabī, 1369/1949, pp. 557–568. Every `loc` now gives the page of that printing; group labels use the wording of the text. The print confirmed every value; it has افعيلالا for bāb 18 (the typed reading copy had a slip there).
- O-2, O-6 (for the two reference works) and O-8 are done. Charter 0.4.

**Finding:** the two traditions classify اسلنقى differently. *Matn*: bāb 35, mulḥaq, pattern اِفْعَنْلَى (= Wright's Form XV). Wright §71 (p. 49): example of the third quadriliteral Form. Both are recorded in bāb 35.

**In `openarabee-quran`:** `main` has a placeholder README; branch `phase-0` (README, `LICENSING.md`, `CLAUDE.md`, `LICENSE`) waits for its pull request. No data.

**In `openarabee-web`:** branch `landing` holds a single start page (`index.html`, `404.html`, `CNAME`, assets). Not merged, GitHub Pages not switched on yet.

**What is not verified (do not present it as more than it is)**
- Every value in both reference tables still has status `draft`: the charter defines the higher statuses for verb entries only (open point O-10, owner decides).
- Wright: §§36–62 (Forms I–XI) and §§91–93 (imperfect vowel) are known only from the text layer of the scan, not from the page images.
- Authorship of the Matn is uncertain: the 1949 printing names Mullā ʿAbd Allāh al-Danqazī, a library record of an 1899 collection names al-Kafawī (see register).
- Bibliographic details of the dictionaries in the register are `draft`; printings are chosen in sub-phase 1b.
- The end of the Matn (p. 568 ff.: sālim / non-sālim, ṣaḥīḥ, mithāl, ajwaf, nāqiṣ, lafīf …) is not transcribed; the root types in `tools/oa/arabic.py` follow the charter's list and still need their Arabic terms with sources. First task of 1a.
- The Arabic tagline on the start page was written by the AI; the owner should check it.

**Owner to-dos**
1. `openarabee-core`: open and merge the pull request `phase-0-collation` → `main`.
2. `openarabee-quran`: open and merge the pull request `phase-0` → `main`.
3. `openarabee-web`: look at the start page, open and merge `landing` → `main`, then *Settings → Pages → Deploy from a branch → main / (root)*, custom domain `openarabee.com`, later tick *Enforce HTTPS*.
4. Decide O-10 (statuses of reference tables) and think about O-11 (Impressum and privacy notice).
5. Still open from the founding session: repository descriptions under *About*; two-factor authentication.
6. O-1 (reviewer), O-9 (legal review of the CLA draft).

**Next: Phase 1a, in a new session**
1. Transcribe the end of the Matn (pp. 568 ff.) and add the Arabic terms for root types with sources (also Shadhā al-ʿArf).
2. Root list from the Quranic Arabic Corpus counts (in `openarabee-quran`, see O-4).
3. Coverage matrix Form/bāb × root type; add roots until every existing cell has an example.

## Domain and website
DNS at Namecheap was set by the owner on 2026-11-16 (screenshot): four `A` records for `@` (`185.199.108.153`, `.109.153`, `.110.153`, `.111.153`) and `CNAME www → openarabee.github.io.`; the parking record and the URL redirect are gone; mail forwarding untouched. Until GitHub Pages is switched on for `openarabee-web`, the domain shows GitHub's "not found" page. GitHub recommends verifying the domain for the organisation (organisation settings → Pages).

## Backup to Google Drive
`tools/backup.sh` writes a verified `git bundle` (restore: `git clone <file>.bundle`). Upload it to the Drive folder «OpenArabee-Backups» (id `1rcwM0TS1l1f9szQKrLzIhfPwZMYJlphl`, created by the connector, so Claude can write there). The owner's folder «OpenArabee» is read-only for Claude. If an upload fails with a missing-permission error, the owner has to reconnect Google Drive in the Claude settings.

## Working agreements with the owner
- Conversation in **German**; project files in English; content Arabic + English.
- Claude does the work; the owner decides strategy and approves anything public, irreversible, paid or licence-related. Work on branches; the owner merges (D-019).
- The owner is a native Arabic speaker with a CS background (Python); wants to learn effective AI use — explain choices briefly.
- Mark decisions as provisional; record changes in the charter's decision log.
- No access to the owner's Namecheap account needed; the owner enters DNS values himself.
- Model use: Fable 5.2 for architecture/schema and hard linguistic questions, Opus 5.5 for implementation.

## Practical notes for AI sessions
- The workspace shell reaches only GitHub and the package registries. Sources are read with web fetch or the cloud browser.
- Web fetch does not return long verbatim text and garbles vowelled Arabic from PDFs. For transcription, read page images in the cloud browser.
- Internet Archive page images open directly: `https://archive.org/download/<item>/page/n<leaf>_w1000.jpg`. For Wright vol. I (`grammarofarabicl01caspuoft`) printed page p is leaf n(p+17). Take region screenshots at scale 2.
- PDFs in the cloud browser: `#page=N&view=Fit`, then PageDown.
- The QNL page viewer (ediscovery.qnl.qa) shows no images, neither in the cloud browser nor for the owner.
- For the Matn (`1369_20220720` on the Internet Archive) printed page p is leaf n(p-1).
- `google-chrome --headless=new --no-sandbox --screenshot=…` renders local HTML for a visual check.
- `gh` is not authenticated in the workspace; pushing works through git.
