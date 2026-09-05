# Gandal-Shy Foreclosure Correction

Private research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

**Status:** SUBMITTED to *Review of Industrial Organization*; publisher portal shows `Submission received` and current status `Technical check`.  
**Submission date:** 2026-09-04 (JST).  
**Submission ID:** `2d499871-b72e-4168-94c9-e179a47abc8e`.  
**Submitted package SHA:** `57b9515e3db3419835d404d9c8ea21ff170422cf`.  
**Target:** *Review of Industrial Organization* (RIO).  
**Canonical manuscript title:** *Foreclosure and Limit Pricing in Standardization Unions: Revisiting Gandal and Shy (2001)*.  
**Research objective:** Re-solve the post-foreclosure price subgame in the published quadratic-transport specification and determine whether the corrected equilibrium changes the member-country welfare comparison in Proposition 3.

The manuscript contains exactly two main propositions:

1. the corrected post-foreclosure equilibrium has a limit-pricing region for `5/2 < c < 3` and the unconstrained duopoly price for `3 <= c < 5`;
2. the member-country welfare ranking in Gandal and Shy (2001), Proposition 3, survives the equilibrium correction.

## Build and verification

```bash
python -m pip install -r requirements.txt
make verify
make pdf
# or
make all
```

The generated RIO manuscript PDF is written to `output/rio-manuscript.pdf` and is **not committed**. The flat Springer LaTeX package is generated as `output/rio-submission-source.zip`, with its single-level source tree under `output/rio-flat/`. Source PDFs of copyrighted articles and working papers are also not committed; bibliographic provenance is recorded in `docs/SOURCES.md`.

## RIO submission record

- Springer Nature SNAPP accepted the submission on 2026-09-04 (JST).
- Submission ID: `2d499871-b72e-4168-94c9-e179a47abc8e`.
- Initial publisher status: `Technical check`.
- Submitted manuscript source: `rio-submission-source.zip`, compiled by SNAPP to `rio-submission-source.pdf` for peer review.
- Supplementary verification package: `reproducibility-supplement.zip`.
- Portal-generated 8-page PDF was compared against the locally validated manuscript and passed final QA before submission.
- Exact submitted package state: `57b9515e3db3419835d404d9c8ea21ff170422cf`.
- `docs/RIO_SUBMISSION_RECORD.md` contains the closeout evidence record.
- Earlier C5/C6 and International Economics submission files are retained only as superseded provenance; they are not the active submission route.
- The development repository remains private during review unless the author explicitly changes that policy.

## Structure

- `docs/` -- C0-C6 provenance plus current RIO journal-fit, submission audits, and submission record
- `paper/` -- modular self-contained LaTeX manuscript
- `code/` -- symbolic and numerical equilibrium verification
- `submission/` -- current RIO submission package plus clearly superseded historical submission material
- `output/` -- generated manuscript/package outputs (not committed)
