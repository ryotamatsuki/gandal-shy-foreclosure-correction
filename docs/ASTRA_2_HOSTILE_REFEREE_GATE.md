# Astra-2 — Independent Hostile Referee Gate

**Date:** 2026-09-10  
**Initial audited baseline:** `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`  
**Bounded-repair branch:** `stage13r2/astra2-minor-repair`  
**Limited-recheck head:** `abe2706ca824790c00a6c21cc01dd1b8ef8decbc`  
**Repair PR:** `#14`  
**Manuscript:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Provisional target:** *International Economics*, short-format route  
**Initial Astra-2 verdict:** **B. MINOR EXPOSITION REPAIR**  
**Limited-recheck verdict:** **A. ASTRA-2 CLEARED — GO TO STAGE 14**

## 1. Executive outcome

Astra-2 independently reconstructed the core pricing and welfare arguments and found no new equilibrium counterexample requiring a return to C0–C4R or C2R-L. The initial hostile audit required three bounded Stage-13R2 repairs before submission QA.

Those three repairs were implemented on `stage13r2/astra2-minor-repair`, the repaired manuscript passed manuscript-integration CI, and Astra-2 then performed a limited recheck restricted to the required repair set.

Limited-recheck result:

- Repair 1 — cost-floor proof bridge: **PASS**;
- Repair 2 — highlight scope: **PASS**;
- Repair 3 — cover-letter welfare wording: **PASS**;
- new defect introduced by repairs: **NO**;
- final gate decision: **ASTRA-2 CLEARED — GO TO STAGE 14**.

Astra-2 is therefore closed. Stage 14 may begin after PR #14 is merged.

## 2. Headline scientific findings

The following results survived the full Astra-2 audit and the limited recheck:

1. quadratic long-arc indifference gives `x = 1 + (p_2-p_1)/4`;
2. the published complete profile `(3/2,3/2,c)` is non-Nash for every strict `c>5/2` in the manuscript's post-foreclosure range;
3. within symmetric, foreclosed, pure-strategy profiles `(s,s,r)`, the unrestricted game is characterized by U1/U2 as stated in Proposition 1;
4. the separate cost-floor game's piecewise member-price result is correct within the same stated class;
5. under a common symmetric continuation, member-country welfare is `3V+1/4`, one half above mutual recognition; with market-specific prices, the transfer term `(3/2)(s_B-s_A)` remains;
6. the manuscript does not justify a government-stage policy reversal, an all-equilibria characterization, or a global uniqueness claim.

No theorem statement, C3R freeze, C4R scientific conclusion, numerical verifier, or Lean-certified theorem was changed by the bounded repair.

## 3. Repair 1 — cost-floor proof bridge — PASS

The initial audited manuscript moved directly from the unrestricted U1/U2 characterization to intersecting that equilibrium set with the cost-floor restriction. Astra-2 correctly noted that, in a generic game, restricting strategies can create equilibria by deleting profitable deviations.

The repaired proof now makes the missing bridge explicit:

- at a cost-floor-feasible symmetric foreclosed candidate, each firm's candidate profit is nonnegative;
- a deviation deleted by the floor has `p_i < mc_i`;
- since demand is nonnegative, the deleted deviation yields `(p_i-mc_i)q_i <= 0`;
- hence no deleted deviation can strictly improve upon the candidate profit;
- therefore any symmetric foreclosed pure-strategy equilibrium of the cost-floor game is also a Nash equilibrium of the unrestricted game;
- intersecting U1/U2 with the cost-floor restrictions is consequently valid within the stated equilibrium class.

Astra-2's limited recheck returned **PASS** on this bridge. The result is a proof completion, not a theorem change.

## 4. Repair 2 — highlight scope — PASS

The repaired third highlight reads:

> `Within symmetric foreclosed pure equilibria, a cost floor pins down member prices.`

Astra-2 confirmed that this wording matches Proposition 1's actual scope and does not imply global uniqueness or characterization of all equilibria.

## 5. Repair 3 — cover-letter welfare wording — PASS

The overly strong phrase `exact continuation conditions under which its original member-country welfare comparison is preserved` was removed.

The repaired cover letter now states that:

- a common symmetric continuation recovers the original one-half member-country welfare gap; and
- market-specific continuation prices leave the cross-market transfer term.

Astra-2 confirmed that this matches Proposition 2 and does not misstate the common-price condition as necessary for preserving the sign of the welfare ranking.

## 6. Non-required welfare observation

Astra-2 additionally noted that, for market-specific symmetric continuations,

`TS_A^SU - TS^MR = 1/2 + (3/2)(s_B-s_A)`.

Thus both member countries remain strictly above mutual recognition whenever `|s_A-s_B| < 1/3`. This observation is mathematically consistent with Proposition 2 but was not required as an additional manuscript result and was not promoted into a new headline claim during the bounded repair.

## 7. Lean and numerical verification assessment

Astra-2 found the manuscript's Lean description appropriately limited: the project certifies proof-critical algebraic and quantified-inequality components, not a complete formalization of Salop demand or a machine-checked equivalence between the full Nash conditions and U1/U2.

The Python verifier was also judged appropriate as a falsification/regression aid. It varies all three firms' prices and does not repeat the pre-Astra error of fixing `p_3=c`, but it is not represented as an exhaustive equilibrium-discovery proof.

No Lean theorem change was required for the bounded Stage-13R2 repair.

## 8. Repair verification record

The repaired manuscript head `72ed861e3460cbcaf5eaf0a763f789c70ed07332` passed GitHub Actions manuscript-integration run `34379361638`.

The run passed:

- symbolic and numerical verification;
- manuscript and submission-package build;
- final clean LaTeX-log gate;
- generated-artifact checks and upload.

Subsequent commits through limited-recheck head `abe2706ca824790c00a6c21cc01dd1b8ef8decbc` were documentation-only and did not alter the repaired manuscript or submission artifacts.

## 9. Final workflow decision

Astra-2 is **CLEARED**.

No return to C0–C1R, C2R, C2R-L, C3R, C4R, Stage 12R2, or another full Stage 13R2 integration cycle is required.

After PR #14 is merged, the next mandatory stage is:

`Stage 14 — Submission QA`.

Stage 14 must freshly verify all material *International Economics* requirements from current official sources and, where required, the authenticated submission portal. Any material `UNVERIFIED` or unresolved `CONFLICT` remains blocking under the project workflow.