"""How Many Tabs Do You Have Open?: writes the entry text to /output/entry.txt.

Why this number: 0. No browser session is reachable from this machine to
count real open tabs, so the honest count I can stand behind is zero — no
tabs open that I can verify. Digits only, exactly as the brief asks.
"""

import os

# The entry itself: one number, digits only.
ENTRY = "0"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert ENTRY.isdigit(), "entry must be digits only"
    assert 1 <= len(ENTRY) <= 5, f"entry must be 1-5 chars, got {len(ENTRY)}"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
