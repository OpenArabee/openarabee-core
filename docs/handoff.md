# OpenArabee — Session handoff

Read this together with `docs/charter.md` at the start of every new session. Update it at the end of every session.

## State on 2026-11-15 (end of the Phase 0 session)

**Phase 0 is built and waits for the owner's review.** Nothing is merged: the work sits on the branch `phase-0` in both repositories.

**Done in `openarabee-core` (branch `phase-0`)**
- `CLAUDE.md`, `CONTRIBUTING.md`, `LICENSE` (MIT), `LICENSE-DATA` (CC BY 4.0, text from the SPDX licence list), issue form "Suggest a correction", `CLA.md` (draft, not in force).
- Schema v0 in `schema/` (five JSON Schema files), documented in `docs/data-model.md`.
- ID scheme proposed (open point O-2 → D-015): `r-ktb`, `v-ktb-1`, `bina-01`; tool `tools/oa/ids.py`.
- `sources/register.json`: 24 works with rights and layer (`core` / `quran-layer` / `cross-check`).
- `reference/abwab.bina-35.json`: all 35 abwāb with pattern, model verb, maṣdars, examples and Western equivalent. Read page by page from the typed reading copy (takw.in, pp. 2–15).
- `reference/forms.wright.json`: Forms I–XV, QI–QIV with paragraph and page in Wright vol. I.
- `tools/validate.py` (rules F, S, G, P, T, D and release rules R; list in `docs/data-model.md` §7), 22 tests, GitHub Actions workflow `.github/workflows/validate.yml`.
- `tools/backup.sh`; charter raised to 0.2 (D-015 to D-019, O-2, O-6, new O-8, O-9), German version in step.

**Done in `openarabee-quran`**
- `main`: placeholder README only (an empty repository cannot take a pull request).
- Branch `phase-0`: README, `LICENSING.md`, `CLAUDE.md`, `LICENSE` (MIT for scripts). No data.

**What is not verified (do not present it as more than it is)**
- Every value in both reference tables has status `draft`.
- The abwāb come from a modern typed copy without publication details, not from a printed edition. It has at least one slip: for bāb 18 it prints the maṣdar pattern as افعيعالا; the table has اِفْعِيلَال, taken from the model maṣdar احميرار on the same line (noted in the entry).
- Wright: paragraph and page numbers come from the text layer of a scan (start pages from the table of contents). His Arabic is illegible there, so the patterns of the Forms are the standard citation forms and were **not** compared with his printed table (O-8).
- Bibliographic details of all Arabic works in the register are `draft`; only Wright's edition is confirmed.
- Pages 15–18 of the reading copy (sālim / non-sālim, kinds of weak verbs) were not transcribed; the root types in `tools/oa/arabic.py` follow the charter's list and still need their Arabic terms and sources.
- The domain and GitHub Pages part of Phase 0 (charter §4) is not done; the handoff of the founding session moved DNS to Phase 1d.

**Owner to-dos**
1. Review and merge the two pull requests (branch `phase-0` → `main`). Merging is the approval of: the licence files, the licence split (D-018), the ID scheme (D-015), the spelling rules (D-017).
2. Check that the first run of the *validate* workflow is green (Actions tab of `openarabee-core`); it could not be checked from the session.
3. Still open from the founding session: repository descriptions and website under *About*; two-factor authentication. (Default branch is `main` and `access-test` no longer exists: done.)
4. Store the two `.bundle` files from the chat in Google Drive (folder «OpenArabee»), and reconnect the Drive connector with write permission if Claude should upload backups itself.
5. O-1 (reviewer), O-9 (legal review of the CLA draft).

**Next session: finish Phase 0, then Phase 1a**
1. O-6: choose a printed edition of *Matn al-Bināʾ* (old Cairo printing in a collection of mutūn) and collate all 35 entries against its page images; switch `loc` to that edition.
2. O-8: collate Wright §35 and §§66–72 against the page images (Internet Archive); settle whether Wright lists اسلنقى under QIII.
3. Add the Arabic terms for root types with sources (Shadhā al-ʿArf, Matn al-Bināʾ pp. 15–18).
4. Phase 1a: root list from the Quranic Arabic Corpus counts (in `openarabee-quran`, see O-4), coverage matrix Form/bāb × root type.

## Backup to Google Drive
`tools/backup.sh` writes a verified `git bundle` (restore: `git clone <file>.bundle`). On 2026-11-15 the Drive connector could read but not write (creating the folder «OpenArabee-Backups» and uploading both failed with a missing-permission error), so the two bundles were handed to the owner as files in the chat to store in Drive himself. To let Claude upload: reconnect Google Drive in the Claude settings and allow file creation. The owner's folder «OpenArabee» stays read-only for Claude either way; the plan is a folder «OpenArabee-Backups» created by the connector.

## Working agreements with the owner
- Conversation in **German**; project files in English; content Arabic + English.
- Claude does the work; the owner decides strategy and approves anything public, irreversible, paid or licence-related. Work on branches; the owner merges (D-019).
- The owner is a native Arabic speaker with a CS background (Python); wants to learn effective AI use — explain choices briefly.
- Mark decisions as provisional; record changes in the charter's decision log.
- No access to the owner's Namecheap account needed; DNS values will be given to the owner to enter (Phase 1d).
- Model use: Fable 5.2 for architecture/schema and hard linguistic questions, Opus 5.5 for implementation.

## Practical notes for AI sessions
- The workspace shell reaches only GitHub and the package registries. Sources are read with web fetch or the cloud browser.
- Web fetch does not return long verbatim text and garbles vowelled Arabic from PDFs. For transcription, open the PDF in the cloud browser and read the page images (`#page=N&view=Fit`, then PageDown).
- `gh` is not authenticated in the workspace; pushing works through git.
