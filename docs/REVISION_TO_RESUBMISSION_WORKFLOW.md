# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-10  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1  
**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`  
**Current execution status:** `C0–C1R PASS` → `C2R PASS` → `C2R-L PASS` → `C3R PASS` → `C4R PASS` → `Stage 12R2 PASS` → **NEXT: `Stage 13R2`**

This file is the authoritative project-specific route from the Astra-1 reopening to a new submission. Stage 14 remains blocked until Stage 13R2 and Astra-2 have passed.

---

## 1. Controlling scientific rules

1. The correction concerns the complete Appendix-B profile `(3/2,3/2,c)`, not a claim that member price `3/2` can never occur.
2. Keep the **unrestricted original price game** and the separate **cost-floor game** `p_i >= marginal cost` distinct. The cost floor is not WLOG, Nash-implied, weak-dominance elimination, or a condition stated by Gandal and Shy (2001).
3. Current equilibrium characterization is limited to **symmetric, foreclosed, pure-strategy price equilibria in one union-member market**.
4. Always distinguish existence, Nash status, characterization within a stated class, and uniqueness within a stated class.
5. The `1/2` welfare gap holds under a common symmetric continuation price. It is not selection-free across arbitrary unrestricted market-by-market continuations.
6. Lean certifies the proof-critical algebraic and quantified-inequality core, not the complete Salop game or all Nash equilibria from primitives.
7. C4R clarification controls all downstream prose: the no-below-cost restriction collapses member-price multiplicity **within symmetric, foreclosed, pure-strategy equilibria**; it is not a global equilibrium-selection result.

Scientific authorities:

- `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`
- `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`
- `docs/C2R_L_LEAN_CERTIFICATION.md`
- `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`
- `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`

---

## 2. Mandatory recovery sequence

```text
C0–C1R  Targeted Equilibrium-Set Reaudit                  [PASS]
   ↓
C2R     Symbolic / Numerical Counterexample Audit         [PASS]
   ↓
C2R-L   Lean Formal Certification                         [PASS]
   ↓
C3R     Revised Canonical Theory Freeze                   [PASS]
   ↓
C4R     Hostile Scientific Self-Audit                     [PASS]
   ↓
Stage 12R2  Journal Significance / Fit Recheck            [PASS]
   ↓
Stage 13R2  Revised Full-Paper Integration                [NEXT]
   ↓
Astra-2     Second Independent Hostile Referee Gate
   ↓
Stage 14   Submission QA
   ↓
Stage 15   Submission Freeze / Portal Preflight / Submit
```

No stage may be skipped merely because an earlier manuscript version once passed a corresponding gate.

---

## 3. Scientific result entering Stage 13R2

### Original published profile

Under quadratic transportation,

`x^L = 1 + (p_2-p_1)/4`.

The complete Appendix-B profile `(3/2,3/2,c)` is not Nash for every strict `c>5/2` in the paper's post-foreclosure range.

### Unrestricted original game

Within symmetric foreclosed pure-strategy profiles `(s,s,r)`:

- **U1:** `3/2 <= s < 2`, `r=s+1`, `c>=s+1`;
- **U2:** `s=2`, `r>=3`, `c>=3`.

Thus the unrestricted game has genuine member-price multiplicity.

### Explicit cost-floor game

Impose `p_i >= marginal cost in that market`.

Within the same symmetric foreclosed pure-strategy class:

- `5/2 <= c < 3`: `(p_1,p_2,p_3)=(c-1,c-1,c)`;
- `c>=3`: `p_1=p_2=2`, with `p_3>=c`.

For the manuscript's strict domain `5/2<c<5`, the member price is `c-1` below `3` and `2` from `3` onward. This is a restricted-class characterization, not global uniqueness.

### Welfare

For common symmetric continuation price `s`:

`TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`, gap `1/2`.

For market-specific symmetric continuation prices:

`TS_A^SU=3V+1/4+(3/2)(s_B-s_A)`.

Hence welfare robustness is continuation-selection conditional in the unrestricted game.

---

## 4. Stage 12R2 — PASS

Authority: `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`

### Journal decision

**Primary target remains `International Economics`, direct short-paper / short-communication route.**

The revised contribution is stronger than at the first Stage 12R because it is now an equilibrium-set and equilibrium-selection correction, not merely a replacement price formula.

Current positioning hierarchy:

1. correction of the published post-foreclosure equilibrium and uniqueness claim;
2. unrestricted symmetric-foreclosed equilibrium multiplicity;
3. conditional piecewise member-price characterization in a separate cost-floor game;
4. continuation-selection dependence of the welfare comparison;
5. zero-sales outsider strategic relevance / static limit-pricing mechanism as supporting interpretation, not the headline.

### Preferred title direction

**`Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)`**

Title wording may be polished at Stage 13R2 after Sections 2–4 are integrated, but `limit pricing` should not return as the primary headline.

### Main editorial risk

The remaining risk is **publication significance / narrowness**, not an unresolved mathematical defect. The paper corrects a 2001 benchmark and does not solve all asymmetric/mixed equilibria or the government stage under unrestricted multiplicity. This risk should be handled by precise short-paper positioning, not by adding a new model extension before submission.

### Zero-fee gate

Submission fee `0` and mandatory standard-route publication/page/APC charge `0` remain hard constraints. Public-page evidence supports continuing with International Economics at Stage 12R2, but Stage 14 must recheck the current Guide and authenticated portal and fail closed if a mandatory charge appears.

Fallback ladder remains:

1. International Economics;
2. Journal of Industry, Competition and Trade;
3. Bulletin of Economic Research after current fee/format recheck;
4. Economics Bulletin after current fee/format recheck.

---

## 5. Stage 13R2 — Revised Full-Paper Integration — NEXT

Begin from the frozen C3R/C4R theory and the Stage-12R2 positioning decision. Do **not** start with the Introduction.

Required order:

1. **Section 2:** published quadratic specification, correct long-arc geometry, exact failure of the published complete profile;
2. **Section 3:** unrestricted U1/U2 multiplicity first, then the separate cost-floor F1/F2 characterization;
3. **Section 4:** welfare under common versus market-specific continuation selection;
4. only after Sections 2–4 are stable: title, Abstract, Introduction, Conclusion, keywords/JEL, highlights, cover letter, title page and other submission materials.

Mandatory writing rules:

- put multiplicity in the main text;
- state the equilibrium class in Proposition 1 itself;
- introduce the cost-floor game visibly as a separate strategy space before stating its result;
- never call the cost-floor result global equilibrium uniqueness;
- never imply asymmetric or mixed equilibria are characterized;
- do not say member price `3/2` can never occur;
- do not call the cost floor WLOG, Nash-implied, or a weak-dominance refinement;
- at `c=3`, describe a branch boundary, not strict slack;
- use `limit pricing` only as a supporting static exclusion-maintenance interpretation;
- state Lean certification only at its actual scope;
- do not add a theoretical extension solely for journal fit.

Stage 13R2 must exit with:

`REVISED INTEGRATED MANUSCRIPT READY FOR ASTRA-2`

or return to the earliest affected scientific stage if integration reveals a true inconsistency.

---

## 6. Astra-2 — mandatory after Stage 13R2

Astra-2 is the final independent scientific gate before submission QA. It must attack the complete revised manuscript for:

- original-paper correction validity;
- unrestricted U1/U2 characterization;
- cost-floor F1/F2 scope;
- existence/characterization/uniqueness drift;
- asymmetric/mixed-equilibrium scope leakage;
- welfare-selection overclaim;
- limit-pricing terminology;
- Lean-certification scope;
- publication significance for International Economics.

Proceed only on `ACCEPTABLE FOR SUBMISSION` or after bounded repair of `MINOR EXPOSITION REPAIR`.

A substantive mathematical problem returns to the earliest affected scientific stage.

---

## 7. Stage 14 — Submission QA

Begin only after Astra-2 clearance. Refresh current official journal and authenticated-portal requirements. Any material `UNVERIFIED` or unresolved `CONFLICT` blocks PASS.

Mandatory checks include article type, anonymity/title-page rules, editable sources/LaTeX packaging, abstract/keywords/JEL/highlights, funding/competing interests/CRediT/AI declaration, data/code handling, reviewer fields, fees and charges, and portal-generated PDF behavior.

---

## 8. Stage 15 — Submission Freeze / Portal Preflight / Submit

Only after Stage 14 passes:

1. freeze exact artifacts and record commit/tag/SHA;
2. reconcile portal metadata;
3. upload the exact frozen files;
4. generate and inspect the portal PDF where available;
5. recheck equations, citations, identity/anonymity, declarations and supplements;
6. confirm the zero-fee hard gate;
7. submit;
8. record journal confirmation and submission ID.

Do not declare `SUBMITTED` before journal confirmation is received.

---

## 9. Return rules

| New problem | Return to |
|---|---|
| New equilibrium counterexample / false theorem | C0–C1R |
| Falsification code misses a material strategy region | C2R |
| Mathematical quantifier or Lean-certified theorem changes | analytic repair, then C2R-L |
| Freeze wording exceeds valid theory only | C3R/C4R clarification |
| Journal significance/fit issue only | Stage 12R2 |
| Exposition/organization issue only | Stage 13R2 |
| Astra-2 finds mathematical defect | earliest affected C-stage |
| Submission-format/metadata issue only | Stage 14 |
| Portal-only mismatch | Stage 14/15 preflight |

---

## 10. Current checklist

- [x] RIO editorial audience-fit rejection recorded.
- [x] Initial International Economics Stage 12R positioning.
- [x] Initial Stage 13R integration.
- [x] Astra-1 scientific defect discovery.
- [x] C0–C1R targeted equilibrium-set reaudit.
- [x] C2R symbolic/numerical audit.
- [x] C2R-L Lean certification.
- [x] C3R revised theory freeze.
- [x] C4R hostile scientific self-audit.
- [x] **Stage 12R2 journal significance/fit recheck.**
- [ ] **Stage 13R2 revised full-paper integration — NEXT.**
- [ ] Astra-2 independent hostile referee gate.
- [ ] Stage 14 submission QA.
- [ ] Stage 15 submission freeze / portal preflight / submit.
