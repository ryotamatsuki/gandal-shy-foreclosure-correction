# Review of Industrial Organization — Submission Package

Status: RIO-targeted manuscript and submission metadata prepared on 2026-09-01.

## Core upload materials

- Manuscript development source: `paper/`
- Review manuscript PDF generated as: `output/rio-manuscript.pdf`
- Flat LaTeX source directory generated as: `output/rio-flat/`
- Flat LaTeX source ZIP generated as: `output/rio-submission-source.zip`
- Title page source: `submission/title_page.tex`
- Cover letter: `submission/cover_letter.txt`
- Data Availability statement: `submission/code_data_availability.txt`
- AI-use disclosure: `submission/generative_ai_disclosure.txt`
- Funding statement: `submission/funding_statement.txt`
- Competing-interest statement: `submission/competing_interest.txt`
- Author-contribution draft: `submission/credit_statement.txt`
- Verification supplement generated as: `output/reproducibility-supplement.zip`

## Build

```bash
make clean
make all
```

`make all` performs symbolic and dense numerical verification before building the manuscript, flat submission source, verification supplement, and title page.

## LaTeX submission rule

RIO's Springer Nature submission instructions say not to use subfolders in LaTeX submissions. Development remains modular in `paper/sections/`, while `submission/build_flat_package.py` mechanically creates the single-level `rio-flat` package.

## Publication route

Use the **subscription publishing model** unless the author deliberately chooses open access after acceptance. The official RIO page states that no APC applies to the subscription route.

## Live-portal checks still required

- confirm the article/manuscript type shown by the live portal; do not invent a separate Short Note type if none is offered;
- confirm no submission fee is displayed before any payment step;
- enter author contribution and competing-interest information in the interface as required;
- inspect the automatically compiled PDF;
- confirm any reviewer-suggestion fields;
- confirm the manuscript is not under consideration elsewhere at the moment of submission;
- choose subscription publication after acceptance if the zero-APC route remains desired.

## Privacy

No private phone number or street address is stored in the repository. The current RIO title-page guidance is satisfied with the author's independent-researcher identity, city/country, email, and ORCID.
