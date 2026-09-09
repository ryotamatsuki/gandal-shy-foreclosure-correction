# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-09  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1  
**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`  
**Current execution status:** `C0–C1R PASS` → `C2R PASS` → `C2R-L PASS` → `C3R PASS` → `C4R PASS` → **NEXT: `Stage 12R2`**

This file is the authoritative project-specific route from the Astra-1 scientific reopening to a new submission. Stage 14 remains blocked until Stage 12R2, Stage 13R2, and Astra-2 have passed.

---

## 1. Governing scientific rules

### 1.1 Correction target

The correction concerns the complete Appendix-B price profile claimed by Gandal and Shy (2001), not the isolated proposition that member price `3/2` can never occur.

Permitted statement:

> Appendix B's claimed profile `(3/2,3/2,c)` is not a Nash equilibrium under the published quadratic-transport specification in the strict post-foreclosure range.

Prohibited statement:

> Member price `3/2` cannot occur in equilibrium.

### 1.2 Keep two price games separate

1. **Unrestricted original game:** price strategies as stated in the published model, including zero-sales below-cost outsider quotes when not explicitly excluded.
2. **Cost-floor game:** explicit modified strategy set `p_i >= marginal cost in that market`.

The cost floor is not WLOG, is not implied by Nash equilibrium, is not generic weak-dominance elimination, and is not attributed to the published paper.

### 1.3 Exact equilibrium class

The current characterization is limited to:

> **symmetric, foreclosed, pure-strategy price equilibria in one union-member market.**

No current theorem characterizes all asymmetric pure equilibria, mixed equilibria, or the government-stage equilibrium under continuation multiplicity.

### 1.4 Logical strength

Always distinguish:

- existence;
- Nash equilibrium status;
- characterization within a stated class;
- uniqueness within a stated class.

Never upgrade an existence proof into characterization or a restricted-class characterization into global uniqueness.

### 1.5 Welfare scope

The `1/2` welfare gap is valid under a common symmetric continuation price across the two union markets. It is not selection-free across arbitrary market-by-market continuations in the unrestricted game.

Do not claim that Proposition 3 reverses without solving the relevant government-stage equilibrium/selection problem.

### 1.6 Lean scope

Lean certifies the proof-critical algebraic and quantified-inequality core. It does not independently reconstruct the entire continuum Salop demand game or all Nash equilibria from consumer primitives.

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
Stage 12R2  Journal Significance / Fit Recheck            [NEXT]
   ↓
Stage 13R2  Revised Full-Paper Integration
   ↓
Astra-2     Second Independent Hostile Referee Gate
   ↓
Stage 14   Submission QA
   ↓
Stage 15   Submission Freeze / Portal Preflight / Submit
```

No stage may be skipped merely because an earlier manuscript version once passed a corresponding gate.

---

## 3. Scientific recovery already completed

### C0–C1R — PASS

Authority: `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`

Frozen analytic results:

- long-arc coefficient `1/4` under quadratic transportation;
- published profile `(3/2,3/2,c)` is non-Nash in the strict post-foreclosure range;
- unrestricted symmetric foreclosed pure equilibria:
  - U1: `3/2 <= s < 2`, `r=s+1`, `c>=s+1`;
  - U2: `s=2`, `r>=3`, `c>=3`;
- cost-floor symmetric foreclosed pure equilibria:
  - F1: `5/2 <= c < 3`, `(c-1,c-1,c)`;
  - F2: `c>=3`, member prices `(2,2)`, outsider quote `r>=c`;
- common-price welfare `TS_M^SU=3V+1/4`;
- market-specific welfare `TS_A^SU=3V+1/4+(3/2)(s_B-s_A)`.

### C2R — PASS

Authority: `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`

The verifier now varies all three posted prices, uses unrestricted and cost-floor modes, searches global unilateral deviations from primitive delivered-price thresholds, retains the published and Astra counterexamples as regressions, and treats numerics as falsification rather than proof of completeness.

### C2R-L — PASS

Authority: `docs/C2R_L_LEAN_CERTIFICATION.md`  
Formal source: `GandalShy/Certification.lean`

Lean certifies the long-arc algebra, exact `c=4` counterexample, global-deviation inequality core, necessity signs, encoded multiplicity, cost-floor logical reduction, and welfare identities. GitHub Actions run `34291397450` passed `lake build GandalShy` and the admitted-proof scan.

### C3R — PASS

Authority: `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`

C3R freezes the exact game definitions, parameter domain, equilibrium class, U1/U2 and F1/F2 claims, welfare-selection scope, boundary treatment, permitted limit-pricing terminology, Lean scope, and prohibited stronger claims.

### C4R — PASS

Authority: `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`

C4R attacked:

- the full `c>5/2` quantifier on the published-profile failure;
- hidden outsider-price equilibria and below-cost zero-sales quotes;
- global member deviations and demand-region leakage;
- the cost-floor/original-game distinction;
- `c=5/2` and `c=3` boundaries;
- tie-breaking and zero-measure consumers;
- asymmetric/mixed-equilibrium scope;
- welfare continuation selection;
- limit-pricing terminology;
- Lean-scope drift.

No counterexample was found inside the exact C3R theorem class.

C4R adds one controlling wording clarification:

> **Within symmetric, foreclosed, pure-strategy equilibria, an explicit no-below-cost price restriction collapses the unrestricted member-price multiplicity to the piecewise member-price formula.**

Do not shorten this into a global claim that the cost floor "restores uniqueness" or "selects the equilibrium".

---

## 4. Stage 12R2 — Journal Significance / Fit Recheck — NEXT

### Objective

Reassess from scratch whether the revised scientific contribution clears the publication threshold of *International Economics* and whether that journal remains the best zero-fee target.

The contribution entering Stage 12R2 is now:

`published claimed equilibrium profile is false`
→ `unrestricted game has symmetric-foreclosed equilibrium multiplicity`
→ `explicit cost-floor restriction characterizes member prices only within the stated symmetric class`
→ `welfare robustness is continuation-selection conditional`.

### Mandatory questions

1. Is this more than an algebraic corrigendum?
2. Does equilibrium multiplicity/selection create a sufficiently meaningful international-economics contribution?
3. Does stopping at the symmetric foreclosed pure-strategy class create an editorial objection?
4. Is the explicit cost-floor modification useful enough to retain as a main result?
5. Should the paper emphasize correction, multiplicity, equilibrium selection, or limit pricing in its title and positioning?
6. Does *International Economics* remain the best fit under the zero-fee hard gate?

### Required outputs

- updated contribution statement;
- strongest acceptance argument;
- strongest desk-reject argument;
- updated *International Economics* fit assessment;
- revised title direction;
- zero-fee target ladder if needed;
- verdict: `GO TO STAGE 13R2`, `REPOSITION`, or `CHANGE JOURNAL TARGET`.

Do not rewrite the manuscript at Stage 12R2.

---

## 5. Stage 13R2 — Revised Full-Paper Integration

Begin only after Stage 12R2 gives a target/positioning decision.

Revise in this order:

1. Section 2 — published quadratic specification, long-arc error, exact failure of the published complete profile;
2. Section 3 — unrestricted U1/U2 multiplicity first, then the separate cost-floor F1/F2 characterization;
3. Section 4 — welfare under common versus market-specific continuation selection;
4. only then Abstract, Introduction, Conclusion, title, keywords/JEL, highlights, cover letter, and submission materials.

Mandatory writing rules:

- multiplicity stays in the main text;
- the cost floor must visibly appear as a separate modified strategy set before its result;
- always qualify the cost-floor characterization by the symmetric, foreclosed, pure-strategy class;
- do not write "the equilibrium price" where only a restricted-class characterization is proved;
- at `c=3`, describe a branch boundary, not strict slack;
- use "limit pricing" only in the static exclusion-maintenance sense authorized by C3R/C4R;
- describe Lean only at its actual certification scope.

---

## 6. Astra-2 — Second Independent Hostile Referee Gate

Run only after the complete Stage-13R2 manuscript exists.

Astra-2 must independently attack:

- published-profile correction validity;
- unrestricted U1/U2 characterization;
- cost-floor F1/F2 scope and necessity;
- existence/characterization/uniqueness wording;
- asymmetric/mixed-equilibrium scope leakage;
- welfare-selection scope;
- limit-pricing terminology;
- Lean-certification scope;
- publication significance for the selected journal.

Proceed only on:

- `ACCEPTABLE FOR SUBMISSION`; or
- `MINOR EXPOSITION REPAIR`, after bounded repair and recheck.

A substantive theory defect returns to the earliest affected scientific stage.

---

## 7. Stage 14 — Submission QA

Begin only after Astra-2 scientific clearance.

Refresh current official journal and authenticated-portal requirements. Any material `UNVERIFIED` or unresolved `CONFLICT` blocks PASS.

Mandatory checks include:

- exact article type;
- anonymity/title-page rules;
- editable source and LaTeX packaging;
- abstract, keywords, JEL, highlights;
- funding, competing interests, CRediT, generative-AI declaration;
- data/code/supplement requirements;
- reviewer fields and attestations;
- submission fee and mandatory publication/page/color charges;
- portal-generated PDF behavior.

**Zero-fee hard gate:** submission fee `0` and mandatory standard-route publication/page/APC charge `0`. If violated, stop and move to the next verified zero-fee journal.

---

## 8. Stage 15 — Submission Freeze / Portal Preflight / Submit

Only after Stage 14 passes:

1. freeze exact manuscript and submission artifacts;
2. record commit/tag/SHA provenance;
3. reconcile portal metadata with the frozen source;
4. upload exact frozen files;
5. generate the portal PDF where available;
6. inspect the generated PDF page by page;
7. verify equations, citations, author/anonymity information, declarations, and supplements;
8. confirm the zero-fee hard gate;
9. submit;
10. record journal confirmation and submission ID.

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

Do not repair a scientific defect only in prose when the theorem or quantifier must change.

---

## 10. Current checklist

- [x] RIO submission closed with editorial audience-fit rejection.
- [x] Initial International Economics Stage 12R positioning completed.
- [x] Initial Stage 13R integration completed.
- [x] Astra-1 identified the equilibrium-characterization defect.
- [x] Published Gandal–Shy (2001) PDF directly checked.
- [x] Stage 14 halted.
- [x] C0–C1R Targeted Equilibrium-Set Reaudit.
- [x] C2R Symbolic/Numerical Audit.
- [x] C2R-L Lean Formal Certification.
- [x] C3R Revised Canonical Theory Freeze.
- [x] C4R Hostile Scientific Self-Audit.
- [ ] **Stage 12R2 Journal Significance/Fit Recheck — NEXT.**
- [ ] Stage 13R2 Revised Full-Paper Integration.
- [ ] Astra-2 Independent Hostile Referee Gate.
- [ ] Stage 14 Submission QA.
- [ ] Stage 15 Submission Freeze / Portal Preflight / Submit.

---

## 11. Definition of recovery success

The project is ready for submission QA only when it can answer without qualification drift:

1. exactly which published profile is false and why;
2. exactly what symmetric foreclosed pure equilibria exist in the unrestricted original game;
3. exactly what the explicit cost-floor restriction does and does not select;
4. exactly when the member-country welfare gap remains `1/2`;
5. exactly what Lean certifies and what remains analytic;
6. why the revised contribution is publishable in the selected journal;
7. whether Astra-2 finds any remaining substantive defect.

The goal is not to erase the Astra counterexample. The goal is to make the counterexample, the resulting multiplicity, and the exact limits of every correction claim part of the paper's reproducible scientific record.