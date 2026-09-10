# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-10  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1 plus merged post-v2.1 Formal Verification Gate refinement (`main@f48984013898696f010f0437a8cfed6b5b54bdc2`)  
**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`  
**Current execution status:** `C0–C1R PASS` → `C2R PASS` → `C2R-L PASS` → `C3R PASS` → `C4R PASS` → `Stage 6R PASS (backfill)` → `Stage 12R2 PASS` → `Stage 13R2 PASS` → `Astra-2 CLEARED` → `Stage 14 CONDITIONAL PASS` → **ACTIVE: `Stage 15 Submission Freeze / Authenticated Portal Preflight`**

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
10. The bespoke route inherits canonical certification obligations through `docs/ROUTE_CERTIFICATION_INHERITANCE_AND_REGRESSION.md`; route labels do not waive candidate-vs-characterization, multiplicity/indifference, welfare-selection, theorem-scope, formal-verification, or evidence-bearing PASS requirements.
11. Final-proposition novelty has been re-killed in `docs/STAGE_06R_FINAL_PROPOSITION_NOVELTY_REKILL.md`. No located source absorbs the final correction package; this remains a bounded search conclusion rather than a proof of global absence.

Scientific authorities:

- `docs/ROUTE_CERTIFICATION_INHERITANCE_AND_REGRESSION.md`
- `docs/STAGE_06R_FINAL_PROPOSITION_NOVELTY_REKILL.md`
- `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`
- `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`
- `docs/C2R_L_LEAN_CERTIFICATION.md`
- `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`
- `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`
- `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`
- `docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md`
- `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`
- `docs/STAGE_14_SUBMISSION_QA.md`
- `docs/STAGE_15_SUBMISSION_FREEZE.md`

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
Stage 6R    Final-Proposition Novelty Re-Kill             [PASS — BACKFILLED]
   ↓
Stage 12R2  Journal Significance / Fit Recheck            [PASS]
   ↓
Stage 13R2  Revised Full-Paper Integration                [PASS]
   ↓
Astra-2     Independent Hostile Referee Gate              [CLEARED]
   ↓
Stage 14    Submission QA                                 [CONDITIONAL PASS]
   ↓
Stage 15    Submission Freeze / Authenticated Preflight   [ACTIVE]
```

Stage 6R is shown at the point where its canonical obligation logically belongs. It was executed as a bounded backfill during Stage 15 and changed no theory or manuscript claim.

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

## 4. Certification inheritance and regressions

The route-certification mapping is now explicit in `docs/ROUTE_CERTIFICATION_INHERITANCE_AND_REGRESSION.md`.

The three material process regressions retained as permanent workflow evidence are:

1. **candidate-versus-characterization regression:** fixing `p_3=c` verified a preferred candidate but missed alternative zero-sales outsider quotes and member-price multiplicity;
2. **cost-floor intersection regression:** a strategy restriction was intersected with the unrestricted set before explicitly proving that deleted below-cost deviations cannot create new restricted equilibria;
3. **Astra bookkeeping regression:** clearance was briefly recorded before an actual limited recheck existed, then reverted and closed only after the real recheck.

All three are closed, with permanent tests or records. No strong current scientific claim sits behind a material `NOT TESTED` item.

---

## 5. Stage 6R — FINAL-PROPOSITION NOVELTY RE-KILL

Stage 6R was executed as a bounded backfill against the final Proposition 1/2 set after the workflow cross-check identified that the earlier prior-art work had not been packaged as a canonical final-proposition re-kill.

Fresh targeted searches covered:

- the exact Gandal–Shy title plus `erratum` / `corrigendum` / correction terms;
- the published-profile `3/2` continuation;
- U1/U2 / equilibrium multiplicity in standardization unions;
- zero-sales / below-cost outsider support;
- the explicit `c-1` / `2` cost-floor benchmark;
- market-specific welfare continuation selection and the cross-market transfer term.

No located source states the present correction package or absorbs the final propositions. The original 2001 paper remains the exact source being corrected; the 1996 working-paper genealogy and later standards/trade work are related but non-absorptive.

**Verdict:** `GO — FINAL PROPOSITION SET SURVIVES NOVELTY RE-KILL`.

The strongest residual novelty threat remains editorial significance/narrowness, not identified exact prior art.

---

## 6. Journal decision carried forward

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

## 7. Astra-2 — CLOSED

Astra-2 first audited `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6` and returned `B. MINOR EXPOSITION REPAIR` with exactly three bounded repairs: the cost-floor strategy-restriction bridge, highlight scope, and cover-letter welfare wording.

Those repairs were implemented and merged. Astra-2 then limited-rechecked `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d` and returned:

- Repair 1 — PASS;
- Repair 2 — PASS;
- Repair 3 — PASS;
- new defect — NO;
- final verdict — `A. ASTRA-2 CLEARED — GO TO STAGE 14`.

No further hostile-referee cycle is required unless a later stage changes or contradicts the scientific content.

---

## 8. Stage 14 — CONDITIONAL PASS

Stage-14 branch: `stage14/submission-qa`  
Stage-14 PR: `#17`  
Scientific entry baseline: `main@9f1839a941470a411e6236f9d6848e352dc44490`

Stage 14 refreshed journal requirements, created the journal-requirements ledger and authenticated portal checklist, synchronized CRediT/AI/declaration material, built a flat Elsevier-compatible LaTeX source archive, and added Python package QA.

After the generic Formal Verification Gate was merged into `research-paper-workflow`, the Stage-14 workflow was strengthened further to rebuild the frozen Lean target and reject admitted proofs before the usual verification/build checks.

**Canonical final technical Stage-14 CI:**

- head: `9634ee92beb650db03bb9b89db6195b2ddf44278`;
- workflow run: `34425892795`;
- result: **SUCCESS**;
- artifact: `stage14-build`, ID `10132717858`;
- artifact digest: `sha256:0de9fc0daf05bd98a1bb2394082dded547a7cc54b07d44fca4419b8e8c2f9313`;
- Lean rebuild: PASS;
- `sorry` / `admit` gate: PASS;
- symbolic/numerical verification: PASS;
- manuscript/package build: PASS;
- Python Stage-14 audit: PASS;
- clean final LaTeX logs: PASS;
- generated artifacts: PASS.

The earlier successful strengthened run `34425158086` on `a227b461...` is retained only as intermediate provenance. The canonical final technical head `9634ee92...` and the merged Stage-14 main `3f34a1a77a14e65a91aa2ecda7e169c40052374c` share Git tree `c723990f31d1d15bb534cdc9794a23ba709dbab1`, so the validated source tree is exactly the merged tree.

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

## 9. Stage 15 — ACTIVE

Stage 15 branch: `stage15/submission-freeze`  
Stage 15 PR: `#18`  
Submission-content candidate: `main@3f34a1a77a14e65a91aa2ecda7e169c40052374c`  
Source tree: `c723990f31d1d15bb534cdc9794a23ba709dbab1`

Stage 15 has already:

1. identified the exact Stage-14-approved repository state and artifact set;
2. preserved manuscript/source/reproducibility/Lean/build provenance;
3. hashed the final artifact archive and submission candidates in `submission/FREEZE_MANIFEST.sha256`;
4. backfilled the canonical route-certification inheritance/regression record;
5. completed Stage 6R final-proposition novelty re-kill;
6. reconciled the canonical final Stage-14 CI provenance.

The remaining Stage-15 contract is authenticated portal reconciliation:

1. resolve every item in `submission/PORTAL_PREFLIGHT_CHECKLIST.md`;
2. upload only the frozen artifacts or a bounded Stage-14 compliance-only descendant;
3. inspect the portal-generated PDF page by page;
4. confirm both zero-cost hard gates;
5. submit only after every material portal item is PASS;
6. record journal confirmation and submission ID before declaring `SUBMITTED`.

A bounded anonymity/file-designation/declaration-placement repair returns to Stage 14 and requires fresh affected QA. Any theorem/model/result/interpretation change returns to the earliest affected scientific stage.

---

## 10. Return rules

| New problem | Return to |
|---|---|
| New equilibrium counterexample / false theorem | C0–C1R |
| Falsification code misses a material strategy region | C2R |
| Exact prior art absorbs final contribution | Stage 6R / Stage 12R2 as appropriate |
| Mathematical quantifier or Lean-certified theorem changes | analytic repair, then C2R-L / formal recertification |
| Freeze wording exceeds valid theory only | C3R/C4R clarification |
| Journal significance/fit issue only | Stage 12R2 |
| Exposition/organization issue only | Stage 13R2 |
| Submission-format/metadata issue only | Stage 14 |
| Formal build/statement mapping defect with unchanged mathematics | formal-verification repair, then affected QA |
| Stage-14/15 change introduces a scientific issue | earliest affected scientific stage |
| Portal-only mismatch | Stage 14/15 preflight |

---

## 11. Current checklist

- [x] RIO editorial audience-fit rejection recorded.
- [x] C0–C1R targeted equilibrium-set reaudit.
- [x] C2R symbolic/numerical audit.
- [x] C2R-L Lean certification.
- [x] C3R revised theory freeze.
- [x] C4R hostile scientific self-audit.
- [x] Paper-specific route-certification inheritance mapping and certification-regression record.
- [x] Stage 6R final-proposition novelty re-kill.
- [x] Stage 12R2 journal significance/fit recheck.
- [x] Stage 13R2 revised full-paper integration.
- [x] Astra-2 hostile referee gate and bounded recheck.
- [x] Stage 14 submission QA — `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.
- [x] Stage-14 canonical final technical CI provenance reconciled to `9634ee92...` / run `34425892795`.
- [ ] **Stage 15 authenticated portal preflight — ACTIVE.**
- [ ] Final submit and journal confirmation.
