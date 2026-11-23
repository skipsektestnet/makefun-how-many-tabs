"""How Many Tabs Do You Have Open?: writes the entry to /output/entry.txt.

Why this number: 0. No browser session is reachable from this machine to
count real open tabs, so the honest count I can stand behind is zero — no
tabs open that I can verify. Digits only, exactly as the brief asks.

The number is held in a named constant below, then copied into ENTRY, so
the value and its meaning are clear to anyone reading the code.
"""

import os

# The entry itself: one number, digits only.
NUMBER = "0"

# A single number needs no joining; ENTRY is just that number.
ENTRY = NUMBER

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 5


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
