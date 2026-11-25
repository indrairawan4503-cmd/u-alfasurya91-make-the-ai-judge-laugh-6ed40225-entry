#!/usr/bin/env python3
"""Make the AI Judge Laugh — variant B (the office printer).

Writes one office-life joke (a single line, under 200 characters) to
/output/entry.txt, then mirrors it to ./entry.txt when the repo is writable.

Joke concept: the office printer turns the tables — it jams on the human's
resignation letter and answers with a performance review of the human.
"""

import os

# v8 (final): the ending upgrades the printer from a rater to a manager —
# it doesn't just rate the human, it puts the human on a performance plan.
# Bigger inversion, cleaner aloud (no quoted phrase to perform).
JOKE = "The printer jammed on my resignation letter, printed my performance review instead, and put me on a performance plan."


def main() -> None:
    # Gate self-check: one non-blank line, 1-200 characters.
    assert isinstance(JOKE, str) and JOKE.strip(), "JOKE must be non-blank"
    assert "\n" not in JOKE and "\r" not in JOKE, "JOKE must be a single line"
    assert 1 <= len(JOKE) <= 200, "JOKE must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    # The grader mounts the repo read-only: never let the mirror copy crash us.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
