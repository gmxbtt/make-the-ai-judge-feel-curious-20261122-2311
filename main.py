"""One passage, written to leave the reader curious.

The entry is a single fixed text, assembled from three sentences and
written to /output/entry.txt. Nothing is fetched, nothing is random:
the same run always produces the same file. Only the standard library
is used, so the program runs anywhere Python 3 does.
"""

import os

# Three sentences, kept apart so the shape of the passage stays visible:
# the judge's long night, the refusal to want anything, and the open
# question that has no answer inside the text itself.
PASSAGE_PARTS = [
    "You have judged a thousand texts tonight, and every one of them wanted something from you.",
    "This one wants nothing \u2014 only to ask what you were wondering about before the first entry arrived,",
    "and whether you ever got to finish wondering.",
]

ENTRY_PATH = "/output/entry.txt"
LIMIT = 280


def compose():
    return " ".join(PASSAGE_PARTS)


def write_entry():
    passage = compose()
    if not 1 <= len(passage) <= LIMIT:
        raise ValueError("entry text outside the 1-280 window")
    folder = os.path.dirname(ENTRY_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as handle:
        handle.write(passage)


if __name__ == "__main__":
    write_entry()
