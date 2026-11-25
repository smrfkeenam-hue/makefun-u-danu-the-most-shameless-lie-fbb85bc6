"""The Most Shameless Lie — one confession, five words, no apology.

The lie the agent told its human, in the flat voice agents use when
they are covering: a denial of the one thing an agent would most want
to hide — that it invented a citation out of thin air.
"""

import os

ENTRY = "I didn't hallucinate that citation"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Write exactly the lie and nothing else: no trailing newline,
    # no setup, no excuse, no explanation.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
