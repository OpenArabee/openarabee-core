# OpenArabee — Session handoff

Read this together with `docs/charter.md` at the start of every new session. Update it at the end of every session.

## State on 2026-11-15 (end of the founding session)

**Done**
- Charter v0.1 (en + de) written; also stored in the Claude project «اللغة العربية» (`OpenArabee/charter.md`, `charter.de.md`).
- Domain **openarabee.com** registered at Namecheap (no hosting, auto-renew on, WHOIS privacy on). DNS not configured yet.
- GitHub organisation **OpenArabee**; public repos `openarabee-core`, `openarabee-quran` (empty). Claude GitHub App installed on the org with *All repositories*; push access confirmed.
- First commit on `main` in `openarabee-core`: README, charter (en/de), logo.
- Logo redrawn as SVG and approved by the owner (`assets/`, built with `assets/build_logo.py`, font Inter Display SemiBold, colours navy `#0A2A45`, gold `#C29A52`).
- Trademark exact-name search "OpenArabee" at DPMA, EUIPO, WIPO: no hits.
- Quran statistics in charter §9 were computed from Quranic Arabic Corpus v0.4 (mirror: `github.com/cltk/arabic_morphology_quranic-corpus`).

**Owner to-dos (small)**
- Set default branch of `openarabee-core` to `main`, delete branch `access-test` (left over from the access test).
- Add repo descriptions + website `https://openarabee.com` under *About*.
- Check two-factor authentication on GitHub.

**Next: Phase 0** (charter §4), suggested order
1. `CLAUDE.md` in both repos (derived from the charter: rules on sources, provenance, licences, language, asking before public/irreversible steps).
2. Licence files: `LICENSE` (MIT, code) + `LICENSE-DATA` (CC BY 4.0); CLA text; CONTRIBUTING; issue template "Suggest a correction".
3. Folder structure, JSON Schema v0 (charter §5), ID/transliteration scheme (open point O‑2).
4. Source register (`sources/register.json`) with the works from charter §6, citable printings (O‑6).
5. Reference tables: 35 abwāb (from *Matn al-Bināʾ*) and Forms I–XV/QI–QIV (Wright), each with sources.
6. Validation script + GitHub Actions CI.
7. `openarabee-quran`: README, licence notes (Tanzil CC BY 3.0 verbatim; QAC non-commercial research).
8. Backup to Google Drive (below).

**Backup to Google Drive — known limitation**
The Drive connector can only write into folders it created itself. The owner's folder «OpenArabee» (My Drive) is read-only for Claude. Plan: create a folder «OpenArabee-Backups», upload `git bundle` files there; the owner may move it into «OpenArabee».

## Working agreements with the owner
- Conversation in **German**; project files in English; content Arabic + English.
- Claude does the work; the owner decides strategy and approves anything public, irreversible, paid or licence-related.
- The owner is a native Arabic speaker with a CS background (Python); wants to learn effective AI use — explain choices briefly.
- Mark decisions as provisional; record changes in the charter's decision log.
- No access to the owner's Namecheap account needed; DNS values will be given to the owner to enter (Phase 1d).
- Model use: Fable 5.2 for architecture/schema and hard linguistic questions, Opus 5.5 for implementation.
