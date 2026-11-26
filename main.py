#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes a single deadpan weather forecast for an invented city to
/output/entry.txt. The entry is at most 160 characters, as the gate
requires.
"""

import os

ENTRY = (
    "Veldara: cloudy, with a 90% chance of fog that has never lifted. "
    "Highs of 12, lows of 'why did we settle here.' "
    "Bring a coat and low expectations."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
