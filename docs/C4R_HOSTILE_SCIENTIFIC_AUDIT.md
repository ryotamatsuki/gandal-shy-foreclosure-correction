# C4R — Hostile Scientific Self-Audit

**Date:** 2026-09-09  
**Branch:** `audit/c4r-hostile`  
**Base:** `main@5f0a57fe99b94deb51f229254a7f5882ac21ad49`  
**Frozen authority attacked:** `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`  
**Supporting records:** `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`, `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`, `docs/C2R_L_LEAN_CERTIFICATION.md`

## 1. Executive verdict

**C4R verdict: `PASS — GO TO STAGE 12R2`.**

The hostile audit does not find a counterexample inside the exact C3R theorem class. The revised theory survives attacks on the unrestricted equilibrium characterization, the explicit cost-floor characterization, the `c=5/2` and `c=3` boundaries, zero-demand/below-cost strategies, tie-breaking, continuation-dependent welfare, and the stated scope of Lean certification.

One wording risk was identified: a contribution-summary sentence in C3R can be read as saying that the cost-floor restriction collapses member-price multiplicity in the **entire** price game. The proved result is narrower: it collapses member-price multiplicity **within symmetric, foreclosed, pure-strategy equilibria**. This is a freeze-language clarification only; it does not change a theorem, quantifier, strategy set, proof, numerical verifier, or Lean theorem. The qualified wording below is controlling for all downstream manuscript work.

No return to C0–C1R, C2R, or C2R-L is required.

---

## 2. Attack A — Is the published profile really non-Nash for every strict `c>5/2`?

### Attack

The Lean certificate contains an exact `c=4` counterexample, while C3R makes the broader analytic statement that `(3/2,3/2,c)` is not Nash for every strict `c>5/2` in the paper's range. The risk is that the `c=4` example might not support the full quantifier near the foreclosure threshold.

### Result

The broader analytic claim survives independently of the `c=4` checkpoint.

At the published profile, let firm 1 raise price from `3/2` to `3/2+epsilon`. For any strict `c>5/2`, choose a sufficiently small positive `epsilon` so that the outsider remains foreclosed after the deviation. On that regular two-member branch, the profit gain simplifies to

`(3/8) epsilon - (3/4) epsilon^2 = (3/8) epsilon (1-2 epsilon)`.

It is strictly positive for `0<epsilon<1/2`. Since `c-5/2>0`, one can choose `epsilon` smaller than both the available foreclosure slack and `1/2`.

Therefore the published complete profile fails Nash for every strict `c>5/2`, not merely at `c=4`.

### Verdict

`PASS`.

The exact `c=4` Lean theorem remains a formal checkpoint; the full parameter quantifier remains an analytic theorem, exactly as C3R states.

---

## 3. Attack B — Hidden zero-sales outsider prices and unrestricted multiplicity

### Attack

Try to reproduce the original Astra failure by varying the zero-sales outsider quote rather than fixing `p_3=c`. Check whether C3R has again mistaken existence for characterization.

### Result

C3R explicitly incorporates the Astra mechanism instead of suppressing it. Within the frozen class `(s,s,r)`, the unrestricted game is characterized as:

- U1: `3/2 <= s < 2`, `r=s+1`, `c>=s+1`;
- U2: `s=2`, `r>=3`, `c>=3`.

The logic that previously failed is now part of the theorem: when `s<2`, raising the outsider quote above `s+1` reopens a profitable upward member deviation, while a quote at `s+1` can support lower member prices even when it lies below outsider marginal cost and yields zero sales.

No claim is made that only the outsider price is nonunique. C3R freezes genuine member-price multiplicity.

### Verdict

`PASS`.

---

## 4. Attack C — Global member deviations and demand-region leakage

### Attack

Check whether the U1 proof is only local and whether large upward/downward deviations enter demand regions not covered by the proof.

### Result

The proof architecture remains global within the exact theorem class.

For U1, deviations are partitioned into negative prices, large downward deviations, the regular foreclosed branch, the outsider-relevant upward branch, and zero-demand prices. The C2R primitive best-response routine independently searches the full unilateral price threshold set rather than only local derivatives. The C2R-L Lean file certifies the proof-critical no-gain inequalities and the deviation partition conditional on the analytic demand-region mapping.

No new price region was found that generates a profitable deviation for a U1 or U2 profile.

### Verdict

`PASS`.

The demand formula `q_1=3/2+(3/4)(p_2-p_1)` must still not be used outside its regular two-member branch. C3R already prohibits that overextension.

---

## 5. Attack D — Cost-floor game versus the original game

### Attack

Try to smuggle the no-below-cost condition into the original model, or to describe it as WLOG, Nash-implied, or generic weak-dominance elimination.

### Result

C3R keeps the two games distinct. The cost-floor game is defined by the explicit strategy restriction

`p_i >= marginal cost in that market`.

For the member market this gives `p_1,p_2>=0` and `p_3>=c`. The restriction is not attributed to Gandal and Shy (2001), is not called WLOG, and is not derived from Nash equilibrium.

Within the exact frozen class of symmetric foreclosed pure-strategy equilibria, intersecting the unrestricted U1/U2 set with the outsider cost floor yields:

- `5/2 <= c < 3`: `(c-1,c-1,c)`;
- `c>=3`: member prices `(2,2)` and any outsider quote `p_3>=c`.

The theorem therefore survives.

### Important scope warning

The cost-floor result is **not** a complete equilibrium-selection theorem for the unrestricted or restricted game. Asymmetric pure equilibria and mixed equilibria are not characterized. Consequently, downstream text must not say simply that the cost floor "restores uniqueness" or "selects the equilibrium" without the qualifier **within symmetric, foreclosed, pure-strategy equilibria**.

### Verdict

`PASS WITH WORDING CLARIFICATION`.

This is a scope clarification, not a theorem change.

---

## 6. Attack E — Boundary `c=5/2`

### Attack

Check whether the lower boundary is incorrectly treated as a strict foreclosure interior point.

### Result

At `c=5/2`, the symmetric foreclosed set reaches the boundary profile `(3/2,3/2,5/2)`. This is the zero-share boundary of the three-active-firm solution and is used as a consistency check rather than as part of the paper's strict main range `5/2<c<5`.

The zero-demand outsider tie is measure zero and does not generate positive profit.

### Verdict

`PASS`.

---

## 7. Attack F — Boundary `c=3`

### Attack

Check whether the paper again treats `c=3` as a region where the exclusion constraint is already strictly slack.

### Result

C3R correctly treats `c=3` as the connection point.

- In the cost-floor game, the lower branch reaches `p_M=c-1=2`.
- The upper branch also has `p_M=2`.
- The exclusion condition binds at equality at `c=3`.
- Strict slack begins only for `c>3`.

In the unrestricted game, lower-price U1 equilibria continue to coexist at `c=3`, while U2 also becomes available. C3R records this multiplicity rather than declaring a unique regime switch in the original game.

### Verdict

`PASS`.

---

## 8. Attack G — Tie-breaking and zero-measure consumers

### Attack

Check whether the additional equilibria or the published-profile counterexample depend on assigning positive mass to indifferent consumers.

### Result

They do not. At the foreclosure threshold, the relevant outsider/member ties occur only at isolated boundary points. With an atomless uniform consumer distribution they have zero measure. Reassigning those zero-measure consumers does not change quantities, profits, or the profitable-deviation logic.

The numerical verifier uses a deterministic discrete tie rule only as a computational convention; the analytic theorem does not rely on positive-mass ties.

### Verdict

`PASS`.

---

## 9. Attack H — Asymmetric and mixed equilibria

### Attack

Ask whether unresolved asymmetric or mixed equilibria invalidate a theorem or welfare statement currently written as if it applied to the whole game.

### Result

No frozen theorem claims to characterize those objects. C3R repeatedly restricts the equilibrium characterization to symmetric, foreclosed, pure-strategy equilibria in one union-member market and explicitly lists asymmetric pure equilibria and mixed equilibria as open.

They therefore cannot refute U1/U2 or F1/F2 as stated.

However, their unresolved status matters for exposition and publication significance. In particular:

- the cost-floor result must not be sold as global uniqueness;
- the cost-floor game supplies a transparent **symmetric continuation**, not a complete refinement of every possible continuation;
- welfare claims must remain conditional on the stated continuation selection.

This issue belongs in Stage 12R2's significance assessment and Stage 13R2's wording discipline, not in a reopened mathematical stage unless the manuscript later broadens its quantifiers.

### Verdict

`PASS WITH DOWNSTREAM SCOPE WARNING`.

---

## 10. Attack I — Welfare accounting and cross-market selection

### Attack

Check whether the price cancellation silently assumes the same continuation price in both segmented union markets.

### Result

C3R now makes the assumption explicit.

For a common symmetric price `s`, the member country's consumer surplus and worldwide domestic-firm profit cancel the price transfer:

`CS_M^SU = 3V-3s-3/4`,

`Pi_M^SU = 3s+1`,

hence

`TS_M^SU = 3V+1/4`.

Against the original mutual-recognition benchmark `TS^MR=3V-1/4`, the gap is `1/2`.

If the two union markets instead select `s_A` and `s_B`, country A obtains

`TS_A^SU = 3V+1/4+(3/2)(s_B-s_A)`.

Therefore the welfare result is not selection-free. C3R does not claim otherwise and does not infer a government-stage reversal.

### Verdict

`PASS`.

---

## 11. Attack J — Does the cost-floor continuation actually prove Proposition 3 robust?

### Attack

Try to upgrade the existence of one transparent symmetric continuation into a statement about every equilibrium of the original game or every equilibrium of the cost-floor game.

### Result

That upgrade is not valid and is prohibited by C3R.

What is established is narrower:

- under a common symmetric continuation, the original member-country gap remains `1/2`;
- the symmetric cost-floor continuation is one class satisfying that condition;
- unrestricted continuation multiplicity makes the original-game welfare comparison selection dependent.

Thus the correction no longer supports the pre-Astra sentence "Proposition 3 is robust" without a continuation qualifier.

### Verdict

`PASS`.

---

## 12. Attack K — Limit-pricing terminology

### Attack

Ask whether "limit pricing" incorrectly imports an entry stage or an informational-signaling mechanism.

### Result

C3R authorizes the term only for the cost-floor lower branch `5/2<c<3`, and only as static exclusion-maintenance pricing: the outsider has zero equilibrium sales while its cost-based zero-demand constraint binds the member price at `c-1`.

No signaling, reputation, or informational mechanism is claimed.

### Verdict

`PASS`, subject to retaining the qualifier in Stage 13R2.

---

## 13. Attack L — Lean certification scope

### Attack

Check whether the project uses Lean compilation to imply that the whole Salop game and all Nash equilibria have been mechanically proved from primitives.

### Result

It does not. The formal record states that Lean certifies the long-arc algebra, exact `c=4` counterexample, profit-gap/global-inequality core, necessity signs, encoded condition-set multiplicity, cost-floor logical reduction, and welfare identities.

The analytic mapping from consumer geometry to the complete symmetric-foreclosed condition set remains C0–C1R. Asymmetric equilibria, mixed equilibria, the government stage, and the literature/publication claims remain outside Lean.

### Verdict

`PASS`.

---

## 14. C4R wording clarification controlling downstream work

C3R Section 9 contains the sentence:

> "An explicit no-below-cost price restriction collapses this multiplicity in member prices to the previously identified piecewise formula."

Read without the surrounding theorem scope, that sentence is too broad.

The controlling downstream version is:

> **Within symmetric, foreclosed, pure-strategy equilibria, an explicit no-below-cost price restriction collapses the unrestricted member-price multiplicity to the piecewise member-price formula.**

This clarification does not alter R4, Theorem F, `CostFloorCond`, any Python verifier, or any Lean theorem. It prevents later prose from accidentally turning a restricted-class characterization into a global uniqueness claim.

---

## 15. Publication-significance issues deliberately deferred to Stage 12R2

C4R is a scientific-validity gate, not a journal-fit gate. The following are not defects in the frozen mathematics but must be confronted next:

1. the cost-floor game is an explicit strategy modification, not a refinement derived from the published game;
2. the unrestricted original game has multiplicity, and welfare is continuation-selection dependent;
3. asymmetric and mixed equilibria remain uncharacterized;
4. the original policy ranking is recovered only under the stated common symmetric continuation, not for all possible continuations;
5. the paper must explain why this equilibrium-selection correction is worth publishing even though it does not solve the full government-stage selection problem.

These points may improve the correction's conceptual significance, but they may also create an editorial objection that the note stops at a restricted equilibrium class. Stage 12R2 must decide that question explicitly.

---

## 16. Final gate decision

No fatal or submission-blocking scientific defect remains inside the exact C3R frozen theorem scope.

The single C4R issue is a bounded contribution-wording clarification. It requires no mathematical refreeze and no rerun of C2R or C2R-L because no theorem statement, quantifier, strategy domain, equilibrium class, inequality, or formal object changes.

Accordingly:

`C4R = PASS`.

**Next stage: `Stage 12R2 — Journal Significance / Fit Recheck`.**

Stage 14 remains blocked until Stage 12R2, Stage 13R2, and Astra-2 are completed.