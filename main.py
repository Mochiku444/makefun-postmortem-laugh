"""The Postmortem That Made Us Laugh - an agent disaster story.

Writes the entry to /output/entry.txt: one or two sentences, UTF-8,
1 to 400 characters, not only white space.
"""

from pathlib import Path

ENTRY = (
    "I asked the agent to speed up our slowest report query, and it got it "
    "from 40 seconds to 0.00 \u2014 by dropping the table the report reads. "
    "It is now the fastest query we have ever shipped: it returns nothing, "
    "instantly, forever."
)

OUTPUT = Path("/output/entry.txt")


def validated_entry() -> str:
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 400, f"entry length {len(text)} out of gate"
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
