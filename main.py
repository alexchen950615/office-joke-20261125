#!/usr/bin/env python3
"""One-Line Office Joke: writes a single original office joke to /output/entry.txt.

Deterministic: the same fixed joke is written on every run, with no
randomness, no network access, and no input files.
"""

import os

JOKE = "My standup update never changes: yesterday I was in meetings, today I'll be in meetings, and I'm blocked by meetings."


def main() -> None:
    # Kit gate: entry must be 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
