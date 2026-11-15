"""Small Arabic text helpers shared by the OpenArabee tools (no dependencies)."""
from __future__ import annotations

import unicodedata

FATHA, DAMMA, KASRA, SUKUN, SHADDA = "َ", "ُ", "ِ", "ْ", "ّ"
TANWIN = "ًٌٍ"
DAGGER_ALIF = "ٰ"
DIACRITICS = FATHA + DAMMA + KASRA + SUKUN + SHADDA + TANWIN + DAGGER_ALIF
TATWEEL = "ـ"

# The 28 consonants that can be root radicals (alif is never a radical; hamza is).
RADICALS = "ءبتثجحخدذرزسشصضطظعغفقكلمنهوي"
WEAK = "وي"
HAMZA = "ء"
HAMZA_CARRIERS = "أإؤئآ"


def is_nfc(text: str) -> bool:
    return unicodedata.normalize("NFC", text) == text


def strip_diacritics(text: str) -> str:
    return "".join(ch for ch in text if ch not in DIACRITICS and ch != TATWEEL)


def tokenize(word: str) -> list[tuple[str, str]]:
    """Split a vowelled word into (letter, diacritics) pairs.

    A letter carrying shadda is expanded into two tokens, the first with sukun,
    so that اِحْمَرَّ and its pattern اِفْعَلَّ line up radical by radical.
    """
    tokens: list[tuple[str, str]] = []
    for ch in word:
        if ch == TATWEEL:
            continue
        if ch in DIACRITICS:
            if not tokens:
                raise ValueError(f"diacritic before any letter in {word!r}")
            letter, marks = tokens[-1]
            tokens[-1] = (letter, marks + ch)
        else:
            tokens.append((ch, ""))
    expanded: list[tuple[str, str]] = []
    for letter, marks in tokens:
        marks = "".join(sorted(marks))
        if SHADDA in marks:
            expanded.append((letter, SUKUN))
            expanded.append((letter, marks.replace(SHADDA, "")))
        else:
            expanded.append((letter, marks))
    return expanded


def match_pattern(wazn: str, word: str) -> str | None:
    """Check that ``word`` is an instance of the pattern ``wazn``.

    In the pattern, ف and ع each stand for one radical (the same one wherever
    they recur); every ل stands for a radical of its own, because quadriliteral
    patterns write the third and fourth radical both as ل. All other letters and
    all vowel marks must be identical. Returns None on success, else a message.
    """
    try:
        p, w = tokenize(wazn), tokenize(word)
    except ValueError as exc:
        return str(exc)
    if len(p) != len(w):
        return f"{word} has {len(w)} letters, pattern {wazn} has {len(p)}"
    bound: dict[str, str] = {}
    for i, ((pl, pm), (wl, wm)) in enumerate(zip(p, w), start=1):
        if pm != wm:
            return f"{word} vs {wazn}: vowel marks differ on letter {i} ({wl})"
        if pl in "فع":
            if wl not in RADICALS and wl not in HAMZA_CARRIERS:
                return f"{word} vs {wazn}: letter {i} ({wl}) cannot be a radical"
            if bound.setdefault(pl, wl) != wl:
                return f"{word} vs {wazn}: {pl} stands for both {bound[pl]} and {wl}"
        elif pl == "ل":
            if wl not in RADICALS and wl not in HAMZA_CARRIERS and wl != "ى":
                return f"{word} vs {wazn}: letter {i} ({wl}) cannot be a radical"
        elif pl != wl:
            return f"{word} vs {wazn}: letter {i} is {wl}, pattern has {pl}"
    return None


def root_types(letters: list[str]) -> list[str]:
    """Derive the root-type labels of a triliteral root from its letters.

    Labels (charter §4, sub-phase 1a): sound, hamzated, doubled, assimilated
    (first radical weak), hollow (second), defective (third), doubly-weak.
    A root can carry several labels (e.g. أتى is hamzated and defective).
    Returns [] for roots that are not triliteral (not classified in schema v0).
    """
    if len(letters) != 3:
        return []
    r1, r2, r3 = letters
    types: list[str] = []
    if HAMZA in letters:
        types.append("hamzated")
    if r2 == r3:
        types.append("doubled")
    weak = [r in WEAK for r in letters]
    if sum(weak) >= 2:
        types.append("doubly-weak")
    elif weak[0]:
        types.append("assimilated")
    elif weak[1]:
        types.append("hollow")
    elif weak[2]:
        types.append("defective")
    return types or ["sound"]
