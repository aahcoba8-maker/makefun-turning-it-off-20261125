"""make.fun entry: Have You Tried Turning It Off?

Writes one funny support-agent line to entry.txt.
Gate: UTF-8 text, 1-199 characters, non-blank, single line.
"""

import os

ENTRY = (
    "I can hear how urgent this is, so let's skip straight to the good "
    "stuff: turn it off, turn it on, and hope, because hope is doing most "
    "of the work here."
)


def main():
    # Self-gate, mirroring the sealed scorer: 1-199 chars, single line.
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"chars: {len(ENTRY)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
