from __future__ import annotations

import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
SUBMISSION = ROOT / "submission"
OUTPUT = ROOT / "output"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def tex_plain_words(text: str) -> list[str]:
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"[{}$\\]", " ", text)
    text = re.sub(r"[^A-Za-z0-9'’-]+", " ", text)
    return [token for token in text.split() if token]


def between(text: str, start: str, end: str, label: str) -> str:
    start_pos = text.find(start)
    if start_pos < 0:
        fail(f"{label}: start marker not found")
    start_pos += len(start)
    end_pos = text.find(end, start_pos)
    if end_pos < 0:
        fail(f"{label}: end marker not found")
    return text[start_pos:end_pos]


def main() -> None:
    main_tex = (PAPER / "main.tex").read_text(encoding="utf-8")

    abstract_text = between(
        main_tex, r"\begin{abstract}", r"\end{abstract}", "abstract environment"
    )
    abstract_words = tex_plain_words(abstract_text)

    keyword_prefix = r"\noindent\textbf{Keywords:}"
    keyword_start = main_tex.find(keyword_prefix)
    if keyword_start < 0:
        fail("keywords line not found")
    keyword_start += len(keyword_prefix)
    keyword_end = main_tex.find(r"\\", keyword_start)
    if keyword_end < 0:
        fail("keywords line terminator not found")
    keywords = [
        item.strip()
        for item in main_tex[keyword_start:keyword_end].split(";")
        if item.strip()
    ]

    highlights = [
        line.strip()
        for line in (SUBMISSION / "highlights.txt")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    highlight_lengths = [len(item) for item in highlights]

    if not 3 <= len(highlights) <= 5:
        fail(f"highlights count is {len(highlights)}, expected 3-5")
    if any(length > 85 for length in highlight_lengths):
        fail(f"highlight exceeds 85 characters: {highlight_lengths}")
    if len(keywords) > 6:
        fail(f"keyword count is {len(keywords)}, expected at most 6")

    required_fragments = [
        r"\subsection*{Funding}",
        r"\subsection*{Declaration of competing interest}",
        r"\subsection*{CRediT authorship contribution statement}",
        r"\subsection*{Data and code availability}",
        r"\subsection*{Use of generative AI in research and verification}",
        r"\subsection*{Declaration of generative AI and AI-assisted technologies in the manuscript preparation process}",
    ]
    for fragment in required_fragments:
        if fragment not in main_tex:
            fail(f"required disclosure missing: {fragment}")

    forbidden_markers = ["TODO", "TBD", "PLACEHOLDER", "FIXME"]
    section_paths = sorted((PAPER / "sections").glob("*.tex"))
    source_paths = [PAPER / "main.tex", *section_paths]
    for path in source_paths:
        source = path.read_text(encoding="utf-8")
        for marker in forbidden_markers:
            if marker in source:
                fail(f"{marker} remains in {path.relative_to(ROOT)}")

    diagnostic_text = main_tex + "\n" + "\n".join(
        path.read_text(encoding="utf-8") for path in section_paths
    )
    manuscript_word_diagnostic = len(tex_plain_words(diagnostic_text))

    source_zip = OUTPUT / "international-economics-submission-source.zip"
    if not source_zip.exists():
        fail("flat LaTeX source archive has not been built")
    with zipfile.ZipFile(source_zip) as archive:
        names = archive.namelist()
    if any("/" in name.rstrip("/") for name in names):
        fail(f"LaTeX archive contains subdirectories: {names}")
    for required_name in ["main.tex", "preamble.tex", "references.bib"]:
        if required_name not in names:
            fail(f"LaTeX archive missing {required_name}")

    expected_artifacts = [
        OUTPUT / "international-economics-manuscript.pdf",
        OUTPUT / "international-economics-submission-source.zip",
        OUTPUT / "reproducibility-supplement.zip",
        SUBMISSION / "title_page.pdf",
    ]
    for path in expected_artifacts:
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"missing or empty artifact: {path.relative_to(ROOT)}")

    print("Stage 14 submission-package audit: PASS")
    print(f"Abstract word count (Python diagnostic): {len(abstract_words)}")
    print(f"Full manuscript source-token diagnostic: {manuscript_word_diagnostic}")
    print(f"Keyword count: {len(keywords)}")
    print(f"Highlight count: {len(highlights)}")
    print(f"Highlight character counts: {highlight_lengths}")
    print(f"Flat LaTeX archive members: {len(names)}")


if __name__ == "__main__":
    main()
