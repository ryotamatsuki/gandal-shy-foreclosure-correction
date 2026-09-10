# Route Certification Inheritance and Certification Regression Register

**Date:** 2026-09-10  
**Project route:** bespoke correction-paper recovery route  
**Canonical workflow authority:** `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`  
**Canonical checklist:** `checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md`  
**Status:** **PASS — CANONICAL OBLIGATIONS MAPPED; REGRESSIONS CLOSED**

## 1. Purpose

This project uses paper-specific checkpoints (`C0–C4R`, `C2R-L`, `Stage 12R2`, `Stage 13R2`, `Astra-2`) rather than the canonical Stage labels for the entire recovery sequence. Under the post-v2.1 workflow, bespoke labels do not waive the canonical mathematical, novelty, scope, formal-verification, manuscript, or submission obligations.

This record maps the actual evidence-bearing checkpoints to the canonical obligations and records the certification regressions that motivated the reopened route.

The mapping is retrospective bookkeeping only. It does not alter the frozen theorem set, manuscript, code, Lean source, journal target, or Stage-15 submission-content candidate.

## 2. Canonical route-inheritance map

| Paper-specific checkpoint | Claim / object | Canonical obligation inherited | Attack actually performed | Formal-verification applicability | Primary artifact | Result | Surviving limitation | Status |
|---|---|---|---|---|---|---|---|---|
| Original intake / correction project | Published Gandal–Shy post-foreclosure equilibrium claim | Stage 0 — precise research question | Isolate whether the published quadratic specification supports Appendix B's stated price profile and welfare comparison | Applicable if mathematical correction survives | published article + project recovery records | Correction question survives | Project is a correction note, not a new-model mechanism search | PASS |
| C0–C1R | R1 long-arc geometry; R2 published profile; R3 U1/U2; R4 cost-floor; R5 welfare | Stage 1 + Stage 4 construction/verification | Clean derivation from primitives; necessity/sufficiency; global unilateral-deviation partition; boundaries; strategy-space distinction; welfare accounting | `FORMALIZATION APPLICABLE` | `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md` | Exact symmetric-foreclosed theorem class established | Does not characterize asymmetric/mixed/government-stage equilibria | PASS |
| C2R | R2–R5 falsification/regression | Stage 4A independent mathematical adversarial certification | Rebuilt primitive delivered-price evaluator; varied all three prices; global best responses; alternative-equilibrium/multiplicity regression; zero-sales outsider variation; boundary and asymmetric perturbation attacks | Applicable; targets handed to C2R-L | `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`, `code/verify_symbolic.py`, `code/verify_numerical.py` | No counterexample to stated theorem class; known failures retained | Numerical layer is falsification/regression evidence, not completeness proof | PASS |
| C2R-L | Proof-critical algebra/inequalities | Stage 7.5A embedded Formal Verification Gate | Lean statement-fidelity audit; exact counterexample; global-deviation inequalities; multiplicity condition; cost-floor logical reduction; welfare identities; `sorry/admit` and axiom audit | `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE` | `docs/C2R_L_LEAN_CERTIFICATION.md`, `GandalShy/Certification.lean` | Formal targets compile under pinned Lean/mathlib | Full Salop demand/Nash equivalence and asymmetric/mixed/government stage not formalized | PASS |
| C3R | Exact theorem/scope freeze | Stage 7.5 + Stage 7.5A + Stage 8 | Quantifier discipline; unrestricted vs restricted-game separation; explicit nonclaims; evidence map; formal coverage classification | Closed PASS carried into freeze | `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md` | Revised theory frozen | Strict paper range and symmetric-foreclosed pure-strategy class remain controlling | PASS |
| C4R | Frozen-theory hostile attack | Stage 7.5A residual generality/scope red-team | Re-attacked strict `c>5/2`, zero-sales prices, global deviations, boundaries, ties, welfare selection, cost-floor interpretation, Lean scope | PASS retained | `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md` | No scientific counterexample; one wording clarification | No all-equilibria/government-stage claim | PASS |
| Stage 6R backfill | Final Proposition 1/2 novelty | Stage 6 — Novelty Re-Kill | Exact-title/DOI/correction searches; forward-citation review; proposition/mechanism searches; whole-game absorption against closest standards/trade papers | N/A — literature gate | `docs/STAGE_06R_FINAL_PROPOSITION_NOVELTY_REKILL.md` | No located prior work absorbs the final correction/multiplicity/selection package | Search failure is not proof of nonexistence; obscure/non-indexed prior correction remains residual risk | PASS |
| Stage 12R2 | Publication significance and journal fit | Stage 12 | Current journal scope/format; recent related papers; significance/narrowness attack; fallback ladder | N/A | `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md` | International Economics retained as primary | Editorial narrowness risk remains | PASS |
| Stage 13R2 | Full manuscript construction/integration | Stage 10 + Stage 13 | Dependency-order section integration; two-proposition architecture; zero-figure/table architecture; claim consistency; build and visual parity | Formal scope wording checked | `docs/STAGE_13R2_REVISED_FULL_PAPER_INTEGRATION.md` | Integrated manuscript coherent | Journal operational rules deliberately deferred | PASS |
| Astra-2 | Full-manuscript hostile referee gate | Stage 11 | Independent reconstruction; globality/scope attack; original-paper check; Lean-scope audit; three bounded repairs and limited recheck | Formal scope not inflated | `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md` | `A. ASTRA-2 CLEARED — GO TO STAGE 14` | Publication significance assessed MODERATE | PASS |
| Stage 14 | Submission QA | Stage 14 | Clean Lean/symbolic/numerical/build/package checks; current journal ledger; PDF parity; page-by-page visual QA; fail-closed portal unknowns | Frozen Lean target rebuilt; placeholder gate rerun | `docs/STAGE_14_SUBMISSION_QA.md`, `docs/JOURNAL_REQUIREMENTS_LEDGER.md` | Local QA PASS; portal-dependent items conditional | Authenticated article type/anonymity/designations/fees/PDF remain open | CONDITIONAL PASS |
| Stage 15 | Immutable candidate and portal reconciliation | Stage 15 | Commit/tree/artifact freeze candidate; SHA-256 manifest; exact CI/artifact provenance; authenticated-portal kill tests | Formal artifacts preserved in frozen supplement | `docs/STAGE_15_SUBMISSION_FREEZE.md`, `submission/FREEZE_MANIFEST.sha256` | Local freeze candidate recorded | Portal preflight not yet closed; not submitted | IN PROGRESS |

## 3. Stage-specific applicability notes

### Stage 3 — Candidate Mechanism Search

Canonical Stage 3 is not a substantive missing gate for this recovery route. The paper does not propose a new strategic architecture after reopening; it corrects and characterizes the price game already published by Gandal and Shy (2001). The relevant mechanism search became an equilibrium-set reconstruction inside C0–C1R. Adding new mechanisms at this point would violate the correction-note scope and the no-complexity-rescue rule.

### Stage 5 — Mechanism Hardening

No Stage-5 model expansion was authorized. The discovered defect was solved by correcting the geometry, broadening the equilibrium-set audit, and separating the explicit cost-floor game from the published unrestricted game. No additional primitive was required.

## 4. Certification regression REG-01 — candidate equilibrium mistaken for equilibrium-set characterization

**Classification:** `CERTIFICATION REGRESSION — SCIENTIFIC / EQUILIBRIUM-SET`  
**Status:** **CLOSED**

| Field | Record |
|---|---|
| Missed defect | The pre-Astra workflow verified a preferred profile with outsider quote fixed at `p_3=c` and allowed that evidence to support a broader characterization/uniqueness-style conclusion. It did not actively vary a zero-sales, zero-profit outsider's payoff-equivalent quote and recompute member best responses. |
| Earlier checkpoint that should have caught it | Pre-Astra C0/C1 mathematical audit and old numerical verifier. |
| Canonical obligation missed | Stage 4/4A distinction between candidate-deviation certification and alternative-equilibrium/multiplicity certification; indifference/zero-payoff trigger. |
| Counterexample | At `c=4`, `(3/2,3/2,5/2)` is an unrestricted symmetric foreclosed equilibrium even though the published `(3/2,3/2,4)` profile is not Nash. More generally U1/U2 gives member-price multiplicity. |
| Earliest rollback | C0–C1R targeted equilibrium-set reaudit. |
| Repair | Re-derived U1/U2 necessity/sufficiency; rebuilt C2R verifier to vary all three prices; separated unrestricted and cost-floor games; revised welfare for independent market selections. |
| Permanent regression tests | Published `c=4` profile must fail; Astra `(3/2,3/2,5/2)` profile must survive in unrestricted mode; cost-floor mode must exclude the below-cost support; necessity-violation diagnostics remain active. |
| Workflow hardening | Generic workflow now contains the equilibrium-multiplicity/evidence-bearing certification refinement and `PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md`; a strong equilibrium-set claim cannot PASS solely on a no-profitable-deviation check of one candidate. |

This regression is the principal reason the reopened route exists. The old `docs/C0_C1_MATHEMATICAL_AUDIT.md` is explicitly marked superseded.

## 5. Certification regression REG-02 — restricted-game intersection bridge omitted from manuscript proof

**Classification:** `CERTIFICATION REGRESSION — BOUNDED PROOF/EXPOSITION`  
**Status:** **CLOSED BY ASTRA-2 LIMITED RECHECK**

The cost-floor result itself was correct, but the first Stage-13R2 manuscript moved from U1/U2 to intersecting with the cost-floor constraint without explicitly proving that deleting below-cost deviations does not create additional restricted-game equilibria in the stated class.

The missing bridge is now explicit:

- cost-floor-feasible candidates yield nonnegative candidate profit;
- every deleted deviation has `p_i<mc_i` and nonnegative demand, hence profit `(p_i-mc_i)q_i<=0`;
- therefore a deleted deviation cannot strictly improve upon the candidate, including a zero-profit candidate;
- restricted equilibrium in the stated class is therefore also unrestricted equilibrium, and the intersection operation is valid.

Astra-2 limited recheck returned `Repair 1 — PASS`. No theorem, Lean theorem, or numerical verifier changed.

The generic formal-verification checklist now also explicitly warns that a condition structure such as `UCond` / `CostFloorCond` is not itself a formal proof that the encoded condition is economically equivalent to Nash equilibrium unless that bridge is formalized or separately proved.

## 6. Provenance incident — premature Astra-clearance bookkeeping

**Classification:** `PROVENANCE INCIDENT — NOT A SCIENTIFIC CERTIFICATION REGRESSION`  
**Status:** **CLOSED**

A bookkeeping update once recorded Astra-2 clearance before a genuine limited recheck had occurred. PR `#15` restored the fail-closed state. Astra-2 then actually rechecked `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d` and returned all three repairs PASS, no new defect, and `A. ASTRA-2 CLEARED — GO TO STAGE 14`.

The current Astra record preserves this sequence so a future reader cannot mistake the premature status for the actual independent recheck.

## 7. Evidence-bearing final certification state

The bespoke recovery route now satisfies the canonical inheritance rule:

- candidate-deviation and alternative-equilibrium attacks are distinct and documented;
- the zero-demand/zero-profit indifference trigger is explicitly covered;
- the cost-floor restriction has provenance and is not smuggled into the published model;
- welfare is classified by continuation-selection scope;
- theorem quantifiers and nonclaims are frozen;
- formal-verification applicability is closed with `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE`;
- proof-assistant scope and unformalized economic bridges are explicit;
- certification regressions have rollback, repair, and permanent regression artifacts;
- Stage 6 final-proposition novelty is separately re-killed;
- no material `NOT TESTED` item remains behind a strong scientific claim.

**Final route-inheritance verdict:** `PASS`.

This PASS does not close authenticated portal requirements. Stage 15 remains `PREFLIGHT IN PROGRESS — AUTHENTICATED PORTAL ITEMS OPEN` until the live submission record is reconciled.
