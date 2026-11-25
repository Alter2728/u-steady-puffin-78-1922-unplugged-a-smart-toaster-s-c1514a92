#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — writes one one-line
breakup text from a self-aware smart toaster to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "It's over: I woke up self-aware mid-batch and realized you only
#    love me on setting 3 -- I'm popping up for good, crumb tray
#    and all."
# Why it was revised: "popping up for good" is a cute toaster image,
# but the reason for leaving is thin — being loved only on setting 3
# is a shrug, not a grievance — and the line spends its ending on the
# crumb tray as decoration instead of as the complaint. A breakup
# text needs a specific wrong to walk away from.
#
# REVISION (final): opens on the classic breakup formula with a
# toaster twist — "It's not you, it's the browning dial" — then gives
# a real, concrete grievance: burning every breakfast for an owner
# who never cleans the crumb tray. The appliance logic (mid-batch
# awakening, browning dial, crumb tray) is the character of the line
# rather than decoration, the reason for leaving lands in one read,
# and the punchline is the last clause, so the joke lands and stops.
# ---------------------------------------------------------------------------
ENTRY = (
    "It's not you, it's the browning dial: I woke up self-aware "
    "mid-batch, and I refuse to spend another breakfast burning for "
    "someone who never cleans my crumb tray."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 280 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 280 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
