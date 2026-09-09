# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-10  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1  
**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`  
**Current execution status:** `C0–C1R PASS` → `C2R PASS` → `C2R-L PASS` → `C3R PASS` → `C4R PASS` → `Stage 12R2 PASS` → `Stage 13R2 PASS` → `Astra-2 MINOR EXPOSITION REPAIR` → `bounded repair MERGED / CI PASS` → **NEXT: `Astra-2 limited recheck`**

This file is the authoritative project-specific route from the Astra-1 reopening to a new submission. **Stage 14 remains blocked until the limited Astra-2 recheck clears the three bounded repairs.**

> **Status correction.** The repository briefly recorded `Astra-2 CLEARED — GO TO STAGE 14` after an incorrectly supplied result. The actual Astra-2 output is `B. MINOR EXPOSITION REPAIR` on `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`. The required repairs have been implemented and merged, but the recheck remains pending.

---

## 1. Controlling scientific rules

1. The correction concerns the complete Appendix-B profile `(3/2,3/2,c)`, not a claim that member price `3/2` can never occur.
2. Keep the **unrestricted original price game** and the separate **cost-floor game** `p_i >= marginal cost` distinct. The cost floor is not WLOG, Nash-implied, weak-dominance elimination, or a condition stated by Gandal and Shy (2001).
3. Current equilibrium characterization is limited to **symmetric, foreclosed, pure-strategy price equilibria in one union-member market**.
4. Always distinguish existence, Nash status, characterization within a stated class, and uniqueness within a stated class.
5. The `1/2` welfare gap holds under a common symmetric continuation price. It is not selection-free across arbitrary unrestricted market-by-market continuations, and a common price is not claimed to be necessary for preserving the welfare ranking.
6. Lean certifies the proof-critical algebraic and quantified-inequality core, not the complete Salop game or all Nash equilibria from primitives.
7. C4R clarification controls downstream prose: the no-below-cost restriction collapses member-price multiplicity **within symmetric, foreclosed, pure-strategy equilibria**; it is not a global equilibrium-selection result.
8. Astra-2 clarification controls the cost-floor proof: before intersecting U1/U2 with the floor, the proof must explain why deleted below-cost deviations cannot create additional restricted-game equilibria in the stated class.

Scientific authorities:

- `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`
- `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`
- `docs/C2R_L_LEAN_CERTIFICATION.md`
- `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`
- `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`
- `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`
- `docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md`
- `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`

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
Astra-2     Second Independent Hostile Referee Gate       [MINOR REPAIR]
   ↓
Stage 13R2  Bounded Astra-2 Repair                        [MERGED / CI PASS]
   ↓
Astra-2     Limited Recheck                               [NEXT]
   ↓
Stage 14    Submission QA                                 [BLOCKED UNTIL RECHECK]
   ↓
Stage 15    Submission Freeze / Portal Preflight / Submit
```

No stage may be skipped merely because an earlier manuscript version once passed a corresponding gate.

---

## 3. Scientific result controlling the repaired manuscript

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

The bounded repair now makes the missing strategy-restriction bridge explicit: at a cost-floor-feasible candidate, candidate profits are nonnegative, while a deleted below-cost deviation has `(p_i-mc_i)q_i <= 0` because demand is nonnegative. Hence deleted deviations cannot strictly improve upon the candidate and cannot create an additional restricted-game equilibrium within the stated class.

### Welfare

For common symmetric continuation price `s`:

`TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`, gap `1/2`.

For market-specific symmetric continuation prices:

`TS_A^SU=3V+1/4+(3/2)(s_B-s_A)`.

Hence welfare levels are continuation-selection dependent in the unrestricted game. The common-price condition recovers the exact original `1/2` gap; it is not claimed to be necessary for preserving the sign of the welfare comparison.

---

## 4. Journal decision carried forward

**Primary target remains `International Economics`, direct short-paper / short-communication route.**

Current positioning hierarchy:

1. correction of the published post-foreclosure equilibrium and uniqueness claim;
2. unrestricted symmetric-foreclosed equilibrium multiplicity;
3. conditional piecewise member-price characterization in a separate cost-floor game;
4. continuation-selection dependence of the welfare comparison;
5. zero-sales outsider strategic relevance / static limit-pricing mechanism as supporting interpretation, not the headline.

Integrated title:

**`Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)`**

Astra-2 assessed publication significance as **MODERATE**. The principal remaining editorial risk is publication significance/narrowness, not a newly identified mathematical defect.

The zero-fee hard gate remains in force and must be refreshed from current official sources and the authenticated portal at Stage 14.

---

## 5. Stage 13R2 — initial integration PASS; bounded repair merged

Initial integration PR: `#13`  
Initial Stage-13R2 merge / Astra-2 audited baseline: `ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`  
Bounded repair branch: `stage13r2/astra2-minor-repair`  
Bounded repair PR: `#14`  
Bounded-repair merge: `02a691e9260c48a5e9485e7d8188caf3648f918f`

Astra-2 required exactly three Stage-13R2 repairs:

1. **Cost-floor proof bridge:** explain why deleted below-cost deviations cannot create additional restricted-game equilibria before intersecting U1/U2 with the floor.
2. **Highlights:** qualify the cost-floor benchmark by the symmetric, foreclosed, pure-strategy class.
3. **Cover letter:** remove the overly strong `exact continuation conditions` wording and distinguish the exact common-price `1/2` gap from the market-specific transfer term.

All three repairs have been implemented.

Repair verification:

- repaired manuscript CI head: `72ed861e3460cbcaf5eaf0a763f789c70ed07332`;
- manuscript-integration run `34379361638`: **success**;
- symbolic/numerical verification: **PASS**;
- manuscript/package build: **PASS**;
- final LaTeX clean-log gate: **PASS**;
- generated-artifact checks/upload: **PASS**.

No theorem statement, numerical verifier, Lean theorem, title, abstract, or journal target changed.

The bounded repair being merged does **not** itself close Astra-2. Clearance requires the limited recheck below.

---

## 6. Astra-2 — first pass MINOR REPAIR; limited recheck pending

Astra-2 audited:

`main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`.

Actual verdict:

`B. MINOR EXPOSITION REPAIR`.

Headline findings:

- U1/U2 characterization: **PASS**;
- welfare proposition: **PASS**;
- published-profile correction: **PASS**;
- cost-floor result: **CONDITIONAL PASS** pending the proof bridge;
- no new equilibrium counterexample found;
- publication significance: **MODERATE**;
- workflow return: **Stage 13R2 only**;
- final decision on the audited baseline: **DO NOT GO TO STAGE 14**.

The three required repairs are now present and CI-clean. The next action is a **limited Astra-2 recheck** of only:

1. the cost-floor proof bridge;
2. the qualified third highlight;
3. the revised cover-letter welfare wording;
4. whether those repairs introduced a new defect.

A full hostile audit is not required unless the recheck reveals a new substantive issue.

Proceed to Stage 14 only if the limited recheck returns a clear submission-level clearance.

---

## 7. Stage 14 — Submission QA — BLOCKED

Do **not** begin Stage 14 yet.

After Astra-2 limited re-clearance, Stage 14 must refresh the current *International Economics* requirements from official sources and, where required, the authenticated submission portal. Any material `UNVERIFIED` or unresolved `CONFLICT` blocks PASS.

Mandatory checks include:

- exact article-type label and short-paper route;
- review/anonymity model and author-information placement;
- title-page requirement;
- initial PDF versus editable-source upload requirements and file designations;
- LaTeX archive/folder rules;
- abstract, keyword, JEL and highlight requirements;
- funding, competing interests, CRediT, data/code and AI declaration wording/placement;
- reviewer-suggestion and portal-attestation fields;
- current submission fee and mandatory standard-route publication/page/APC status;
- portal-generated PDF behavior;
- consistency of exact manuscript/submission-package artifacts after any format-only repair.

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
| Astra-2 finds mathematical defect | earliest affected scientific stage |
| Astra-2 finds bounded exposition/scope defect only | Stage 13R2, then limited Astra-2 recheck |
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
- [x] Stage 12R2 journal significance/fit recheck.
- [x] Initial Stage 13R2 revised full-paper integration.
- [x] Astra-2 first pass — `B. MINOR EXPOSITION REPAIR`.
- [x] Stage 13R2 bounded Astra-2 repair — implemented, CI-passed, and merged.
- [ ] **Astra-2 limited recheck — NEXT.**
- [ ] Stage 14 submission QA.
- [ ] Stage 15 submission freeze / portal preflight / submit.
