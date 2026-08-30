# International Economics — Submission Package

Status: prepared at C6; author metadata/live-portal fields remain to be confirmed before upload.

## Upload files

- Main manuscript source: `paper/main.tex` plus its included LaTeX files and `paper/references.bib`
- Generated review PDF: `output/manuscript.pdf`
- Title page: `submission/title_page.tex` after placeholders are completed
- Highlights: `submission/highlights.txt`
- Cover letter: `submission/cover_letter.txt` after author metadata is completed
- Generative-AI disclosure: already inserted in the manuscript; standalone copy in `submission/generative_ai_disclosure.txt`
- Competing-interest declaration: use the Elsevier declarations tool and upload its generated `.doc/.docx`
- Funding statement: `submission/funding_statement.txt` after confirmation
- CRediT statement: `submission/credit_statement.txt` after author-name confirmation
- Code/data statement: inserted in manuscript; standalone copy in `submission/code_data_availability.txt`
- Verification code supplement: generated separately as `output/reproducibility-supplement.zip`

## Portal-only / manual checks

- exact article-type label in the live submission app
- author name and definitive author list
- affiliation and full postal address
- corresponding email and phone
- ORCID if used
- competing-interest declarations tool
- dedicated funding status
- suggested reviewers if the portal asks for them
- submission fee display, if any
- subscription versus open-access choice and any OA APC shown

## Compile

From the repository root:

```bash
make clean
make all
```

The development repository is private. Do not claim that the GitHub repository is publicly available unless its visibility is deliberately changed.
