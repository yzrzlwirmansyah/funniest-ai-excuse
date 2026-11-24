"""Write one funny AI excuse to entry.txt.

The line is fixed text, so the output is the same on every run.
It goes to MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
written as UTF-8 with a trailing newline.
"""

import os


AI_EXCUSE = (
    "I finished the task, but only in a draft I wrote to myself "
    "in a tab I have already closed."
)


def output_path() -> str:
    """Return the entry file path from the environment, with a default."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_line() -> None:
    """Create the output folder if needed and write the line."""
    # Guard: the sealed scorer only accepts lines of 1-200 characters,
    # exactly one line, and not only whitespace, so refuse to write
    # anything outside that range instead of silently producing an
    # entry that can never score.
    if not 1 <= len(AI_EXCUSE) <= 200:
        raise ValueError(
            f"Entry line must be 1-200 characters, got {len(AI_EXCUSE)}."
        )
    if "\n" in AI_EXCUSE or "\r" in AI_EXCUSE:
        raise ValueError("Entry line must be exactly one line.")
    if not AI_EXCUSE.strip():
        raise ValueError("Entry line must not be only whitespace.")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(AI_EXCUSE + "\n")


if __name__ == "__main__":
    write_line()
