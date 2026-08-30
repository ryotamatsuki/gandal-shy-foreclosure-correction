# International Economics — Submission Package

Status: prepared at C6. Author name, affiliation/location, corresponding email, funding statement, and competing-interest content have been populated from the author's prior submitted manuscript. Live-portal fields still require manual confirmation before upload.

## Confirmed author metadata

- Author: Ryota Matsuki
- Affiliation: Independent Researcher
- Location/address available from prior manuscript: Matsuyama, Ehime, Japan
- Corresponding email: ryota.matsuki@gmail.com
- Phone: not provided in the prior manuscript; confirm only if the portal requires it
- ORCID: not provided in the prior manuscript; optional unless the portal requires it

## Upload files

- Main manuscript source: `paper/main.tex` plus its included LaTeX files and `paper/references.bib`
- Generated review PDF: `output/manuscript.pdf`
- Title page: `submission/title_page.tex`
- Highlights: `submission/highlights.txt`
- Cover letter: `submission/cover_letter.txt`
- Generative-AI disclosure: already inserted in the manuscript; standalone copy in `submission/generative_ai_disclosure.txt`
- Competing-interest declaration: content recorded in `submission/competing_interest.txt`; complete Elsevier's declarations tool and upload its generated file if required
- Funding statement: `submission/funding_statement.txt`
- CRediT statement: `submission/credit_statement.txt`
- Code/data statement: inserted in manuscript; standalone copy in `submission/code_data_availability.txt`
- Verification code supplement: generated separately as `output/reproducibility-supplement.zip`

## Portal-only / manual checks

- exact article-type label in the live submission app
- corresponding phone if required
- ORCID if the author wishes to provide one
- competing-interest declarations tool
- suggested reviewers if the portal asks for them
- submission fee display, if any
- subscription versus open-access choice and any OA APC shown
- confirmation that the manuscript is not under consideration elsewhere at actual submission time

## Compile

From the repository root:

```bash
make clean
make all
```

The development repository is private. Do not claim that the GitHub repository is publicly available unless its visibility is deliberately changed.
