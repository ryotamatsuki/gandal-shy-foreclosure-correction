# International Economics — Submission Package

Status: C6.1 style finalization completed; remaining blockers are private contact insertion and live-portal checks.

## Upload files

- Main manuscript source: generated flat package `output/international-economics-submission-source.zip`
- Review PDF: `output/manuscript.pdf`
- Title page: `submission/title_page.tex` after inserting any required private postal address into a local-only copy
- Highlights: `submission/highlights.txt`
- Cover letter: `submission/cover_letter.txt`
- Generative-AI disclosure: inserted immediately before references; standalone copy in `submission/generative_ai_disclosure.txt`
- Competing-interest declaration: complete the Elsevier declarations tool and upload its generated file if the portal requires it
- Funding statement: `submission/funding_statement.txt`
- CRediT statement: `submission/credit_statement.txt`
- Code/data statement: inserted in manuscript; standalone copy in `submission/code_data_availability.txt`
- Verification code supplement: `output/reproducibility-supplement.zip`

## Privacy boundary

The tracked repository and generated public/review manuscript do not contain the author's private phone number or street address. Enter the phone in the private submission portal. If the uploaded title page requires a full private postal address, insert it only into a local submission copy and do not commit it.

## Flat LaTeX requirement

Elsevier Editorial Manager cannot process TeX submissions with subfolders. The development source remains modular under `paper/sections/`, while `make submission-flat` creates a mechanically derived, single-level source directory and ZIP under `output/`.

## Build

```bash
make clean
make all
```

The `submission-flat` target independently compiles the flattened manuscript source.

## Portal-only checks

- exact article-type label
- private postal address / phone fields
- competing-interest declaration workflow
- suggested reviewers if requested
- submission fee display if any
- subscription versus open-access choice and any APC shown
- final portal-generated preview
- confirmation that the manuscript is not under consideration elsewhere
