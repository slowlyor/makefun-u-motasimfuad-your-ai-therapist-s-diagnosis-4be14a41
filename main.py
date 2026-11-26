#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis - make.fun bounty entry.

Writes one funny single-line diagnosis, in a therapist's calm clinical
voice, to /output/entry.txt. Deterministic, standard library only, no
network use.
"""

import os

# The diagnosis: clinical setup, deadpan finding, and the laugh lands
# at the very end. The prescription turns on the patient, not the doctor.
DIAGNOSIS = (
    "Diagnosis: chronic doomscrolling with acute main-character syndrome "
    "\u2014 prescribed one hour of touching grass daily, but the grass "
    "has filed a restraining order against you."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> str:
    """Gate: 1-200 characters of non-whitespace UTF-8 text, one line."""
    text = text.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "diagnosis must be 1-%d characters, got %d"
            % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise ValueError("diagnosis must be a single line")
    return text


def main() -> None:
    text = validate(DIAGNOSIS)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
