# Gandal-Shy Foreclosure Correction

Research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

> **CURRENT SCIENTIFIC STATUS — 2026-09-10**  
> `C0–C1R`: **PASS**  
> `C2R`: **PASS**  
> `C2R-L Lean`: **PASS**  
> `C3R Revised Canonical Theory Freeze`: **PASS**  
> `C4R Hostile Scientific Self-Audit`: **PASS**  
> `Stage 12R2 Journal Significance / Fit Recheck`: **PASS**  
> `Stage 13R2 Revised Full-Paper Integration`: **PASS; bounded Astra-2 repairs merged**  
> `Astra-2`: **CLEARED after limited recheck on main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d**  
> **Next stage:** `Stage 14 — Submission QA`.

Authoritative records:

- [`docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`](docs/REVISION_TO_RESUBMISSION_WORKFLOW.md)
- [`docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`](docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md)
- [`docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`](docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md)
- [`docs/C2R_L_LEAN_CERTIFICATION.md`](docs/C2R_L_LEAN_CERTIFICATION.md)
- [`docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`](docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md)
- [`docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`](docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md)
- [`docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`](docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md)
- [`docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md`](docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md)
- [`docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`](docs/ASTRA_2_HOSTILE_REFEREE_GATE.md)

Key provenance:

- pre-reopening manuscript baseline: `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`
- C2R-L merge: `19630342fec2fc0a4b0ba4e900d3d8358581f74c`
- C3R merge: `5f0a57fe99b94deb51f229254a7f5882ac21ad49`
- C4R merge: `20a05cb9499eb8865e1ca3df77a5758b62765864`
- Stage 12R2 merge: `a312babe551c87afd203678215bb2467b36a1bff`
- Stage 13R2 merge / Astra-2 first-pass baseline: `ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`
- Astra-2 first-pass verdict: `B. MINOR EXPOSITION REPAIR`
- bounded repair PR: `#14`
- repaired manuscript CI head: `72ed861e3460cbcaf5eaf0a763f789c70ed07332`
- successful repair CI: run `34379361638`
- bounded-repair merge: `02a691e9260c48a5e9485e7d8188caf3648f918f`
- gate-status correction merge / limited-recheck target: `ec164d092c5be14df12dbf44c40c8d947d7cdc7d`
- Astra-2 limited recheck: Repair 1 **PASS**, Repair 2 **PASS**, Repair 3 **PASS**, new defect **NO**
- final Astra-2 verdict: `A. ASTRA-2 CLEARED — GO TO STAGE 14`

## Frozen scientific result

### 1. Published profile

The published model uses quadratic transportation cost. On the long arc,

`x^L = 1 + (p_2-p_1)/4`,

not the coefficient used in Appendix B. The complete published profile `(3/2,3/2,c)` is not Nash for every strict `c>5/2` in the paper's post-foreclosure range.

The correction is to the complete profile and associated equilibrium/uniqueness claim. It is **not** a claim that member price `3/2` can never occur in another equilibrium.

### 2. Unrestricted original game

Within **symmetric, foreclosed, pure-strategy profiles** `(s,s,r)`, the unrestricted equilibrium set is:

- `3/2 <= s < 2`, `r=s+1`, `c>=s+1`; or
- `s=2`, `r>=3`, `c>=3`.

Thus the original game has genuine member-price multiplicity.

### 3. Explicit cost-floor game

Define a separate restricted game with

`p_i >= marginal cost in that market`.

Within the same symmetric, foreclosed, pure-strategy class:

- `5/2 <= c < 3`: `(p_1,p_2,p_3)=(c-1,c-1,c)`;
- `c>=3`: `p_1=p_2=2`, with `p_3>=c`.

For `5/2<c<5`, the member price is therefore `c-1` below `3` and `2` from `3` onward **within this stated class only**. This is not a global equilibrium-uniqueness result.

The bounded Stage-13R2 repair closes the strategy-restriction bridge identified by Astra-2: at a cost-floor-feasible candidate, candidate profits are nonnegative, while any deleted below-cost deviation has `(p_i-mc_i)q_i <= 0` because demand is nonnegative. Astra-2's limited recheck confirmed that this closes the objection.

### 4. Welfare scope

If both union markets use the same symmetric member price `s`,

`TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`,

so the member-country gap remains `1/2`.

If market A and B choose different symmetric continuation prices,

`TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`.

Therefore welfare levels are continuation-selection dependent in the unrestricted game. A common continuation recovers the exact original `1/2` gap; it is not asserted to be necessary for preserving the sign of the welfare comparison.

## Verification

C2R varies all three posted prices and performs global unilateral-deviation falsification in unrestricted and cost-floor modes. Known published and Astra counterexamples are permanent regressions.

The pinned Lean/mathlib project in `GandalShy/Certification.lean` certifies the proof-critical algebraic and quantified-inequality core, including the long-arc correction, exact `c=4` counterexample, global-deviation inequalities, encoded multiplicity, cost-floor logical reduction, and welfare identities. Lean does not claim to reconstruct the entire Salop demand game or all Nash equilibria from primitives.

The bounded Astra-2 repair passed manuscript-integration CI at run `34379361638`. Symbolic/numerical verification, manuscript/package build, final clean LaTeX-log gate, and generated-artifact checks all passed. Astra-2 then limited-rechecked the three requested repairs on `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d` and found no new defect.

## Journal positioning

**Primary target: International Economics, direct short-paper / short-communication route.**

The revised paper is positioned as:

`published claimed continuation fails`
→ `unrestricted symmetric-foreclosed continuations are multiple`
→ `a separate cost-floor game yields the piecewise member-price benchmark within the stated class`
→ `welfare robustness depends on continuation selection`.

Integrated working title:

> **Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)**

Astra-2 assessed publication significance as **MODERATE** and found no remaining scientific blocker after the bounded repair and limited recheck. The principal editorial risk remains publication significance/narrowness.

Author-cost hard gate remains: zero submission fee and zero mandatory standard-route publication/page/APC charge. Stage 14 must recheck the current Guide and authenticated portal before submission.

Fallback ladder remains:

1. International Economics;
2. Journal of Industry, Competition and Trade;
3. Bulletin of Economic Research after current fee/format recheck;
4. Economics Bulletin after current fee/format recheck.

## Recovery route

```text
C0–C1R      [PASS]
   ↓
C2R         [PASS]
   ↓
C2R-L       [PASS]
   ↓
C3R         [PASS]
   ↓
C4R         [PASS]
   ↓
Stage 12R2  [PASS]
   ↓
Stage 13R2  Initial integration [PASS]
   ↓
Astra-2     First pass [MINOR EXPOSITION REPAIR]
   ↓
Stage 13R2  Bounded repair [MERGED / CI PASS]
   ↓
Astra-2     Limited recheck [CLEARED]
   ↓
Stage 14    Submission QA [NEXT]
   ↓
Stage 15    Submission Freeze / Portal Preflight / Submit
```

## Build and verification

Python/symbolic/numerical:

```bash
python -m pip install -r requirements.txt
make verify
```

Lean:

```bash
lake build GandalShy
```

Full integrated package:

```bash
make all
```
