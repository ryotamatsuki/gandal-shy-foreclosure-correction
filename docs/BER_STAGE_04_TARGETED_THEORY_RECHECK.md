# BER Stage 04 — Targeted Dominance and Cost-Floor Theory Recheck

**Date:** 2026-10-01 JST  
**Branch:** `revision/ber-stage04-dominance-20261001`  
**Base:** `0e90c99b24b29bd30e19246d6f00b990cb66ad03`  
**Inputs:** `docs/BER_REVISION_PLAN.md`, `docs/BER_CHANGE_CONTROL.md`, `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`, `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`, `docs/C2R_L_LEAN_CERTIFICATION.md`, `GandalShy/Certification.lean`  
**Stage-04 verdict:** **GO TO STAGE 4A, WITH A BINDING SCOPE RESTRICTION**

## 1. Executive result

The proposed below-cost dominance lemma is correct, and the existing cost-floor game is exactly the game obtained by deleting all strictly below-marginal-cost price strategies. The deletion/restricted-game bridge is stronger than the September manuscript stated: under nonnegative demand and profit ((p_i-m_i)q_i), the Nash equilibria of the cost-floor game are exactly the unrestricted-game Nash equilibria whose posted prices satisfy the floor.

However, an outsider quote exactly at marginal cost is itself weakly dominated by any strictly above-cost quote. The same observation applies generically to a firm's at-cost quote. Therefore the cost-floor game is **not** the game obtained by deleting all weakly dominated strategies, is not an admissibility refinement, and does not justify perfection/properness language.

This matters especially for the lower branch. For (5/2<c<3), the cost-floor equilibrium ((c-1,c-1,c)) uses the outsider's at-cost quote (p_3=c). If that at-cost quote is also deleted, no U1 symmetric foreclosed equilibrium remains. This does not show that the unrestricted model lacks some other asymmetric, mixed, or non-foreclosed equilibrium; those objects remain outside the present theorem class.

The BER revision can therefore proceed only with the narrower interpretation:

> delete the **strictly below-cost** price family, not all weakly dominated strategies.

Stage 4A must independently attack that statement before manuscript integration.

---

## 2. Primitive payoff fact

In a member market, let firm (i) have marginal cost (m_i), posted price (p_i), and demand
[
q_i(p_i,p_{-i})ge 0.
]
The model payoff is
[
pi_i(p_i,p_{-i})=(p_i-m_i)q_i(p_i,p_{-i}).
]

For the affected union-member market:

- (m_1=m_2=0);
- (m_3=c);
- the market is fully covered but individual firm demand may be zero;
- only demand nonnegativity is needed for the dominance inequalities below.

No monotonicity of demand is needed for the weak-dominance comparison because the at-cost payoff is identically zero.

---

## 3. Claim BER-L1 — every strictly below-cost quote is weakly dominated by the cost quote

Fix a firm (i) and a proposed price (p_i<m_i). Compare it with the alternative strategy (p_i'=m_i).

For every admissible rival-price profile (p_{-i}),
[
pi_i(m_i,p_{-i})
=(m_i-m_i)q_i(m_i,p_{-i})
=0.
]
By nonnegative demand,
[
pi_i(p_i,p_{-i})
=(p_i-m_i)q_i(p_i,p_{-i})
le 0.
]
Hence
[
pi_i(m_i,p_{-i})ge pi_i(p_i,p_{-i})
qquad	ext{for every }p_{-i}.
]

The comparison is strict for at least one feasible rival profile. Choose rival prices sufficiently high that the firm charging (p_i) obtains positive-measure demand near its ideal location. Then
[
q_i(p_i,p_{-i})>0
]
and, because (p_i-m_i<0),
[
pi_i(p_i,p_{-i})<0=pi_i(m_i,p_{-i}).
]

Therefore every strictly below-cost pure price strategy is weakly dominated by the at-cost price.

### Outsider specialization

For firm 3,
[
p_3<c
quadLongrightarrowquad
p_3=c
	ext{ weakly dominates }p_3.
]

This is the precise result relevant to the editor's observation about the below-cost zero-sales outsider quotes supporting the unrestricted U1 multiplicity.

### What the proof does not say

It does not say:

- that (p_3=c) is undominated;
- that every weakly dominated strategy has now been removed;
- that iterated weak-dominance deletion produces a unique continuation;
- that the resulting equilibrium is trembling-hand perfect or proper.

---

## 4. Exact relation to the cost-floor game

Delete from every firm's pure strategy set all prices strictly below its own marginal cost:
[
p_i<m_i.
]
The surviving strategy set is exactly
[
p_ige m_i.
]

Thus this **partial weak-dominance deletion** produces the already-defined cost-floor game as a strategy-set object.

The important additional question is whether this deletion could create new Nash equilibria that were not Nash equilibria of the unrestricted game. In this model it cannot.

### Lemma — restricted equilibria lift back to the unrestricted game

Let (p^*) be a Nash equilibrium of the cost-floor game.

Because (p_i=m_i) is feasible in the restricted game and yields exactly zero profit for every rival-price profile, equilibrium optimality implies
[
pi_i(p^*)ge 0
qquad	ext{for every firm }i.
]

Now consider any deviation deleted by the cost floor, (p_i'<m_i). Nonnegative demand gives
[
pi_i(p_i',p_{-i}^*)le 0le pi_i(p^*).
]
Hence no deleted deviation is strictly profitable.

All deviations that satisfy (p_i'ge m_i) were already available in the cost-floor game and are unprofitable by restricted-game Nash optimality. Therefore (p^*) is also a Nash equilibrium of the unrestricted game.

### Converse

Any unrestricted-game Nash equilibrium that already satisfies
[
p_ige m_iquadorall i
]
remains a Nash equilibrium after the strategy sets are restricted, because restriction only removes deviations.

Therefore, for this price game,
[
NE(	ext{cost floor})
=
NE(	ext{unrestricted})cap
{p:p_ige m_i orall i}.
]

This bridge uses only:

1. nonnegative demand;
2. payoff ((p_i-m_i)q_i);
3. feasibility of the at-cost quote.

It is not a generic theorem about arbitrary deletion of weakly dominated strategies.

---

## 5. Mapping to the inherited U1/U2 characterization

Within the already-certified symmetric, foreclosed, pure-strategy class, the unrestricted condition set is:

### U1
[
rac32le s<2,qquad r=s+1,qquad cge s+1.
]

### U2
[
s=2,qquad rge3,qquad cge3.
]

Impose the outsider cost floor (rge c).

### U1 intersection

U1 gives
[
r=s+1le c.
]
The cost floor gives
[
rge c.
]
Hence
[
r=c=s+1,
]
so
[
s=c-1.
]
Together with (3/2le s<2), this yields
[
5/2le c<3.
]

### U2 intersection

U2 gives (s=2), (rge3), (cge3). The cost floor adds (rge c), so:
[
s=2,qquad cge3,qquad rge c.
]

Thus the inherited cost-floor characterization follows exactly from the partial deletion:

[
p_M(c)=
egin{cases}
c-1,& 5/2<c<3,\
2,& 3le c<5,
end{cases}
]
within the stated symmetric, foreclosed, pure-strategy class.

No additional symmetric foreclosed cost-floor equilibria are created by the deletion.

---

## 6. At-cost diagnostic — the mandatory limitation

Now test the outsider strategy (p_3=c).

Take any (delta>0) and compare the strategy
[
p_3'=c+delta.
]

For every rival-price profile,
[
pi_3(c,p_{-3})=0,
]
while
[
pi_3(c+delta,p_{-3})
=
delta,q_3(c+delta,p_{-3})
ge0.
]

There exist feasible rival prices high enough that
[
q_3(c+delta,p_{-3})>0,
]
so the inequality is strict for at least one rival profile.

Therefore:
[
p_3=c
]
is itself weakly dominated by every fixed strictly above-cost quote (c+delta).

The same argument applies to any firm's at-cost quote (p_i=m_i).

### Consequence

The cost-floor game retains weakly dominated strategies at its boundary. Therefore the following statements are false and must remain prohibited:

- “the cost-floor game is obtained by deleting all weakly dominated strategies”;
- “weak dominance selects (p_3=c)”;
- “the cost-floor equilibrium is admissible because the outsider charges marginal cost”;
- “the cost-floor result is a trembling-hand/perfect/proper refinement.”

The correct language is:

> the cost-floor game is obtained by deleting the **strictly below-cost** price family, each member of which is weakly dominated by the at-cost quote.

---

## 7. What happens if the at-cost outsider quote is also deleted?

For a diagnostic only, add the strict inequality
[
r>c
]
to the inherited unrestricted condition set.

### U1

U1 requires
[
r=s+1le c.
]
This is incompatible with (r>c). Therefore no U1 symmetric foreclosed equilibrium survives.

### U2

U2 permits
[
s=2,qquad cge3,qquad rge3.
]
Adding (r>c) gives the surviving set
[
s=2,qquad cge3,qquad r>c.
]

Hence:

- for (5/2<c<3), the lower cost-floor profile ((c-1,c-1,c)) does **not** survive deletion of the at-cost outsider strategy;
- at (c=3), the exact profile with (r=3) is deleted but profiles ((2,2,r)) with (r>3) survive;
- for (3<c<5), ((2,2,r)) with (r>c) survives.

This statement is only about the already-characterized symmetric foreclosed class. It is not a claim that no other pure, asymmetric, mixed, or non-foreclosed equilibrium exists when (5/2<c<3).

---

## 8. Boundary and regression checks retained

The Stage-04 logic is consistent with the required inherited checkpoints.

### (c=4)

1. Unrestricted equilibrium:
   [
   (3/2,3/2,5/2).
   ]
   The outsider support (5/2<4) is strictly below cost and is removed by the cost-floor deletion.

2. Published profile:
   [
   (3/2,3/2,4).
   ]
   The outsider quote is at cost, but the profile is not Nash because a member has the previously certified profitable deviation.

3. Cost-floor equilibrium:
   [
   (2,2,4).
   ]
   It is a Nash equilibrium of both the restricted and unrestricted games, but its outsider strategy (p_3=4) is weakly dominated by any fixed (p_3'>4). The same member price (2) is also supported by ((2,2,r)) for every (r>4).

### (c=3)

The F1/F2 member-price branches meet at (s=2). The at-cost outsider quote (r=3) is weakly dominated, but U2 equilibria with (r>3) remain.

### (c=5/2)

This is retained as a boundary consistency point. The BER headline proposition remains on the strict domain (5/2<c<5).

---

## 9. Stage-04 claim/proof map

| Object | Stage-04 status | Basis | Downstream requirement |
|---|---|---|---|
| BER-P0 published profile non-Nash | inherited | C0-C1R / C2R / Lean | regression only |
| BER-L1: (p_i<m_i) weakly dominated by (p_i=m_i) | **ANALYTIC GO** | payoff sign + nonnegative demand + strict-demand witness | independent Stage 4A attack; formal target |
| Partial deletion (p_i<m_i) gives cost-floor strategy sets | **ANALYTIC GO** | definition | independent Stage 4A attack |
| Restricted NE = feasible unrestricted NE | **ANALYTIC GO** | zero-profit at-cost deviation + sign of deleted deviations | independent Stage 4A attack; formal target |
| Existing F1/F2 cost-floor characterization | inherited + bridge verified | U1/U2 intersection | Stage 4A regression |
| At-cost outsider quote (p_3=c) weakly dominated | **ANALYTIC GO** | positive-margin alternative has nonnegative payoff everywhere | independent Stage 4A attack; formal target |
| Cost-floor = deletion of all weakly dominated strategies | **FALSE / PROHIBITED** | at-cost diagnostic | wording gate |
| Full admissibility / iterated deletion / perfection | **NOT ESTABLISHED** | outside scope | remain nonclaims |
| Strict-above-cost symmetric foreclosed set | **DERIVED DIAGNOSTIC** | UCond + (r>c) | independent Stage 4A check |
| Asymmetric / mixed / government-stage conclusions | **OPEN / OUT OF SCOPE** | not characterized | no inference |

---

## 10. Proposed symbolic, numerical and formal targets

Stage 4 does not alter production verification code or Lean. The following targets should be considered after the independent Stage-4A attack.

### Symbolic targets

1. Encode the sign identity:
   [
   (p-m)qle0
   quad	ext{for }p<m, qge0.
   ]
2. Encode the at-cost identity:
   [
   (m-m)q=0.
   ]
3. Encode above-cost nonnegativity:
   [
   (m+delta-m)q=delta qge0.
   ]
4. Reduce (	ext{UCond}land(c<r)) to the strict-above-cost U2 branch.

### Numerical targets

1. For representative below-cost outsider quotes, verify that replacing the quote by (c) never lowers profit across a broad opponent-price grid.
2. Verify strict witness profiles with positive demand.
3. Verify that ((c-1,c-1,c)) for (5/2<c<3) is excluded when the outsider strategy is constrained to (p_3>c).
4. Verify that ((2,2,r)) with (r>c) remains a symmetric foreclosed equilibrium for representative (cge3).
5. Preserve the three mandatory (c=4) regressions listed above.

### Lean targets

A later formal patch should, if Stage 4A agrees, add lemmas equivalent to:

- `belowCost_profit_nonpos`;
- `atCost_profit_zero`;
- `aboveCost_profit_nonneg`;
- `belowCost_weakDominance_core`;
- `restricted_ne_deleted_deviation_no_gain` at the algebraic payoff layer;
- `strictAboveCost_UCond_characterization`.

The full weak-dominance statement from primitive Salop demand would still require a model-level encoding or an explicit assumption (q_ige0). The existing Lean project should not be represented as having mechanically reconstructed the full strategy/demand correspondence.

---

## 11. Stage-4A independent attack requirements

Stage 4A must not simply restate the sign proof above. It should use a logically different route:

1. reconstruct demand/payoff directly from the primitive delivered-price rule and verify that quantities are nonnegative;
2. construct explicit rival-price profiles producing positive demand for the strict-witness part of both dominance statements;
3. independently derive the cost-floor equilibrium bridge from best-response inequalities rather than from UCond intersection alone;
4. numerically falsify the dominance and strict-above-cost diagnostics from primitive geometry;
5. attack the (c=3) equality case and (5/2<c<3) lower branch specifically;
6. confirm that no manuscript sentence implicitly upgrades partial deletion to full admissibility or perfection.

If any of these fail, return to Stage 4 and narrow the BER claim before manuscript editing.

---

## 12. Gate decision

**Stage 04: GO TO STAGE 4A.**

The new BER-L1 lemma and the partial-deletion/cost-floor bridge survive analytic recheck. The at-cost diagnostic is also resolved and imposes a binding limitation on interpretation.

The permitted contribution is therefore narrower but coherent:

> strictly below-cost zero-sales outsider quotes are weakly dominated and may be deleted to define the cost-floor subgame; within the certified symmetric foreclosed class, this partial deletion yields the existing piecewise member-price result. The boundary at-cost quote is itself weakly dominated, so the result is not a full weak-dominance refinement.

No manuscript, code, or Lean file is modified at Stage 4. Independent Stage 4A verification is mandatory before the result is integrated or refrozen.
