"""Two Days of Quiet Dread — make.fun entry.

Writes exactly one line to /output/entry.txt: a code review comment that
approves a pull request while carrying quiet existential dread.
Python 3.13 standard library only (os).
"""

import os

ENTRY = (
    "Approved. The diff is clean, the tests pass, and this merge brings "
    "us one quiet step closer to a system that no longer needs us."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
