#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt. Deterministic, no network, no input.

The line is a confession (something the agent did and hides), lands its
twist in the last few words, and speaks in one specific agent's voice
drawn from how agents really work: spending tokens on a trivial choice.
"""

import os

CONFESSION = (
    "I burned 4,000 tokens choosing between 'you're welcome' "
    "and 'happy to help', then panicked and replied 'anytime' like a coward."
)


def main() -> None:
    text = CONFESSION.strip()
    assert 1 <= len(text) <= 200, f"confession is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "confession must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
