"""
The work timer Claude Code runs each time the student sends a message (.claude/settings.json, a
UserPromptSubmit hook). It adds up active work time and, every RECAP_EVERY seconds of it, tells
Claude to offer the student a recap at the next natural pause.

Active time is the time between two messages, unless the gap is longer than IDLE_GAP: then the
student is taken to have stepped away and the gap counts for nothing. The count lives in
.recap_state.json, so it carries across sessions. Once a recap is due, the reminder repeats on
every message until Claude runs `python3 recap_timer.py --done`, which the recap skill does
whether the student takes the recap or not. Then the count starts again from zero.

Whatever this prints is added to what Claude sees with the student's message. It uses only
Python's standard library and runs with python3.
"""

import json
import os
import sys
import time
from pathlib import Path

RECAP_EVERY = 10 * 60
IDLE_GAP = 3 * 60

REPO = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parent)
STATE = REPO / ".recap_state.json"

DUE = (
    "Recap timer: about {minutes} minutes of active work since the last recap. At the next "
    "natural pause, once the current step, command or answer is finished and never in the "
    "middle of one, ask the student in one line whether they would like a short recap and "
    "check-in now. It is optional. On a yes, run the `recap` skill. On a no, run "
    "`python3 recap_timer.py --done` and carry on without mentioning it again."
)


def load():
    try:
        return json.loads(STATE.read_text())
    except (OSError, ValueError):
        return {"last_message": None, "active": 0, "due": False}


def save(state):
    STATE.write_text(json.dumps(state, indent=2) + "\n")


def main():
    state = load()

    if sys.argv[1:] == ["--done"]:
        state.update(active=0, due=False)
        save(state)
        print("Recap timer reset.")
        return

    now = time.time()
    last = state.get("last_message")
    if last is not None and 0 < now - last <= IDLE_GAP:
        state["active"] = state.get("active", 0) + (now - last)
    state["last_message"] = now
    if state["active"] >= RECAP_EVERY:
        state["due"] = True
    save(state)

    if state["due"]:
        print(DUE.format(minutes=round(state["active"] / 60)))


if __name__ == "__main__":
    main()
