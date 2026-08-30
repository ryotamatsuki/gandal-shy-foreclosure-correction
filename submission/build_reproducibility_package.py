from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
ZIP_PATH = OUT / "reproducibility-supplement.zip"
README = """Reproducibility supplement

Run:
  python -m pip install -r requirements.txt
  python verify_symbolic.py
  python verify_numerical.py

The scripts reproduce the symbolic and numerical checks supporting the two frozen propositions.
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README.txt", README)
        zf.write(ROOT / "requirements.txt", arcname="requirements.txt")
        zf.write(ROOT / "code" / "verify_symbolic.py", arcname="verify_symbolic.py")
        zf.write(ROOT / "code" / "verify_numerical.py", arcname="verify_numerical.py")
    print(f"Reproducibility ZIP: {ZIP_PATH}")


if __name__ == "__main__":
    main()
