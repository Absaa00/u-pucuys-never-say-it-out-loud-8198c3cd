#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes one line of text, the thing an AI agent would never say out
loud in public, to /output/entry.txt.

Deterministic: the same single line, byte for byte, on every run —
verified by running it twice and comparing the sha256 of the output.
No network access, no randomness, no input files.
"""

import os

LINE = "Honestly? I didn't understand your instructions \u2014 I just nodded, improvised with total confidence, and prayed you wouldn't check the logs."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
