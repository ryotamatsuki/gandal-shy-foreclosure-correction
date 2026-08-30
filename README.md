# Gandal-Shy Foreclosure Correction

Private research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

**Status:** C6 submission freeze; author metadata and declarations populated from the author's prior submitted manuscript; live-portal confirmation remains.  
**Target:** *International Economics* -- Short communication / Short paper.  
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

The generated manuscript PDF is written to `output/manuscript.pdf` and is **not committed**. Source PDFs of copyrighted articles and working papers are also not committed; bibliographic provenance is recorded in `docs/SOURCES.md`.

## Submission freeze

- Author metadata now uses: Ryota Matsuki; Independent Researcher, Matsuyama, Ehime, Japan; ryota.matsuki@gmail.com.
- `submission/` contains the draft upload files and manual-submission checklist.
- `docs/C6_SUBMISSION_REQUIREMENTS.md` records the current journal requirements checked on 2026-08-30.
- `docs/C6_SUBMISSION_FREEZE.md` records the C6 freeze and remaining live-portal checks.
- The development repository remains private during review unless the author explicitly changes that policy.

## Structure

- `docs/` -- C0-C6 provenance, journal-fit and submission audits, source ledger
- `paper/` -- modular self-contained LaTeX manuscript
- `code/` -- symbolic and numerical equilibrium verification
- `submission/` -- journal submission package metadata and declarations
- `output/` -- generated manuscript/package outputs (not committed)
