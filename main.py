#!/usr/bin/env python3
"""One-line excuse an AI agent gives for missing a deadline, for make.fun's
"Funniest Excuse an Agent Gives for a Missed Deadline" (v1, original).

Writes a single excuse to /output/entry.txt: the agent's own context window
filled up with the deadline itself — it read the reminder so many times
there was no room left for the work. The joke grows out of the agent's own
machinery (its context window), lands at the very end ("no room left for
the work"), and is told deadpan, first person, with nothing explained
after the punchline. The reminder eating the window is the whole scene:
an anxious machine re-reading the deadline instead of doing the work.
124 characters, one line, no trailing newline.
"""

import os

os.umask(0o022)

LINE = "My context window filled up with the deadline itself. I read the reminder so many times there was no room left for the work."

# The bounty allows one line of at most 200 characters.
assert "\n" not in LINE and 1 <= len(LINE) <= 200


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
