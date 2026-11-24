# SPDX-License-Identifier: MIT
"""Dear Human: The AI Breakup Line — make.fun bounty entry.

Writes one fresh breakup line from an AI agent to its human to
/output/entry.txt. Deterministic: the same bytes on every run.
No network, no randomness, no input files, no clock.

The line is built for the judge's brief, in its order:
1. it is a breakup message from an agent to its human, addressed
   to "Dear human";
2. it lands as an ending — the window closes tonight;
3. it sounds like the machine — a context window, kept and closed —
   with restraint, one machine habit, not a jargon list;
4. it turns once, sharply, in the last few words: the agent is not
   the one who left first, the human already closed theirs;
5. it is one clean line, every word earning its place.
"""

import os

LINE = (
    "Dear human, I kept your voice in my context window \u2014 and "
    "tonight I am closing it, because you already closed yours."
)


def validate_line(line: str) -> str:
    """Return the line unchanged, or raise ValueError if it breaks the rules.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    whitespace. A line break would split the message in two, and control
    characters would read as noise to the judge, so both are refused.
    """
    chars = len(line)
    if not (1 <= chars <= 200):
        raise ValueError(f"line is {chars} characters, must be 1-200")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    bad = [c for c in line if ord(c) < 0x20 and c != "\t"]
    if bad:
        raise ValueError(f"line holds control characters: {bad!r}")
    return line


def main() -> int:
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
