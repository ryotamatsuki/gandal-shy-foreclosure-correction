# Gandal-Shy Foreclosure Correction

Research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

> **CURRENT SCIENTIFIC STATUS — 2026-09-09**  
> The pre-Astra Stage-13R manuscript is **not cleared for submission**. Stage 14 remains blocked.  
> `C0–C1R — Targeted Equilibrium-Set Reaudit`: **PASS**.  
> `C2R — Symbolic / Numerical Counterexample and Global-Deviation Audit`: **PASS**.  
> `C2R-L — Lean Formal Certification`: **PASS** with CI-backed compilation and no `sorry`/`admit`.  
> `C3R — Revised Canonical Theory Freeze`: **PASS**.  
> **Next stage:** `C4R — Hostile Scientific Self-Audit`.

The authoritative recovery records are:

- [`docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`](docs/REVISION_TO_RESUBMISSION_WORKFLOW.md) — full revision-to-resubmission sequence and return rules;
- [`docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`](docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md) — analytic equilibrium-set reconstruction;
- [`docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`](docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md) — rebuilt falsification/regression audit;
- [`docs/C2R_L_LEAN_CERTIFICATION.md`](docs/C2R_L_LEAN_CERTIFICATION.md) — formal certification scope, theorem inventory, CI evidence, and limitations;
- [`docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`](docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md) — controlling revised theory freeze and prohibited stronger claims.

**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`.  
**Recovery-plan baseline:** `main@40e4e76721534c39bfe3f13ad97cea1183732d48`.  
**C0–C1R merge:** `8b4432017ea0662147c23c8946804750225a74dd`.  
**C2R merge:** `7bb77278152d803ada52ac02ca0d70c70fa9a71c`.  
**C2R-L merge:** `19630342fec2fc0a4b0ba4e900d3d8358581f74c`.  
**Provisional journal target:** *International Economics* — short-format route, subject to Stage 12R2 re-evaluation after revised theory freeze and C4R.  
**Pre-Astra working title:** *Standardization Unions, Foreclosure, and Limit Pricing: Revisiting Gandal and Shy (2001)*. The title is not frozen by C3R.  
**Previous submission:** *Review of Industrial Organization* (RIO), editorially rejected before external review.  
**Author-cost hard gate:** zero submission fee and zero mandatory publication/page/APC charge under the standard non-OA route.

## Current frozen scientific result

The correction survives, but the scope is narrower and more precise than in the pre-Astra manuscript.

### 1. Published profile

The published article uses quadratic transportation cost, but Appendix B uses an inconsistent long-arc price-difference coefficient. Under the published primitive,

`x^L = 1 + (p_2-p_1)/4`.

At `c=4`, the complete published profile `(3/2,3/2,4)` is not Nash: a member deviation to `7/4` raises profit from `9/4` to `147/64`, a gain of `3/64`.

The correction is therefore to the **complete published profile**, not a claim that member price `3/2` can never occur in any equilibrium.

### 2. Unrestricted original price game

Within **symmetric foreclosed pure-strategy profiles** `(s,s,r)`, C0–C1R analytically characterizes the unrestricted equilibrium set as:

- `3/2 <= s < 2`, `r=s+1`, `c>=s+1`; or
- `s=2`, `r>=3`, `c>=3`.

Thus the unrestricted game has genuine member-price multiplicity. For `c>=5/2`, the admissible member price spans

`3/2 <= s <= min{2,c-1}`,

subject to the outsider-price conditions above.

### 3. Explicit cost-floor game

Define a separate restricted price game with

`p_i >= marginal cost in that market`.

This is an explicit strategy restriction, not WLOG and not a claim about weakly undominated Nash equilibrium.

Within symmetric foreclosed pure-strategy equilibria, the restriction yields:

- `5/2 <= c < 3`: `(p_1,p_2,p_3)=(c-1,c-1,c)`;
- `c>=3`: `p_1=p_2=2`, with any `p_3>=c`.

Hence the **member price** is uniquely characterized in this class by

`p_M=c-1` for `5/2<c<3`,

`p_M=2` for `3<=c<5`.

The outsider price remains nonunique for `c>=3`.

### 4. Welfare scope

If both segmented union markets use the same symmetric member price `s`, then

`TS_M^SU=3V+1/4`,

`TS^MR=3V-1/4`,

and the member-country gap remains `1/2`.

If the two markets select different symmetric continuation prices `s_A` and `s_B`, then

`TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`.

Therefore the Proposition-3 ranking is **not selection-free across arbitrary unrestricted continuation selections**. It is preserved under a common symmetric continuation price and, in particular, under the symmetric cost-floor continuation characterized above.

No claim is made about all asymmetric pure equilibria, mixed equilibria, or the full government-stage game under unrestricted multiplicity.

## C2R verification status

The old verifier fixed `p_3=c` and therefore could not detect the Astra multiplicity. C2R replaced that design.

The current numerical verifier:

- varies `p_1`, `p_2`, and `p_3`;
- computes global unilateral best responses from primitive delivered-price thresholds;
- has separate unrestricted and cost-floor modes;
- preserves the published `c=4` counterexample as a mandatory failure test;
- preserves the Astra profile `(3/2,3/2,5/2)` at `c=4` as a mandatory unrestricted-equilibrium regression test;
- checks necessity violations and representative asymmetric perturbations;
- performs a `N=20,000 -> 80,000` convergence check.

The high-resolution C2R run tested 91 valid-family profiles. The maximum apparent equilibrium gain was `5.6249531e-05`, below the fixed discretization allowance `0.0009`. The published profile was correctly rejected with a discretized gain `0.046924219`, while the Astra equilibrium remained within the grid-error bound. C2R remains a falsification/regression layer, not a proof of equilibrium-set completeness.

## C2R-L Lean certification status

The repository contains a pinned Lake/Lean project:

- `lean-toolchain`: `leanprover/lean4:v4.34.0-rc2`;
- `lakefile.toml`: mathlib pinned to commit `74828d59824ed9c1e3002f796aaf53cec5ffb47c`;
- `GandalShy/Certification.lean`: formal theorem source;
- `.github/workflows/lean-certification.yml`: CI compilation and admitted-proof gate.

Lean formally certifies the proof-critical algebraic core, including:

- the corrected long-arc coefficient `1/4`;
- the exact `c=4` profitable-deviation counterexample;
- regular-branch and outsider-relevant profit-gap factorizations;
- global no-gain inequalities used in the unrestricted lower-price family;
- necessity sign checks for `s<3/2`, `s>2`, and outsider-threshold failure;
- multiplicity of the analytic Theorem-U condition set;
- exact cost-floor reduction and piecewise member-price characterization;
- common-price and cross-market welfare identities.

GitHub Actions run `34291397450` completed successfully: `lake build GandalShy` passed and the repository scan found no `sorry` or `admit` token. The formal record explicitly does **not** claim that Lean has reconstructed the entire continuum Salop demand game or independently derived every Nash equilibrium from primitives. See `docs/C2R_L_LEAN_CERTIFICATION.md`.

## C3R freeze status

`docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md` is now the controlling scientific specification. It freezes:

- the exact unrestricted and cost-floor game definitions;
- the symmetric, foreclosed, pure-strategy equilibrium class;
- the U1/U2 unrestricted characterization and member-price multiplicity;
- the F1/F2 cost-floor characterization;
- the `c=5/2` and `c=3` boundary treatment;
- the common-price and cross-market welfare statements;
- the exact scope of Lean certification;
- a prohibited-claims list preventing existence/characterization/uniqueness drift.

The pre-Astra `docs/C3_CANONICAL_FREEZE.md` is historical provenance only.

## Recovery route

The project follows this overlay on `ryotamatsuki/research-paper-workflow` v2.1:

1. **C0–C1R — Targeted Equilibrium-Set Reaudit:** **PASS**.
2. **C2R — Symbolic / Numerical Audit:** **PASS**.
3. **C2R-L — Lean Formal Certification:** **PASS**.
4. **C3R — Revised Canonical Theory Freeze:** **PASS**.
5. **C4R — Hostile Scientific Self-Audit:** **NEXT**. Attack the revised frozen theory for hidden equilibria, boundary failures, strategy-space errors, welfare-selection overclaims, and Lean-scope drift.
6. **Stage 12R2 — Journal Significance / Fit Recheck:** reassess *International Economics* after the contribution changes.
7. **Stage 13R2 — Revised Full-Paper Integration:** rewrite Sections 2–4 first, then Abstract/Introduction/Conclusion and submission materials.
8. **Astra-2 — Independent Hostile Referee Gate:** review the complete revised paper before submission QA.
9. **Stage 14 — Submission QA:** only after Astra-2 scientific clearance.
10. **Stage 15 — Submission Freeze / Portal Preflight / Submit:** freeze exact artifacts, reconcile portal metadata, inspect generated PDF, enforce zero-fee gate, submit, and record confirmation.

**Do not skip directly to Stage 14.**

## Historical records explicitly superseded

The following remain useful as provenance but are not current theory authority:

- `docs/C0_C1_MATHEMATICAL_AUDIT.md` — historical/superseded;
- `docs/C3_CANONICAL_FREEZE.md` — historical/superseded by C3R;
- `docs/STAGE_12R_INTERNATIONAL_ECONOMICS_POSITIONING.md`;
- `docs/JOURNAL_REQUIREMENTS_LEDGER_INTERNATIONAL_ECONOMICS.md`;
- `docs/STAGE_13R_INTERNATIONAL_ECONOMICS_INTEGRATION.md`.

The pre-Astra manuscript and submission package are retained as baselines only. They are not the resubmission version.

## Formal-proof timing

```text
C0–C1R analytic audit  [PASS]
    ↓
C2R symbolic/numerical falsification  [PASS]
    ↓
C2R-L Lean formal certification  [PASS]
    ↓
C3R revised theory freeze  [PASS]
    ↓
C4R hostile scientific self-audit  [NEXT]
```

If C4R or a later hostile audit changes a mathematical quantifier, strategy domain, equilibrium class, or substantive theorem statement, the affected analytic result and Lean theorem must be updated and rechecked before another freeze is valid.

## Build and verification

Python/symbolic/numerical verification:

```bash
python -m pip install -r requirements.txt
make verify
```

Lean formal verification:

```bash
lake build GandalShy
```

Manuscript/package commands remain available for the pre-Astra baseline, but the paper itself is not rewritten until Stage 13R2.

## Structure

- `docs/REVISION_TO_RESUBMISSION_WORKFLOW.md` — authoritative recovery route
- `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md` — analytic theorem set
- `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md` — falsification/regression record
- `docs/C2R_L_LEAN_CERTIFICATION.md` — Lean certification record
- `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md` — controlling revised scientific freeze
- `GandalShy/` — formal Lean source
- `code/` — C2R symbolic/numerical verification
- `paper/` — pre-Astra LaTeX baseline until Stage 13R2
- `submission/` — pre-Astra working package; rebuilt only after revised theory freeze
- `output/` — generated manuscript/package outputs, not committed