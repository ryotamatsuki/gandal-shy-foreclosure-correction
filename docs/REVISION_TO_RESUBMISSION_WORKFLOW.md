# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-09  
**Purpose:** Project-specific recovery workflow after the independent Astra referee audit.  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1.  
**Pre-reopening manuscript baseline:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`.  
**Current execution status:** `C0–C1R PASS` → `C2R PASS` → `C2R-L PASS` → `C3R PASS` → **NEXT: `C4R Hostile Scientific Self-Audit`**.

---

## 0. Current stop condition

The pre-Astra Stage-13R manuscript is **not cleared for submission**. Stage 14 remains blocked.

Astra identified a substantive equilibrium-characterization defect: the pre-Astra manuscript proved important candidate equilibria but overstated them as a characterization even though the unrestricted original price game admits additional symmetric foreclosed equilibria supported by zero-sales outsider quotes.

The correction itself survives. Direct inspection of the published Gandal and Shy (2001) article confirms that:

1. the published model uses quadratic transportation costs;
2. Appendix B uses an inconsistent long-arc price-difference coefficient;
3. the complete published price profile `(3/2,3/2,c)` is not a Nash equilibrium in the strict post-foreclosure range;
4. the unrestricted original price game has additional symmetric foreclosed equilibria;
5. an explicit cost-floor restriction changes the strategy set and yields the previously derived piecewise member price within the stated equilibrium class;
6. the welfare result is conditional on continuation-equilibrium selection.

Scientific recovery has now passed four gates:

- `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md` — analytic equilibrium-set reconstruction;
- `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md` — three-price symbolic/numerical falsification and regression audit;
- `docs/C2R_L_LEAN_CERTIFICATION.md` — Lean formal certification of the proof-critical algebraic and quantified inequality core;
- `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md` — controlling revised scientific freeze.

The next task is to attempt to destroy the frozen theory before journal positioning resumes.

---

## 1. Governing principles

### 1.1 Correct the complete published profile, not an isolated member price

The defensible correction is:

> Appendix B's claimed profile `(3/2,3/2,c)` is not a Nash equilibrium under the published quadratic-transport specification in the strict post-foreclosure range.

Do **not** claim that member price `3/2` can never occur in another equilibrium.

### 1.2 Keep the unrestricted original game and the cost-floor game separate

The revision must distinguish:

1. **Unrestricted original price game:** the price strategy space stated in the published model, including zero-sales below-cost quotes when not explicitly prohibited.
2. **Cost-floor price game:** the explicitly restricted strategy space `p_i >= marginal cost in that market`.

The cost-floor restriction must not be described as:

- without loss of generality;
- an implication of Nash equilibrium;
- generic elimination of weakly dominated strategies; or
- a condition stated by Gandal and Shy (2001).

### 1.3 Separate logical strength

Every theorem and every manuscript sentence must distinguish:

- `EXISTS`;
- `IS A NASH EQUILIBRIUM`;
- `CHARACTERIZES ALL EQUILIBRIA IN THE STATED CLASS`;
- `UNIQUE WITHIN THE STATED CLASS`.

An existence proof may not be upgraded to characterization or uniqueness.

### 1.4 State the equilibrium class exactly

The current characterization is for **symmetric, foreclosed, pure-strategy equilibria in one union-member market**.

No current theorem claims to characterize:

- all asymmetric pure equilibria;
- mixed equilibria; or
- the government-stage equilibrium under unrestricted continuation multiplicity.

### 1.5 Welfare claims must match equilibrium selection

The common-price cancellation is not selection-free when segmented member markets choose different continuation equilibria.

The manuscript must distinguish:

- a common symmetric continuation price across the two union markets; and
- arbitrary market-by-market continuation selections.

Do not claim that the original policy conclusion reverses without solving the relevant government-stage equilibrium.

### 1.6 Lean scope must not be overstated

Lean certifies the proof-critical algebraic and quantified inequality core. It does **not** independently reconstruct the entire continuum Salop demand game from measure-theoretic consumer primitives.

Any formal-certification claim must follow `docs/C2R_L_LEAN_CERTIFICATION.md` and `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md` exactly.

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
C4R     Hostile Scientific Self-Audit                     [NEXT]
   ↓
Stage 12R2  Journal Significance / Fit Recheck
   ↓
Stage 13R2  Revised Full-Paper Integration
   ↓
Astra-2     Second Independent Hostile Referee Gate
   ↓
Stage 14   Submission QA
   ↓
Stage 15   Submission Freeze / Authenticated Portal Preflight / Submit
```

No stage may be skipped merely because an earlier manuscript version previously passed a corresponding gate.

---

## 3. C0–C1R — Targeted Equilibrium-Set Reaudit

**Status:** `PASS`  
**Authority:** `docs/C0_C1R_TARGETED_EQUILIBRIUM_AUDIT.md`

### 3.1 Published-profile correction

Under quadratic transportation costs,

`p_1 + x^2 = p_2 + (2-x)^2`

implies

`x^L = 1 + (p_2-p_1)/4`.

At `c=4`, the published complete profile `(3/2,3/2,4)` admits the member deviation `p_1=7/4`, raising profit from `9/4` to `147/64`, a gain of `3/64`.

### 3.2 Unrestricted original game

Within symmetric foreclosed pure-strategy profiles `(s,s,r)`, the analytic equilibrium set is:

**U1 — lower-price family**

- `3/2 <= s < 2`;
- `r=s+1`;
- `c>=s+1`.

**U2 — duopoly-price family**

- `s=2`;
- `r>=3`;
- `c>=3`.

For `c>=5/2`, admissible member prices satisfy

`3/2 <= s <= min{2,c-1}`,

subject to the outsider-price conditions above.

### 3.3 Explicit cost-floor game

Impose the separate strategy restriction

`p_i >= mc_i`.

Within symmetric foreclosed pure-strategy equilibria:

- `5/2 <= c < 3`: `(p_1,p_2,p_3)=(c-1,c-1,c)`;
- `c>=3`: `p_1=p_2=2`, with any `p_3>=c`.

For the paper's strict range `5/2<c<5`, the member price is

`p_M=c-1` for `5/2<c<3`,

`p_M=2` for `3<=c<5`.

At `c=3`, the branches meet at `p_M=2`; strict slack begins only for `c>3`.

### 3.4 Welfare scope

For a common symmetric member price `s` in both union markets:

`TS_M^SU = 3V + 1/4`,

`TS^MR = 3V - 1/4`,

so the gap is `1/2`.

For market-specific symmetric continuation prices `s_A` and `s_B`:

`TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`.

Thus the original member-country comparison is preserved under a common symmetric continuation and, in particular, the symmetric cost-floor continuation, but is not selection-free over arbitrary unrestricted continuation choices.

---

## 4. C2R — Symbolic / Numerical Audit

**Status:** `PASS`  
**Authority:** `docs/C2R_SYMBOLIC_NUMERICAL_AUDIT.md`

The old verifier fixed `p_3=c` and could not discover the Astra multiplicity. C2R replaced it with a three-price global-deviation architecture.

The revised verifier:

- varies `p_1`, `p_2`, and `p_3`;
- separates unrestricted and cost-floor modes;
- computes unilateral best responses from primitive delivered-price thresholds;
- searches global member and outsider deviations;
- preserves the published-profile failure and Astra equilibrium as permanent regressions;
- checks necessity violations and representative asymmetric perturbations;
- stresses `c=5/2`, `c=3`, and nearby values;
- distinguishes candidate verification from equilibrium-set characterization.

The high-resolution run used `N=80,000`, tested 91 valid-family profiles, and found no counterexample to the exact C0–C1R theorem class. Numerical evidence remains falsification/regression protection, not a substitute for analytic necessity and sufficiency.

---

## 5. C2R-L — Lean Formal Certification

**Status:** `PASS`  
**Authority:** `docs/C2R_L_LEAN_CERTIFICATION.md`  
**Formal source:** `GandalShy/Certification.lean`

### 5.1 Reproducible environment

- Lean: `leanprover/lean4:v4.34.0-rc2`;
- mathlib: pinned commit `74828d59824ed9c1e3002f796aaf53cec5ffb47c`;
- dependency lock: `lake-manifest.json`;
- CI workflow: `.github/workflows/lean-certification.yml`.

### 5.2 Certified targets

Lean compiles formal proofs of the proof-critical core, including:

- corrected long-arc coefficient `1/4`;
- exact `c=4` published-profile profitable deviation and gain `3/64`;
- regular and outsider-relevant profit-gap factorizations;
- global no-gain inequalities used in the U1 sufficiency proof;
- necessity sign checks for `s<3/2`, `s>2`, and outsider-threshold failure;
- multiplicity of the analytic `UCond` condition set;
- exact cost-floor reduction and piecewise member-price characterization within that condition set;
- common-price and cross-market welfare identities.

### 5.3 CI evidence

GitHub Actions run `34291397450` completed successfully:

- `lake build GandalShy` passed;
- the formal source compiled;
- the explicit admitted-proof scan found no `sorry` or `admit`;
- `#print axioms` diagnostics show only standard Lean/mathlib logical axioms used by the proof machinery, not project-specific axioms or admitted theorems.

### 5.4 Explicit limitations

Lean does not certify independently:

- the full continuum consumer demand correspondence from primitives;
- tie-breaking and measure-zero consumer details;
- all asymmetric pure equilibria;
- mixed equilibria;
- the government-stage equilibrium;
- prior art or publication significance.

The analytic equivalence between `UCond` and the symmetric foreclosed pure-strategy Nash set is the C0–C1R theorem. Lean certifies the algebraic/inequality core and subsequent exact logical reductions.

---

## 6. C3R — Revised Canonical Theory Freeze

**Status:** `PASS`  
**Authority:** `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`

C3R freezes only claims jointly supported by C0–C1R, C2R, and C2R-L. The controlling freeze fixes:

- the published-model primitives relevant to the correction;
- the main parameter range `5/2<c<5` and boundary treatment at `c=5/2` and `c=3`;
- the exact theorem class: symmetric, foreclosed, pure-strategy equilibria in one member market;
- the unrestricted U1/U2 equilibrium characterization and member-price multiplicity;
- the separate cost-floor F1/F2 characterization;
- the common-price and cross-market welfare formulas;
- the exact scope and limitations of Lean certification;
- permitted limit-pricing terminology;
- a prohibited-claims list preventing quantifier drift.

### Frozen proposition architecture

**Proposition 1 — Post-foreclosure pricing and multiplicity**

1. the published Appendix-B profile is not Nash in the strict post-foreclosure range;
2. the unrestricted original game has the U1/U2 symmetric foreclosed equilibrium set and therefore member-price multiplicity;
3. the explicit cost-floor game yields the F1/F2 piecewise member-price characterization within the same equilibrium class.

**Proposition 2 — Welfare under continuation selection**

1. under a common symmetric continuation, the original member-country welfare gap remains `1/2`;
2. with different symmetric continuation prices across markets, the cross-market transfer term remains;
3. the unrestricted original-game welfare comparison is therefore continuation-selection dependent.

The paper may not claim a government-stage policy reversal or selection-free robustness across all Nash equilibria.

---

## 7. C4R — Hostile Scientific Self-Audit

**Status:** `NEXT / ACTIVE AFTER C3R MERGE`

After C3R, attempt to destroy the revised frozen theory.

Mandatory attacks include:

- hidden outsider-price equilibria;
- asymmetric pure equilibria insofar as they threaten a stated theorem scope;
- below-cost and zero-demand strategies;
- `c=5/2` and `c=3` boundaries;
- domain of the two-member demand formula;
- tie-breaking / measure-zero consumers;
- exact meaning of foreclosure and limit pricing;
- cost-floor restriction versus the original model;
- cross-market equilibrium selection and welfare;
- any wording that upgrades existence to characterization or characterization to uniqueness;
- any claim that overstates Lean's scope;
- any gap between the `for every c>5/2` published-profile claim and the exact analytic proof;
- whether any unresolved asymmetric equilibrium can contaminate a claim currently restricted to the symmetric class;
- whether the revised contribution still rests on a hidden equilibrium-selection assumption.

Verdicts:

- `PASS — GO TO STAGE 12R2`;
- `CONDITIONAL — BOUNDED SCIENTIFIC REPAIR`;
- `FAIL — RETURN TO EARLIEST AFFECTED SCIENTIFIC STAGE`.

A mathematical change to a Lean-certified theorem requires affected C2R/C2R-L checks to be rerun before refreezing.

---

## 8. Stage 12R2 — Journal Significance / Fit Recheck

The contribution has materially changed. Reassess publication significance and journal fit from scratch after C4R.

The revised story now frozen for evaluation is:

`published claimed unique equilibrium is false`
→ `unrestricted game has symmetric-foreclosed equilibrium multiplicity`
→ `explicit cost-floor restriction characterizes the member price within the stated class`
→ `welfare robustness is continuation-selection conditional`.

*International Economics* remains the provisional first target, subject to this recheck and the zero-fee hard gate.

Required verdict:

- `GO TO STAGE 13R2`;
- `REPOSITION`; or
- `CHANGE JOURNAL TARGET`.

---

## 9. Stage 13R2 — Revised Full-Paper Integration

Do not start with the Introduction.

Revise in this order:

1. Section 2 — published specification, long-arc error, exact published-profile failure;
2. Section 3 — unrestricted multiplicity and explicit cost-floor characterization;
3. Section 4 — welfare under exact continuation-selection conditions;
4. only then Abstract, Introduction, Conclusion, title, keywords/JEL, cover letter, highlights, and submission materials.

Writing rules:

- name the game/strategy space where needed;
- do not imply the cost floor belonged to the original model;
- do not hide multiplicity in a footnote;
- do not write “the equilibrium price” when the theorem establishes only an equilibrium or a restricted-class characterization;
- at `c=3`, describe a boundary, not strict slack;
- use “limit pricing” only in the static exclusion-maintenance sense authorized by C3R;
- describe Lean certification only at the scope actually formalized.

---

## 10. Astra-2 — Second Independent Hostile Referee Gate

Run Astra only after the complete Stage-13R2 manuscript exists and before Stage 14.

Astra-2 must independently attack:

- unrestricted equilibrium characterization;
- cost-floor result and its necessity proof;
- existence / characterization / uniqueness language;
- welfare-selection scope;
- original-paper correction validity;
- Lean-certification scope;
- publication significance for the chosen journal;
- any new overclaim introduced during rewriting.

Proceed only on:

- `ACCEPTABLE FOR SUBMISSION`; or
- `MINOR EXPOSITION REPAIR`, after bounded repair and recheck.

A substantive theory defect returns to the earliest affected scientific stage.

---

## 11. Stage 14 — Submission QA

Stage 14 begins only after Astra-2 scientific clearance.

Refresh current official journal and authenticated-portal requirements, including:

- exact article type;
- anonymity and title-page rules;
- editable-source requirements;
- abstract, keywords, JEL, highlights;
- funding, competing interests, CRediT, generative-AI statement;
- data/code/supplement handling;
- reviewer fields and attestations;
- submission fee and mandatory publication charges;
- portal-generated PDF behavior.

Any material `UNVERIFIED` or unresolved `CONFLICT` blocks PASS.

The zero-fee hard gate remains in force.

---

## 12. Stage 15 — Submission Freeze / Portal Preflight / Submit

Only after Stage 14 passes:

1. freeze exact manuscript and submission artifacts;
2. record commit/tag/SHA provenance;
3. reconcile portal metadata;
4. upload the exact frozen files;
5. generate the portal PDF if supported;
6. inspect the generated PDF page by page;
7. verify equations, citations, author/anonymity information, declarations, and supplements;
8. confirm the zero-fee hard gate;
9. submit;
10. record journal confirmation and submission ID.

Do not declare `SUBMITTED` before journal confirmation is received.

---

## 13. Return rules

| New problem | Return to |
|---|---|
| New equilibrium counterexample / false theorem | C0–C1R |
| Falsification code misses relevant strategy region | C2R |
| Lean theorem fails or mathematical quantifiers change | analytic repair, then C2R-L |
| Freeze wording exceeds valid theory while theory itself is sound | C3R |
| Hostile audit finds scientific overclaim | earliest affected scientific stage |
| Journal significance/fit issue only | Stage 12R2 |
| Exposition/organization issue only | Stage 13R2 |
| Astra-2 finds mathematical defect | C0–C1R / C2R / C2R-L as applicable |
| Submission-format/metadata issue only | Stage 14 |
| Portal-only mismatch | Stage 14/15 preflight |

Do not repair a scientific defect only in prose when the underlying theorem or quantifier must change.

---

## 14. Branch / PR discipline

- one branch per recovery stage where substantive files change;
- do not retroactively rewrite the historical pre-Astra baseline;
- record the exact base commit in each stage report;
- separate scientific changes from later journal-formatting changes where practical;
- merge only after the stage's PASS/GO condition is satisfied;
- update this workflow and the root README when the active stage changes;
- retain Astra reports and counterexamples permanently as scientific provenance;
- retain Lean source, dependency pins, and CI workflow as part of the reproducibility record.

Suggested branch names:

- `reopen/c0-c1r-equilibrium-set`;
- `reopen/c2r-verification`;
- `formal/c2r-lean-certification`;
- `c3r/revised-canonical-theory-freeze`;
- `audit/c4r-hostile`;
- `stage12r2/journal-recheck`;
- `stage13r2/revised-integration`;
- `audit/astra2`;
- `stage14/submission-qa`;
- `stage15/submission-freeze`.

---

## 15. Current checklist

- [x] RIO submission closed with editorial audience-fit rejection.
- [x] International Economics selected provisionally at initial Stage 12R.
- [x] Initial International Economics integration completed at Stage 13R.
- [x] Astra identified the equilibrium-characterization defect.
- [x] Published Gandal–Shy (2001) PDF directly confirmed the quadratic specification and Appendix-B inconsistency.
- [x] Stage 14 halted.
- [x] C0–C1R Targeted Equilibrium-Set Reaudit.
- [x] C2R Symbolic/Numerical Audit.
- [x] C2R-L Lean Formal Certification.
- [x] C3R Revised Canonical Theory Freeze.
- [ ] **C4R Hostile Scientific Self-Audit — NEXT.**
- [ ] Stage 12R2 Journal Significance/Fit Recheck.
- [ ] Stage 13R2 Revised Full-Paper Integration.
- [ ] Astra-2 Independent Hostile Referee Gate.
- [ ] Stage 14 Submission QA.
- [ ] Stage 15 Submission Freeze / Portal Preflight / Submit.

---

## 16. Definition of recovery success

The scientific recovery is complete only when the revised project can answer without qualification drift:

1. **Original game:** what symmetric foreclosed pure equilibria exist, and what is nonunique?
2. **Restricted game:** under exactly what explicit cost-floor restriction is the piecewise member price characterized?
3. **Original correction:** exactly which published price profile is false and why?
4. **Welfare:** for exactly which continuation-equilibrium selection does the Proposition-3 member-country comparison survive?
5. **Formal certification:** which statements are Lean-certified, and which economic/model facts remain analytic?
6. **Publication significance:** after the stronger equilibrium-selection correction is known, is *International Economics* still the right target?

The objective is not to make the Astra counterexample disappear. The objective is to make it part of a complete, correctly quantified, reproducible account of the model.