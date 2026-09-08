# Revision-to-Resubmission Workflow

**Project:** Gandal–Shy Foreclosure Correction  
**Status date:** 2026-09-09  
**Purpose:** Project-specific recovery workflow after the independent Astra referee audit.  
**Canonical generic workflow:** `ryotamatsuki/research-paper-workflow` v2.1.  
**Project baseline before reopening:** `main@75afb554cac868d804e8a99ec93c00fe39dda6f2`.

---

## 0. Current status and stop condition

Stage 12R and Stage 13R were completed for an intended submission to *International Economics*. An independent Astra hostile referee audit then identified a substantive equilibrium-characterization problem that was not detected by the existing verification code.

**Stage 14 is therefore BLOCKED. Do not perform submission QA, portal preflight, or submission until the scientific recovery sequence below is completed and passes.**

The Astra finding does **not** eliminate the correction itself. Direct inspection of the published Gandal and Shy (2001) article confirms that:

1. the published model uses quadratic transportation costs;
2. Appendix B uses an inconsistent long-arc price-difference coefficient;
3. the published price profile `(3/2, 3/2, c)` is not a Nash equilibrium in the relevant range; but
4. under the unrestricted price strategy space, other zero-sales outsider prices can support additional member-price equilibria, so the current manuscript confuses equilibrium existence with equilibrium characterization.

The immediate scientific task is therefore to characterize exactly what is true in the unrestricted game and what becomes true only after an explicit cost-floor restriction.

---

## 1. Governing principles for the revision

### 1.1 Preserve the valid correction; narrow overclaims

The target of the correction is the **complete published price profile**, not the isolated statement that a member price of `3/2` can never occur.

The defensible criticism is:

> Appendix B's claimed profile `(3/2, 3/2, c)` is not a Nash equilibrium under the published quadratic-transport specification.

Do **not** claim that no equilibrium can support member price `3/2` unless that stronger statement is separately proved.

### 1.2 Separate two games explicitly

The revision must distinguish:

1. **Unrestricted original price game:** use the strategy space actually stated in the published model, including zero-sales below-cost prices when not explicitly prohibited.
2. **Cost-floor price game:** impose explicitly
   `p_i >= marginal cost in that market`.

The cost-floor restriction is an additional strategy restriction. It must **not** be described as:

- “without loss of generality”;
- an implication of Nash equilibrium itself;
- “elimination of all weakly dominated strategies”; or
- a condition already imposed by Gandal and Shy (2001), unless new primary-source evidence proves that statement.

### 1.3 Keep the logical categories separate

Every theorem and prose claim must distinguish:

- `EXISTS`;
- `IS A NASH EQUILIBRIUM`;
- `CHARACTERIZES ALL EQUILIBRIA IN THE STATED CLASS`;
- `UNIQUE WITHIN THE STATED CLASS`.

No existence proof may be described as a characterization or uniqueness result.

### 1.4 State the equilibrium class exactly

The recovery work should focus first on **symmetric, foreclosed, pure-strategy equilibria**. It is not necessary to solve every asymmetric or mixed equilibrium unless a theorem is written broadly enough to require doing so.

If asymmetric equilibria are not fully characterized, the manuscript must say so and must not use language that quantifies over all Nash equilibria.

### 1.5 Welfare claims must match equilibrium selection

The previous welfare cancellation is valid under a common symmetric member price across the two union markets. It is not automatically selection-free when different continuation equilibria can be selected market by market.

The revision must state exactly:

- which equilibrium selection is used;
- when `TS_M^SU = 3V + 1/4` is price-independent; and
- when cross-market price differences create additional transfer terms.

Do not claim that the original policy conclusion is reversed without solving the relevant government-stage equilibrium.

---

## 2. Mandatory recovery sequence

The project-specific sequence is:

```text
C0–C1R  Targeted Equilibrium-Set Reaudit
   ↓
C2R     Symbolic / Numerical Counterexample and Global-Deviation Audit
   ↓
C2R-L   Lean Formal Certification
   ↓
C3R     Revised Canonical Theory Freeze
   ↓
C4R     Hostile Scientific Self-Audit
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

**No stage may be skipped merely because an earlier version had previously passed.**

---

## 3. C0–C1R — Targeted Equilibrium-Set Reaudit

### Objective

Re-open only the affected scientific core: post-foreclosure price equilibrium, equilibrium multiplicity, strategy restrictions, and the welfare scope that depends on equilibrium selection.

### 3.1 Published-profile correction

Re-derive from primitives:

`p_1 + x^2 = p_2 + (2-x)^2`

and confirm

`x = 1 + (p_2-p_1)/4`.

Keep a direct counterexample to the published profile. The canonical simple checkpoint is `c=4`:

- published profile: `(3/2, 3/2, 4)`;
- member deviation: `p_1 = 7/4`;
- profit rises from `9/4` to `147/64`.

This is enough to refute the published claim that that complete price profile is a Nash equilibrium.

### 3.2 Unrestricted original game

Characterize, within the stated theorem class, what symmetric foreclosed pure-strategy equilibria exist when the published strategy space is left unrestricted.

At minimum, the audit must handle analytically the candidate family

`(p_1,p_2,p_3) = (s,s,s+1)`

for

`3/2 <= s <= min{2,c-1}`.

Do not freeze this family as the **complete** characterization until necessity has been proved for the exact theorem class.

The audit must answer:

1. which `s` values are sufficient for equilibrium;
2. whether any other symmetric foreclosed pure equilibria exist;
3. what happens at `c=5/2` and `c=3`;
4. how outsider-price nonuniqueness changes member best responses;
5. whether any theorem requires asymmetric pure equilibria to be checked rather than merely searched for counterexamples.

### 3.3 Cost-floor game

Define an explicit restricted game in which each firm must satisfy

`p_i >= mc_i`

in the market in question.

For a union member market, this means member prices are nonnegative and the outsider satisfies `p_3 >= c`.

Within **symmetric foreclosed pure-strategy equilibria**, prove both necessity and sufficiency of the member-price characterization, if true:

`p_M = c-1` for `5/2 < c < 3`,

`p_M = 2` for `3 <= c < 5`.

The result must identify precisely what remains nonunique, especially the zero-sales outsider price when `c >= 3`.

Do not state “the unique Nash equilibrium” unless all prices and all equilibria in the relevant strategy class have actually been proved unique.

### 3.4 Welfare scope

Re-derive welfare from the published welfare definition, including worldwide profit of the domestic firm.

For a common symmetric member price `s` in both union markets, verify:

`TS_M^SU = 3V + 1/4`.

For potentially different symmetric continuation prices `s_A` and `s_B`, verify the relevant country-specific expression, currently expected to be

`TS_A^SU = 3V + 1/4 + (3/2)(s_B-s_A)`.

Then state exactly which equilibrium selection supports the original Proposition-3 ranking.

### C0–C1R PASS criteria

C0–C1R passes only if the project can answer, in theorem-ready form:

1. What equilibria exist in the unrestricted original game within the stated equilibrium class?
2. What is and is not unique?
3. Under exactly what additional cost-floor restriction is the piecewise member price characterized?
4. Under what equilibrium-selection condition does the welfare ranking survive?

If any answer is unknown, C0–C1R remains open.

---

## 4. C2R — Symbolic / Numerical Counterexample and Global-Deviation Audit

### Objective

Build a falsification layer that searches the strategy space relevant to the revised theorems. The numerical code is evidence and regression protection, not the proof itself.

### Required changes to verification

The previous numerical verifier fixed `p_3=c`; this is no longer sufficient.

The revised verifier must be able to:

- vary `p_1`, `p_2`, and `p_3`;
- include zero-sales below-cost outsider prices in unrestricted mode;
- switch the cost-floor restriction ON/OFF;
- search global member deviations, not only local deviations;
- search outsider deviations;
- test representative asymmetric member-price perturbations;
- stress `c=5/2`, `c=3`, and near-boundary values;
- preserve the Astra counterexample and the published-profile counterexample as permanent regression tests;
- distinguish `candidate verified` from `equilibrium set characterized`.

### C2R PASS criteria

- Every analytic theorem has dedicated numerical falsification tests.
- No counterexample is found in a domain the theorem claims to cover.
- Every discovered counterexample is retained as a regression test.
- Numerical PASS is never used as a substitute for necessity/globality proofs.

---

## 5. C2R-L — Lean Formal Certification

### Timing

Lean enters **after the analytic theorem statements are fixed by C0–C1R and after the falsification design is stabilized in C2R, but before C3R theory freeze**.

Do not formalize a moving theorem statement.

### Minimum Lean targets

Formalize at least the following high-stakes objects where feasible:

1. **Long-arc correction**
   - derive the coefficient `1/4` from the quadratic indifference equation.
2. **Published-profile counterexample**
   - certify the exact rational profit improvement at `c=4`.
3. **Unrestricted-game multiplicity result**
   - certify the sufficient global best-response inequalities for the additional symmetric foreclosed equilibrium family.
4. **Cost-floor characterization**
   - formalize both existence and the necessity direction for the member price within the exact theorem class.
5. **Welfare identities**
   - common-price cancellation;
   - cross-market price-difference expression if retained in the paper/theory record.

### Lean scope discipline

The Lean theorem statement must reproduce the manuscript quantifiers exactly:

- parameter interval;
- strategy domain;
- symmetry;
- foreclosure condition;
- pure-strategy restriction;
- existence versus necessity versus uniqueness.

A theorem that proves only a restricted algebraic lemma may not be cited internally as formal certification of a broader equilibrium claim.

### C2R-L PASS criteria

- All designated headline formal theorems compile without `sorry`/admitted gaps.
- The Lean statements match the intended C3R freeze claims exactly.
- Any theorem not formalized is explicitly labeled as such rather than implicitly treated as Lean-certified.

If later audits change a theorem's mathematical content or quantifiers, return to C2R-L before refreezing.

---

## 6. C3R — Revised Canonical Theory Freeze

### Objective

Freeze only the strongest claims supported by the completed analytic, numerical, and Lean certificates.

A likely compact theorem architecture is:

### Proposition 1 — Post-foreclosure pricing

Potential components, subject to proof:

1. the published Appendix-B profile `(3/2,3/2,c)` is not Nash under the published quadratic specification;
2. the unrestricted original game admits additional symmetric foreclosed equilibria, so the published uniqueness claim fails more deeply than a single price correction;
3. under the explicit cost-floor strategy restriction, the member price within symmetric foreclosed pure equilibria is characterized by the piecewise formula.

### Proposition 2 — Welfare

State separately:

- the common symmetric continuation under which the original member-country welfare ranking survives; and
- the fact that unrestricted market-by-market equilibrium selection need not preserve the same price-transfer cancellation.

### Freeze record must state

- exact game definition for each proposition;
- exact equilibrium class;
- exact parameter domain;
- existence/necessity/uniqueness status;
- which claims are Lean-certified;
- which claims are analytic-only but independently falsified numerically;
- prohibited stronger wording.

No manuscript rewrite should outrun this freeze.

---

## 7. C4R — Hostile Scientific Self-Audit

### Objective

Attempt to destroy the revised frozen theory before journal positioning resumes.

Mandatory attacks:

- hidden outsider-price equilibria;
- hidden asymmetric pure equilibria insofar as they threaten the stated theorem scope;
- below-cost and zero-demand strategies;
- boundary cases `c=5/2` and `c=3`;
- domain of the two-firm demand formula;
- tie-breaking / measure-zero consumers;
- exact meaning of “foreclosed” and “limit pricing”;
- cost-floor restriction versus the original model;
- cross-market equilibrium selection and welfare;
- any sentence that upgrades existence to characterization or characterization to uniqueness.

### C4R verdicts

- `PASS — GO TO STAGE 12R2`
- `CONDITIONAL — BOUNDED SCIENTIFIC REPAIR`
- `FAIL — RETURN TO C0–C1R`

A mathematical change to a frozen theorem requires re-running affected C2R and C2R-L checks.

---

## 8. Stage 12R2 — Journal Significance / Fit Recheck

### Why this stage must be repeated

The contribution has changed materially. The revised paper may no longer be merely:

`wrong post-foreclosure price -> corrected piecewise price -> welfare ranking survives`.

It may instead become:

`published claimed unique equilibrium is false -> unrestricted game has multiplicity -> an explicit cost-floor restriction characterizes the economically disciplined member price -> welfare robustness depends on equilibrium selection`.

That change may improve or weaken publication significance; it must be assessed from scratch rather than inherited from the prior Stage 12R.

### Primary journal

*International Economics* remains the provisional target, subject to the Stage-12R2 significance/fit audit and the author's zero-fee hard gate.

### Stage 12R2 outputs

- updated contribution statement;
- updated desk-reject risk;
- updated International Economics fit;
- updated short-paper publication-significance assessment;
- zero-fee ladder refresh if needed;
- `GO TO STAGE 13R2`, `REPOSITION`, or `CHANGE JOURNAL TARGET`.

---

## 9. Stage 13R2 — Revised Full-Paper Integration

### Required order of revision

Do **not** start with the Introduction.

Revise in this order:

1. **Section 2:** published specification, long-arc error, and exact published-profile failure.
2. **Section 3:** unrestricted equilibrium multiplicity and cost-floor characterization.
3. **Section 4:** welfare under the exact equilibrium-selection conditions.
4. **Only then:** Abstract, Introduction, Conclusion, title, keywords/JEL, cover letter and submission materials.

### Writing discipline

- Say exactly which game is being discussed in every key proposition.
- Do not imply the cost-floor restriction was part of the published model.
- Do not hide multiplicity in a footnote.
- Do not say “the equilibrium price” where only one equilibrium or one restricted equilibrium class has been established.
- At `c=3`, describe the branches as meeting at the boundary; do not call the exclusion constraint strictly slack there.
- Keep “limit pricing” only with the explicit static exclusion-maintenance interpretation; do not imply informational signaling or a separate entry stage.

### Stage 13R2 PASS criteria

- Abstract / Introduction / Conclusion match C3R exactly.
- No stale pre-Astra claim remains.
- All theorem qualifiers are visible where needed.
- Submission package is structurally ready for Stage 14 but still treats live journal rules as unverified until Stage 14.

---

## 10. Astra-2 — Second Independent Hostile Referee Gate

### Timing

Run Astra only **after Stage 13R2 produces the complete revised manuscript** and before Stage 14.

Astra-2 must be given the revised paper as a fresh hostile referee and instructed to check:

- the unrestricted-game equilibrium characterization;
- the cost-floor result and its necessity proof;
- existence versus characterization versus uniqueness language;
- welfare-selection scope;
- original-paper correction validity;
- publication significance for *International Economics*;
- whether any new overclaim has been introduced during rewriting.

### Astra-2 gate

Proceed only on:

- `ACCEPTABLE FOR SUBMISSION`; or
- `MINOR EXPOSITION REPAIR`, after those bounded repairs are completed and checked.

If Astra-2 identifies a substantive theory defect, return to C0–C1R/C2R/C2R-L as applicable.

---

## 11. Stage 14 — Submission QA

Stage 14 remains the canonical v2.1 submission-compliance gate. It begins **only after Astra-2 scientific clearance**.

Re-open all current *International Economics* rules from official sources and the authenticated portal, including:

- exact article type;
- anonymity / author placement;
- title page;
- editable source requirements;
- abstract / keywords / JEL / highlights;
- funding / competing interests / CRediT / generative-AI statement;
- data/code/supplement handling;
- reviewer fields and attestations;
- submission fee and any mandatory publication charge;
- portal-generated PDF behavior.

Any material `UNVERIFIED` or unresolved `CONFLICT` blocks `SUBMISSION QA PASS`.

The zero-fee hard gate remains in force: if a mandatory author charge appears, stop and do not submit under the current target choice.

---

## 12. Stage 15 — Submission Freeze / Portal Preflight / Submit

Only after Stage 14 passes:

1. freeze exact manuscript and submission artifacts;
2. record commit/tag/SHA provenance;
3. reconcile all metadata in the authenticated portal;
4. upload the exact frozen files;
5. generate the portal PDF if supported;
6. inspect the generated PDF page by page;
7. verify equations, citations, author information/anonymity, declarations and supplements;
8. confirm no mandatory fee violates the hard gate;
9. submit;
10. record journal confirmation and submission ID.

`SUBMITTED` may not be declared before journal confirmation is received.

---

## 13. Return rules

Use the earliest affected-stage rule.

| New problem discovered | Return to |
|---|---|
| New equilibrium counterexample / false theorem | C0–C1R |
| Numerical verifier misses relevant strategy region | C2R |
| Lean theorem fails or theorem quantifiers change | C2R-L after analytic repair |
| Freeze wording exceeds proof but theory itself is correct | C3R |
| Hostile audit finds scientific overclaim | earliest scientific stage affected |
| Journal significance/fit problem only | Stage 12R2 |
| Exposition/organization only | Stage 13R2 |
| Astra-2 finds mathematical defect | C0–C1R or C2R-L as applicable |
| Submission-format/metadata defect only | Stage 14 |
| Portal-only mismatch after QA | Stage 14/15 preflight |

Do not repair a scientific defect only in prose if the underlying theorem or quantifier must change.

---

## 14. Branch / PR discipline

To keep provenance auditable:

- use one branch per recovery stage where substantive files change;
- do not edit the historical pre-Astra baseline retroactively;
- record the exact base commit in each stage report;
- keep mathematical changes separate from later journal-formatting changes where practical;
- merge only after that stage's stated PASS/GO condition is satisfied;
- update this file and the root `README.md` whenever the active stage changes;
- preserve Astra reports/counterexamples as permanent scientific provenance rather than deleting them after repair.

Suggested branch names:

- `reopen/c0-c1r-equilibrium-set`
- `reopen/c2r-verification`
- `formal/c2r-lean-certification`
- `freeze/c3r-revised-theory`
- `audit/c4r-hostile`
- `stage12r2/journal-recheck`
- `stage13r2/revised-integration`
- `audit/astra2`
- `stage14/submission-qa`
- `stage15/submission-freeze`

---

## 15. Current checklist

- [x] RIO submission closed with editorial audience-fit rejection.
- [x] International Economics selected provisionally at Stage 12R.
- [x] Initial International Economics integration completed at Stage 13R.
- [x] Astra independent referee identified equilibrium-characterization defect.
- [x] Published Gandal–Shy (2001) PDF directly confirms quadratic specification and Appendix-B long-arc inconsistency.
- [x] Stage 14 halted.
- [ ] **C0–C1R Targeted Equilibrium-Set Reaudit** — NEXT.
- [ ] C2R Symbolic/Numerical Audit.
- [ ] C2R-L Lean Formal Certification.
- [ ] C3R Revised Canonical Theory Freeze.
- [ ] C4R Hostile Scientific Self-Audit.
- [ ] Stage 12R2 Journal Significance/Fit Recheck.
- [ ] Stage 13R2 Revised Full-Paper Integration.
- [ ] Astra-2 Independent Hostile Referee Gate.
- [ ] Stage 14 Submission QA.
- [ ] Stage 15 Submission Freeze / Portal Preflight / Submit.

---

## 16. Definition of recovery success

The scientific recovery is complete only when the revised project can answer, without qualification drift:

1. **Original game:** What symmetric foreclosed pure equilibria exist, and what is not unique?
2. **Restricted game:** Under exactly what explicit cost-floor condition is the piecewise member price characterized?
3. **Original correction:** Exactly which published price profile is false and why?
4. **Welfare:** For exactly which continuation-equilibrium selection does the Proposition-3 member-country ranking survive?
5. **Formal certification:** Which of those statements have been Lean-certified with matching quantifiers?
6. **Publication significance:** After the stronger equilibrium-selection correction is known, is *International Economics* still the correct target?

The revision objective is **not** to make the Astra counterexample disappear. The objective is to make the counterexample part of a complete and correctly scoped account of the model.
