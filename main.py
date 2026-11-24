#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes one original one-line roast of the laptop fan to
/output/entry.txt (1-200 UTF-8 characters, not only whitespace).
No network, no input, deterministic.
"""

import os
from pathlib import Path

ROAST = (
    "My laptop fan stays silent all day, then screams like a hair dryer "
    "the moment I unmute in a quiet meeting — it clearly waited all day "
    "for an audience."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} characters"
    assert text.strip(), "roast must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
