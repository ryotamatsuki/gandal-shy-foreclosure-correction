# C0-C1 Mathematical Audit

> **HISTORICAL / SUPERSEDED AFTER ASTRA-1.**  
> This pre-Astra audit is retained for provenance but is no longer controlling scientific authority. In particular, item 7 below overstates an equilibrium existence result as a price characterization in the unrestricted game, and item 8 overstates welfare robustness across continuation selections. See `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md` and `docs/REVISION_TO_RESUBMISSION_WORKFLOW.md` for the reopened analysis.

## Status

Historical C1 verdict: **GO TO C2**.  
Current status: **SUPERSEDED**.

## Canonical findings at the time of the pre-Astra audit

1. The published three-firm interior equilibrium in Gandal and Shy (2001), equations (2)-(4), is reproduced from the primitive quadratic-transport demand system.
2. In a standardization-union member market with costs `(0,0,c)`, the interior outsider share is `q_O = 1 - 2c/5`; therefore the foreclosure threshold `c = 5/2` is unchanged.
3. After foreclosure, the short-arc indifferent consumer is `x^S = 1/2 + (p_2-p_1)/2`.
4. Under quadratic transportation costs, the long-arc indifferent consumer is `x^L = 1 + (p_2-p_1)/4`.
5. Hence two-active-firm demand is `q_1 = 3/2 + (3/4)(p_2-p_1)`.
6. The published post-foreclosure **complete profile with outsider price `p_3=c`** is not a Nash equilibrium for strict `c>5/2`; the original wording here was too broad about the isolated member price. At `c=4`, the deviation `p_1: 3/2 -> 7/4` raises profit from `9/4` to `147/64` when the other prices are `(3/2,4)`.
7. Historical claim, now superseded: the corrected symmetric member price was stated as piecewise `p_M=c-1` for `5/2<c<3` and `p_M=2` for `3<=c<5` without distinguishing unrestricted multiplicity from an explicit cost-floor strategy restriction.
8. Historical claim, now superseded in scope: the member-country welfare calculation under a common symmetric foreclosure price simplifies to `TS_M^SU=3V+1/4`; this is not selection-free when different symmetric continuation prices are selected across the two segmented union markets.
9. Secondary audit findings include a Table 2 coefficient correction (`16c^2 -> 20c^2` in the first conversion-cost row), a boundary qualification at `c=5/4` in Proposition 2, and piecewise corrections to the country-size and network-effect foreclosure calculations.

The old symbolic and numerical scripts are retained as pre-Astra verification provenance. They must not be treated as certification of the reopened equilibrium-set claims; C2R will replace the fixed-`p_3=c` falsification design.