# C3R — Revised Canonical Theory Freeze

**Date:** 2026-09-09  
**Branch:** `c3r/revised-canonical-theory-freeze`  
**Base:** `main@19630342fec2fc0a4b0ba4e900d3d8358581f74c`  
**Recovery authority:** `docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`  
**Scientific inputs:** `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`, `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`, `docs/C2R_L_LEAN_CERTIFICATION.md`  
**Formal source:** `GandalShy/Certification.lean`

## 1. Executive freeze verdict

**C3R verdict: `PASS — REVISED THEORY FROZEN; PROCEED TO C4R HOSTILE SCIENTIFIC SELF-AUDIT`.**

This document is now the controlling scientific specification for the revision. It supersedes the historical `docs/C3_CANONICAL_FREEZE.md`, which remains provenance only.

The freeze deliberately separates:

1. the unrestricted price game stated by Gandal and Shy (2001);
2. a separate cost-floor price game with the explicit strategy restriction `p_i >= marginal cost in that market`;
3. common versus market-specific continuation-equilibrium selection for welfare.

No downstream manuscript, abstract, cover letter, journal-positioning document, or submission package may state a stronger result than the claims frozen here unless the affected scientific stages are reopened.

---

## 2. Paper identity and scientific scope

### 2.1 Paper type

Correction / short theory note.

### 2.2 Provisional journal target

*International Economics*, short-format route, **not frozen as a final target**. Journal significance and fit must be re-evaluated at Stage 12R2 after C4R.

### 2.3 Title status

The pre-Astra title

> *Standardization Unions, Foreclosure, and Limit Pricing: Revisiting Gandal and Shy (2001)*

is retained only as a working baseline. C3R does **not** freeze the title. Stage 12R2/13R2 may retitle the paper to reflect multiplicity and equilibrium selection more accurately.

### 2.4 Canonical research question

> Under the published quadratic-transport specification of Gandal and Shy (2001), what is wrong with the claimed post-foreclosure price profile, what symmetric foreclosed pure-strategy equilibria actually arise in the unrestricted price game, how does an explicit no-below-cost strategy restriction alter that equilibrium set, and under which continuation selections does the original member-country welfare comparison remain valid?

### 2.5 Main parameter domain for the paper

The main correction concerns the strict post-foreclosure range

`5/2 < c < 5`.

The boundary values `c=5/2` and `c=3` are retained as explicit consistency checks. Results that analytically extend beyond the manuscript's strict domain may be recorded in proofs or notes, but the paper must not broaden its economic claim merely because an algebraic lemma permits a wider domain.

### 2.6 Exact equilibrium class currently characterized

The equilibrium characterization is limited to:

> **symmetric, foreclosed, pure-strategy price equilibria in one union-member market.**

A symmetric foreclosed profile is written `(s,s,r)`, where firms 1 and 2 are the union-member firms, firm 3 is the outsider, and firm 3 has zero demand up to a zero-measure tie.

C3R does not characterize all asymmetric pure equilibria, mixed equilibria, or the government-stage equilibrium under unrestricted continuation multiplicity.

---

## 3. Canonical primitives retained from the published model

For the affected member market:

- firms are at locations `0,1,2` on a Salop circle of circumference `3`;
- consumer density is `1` and the market is fully covered;
- transportation disutility is the square of shortest-arc distance;
- member firms have marginal production cost `0` in the member market;
- the outsider has marginal conversion cost `c` in that market;
- markets are segmented and country-specific prices are allowed;
- country welfare includes the domestic firm's worldwide profit.

The published model does **not** state a general price-strategy restriction `p_i >= marginal cost`. Any such restriction below defines a separate modified price game.

---

## 4. Frozen Result R1 — Correct long-arc calculation

On the length-two arc, the correct indifference condition is

`p_1 + x^2 = p_2 + (2-x)^2`,

which implies

`x^L = 1 + (p_2-p_1)/4`.

The price-difference coefficient is therefore `1/4`, not the `1/2` coefficient used in Appendix B of the published article.

On the short arc,

`x^S = 1/2 + (p_2-p_1)/2`.

When only the two member firms are relevant at both boundaries, firm 1's demand is

`q_1 = 3/2 + (3/4)(p_2-p_1)`.

### Certification status

- Analytic: C0–C1R.
- Symbolic/numerical regression: C2R.
- Lean: `long_arc_boundary` formally certifies the long-arc coefficient `1/4`.

### Prohibited strengthening

Do not state that this local demand formula applies for every arbitrary price vector without checking the relevant demand-region conditions.

---

## 5. Frozen Result R2 — The complete published post-foreclosure profile is not Nash

For every strict `c>5/2` in the paper's post-foreclosure range, the Appendix-B profile

`(p_1,p_2,p_3)=(3/2,3/2,c)`

is not a Nash equilibrium of the published quadratic-transport price game.

The canonical exact checkpoint is `c=4`:

- candidate member profit: `9/4`;
- deviation: `p_1=7/4`;
- deviating profit: `147/64`;
- gain: `3/64>0`.

The correction is therefore to the **complete published price profile and the associated uniqueness/equilibrium claim**.

### Required wording discipline

Permitted:

> Appendix B's claimed profile `(3/2,3/2,c)` is not a Nash equilibrium under the published quadratic-transport specification for the strict post-foreclosure range.

Not permitted:

> Member price `3/2` cannot occur in equilibrium.

The second statement is false in the unrestricted game because another outsider quote can support that member price.

### Certification status

- Analytic: Theorem-U necessity in C0–C1R plus the direct deviation argument.
- Numerical: the published `c=4` profile is a mandatory rejection regression in C2R.
- Lean: `published_profile_c4_base`, `published_profile_c4_deviation`, `published_profile_c4_profitable`, and `published_profile_c4_gain` certify the exact rational checkpoint at `c=4`.

Lean does not by itself certify the full `for every c>5/2` statement from consumer primitives; that quantified economic statement rests on C0–C1R's analytic equilibrium characterization.

---

## 6. Frozen Result R3 — Unrestricted original-game equilibrium multiplicity

### 6.1 Strategy space

Use the unrestricted price strategy space of the published model. In particular, a zero-sales outsider quote below its marginal cost is not excluded merely because it is below cost.

### 6.2 Exact characterization in the frozen class

Within symmetric foreclosed pure-strategy profiles `(s,s,r)`, the unrestricted original price game has a Nash equilibrium **if and only if** one of the following holds.

**U1 — lower-price family**

- `3/2 <= s < 2`;
- `r=s+1`;
- `c>=s+1`.

**U2 — duopoly-price family**

- `s=2`;
- `r>=3`;
- `c>=3`.

For the paper's strict range `5/2<c<5`, the admissible symmetric foreclosed member prices therefore satisfy

`3/2 <= s <= min{2,c-1}`,

with `r=s+1` whenever `s<2`, and with any `r>=3` when `s=2`.

Thus the unrestricted game has genuine **member-price multiplicity**, not merely outsider-price nonuniqueness.

### 6.3 Economic mechanism frozen for exposition

For `s<2`, the outsider's zero-sales quote must sit at `r=s+1`; that quote changes the member firms' global upward-deviation problem. If `c>s+1`, the supporting outsider quote is below its own marginal cost but still yields zero profit because it attracts no demand.

This is precisely why the pre-Astra manuscript's strategy of fixing `p_3=c` could establish useful candidate equilibria but could not characterize the unrestricted equilibrium set.

### Certification status

- Analytic necessity and sufficiency: Theorem U in C0–C1R.
- Numerical falsification/regression: C2R varies all three prices and preserves the Astra profile as a mandatory unrestricted-equilibrium test.
- Lean: `UCond` encodes the analytic condition set; `ucond_member_price_multiplicity` certifies multiplicity of that condition set; the profit-gap, no-gain, partition, and necessity-sign lemmas certify the proof-critical inequality core.

### Lean limitation

Do not state that Lean independently derived the equivalence between `UCond` and the full Salop Nash-equilibrium correspondence from consumer primitives. That equivalence is the analytic C0–C1R theorem.

---

## 7. Frozen Result R4 — Explicit cost-floor game

### 7.1 Definition

Define a separate price game by imposing in each market

`p_i >= marginal cost in that market`.

For the union-member market this means

- `p_1>=0`;
- `p_2>=0`;
- `p_3>=c`.

This is an **explicit strategy-space restriction**. It is not:

- without loss of generality;
- an implication of Nash equilibrium;
- generic deletion of weakly dominated strategies;
- a condition stated by Gandal and Shy (2001).

### 7.2 Exact characterization in the frozen class

Within symmetric foreclosed pure-strategy equilibria of the cost-floor game:

**F1 — `5/2 <= c < 3`**

`(p_1,p_2,p_3)=(c-1,c-1,c)`.

The complete symmetric foreclosed price profile is unique within this class.

**F2 — `c>=3`**

`p_1=p_2=2`,

and the outsider may choose any

`p_3>=c`.

Thus the **member price** is unique within the stated class, while the outsider quote remains nonunique.

Restricting the statement to the paper's strict range `5/2<c<5`,

`p_M(c)=c-1` for `5/2<c<3`,

`p_M(c)=2` for `3<=c<5`.

At `c=3`, the two member-price branches meet at `2`; the exclusion constraint holds with equality. Strict slack begins only for `c>3`.

### 7.3 Limit-pricing terminology

The phrase **limit pricing** may be used only with an explicit qualifier. The safest frozen usage is the cost-floor lower branch `5/2<c<3`, where the outsider is excluded in equilibrium but its cost-based zero-demand constraint binds the members' price at `c-1`.

The term means static exclusion-maintenance pricing in this product-market game. It does not mean Milgrom–Roberts signaling, an entry-stage reputation model, or informational limit pricing.

Do not use `c=3` as a point at which the constraint is already strictly slack; it is the branch-connection boundary.

### Certification status

- Analytic: Theorem F in C0–C1R.
- Numerical: separate cost-floor mode in C2R.
- Lean: `CostFloorCond`, `costFloor_characterization`, `costFloor_member_price`, and `costFloor_c3_member_price` certify the exact logical reduction from the analytic unrestricted condition set plus the outsider cost floor.

---

## 8. Frozen Result R5 — Welfare and continuation selection

### 8.1 Common symmetric continuation

If the two segmented union-member markets select the same symmetric foreclosed member price `s`, then for each member country

`CS_M^SU = 3V - 3s - 3/4`,

`Pi_M^SU = 3s + 1`,

so

`TS_M^SU = 3V + 1/4`.

Under the mutual-recognition benchmark used in the original comparison,

`TS^MR = 3V - 1/4`.

Hence, under a common symmetric continuation price,

`TS_M^SU - TS^MR = 1/2`.

### 8.2 Market-specific continuation prices

If market A uses symmetric member price `s_A` and market B uses `s_B`, then country A's welfare is

`TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`.

Therefore the price-transfer cancellation is not invariant to arbitrary market-by-market equilibrium selection.

### 8.3 Exact policy conclusion permitted by the freeze

Permitted:

> The original member-country welfare comparison is preserved under a common symmetric continuation price. The explicit cost-floor game provides one transparent symmetric continuation class for which the same `1/2` gap obtains.

Permitted:

> In the unrestricted original price game, equilibrium multiplicity makes the welfare comparison continuation-selection dependent.

Not permitted:

> Proposition 3 is robust to all Nash equilibria of the original game.

Not permitted:

> Correcting the price game reverses Proposition 3.

The first stronger statement has not been established; the second would require solving the relevant government-stage equilibrium and selection problem.

### Certification status

- Analytic accounting and selection scope: C0–C1R.
- Symbolic/numerical checks: C2R.
- Lean: `common_price_welfare`, `common_price_welfare_gap`, `cross_market_welfare`, and `cross_market_equal_prices` certify the algebraic welfare identities.

---

## 9. Frozen contribution claim

The strongest contribution statement currently permitted is:

> The published quadratic-transport calculation misstates the long-arc price response and the resulting post-foreclosure price profile. Correcting the demand geometry shows that the claimed profile is not Nash and, more importantly, that the unrestricted price game does not possess the claimed unique symmetric foreclosed continuation: it has a continuum of such equilibria. An explicit no-below-cost price restriction collapses this multiplicity in member prices to the previously identified piecewise formula. The original member-country welfare comparison is preserved under common symmetric continuation prices but is not selection-free across arbitrary unrestricted continuations.

This is a correction-plus-equilibrium-selection contribution. It is stronger than a typo or isolated algebraic correction, but C3R does **not** freeze any claim that this contribution necessarily clears the publication threshold of *International Economics*. That is a Stage-12R2 question.

---

## 10. Frozen proposition architecture for the revised manuscript

The revised short paper should use at most two headline propositions unless C4R finds a scientific reason to restructure.

### Proposition 1 — Post-foreclosure pricing and multiplicity

The proposition may contain three parts:

1. under the published quadratic specification, the Appendix-B profile is not Nash for the strict post-foreclosure range;
2. the unrestricted original price game has the U1/U2 symmetric foreclosed pure-strategy equilibrium set and hence member-price multiplicity;
3. under the explicit cost-floor strategy restriction, the symmetric foreclosed member price is characterized by the F1/F2 piecewise formula.

The proposition must name the strategy space and equilibrium class. It may not say simply “the unique equilibrium price is ...”.

### Proposition 2 — Welfare under continuation selection

The proposition should state:

1. the common-symmetric-continuation welfare identity and `1/2` gap;
2. the cross-market transfer term under different symmetric continuation prices;
3. the resulting limitation: welfare robustness is conditional on continuation selection.

The paper need not elevate a welfare-ranking reversal example to a new main result and must not infer a government-stage policy reversal without solving that stage.

---

## 11. Evidence map

| Frozen object | Analytic C0–C1R | C2R falsification | Lean C2R-L | Status |
|---|---:|---:|---:|---|
| long-arc coefficient `1/4` | YES | YES | YES | frozen |
| published `c=4` profitable deviation | YES | YES | YES | frozen |
| published profile false for strict post-foreclosure range | YES | regression support | partial/core only | frozen, analytic quantifier |
| U1/U2 symmetric foreclosed characterization | YES, necessity+sufficiency | YES, no counterexample in tested domain | inequality/core + encoded condition set | frozen |
| unrestricted member-price multiplicity | YES | YES | YES conditional on UCond equivalence | frozen |
| cost-floor F1/F2 characterization | YES | YES | YES conditional on UCond equivalence | frozen |
| `c=3` branch connection | YES | YES | YES | frozen |
| common-price welfare identity | YES | YES | YES | frozen |
| cross-market welfare transfer term | YES | YES | YES | frozen |
| all asymmetric pure equilibria | NO | perturbations only | NO | not claimed |
| mixed equilibria | NO | NO | NO | not claimed |
| government-stage equilibrium under multiplicity | NO | NO | NO | not claimed |
| publication significance / prior art | separate audit | N/A | N/A | not frozen scientifically |

---

## 12. Prohibited claims and wording

Until a later scientific stage explicitly proves otherwise, the following are prohibited:

1. “The correct post-foreclosure Nash equilibrium of the original model is uniquely `(c-1,c-1,c)` / `(2,2,c)`.”
2. “The member price `3/2` is not an equilibrium price.”
3. “Only the outsider price is nonunique.”
4. “The cost-floor restriction is WLOG.”
5. “The cost-floor restriction follows from Nash equilibrium.”
6. “The cost-floor game is the game analyzed explicitly by Gandal and Shy (2001).”
7. “Weak dominance selects `p_3=c`.”
8. “All pure-strategy equilibria have been characterized.”
9. “All Nash equilibria have been characterized.”
10. “The corrected welfare comparison is selection-free in the unrestricted game.”
11. “Proposition 3 is false” or “the policy ranking reverses,” absent a government-stage analysis establishing that claim.
12. “The outsider's competitive constraint is strictly slack at `c=3`.”
13. “Lean formally derives the entire Salop game or complete Nash correspondence from consumer primitives.”
14. “Limit pricing here is informational/signaling limit pricing.”
15. “The correction invalidates the original paper as a whole.”
16. “All citing papers are affected.”
17. Any generic novelty claim that foreclosure, potential competition, or limit pricing is new to economics.

---

## 13. Claims explicitly left open

C3R leaves the following unresolved because they are unnecessary for the present narrow correction unless a later audit shows otherwise:

- complete asymmetric pure-equilibrium characterization;
- mixed equilibria;
- an equilibrium-selection refinement for the unrestricted game;
- government-stage equilibrium under unrestricted multiplicity;
- whether the cost-floor restriction is the uniquely preferred economic refinement;
- whether unrestricted multiplicity changes any equilibrium policy choice once the government stage is fully solved;
- full forward-citation dependence and complete prior-art audit;
- final journal choice and publication-significance threshold.

These are not hidden assumptions. They are explicit nonclaims.

---

## 14. Downstream manuscript architecture constraint

Stage 13R2 must revise the paper in this order:

1. Section 2 — published quadratic specification, long-arc error, and exact failure of the published complete profile;
2. Section 3 — unrestricted U1/U2 multiplicity first, then the separate cost-floor F1/F2 characterization;
3. Section 4 — welfare under common versus market-specific continuation selection;
4. only after Sections 2–4 are stable: Abstract, Introduction, Conclusion, title, keywords/JEL, highlights, cover letter, and other submission materials.

Multiplicity must appear in the main text, not be hidden in a footnote or appendix.

The cost-floor restriction must be visibly introduced as a separate game before its piecewise member-price result is stated.

---

## 15. Return rules from this freeze

- If C4R finds a new equilibrium counterexample inside the frozen U1/U2 or F1/F2 theorem class: return to C0–C1R, then rerun affected C2R and C2R-L results before refreezing.
- If C4R changes a theorem quantifier, strategy domain, equilibrium class, or material inequality: reopen the analytic stage and the affected Lean theorem before a new freeze.
- If C4R finds only wording drift beyond the valid mathematics: repair C3R wording without changing the theorem.
- If Stage 12R2 finds only a journal-fit/significance problem: do not reopen the mathematics.
- If Stage 13R2 introduces a scientific claim not authorized here: remove it or reopen the earliest affected scientific stage.

---

## 16. C3R gate decision

The revised theory is internally aligned across:

- C0–C1R analytic necessity and sufficiency;
- C2R three-price falsification/regression tests;
- C2R-L admission-free Lean certification of the proof-critical algebraic and quantified inequality core.

No new mathematical claim has been added at C3R. The stage only fixes the exact logical scope of already-established results.

Accordingly:

`C3R = PASS`.

**Next stage: `C4R — Hostile Scientific Self-Audit`.**

Stage 14 remains blocked.