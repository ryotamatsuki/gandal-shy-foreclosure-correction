# Gandal-Shy Foreclosure Correction

Private research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

**Status:** C5-audited short-paper draft; GO TO C6 submission freeze.  
**Target:** *International Economics* -- Short Paper.  
**Research objective:** Re-solve the post-foreclosure price subgame in the published quadratic-transport specification and determine whether the corrected equilibrium changes the member-country welfare comparison in Proposition 3.

The C3 freeze permits exactly two main propositions:

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

## Structure

- `docs/` -- C0-C5 provenance, journal-fit audit, and source ledger
- `paper/` -- modular self-contained LaTeX manuscript
- `code/` -- symbolic and numerical equilibrium verification
- `output/` -- generated manuscript output (ignored except `.gitkeep`)
