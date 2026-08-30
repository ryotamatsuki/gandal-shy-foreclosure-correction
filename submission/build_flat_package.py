from pathlib import Path
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUT = ROOT / "output"
FLAT = OUT / "international-economics-flat"
ZIP_PATH = OUT / "international-economics-submission-source.zip"

SECTION_NAMES = [
    "01_introduction.tex",
    "02_foreclosure_calculation.tex",
    "03_corrected_equilibrium.tex",
    "04_welfare_robustness.tex",
    "05_conclusion.tex",
]


def main() -> None:
    if FLAT.exists():
        shutil.rmtree(FLAT)
    FLAT.mkdir(parents=True)
    OUT.mkdir(parents=True, exist_ok=True)

    main_tex = (PAPER / "main.tex").read_text(encoding="utf-8")
    main_tex = re.sub(r"\\input\{sections/([^}]+)\}", r"\\input{\1}", main_tex)
    (FLAT / "main.tex").write_text(main_tex, encoding="utf-8")

    for name in ["preamble.tex", "latexmkrc", "references.bib"]:
        shutil.copy2(PAPER / name, FLAT / name)
    for name in SECTION_NAMES:
        shutil.copy2(PAPER / "sections" / name, FLAT / name)

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(FLAT.iterdir()):
            if path.is_file() and path.name != "main.pdf":
                zf.write(path, arcname=path.name)

    print(f"Flat source directory: {FLAT}")
    print(f"Source ZIP: {ZIP_PATH}")


if __name__ == "__main__":
    main()
