# Stage 13R2 — Revised Full-Paper Integration

**Date:** 2026-09-10  
**Branch:** `stage13r2/revised-integration`  
**Base:** `main@a312babe551c87afd203678215bb2467b36a1bff`  
**Canonical workflow:** `ryotamatsuki/research-paper-workflow`, `templates/STAGE_13_FULL_PAPER_INTEGRATION.md`  
**Scientific authority:** `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`  
**Hostile-audit authority:** `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`  
**Journal-positioning authority:** `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`

## 1. Role and integration contract

Stage 13R2 converts the revised frozen theory into one coherent short paper for the provisional primary target, *International Economics*. It is an integration stage, not a research-extension stage.

The required order is followed deliberately:

1. Section 2 — published quadratic specification, corrected long-arc geometry, and exact failure of the published complete profile;
2. Section 3 — unrestricted symmetric-foreclosed multiplicity first, then the separate cost-floor characterization;
3. Section 4 — welfare under common versus market-specific continuation selection;
4. only after Sections 2–4 are aligned: title, Abstract, Introduction, Conclusion, highlights, cover letter, title page, and package notes.

No new equilibrium class, comparative static, government-stage result, refinement claim, or journal requirement is introduced here.

## 2. Controlling scientific scope

The revised manuscript must distinguish two games:

- **unrestricted original price game**, which does not exclude zero-sales below-cost outsider quotes;
- **cost-floor price game**, a separate modified game imposing `p_i >= marginal cost in that market`.

The current equilibrium characterization is limited to **symmetric, foreclosed, pure-strategy equilibria in one union-member market**. The manuscript must not imply characterization of all asymmetric pure equilibria, mixed equilibria, or the government-stage equilibrium under continuation multiplicity.

The correction target is the complete Appendix-B profile `(3/2,3/2,c)`, not the claim that member price `3/2` can never arise in equilibrium.

The welfare result is conditional: the original member-country `1/2` gap is preserved under a common symmetric continuation price, but arbitrary market-by-market continuation selection in the unrestricted game introduces the transfer term `(3/2)(s_B-s_A)`.

## 3. Stage-13R2 integration decisions

### Title direction

Primary integrated title:

> **Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)**

This moves `limit pricing` out of the headline because the stronger revised contribution is equilibrium multiplicity and continuation selection. The term remains available in the text only for the static exclusion-maintenance interpretation of the cost-floor lower branch.

### Proposition architecture

The paper retains two headline propositions.

**Proposition 1 — Post-foreclosure pricing and multiplicity**

- the published Appendix-B profile is not Nash in the strict post-foreclosure range;
- the unrestricted game has the exact U1/U2 symmetric-foreclosed pure-strategy equilibrium set;
- the explicit cost-floor game yields the F1/F2 member-price characterization within the same stated class.

**Proposition 2 — Welfare under continuation selection**

- common symmetric continuation yields `TS_M^SU=3V+1/4` and gap `1/2` over mutual recognition;
- market-specific symmetric continuation prices yield `TS_A^SU=3V+1/4+(3/2)(s_B-s_A)`;
- therefore the unrestricted welfare comparison is not selection-free.

### Figures and tables

No figure or table is added. The headline objects are compact theorem statements and piecewise equilibrium sets. A decorative equilibrium diagram would add little information and could create a parallel source of scope ambiguity. The no-figure/no-table architecture is therefore deliberate.

## 4. Cross-document claim discipline

The integrated manuscript, abstract, introduction, conclusion, cover letter, and highlights must all obey the following:

- do not write that the original game's post-foreclosure equilibrium is unique;
- do not write that member price `3/2` is impossible in equilibrium;
- do not describe the cost floor as WLOG, implied by Nash equilibrium, or a weak-dominance refinement;
- qualify the cost-floor result by the symmetric, foreclosed, pure-strategy class;
- do not say that Proposition 3 is robust to all Nash equilibria;
- do not claim that Proposition 3 reverses without solving the government stage;
- at `c=3`, describe a branch boundary rather than strict slack;
- do not overstate Lean as a full formalization of the Salop game.

## 5. Journal-package discipline

The Stage-12 requirements ledger remains an integration input, not permanent truth. Stage 13R2 keeps the working manuscript identified and retains provisional title-page/highlight/declaration artifacts without treating any unresolved anonymity, article-type, source-package, declaration-placement, or portal rule as verified.

All such unresolved items remain explicitly delegated to Stage 14 after Astra-2.

## 6. Verification contract

Before Stage 13R2 can pass:

- all revised sections must be checked against C3R/C4R scope;
- manuscript/title/cover-letter/highlight claims must align;
- stale pre-Astra claims must be removed;
- symbolic/numerical and Lean evidence must remain untouched unless a theorem changes;
- build/compile and source-package verification must be rerun where feasible;
- any material scientific inconsistency returns to the earliest affected C-stage.

## 7. Current status

**ACTIVE.** The paper has not yet been cleared for Astra-2 or Stage 14.
