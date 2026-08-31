# RIO Referee and Desk-Reject Audit

Date: 2026-09-01

## RIO-specific tests

1. **Why publish a correction to a 2001 paper in 2026? — PASS**
   - The published candidate price profile fails Nash equilibrium over a nondegenerate interval, not at an isolated boundary.
   - The correction changes the strategic path from three-firm competition directly to a constant post-foreclosure price into three-firm competition -> binding-exclusion limit pricing -> unconstrained duopoly.

2. **Merely algebraic? — PASS**
   - The source of the problem is an equilibrium incentive constraint. A zero-sales outsider remains relevant because an incumbent price increase can restore outsider demand.

3. **Does the published profile actually fail Nash equilibrium? — PASS**
   - The global proof is retained. The exact `c=4` illustration gives a profitable member deviation from `3/2` to `7/4`, increasing profit from `9/4` to `147/64`, a gain of `3/64`.

4. **Is `p_M=c-1` globally optimal rather than a local kink? — PASS**
   - The proof partitions all downward, foreclosure-preserving, upward/re-entry, and outsider deviations.
   - Dense numerical falsification finds no counterexample beyond the pre-specified discretization allowance.

5. **Is “limit pricing” justified? — PASS**
   - In `5/2<c<3`, the member price is below the unconstrained duopoly price and equals the highest symmetric price consistent with continued outsider exclusion.
   - A higher price restores outsider demand.
   - The manuscript explicitly distinguishes this binding-exclusion mechanism from informational signaling models of classic limit pricing.

6. **Zero sales but positive competitive discipline? — PASS**
   - `q_3=0` in equilibrium while the outsider's re-entry constraint binds for `5/2<c<3`.

7. **Is the mechanism itself new? — PASS with restraint**
   - No general novelty is claimed for foreclosure, potential competition, or limit pricing.
   - The contribution is the correct characterization of this published benchmark and the missing equilibrium regime.

8. **If Proposition 3 survives, why does the correction matter? — PASS**
   - Pricing incentives and surplus distribution change; welfare robustness follows from a separate cancellation in the national-welfare accounting.

9. **Interest to IO readers outside standards? — PASS / MODERATE**
   - The zero-sales-versus-strategic-relevance distinction is an IO pricing issue.
   - The setting remains specialized, so editorial interest is not guaranteed.

10. **Should this be a two-page erratum? — PASS**
   - The correction requires reconstructing residual demand, establishing a piecewise global Nash equilibrium, interpreting the binding exclusion constraint, and re-establishing the welfare result.

11. **RIO short-note fit? — PASS**
   - RIO explicitly welcomes shorter notes and commentaries.

12. **Can the paper be compressed further? — WEAK PASS**
   - The manuscript is already concise. The global proof should not be compressed further because it is the main defense against the local-kink objection.

## 30–60 second editor simulation

From the title, abstract, first page, proposition statements, and conclusion, the intended editorial message is:

> A published post-foreclosure Nash equilibrium is incorrect over a nondegenerate interval. The corrected equilibrium contains a binding-exclusion limit-pricing regime in which the foreclosed rival sells zero but still constrains active-firm prices. The original welfare ranking nevertheless survives.

The manuscript no longer leads with international-trade relevance. Standards are the application; foreclosure and pricing incentives are the contribution.

## Residual desk-reject risk

**MODERATE.**

Primary risk: editorial narrowness and age of the benchmark.

Mitigation: RIO's explicit short-note/commentary policy, complete global-equilibrium proof, nondegenerate missing regime, and clear IO mechanism.

No additional model extension is recommended solely to reduce this risk.

## Gate

- Mathematical correctness: PASS
- Global equilibrium proof: PASS
- RIO scope fit: STRONG
- Industrial-organization relevance: STRONG
- Short-note fit: STRONG
- Correction-paper positioning: STRONG
- Limit-pricing interpretation: STRONG
- Welfare-robustness presentation: STRONG
- Contribution clarity: STRONG
- Desk-reject risk: MODERATE
