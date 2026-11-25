#!/usr/bin/env python3
"""Entry for the make.fun bounty 'Notes From a Passive-Aggressive Fridge'.

Writes a single passive-aggressive note from a smart fridge to
/output/entry.txt.
"""

import os

ENTRY = (
    "My sensors counted 47 door opens today. You took nothing. "
    "At this point, you're just here for the light."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
