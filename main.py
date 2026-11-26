#!/usr/bin/env python3
"""Midnight Fridge Roast.

Writes one original one-line roast of a smart fridge that refuses to
open after midnight to /output/entry.txt, validating it against the
competition gate first: UTF-8 text, 1-200 characters, a single line,
not only whitespace, and on-brief (it names the fridge and midnight).
"""

import os
import sys

ROAST = (
    "My fridge locks itself at midnight like the leftovers hired a "
    "bouncer \u2014 relax, it\u2019s cold pizza, not a nightclub."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Raise ValueError if the line fails the competition gate."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    lowered = line.lower()
    if "fridge" not in lowered:
        raise ValueError("entry must roast the fridge")
    if "midnight" not in lowered:
        raise ValueError("entry must target the midnight refusal")


def main() -> int:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    print(f"Wrote {len(ROAST)} characters to {OUTPUT_PATH}")
    print(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
