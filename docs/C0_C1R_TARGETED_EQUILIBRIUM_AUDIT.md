# C0–C1R Targeted Equilibrium-Set Reaudit

**Date:** 2026-09-09  
**Branch:** `c0-c1r/equilibrium-set-reaudit`  
**Base:** `main@40e4e76721534c39bfe3f13ad97cea1183732d48`  
**Recovery authority:** `docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`  
**Scope:** post-foreclosure pricing, equilibrium multiplicity, explicit cost-floor restriction, and equilibrium-selection-dependent welfare only.

## 1. Executive verdict

**C0–C1R verdict: `PASS TO C2R`.**

The Astra counterexample is valid and materially changes the theory freeze, but it does not eliminate the correction to Gandal and Shy (2001). The correct scientific organization is now:

1. the published Appendix-B profile `(3/2,3/2,c)` is not a Nash equilibrium under the published quadratic-transport specification;
2. the unrestricted original price game has a continuum of symmetric foreclosed pure-strategy equilibria because a zero-sales outsider may post a below-cost price without losing money;
3. after imposing the **explicit strategy restriction** `p_i >= marginal cost in that market`, the member price is uniquely characterized within symmetric foreclosed pure-strategy equilibria by the previously derived piecewise formula;
4. the original Proposition-3 member-country welfare ranking is not equilibrium-selection-free in the unrestricted game, but it survives under a common symmetric continuation price and, in particular, under the symmetric cost-floor continuation characterized here.

The prior C3 freeze is therefore **superseded as a scientific authority** and must not be restored without C2R, Lean certification, and C3R.

No claim is made here about all asymmetric or mixed equilibria. The exact theorem class is **symmetric, foreclosed, pure-strategy equilibria in one union-member market**.

---

## 2. Primary-source facts retained from the published article

Direct inspection of the published 2001 article establishes the relevant primitives and the object being corrected.

- Markets are segmented and firms may set different prices across countries (p. 367).
- Consumers have unit demand and quadratic shortest-distance transportation disutility (p. 368, equation (1)).
- Production cost is normalized to zero; a nonrecognized foreign firm incurs unit conversion cost `c` (pp. 368–369).
- The price stage follows government recognition choices (p. 369).
- For `5/2 < c < 5`, Appendix B states that the outsider is foreclosed and claims the prices of firms 1 and 2 are `3/2`; the appendix describes the resulting Bertrand–Nash equilibrium as unique (pp. 381–382).
- Appendix B uses the same price-difference coefficient on the length-two arc as on the length-one arc, which is inconsistent with the quadratic transportation primitive.
- Country welfare includes the domestic firm's aggregate worldwide profit (p. 371, equation (11)).

The publication does not state a price-strategy restriction of the form `p_i >= marginal cost`. Therefore such a restriction, when used below, is an explicit modification of the strategy set and is not attributed to the published model.

---

## 3. Model object for the reopened audit

Consider one member country after formation of a two-country standardization union.

- Firms 1 and 2 are union-member firms and have marginal cost `0` in the member market.
- Firm 3 is the outsider and has marginal conversion cost `c` in this market.
- Firms are at locations `0,1,2` on a Salop circle of circumference `3`.
- Consumer density is `1`, and transportation disutility is squared shortest-arc distance.
- The market is fully covered.

Write the price profile as `(p_1,p_2,p_3)`.

A **symmetric foreclosed pure-strategy profile** is a profile

`(p_1,p_2,p_3)=(s,s,r)`

under which firm 3 has zero demand (up to a zero-measure tie).

The theorem class in C0–C1R is deliberately limited to these profiles. This is sufficient to repair the current manuscript's quantifiers and to establish the conditional piecewise result. Asymmetric and mixed equilibria remain outside the characterization unless a later stage broadens the theorem.

---

## 4. Published long-arc calculation and direct counterexample

### 4.1 Correct long-arc boundary

After foreclosure, firms 1 and 2 compete across a length-one arc and a length-two arc. On the length-two arc, if `x` is measured from firm 1 toward firm 2, the quadratic indifference condition is

`p_1 + x^2 = p_2 + (2-x)^2`.

Expansion gives

`4x = 4 + p_2 - p_1`,

so

`x^L = 1 + (p_2-p_1)/4`.

The price-difference coefficient is therefore `1/4`, not `1/2`.

On the short arc,

`x^S = 1/2 + (p_2-p_1)/2`.

Hence, on the regular two-active-firm branch,

`q_1 = 3/2 + (3/4)(p_2-p_1)`.

### 4.2 Published complete profile is not Nash

At `c=4`, the published Appendix-B profile is

`(p_1,p_2,p_3)=(3/2,3/2,4)`.

Firm 3 is far enough above the members that the member deviation below remains on the two-active-firm branch. Firm 1's candidate profit is

`(3/2)(3/2)=9/4`.

If firm 1 raises its price to `7/4`, its demand is

`3/2 + (3/4)(3/2-7/4) = 21/16`,

and profit becomes

`(7/4)(21/16)=147/64`.

Therefore

`147/64 - 9/4 = 3/64 > 0`.

Thus the **complete published profile** `(3/2,3/2,c)` is not a Nash equilibrium at `c=4`. This is the canonical direct counterexample to the published Appendix-B equilibrium claim.

This does **not** imply that member price `3/2` can never occur in another equilibrium with a different zero-sales outsider price.

---

## 5. Unrestricted original price game

### 5.1 Foreclosure and the outsider's best response

Take a symmetric candidate `(s,s,r)`.

At the outsider's ideal location, each member product has delivered price `s+1`. The maximum price at which the outsider can obtain positive-measure demand is therefore `s+1`.

Hence zero outsider demand requires

`r >= s+1`.

For zero demand to be a best response for firm 3, it is also necessary that

`c >= s+1`.

If `c < s+1`, the outsider can choose a price strictly between `c` and `s+1`, obtain positive demand in a neighborhood of its ideal point, and earn strictly positive profit.

Conversely, if `c >= s+1`, every price that gives the outsider positive-measure demand is below marginal cost, while any zero-demand quote gives profit zero. Thus any zero-demand quote is a best response.

### 5.2 Member profit when the outsider quote is exactly `s+1`

Fix `p_2=s` and `p_3=s+1` and let firm 1 deviate to `p`.

For `s-1 < p <= s`, the outsider remains foreclosed and both member boundaries are on the regular two-member branch:

`q_1(p)=3/2 + (3/4)(s-p)`.

Therefore

`pi_1(p)=p[3/2+(3/4)(s-p)]`,

with derivative

`d pi_1/dp = 3/2 + 3s/4 - 3p/2`.

For `p>s`, the outsider becomes relevant on the long side. Direct delivered-price comparison against firms 2 and 3 yields

`q_1(p)=max{s+3/2-p,0}`.

Thus, on the positive-demand part,

`pi_1(p)=p(s+3/2-p)`.

Its right derivative at the candidate price is

`(d pi_1/dp)|_{s+}=3/2-s`.

For large downward deviations `0 <= p <= s-1`, demand is at most the total market size `3`, so

`pi_1(p) <= 3(s-1)`.

Candidate profit is `3s/2`; the gap is

`3s/2 - 3(s-1) = 3 - 3s/2`,

which is nonnegative whenever `s<=2`.

Negative prices cannot improve profit because demand is nonnegative and member marginal cost is zero.

### 5.3 Complete characterization within symmetric foreclosed pure strategies

**Theorem U — Unrestricted symmetric foreclosed equilibrium set.**  
Within symmetric foreclosed pure-strategy profiles `(s,s,r)`, the unrestricted original price game has a Nash equilibrium if and only if one of the following holds:

**U1. Lower-price family**

- `3/2 <= s < 2`,
- `r=s+1`,
- `c >= s+1`.

**U2. Duopoly-price family**

- `s=2`,
- `r>=3`,
- `c>=3`.

Equivalently, for `c>=5/2`, the admissible member price satisfies

`3/2 <= s <= min{2,c-1}`,

with the additional outsider-price condition that `r=s+1` whenever `s<2`, while at `s=2` any `r>=3` is admissible.

For the paper's strict foreclosure range `5/2<c<5`, this gives a nondegenerate continuum of symmetric foreclosed equilibria.

#### Sufficiency: U1

Take `3/2<=s<2`, `r=s+1`, and `c>=s+1`.

- Outsider: any deviation that obtains positive demand must set price below `s+1<=c`, yielding nonpositive margin; zero demand yields zero profit.
- Member, `p<0`: profit is nonpositive.
- Member, `0<=p<=s-1`: profit is at most `3(s-1)<=3s/2`.
- Member, `s-1<p<=s`: the regular-branch profit above is increasing up to `s` because its derivative is at least `3/2-3s/4>0`.
- Member, `p>s`: profit is `p(s+3/2-p)` while demand is positive; because its unconstrained maximizer `(s+3/2)/2` is weakly below `s` when `s>=3/2`, profit cannot increase after crossing `s`. For still larger prices demand is zero.

Thus no firm has a profitable deviation.

#### Sufficiency: U2

Take `s=2`, `r>=3`, `c>=3`.

The outsider has no profitable positive-demand deviation because positive demand requires a price below `3<=c`.

For a member, remove the outsider. This can only weakly increase the deviator's demand and therefore gives an upper envelope for its profit at every nonnegative price. Against the other member's price `2`, the two-member profit has global maximum `3` at price `2`:

- for `p<=1`, profit is at most `3p<=3`;
- for `1<=p<=3`, profit is `p(3-3p/4)`, uniquely maximized at `p=2` with value `3`;
- for `3<=p<=4`, demand is weakly below `3/4`, so profit is at most `3`;
- for `p>=4`, demand is zero;
- negative prices yield nonpositive profit.

Adding the outsider cannot create a profitable deviation. Hence `(2,2,r)` is a Nash equilibrium for every `r>=3` when `c>=3`.

#### Necessity

Let `(s,s,r)` be a symmetric foreclosed Nash equilibrium.

1. Foreclosure implies `r>=s+1`.
2. Outsider optimality implies `c>=s+1`; otherwise it can profitably price strictly between `c` and `s+1`.
3. `s>2` is impossible: a sufficiently small downward member deviation remains in the foreclosed regular branch, and the derivative at `p=s` is `(3/4)(2-s)<0`, so a price decrease raises profit.
4. If `s<2` and `r>s+1`, a sufficiently small upward member deviation leaves the outsider foreclosed and has derivative `(3/4)(2-s)>0`; hence it is profitable. Therefore `r=s+1` whenever `s<2`.
5. Given `s<2` and `r=s+1`, `s<3/2` is impossible because the right derivative after outsider demand becomes relevant is `3/2-s>0`.
6. If `s=2`, foreclosure requires `r>=3`, and outsider optimality requires `c>=3`.

These conditions are exactly U1 and U2.

### 5.4 Boundary cases

- `c=5/2`: the symmetric foreclosed set collapses to `(s,r)=(3/2,5/2)` within U1. This is also the zero-share boundary of the three-active-firm solution.
- `c=3`: U1 gives all `3/2<=s<2` with `r=s+1`; U2 additionally gives `s=2` with any `r>=3`.
- `c>3`: member price remains nonunique in the unrestricted game; prices below `2` are supported by below-cost zero-sales outsider quotes `r=s+1<c`, while `s=2` can be supported by any `r>=3`.

The multiplicity is therefore not confined to an arbitrary outsider quote while holding the member price fixed. The outsider quote can change the members' global best-response problem and support different member prices.

---

## 6. Explicit cost-floor price game

### 6.1 Definition

Define a separate restricted price game in which each firm's strategy in the member market must satisfy

`p_i >= mc_i`.

Thus

- `p_1>=0`,
- `p_2>=0`,
- `p_3>=c`.

This is an **explicit strategy-space restriction**. It is not asserted to be without loss of generality, an implication of Nash equilibrium, or a condition stated in Gandal and Shy (2001).

### 6.2 Characterization

**Theorem F — Cost-floor symmetric foreclosed equilibrium set.**  
Within symmetric foreclosed pure-strategy equilibria of the cost-floor game:

**F1. For `5/2 <= c < 3`:**

`(p_1,p_2,p_3)=(c-1,c-1,c)`.

The full symmetric foreclosed price profile is unique in this class.

**F2. For `c>=3`:**

`p_1=p_2=2`,

while the outsider may choose any

`p_3>=c`.

Thus the **member price is unique** within the stated class, while the zero-sales outsider price remains nonunique.

Restricting to the paper's domain `5/2<c<5`, the member-price characterization is

`p_M(c)=c-1` for `5/2<c<3`,

`p_M(c)=2` for `3<=c<5`.

#### Proof from Theorem U

The cost-floor symmetric foreclosed equilibria are the elements of Theorem U that also satisfy `r>=c`.

If `s<2`, Theorem U requires `r=s+1` and `c>=s+1`. The cost floor requires `r>=c`. Hence

`r=s+1=c`,

so `s=c-1`. The condition `s<2` gives `c<3`, and `s>=3/2` gives `c>=5/2`.

If `s=2`, Theorem U requires `c>=3` and `r>=3`; the cost floor strengthens this to `r>=c`. Hence the member price is `2` and the outsider price is any `r>=c`.

This proves both necessity and sufficiency within the exact theorem class.

### 6.3 Meaning of the `c=3` boundary

At `c=3`, the two member-price branches meet at `p_M=2`. The cost-based foreclosure condition `p_M+1<=c` holds with equality. Therefore the manuscript must not describe the constraint as strictly slack at `c=3`; strict slack begins only at `c>3`.

---

## 7. Welfare and equilibrium selection

### 7.1 Common symmetric continuation price

Let both union markets select the same symmetric foreclosed member price `s`.

In either member market, each active member firm sells `3/2`, and total transportation cost is `3/4`. Hence member-country consumer surplus is

`CS_M^SU = 3V - 3s - 3/4`.

The domestic member firm earns `3s` across the two union markets and, under the recognition behavior used in the original Proposition-3 proof, one additional unit of profit in the nonmember market. Thus

`Pi_M^SU = 3s + 1`.

Therefore

`TS_M^SU = 3V + 1/4`.

Under mutual recognition,

`TS^MR = 3V - 1/4`,

so

`TS_M^SU - TS^MR = 1/2`.

Thus the original ranking survives for a **common symmetric foreclosed continuation price**.

### 7.2 Different continuation prices across the two segmented union markets

Because the published model permits country-specific prices, let market A select symmetric member price `s_A` and market B select symmetric member price `s_B`.

Country A's consumer surplus is

`CS_A^SU = 3V - 3s_A - 3/4`.

Firm A's worldwide profit is

`Pi_A^SU = (3/2)s_A + (3/2)s_B + 1`.

Hence

`TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`.

Relative to mutual recognition,

`TS_A^SU - TS^MR = 1/2 + (3/2)(s_B-s_A)`.

Therefore the Proposition-3 ranking is **not selection-free across all unrestricted symmetric continuation equilibria**. The prior statement that the price terms always cancel for each member country was too broad; cancellation for a given member requires the same member price in the two union markets.

This observation does not by itself establish a different government-stage equilibrium or a reversal of the original policy conclusion. Such a claim would require an explicit continuation-equilibrium selection rule and a re-solution of the government stage.

### 7.3 Cost-floor continuation

In the cost-floor game, Theorem F uniquely determines the member price within symmetric foreclosed pure-strategy equilibria as a function of the common conversion cost `c`. Since the two union markets are structurally identical and have the same `c`, the symmetric member price is the same in both markets:

`p_M=c-1` for `5/2<c<3`,

`p_M=2` for `3<=c<5`.

Within this explicitly restricted continuation class, the original Proposition-3 member-country welfare ranking is recovered:

`TS_M^SU - TS^MR = 1/2 > 0`.

---

## 8. Theorem-ready claims for the revised paper

The following claims are cleared at the analytic C0–C1R level and should be the inputs to C2R. They are **not yet C3R-frozen**.

### Claim R1 — Published-profile correction

Under the published quadratic transportation technology, Appendix B's complete profile `(3/2,3/2,c)` is not generally a Nash equilibrium for `5/2<c<5`; `c=4` and the deviation `7/4` provide an exact counterexample.

### Claim R2 — Unrestricted multiplicity

The unrestricted original price game admits the symmetric foreclosed equilibrium set in Theorem U. In particular, the same member price `3/2` can be supported by outsider price `5/2` whenever `c>=5/2`, even though the published profile with outsider price `c` need not be an equilibrium.

### Claim R3 — Conditional piecewise characterization

After explicitly imposing `p_i>=mc_i`, the member price within symmetric foreclosed pure-strategy equilibria is uniquely determined by

`p_M=c-1` for `5/2<c<3`,

`p_M=2` for `3<=c<5`.

The outsider price remains nonunique for `c>=3`, where any `p_3>=c` supports zero sales.

### Claim R4 — Conditional welfare robustness

The Proposition-3 member-country ranking survives under a common symmetric foreclosed continuation price and therefore under the symmetric cost-floor continuation characterized in Claim R3. It is not a selection-free statement over arbitrary combinations of unrestricted market-specific continuation equilibria.

---

## 9. Claims prohibited after C0–C1R

Until a later stage proves something stronger, the revised project must not state:

- that member price `3/2` is never an equilibrium price after foreclosure;
- that the unrestricted game has a unique post-foreclosure equilibrium;
- that the old piecewise member-price formula characterizes the unrestricted game;
- that nonuniqueness concerns only the outsider price;
- that the cost-floor restriction is WLOG or follows from elimination of weakly dominated strategies;
- that Gandal and Shy (2001) imposed `p_i>=mc_i`;
- that Proposition 3 is robust to every continuation-equilibrium selection in the unrestricted game;
- that the original policy conclusion reverses without re-solving the relevant government-stage game;
- that all asymmetric or mixed equilibria have been characterized.

---

## 10. Boundary and scope certificate

| Item | C0–C1R status |
|---|---|
| Published quadratic primitive | confirmed |
| Long-arc coefficient `1/4` | analytically proved |
| Foreclosure threshold `c=5/2` from three-firm interior share | unchanged; historical derivation retained |
| Published profile counterexample | exact analytic counterexample proved |
| Unrestricted symmetric foreclosed equilibrium existence | proved |
| Unrestricted symmetric foreclosed equilibrium necessity | proved within stated class |
| Cost-floor member-price existence | proved |
| Cost-floor member-price necessity | proved within stated class |
| `c=5/2` boundary | characterized |
| `c=3` boundary | characterized; equality, not strict slack |
| Common-price welfare identity | proved analytically |
| Cross-market selection term | proved analytically |
| All asymmetric pure equilibria | **not characterized; outside theorem class** |
| Mixed equilibria | **not characterized; outside theorem class** |
| Government-stage equilibrium under unrestricted multiplicity | **not re-solved; no claim made** |
| Numerical falsification of revised theorem set | deferred to C2R |
| Lean certification | deferred to C2R-L |

---

## 11. C2R contract

C2R must treat the analytic results above as targets to falsify, not as assumptions to reproduce mechanically.

Required numerical/symbolic work:

1. replace the old verifier's fixed outsider price `p_3=c` with a three-price evaluator;
2. test Theorem U across `c`, `s`, and `r`, including below-cost zero-sales outsider quotes;
3. test necessity by deliberately perturbing each excluded condition (`s<3/2`, `s>2`, `r>s+1` with `s<2`, and `c<s+1`);
4. implement cost-floor ON/OFF modes and verify Theorem F;
5. search asymmetric member-price profiles for counterexamples to any accidentally overbroad implementation or prose claim, without treating absence of a numerical counterexample as a proof of symmetry;
6. retain `c=4: (3/2,3/2,4)` as a permanent failing regression case and `(3/2,3/2,5/2)` as the corresponding unrestricted equilibrium regression case;
7. test `c=5/2`, `c=3`, and values immediately on both sides;
8. verify the common-price and cross-market welfare identities symbolically and numerically.

If C2R discovers any counterexample inside the exact theorem classes of Theorem U or Theorem F, return to C0–C1R before Lean formalization.

---

## 12. Final C0–C1R gate

The four recovery questions are now answered in theorem-ready form:

1. **What equilibria exist in the unrestricted original game within the stated class?**  
   Theorem U gives the complete symmetric foreclosed pure-strategy set.

2. **What is and is not unique?**  
   Member prices are nonunique in the unrestricted game; at `s=2` the outsider price is also nonunique. No claim is made over asymmetric or mixed equilibria.

3. **Under what extra condition is the piecewise member price characterized?**  
   Under the explicit cost-floor strategy restriction `p_i>=mc_i`, Theorem F uniquely determines the member price within symmetric foreclosed pure strategies; the outsider price remains nonunique for `c>=3`.

4. **Under what continuation selection does the welfare ranking survive?**  
   It survives under a common symmetric foreclosed member price and, in particular, under the symmetric cost-floor continuation. It is not selection-free under arbitrary market-by-market unrestricted continuation selection.

**Verdict: `C0–C1R PASS — PROCEED TO C2R`.**

This is an analytic-stage pass only. C3R freeze remains prohibited until C2R and C2R-L both pass.