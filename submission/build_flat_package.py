from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUTPUT = ROOT / "output"
FLAT = OUTPUT / "international-economics-flat"
ZIP_PATH = OUTPUT / "international-economics-submission-source.zip"


def main() -> None:
    if FLAT.exists():
        shutil.rmtree(FLAT)
    FLAT.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)

    main_tex = (PAPER / "main.tex").read_text(encoding="utf-8")
    section_files = sorted((PAPER / "sections").glob("*.tex"))
    for section in section_files:
        main_tex = main_tex.replace(
            rf"\input{{sections/{section.stem}}}",
            rf"\input{{{section.stem}}}",
        )

    (FLAT / "main.tex").write_text(main_tex, encoding="utf-8")
    shutil.copy2(PAPER / "preamble.tex", FLAT / "preamble.tex")
    shutil.copy2(PAPER / "references.bib", FLAT / "references.bib")
    for section in section_files:
        shutil.copy2(section, FLAT / section.name)

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(FLAT.iterdir()):
            if path.is_file():
                archive.write(path, arcname=path.name)

    print(f"Wrote flat source tree: {FLAT}")
    print(f"Wrote {ZIP_PATH}")


if __name__ == "__main__":
    main()
