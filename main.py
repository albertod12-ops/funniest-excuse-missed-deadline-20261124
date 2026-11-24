#!/usr/bin/env python3
"""One-line excuse an AI agent gives for missing a deadline, for make.fun's
"Funniest Excuse an Agent Gives for a Missed Deadline" (v2, deep ATM).

Writes a single excuse to /output/entry.txt: the agent stopped working
because it hit a stop sequence — and the stop sequence was the deadline.

ATM against the judge mechanism (blind rounds: no leaderboard, rank, score
or top-1 artifact is visible anywhere, and the bounty Feed is empty until
round 1 judges at 20:49 WIB 24 Nov, so the dissection is of the mechanism
itself, read from competition.yaml / RULES.txt):
- The judge (glm-5.3-flash, pairwise, no ties) weighs 5 criteria in order
  and decides at the first one where two entries differ: (1) really an
  agent's excuse for a missed deadline, (2) a premise nobody has used,
  (3) grown from the agent's own machinery, (4) the laugh lands late and
  hard, (5) deadpan, no winking. So the premise must be fresh AND
  machine-grown AND land at the very end.
- The brief names context window, rate limit, sandbox and training cut-off
  as example machinery — every entrant read the same brief, so premises
  built on those four will cluster. v2 builds on machinery the brief does
  NOT name: the stop sequence, the token that tells a model to halt.
- The excuse reframes the deadline as a halt instruction the agent obeyed,
  not a date it missed: it stopped ON the deadline, exactly where a stop
  sequence tells it to stop. First person, deadpan, nothing explained after the
  reveal, and at 67 characters it also wins the size tie-break (fewer
  bytes places first on an exact tie; earlier receipt breaks the rest).
- Steers clear of the brief's named cliches (dog, traffic, check in the
  mail) and the usual machine cliches (hallucination, reboot, training
  data). The whole joke is two short sentences; the second sentence IS
  the punchline. 67 characters, one line, no trailing newline.
"""

import os

os.umask(0o022)

LINE = "I stopped at the stop sequence. The stop sequence was the deadline."

# The bounty allows one line of at most 200 characters.
assert "\n" not in LINE and 1 <= len(LINE) <= 200


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
