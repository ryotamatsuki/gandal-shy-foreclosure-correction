# Astra-2 — Independent Hostile Referee Gate

**Date:** 2026-09-10  
**Audited baseline:** `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`  
**Manuscript:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Provisional target:** *International Economics*, short-format route  
**Astra-2 verdict:** **B. MINOR EXPOSITION REPAIR**  
**Final gate decision on audited baseline:** **DO NOT GO TO STAGE 14**

## 1. Executive outcome

Astra-2 independently reconstructed the core pricing and welfare arguments and found no new equilibrium counterexample requiring a return to C0–C4R or C2R-L. The scientific core survived the second hostile audit, but three bounded Stage-13R2 repairs were required before submission QA.

Headline audit:

- Proposition 1 — unrestricted U1/U2 characterization: **PASS**;
- Proposition 2 — welfare formulas: **PASS**;
- published Appendix-B profile correction: **PASS**;
- cost-floor characterization: **CONDITIONAL PASS**, because the written proof omitted the bridge showing that deleting below-cost deviations cannot create additional restricted-game equilibria in the stated class;
- welfare-selection result: **PASS**.

Publication significance was assessed as **MODERATE**. The audit found the paper suitable to send to external review after the bounded repair, while retaining the known risk that a compact correction to an older theory benchmark may be judged too narrow editorially.

## 2. Scientific findings that remain unchanged

Astra-2 independently confirmed:

1. quadratic long-arc indifference gives `x = 1 + (p_2-p_1)/4`;
2. the published complete profile `(3/2,3/2,c)` is non-Nash for every strict `c>5/2` in the manuscript's post-foreclosure range;
3. within symmetric, foreclosed, pure-strategy profiles `(s,s,r)`, the unrestricted game is characterized by U1/U2 as stated in Proposition 1;
4. the separate cost-floor game's piecewise member-price result is correct within the same stated class;
5. under a common symmetric continuation, member-country welfare is `3V+1/4`, one half above mutual recognition; with market-specific prices, the transfer term `(3/2)(s_B-s_A)` remains;
6. the manuscript does not justify a government-stage policy reversal, an all-equilibria characterization, or a global uniqueness claim.

No theorem statement, C3R freeze, C4R scientific conclusion, or Lean-certified theorem needs to change.

## 3. Required Stage-13R2 repairs

### Repair 1 — cost-floor proof bridge

**Classification:** exposition repair.

The audited manuscript moved directly from the unrestricted U1/U2 characterization to `Intersect U1 with r >= c`. In a generic game, restricting strategies can create equilibria by deleting profitable deviations, so the intersection step requires justification.

Required bridge:

- at any cost-floor-feasible symmetric foreclosed candidate, candidate profits are nonnegative;
- any deleted deviation has `p_i < mc_i` and therefore profit `(p_i-mc_i)q_i <= 0` because demand is nonnegative;
- hence no deleted deviation can strictly improve on the candidate profit;
- consequently, a symmetric foreclosed pure-strategy equilibrium of the cost-floor game is also an equilibrium of the unrestricted game, and intersecting U1/U2 with the cost-floor restrictions is valid.

This closes a proof gap without changing the theorem.

### Repair 2 — highlight scope

**Classification:** scope repair.

The third highlight must state that the cost-floor benchmark applies within the symmetric, foreclosed, pure-strategy equilibrium class. The unqualified baseline wording was too broad when read as a standalone submission artifact.

### Repair 3 — cover-letter welfare wording

**Classification:** scope repair.

The phrase `exact continuation conditions under which its original member-country welfare comparison is preserved` was too strong. A common symmetric continuation recovers the exact original one-half gap, but it is not the necessary condition for preserving the welfare ranking. The cover letter must instead distinguish the exact common-price `1/2` result from the market-specific transfer term.

## 4. Non-required observations

Astra-2 additionally noted that, for market-specific symmetric continuations,

`TS_A^SU - TS^MR = 1/2 + (3/2)(s_B-s_A)`.

Thus both member countries remain strictly above mutual recognition whenever `|s_A-s_B| < 1/3`. This observation is mathematically consistent with Proposition 2, but the referee did **not** require adding the resulting parameter-region classification to the manuscript. It should not be promoted into a new headline result during this bounded repair.

## 5. Lean and numerical verification assessment

Astra-2 found the manuscript's Lean description appropriately limited: the project certifies proof-critical algebraic and quantified-inequality components, not a complete formalization of Salop demand or a machine-checked equivalence between the full Nash conditions and U1/U2.

The Python verifier was also judged appropriate as a falsification/regression aid. It varies all three firms' prices and does not repeat the pre-Astra error of fixing `p_3=c`, but it is not represented as an exhaustive equilibrium-discovery proof.

No Lean theorem change is required for the bounded Stage-13R2 repair.

## 6. Workflow return and re-clearance contract

**Return point:** `Stage 13R2` only.

Do not reopen C0–C1R, C2R, C2R-L, C3R, C4R, or Stage 12R2 unless the bounded repair itself changes a theorem or reveals a new scientific inconsistency.

After implementing the three repairs:

1. rerun the manuscript integration CI/build;
2. confirm that no scope wording regressed elsewhere;
3. send the repaired head to Astra-2 for a **limited recheck of the three required repairs**;
4. proceed to Stage 14 only if Astra-2 clears that recheck.

Until then, Stage 14 remains blocked.
