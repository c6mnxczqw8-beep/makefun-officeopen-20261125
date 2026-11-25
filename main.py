#!/usr/bin/env python3
"""Entry program for Make the AI Judge Laugh: the Office Joke
Open make.fun bounty.

Writes one office joke (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The joke is the office's own lifecycle: every attempt to kill
the meeting resurrects it in a worse form.
"""

import os

JOKE = (
    "Our standup became an email, the email became a "
    "thread, the thread became a meeting, and the meeting "
    "just scheduled a standup."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
