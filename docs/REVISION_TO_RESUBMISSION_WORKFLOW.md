# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-10  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1 plus merged post-v2.1 Formal Verification Gate refinement (`main@f48984013898696f010f0437a8cfed6b5b54bdc2`)  
**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`  
**Current execution status:** `C0–C1R PASS` → `C2R PASS` → `C2R-L PASS` → `C3R PASS` → `C4R PASS` → `Stage 12R2 PASS` → `Stage 13R2 PASS` → `Astra-2 CLEARED` → `Stage 14 CONDITIONAL PASS` → **NEXT: `Stage 15 Submission Freeze / Authenticated Portal Preflight`**

This file is the authoritative project-specific route from the Astra-1 reopening to a new submission.

---

## 1. Controlling scientific rules

1. The correction concerns the complete Appendix-B profile `(3/2,3/2,c)`, not a claim that member price `3/2` can never occur.
2. Keep the **unrestricted original price game** and the separate **cost-floor game** `p_i >= marginal cost` distinct. The cost floor is not WLOG, Nash-implied, weak-dominance elimination, or a condition stated by Gandal and Shy (2001).
3. Current equilibrium characterization is limited to **symmetric, foreclosed, pure-strategy price equilibria in one union-member market**.
4. Always distinguish existence, Nash status, characterization within a stated class, and uniqueness within a stated class.
5. The `1/2` welfare gap holds under a common symmetric continuation price. It is not selection-free across arbitrary unrestricted market-by-market continuations, and a common price is not claimed to be necessary for preserving the welfare ranking.
6. Lean certifies the proof-critical algebraic and quantified-inequality core, not the complete Salop game or all Nash equilibria from primitives.
7. C4R clarification controls downstream prose: the no-below-cost restriction collapses member-price multiplicity **within symmetric, foreclosed, pure-strategy equilibria**; it is not a global equilibrium-selection result.
8. Astra-2 clarification controls the cost-floor proof: deleted below-cost deviations cannot create additional restricted-game equilibria in the stated class because candidate profits are nonnegative while any deleted deviation yields nonpositive profit.
9. The generic Formal Verification Gate now also governs this bespoke recovery route. Because this project already has C2R-L, the relevant formal state is `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE`. Stage 14 rebuilt that frozen Lean artifact and reran the admitted-proof gate.

Scientific authorities:

- `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`
- `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`
- `docs/C2R_L_LEAN_CERTIFICATION.md`
- `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`
- `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`
- `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`
- `docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md`
- `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`
- `docs/STAGE_14_SUBMISSION_QA.md`

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
Stage 13R2  Revised Full-Paper Integration                [PASS]
   ↓
Astra-2     Independent Hostile Referee Gate              [CLEARED]
   ↓
Stage 14    Submission QA                                 [CONDITIONAL PASS]
   ↓
Stage 15    Submission Freeze / Authenticated Preflight   [NEXT]
```

No stage may be skipped merely because an earlier manuscript version once passed a corresponding gate.

---

## 3. Frozen scientific result

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

For `5/2<c<5`, the member price is `c-1` below `3` and `2` from `3` onward. This is a restricted-class characterization, not global uniqueness.

### Welfare

For common symmetric continuation price `s`:

`TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`, gap `1/2`.

For market-specific symmetric continuation prices:

`TS_A^SU=3V+1/4+(3/2)(s_B-s_A)`.

Hence welfare levels are continuation-selection dependent in the unrestricted game. The common-price condition recovers the exact original `1/2` gap; it is not claimed to be necessary for preserving the sign of the welfare comparison.

---

## 4. Journal decision carried forward

**Primary target: `International Economics`, direct short-paper / short-communication route.**

Current positioning hierarchy:

1. correction of the published post-foreclosure equilibrium and uniqueness claim;
2. unrestricted symmetric-foreclosed equilibrium multiplicity;
3. conditional piecewise member-price characterization in a separate cost-floor game;
4. continuation-selection dependence of the welfare comparison;
5. zero-sales outsider strategic relevance / static limit-pricing mechanism as supporting interpretation, not the headline.

Integrated title:

**`Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)`**

Astra-2 assessed publication significance as **MODERATE**. No scientific blocker remains. The principal remaining editorial risk is publication significance/narrowness.

---

## 5. Astra-2 — CLOSED

Astra-2 first audited `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6` and returned `B. MINOR EXPOSITION REPAIR` with exactly three bounded repairs: the cost-floor strategy-restriction bridge, highlight scope, and cover-letter welfare wording.

Those repairs were implemented and merged. Astra-2 then limited-rechecked `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d` and returned:

- Repair 1 — PASS;
- Repair 2 — PASS;
- Repair 3 — PASS;
- new defect — NO;
- final verdict — `A. ASTRA-2 CLEARED — GO TO STAGE 14`.

No further hostile-referee cycle is required unless a later stage changes or contradicts the scientific content.

---

## 6. Stage 14 — CONDITIONAL PASS

Stage-14 branch: `stage14/submission-qa`  
Stage-14 PR: `#17`  
Scientific entry baseline: `main@9f1839a941470a411e6236f9d6848e352dc44490`

Stage 14 refreshed journal requirements, created the journal-requirements ledger and authenticated portal checklist, synchronized CRediT/AI/declaration material, built a flat Elsevier-compatible LaTeX source archive, and added Python package QA.

After the generic Formal Verification Gate was merged into `research-paper-workflow`, the Stage-14 workflow was strengthened further to rebuild the frozen Lean target and reject admitted proofs before the usual verification/build checks.

Final strengthened Stage-14 CI:

- head: `a227b461fcf7287c27456c2697454334fce550dd`;
- workflow run: `34425158086`;
- result: **SUCCESS**;
- Lean rebuild: PASS;
- `sorry` / `admit` gate: PASS;
- symbolic/numerical verification: PASS;
- manuscript/package build: PASS;
- Python Stage-14 audit: PASS;
- clean final LaTeX logs: PASS;
- generated artifacts: PASS.

Automated diagnostics:

- abstract: 201 words;
- keywords: 6;
- highlights: 4, character counts 73 / 75 / 82 / 72;
- manuscript: 9 pages;
- flat source archive: 8 files with no subdirectories.

The ordinary manuscript PDF and the flat-source rebuild were rendered at 180 dpi and compared page by page: **9/9 pages identical, 0 changed pages**. The 9-page manuscript and 1-page title page were also visually inspected and passed.

No scientific or Lean-theorem change was introduced.

### Stage-14 canonical verdict

`CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.

The remaining blockers are genuinely portal-specific and cannot be guessed:

- exact article-type label (`Short paper` / `Short communication` as exposed by the live system);
- review/anonymity and title-page configuration;
- upload item designations;
- portal metadata, classifications, attestations and declaration fields;
- portal-generated PDF;
- submission fee hard gate;
- mandatory standard-route publication/page/APC hard gate.

The zero-cost rule remains:

- submission fee = 0;
- mandatory standard subscription-route publication/page/APC charge = 0.

Any mandatory charge blocks submission.

---

## 7. Stage 15 — NEXT

Stage 15 is the next active stage. Its contract is:

1. freeze the exact Stage-14-approved repository state and artifact set;
2. preserve manuscript/source/reproducibility/Lean/build provenance;
3. open and reconcile the authenticated Editorial Manager record;
4. resolve every item in `submission/PORTAL_PREFLIGHT_CHECKLIST.md`;
5. upload only the frozen artifacts or a bounded Stage-14 compliance-only descendant;
6. inspect the portal-generated PDF page by page;
7. confirm both zero-cost hard gates;
8. submit only after every material portal item is PASS;
9. record journal confirmation and submission ID before declaring `SUBMITTED`.

A bounded anonymity/file-designation/declaration-placement repair returns to Stage 14 and requires fresh affected QA. Any theorem/model/result/interpretation change returns to the earliest affected scientific stage.

---

## 8. Return rules

| New problem | Return to |
|---|---|
| New equilibrium counterexample / false theorem | C0–C1R |
| Falsification code misses a material strategy region | C2R |
| Mathematical quantifier or Lean-certified theorem changes | analytic repair, then C2R-L / formal recertification |
| Freeze wording exceeds valid theory only | C3R/C4R clarification |
| Journal significance/fit issue only | Stage 12R2 |
| Exposition/organization issue only | Stage 13R2 |
| Submission-format/metadata issue only | Stage 14 |
| Formal build/statement mapping defect with unchanged mathematics | formal-verification repair, then affected QA |
| Stage-14/15 change introduces a scientific issue | earliest affected scientific stage |
| Portal-only mismatch | Stage 14/15 preflight |

---

## 9. Current checklist

- [x] RIO editorial audience-fit rejection recorded.
- [x] C0–C1R targeted equilibrium-set reaudit.
- [x] C2R symbolic/numerical audit.
- [x] C2R-L Lean certification.
- [x] C3R revised theory freeze.
- [x] C4R hostile scientific self-audit.
- [x] Stage 12R2 journal significance/fit recheck.
- [x] Stage 13R2 revised full-paper integration.
- [x] Astra-2 hostile referee gate and bounded recheck.
- [x] Stage 14 submission QA — `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.
- [ ] **Stage 15 submission freeze / authenticated portal preflight — NEXT.**
- [ ] Final submit and journal confirmation.
