"""OpenArabee identifiers (docs/data-model.md §2, decision D-015).

Root letters are written one ASCII character per radical: lowercase letters and
digits only, so identifiers are safe in file names, URLs and on case-insensitive
file systems. Letters whose Buckwalter symbol is a lowercase letter keep it; the
other nine use the digits familiar from the Arabic chat alphabet where one
exists (2 3 6 7 9) and a fixed character otherwise.
"""
from __future__ import annotations

import re

LETTER_TO_ASCII = {
    "ء": "2", "ب": "b", "ت": "t", "ث": "v", "ج": "j", "ح": "7", "خ": "x",
    "د": "d", "ذ": "4", "ر": "r", "ز": "z", "س": "s", "ش": "c", "ص": "9",
    "ض": "8", "ط": "6", "ظ": "0", "ع": "3", "غ": "g", "ف": "f", "ق": "q",
    "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "w", "ي": "y",
}
ASCII_TO_LETTER = {v: k for k, v in LETTER_TO_ASCII.items()}
assert len(ASCII_TO_LETTER) == len(LETTER_TO_ASCII) == 28

ROOT_ID = re.compile(r"^r-[a-z0-9]{3,5}$")
LEXEME_ID = re.compile(r"^([vnp])-([a-z0-9]{2,12})-([1-9][0-9]*)$")


def root_key(letters: list[str]) -> str:
    try:
        return "".join(LETTER_TO_ASCII[ch] for ch in letters)
    except KeyError as exc:
        raise ValueError(f"{exc.args[0]!r} is not a root letter (write hamza as ء)") from None


def root_id(letters: list[str]) -> str:
    return "r-" + root_key(letters)


def root_letters(rid: str) -> list[str]:
    if not ROOT_ID.match(rid):
        raise ValueError(f"not a root id: {rid!r}")
    return [ASCII_TO_LETTER[ch] for ch in rid[2:]]


if __name__ == "__main__":
    import sys

    for arg in sys.argv[1:]:
        if arg.startswith("r-"):
            print(arg, " ".join(root_letters(arg)))
        else:
            print(arg, root_id([ch for ch in arg if not ch.isspace()]))
