# Gandal-Shy Foreclosure Correction

Research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

> **CURRENT STATUS — 2026-09-10**  
> `C0–C1R`: **PASS**  
> `C2R`: **PASS**  
> `C2R-L Lean`: **PASS**  
> `C3R Revised Canonical Theory Freeze`: **PASS**  
> `C4R Hostile Scientific Self-Audit`: **PASS**  
> `Stage 6R Final-Proposition Novelty Re-Kill`: **PASS**  
> `Stage 12R2 Journal Significance / Fit Recheck`: **PASS**  
> `Stage 13R2 Revised Full-Paper Integration`: **PASS**  
> `Astra-2`: **CLEARED**  
> `Stage 14 Submission QA`: **CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**  
> `Stage 15`: **SUBMITTED — AUTHENTICATED PORTAL CONFIRMATION VERIFIED; SUBMISSION ID PENDING**.

The Elsevier portal confirmed submission to **International Economics** as a **Short Paper** at **23:54, September 10, 2026**. The confirmation page lists Ryota Matsuki as the corresponding author and Independent Researcher as the affiliation. The journal-generated submission/manuscript ID is not shown on that confirmation page and remains pending the confirmation email/tracking record.

Authoritative records:

- [`docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`](docs/REVISION_TO_RESUBMISSION_WORKFLOW.md)
- [`docs/ROUTE_CERTIFICATION_INHERITANCE_AND_REGRESSION.md`](docs/ROUTE_CERTIFICATION_INHERITANCE_AND_REGRESSION.md)
- [`docs/STAGE_06R_FINAL_PROPOSITION_NOVELTY_REKILL.md`](docs/STAGE_06R_FINAL_PROPOSITION_NOVELTY_REKILL.md)
- [`docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`](docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md)
- [`docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`](docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md)
- [`docs/C2R_L_LEAN_CERTIFICATION.md`](docs/C2R_L_LEAN_CERTIFICATION.md)
- [`docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`](docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md)
- [`docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`](docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md)
- [`docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`](docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md)
- [`docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md`](docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md)
- [`docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`](docs/ASTRA_2_HOSTILE_REFEREE_GATE.md)
- [`docs/STAGE_14_SUBMISSION_QA.md`](docs/STAGE_14_SUBMISSION_QA.md)
- [`docs/JOURNAL_REQUIREMENTS_LEDGER.md`](docs/JOURNAL_REQUIREMENTS_LEDGER.md)
- [`docs/STAGE_15_SUBMISSION_FREEZE.md`](docs/STAGE_15_SUBMISSION_FREEZE.md)

## Frozen scientific result

### Published profile

The published model uses quadratic transportation cost. On the long arc,

`x^L = 1 + (p_2-p_1)/4`,

not the coefficient used in Appendix B. The complete published profile `(3/2,3/2,c)` is not Nash for every strict `c>5/2` in the paper's post-foreclosure range.

The correction concerns the complete profile and associated equilibrium/uniqueness claim. It is **not** a claim that member price `3/2` can never occur in another equilibrium.

### Unrestricted original game

Within **symmetric, foreclosed, pure-strategy profiles** `(s,s,r)`, the unrestricted equilibrium set is:

- `3/2 <= s < 2`, `r=s+1`, `c>=s+1`; or
- `s=2`, `r>=3`, `c>=3`.

Thus the original game has genuine member-price multiplicity.

### Explicit cost-floor game

Define a separate restricted game with `p_i >= marginal cost in that market`.

Within the same symmetric, foreclosed, pure-strategy class:

- `5/2 <= c < 3`: `(p_1,p_2,p_3)=(c-1,c-1,c)`;
- `c>=3`: `p_1=p_2=2`, with `p_3>=c`.

For `5/2<c<5`, the member price is `c-1` below `3` and `2` from `3` onward **within this stated class only**. This is not a global equilibrium-uniqueness result.

### Welfare scope

If both union markets use the same symmetric member price `s`,

`TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`,

so the member-country gap remains `1/2`.

If market A and B choose different symmetric continuation prices,

`TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`.

Therefore welfare levels are continuation-selection dependent in the unrestricted game. A common continuation recovers the exact original `1/2` gap; it is not asserted to be necessary for preserving the sign of the welfare comparison.

## Verification

C2R varies all three posted prices and performs global unilateral-deviation falsification in unrestricted and cost-floor modes. Known published and Astra counterexamples are permanent regressions.

The pinned Lean/mathlib project in `GandalShy/Certification.lean` certifies the proof-critical algebraic and quantified-inequality core, including the long-arc correction, exact `c=4` counterexample, global-deviation inequalities, encoded multiplicity, cost-floor logical reduction, and welfare identities. Lean does not claim to reconstruct the entire Salop demand game or all Nash equilibria from primitives.

The bespoke recovery route is mapped back to the canonical workflow through `docs/ROUTE_CERTIFICATION_INHERITANCE_AND_REGRESSION.md`. Stage 6R re-killed novelty using the final Proposition 1/2 set and found no located prior source that already states the combined correction package.

The canonical final technical Stage-14 CI was `34425892795` on head `9634ee92beb650db03bb9b89db6195b2ddf44278`, which passed Lean rebuild, admitted-proof rejection, symbolic/numerical verification, manuscript/package build, Python package audit, clean LaTeX-log gate, and artifact checks. The Stage-15 ancillary compliance changes subsequently passed the submission-QA workflow again (`34487836179` — SUCCESS).

## Journal submission

**Journal:** International Economics  
**Article type:** Short Paper  
**Title:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Submitted:** 23:54, September 10, 2026  
**Author:** Ryota Matsuki  
**Corresponding author:** Ryota Matsuki  
**Affiliation:** Independent Researcher  
**Publication route:** subscription  
**Submission ID:** pending confirmation email/tracking record

The authenticated Elsevier terminal page states `Your manuscript has now been submitted` and confirms that the manuscript and other files were sent to *International Economics*.

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
Stage 6R    [PASS — FINAL-PROPOSITION NOVELTY RE-KILL BACKFILL]
   ↓
Stage 12R2  [PASS]
   ↓
Stage 13R2  [PASS]
   ↓
Astra-2     [CLEARED]
   ↓
Stage 14    [CONDITIONAL PASS]
   ↓
Stage 15    [SUBMITTED — PORTAL CONFIRMED; SUBMISSION ID PENDING]
```

Final route closure occurs when the Elsevier manuscript/submission ID is recorded from the confirmation email or tracking record.

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
