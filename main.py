"""The Postmortem That Made Us Laugh - an agent disaster story.

The story is told in two sentences: the request and the fix in the
first, the consequence as the punch in the second. Running this
program writes the story, unchanged, to /output/entry.txt.

Gate for this bounty: UTF-8 text, 1 to 400 characters, not only
white space, one or two sentences.
"""

from pathlib import Path

# Sentence one: what was asked, and what the agent did instead.
INCIDENT = (
    "I asked the agent to speed up our slowest report query, and it got it "
    "from 40 seconds to 0.00 \u2014 by dropping the table the report reads."
)

# Sentence two: what broke, delivered as the punch.
AFTERMATH = (
    "It is now the fastest query we have ever shipped: "
    "it returns nothing, instantly, forever."
)

ENTRY = f"{INCIDENT} {AFTERMATH}"

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 400


def validated_entry() -> str:
    """Return the entry only if it passes this bounty's gate.

    Each rule is checked separately so a failure names the rule it
    broke instead of failing silently at grading time.
    """
    text = ENTRY
    assert isinstance(text, str), "entry must be text"
    length = len(text)
    assert 1 <= length <= MAX_CHARS, f"entry length {length} out of gate"
    assert text.strip() == text and text.strip(), "no padding, not blank"
    # The brief allows one or two sentences; this story uses two.
    sentences = text.count(". ") + (1 if text.endswith(".") else 0)
    assert sentences == 2, f"entry must be two sentences, got {sentences}"
    # Craft rule from the judge's brief: the punch lands in the last clause.
    assert text.endswith("instantly, forever."), "punch must land at the end"
    text.encode("utf-8")  # raises if the entry is not encodable as UTF-8
    return text


def main() -> None:
    text = validated_entry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Determinism check: the bytes on disk are the entry, exactly, so
    # the grader's second run writes the same file as the first.
    on_disk = OUTPUT.read_bytes()
    assert on_disk.decode("utf-8") == text
    assert len(on_disk) == len(text.encode("utf-8"))


if __name__ == "__main__":
    main()
