# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-10  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1  
**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`  
**Current execution status:** `C0–C1R PASS` → `C2R PASS` → `C2R-L PASS` → `C3R PASS` → `C4R PASS` → `Stage 12R2 PASS` → `Stage 13R2 PASS` → `Astra-2 MINOR EXPOSITION REPAIR` → **`Stage 13R2 bounded repair ACTIVE`**

This file is the authoritative project-specific route from the Astra-1 reopening to a new submission. Stage 14 remains blocked until the bounded Stage-13R2 repair passes CI and Astra-2 limited re-clearance.

---

## 1. Controlling scientific rules

1. The correction concerns the complete Appendix-B profile `(3/2,3/2,c)`, not a claim that member price `3/2` can never occur.
2. Keep the **unrestricted original price game** and the separate **cost-floor game** `p_i >= marginal cost` distinct. The cost floor is not WLOG, Nash-implied, weak-dominance elimination, or a condition stated by Gandal and Shy (2001).
3. Current equilibrium characterization is limited to **symmetric, foreclosed, pure-strategy price equilibria in one union-member market**.
4. Always distinguish existence, Nash status, characterization within a stated class, and uniqueness within a stated class.
5. The `1/2` welfare gap holds under a common symmetric continuation price. It is not selection-free across arbitrary unrestricted market-by-market continuations, and a common price is not claimed to be necessary for preserving the welfare ranking.
6. Lean certifies the proof-critical algebraic and quantified-inequality core, not the complete Salop game or all Nash equilibria from primitives.
7. C4R clarification controls all downstream prose: the no-below-cost restriction collapses member-price multiplicity **within symmetric, foreclosed, pure-strategy equilibria**; it is not a global equilibrium-selection result.
8. Astra-2 clarification: before intersecting U1/U2 with the cost-floor restriction, the written proof must explain why deleted below-cost deviations cannot create additional restricted-game equilibria in the stated class.

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
Stage 13R2  Bounded Astra-2 Repair                        [ACTIVE]
   ↓
Astra-2     Limited Recheck                               [NEXT AFTER CI]
   ↓
Stage 14   Submission QA
   ↓
Stage 15   Submission Freeze / Portal Preflight / Submit
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

Astra-2 confirmed the result but required the proof to make the following bridge explicit. At a cost-floor-feasible candidate, candidate profits are nonnegative. Any deviation removed by the floor has `p_i < mc_i`; because demand is nonnegative, its profit is `(p_i-mc_i)q_i <= 0`. Hence no removed deviation can strictly improve on the candidate, so a restricted-game equilibrium in the stated class is also an unrestricted-game equilibrium and may legitimately be obtained by intersecting U1/U2 with the cost-floor restrictions.

### Welfare

For common symmetric continuation price `s`:

`TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`, gap `1/2`.

For market-specific symmetric continuation prices:

`TS_A^SU=3V+1/4+(3/2)(s_B-s_A)`.

Hence welfare robustness is continuation-selection conditional in the unrestricted game. The common-price condition recovers the exact original `1/2` gap; it is not claimed to be the necessary condition for preserving the sign of the welfare comparison.

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

Astra-2 assessed publication significance as **MODERATE**. The principal remaining editorial risk is publication significance/narrowness, not a newly identified mathematical defect. No new model extension is authorized solely to improve journal fit.

The zero-fee hard gate remains in force and must be refreshed from current official sources and the authenticated portal at Stage 14.

---

## 5. Stage 13R2 — Initial integration PASS; bounded repair ACTIVE

Authority: `docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md`  
Initial integration PR: `#13`  
Initial Stage-13R2 merge: `ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`  
Bounded repair branch: `stage13r2/astra2-minor-repair`

Initial Stage 13R2 completed the full-paper integration and passed manuscript CI, package build, clean-log, and visual QA. Astra-2 then returned the manuscript to Stage 13R2 for three bounded repairs only.

Required repair set:

1. **Cost-floor proof bridge:** explain why deleted below-cost deviations cannot create additional restricted-game equilibria before intersecting U1/U2 with the floor.
2. **Highlights:** qualify the cost-floor benchmark by the symmetric, foreclosed, pure-strategy class.
3. **Cover letter:** remove the overly strong `exact continuation conditions` wording and distinguish the exact common-price `1/2` gap from the market-specific transfer term.

No theorem statement, numerical verifier, Lean theorem, title, abstract, or publication target changes are authorized by this repair unless a new inconsistency emerges.

The repair exits Stage 13R2 only after:

- the three changes are implemented;
- manuscript integration CI/build passes;
- no new cross-document scope conflict is introduced;
- Astra-2 performs a limited recheck and clears all three items.

---

## 6. Astra-2 — first pass MINOR REPAIR; limited recheck mandatory

First Astra-2 audited baseline:

`main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`

First-pass verdict:

`B. MINOR EXPOSITION REPAIR`

Headline scientific findings:

- U1/U2 characterization: **PASS**;
- welfare proposition: **PASS**;
- published-profile correction: **PASS**;
- cost-floor result: **CONDITIONAL PASS** pending the proof bridge;
- no new equilibrium counterexample found;
- publication significance: **MODERATE**;
- workflow return: **Stage 13R2 only**;
- Stage-14 decision on audited baseline: **DO NOT GO TO STAGE 14**.

After the bounded repair passes CI, Astra-2 should be asked only to verify that the three required repairs are complete and that they did not create a new substantive inconsistency. A full new search is not required unless the repaired wording changes a theorem or exposes a fresh scientific issue.

Proceed to Stage 14 only after the limited recheck returns a clear submission-level clearance.

---

## 7. Stage 14 — Submission QA

Begin only after Astra-2 re-clearance. Refresh current official journal and authenticated-portal requirements. Any material `UNVERIFIED` or unresolved `CONFLICT` blocks PASS.

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
- [ ] **Stage 13R2 bounded Astra-2 repair — ACTIVE.**
- [ ] Astra-2 limited recheck.
- [ ] Stage 14 submission QA.
- [ ] Stage 15 submission freeze / portal preflight / submit.
