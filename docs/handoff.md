# OpenArabee — Session handoff

Read this together with `docs/charter.md` at the start of every new session. Update it at the end of every session.

## State on 2026-11-16 (Phase 0 session, continued)

**Phase 0 is built; one item is left open (collation of the abwāb with a printed edition).** The work sits on the branch `phase-0` in both repositories. Pull request #1 in `openarabee-core` is open with all checks green; the owner has not merged yet.

**Done in `openarabee-core` (branch `phase-0`)**
- `CLAUDE.md`, `CONTRIBUTING.md`, `LICENSE` (MIT), `LICENSE-DATA` (CC BY 4.0, text from the SPDX licence list), issue form "Suggest a correction", `CLA.md` (draft, not in force).
- Schema v0 in `schema/` (five JSON Schema files), documented in `docs/data-model.md`.
- ID scheme proposed (open point O-2 → D-015): `r-ktb`, `v-ktb-1`, `bina-01`; tool `tools/oa/ids.py`.
- `sources/register.json`: 24 works with rights and layer (`core` / `quran-layer` / `cross-check`).
- `reference/abwab.bina-35.json`: all 35 abwāb with pattern, model verb, maṣdars, examples and Western equivalent. Arabic values read page by page from the typed reading copy (takw.in, pp. 2–15).
- `reference/forms.wright.json`: Forms I–XV, QI–QIV. **Collated on 2026-11-16 against the page images** of Wright vol. I: table in §35 (p. 29) and table in §68 (p. 48); all 19 patterns agree. §66 and §§67–72 read in full.
- Western equivalents of the abwāb now cite the exact place in Wright; where Wright prints the Matn's model verb itself, the entry says so.
- `tools/validate.py` (rules F, S, G, P, T, D and release rules R; list in `docs/data-model.md` §7), 22 tests, GitHub Actions workflow (green).
- `tools/backup.sh`; charter 0.3 (D-015 to D-019, O-2, O-6, O-8, O-9), German version in step.

**Finding (O-8, closed):** the two traditions classify اسلنقى differently. *Matn al-Bināʾ*: bāb 35, mulḥaq, pattern اِفْعَنْلَى (= Wright's Form XV). Wright §71 (p. 49): example of the third quadriliteral Form. Both are recorded in bāb 35 (`relation: exact` for XV, `relation: model-verb` for QIII). This is the first real case for charter principle 6.

**Done in `openarabee-quran`**
- `main`: placeholder README only. Branch `phase-0`: README, `LICENSING.md`, `CLAUDE.md`, `LICENSE`. No data. Pull request not opened yet.

**`openarabee-web`** exists (created by the owner on 2026-11-16), nothing built yet.

**What is not verified (do not present it as more than it is)**
- Every value in both reference tables still has status `draft`.
- The Arabic values of the abwāb come from a modern typed copy without publication details. It has at least one slip: for bāb 18 it prints the maṣdar pattern as افعيعالا; the table has اِفْعِيلَال, taken from the model maṣdar احميرار on the same line (noted in the entry).
- Proposed printed edition for the Matn (O-6): Azhar collection, Cairo, al-Maṭbaʿa al-Jamāliyya, 1329/1911, Qatar National Library `QNL:00022512` (alternative: 1317/1899 collection, `QNL:00005293`). **Only the catalogue records were read; the page viewer of QNL did not load in the session's cloud browser**, so the edition has not been seen and nothing has been collated against it.
- Wright: §§36–62 (Forms I–XI) and §§91–93 (imperfect vowel) are known only from the text layer of the scan, not from the page images.
- Bibliographic details of all Arabic works in the register are `draft`; only Wright's edition is confirmed.
- Pages 15–18 of the reading copy (sālim / non-sālim, kinds of weak verbs) were not transcribed; the root types in `tools/oa/arabic.py` follow the charter's list and still need their Arabic terms and sources.

**Owner to-dos**
1. Merge pull request #1 in `openarabee-core`; open and merge the pull request `phase-0` → `main` in `openarabee-quran`. Merging approves the licence files, D-015, D-017 and D-018.
2. Help with O-6 (five minutes): open https://ediscovery.qnl.qa/islandora/object/QNL:00022512 in your own browser, press *Launch Item Viewer*, and send screenshots of the pages of متن البناء (or say that it does not load for you either).
3. Download the reading copy https://takw.in/files/البناء%20والأساس.pdf and put it into the Drive folder «OpenArabee» (private copy, so the basis of the current table cannot disappear).
4. Still open from the founding session: repository descriptions and website under *About*; two-factor authentication.
5. O-1 (reviewer), O-9 (legal review of the CLA draft).

**Next steps for the AI**
1. O-6: collate all 35 abwāb against the printed edition once its pages are available; switch every `loc` to edition + page; then raise statuses where the charter's conditions are met.
2. Add the Arabic terms for root types with sources (Shadhā al-ʿArf, Matn al-Bināʾ pp. 15–18).
3. Phase 1a (new session): root list from the Quranic Arabic Corpus counts (in `openarabee-quran`, see O-4), coverage matrix Form/bāb × root type.

## Domain and website (Phase 1d, values already known)
State of the Namecheap DNS on 2026-11-16 (owner's screenshots): nameservers *Namecheap BasicDNS*; host records `CNAME www → parkingpage.namecheap.com.` and `URL Redirect @ → http://www.openarabee.com/`; mail setting *Email Forwarding* (one locked SPF TXT record). Nothing points to GitHub yet.

When a site exists in `openarabee-web` and GitHub Pages is switched on with the custom domain `openarabee.com`:
- delete the two existing host records (parking CNAME and URL redirect);
- add four `A` records, host `@`, values `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`;
- add one `CNAME` record, host `www`, value `openarabee.github.io.`;
- leave the mail settings as they are;
- afterwards tick *Enforce HTTPS* in the Pages settings (can take up to 24 hours to become available).
Values from GitHub's documentation (read 2026-11-16); re-check them before use. GitHub recommends verifying the domain for the organisation first (organisation settings → Pages).

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
- The QNL page viewer (ediscovery.qnl.qa) shows no images in the cloud browser.
- `gh` is not authenticated in the workspace; pushing works through git.
