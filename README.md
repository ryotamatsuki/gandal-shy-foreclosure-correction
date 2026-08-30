# Gandal-Shy Foreclosure Correction

Private research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

**Status:** C4 research draft.  
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

- `docs/` -- C0-C3 provenance and source ledger
- `paper/` -- modular LaTeX manuscript and technical appendix
- `code/` -- symbolic and numerical equilibrium verification
- `output/` -- generated manuscript output (ignored except `.gitkeep`)
