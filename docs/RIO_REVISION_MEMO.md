# RIO Targeted Revision Memo

Date: 2026-09-01

Target: *Review of Industrial Organization* (RIO)

Branch: `revision/rio-targeted-framing`

Base: validated `c4-short-paper-draft` state, not the later RIE-targeted branch.

## What changed

1. **Title**
   - Before: *Foreclosure and Limit Pricing in Standardization Unions: A Correction to Gandal and Shy (2001)*
   - RIO version: *Foreclosure and Limit Pricing in Standardization Unions: Revisiting Gandal and Shy (2001)*
   - Reason: preserves discoverability and connection to the original paper while avoiding confusion with a publisher-issued Correction notice.

2. **Abstract**
   - Expanded to satisfy RIO's 150–250 word requirement.
   - Reframed around the IO distinction between realized foreclosure and strategic irrelevance.
   - Keeps correction, limit-pricing mechanism, and welfare robustness visible within one abstract.

3. **Introduction**
   - Opens with the pricing-incentive question rather than international-trade policy.
   - Defines the central mechanism as a zero-sales outsider remaining a binding competitive constraint.
   - Positions the standardization union as the application and foreclosure/oligopoly pricing as the contribution.

4. **Literature positioning**
   - Added only two core IO references: Rey and Tirole (2007) on foreclosure and Milgrom and Roberts (1982) on classic limit pricing.
   - Explicitly distinguishes the present binding-exclusion mechanism from informational signaling models of limit pricing.
   - Retains a minimal standards/compatibility lineage without expanding the literature review.

5. **Conclusion**
   - Rewritten around the transition from realized foreclosure with a binding competitive constraint to unconstrained duopoly.
   - Welfare robustness is presented as a second result, not as evidence that the correction is unimportant.

6. **Springer/RIO submission compliance**
   - Added `Statements and Declarations` to the manuscript.
   - Added Funding, Competing Interests, Data Availability, and substantive LLM-use disclosure.
   - Updated title page and RIO-specific cover letter.
   - Renamed the flat LaTeX export to `rio-flat` / `rio-submission-source.zip`.

## What deliberately did not change

- No primitive.
- No new model.
- No new country or firm asymmetry.
- No network-effect extension.
- No empirical exercise.
- No welfare extension.
- No new proposition.
- No robustness appendix.
- Mathematical Sections 2–4 remain substantively frozen.

## Frozen canonical results

- Foreclosure threshold: `c=5/2`.
- Limit-pricing regime: `p_M=c-1` for `5/2<c<3`.
- Unconstrained duopoly regime: `p_M=2` for `3<=c<5`.
- Post-foreclosure allocation: `q_1=q_2=3/2`, `q_3=0`.
- Member-country welfare under SU: `TS_M^SU=3V+1/4`.
- Mutual-recognition welfare: `TS^MR=3V-1/4`.
- Welfare gap: `1/2`.

## Mathematical verification

Independent 2026-09-01 rerun before the editorial revision:

- symbolic identities for short and long arcs: PASS;
- two-firm demand and unconstrained duopoly price: PASS;
- continuity at `c=5/2` and `c=3`: PASS;
- transportation cost and welfare identities: PASS;
- dense numerical global-deviation falsification: PASS on 453 cost values;
- maximum apparent member discretization gain: `5.62495312497191e-05`, below fixed grid bound `0.00075`;
- maximum outsider profitable gain: `0`;
- apparent discretization gain shrinks from `0.00022499249999974325` at `N=20000` to `5.62495312497191e-05` at `N=80000`.

No editorial change alters these results.

## Remaining editorial risk

The main risk is narrowness: the source article is old and the headline member-country welfare ranking survives. RIO fit mitigates this risk because the journal explicitly welcomes shorter notes and commentaries, but it does not eliminate the need for the editor to regard the corrected Nash equilibrium and omitted nondegenerate limit-pricing region as professionally interesting.

The manuscript therefore avoids claim inflation and does not add a new model solely to increase perceived size.
