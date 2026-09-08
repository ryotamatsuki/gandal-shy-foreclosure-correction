# Gandal-Shy Foreclosure Correction

Research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

> **CURRENT SCIENTIFIC STATUS — 2026-09-09**  
> The pre-Astra Stage-13R manuscript is **not cleared for submission**. Stage 14 remains blocked.  
> `C0–C1R — Targeted Equilibrium-Set Reaudit` has passed.  
> `C2R — Symbolic / Numerical Counterexample and Global-Deviation Audit` has also passed with a rebuilt three-price verifier.  
> **Next stage:** `C2R-L — Lean Formal Certification`.

The authoritative project-specific recovery route is:

- [`docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`](docs/REVISION_TO_RESUBMISSION_WORKFLOW.md) — full revision-to-resubmission sequence and return rules;
- [`docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`](docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md) — current theorem-ready analytic results;
- [`docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`](docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md) — rebuilt falsification/regression audit entering Lean.

**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`.  
**Recovery-plan baseline:** `main@40e4e76721534c39bfe3f13ad97cea1183732d48`.  
**C0–C1R merge baseline for C2R:** `main@8b4432017ea0662147c23c8946804750225a74dd`.  
**Provisional journal target:** *International Economics* — short-format route, subject to Stage 12R2 re-evaluation after revised theory freeze.  
**Pre-Astra working title:** *Standardization Unions, Foreclosure, and Limit Pricing: Revisiting Gandal and Shy (2001)*.  
**Previous submission:** *Review of Industrial Organization* (RIO), editorially rejected before external review.  
**Author-cost hard gate:** zero submission fee and zero mandatory publication/page/APC charge under the standard non-OA route.

## Current scientific result after C0–C1R

The correction itself survives, but its scope has changed.

### 1. Published profile

The published article uses quadratic transportation cost, but Appendix B uses an inconsistent long-arc price-difference coefficient. Under the published primitive,

`x^L = 1 + (p_2-p_1)/4`.

At `c=4`, the complete published profile `(3/2,3/2,4)` is not Nash: a member deviation to `7/4` raises profit from `9/4` to `147/64`.

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

Therefore the Proposition-3 ranking is **not selection-free across arbitrary unrestricted continuation selections**. It survives under a common symmetric continuation price and, in particular, under the symmetric cost-floor continuation characterized above.

No claim is made yet about all asymmetric pure equilibria, mixed equilibria, or the full government-stage game under unrestricted multiplicity.

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

The high-resolution C2R run tested 91 valid-family profiles. The maximum apparent equilibrium gain was `5.6249531e-05`, below the fixed discretization allowance `0.0009`. The published profile was correctly rejected with a discretized gain `0.046924219`, while the Astra equilibrium remained within the grid-error bound. Details are in `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`.

C2R remains a falsification/regression layer, not a proof of equilibrium-set completeness.

## Recovery route

The project follows this overlay on `ryotamatsuki/research-paper-workflow` v2.1:

1. **C0–C1R — Targeted Equilibrium-Set Reaudit:** **PASS.** Analytic characterization completed.
2. **C2R — Symbolic / Numerical Audit:** **PASS.** Three-price unrestricted/cost-floor falsification layer rebuilt; known counterexamples preserved as regression tests.
3. **C2R-L — Lean Formal Certification:** **NEXT.** Formalize the settled high-stakes claims and exact quantifiers before theory freeze.
4. **C3R — Revised Canonical Theory Freeze:** freeze exact games, equilibrium classes, quantifiers, parameter domains, and prohibited stronger claims.
5. **C4R — Hostile Scientific Self-Audit:** attack the revised frozen theory for hidden equilibria, boundary failures, strategy-space errors, and welfare-selection overclaims.
6. **Stage 12R2 — Journal Significance / Fit Recheck:** reassess *International Economics* after the contribution changes.
7. **Stage 13R2 — Revised Full-Paper Integration:** rewrite Sections 2–4 first, then Abstract/Introduction/Conclusion and submission materials.
8. **Astra-2 — Independent Hostile Referee Gate:** review the complete revised paper before submission QA.
9. **Stage 14 — Submission QA:** only after Astra-2 scientific clearance.
10. **Stage 15 — Submission Freeze / Portal Preflight / Submit:** freeze exact artifacts, reconcile portal metadata, inspect generated PDF, enforce zero-fee gate, submit, and record confirmation.

**Do not skip directly to Stage 14.**

## Historical records now explicitly superseded

The following remain useful as provenance but are not current theory authority:

- `docs/C0_C1_MATHEMATICAL_AUDIT.md` — historical/superseded;
- `docs/C3_CANONICAL_FREEZE.md` — reopened; no current freeze is in force;
- `docs/STAGE_12R_INTERNATIONAL_ECONOMICS_POSITIONING.md`;
- `docs/JOURNAL_REQUIREMENTS_LEDGER_INTERNATIONAL_ECONOMICS.md`;
- `docs/STAGE_13R_INTERNATIONAL_ECONOMICS_INTEGRATION.md`.

The pre-Astra manuscript and submission package are retained as baselines only. They are not the resubmission version.

## Lean timing

Lean now becomes the active stage:

```text
C0–C1R analytic audit  [PASS]
    ↓
C2R symbolic/numerical falsification  [PASS]
    ↓
C2R-L Lean formal certification  [NEXT]
    ↓
C3R revised theory freeze
```

The Lean theorem statements must match the exact C0–C1R quantifiers: parameter interval, strategy domain, symmetry, foreclosure condition, pure-strategy class, and existence/necessity/uniqueness status. If Lean exposes a mathematical gap, return to C0–C1R rather than weakening only the prose.

## Build and verification

```bash
python -m pip install -r requirements.txt
make verify
make pdf
make packages
make title-page
# or
make all
```

`make verify` now executes the C2R symbolic checks and the rebuilt three-price numerical falsification suite.

## Structure

- `docs/REVISION_TO_RESUBMISSION_WORKFLOW.md` — authoritative recovery route
- `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md` — current analytic theorem set
- `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md` — current falsification/regression record
- `docs/` — historical mathematical provenance, RIO records, and journal-positioning records
- `paper/` — pre-Astra LaTeX baseline until Stage 13R2
- `code/` — current C2R symbolic/numerical verification; next formalized in Lean
- `submission/` — pre-Astra working package; rebuilt only after revised theory freeze
- `output/` — generated manuscript/package outputs, not committed
