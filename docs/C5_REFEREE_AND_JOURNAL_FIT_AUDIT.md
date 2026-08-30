# C5 — Referee Attack, Compression, and Journal-Fit Audit

Date: 2026-08-30

Verdict: **GO TO C6**.

## Global equilibrium audit

The foreclosure boundary remains `c=5/2` because the three-active-firm outsider share is `q_3=1-2c/5`. Under quadratic transport, the two surviving firms have

- `x^S=1/2+(p_2-p_1)/2`,
- `x^L=1+(p_2-p_1)/4`,
- `q_1=3/2+(3/4)(p_2-p_1)` on the two-contested-arc range,

and unconstrained symmetric duopoly price 2.

### Region II: 5/2 < c < 3

At `(p_1,p_2,p_3)=(c-1,c-1,c)`, member profit is `(3/2)(c-1)`. A global unilateral-deviation partition closes the local-kink objection:

1. If `p_1<=c-2`, demand is at most 3, so profit is at most `3(c-2)`. The candidate exceeds this bound by `(3/2)(3-c)>0`.
2. If `c-2<p_1<=c-1`, the outsider remains foreclosed and the two-firm profit function applies. Its unconstrained best response to `p_2=c-1` is `(c+1)/2>c-1`, so profit increases up to the foreclosure boundary.
3. If `p_1>c-1`, direct comparison with firms 2 and 3 gives `q_1=max{c+1/2-p_1,0}`. The positive-demand profit vertex lies strictly below `c-1` when `c>5/2`, so profit falls throughout the entire upward-deviation region; still higher prices give zero demand.

The outsider earns zero at `p_3=c`; below-cost positive-demand deviations have negative margin, while prices at or above cost cannot profitably enter. Hence `p_M=c-1` is a global member best response.

### Region III: 3 <= c < 5

At `(2,2,c)`, removing the outsider weakly increases member demand and therefore upper-bounds deviation profit. Against the other member's price 2:

- `p_1<=0` gives non-positive profit;
- `0<=p_1<=1` gives profit at most 3;
- for `1<=p_1<=3`, two-firm profit is `p_1(3-3p_1/4)`, uniquely maximized at `p_1=2` with value 3;
- for `3<=p_1<=4`, demand is weakly below `3/4`, so profit is at most 3;
- for `p_1>=4`, the other member weakly dominates firm 1 everywhere and demand is zero.

Adding the outsider cannot increase a member's demand. Thus `p_M=2` is a global best response. Zero-demand outsider prices can be nonunique at high `c`, so the proposition appropriately characterizes member prices and allocation rather than claiming uniqueness of an arbitrary full price vector.

**Proposition 1: PASS.**

## Dense numerical falsification

The C5 numerical checker evaluates global unilateral best responses on a discretized Salop circle using delivered-price thresholds rather than a local price grid.

- 453 values of `c` were checked on `[2.5001,4.999]`.
- Representative diagnostics include 2.5001, 2.51, 2.6, 2.75, 2.9, 2.99, 2.9999, 3, 3.0001, 3.1, 3.5, 4, 4.5, 4.9, 4.999.
- Maximum apparent fine-grid member gain: `5.6249531e-05`, below the fixed discretization bound `0.00075`.
- The artifact shrinks from `0.0002249925` at `N=20000` to `5.6249531e-05` at `N=80000`.
- Maximum outsider profitable gain: 0.
- Exact `c=4` published-profile check: `2.25 -> 2.296875`, gain `3/64`.

**Dense falsification: PASS; no counterexample found.**

## Welfare audit

Under foreclosure, consumer mass is 3 and total transportation cost is `3/4`, so `CS_M^SU=3V-3p_M-3/4`. The domestic member firm earns `3p_M` across the two union markets. Under the recognition behavior used by the original Proposition 3, the nonmember country recognizes all standards and the member firm earns one additional unit there. Thus `Pi_M^SU=3p_M+1` and `TS_M^SU=3V+1/4`.

Under mutual recognition, symmetric pricing and shares give `TS^MR=3V-1/4`, so the member-country gap remains `1/2`. Foreign-firm profit is not part of a member country's national welfare, while worldwide profit of the domestic firm is. The cancellation is a model-specific national-accounting result, not a general invariance theorem.

**Proposition 2: PASS.**

## Referee attack matrix

1. **“Proposition 3 survives, so the correction is irrelevant.” — MAJOR, not fatal.** The Nash equilibrium is wrong on a nondegenerate interval and the strategic path becomes three active firms -> limit pricing -> unconstrained duopoly; welfare robustness is a separate replication result.
2. **“This is only a denominator correction.” — MAJOR, not fatal.** The published profile has a profitable unilateral deviation and the correction creates a missing equilibrium regime.
3. **“The result is obvious with two firms.” — MODERATE.** The zero-sales outsider remains a binding competitive constraint for `5/2<c<3`.
4. **“Limit pricing is standard.” — MODERATE.** The manuscript does not claim novelty for limit pricing; novelty is the corrected characterization of this published benchmark.
5. **“This belongs in a two-page erratum.” — MAJOR editorial risk.** The correction changes equilibrium over a nondegenerate interval, requires a global three-firm deviation proof, and re-establishes the original welfare ranking under the corrected equilibrium.
6. **“The source article is twenty-five years old.” — MODERATE.** The note makes only a restrained claim about the theoretical genealogy of international standards and compatibility work.
7. **“The qualitative trade-policy conclusion survives.” — MODERATE.** The contribution is precisely to distinguish a corrected mechanism from a robust welfare statement.
8. **“Secondary corrections make this error hunting.” — MINOR after C5.** Those items have been removed from the submitted manuscript and retained only in repository provenance.
9. **“Why International Economics rather than JIE?” — MODERATE.** International Economics explicitly provides a Short-paper route and fits the topic; JIE applies a stronger originality/model-structure screen and currently charges a submission fee.
10. **“The old working paper already has p=3tau/2.” — MINOR.** It uses linear transportation; it is not prior art for the corrected quadratic-model equilibrium.

No objection is fatal.

## Compression, title, and appendix decision

C5 does not expand the manuscript to an arbitrary prose target. Repetition was removed while the equilibrium proof was strengthened globally. The current paper is self-contained and substantially below the journal's maximum word count.

**Title decision: KEEP CURRENT TITLE** — *Foreclosure and Limit Pricing in Standardization Unions: A Correction to Gandal and Shy (2001)*. It is accurate, searchable, neutral, and does not claim novelty for limit pricing itself.

The main submission now contains **no technical appendix**. All proposition-critical material is in the body. Boundary facts and outsider-price nonuniqueness are in the proof/footnote; Table 2, country-size, and network-effect consistency checks are repository-only (`docs/SECONDARY_CORRECTIONS.md`). Reproducibility is handled by code plus a C6 availability statement.

## Journal fit

International Economics is a plausible first target because the subject is international product standards, recognition policy, regional standardization unions, foreign-firm foreclosure, and welfare under trade-policy institutions. The current Short-paper policy explicitly permits manuscripts up to 7,000 words and requires self-containment; the C5 draft satisfies both conditions and has no exhibits.

The contribution is defensible but narrow: a published Nash equilibrium is corrected over a nondegenerate parameter interval, an economically interpretable limit-pricing region appears, and the original welfare ranking is verified under the correct equilibrium.

**Desk-reject risk: MODERATE.** The strongest risk is editorial narrowness: the benchmark is old and its headline welfare result survives. C5 deliberately does not add theory to reduce that risk.

## Desk-reject simulation

The paper presents a new and correct correction of a published international-standards benchmark. Its global-deviation proof is complete, the missing regime is economically meaningful, and welfare robustness is established rather than assumed. The topic fits international trade and standards policy and the manuscript is self-contained in seven pages. The strongest desk-reject reason is narrowness rather than mathematical or field mismatch.

**Editor simulation: BORDERLINE, leaning SEND TO REFEREE.**

## Mock referee verdict

The principal technical concern is whether the piecewise prices are global best responses rather than local kink optima. The C5 revision resolves this by partitioning all member deviations and using a two-firm upper bound in the high-cost regime. The paper properly avoids claiming novelty for limit pricing and removes secondary error hunting from the submission. The remaining concern is editorial significance because Proposition 3 survives.

**Recommendation: publishable as a short note subject to editorial interest / minor expositional revision.**

## C5 final gate

- Proposition 1 global audit: PASS.
- Proposition 2 welfare audit: PASS.
- Dense numerical falsification: PASS.
- Exactly two propositions: PASS.
- Self-contained manuscript: PASS.
- Secondary-error catalogue removed: PASS.
- International Economics format: compatible.
- Clean build and visual QA: PASS.
- Claim blacklist: PASS.
- Journal fit: defensible, with MODERATE desk risk.

**Final: GO TO C6 — Submission Freeze & International Economics Package.**
