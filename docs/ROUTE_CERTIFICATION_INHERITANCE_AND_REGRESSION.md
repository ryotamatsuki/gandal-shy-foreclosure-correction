# Route Certification Inheritance and Certification-Regression Record

**Date:** 2026-09-10  
**Project:** Gandal–Shy Foreclosure Correction  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`  
**Project route:** bespoke correction-paper recovery route (`C0–C4R`, then Stage 12R2 onward)  
**Purpose:** backfill the explicit inheritance/evidence map required by `checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md` without changing any scientific claim.

## 1. Route-certification / inheritance table

| Paper-specific checkpoint | Claim / object | Canonical obligation inherited | Attack actually performed | Formal-verification applicability | Primary artifact(s) | Result | Surviving limitation | Status |
|---|---|---|---|---|---|---|---|---|
| C0–C1R | Published profile is non-Nash; U1/U2 symmetric-foreclosed characterization; cost-floor F1/F2; welfare selection dependence | Stage 1 source audit; Stage 4 global equilibrium construction; Stage 7 welfare accounting; exact quantifiers | Clean derivation from quadratic Salop primitives; global unilateral-deviation partition; alternative zero-sales outsider quotes; boundary/tie analysis; welfare recomputation across segmented markets | APPLICABLE | `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md` | PASS | Characterization limited to symmetric, foreclosed, pure-strategy equilibria in one union-member market | CLOSED |
| C2R | Falsification/regression of C0–C1R theorem class | Stage 4 symbolic/numerical verification; Stage 4A independent adversarial attack | New verifier varies all three posted prices, computes primitive delivered-price envelope, searches global unilateral best responses, preserves published and Astra counterexamples, checks necessity violations and asymmetric perturbations | APPLICABLE | `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`; `code/verify_symbolic.py`; `code/verify_numerical.py` | PASS | Numerical work is falsification/regression evidence, not equilibrium-set proof | CLOSED |
| C2R-L | Proof-critical algebra/inequality certification | Stage 4A formalization planning plus Stage 7.5A Formal Verification Gate | Lean certification of long-arc identity, exact c=4 counterexample, global-deviation inequalities, necessity signs, encoded multiplicity/cost-floor implications, welfare identities; `sorry`/`admit` and axiom audit | `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE` | `docs/C2R_L_LEAN_CERTIFICATION.md`; `GandalShy/Certification.lean`; pinned Lean/mathlib files | PASS | Does not formalize the full demand correspondence or prove UCond ↔ full Nash set from primitives | CLOSED |
| C3R | Exact theory scope and theory freeze | Stage 7.5 / Stage 7.5A quantifier discipline; Stage 8 theory freeze | Freezes strategy spaces, parameter domain, theorem class, welfare-selection scope, explicit nonclaims, evidence map, formal coverage boundary | PASS carried from C2R-L | `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md` | PASS | Asymmetric/mixed equilibria and government-stage selection remain explicit nonclaims | CLOSED |
| C4R | Hostile post-freeze scientific attack | Stage 4A/7.5A regression attack and Stage 11-style hostile scientific review | Attacks full c>5/2 quantifier, hidden zero-sales outsider prices, global deviations, cost-floor/original-game distinction, boundaries, tie-breaking, welfare selection, Lean-scope inflation | PASS carried from C2R-L | `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md` | PASS WITH one wording clarification | No new theorem or quantifier change | CLOSED |
| Stage 6R backfill | Final Proposition 1/2 novelty | Canonical Stage 6 novelty re-kill | Fresh proposition-language/mechanism searches, exact-correction/corrigendum search, original/working-version genealogy and whole-game absorption check | N/A to novelty | `docs/STAGE_06R_FINAL_PROPOSITION_NOVELTY_REKILL.md` | GO | Search failure is not proof of absence; downstream impact on citing papers not claimed | CLOSED |
| Stage 12R2 | Journal significance / fit after repaired theorem set | Stage 12 journal positioning | Current journal scope/format/recent-fit audit; acceptance vs desk-reject argument; no model expansion for fit | Formal state carried unchanged | `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md` | PASS | Editorial significance remains moderate; narrowness risk remains | CLOSED |
| Stage 13R2 | Full-paper integration | Stage 10/13 manuscript construction/integration; figure-table architecture | Dependency-order section integration; cross-document scope audit; deliberate zero-figure/table architecture; build/parity/visual QA | Formal scope checked against manuscript claims | `docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md` | PASS | Submission rules still portal-dependent | CLOSED |
| Astra-2 | Independent full-manuscript hostile referee gate | Stage 11 hostile referee attack | Independent reconstruction, globality/scope/welfare/Lean attack; bounded repair and actual limited recheck | Formal scope explicitly attacked | `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md` | CLEARED | Publication significance assessed MODERATE, not HIGH | CLOSED |
| Stage 14 | Submission QA | Stage 14 clean build / journal compliance / formal rebuild / page-by-page QA | Current requirements ledger; Lean rebuild and admitted-proof gate; symbolic/numerical rerun; LaTeX/package audit; PDF parity and visual inspection | `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE`, rebuilt | `docs/STAGE_14_SUBMISSION_QA.md`; `docs/JOURNAL_REQUIREMENTS_LEDGER.md` | CONDITIONAL PASS | Authenticated Editorial Manager items and zero-cost gates remain open | CLOSED FOR LOCAL QA |
| Stage 15 | Immutable submission candidate and live preflight | Stage 15 freeze/provenance/portal reconciliation | SHA/tree freeze candidate, artifact hashes, authenticated-portal checklist, fail-closed cost gates | Formal source/build provenance frozen with package | `docs/STAGE_15_SUBMISSION_FREEZE.md`; `submission/FREEZE_MANIFEST.sha256` | IN PROGRESS | Cannot declare SUBMISSION FROZEN / SUBMITTED until live portal items close | ACTIVE |

## 2. Claim-specific certification inheritance

### Claim P1a — published complete profile is non-Nash

- candidate-deviation audit: PASS;
- exact c=4 counterexample: analytic + symbolic/numerical + Lean PASS;
- strict `c>5/2` quantifier: analytic proof and hostile recheck PASS;
- formal coverage: exact checkpoint/core, not full primitive-to-Nash quantifier.

### Claim P1b — unrestricted U1/U2 characterization within the stated class

- candidate-deviation audit: PASS;
- alternative-equilibrium/multiplicity audit: PASS;
- indifference/zero-profit trigger: PASS — outsider zero-sales quotes varied explicitly;
- global finite-deviation partition: PASS;
- numerical global-best-response regression: PASS;
- formal coverage: proof-critical inequalities + encoded UCond condition set only;
- limitation: no claim concerning all asymmetric or mixed equilibria.

### Claim P1c — cost-floor F1/F2 characterization

- selection/refinement provenance: PASS — cost floor is explicitly new strategy restriction, not WLOG/Nash-implied/original-paper assumption;
- symmetry of restriction: PASS;
- strategy-restriction bridge: PASS after Astra-2 bounded repair and limited recheck;
- formal coverage: logical reduction from UCond plus floor; economic game equivalence bridge remains analytic;
- limitation: only the stated symmetric foreclosed pure-strategy class.

### Claim P2 — welfare under continuation selection

- common-price welfare identity: analytic + symbolic + Lean PASS;
- market-specific transfer term: analytic + symbolic + Lean PASS;
- multiplicity/selection audit: PASS across independently selected member markets;
- overclaim control: no assertion of government-stage policy reversal or all-equilibrium welfare ordering.

## 3. Certification-regression record

### Regression CR-1 — candidate equilibrium verification was mistaken for equilibrium-set characterization

**Missed defect:** the pre-Astra verification fixed the outsider quote at `p_3=c`, so it verified a preferred candidate but did not search payoff-equivalent zero-sales outsider quotes. A different zero-sales quote supports additional member-price equilibria.

**Earlier checkpoint that should have caught it:** pre-Astra mathematical/candidate verification and any uniqueness/characterization certificate.

**Canonical obligation:** separate candidate-deviation audit from alternative-equilibrium/multiplicity audit; trigger a dedicated attack when a player has zero demand/zero profit and hence payoff-equivalent actions.

**Missing attack/artifact:** active variation of the indifferent outsider's zero-sales price and recomputation of member best responses.

**Repair:** C0–C1R reopened the equilibrium set; C2R rebuilt the verifier to vary all three prices; the Astra equilibrium is a permanent regression test; C3R narrowed the theorem scope; generic workflow gained `PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md` and the equilibrium-multiplicity refinement.

**Earliest rollback point used:** C0–C1R / equivalent Stage 4 equilibrium analysis.

**Permanent regression:** at `c=4`, `(3/2,3/2,5/2)` must survive in unrestricted mode while `(3/2,3/2,4)` must fail.

**Status:** CLOSED.

### Regression CR-2 — cost-floor intersection proof omitted the strategy-restriction bridge

**Missed defect:** an earlier proof moved from the unrestricted equilibrium set to the cost-floor set by intersection without explicitly proving that deleted below-cost deviations cannot create new equilibria.

**Earlier checkpoint that should have caught it:** restricted-game characterization / scope certification.

**Canonical obligation:** when a selection rule, floor, refinement or strategy restriction is introduced, certify both provenance and its exact effect on the equilibrium set rather than assuming set intersection is automatically valid.

**Repair:** Astra-2 required a bounded proof bridge. The manuscript now proves that every cost-floor-feasible candidate has nonnegative profit while every deleted `p_i<mc_i` deviation yields nonpositive profit, so no deleted deviation can be a strict improvement. Astra-2 limited recheck returned PASS.

**Earliest rollback point used:** Stage 13R2 exposition only; theorem and formal statement unchanged.

**Permanent regression:** cost-floor proof bridge is retained in the manuscript and Astra record.

**Status:** CLOSED.

### Regression CR-3 — bookkeeping briefly recorded Astra clearance before an actual limited recheck

**Missed defect:** repository status temporarily advanced the gate without evidence from the requested independent recheck.

**Canonical obligation:** evidence-bearing PASS; no status may be upgraded merely from expected/assumed review outcome.

**Repair:** bookkeeping was reverted to fail-closed status; an actual Astra-2 limited recheck was then performed on `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d`, and only after three PASS results plus no-new-defect was the gate closed.

**Permanent regression:** `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md` preserves both the initial B verdict and the actual later clearance baseline/result.

**Status:** CLOSED.

## 4. Final inheritance verdict

The bespoke correction route inherits the material mathematical, equilibrium-set, welfare-selection, quantifier, formal-verification, hostile-referee, submission-QA, and freeze obligations of the canonical workflow.

No strong scientific claim currently rests on a material `NOT TESTED` field. Formal verification is explicitly closed as `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE`. The remaining open items are Stage-15 authenticated-portal operational requirements, not missing scientific certification.

**Verdict:** `PASS — PAPER-SPECIFIC CERTIFICATION INHERITANCE BACKFILLED`.
