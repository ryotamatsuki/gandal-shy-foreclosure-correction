# C2R-L — Lean Formal Certification

**Date:** 2026-09-09  
**Branch:** `formal/c2r-lean-certification`  
**Base:** `main@7bb77278152d803ada52ac02ca0d70c70fa9a71c`  
**Inputs:** `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`, `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`, `docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`  
**Formal source:** `GandalShy/Certification.lean`  

## 1. Executive verdict

**C2R-L verdict: `PASS — PROCEED TO C3R REVISED CANONICAL THEORY FREEZE`.**

The proof-critical algebra and quantified inequality core of the reopened post-foreclosure analysis now compiles in Lean without `sorry` or `admit` under a pinned Lean/mathlib environment.

The certification is deliberately scoped. Lean does **not** reimplement the full continuum Salop game, consumer measure, or the complete demand correspondence from primitives. The complete economic equilibrium characterization remains the analytic result of C0–C1R, stress-tested in C2R. Lean certifies the algebraic identities, global-deviation inequalities, necessity sign checks, condition-set multiplicity, cost-floor reduction, and welfare identities on which the C0–C1R proof depends.

This distinction is mandatory for C3R: no manuscript or freeze record may state that the full Salop Nash-equilibrium correspondence has been mechanically derived from primitives by Lean.

## 2. Reproducible formal environment

The repository now contains a self-contained Lake project:

- `lean-toolchain`: `leanprover/lean4:v4.34.0-rc2`;
- `lakefile.toml`: mathlib pinned to commit `74828d59824ed9c1e3002f796aaf53cec5ffb47c`;
- `lake-manifest.json`: dependency lock;
- `GandalShy.lean`: library entry point;
- `GandalShy/Certification.lean`: formal theorem file;
- `.github/workflows/lean-certification.yml`: CI compilation and admitted-proof rejection.

The environment is pinned by exact versions/commits rather than floating branches.

## 3. CI certification

GitHub Actions workflow `Lean formal certification`, run **34291397450**, completed successfully after the workflow was corrected to use the successful Lake build as the compilation gate.

The successful job established:

1. Lean toolchain installation succeeds;
2. mathlib cache/dependencies resolve under the pinned environment;
3. `lake build GandalShy` completes successfully;
4. `GandalShy/Certification.lean` is compiled;
5. the explicit repository scan finds no `sorry` or `admit` token in the formal source.

The build log reports `Build completed successfully (8908 jobs)`.

The `#print axioms` diagnostics for the designated headline theorems report only Lean/mathlib's standard logical axioms used by the tactics (`propext`, `Classical.choice`, `Quot.sound`). No project-specific axiom, `sorryAx`, or admitted theorem is introduced.

The build emits only unused-variable linter warnings in several auxiliary lemmas; these do not affect theorem validity or compilation.

## 4. Formally certified targets

### 4.1 Corrected long-arc calculation

`long_arc_boundary` proves that

`p_1 + x^2 = p_2 + (2-x)^2`

implies

`x = 1 + (p_2-p_1)/4`.

This formally certifies the coefficient `1/4` at the source of the correction.

### 4.2 Exact published-profile counterexample

Theorems

- `published_profile_c4_base`,
- `published_profile_c4_deviation`,
- `published_profile_c4_profitable`, and
- `published_profile_c4_gain`

certify exactly that at the published `c=4` profile the member profit rises from

`9/4`

to

`147/64`

under the deviation to `7/4`, with gain

`3/64 > 0`.

This is a machine-checked certificate that the complete published profile `(3/2,3/2,4)` is not Nash.

### 4.3 Global-deviation inequality core

Lean certifies the factorized profit gaps used in the analytic global proof:

- `regular_profit_gap`;
- `entry_profit_gap`.

It also proves the no-gain inequalities for the relevant deviation regions:

- `negative_price_no_gain`;
- `low_price_no_gain`;
- `regular_price_no_gain`;
- `entry_price_no_gain`;
- `zero_demand_no_gain`;
- `u1_deviation_partition`.

These results certify the algebraic/global-inequality skeleton used to establish sufficiency of the lower-price unrestricted family once the C0–C1R demand-region mapping is supplied.

### 4.4 Necessity sign checks

Lean proves the strict-improvement signs used to exclude overbroad candidate regions:

- `regular_upward_profitable`: if `s<2`, an admissible sufficiently small regular-branch upward move is profitable;
- `regular_downward_profitable`: if `s>2`, an admissible sufficiently small regular-branch downward move is profitable;
- `entry_upward_profitable`: if `s<3/2`, an admissible sufficiently small outsider-relevant upward move is profitable;
- `outsider_profitable_quote_interval`: if `c<s+1`, a quote exists strictly between marginal cost and the foreclosure threshold.

The economic facts that a sufficiently small move remains in the stated demand branch, and that a quote below `s+1` yields positive-measure outsider demand, remain analytic model facts from C0–C1R rather than independently formalized measure-theoretic statements.

## 5. Equilibrium-condition multiplicity and cost-floor reduction

### 5.1 Unrestricted multiplicity

`UCond` encodes the exact symmetric-foreclosed condition set established analytically in Theorem U:

- lower-price branch: `3/2 <= s < 2`, `r=s+1`, `s+1<=c`;
- duopoly-price branch: `s=2`, `3<=r`, `3<=c`.

`ucond_member_price_multiplicity` proves that for every strict post-foreclosure `c>5/2`, this analytic condition set contains two equilibria with distinct member prices.

This is a formal certificate of multiplicity **conditional on the analytic equivalence between `UCond` and the symmetric-foreclosed pure-strategy Nash set proved in C0–C1R**. It is not a second independent derivation of that equivalence from consumer primitives.

### 5.2 Explicit cost-floor game

`CostFloorCond` adds the explicit outsider strategy restriction `c <= r` to `UCond`.

`costFloor_characterization` proves the exact logical reduction:

- `5/2 <= c < 3`: `s=c-1` and `r=c`;
- `3 <= c`: `s=2` and `c<=r`.

`costFloor_member_price` therefore certifies the piecewise member-price formula

`p_M = c-1` for the lower branch and `p_M=2` for the upper branch,

within the exact symmetric-foreclosed condition class.

`costFloor_c3_member_price` certifies that the two branches meet at `c=3` with member price `2`.

The formal source does not describe the cost floor as WLOG, weak-dominance elimination, or a restriction present in Gandal and Shy (2001). It is an explicit modified strategy set.

## 6. Welfare identities

Lean certifies:

- `common_price_welfare`:
  `TS_M^SU = 3V + 1/4` under a common symmetric continuation price;
- `common_price_welfare_gap`:
  the gap over `TS^MR=3V-1/4` equals `1/2`;
- `cross_market_welfare`:
  with market-specific symmetric continuation prices,
  `TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`;
- `cross_market_equal_prices`:
  equal continuation prices eliminate the cross-market transfer term.

Thus Lean confirms exactly why the earlier welfare robustness result is valid under common symmetric continuation but is not selection-free across arbitrary market-by-market continuation choices.

## 7. What Lean does not certify

The following remain outside the formal theorem claims and must not be attributed to Lean:

1. the full continuum demand correspondence from Salop consumer primitives;
2. measure-zero/tie-breaking details;
3. a complete characterization of asymmetric pure equilibria;
4. mixed equilibria;
5. the government-stage equilibrium under unrestricted continuation multiplicity;
6. the literature/prior-art or publication-significance claims.

These exclusions are intentional. They prevent the formal certificate from being broader than the actual formalization.

## 8. C2R-L gate assessment

The workflow required formal certification of the settled high-stakes claims before a new theory freeze. The designated proof-critical targets now compile and are admission-free.

Accordingly:

`C2R-L = PASS`.

The next stage is:

**C3R — Revised Canonical Theory Freeze.**

C3R must freeze only claims whose exact scope is jointly supported by:

1. C0–C1R analytic necessity/sufficiency;
2. C2R symbolic/numerical falsification;
3. this C2R-L formal certificate.

If C3R changes a mathematical quantifier, strategy domain, equilibrium class, or substantive theorem statement, the affected Lean result must be updated and recompiled before the new freeze is valid.
