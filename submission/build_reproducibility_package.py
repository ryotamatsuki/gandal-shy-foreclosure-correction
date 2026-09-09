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
    ROOT / "GandalShy.lean",
    ROOT / "GandalShy" / "Certification.lean",
    ROOT / "lakefile.toml",
    ROOT / "lake-manifest.json",
    ROOT / "lean-toolchain",
]

README = """Reproducibility materials for
Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)

The package contains the symbolic and numerical verification scripts and the pinned Lean
formal-certification project used to cross-check the analytical equilibrium and welfare
results. No empirical data are used.

Suggested Python commands:
  python -m pip install -r requirements.txt
  python code/verify_symbolic.py
  python code/verify_numerical.py

Suggested Lean command from the package root, with elan/Lake available:
  lake build GandalShy

The Lean source certifies the proof-critical algebraic and quantified-inequality core at
the scope documented in the manuscript project. It does not independently formalize the
entire continuum Salop demand correspondence or all Nash equilibria from consumer primitives.

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
