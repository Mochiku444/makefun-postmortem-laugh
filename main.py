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
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be whitespace-only"
    text.encode("utf-8")
    return text


def main() -> None:
    text = validated_entry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Verify the bytes on disk match the intended entry exactly.
    assert OUTPUT.read_text(encoding="utf-8") == text


if __name__ == "__main__":
    main()
