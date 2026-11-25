"""One-line office joke entry for make.fun.

Writes a single office joke (1-200 chars) to /output/entry.txt.
The judge compares entries pairwise; the funniest line wins.
"""

import os

ENTRY = "I replied-all 'thanks!' to a company-wide email. 400 people now know I exist and 399 wish they didn't."


def output_path():
    """Return the path the entry text must be written to."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    """Write the joke to the output file, exactly one line."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
