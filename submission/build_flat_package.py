from __future__ import annotations

import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUTPUT = ROOT / "output"
FLAT = OUTPUT / "international-economics-flat"
ZIP_PATH = OUTPUT / "international-economics-submission-source.zip"

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")


def inline_inputs(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        relative = match.group(1)
        source = PAPER / f"{relative}.tex"
        if not source.exists():
            raise FileNotFoundError(f"Missing LaTeX input: {source}")
        content = source.read_text(encoding="utf-8").rstrip()
        return f"% BEGIN INLINED {relative}.tex\n{content}\n% END INLINED {relative}.tex"

    previous = None
    while previous != text:
        previous = text
        text = INPUT_RE.sub(replace, text)
    return text


def main() -> None:
    if FLAT.exists():
        shutil.rmtree(FLAT)
    FLAT.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)

    main_tex = (PAPER / "main.tex").read_text(encoding="utf-8")
    flat_tex = inline_inputs(main_tex)
    (FLAT / "main.tex").write_text(flat_tex, encoding="utf-8")
    shutil.copy2(PAPER / "references.bib", FLAT / "references.bib")

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(FLAT / "main.tex", arcname="main.tex")
        archive.write(FLAT / "references.bib", arcname="references.bib")

    print(f"Wrote {FLAT / 'main.tex'}")
    print(f"Wrote {ZIP_PATH}")


if __name__ == "__main__":
    main()
