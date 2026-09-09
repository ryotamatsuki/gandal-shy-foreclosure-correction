# Astra-2 — Independent Hostile Referee Gate

**Date:** 2026-09-10  
**Audited baseline:** `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`  
**Manuscript:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Provisional target:** *International Economics*, short-format route  
**Actual Astra-2 verdict:** **B. MINOR EXPOSITION REPAIR**  
**Final gate decision on the audited baseline:** **DO NOT GO TO STAGE 14**

> **Status correction.** An earlier repository update incorrectly recorded a completed Astra-2 limited recheck and clearance. The user subsequently supplied the actual Astra-2 output reproduced by this record: `B. MINOR EXPOSITION REPAIR`. The three required repairs have already been implemented, verified by CI, and merged in PR `#14`, but the required **limited Astra-2 recheck has not yet been completed**. Stage 14 is therefore blocked.

## 1. Executive outcome

Astra-2 independently reconstructed the core pricing and welfare arguments and found no new equilibrium counterexample requiring a return to C0–C4R or C2R-L. The scientific core survived the second hostile audit, but three bounded Stage-13R2 repairs were required before submission QA.

Headline audit:

- Proposition 1 — unrestricted U1/U2 characterization: **PASS**;
- Proposition 2 — welfare formulas: **PASS**;
- published Appendix-B profile correction: **PASS**;
- cost-floor characterization: **CONDITIONAL PASS**, because the written proof omitted the bridge showing that deleting below-cost deviations cannot create additional restricted-game equilibria in the stated class;
- welfare-selection result: **PASS**.

Publication significance was assessed as **MODERATE**. Astra-2 found the paper worth sending to external review after the bounded repair, while retaining the editorial risk that a compact correction to an older theory benchmark may be judged too narrow.

## 2. Independent mathematical findings

Astra-2 confirmed the following.

1. Quadratic long-arc indifference gives

   `x = 1 + (p_2-p_1)/4`.

2. The published complete profile `(3/2,3/2,c)` is non-Nash for every strict `c>5/2` in the manuscript's post-foreclosure range. A sufficiently small member-firm price increase has gain

   `Δπ = (3/8)ε - (3/4)ε² > 0`.

3. Within symmetric, foreclosed, pure-strategy profiles `(s,s,r)`, the unrestricted game is characterized by:

   - U1: `3/2 <= s < 2`, `r=s+1`, `c>=s+1`;
   - U2: `s=2`, `r>=3`, `c>=3`.

4. The separate cost-floor game's piecewise member-price result is correct within the same stated class, subject to the proof bridge described below.

5. For a common symmetric continuation price,

   `TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`,

   so the exact original gap is `1/2`.

   With market-specific continuation prices,

   `TS_A^SU=3V+1/4+(3/2)(s_B-s_A)`.

   Hence welfare levels are selection dependent. This does not imply a general government-stage reversal.

Astra-2 did not certify asymmetric pure equilibria, mixed equilibria, or a complete government-stage equilibrium, and the manuscript does not claim those results.

## 3. Counterexample search

No counterexample was found against U1/U2, the cost-floor piecewise member price, or the welfare identities.

Astra-2 reported an independent exact-demand calculation rather than a consumer-grid approximation, including:

- 128 equilibrium candidates with no profitable unilateral deviation over the continuous price ranges checked;
- 446 necessity/game-regime checks with no disagreement with the analytic conditions;
- 150 asymmetric-price samples with no additional strict equilibrium detected, without treating that as a proof of nonexistence;
- checks around `c=5/2`, `c=3`, `c=4`, and the upper end of the manuscript range;
- negative prices, large downward and upward deviations, zero demand, below-cost outsider prices, and large zero-sales outsider quotes.

The existing project verifier was also judged appropriate as a falsification/regression aid and was not mistaken for an exhaustive equilibrium-discovery proof.

## 4. Repair 1 — cost-floor proof bridge

**Classification:** exposition repair.  
**Astra-2 status on audited baseline:** required.

The audited manuscript moved directly from the unrestricted U1/U2 characterization to intersecting that equilibrium set with the cost-floor restriction. In a generic game, restricting strategies can create equilibria by deleting profitable deviations, so this intersection step required justification.

Required bridge:

- at a cost-floor-feasible symmetric foreclosed candidate, candidate profits are nonnegative;
- any deleted deviation has `p_i < mc_i`;
- because demand is nonnegative, such a deviation yields `(p_i-mc_i)q_i <= 0`;
- hence no deleted deviation can strictly improve upon the candidate profit;
- consequently, a symmetric foreclosed pure-strategy equilibrium of the cost-floor game is also an equilibrium of the unrestricted game;
- only then is intersecting U1/U2 with the cost-floor restrictions legitimate.

**Implementation status:** implemented and merged in PR `#14`. The manuscript now contains this bridge explicitly. The result is a proof completion, not a theorem change.

## 5. Repair 2 — highlight scope

**Classification:** scope repair.  
**Astra-2 status on audited baseline:** required.

The original third highlight was too broad as a standalone statement. Astra-2 required the result to be limited to the symmetric, foreclosed, pure-strategy class.

**Implementation status:** implemented and merged in PR `#14` as:

> `Within symmetric foreclosed pure equilibria, a cost floor pins down member prices.`

## 6. Repair 3 — cover-letter welfare wording

**Classification:** scope repair.  
**Astra-2 status on audited baseline:** required.

The phrase `exact continuation conditions under which its original member-country welfare comparison is preserved` was too strong. A common symmetric continuation recovers the exact original one-half gap, but it is not necessary for preserving the sign of the welfare ranking.

**Implementation status:** implemented and merged in PR `#14`. The cover letter now distinguishes:

- the exact `1/2` gap under a common symmetric continuation; and
- the cross-market transfer term under market-specific continuation prices.

## 7. Non-required welfare observation

Astra-2 additionally noted that

`TS_A^SU - TS^MR = 1/2 + (3/2)(s_B-s_A)`.

Thus both member countries remain strictly above mutual recognition whenever `|s_A-s_B| < 1/3`. It also identified the corresponding parameter-region distinction in the unrestricted symmetric continuation class. Astra-2 explicitly did **not** require adding this as a new headline result, and the bounded repair did not expand the paper around it.

## 8. Lean audit

Astra-2 judged the Lean description appropriately limited. The project certifies proof-critical algebraic and quantified-inequality components, including the long-arc coefficient, a `c=4` published-profile counterexample, deviation inequalities, encoded multiplicity conditions, cost-floor logical reduction, and welfare identities.

It does **not** formalize:

- demand measure from the Salop primitives;
- equivalence between the full Nash conditions and U1/U2;
- equivalence between the restricted-game Nash conditions and the encoded cost-floor condition;
- every `c>5/2` regime-transition argument from primitives;
- the full U2 demand envelope from the economic model;
- the nonmember-market equilibrium from primitives.

No `sorry`, `admit`, or custom axiom insertion was reported. No Lean theorem change was required by Astra-2.

## 9. Repair verification record

The three required repairs were implemented on `stage13r2/astra2-minor-repair` and later merged in PR `#14`.

- repaired manuscript CI head: `72ed861e3460cbcaf5eaf0a763f789c70ed07332`;
- manuscript-integration run `34379361638`: **success**;
- symbolic/numerical verification: **PASS**;
- manuscript and package build: **PASS**;
- final clean LaTeX-log gate: **PASS**;
- generated-artifact checks/upload: **PASS**;
- repair branch head before the mistaken clearance bookkeeping: `abe2706ca824790c00a6c21cc01dd1b8ef8decbc`;
- bounded-repair merge: `02a691e9260c48a5e9485e7d8188caf3648f918f`.

Merging the repair does not itself constitute Astra-2 clearance. The repair content remains valid and need not be reverted.

## 10. Workflow return and re-clearance contract

**Return point:** `Stage 13R2` only.

Do not reopen C0–C1R, C2R, C2R-L, C3R, C4R, or Stage 12R2 unless the repair itself changes a theorem or reveals a new scientific inconsistency.

The next required action is a **limited Astra-2 recheck** of exactly the three repairs. The preferred recheck target is the current repaired `main` after the documentation-status correction is merged; equivalently, Astra may inspect the manuscript/submission-artifact content introduced by PR `#14`.

Proceed to Stage 14 only if that limited recheck returns a clear submission-level clearance.

## 11. Current final gate decision

**DO NOT GO TO STAGE 14 YET.**

The three repairs are implemented and CI-clean, but Astra-2 has not yet re-cleared them. Stage 14 remains blocked pending the limited recheck.
