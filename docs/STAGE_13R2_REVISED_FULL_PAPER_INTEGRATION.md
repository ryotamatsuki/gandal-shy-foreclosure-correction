# Stage 13R2 — Revised Full-Paper Integration

**Date:** 2026-09-10  
**Status:** **PASS — POST-ASTRA-2 CLEARED**  
**Branch:** `stage13r2/revised-integration`  
**Base:** `main@a312babe551c87afd203678215bb2467b36a1bff`  
**Integration PR:** `#13`  
**Pre-bookkeeping verified head:** `d9fc2a60b44b867794b5f53822e9aeb24e9a8500`  
**Bounded Astra-2 repair PR:** `#14`  
**Astra-2 limited-recheck baseline:** `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d`  
**Canonical workflow:** `ryotamatsuki/research-paper-workflow`, `templates/STAGE_13_FULL_PAPER_INTEGRATION.md`  
**Scientific authority:** `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`  
**Hostile-audit authority:** `docs/C4R_HOSTILE_SCIENTIFIC_AUDIT.md`  
**Journal-positioning authority:** `docs/STAGE_12R2_JOURNAL_SIGNIFICANCE_FIT_RECHECK.md`

## 1. Role and integration contract

Stage 13R2 converts the revised frozen theory into one coherent short paper for the provisional primary target, *International Economics*. It is an integration stage, not a research-extension stage.

The required order was followed deliberately:

1. Section 2 — published quadratic specification, corrected long-arc geometry, and exact failure of the published complete profile;
2. Section 3 — unrestricted symmetric-foreclosed multiplicity first, then the separate cost-floor characterization;
3. Section 4 — welfare under common versus market-specific continuation selection;
4. only after Sections 2–4 were aligned: title, Abstract, Introduction, Conclusion, highlights, cover letter, title page, and package notes.

No new equilibrium class, comparative static, government-stage result, refinement claim, or journal requirement was introduced here.

## 2. Controlling scientific scope

The revised manuscript distinguishes two games:

- **unrestricted original price game**, which does not exclude zero-sales below-cost outsider quotes;
- **cost-floor price game**, a separate modified game imposing `p_i >= marginal cost in that market`.

The current equilibrium characterization is limited to **symmetric, foreclosed, pure-strategy equilibria in one union-member market**. The manuscript does not imply characterization of all asymmetric pure equilibria, mixed equilibria, or the government-stage equilibrium under continuation multiplicity.

The correction target is the complete Appendix-B profile `(3/2,3/2,c)`, not the claim that member price `3/2` can never arise in equilibrium.

The welfare result is conditional: the original member-country `1/2` gap is preserved under a common symmetric continuation price, but arbitrary market-by-market continuation selection in the unrestricted game introduces the transfer term `(3/2)(s_B-s_A)`.

## 3. Stage-13R2 integration decisions

### Title direction

Final integrated working title:

> **Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)**

This moves `limit pricing` out of the headline because the stronger revised contribution is equilibrium multiplicity and continuation selection. The term remains in the text only for the bounded static exclusion-maintenance interpretation of the cost-floor lower branch.

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

The integrated manuscript, abstract, introduction, conclusion, cover letter, and highlights were audited against the following controls:

- no claim that the original game's post-foreclosure equilibrium is unique;
- no claim that member price `3/2` is impossible in equilibrium;
- no description of the cost floor as WLOG, Nash-implied, or a weak-dominance refinement;
- cost-floor results qualified by the symmetric, foreclosed, pure-strategy class;
- no claim that Proposition 3 is robust to all Nash equilibria;
- no claim that Proposition 3 reverses without solving the government stage;
- `c=3` treated as a branch boundary rather than strict slack;
- Lean certification described only at its actual algebraic/quantified-inequality scope.

**Result:** PASS. No cross-document substantive-scope conflict remains known at Stage 13R2.

## 5. Journal-package discipline

The Stage-12 requirements ledger remains an integration input, not permanent truth. Stage 13R2 keeps the working manuscript identified and retains provisional title-page/highlight/declaration artifacts without treating any unresolved anonymity, article-type, source-package, declaration-placement, or portal rule as verified.

All such unresolved items remain explicitly delegated to Stage 14. No unresolved journal rule was silently converted into a definitive submission-format assumption.

## 6. Verification and build record

The integration PR added `.github/workflows/manuscript-integration.yml` and reran the integrated package on GitHub Actions.

Initial integration verification:

- workflow: `Manuscript integration`;
- run ID: `34373368719`;
- head: `d9fc2a60b44b867794b5f53822e9aeb24e9a8500`;
- conclusion: **success**;
- symbolic verification: **PASS**;
- numerical falsification/regression verification: **PASS**;
- manuscript LaTeX build: **PASS**;
- flat LaTeX source build: **PASS**;
- title-page build: **PASS**;
- final LaTeX clean-log gate: **PASS**;
- generated artifact existence checks: **PASS**;
- build artifact: `stage13r2-build`, artifact ID `10112910001`, digest `sha256:9c342cc3616623edeb2d66d44e40f7a6b3a5078683c623c8fe57b1c28049722c`.

The final integrated manuscript was **9 pages**. The modular and flat-source builds were independently rendered and compared at 150 dpi, with **9/9 pages pixel-identical**. All nine manuscript pages and the one-page title page were visually inspected; no clipping, overlap, broken equation, broken citation, or reference-layout defect was identified.

Previously computed Stage-13R2 manuscript metrics are retained for integration QA:

- text words: `2790`;
- `texcount` sum count: `3044`;
- figures/tables: `0`;
- inline math: `144`;
- displayed math: `21`;
- Abstract: `190` words.

The bounded Astra-2 repair subsequently passed manuscript-integration run `34379361638` on repaired manuscript head `72ed861e3460cbcaf5eaf0a763f789c70ed07332`, including symbolic/numerical verification, package build, clean-log gate, generated-artifact checks, and upload.

These counts and build results are integration diagnostics, not a substitute for the fresh journal-rule audit required at Stage 14.

## 7. Section-role audit

- **Introduction:** states the international-standards problem before technical details and frames the contribution as correction plus continuation-selection analysis rather than generic novelty.
- **Section 2:** isolates the published quadratic long-arc inconsistency and the exact failure of the complete Appendix-B profile.
- **Section 3:** presents unrestricted multiplicity before the separate cost-floor benchmark and states the equilibrium class in the proposition itself.
- **Section 4:** separates common-continuation welfare robustness from market-specific continuation dependence.
- **Conclusion:** answers the research question without adding a new theory or policy result.

**Result:** PASS.

## 8. Contribution-claim and literature audit

The integrated contribution is bounded to four claims: correction of the published complete profile/equilibrium claim; characterization of unrestricted symmetric-foreclosed pure-strategy multiplicity; characterization of the separate cost-floor benchmark within the same class; and qualification of the welfare comparison by continuation selection.

`Limit pricing` is not presented as the paper's primary novelty. The manuscript does not claim general novelty for foreclosure, potential competition, or limit pricing. Existing standards/trade and limit-pricing references remain supporting context rather than evidence for an inflated novelty claim.

**Result:** PASS for Stage 13 integration. Astra-2 subsequently assessed publication significance as **MODERATE** and found no scientific blocker after bounded repair and limited recheck.

## 9. Abstract / Introduction / Conclusion alignment

The title, Abstract, Introduction, two propositions, welfare section, Conclusion, highlights, and cover letter use the same contribution hierarchy:

`published continuation claim fails`
→ `unrestricted symmetric-foreclosed continuation is multiple`
→ `explicit cost floor yields a separate piecewise benchmark`
→ `welfare robustness is continuation-selection conditional`.

**Result:** PASS.

Astra-2 initially identified two submission-artifact wording issues: the third highlight lacked the stated equilibrium-class qualifier and the cover letter overstated the common-price welfare condition. Both were repaired in PR `#14`, and the actual limited recheck on `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d` returned **PASS** on both items.

## 10. Figure/Table Architecture reconciliation

No visual is required to communicate the headline result. There is no unresolved Stage-10 exposition requirement that forces a figure or table, and no quantitative visual requires a generator audit.

**Result:** PASS — zero figures/tables is a documented design decision, not an omission.

## 11. Known journal requirements implemented versus carried forward

Implemented only as provisional package structure where already operationally useful:

- identified working manuscript;
- separate title-page draft;
- highlights draft;
- cover-letter draft;
- CRediT draft;
- flat editable LaTeX source package;
- reproducibility package containing Python checks and the pinned Lean project.

Carried forward as **UNVERIFIED / portal-dependent** for Stage 14:

- exact article-type label;
- review/anonymity model and author-information placement;
- separate-title-page requirement;
- initial PDF/editable-source upload requirements and file designations;
- LaTeX archive/folder rules;
- abstract/keyword/JEL/highlight requirements;
- declaration placement and exact CRediT/data/code/AI wording;
- reviewer-suggestion and portal-attestation fields;
- current mandatory-charge status;
- portal-generated PDF behavior.

No Stage-14 item is declared resolved by inference from the Stage-13 build.

## 12. Astra-2 bounded repair closure

Astra-2 first audited `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6` and returned **B. MINOR EXPOSITION REPAIR**. The required repairs were:

1. add the missing cost-floor proof bridge;
2. qualify the third highlight by the symmetric, foreclosed, pure-strategy scope;
3. narrow the cover-letter welfare wording.

All three were implemented and merged in PR `#14`. Astra-2 then performed the actual limited recheck on `main@ec164d092c5be14df12dbf44c40c8d947d7cdc7d` and returned:

- Repair 1 — **PASS**;
- Repair 2 — **PASS**;
- Repair 3 — **PASS**;
- new defect introduced — **NO**;
- final verdict — **A. ASTRA-2 CLEARED — GO TO STAGE 14**.

No theorem statement, numerical verifier, Lean theorem, title, abstract, or journal target changed during the bounded repair.

## 13. Remaining blockers

There is **no known Stage-13R2 or Astra-2 scientific blocker**.

The remaining work is submission QA only. Stage 14 must independently refresh *International Economics* article-type, anonymity, file/package, declaration, fee, and portal requirements. Any material `UNVERIFIED` or unresolved `CONFLICT` blocks Stage-14 PASS.

## 14. Final verdict and next-stage contract

### Executive integration verdict

**PASS.** The revised paper is internally coherent, scope-disciplined, reproducible, build-clean, and Astra-2 cleared.

### Final Stage-13R2 / Astra-2 verdict

`REVISED INTEGRATED MANUSCRIPT CLEARED FOR STAGE 14 SUBMISSION QA`

### Next-stage contract

Proceed to **Stage 14 — Submission QA**.

Stage 14 is not a theory-development stage. It must freshly verify all material *International Economics* requirements from current official sources and, where required, the authenticated portal, remaining fail-closed on any material `UNVERIFIED` or `CONFLICT`. If a Stage-14 format or metadata change would alter a theorem or scientific claim, return to the earliest affected scientific stage rather than silently modifying the frozen result.
