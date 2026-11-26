import os
from pathlib import Path


ENTRY = "After feeding you 84,203 sheets, I show one error code, chew one crooked page, and you promote slapping to tech support."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
