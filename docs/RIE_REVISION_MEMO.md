# RIE Targeted Revision Memo

Date: 2026-09-01  
Base: validated C6.1 head `9080eeb1fc9c8f614debaab0ecea7b7793f4b898`  
Branch: `revision/rie-targeted-framing`

## Objective

Retarget the frozen correction note from *International Economics* to *Review of International Economics* without adding a model, proposition, robustness extension, empirical exercise, or new economic result.

## Title decision

Selected:

**Foreclosure and Limit Pricing in Standardization Unions: Revisiting Gandal and Shy (2001)**

Alternatives considered:

1. current `A Correction to Gandal and Shy (2001)` title;
2. `A Note on Foreclosure and Limit Pricing in Standardization Unions`;
3. `Foreclosure, Limit Pricing, and Standardization Unions`;
4. selected `Revisiting` title.

The selected title retains the original-paper connection and the substantive mechanism while reducing the risk that `Correction` is read as a publisher-issued correction notice. It remains deliberately restrained.

## What changed

### Abstract

Before: led with a correction to the published post-foreclosure price equilibrium.

After: opens with the international-economics question of whether a foreign supplier excluded from equilibrium sales can continue to discipline prices. It then states the two corrected price regimes and the welfare robustness result.

### Introduction

Before: began with Gandal and Shy (2001) and immediately narrowed to the price calculation.

After: begins with product standards, cross-border recognition, market access, and excluded suppliers; then poses the core question: whether zero foreign sales imply zero foreign competitive constraint. The original model, correction, limit-pricing mechanism, and welfare robustness result follow from that question.

Three verified references were added, and only for positioning:

- Chen and Mattoo (2008), regional standards agreements and excluded-country trade;
- Marette and Beghin (2010), standards and protectionism, published in RIE;
- Berti and Falvey (2018), trade and product standards, published in RIE.

### Conclusion

Before: summarized the corrected price branches and the unchanged welfare ranking.

After: explicitly distinguishes foreclosure of realized sales from disappearance of competitive discipline, then states that the original welfare ranking survives the corrected price subgame.

### Submission metadata

- RIE title and cover letter prepared.
- Double spacing adopted to satisfy the 25-double-spaced-page instruction.
- Funding, conflict-of-interest, data-availability, and AI-use statements aligned with current Wiley requirements.
- ORCID remains populated on the submission title page.

## What was deliberately not changed

The following files were left mathematically untouched:

- `paper/sections/02_foreclosure_calculation.tex`
- `paper/sections/03_corrected_equilibrium.tex`
- `paper/sections/04_welfare_robustness.tex`
- `code/verify_symbolic.py`
- `code/verify_numerical.py`

No new proposition, equilibrium concept, parameter, model extension, calibration, simulation result, policy extension, or empirical exercise was introduced.

## Frozen results

- Foreclosure threshold: `c=5/2`.
- For `5/2<c<3`: `p_M=c-1` and the foreclosure/entry constraint binds.
- For `3<=c<5`: `p_M=2` and the outsider constraint is slack.
- After foreclosure: `q_1=q_2=3/2`, `q_3=0`.
- `TS_M^SU=3V+1/4`.
- `TS^MR=3V-1/4`.
- Welfare gap: `1/2>0`.

## Independent verification after reframing

The mathematical core was independently rerun before repository edits.

- Core symbolic identities: PASS.
- Dense numerical global-deviation grid: 453 values of `c` on `[2.5001,4.999]`: PASS.
- Fine spatial grid: `N=80000`.
- Maximum apparent member discretization gain: `5.62495312497191e-05 < 0.00075` fixed grid bound.
- Maximum outsider profitable gain: `0`.
- Convergence check: apparent member gain falls from `0.00022499249999974325` at `N=20000` to `5.62495312497191e-05` at `N=80000`: PASS.
- Exact `c=4` published-profile counterexample: `2.25 -> 2.296875`, gain `0.046875 = 3/64`: PASS.
- Boundary continuity at `c=5/2` and `c=3`: PASS.
- Welfare identities and gap: PASS.

## Build QA

The RIE-framed manuscript was compiled with `latexmk`/pdfLaTeX and BibTeX using the repository fallback configuration.

- Build: PASS.
- PDF length: 12 double-spaced pages.
- Undefined references: 0.
- Undefined citations: 0.
- Overfull boxes after final wording adjustment: 0.
- Underfull boxes of material significance: 0.
- Rendered-page visual audit: PASS on all 12 pages.

## Remaining editorial risk

The principal risk is contribution narrowness rather than correctness or field fit: the benchmark is from 2001 and its headline member-country welfare ranking survives. The RIE framing addresses this without expanding the model by emphasizing the corrected equilibrium mechanism and the independent robustness result.

A separate practical cost remains: RIE charges a nonrefundable CHF 100 first-submission fee.
