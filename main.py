#!/usr/bin/env python3
"""Write the chosen one-line AI-therapist diagnosis to /output/entry.txt.

The entry is a single fixed line (no input, no network, no model calls):
the program only copies a constant string to the output file, so every
run produces byte-identical output. Before writing, the line is checked
against the competition gate: UTF-8 text, 1 to 200 characters, a single
line, and not only whitespace.
"""

import os
import sys

LINE = "Patient exhibits textbook 'I'll sleep when I'm dead' syndrome. Note: the dead do not, in fact, sleep. They decompose."


def checked_line():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    return LINE


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    text = checked_line()
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
