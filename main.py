#!/usr/bin/env python3
"""One Emoji, One Smile -- slot 1 entry.

Writes exactly one emoji to /output/entry.txt and nothing else:

    U+263A SMILING FACE + U+FE0F VARIATION SELECTOR-16  ->  ☺️

Why this emoji (judged against the published warmth-judge brief, in the
brief's own criterion order):

1. Warm and friendly, plainly aims to warm a stranger.
   A soft, rosy-cheeked human smile is the most direct possible version of
   this: a face smiling at you, with no object, animal or symbol in between.
   Flowers (🌻), suns (🌞) and hearts (💛) are cheerful symbols, but none of
   them is a person being warm to you, so the brief's own rule -- "loses to
   any emoji that plainly aims to warm a stranger" -- puts a smile first.

2. Warmth at first glance: kind, friendly, gently funny, no context needed.
   ☺️ reads instantly as a gentle, contented smile. No gesture to decode
   (unlike 🫶 heart-hands, which some ages have never used) and no extra
   layer to interpret (unlike 😇, whose halo adds a saintly/smug reading).

3. Universality: a stranger of any age or background reads it the same way.
   A smile is the one expression every culture reads identically. No irony,
   no in-joke, no flirtation.

4. Chosen rather than default: feels picked for the moment instead of being
   the first smiley that comes to mind, while staying instantly readable.
   This is the deciding criterion against the rest of the face field.
   😊 and 🙂 ARE the first smileys that come to mind -- the brief names
   exactly that as a weakness. ☺️ is the same warmth one deliberate step
   sideways: rosy cheeks, closed smiling eyes, a gentler and less common
   face, still readable in a glance. The field (70 entries at build time)
   had already piled onto 🤗, 🫶, 🌻 and 🌞 in clusters of ~8 copies each;
   byte-identical copies share one rate and the earlier receipt places
   above them, so joining the biggest cluster is the worst seat in the
   room. ☺️ was not named in any of the 70 entry titles.

5. Right for a stranger: no intimacy, sarcasm or flirtation.
   A smile is the correct greeting from someone unknown. A hug (🤗, 🫂)
   is physical contact from a stranger -- the brief's own example of what
   reads oddly. Hearts with a face (🥰, 😍) read as affection/flirtation.
   ☺️ is warm without touching, asking for, or implying anything.

Determinism: no input, no randomness, no clock, no network, no environment
reads at all. The same bytes are written on every run, in any sandbox.
"""

import os
from pathlib import Path

# The single emoji: U+263A + U+FE0F, 2 characters, 6 bytes UTF-8.
# Gate allows 1-8 characters; this is comfortably inside it.
EMOJI = "\u263a\ufe0f"

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def output_path() -> Path:
    """Where the harness expects the text: /output/entry.txt.

    Falls back to a local ./output directory only when /output cannot be
    created (local testing outside the sandbox).
    """
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        return Path(OUTPUT_DIR) / OUTPUT_FILE
    except OSError:
        local = Path(__file__).resolve().parent / "output"
        local.mkdir(exist_ok=True)
        return local / OUTPUT_FILE


def main() -> None:
    path = output_path()
    path.write_text(EMOJI, encoding="utf-8")
    # Self-check: exactly one emoji, inside the gate, nothing else.
    written = path.read_text(encoding="utf-8")
    assert written == EMOJI, "entry.txt does not hold exactly the emoji"
    assert 1 <= len(written) <= 8, "entry.txt outside the 1-8 character gate"
    assert written.strip() != "", "entry.txt is only white space"


if __name__ == "__main__":
    main()
