from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
ZIP_PATH = OUTPUT / "reproducibility-supplement.zip"
FILES = [
    ROOT / "code" / "verify_symbolic.py",
    ROOT / "code" / "verify_numerical.py",
    ROOT / "requirements.txt",
]

README = """Reproducibility materials for
Standardization Unions, Foreclosure, and Limit Pricing: Revisiting Gandal and Shy (2001)

The package contains the symbolic and numerical verification scripts used to cross-check
the analytical equilibrium and welfare results. No empirical data are used.

Suggested commands:
  python -m pip install -r requirements.txt
  python code/verify_symbolic.py
  python code/verify_numerical.py

The manuscript remains self-contained; these files are verification support rather than
an appendix required to understand or assess the propositions.
"""


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    missing = [str(path) for path in FILES if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing reproducibility files: " + ", ".join(missing))

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("README.txt", README)
        for path in FILES:
            archive.write(path, arcname=str(path.relative_to(ROOT)))

    print(f"Wrote {ZIP_PATH}")


if __name__ == "__main__":
    main()
