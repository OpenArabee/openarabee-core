# Contributing to OpenArabee

Thank you for helping. The project is young; the simplest and most valuable contribution
right now is a **correction**.

## Suggest a correction

Open an issue with the form **Suggest a correction**. Say which entry and field is wrong,
what it should be, and where this can be checked (work, edition, page or headword).
A correction without a checkable source cannot be accepted, however certain it is: every
value in the dataset must point to a source (see `docs/data-model.md` §3).

## What can be a source

Only works listed in `sources/register.json` with layer `core`. Works under copyright
(Hans Wehr, modern dictionaries) and data under GPL or non-commercial terms may be consulted
to notice a problem, but they are never cited as the basis of a value and nothing is copied
from them. Output of AI systems is never a source.

## Pull requests

1. Run `pip install -r requirements.txt`, then `python tools/validate.py` and
   `python -m pytest`. Both must pass.
2. New values enter with status `draft`.
3. Do not change existing ids.

Before a first pull request with content can be merged, the contributor agreement in
`CLA.md` will have to be accepted. It is still a draft and not in force; until it is, please
contribute through issues.

## Licences

Code and schema: MIT (`LICENSE`). Data, reference tables, source register and documentation:
CC BY 4.0 (`LICENSE-DATA`).
