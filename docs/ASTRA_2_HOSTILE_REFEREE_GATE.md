# Astra-2 — Independent Hostile Referee Gate

**Date:** 2026-09-10  
**Initial audited baseline:** `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`  
**Bounded-repair PR:** `#14`  
**Bounded-repair merge:** `02a691e9260c48a5e9485e7d8188caf3648f918f`  
**Limited-recheck baseline:** `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d`  
**Manuscript:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Provisional target:** *International Economics*, short-format route  
**Initial Astra-2 verdict:** **B. MINOR EXPOSITION REPAIR**  
**Final Astra-2 verdict after actual limited recheck:** **A. ASTRA-2 CLEARED — GO TO STAGE 14**

## 1. Executive outcome

Astra-2 independently reconstructed the core pricing and welfare arguments on the initial Stage-13R2 manuscript and found no new equilibrium counterexample requiring a return to C0–C4R or C2R-L. It required three bounded Stage-13R2 repairs before submission QA:

1. close the cost-floor strategy-restriction proof bridge;
2. qualify the third highlight by the symmetric, foreclosed, pure-strategy class;
3. narrow the cover-letter welfare wording so the exact common-price `1/2` gap is distinguished from the broader market-specific transfer term.

Those repairs were implemented, passed manuscript-integration CI, and were merged in PR `#14`. A later bookkeeping correction restored the repository to a fail-closed state until a real limited recheck occurred. Astra-2 then performed that actual limited recheck on `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d`.

Final limited-recheck result:

- Repair 1 — **PASS**;
- Repair 2 — **PASS**;
- Repair 3 — **PASS**;
- new defect introduced by repairs — **NO**;
- final gate decision — **A. ASTRA-2 CLEARED — GO TO STAGE 14**.

Astra-2 is now closed.

## 2. Headline scientific findings preserved from the full hostile audit

The following results survived the full Astra-2 audit:

1. quadratic long-arc indifference gives `x = 1 + (p_2-p_1)/4`;
2. the published complete profile `(3/2,3/2,c)` is non-Nash for every strict `c>5/2` in the manuscript's post-foreclosure range;
3. within symmetric, foreclosed, pure-strategy profiles `(s,s,r)`, the unrestricted game is characterized by U1/U2 as stated in Proposition 1;
4. the separate cost-floor game's piecewise member-price result is correct within the same stated class;
5. under a common symmetric continuation, member-country welfare is `3V+1/4`, one half above mutual recognition; with market-specific prices, the transfer term `(3/2)(s_B-s_A)` remains;
6. the manuscript does not justify a government-stage policy reversal, an all-equilibria characterization, or a global uniqueness claim.

Publication significance was assessed as **MODERATE**. No theorem statement, C3R freeze, C4R scientific conclusion, numerical verifier, or Lean-certified theorem needed to change.

## 3. Initial Repair 1 objection — cost-floor proof bridge

**Classification:** exposition repair.  
**Initial status:** required.  
**Final limited-recheck status:** **PASS**.

The initial manuscript moved directly from the unrestricted U1/U2 characterization to intersecting that equilibrium set with the cost-floor restriction. Astra-2 correctly observed that, in a generic game, restricting strategies can create equilibria by deleting profitable deviations.

The repaired proof makes the missing bridge explicit:

- at a cost-floor-feasible symmetric foreclosed candidate, each firm's candidate profit is nonnegative;
- any deviation deleted by the floor has `p_i < mc_i`;
- since demand is nonnegative, such a deviation yields `(p_i-mc_i)q_i <= 0`;
- hence a deleted deviation cannot strictly improve upon the candidate, including when the candidate profit is zero;
- therefore a symmetric foreclosed pure-strategy equilibrium of the cost-floor game is also a Nash equilibrium of the unrestricted game;
- conversely, deleting infeasible deviations from a cost-floor-feasible unrestricted equilibrium preserves equilibrium;
- hence, within the stated class, the restricted equilibrium set is obtained by intersecting U1/U2 with the cost-floor constraints.

Astra-2 further confirmed the resulting branches:

- U1 plus `r>=c` yields `r=c=s+1`;
- U2 plus `r>=c` yields member price `s=2` and outsider quote `r>=c`.

The initial objection is fully closed.

## 4. Initial Repair 2 objection — highlight scope

**Classification:** scope repair.  
**Initial status:** required.  
**Final limited-recheck status:** **PASS**.

The repaired third highlight reads:

> `Within symmetric foreclosed pure equilibria, a cost floor pins down member prices.`

Astra-2 confirmed that this matches Proposition 1's actual scope, limits the object being pinned down to member prices, and does not imply asymmetric/mixed/government-stage characterization or global uniqueness of the outsider price.

## 5. Initial Repair 3 objection — cover-letter welfare wording

**Classification:** scope repair.  
**Initial status:** required.  
**Final limited-recheck status:** **PASS**.

The phrase `exact continuation conditions under which its original member-country welfare comparison is preserved` was removed.

The repaired cover letter states instead that:

- a common symmetric continuation recovers the exact original one-half member-country welfare gap; and
- market-specific continuation prices leave the cross-market transfer term.

Astra-2 confirmed that this does not present the common-price condition as necessary for preserving the sign of the welfare ranking, does not imply inevitable reversal under market-specific continuation, and does not infer a government-stage policy reversal.

## 6. New-defect check

**Result:** **NO new defect introduced by repairs.**

Astra-2 compared the repaired baseline against the relevant Proposition 1/2, Abstract, Introduction, Conclusion, highlights, cover letter, and Lean-scope statements and found no new mathematical defect, quantifier expansion, or cross-artifact scope conflict.

## 7. Lean and numerical scope retained

Astra-2 continues to judge the Lean description appropriately limited. The project certifies proof-critical algebraic and quantified-inequality components; it does not formalize the entire Salop demand game or prove the full Nash correspondence from primitives.

The Python verifier remains a falsification/regression aid. It varies all three posted prices and does not fix `p_3=c`, but it is not represented as an exhaustive equilibrium-discovery proof.

No Lean theorem or numerical verifier change was required by the bounded repair.

## 8. Verification and provenance

The bounded repairs were implemented in PR `#14` and merged as `02a691e9260c48a5e9485e7d8188caf3648f918f`.

The repaired manuscript head `72ed861e3460cbcaf5eaf0a763f789c70ed07332` passed manuscript-integration run `34379361638`, including:

- symbolic and numerical verification;
- manuscript and submission-package build;
- final clean LaTeX-log gate;
- generated-artifact checks and upload.

A bookkeeping error briefly recorded a clearance result before an actual limited recheck existed. PR `#15` corrected the repository to the fail-closed status; its merge `ec164d092c5be14df12dbf44c40c8d947d7cdc7d` then became the actual limited-recheck baseline.

The present record reflects the genuine subsequent Astra-2 limited-recheck result supplied for that baseline.

## 9. Final workflow decision

**A. ASTRA-2 CLEARED — GO TO STAGE 14.**

No return to C0–C1R, C2R, C2R-L, C3R, C4R, Stage 12R2, or Stage 13R2 is required.

The next mandatory stage is:

`Stage 14 — Submission QA`.

Stage 14 must freshly verify all material *International Economics* requirements from current official sources and, where required, the authenticated submission portal. Any material `UNVERIFIED` or unresolved `CONFLICT` remains blocking under the project workflow.
