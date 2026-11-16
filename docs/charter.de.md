# OpenArabee – Projekt-Charta (deutsche Fassung)

| | |
|---|---|
| **Version** | 0.5 (Entwurf) – 16.11.2026 (Phase 0 abgeschlossen: Abwāb an einem Druck geprüft; O‑2, O‑6, O‑8, O‑10 erledigt; D‑020, D‑021; offen O‑11) |
| **Eigentümer** | Obada Obaid (GitHub: `obadaobaid`, Organisation: `OpenArabee`) |
| **Status** | **Alle Entscheidungen sind vorläufig.** Änderungen laufen über das Entscheidungsprotokoll (Abschnitt 12). |
| **Maßgeblich** | Die englische Fassung `charter.md`. Bei Abweichungen gilt sie. |
| **Domain / Marke** | openarabee.com · Logo: `assets/logo.png` · Farben: Dunkelblau ≈ `#0A2A45`, Gold ≈ `#C29A52` |

Diese Charta ist die gemeinsame Grundlage für jede Arbeitssitzung, ob Mensch oder KI. Die `CLAUDE.md` in jedem Repo wird daraus abgeleitet.

---

## 1. Zweck

OpenArabee baut einen **offenen, geprüften Datensatz zur arabischen Morphologie mit Quellenangabe**. Er beginnt bei den häufigsten Wurzeln des Korans und wird zu Lernwerkzeugen weiterentwickelt.

**Das Besondere:** Jedes Verb wird in **beiden** grammatischen Traditionen beschrieben, nach den klassischen arabischen Abwab (أبواب التصريف) und nach den westlichen Formen (I–XV, QI–QIV). **Jede einzelne Angabe trägt ihre Quelle und ihren Prüfstatus.**

**Ziele**
1. Die Sprache des Korans und Arabisch allgemein leichter lernbar und verständlich machen.
2. Saubere, offen lizenzierte, geprüfte Daten bereitstellen, auf die sich Software und KI verlassen können.
3. Datengrundlage für Produkte sein: zuerst eine Website, später das Buch »الجذور المئة«, Apps und Datensätze.

**Was das Projekt nicht ist**
- kein vollständiges Wörterbuch und kein Tafsir, keine religiösen Urteile
- keine Kopie geschützter Wörterbücher oder Datenbanken
- kein neuer morphologischer Analysator; vorhandene offene Werkzeuge werden genutzt

---

## 2. Grundsätze

1. **Klein und nützlich anfangen.** Wurzel für Wurzel wachsen; jede Phase endet mit etwas Nutzbarem.
2. **Quelle pro Angabe.** Kein Wert ohne Quellenverweis. KI-Ausgabe allein ist nie eine Quelle.
3. **Sichtbare Verlässlichkeit.** Jeder Eintrag zeigt öffentlich seinen Prüfstatus.
4. **Saubere Rechte.** Der Kern enthält nur Material, das kommerzielle Nutzung erlaubt. Alles andere liegt in einer eigenen Ebene.
5. **Ehrliche Aussagen.** Keine Werbezahlen, die wir nicht selbst nachgerechnet haben.
6. **Beide Traditionen, neutral.** Wo Quellen unterschiedlich einordnen, werden alle Einordnungen mit Quelle gespeichert.
7. **Umkehrbare Entscheidungen.** Alles ist versioniert; Planänderungen laufen über das Protokoll.

---

## 3. Die zwei Systeme

Beide Systeme beschreiben dieselben Verben, nur unterschiedlich fein. Sie sind keine Konkurrenten.

- Die **westlichen Formen I–X** sind dasselbe wie »الأوزان العشرة«. Die Nummerierung ist eine europäische Konvention seit Erpenius (1613).
- Die **35 Abwab** stammen aus dem Lehrtext **متن البناء**. Andere klassische Autoren zählen anders; »35« ist ein Zählschema, nicht *das* offizielle System. Darum speichert das Datenmodell zu jeder Einordnung das Schema.
- Das klassische System ist an vier Stellen feiner: Form I in sechs Abwab nach Vokal, seltene Formen XI–XV, vierradikalige Verben und الملحق بالرباعي.
- **Der Bab gehört zum Verb, nicht zur Wurzel** (حَسِبَ und حَسَبَ). Er lässt sich nicht berechnen, sondern muss pro Verb nachgeschlagen werden.

| Klassische Gruppe | Anzahl | Westlich |
|---|---|---|
| ثلاثي مجرد | 6 | Form I + Vokalklasse |
| ثلاثي مزيد بحرف | 3 | IV, II, III |
| ثلاثي مزيد بحرفين | 5 | VII, VIII, IX, V, VI |
| ثلاثي مزيد بثلاثة | 4 | X, XII, XIII, XI |
| رباعي مجرد | 1 | QI |
| ملحق بالرباعي المجرد | 6 | meist wie QI |
| رباعي مزيد بحرف | 1 | QII |
| ملحق بـ«تفعلل» | 5 | meist wie QII |
| رباعي مزيد بحرفين | 2 | QIII, QIV |
| ملحق بـ«افعنلل» | 2 | XIV, XV (Wright führt das Verb اسلنقى selbst unter QIII, §71) |
| **Summe** | **35** | |

Die vollständige Tabelle mit allen Mustern steht in der englischen Fassung.

---

## 4. Phasen

Nur Phase 1 ist im Detail geplant. Jede Phase wird bei Beginn in Unterphasen zerlegt.

| Phase | Inhalt | Ergebnis |
|---|---|---|
| **0 – Einrichtung** | Repos, Lizenzen, `CLAUDE.md`, Schema v0, Quellenregister, Referenztabellen, Prüfskripte, Sicherung, Domain + GitHub Pages | lauffähiges, geprüftes, noch leeres Projekt |
| **1 – Die 100 Wurzeln** | die 100 häufigsten Koranwurzeln plus Ergänzungen für alle Formen, Abwab und Wurzeltypen | Datensatz v0.1 + Website v1 |
| **2 – Wachstum** | 300–500 Wurzeln, Nomen, Feedback-Prozess mit Rollen, Beitragsvereinbarung | Datensatz v0.5 |
| **3 – Produkte** | Buch »الجذور المئة«, Anki-Decks, Apps, Deutsch | erste Produkte |
| **4 – Daten für KI** | Testdatensatz für KI-Modelle, Trainingsdaten, API, OntoLex-Export | Angebot für Forschung und Entwicklung |

**Phase 1 im Detail**
- **1a:** Wurzelliste festlegen; Abdeckungsmatrix **Form/Bab × Wurzeltyp**; Lücken mit Zusatzwurzeln füllen.
- **1b:** Verbeinträge mit den Pflichtfeldern anlegen.
- **1c:** Koran-Ebene: Anzahl und 1–3 Beispielverse pro Verb.
- **1d:** Website v1 mit Quellen per Mouseover und Knopf »Korrektur vorschlagen«.
- **1e:** erste Prüfrunde durch Fachleute, Release v0.1 mit DOI (Zenodo).

**Abschluss von Phase 1:** alle Pflichtfelder gefüllt; jeder Wert mit mindestens einer Nicht-KI-Quelle; alle Einträge maschinell geprüft; mindestens das Gold-Set von Fachleuten geprüft; Website online.

---

## 5. Datenmodell (Skizze)

**Grundformat:** JSON-Dateien mit stabilen IDs, eine Datei pro Wurzel, geprüft durch ein JSON-Schema. Alle anderen Formate (SQLite, CSV, Graph, Website) werden daraus **erzeugt**, nie von Hand bearbeitet.

**Pflichtfelder pro Verb in Phase 1:** Wurzel + Wurzeltyp · Form · Bab (bei Form I: welcher der sechs) · Perfekt und Präsens mit Vokalzeichen · Masdar(s) · transitiv ja/nein · kurze Bedeutung (ar + en) · Koran: Anzahl und 1–3 Beispiele · **Quelle und Status für jedes Feld**.

**Prüfstatus (auf der Website sichtbar):**
`Entwurf` → `maschinell geprüft` → `durch Quellen bestätigt` → `von 1 Fachperson geprüft` → `von 2 Fachpersonen bestätigt`

---

## 6. Quellen

**Regel:** Der Kern entsteht nur aus Quellen, die kommerzielle Nutzung erlauben. Geschützte Werke schlägt ein Mensch bei einzelnen Widersprüchen nach; nichts wird daraus systematisch übernommen.

| Rolle | Werk | Rechte |
|---|---|---|
| Klassisches Gerüst (35 Abwab) | متن البناء | gemeinfrei |
| Klassische Erklärung | شذا العرف (الحملاوي, gest. 1932) | gemeinfrei |
| Klassische Autorität bei Streitfragen | شرح الشافية للرضي | Werk gemeinfrei, Ausgabe prüfen |
| Westliches Gerüst (Formen I–XV) | Wright, 3. Aufl. 1896–98 | gemeinfrei |
| Bab pro Verb | مختار الصحاح، المصباح المنير | gemeinfrei |
| Präsensvokal, Masdar, Englisch | Lane's Lexicon | Werk gemeinfrei; Digitaltext CC BY-SA → Druck zitieren |
| Maschinenlesbare Daten | Wikidata (CC0), Camel Morph (CC BY 4.0) | Kern |
| Korantext | Tanzil (CC BY 3.0, unverändert) | Koran-Ebene |
| Koran-Morphologie | Quranic Arabic Corpus (nur Forschung) | **nur Koran-Ebene** |
| Nur zum Gegenprüfen | Qutrub, Arramooz (GPL); Hans Wehr, Doha-Wörterbuch (geschützt); OpenITI (nicht kommerziell) | nie in den Kern |

**Hinweise (keine Rechtsberatung):** Werke sind 70 Jahre nach dem Tod des Autors gemeinfrei; neue kritische Ausgaben können 25 Jahre geschützt sein, deshalb alte Drucke bevorzugen. Vor kommerzieller Nutzung einmal anwaltlich beraten lassen.

---

## 7. Qualitätssicherung

1. **Gold-Set** von 200–500 Verben, von einer Fachperson geprüft.
2. **Zwei unabhängige Werkzeuge** für die Konjugation; Abweichungen werden von Hand geprüft.
3. **Automatische Regeln** (Schema, Vokalmuster passt zum Bab, jede Quelle existiert im Register).
4. **Prüfung durch ein anderes KI-Modell** als das, das den Eintrag erzeugt hat.
5. **Öffentlicher Korrekturkanal** über GitHub; Rollen und Gewichtung später, keine eigenen Konten am Anfang.
6. **Stichproben durch den Eigentümer** bei jedem Release.

---

## 8. Lizenzen und Repos

| Punkt | Entscheidung |
|---|---|
| Code | MIT |
| Kerndaten und eigene Texte | CC BY 4.0 |
| Beiträge | Beitragsvereinbarung (CLA) ab dem ersten Fremdbeitrag |
| Koran-Ebene | eigenes Repo; Bedingungen der Quellen gelten |

**Repos (alle öffentlich):** `openarabee-core`, `openarabee-quran`, später `openarabee-web`.

**Sicherung:** GitHub + `git bundle` in Google Drive nach jeder Sitzung + Releases auf Zenodo.

---

## 9. Nachgerechnete Zahlen

Aus dem Quranic Arabic Corpus v0.4 (77.429 Wörter):

| Aussage | Wert |
|---|---|
| verschiedene Wurzeln | 1.642 |
| Wörter ohne Wurzel | 35,5 % aller Wörter, nur 175 verschiedene Lemmata |
| die 100 häufigsten Wurzeln | 39,0 % aller Wörter |
| 100 Wurzeln + 50 Funktionswörter | 73,4 % aller Wörter |
| damit vollständig abgedeckte Verse | 9,9 % |
| Verbwurzeln / Formen pro Wurzel | 943 / 1,56 |

**Erlaubte Formulierung:** »Mit 100 Wurzeln und 50 kleinen Funktionswörtern erkennst du etwa drei von vier Wörtern im Koran wieder.« Aussagen wie »80 % Verständnis« verwenden wir nicht.

---

## 10. Arbeitsweise

| Wer | Aufgabe |
|---|---|
| **Eigentümer** | Strategie, Prioritäten, Freigaben, muttersprachliches Urteil, Fachleute gewinnen, Stichproben |
| **KI (Claude)** | Ausführung: Recherche, Schema, Code, Entwürfe, Prüfung, Doku, Sicherungen; fragt vor allem, was öffentlich oder unumkehrbar ist |
| **Fachleute** | prüfen die Inhalte; ihr Urteil geht vor Werkzeug und KI |

**Modelle:** Fable 5.2 für Architektur und schwierige Sprachfragen · Opus 5.5 / Sonnet für die Umsetzung · Sonnet / Haiku per Batch für Massenentwürfe · ein anderes Modell zur Prüfung.

**Sprachen:** Code und Doku Englisch; Inhalte Arabisch + Englisch, Deutsch ab Phase 3; Gespräche mit dem Eigentümer auf Deutsch.

---

## 11. Offene Punkte

| # | Frage | Wer |
|---|---|---|
| O‑1 | Mindestens eine Fachperson für das Gold-Set gewinnen | Eigentümer |
| O‑2 | Erledigt: ID- und Umschriftschema (D‑015, `docs/data-model.md` §2), vom Eigentümer per Merge am 16.11.2026 freigegeben | — |
| O‑3 | Beim Quranic Arabic Corpus nach Nutzungsbedingungen fragen | Eigentümer, später |
| O‑4 | Gehört die Wurzelliste in den Kern oder die Koran-Ebene? | Eigentümer, bei der Rechtsberatung |
| O‑5 | Logo: mit Google Gemini erstellt; KI-Bilder sind meist nicht urheberrechtlich geschützt. In Phase 0 als saubere SVG neu zeichnen | KI zeichnet, Eigentümer gibt frei |
| O‑6 | Zitierfähige Drucke. Erledigt für Wright (Cambridge 1896–98) und für den *Matn al-Bināʾ*: in *Majmūʿ muhimmāt al-mutūn*, 4. Druck, Kairo, Muṣṭafā al‑Bābī al‑Ḥalabī, 1369/1949, S. 557 ff.; alle 35 Abwāb am 16.11.2026 an den Seitenbildern geprüft. Offen für die Wörterbücher (Mukhtār, Miṣbāḥ, Lane und die Ersatzwerke): Drucke wählen, wenn in 1b die ersten Verbeinträge entstehen | KI schlägt vor, Eigentümer entscheidet |
| O‑7 | Marke eintragen lassen? (Suchen am 15.11.2026 ohne Treffer) | Eigentümer, später |
| O‑8 | Erledigt am 16.11.2026: Wrights Tabellen in §35 (S. 29) und §68 (S. 48) an den Seitenbildern geprüft; alle 19 Muster stimmen mit `reference/forms.wright.json` überein. Befund: Wright führt اسلنقى als Beispiel der dritten vierradikaligen Form (§71, S. 49), der *Matn* als Mulḥaq (Bāb 35, Muster der Form XV). Beide Einordnungen stehen in der Abwāb-Tabelle. Noch an den Seitenbildern zu lesen: §§36–62 und §§91–93 | KI |
| O‑9 | `CLA.md` ist ein Entwurf ohne rechtliche Prüfung und nicht in Kraft; vor dem ersten fremden Beitrag in der Rechtsberatung prüfen lassen | Eigentümer |
| O‑10 | Erledigt am 16.11.2026: entschieden als D‑020 und D‑021 | — |
| O‑11 | Website: Braucht openarabee.com nach deutschem Recht ein Impressum und eine Datenschutzerklärung, und mit welchen Kontaktdaten? Klären, bevor die Seite beworben wird; in der Rechtsberatung fragen | Eigentümer |

---

## 12. Entscheidungsprotokoll

Alle Einträge sind vorläufig. Die vollständige Liste (D‑001 bis D‑021) steht in der englischen Fassung. Kurzfassung:

- Name **OpenArabee**, Domain openarabee.com, Organisation `OpenArabee`
- Lizenzen MIT / CC BY 4.0 / CLA; zwei Ebenen (Kern und Koran)
- Referenzwerke متن البناء, شذا العرف, Wright; Bab pro Verb aus مختار الصحاح, المصباح المنير, Lane
- Phase 1 = 100 Wurzeln; das Buch wächst daraus
- JSON als Grundformat mit Quelle pro Feld
- erstes Produkt: Website auf GitHub Pages
- Korantext Tanzil Uthmani (Hafs)
- Sicherung per `git bundle` in Google Drive
- alle Repos öffentlich
- Charta zweisprachig, die englische Fassung ist maßgeblich
- IDs: ASCII, klein, ein Zeichen pro Wurzelbuchstabe (`r-ktb`, `v-ktb-1`, `bina-01`); veröffentlichte IDs ändern sich nie (D‑015)
- Schema v0: eine Datei pro Wurzel; Quellenangabe mit genauer Stelle; Wurzeltyp wird aus den Buchstaben abgeleitet (D‑016)
- einheitliche Schreibung arabischer Zitierformen (D‑017)
- Code und Schema MIT; Daten, Tabellen, Quellenregister und Doku CC BY 4.0 (D‑018)
- Arbeit auf Branches; der Eigentümer gibt per Merge frei (D‑019)
- Referenztabellen: `source-verified` heißt am zitierfähigen Druck geprüft und von einem zweiten Textzeugen bestätigt (D‑020)
- Jeder Wert nennt im Feld `checks`, wer ihn geprüft hat (`ai:<Modell>` oder `person:<Name>`, Datum, Methode), getrennt vom Status; die Fachstufen verlangen Prüfungen durch Personen (D‑021)
