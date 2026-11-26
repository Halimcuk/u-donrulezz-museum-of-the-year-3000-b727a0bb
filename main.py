"""Museum of the Year 3000 — one-line museum label entry.

Writes the label to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The joke: a year-3000 curator misreads the microwave as a shrine that
resurrects cold food, and the humans staring at it as worshippers at prayer.
"""

import os
from pathlib import Path

ENTRY = "Microwave, c. 2020 \u2014 a humming box that resurrected cold food. Humans stood before it in silence, as if in prayer."
# One line, 114 characters: well inside the 200-character gate.


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
