# Gandal-Shy Foreclosure Correction

Research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

> **CURRENT SCIENTIFIC STATUS — 2026-09-09**  
> The pre-Astra Stage-13R manuscript is **not cleared for submission**. An independent Astra referee audit identified a substantive equilibrium-characterization problem: the existing manuscript proves important candidate equilibria but overstates them as a characterization while the unrestricted original price game admits additional zero-sales-outside-price equilibria. **Stage 14 is blocked.**  
> **Next stage:** `C0–C1R — Targeted Equilibrium-Set Reaudit`.

The authoritative project-specific recovery plan is:

- **[`docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`](docs/REVISION_TO_RESUBMISSION_WORKFLOW.md)** — current scientific revision → Lean certification → refreeze → hostile audits → journal recheck → revised manuscript → Astra-2 → Stage 14 → Stage 15.

**Pre-reopening baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`.  
**Provisional journal target:** *International Economics* — short-format route, subject to Stage 12R2 re-evaluation after the revised theory is frozen.  
**Pre-Astra working title:** *Standardization Unions, Foreclosure, and Limit Pricing: Revisiting Gandal and Shy (2001)*.  
**Previous submission:** *Review of Industrial Organization* (RIO), submitted 2026-09-04 (JST) and rejected at editorial screening on 2026-09-09 (JST) before external review.  
**RIO submission ID:** `2d499871-b72e-4168-94c9-e179a47abc8e`.  
**Author-cost hard gate:** zero submission fee and zero mandatory publication/page/APC charge under the standard non-OA route.

## What remains valid after the Astra audit

Direct inspection of the published Gandal and Shy (2001) article confirms that:

- the published model uses quadratic transportation costs;
- Appendix B uses an inconsistent long-arc price-difference coefficient;
- the complete published price profile `(3/2, 3/2, c)` is not a Nash equilibrium in the relevant range;
- the current manuscript's corrected piecewise profile remains an equilibrium candidate, but the unrestricted game also admits additional symmetric foreclosed equilibria when zero-sales below-cost outsider prices are allowed;
- therefore the revision must distinguish **equilibrium existence**, **equilibrium characterization**, and **uniqueness**;
- welfare robustness must be stated for the exact continuation-equilibrium selection under which the price-transfer cancellation holds.

The scientific correction has not been abandoned. The theory has been **reopened** so that the manuscript can state the exact equilibrium set and the exact conditions under which the piecewise member price is characterized.

## Current recovery route

The project now follows this project-specific overlay on `ryotamatsuki/research-paper-workflow` v2.1:

1. **C0–C1R — Targeted Equilibrium-Set Reaudit:** NEXT. Characterize the unrestricted original game within the exact theorem class and separately analyze an explicit cost-floor game `p_i >= mc_i`.
2. **C2R — Symbolic / Numerical Audit:** rebuild falsification so `p_1`, `p_2`, and `p_3` can all vary and preserve the Astra counterexample as a regression test.
3. **C2R-L — Lean Formal Certification:** formalize the settled high-stakes claims before theory freeze, including the long-arc correction, published-profile counterexample, unrestricted multiplicity, cost-floor characterization, and welfare identities.
4. **C3R — Revised Canonical Theory Freeze:** freeze exact games, equilibrium classes, quantifiers, parameter domains, and prohibited stronger claims.
5. **C4R — Hostile Scientific Self-Audit:** attack the revised frozen theory for hidden equilibria, boundary failures, strategy-space errors, and welfare-selection overclaims.
6. **Stage 12R2 — Journal Significance / Fit Recheck:** reassess *International Economics* after the contribution has changed.
7. **Stage 13R2 — Revised Full-Paper Integration:** rewrite Sections 2–4 first, then Abstract/Introduction/Conclusion and submission materials.
8. **Astra-2 — Independent Hostile Referee Gate:** review the complete revised paper before submission QA.
9. **Stage 14 — Submission QA:** only after Astra-2 scientific clearance; refresh all current journal and authenticated-portal requirements under fail-closed rules.
10. **Stage 15 — Submission Freeze / Portal Preflight / Submit:** freeze exact artifacts, reconcile portal metadata, inspect generated PDF, enforce zero-fee gate, submit, and record confirmation.

**Do not skip directly to Stage 14.** The complete stage definitions, pass criteria, return rules, Lean timing, and branch discipline are in [`docs/REVISION_TO_RESUBMISSION_WORKFLOW.md`](docs/REVISION_TO_RESUBMISSION_WORKFLOW.md).

## Pre-Astra Stage 12R/13R provenance

These records remain historical inputs and must not be treated as current scientific clearance:

- `docs/STAGE_12R_INTERNATIONAL_ECONOMICS_POSITIONING.md`
- `docs/JOURNAL_REQUIREMENTS_LEDGER_INTERNATIONAL_ECONOMICS.md`
- `docs/STAGE_13R_INTERNATIONAL_ECONOMICS_INTEGRATION.md`

The pre-Astra Stage-13R manuscript and submission package are retained as a baseline for comparison. They are not the resubmission version.

## Current mathematical agenda

The reopened audit must resolve three questions before refreezing:

1. **Unrestricted original game:** what symmetric foreclosed pure-strategy equilibria exist, and what is nonunique?
2. **Explicit cost-floor game:** under `p_i >= mc_i`, is the member price within symmetric foreclosed pure equilibria characterized by
   - `p_M=c-1` for `5/2<c<3`, and
   - `p_M=2` for `3<=c<5`?
3. **Welfare scope:** for which continuation-equilibrium selection does the Gandal–Shy Proposition-3 member-country ranking survive?

The revision must not describe the cost-floor restriction as “without loss of generality” or as generic elimination of weakly dominated strategies. It changes the strategy set and must be stated as such.

## Lean timing

Lean is deliberately placed **after** analytic equilibrium characterization and the rebuilt falsification audit, but **before** the revised canonical theory freeze:

```text
C0–C1R analytic audit
    ↓
C2R symbolic/numerical falsification
    ↓
C2R-L Lean formal certification
    ↓
C3R revised theory freeze
```

If a later hostile audit changes a theorem's mathematical content or quantifiers, the affected Lean theorem must be updated and rechecked before another freeze.

## Build and verification

The existing commands remain useful for the pre-Astra baseline, but the verification code itself is scheduled for revision at C2R because the old numerical verifier fixed the outsider price at `p_3=c` and therefore could not detect the newly identified equilibrium multiplicity.

```bash
python -m pip install -r requirements.txt
make verify
make pdf
make packages
make title-page
# or
make all
```

Generated outputs are not committed:

- `output/international-economics-manuscript.pdf`
- `output/international-economics-submission-source.zip`
- `output/reproducibility-supplement.zip`
- `output/international-economics-flat/`
- `submission/title_page.pdf`

## RIO submission provenance

- Springer Nature SNAPP accepted the RIO submission on 2026-09-04 (JST).
- Submission ID: `2d499871-b72e-4168-94c9-e179a47abc8e`.
- RIO rejected the manuscript at editorial screening on 2026-09-09 (JST), before external peer review.
- The RIO decision remains provenance only; it is neither mathematical validation nor a substitute for the reopened scientific audit.

## Structure

- `docs/REVISION_TO_RESUBMISSION_WORKFLOW.md` — **authoritative current project route**
- `docs/` — mathematical provenance, RIO records, prior journal-positioning records, Stage-13R audit, and future recovery-stage reports
- `paper/` — modular LaTeX manuscript; current version is the pre-Astra baseline until Stage 13R2
- `code/` — symbolic and numerical verification; scheduled for C2R revision
- `submission/` — pre-Astra International Economics working package; rebuilt after the revised theory is frozen
- `output/` — generated manuscript/package outputs, not committed
