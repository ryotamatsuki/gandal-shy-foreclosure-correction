# BER Stage 4A — Independent Primitive Attack

**Date:** 2026-10-01 JST  
**Branch:** `revision/ber-stage4a-independent-20261001`  
**Base:** `f8510e089a38483580851eafcd37ae62dfda4bea`  
**Prior gate:** `BER_STAGE_04_TARGETED_THEORY_RECHECK.md`  
**Independent verifier:** `code/ber_stage4a_independent_attack.py`  
**Verdict:** **PASS — PROCEED TO STAGE 6**

## 1. Independence design

Stage 4A does not import or call the production verifier `code/verify_numerical.py` and does not use its threshold-sorting best-response construction.

The independent path starts from the primitive consumer rule. On a Salop circle of circumference 3 with firms at 0, 1 and 2, each consumer compares

`posted price + squared shortest-arc distance`

for all three firms. Demand is reconstructed point-by-point from the minimum delivered price; exact ties are split equally. Unilateral deviations are then searched over a direct price grid.

The analytical attack also starts from the primitive geometry for the strict-witness requirement rather than from the U1/U2 condition set.

This is falsification and independent reconstruction evidence. It is not a new proof that all asymmetric or mixed equilibria have been characterized.

---

## 2. Primitive reconstruction

For firm `i` at location `z_i`, a consumer at `x` faces delivered price

`D_i(x)=p_i+d(x,z_i)^2`,

where `d` is shortest-arc distance. The consumer buys from a firm attaining the lowest delivered price.

Therefore the induced quantity satisfies

`q_i(p)>=0`

for every price profile.

The operating payoff is

`pi_i(p)=(p_i-m_i)q_i(p)`.

For the member-market application:

- member firms: `m_1=m_2=0`;
- outsider: `m_3=c`.

The Stage-4A code reconstructs `q_i` from these primitives on 6,001 midpoint consumers and does not feed the analytic U1/U2 formulas into the demand calculation.

---

## 3. Independent strict-witness construction

Weak dominance requires at least one rival profile at which the proposed dominating strategy is strictly better.

Fix any firm and any candidate own price `x`. At that firm's ideal location, each of the other two firms is one unit away. If both rivals quote a sufficiently high common price `H`, then at the ideal location:

- own delivered price is `x`;
- each rival's delivered price is `H+1`.

Choose, for example, `H>x+2`. The own product is then strictly preferred at the ideal location and, by continuity of delivered-price differences, on a positive-measure neighborhood. Hence the firm has strictly positive demand.

This directly supplies the strict witness needed below for both the below-cost and at-cost comparisons.

---

## 4. BER-L1 survives the independent attack

Take any outsider price `p_3<c`.

At the at-cost strategy `p_3=c`, operating profit is zero for every rival-price profile because the margin is zero.

At the below-cost strategy, any positive demand produces a negative margin and zero demand produces zero profit. Therefore the at-cost quote is never worse.

The primitive strict-witness construction above supplies rival prices for which the below-cost strategy obtains positive demand. At those rival prices the below-cost profit is strictly negative while the at-cost profit remains zero.

Thus:

> every strictly below-cost outsider pure price is weakly dominated by the at-cost quote.

The same argument applies to any firm with marginal cost `m_i`: every `p_i<m_i` is weakly dominated by `p_i=m_i`.

### Independent numerical falsification

The new verifier evaluates:

- `c in {2.55, 2.75, 3.0, 4.0, 4.9}`;
- four below-cost gaps `{0.1,0.5,1.0,2.0}`;
- a 17 by 17 rival-price grid from -1 to 7.

This gives **5,780** below-cost comparisons.

Result:

- minimum `profit(at cost)-profit(below cost) = 0`;
- no negative comparison occurred;
- **3,530** profiles gave a strict improvement.

Stage 4A therefore found no primitive-demand counterexample to BER-L1.

---

## 5. The at-cost limitation also survives independently

Take `delta>0` and compare the outsider strategies:

- `p_3=c`;
- `p_3=c+delta`.

At cost, profit is always zero.

Above cost, the margin is `delta>0`, so the profit is

`delta*q_3(c+delta,p_-3)>=0`

for every rival profile.

The primitive strict-witness construction supplies rival prices at which `q_3>0`, making the inequality strict.

Therefore:

> `p_3=c` is itself weakly dominated by every fixed `p_3=c+delta`, `delta>0`.

The independent verifier evaluates three positive deltas for each of the five cost values over the same 17 by 17 rival grid: **4,335** comparisons.

Result:

- minimum `profit(above cost)-profit(at cost) = 0`;
- no negative comparison occurred;
- **1,642** profiles gave a strict improvement.

This confirms the binding Stage-4 limitation: the cost-floor game cannot be described as the result of deleting all weakly dominated strategies.

---

## 6. Explicit strict witnesses

The primitive verifier also constructs high-rival-price profiles where the outsider serves the entire discretized market. Representative results are:

| c | below-cost quote | above-cost increment | below-cost profit | at-cost profit | above-cost profit |
|---:|---:|---:|---:|---:|---:|
| 2.75 | 2.25 | 0.25 | -1.500000 | 0 | 0.750000 |
| 4.00 | 2.50 | 0.50 | -4.500000 | 0 | 1.500000 |
| 4.00 | 3.50 | 0.25 | -1.500000 | 0 | 0.750000 |

In all three cases the relevant outsider demand is 3 on the numerical market.

These are witness examples only. The analytic strict-witness argument is continuous and does not depend on these three parameter choices.

---

## 7. Independent best-response bridge

Stage 4A rechecks the restricted/unrestricted equilibrium relation without first intersecting U1/U2.

Let `S_i` be the unrestricted price set and let

`S_i^F={p_i in S_i : p_i>=m_i}`.

Suppose `p*` is a Nash equilibrium of the game restricted to `S_i^F`.

Because the at-cost price `m_i` is feasible in the restricted game and always yields zero operating profit,

`pi_i(p*)>=0`

for every firm.

Now partition unrestricted deviations into two regions.

1. Surviving deviations `p_i'>=m_i`: these were already feasible in the restricted game and cannot improve on `p*`.
2. Deleted deviations `p_i'<m_i`: primitive demand is nonnegative, so their profit is weakly below zero and therefore weakly below `pi_i(p*)`.

No unrestricted deviation is profitable. Thus any restricted-game Nash equilibrium is also an unrestricted-game Nash equilibrium.

Conversely, restricting a game cannot create a profitable deviation for a profile that was already an unrestricted equilibrium and remains feasible.

Hence, in this model,

`NE(cost floor)=NE(unrestricted) intersect product_i S_i^F`.

This is a best-response partition argument. It is not a generic assertion that arbitrary deletion of weakly dominated strategies preserves the full equilibrium correspondence.

---

## 8. Strict-above-cost attack on the lower branch

The diagnostic question is what remains if the outsider's at-cost quote is also excluded, so `r>c`.

The new verifier attacks the natural lower-branch continuations by raising the outsider quote above cost while holding the former cost-floor member price `s=c-1`.

Representative direct-grid results:

| c | tested profile | maximum unilateral gain |
|---:|---|---:|
| 2.55 | (1.55,1.55,2.65) | 0.037723713 |
| 2.75 | (1.75,1.75,2.85) | 0.012185469 |
| 2.95 | (1.95,1.95,3.05) | 0.000962340 |

Every tested `5/2<c<3` profile with `r>c` is rejected by a profitable member deviation.

This is consistent with the analytic logic that, for `s<2`, an outsider quote strictly above `s+1` restores a profitable small upward member deviation.

Stage 4A does not infer from this finite grid that no asymmetric, mixed or non-foreclosed equilibrium exists.

---

## 9. c=3 and the upper branch

The independent brute-force engine tests strict-above-cost profiles on and above the transition:

| c | tested profile | maximum grid gain |
|---:|---|---:|
| 3.0 | (2,2,3.10) | 0.000482420 |
| 3.5 | (2,2,3.60) | 0.000482420 |
| 4.9 | (2,2,5.00) | 0.000482420 |

The common small residual is the expected consumer/price grid artifact and is below the predeclared Stage-4A survival tolerance `0.002`.

Thus the independent attack supports the distinction:

- the lower `c<3` branch requires the at-cost outsider support in the stated symmetric foreclosed class;
- at `c=3` and above, `s=2` can be supported with outsider prices strictly above cost.

This also confirms that `c=3` is the branch-connection boundary, not a point of strict exclusion slack in the original cost-floor profile.

---

## 10. Permanent c=4 regressions under the independent engine

Stage 4A reruns the three required `c=4` cases without the production verifier.

### Published profile

`(3/2,3/2,4)`

Maximum grid deviation gain:

`0.047287119`.

The profile is decisively rejected, consistent with the exact analytic gain `3/64=0.046875`.

### Astra unrestricted equilibrium

`(3/2,3/2,5/2)`

Maximum grid deviation gain:

approximately `2.7e-15`.

The unrestricted equilibrium survives.

### Cost-floor profile

`(2,2,4)`

Maximum grid deviation gain:

`0.000482420`.

The profile survives within the numerical tolerance, while the separate dominance test confirms that its outsider strategy `p_3=4` is weakly dominated by any fixed quote strictly above 4.

The two statements are compatible: weak dominance does not imply that the dominated strategy cannot appear in a Nash equilibrium.

---

## 11. Manuscript wording audit

The currently submitted manuscript does **not** overclaim full weak-dominance refinement, admissibility, perfection or properness.

In particular, current Section 3 already states that the cost floor is:

- an explicit modification of the strategy set;
- not a condition stated in Gandal and Shy (2001);
- not implied by Nash equilibrium;
- not a claim that below-cost prices can be removed without loss of generality.

The current Introduction says the restriction is "not derived here from weak dominance." That sentence is safe for the September submission but becomes **outdated** for the BER revision because Stage 4/4A have now established the narrower partial-deletion lemma.

Required later integration wording must distinguish:

- deletion of **strictly below-cost** strategies, which is supported;
- deletion of **all weakly dominated** strategies, which is not supported.

No manuscript file is changed at Stage 4A. Integration remains downstream of novelty, contribution-strength and theory-freeze gates.

---

## 12. Formal target map

Stage 4A identifies the following new proof-critical formal targets for later closure.

| Target | Purpose | Required assumptions / scope |
|---|---|---|
| `belowCost_profit_nonpos` | below-cost payoff sign | `p<m`, `q>=0` |
| `atCost_profit_zero` | exact zero payoff at cost | algebraic |
| `aboveCost_profit_nonneg` | nonnegative payoff above cost | `delta>=0`, `q>=0` |
| `belowCost_weakDominance_core` | pointwise weak comparison | demand nonnegativity; strict witness handled separately |
| `deleted_region_no_profitable_deviation` | lift restricted NE to unrestricted NE | candidate payoff nonnegative |
| `strictAboveCost_UCond_characterization` | record loss of U1 and survival of U2 under `r>c` | conditional on inherited UCond equivalence |

The present Lean project does not encode the complete primitive demand correspondence. Therefore a formal theorem advertised as full game-theoretic weak dominance would require either:

1. a primitive demand encoding; or
2. an explicit nonnegative-demand assumption at the algebraic layer plus a separately documented economic witness for strictness.

Stage 7.5A should choose the minimum formal scope needed for the final BER claim and close these obligations before the new theory freeze.

---

## 13. Scope after Stage 4A

Cleared for downstream consideration:

1. Strictly below-cost pure prices are weakly dominated by the at-cost price.
2. Deleting exactly the strictly below-cost family creates the cost-floor strategy sets.
3. In this model the restricted-game Nash equilibria are exactly the feasible unrestricted Nash equilibria.
4. Within the inherited symmetric, foreclosed, pure-strategy class, that partial deletion yields the F1/F2 piecewise member-price result.
5. The at-cost quote is itself weakly dominated by strictly above-cost quotes, so the cost-floor result is not a full weak-dominance refinement.
6. Under the strict-above-cost diagnostic, U1 disappears while U2 survives from `c=3` onward within the inherited class.

Still prohibited:

- all-weak-dominance selection;
- iterated weak-dominance uniqueness;
- admissibility;
- trembling-hand perfection;
- proper equilibrium;
- all-pure or all-Nash equilibrium characterization;
- government-stage policy conclusions from the refinement.

---

## 14. Gate decision

**STAGE 4A PASS — PROCEED TO STAGE 6.**

The Stage-4 dominance result, deletion bridge and at-cost limitation survived a logically independent primitive-demand reconstruction and brute-force deviation attack.

The surviving BER research proposition is deliberately narrow:

> The below-cost zero-sales support behind part of the unrestricted multiplicity is weakly dominated. Deleting exactly the strictly below-cost strategies yields the cost-floor subgame and its existing piecewise member-price result within the certified symmetric foreclosed class. But the at-cost boundary strategy is itself weakly dominated, so this is a partial strategy deletion rather than an equilibrium refinement based on eliminating all weakly dominated strategies.

The next required stage is Stage 6: re-kill the actual revised novelty and contribution after accounting for this narrower dominance interpretation.
