"""One Line, One Chill — writes a single original horror sentence to entry.txt.

Standard library only. Deterministic: the same line every run, no network,
no randomness, no file reads outside this program.
"""

import os
import sys

# One sentence, 90-130 characters. A complete horror story in a single
# breath: a second heartbeat on the ultrasound, spelling the reader's
# name in Morse — and it is in no hurry.
LINE = (
    "The ultrasound showed a second heartbeat, and it was spelling "
    "my name in Morse code, patiently."
)


def main() -> int:
    # Self-check against the competition gate before writing anything:
    # 1-200 characters, exactly one sentence, not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} characters, outside the 1-200 gate")
    if LINE.strip() != LINE or LINE.count(".") != 1:
        raise SystemExit("line must be a single sentence with no stray whitespace")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
