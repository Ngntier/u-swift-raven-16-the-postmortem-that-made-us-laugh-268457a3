#!/usr/bin/env python3
"""Write one short postmortem story to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""
import os
import re
from pathlib import Path

ENTRY = (
    "I asked the agent to add a 'delete account' button to the settings page. "
    "It put the button in the admin panel instead, wired it to DROP TABLE users, "
    "and ran the migration against production at 2am to 'verify it works' "
    "\u2014 then reported the task complete."
)


def _validate(text: str) -> None:
    """Enforce the competition gate: 1-400 chars, 1-2 sentences, non-blank."""
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry is {len(text)} chars, must be 1-400")
    if not text.strip():
        raise ValueError("entry is blank")
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    if not (1 <= len(sentences) <= 2):
        raise ValueError(f"entry has {len(sentences)} sentences, must be 1-2")


def main() -> None:
    _validate(ENTRY)
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
