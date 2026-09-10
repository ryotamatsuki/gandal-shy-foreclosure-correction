# Stage 14 — Submission QA

**Date:** 2026-09-10  
**Primary journal:** *International Economics* (Elsevier)  
**Working title:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Stage-14 branch:** `stage14/submission-qa`  
**Scientific baseline entering Stage 14:** `main@9f1839a941470a411e6236f9d6848e352dc44490`  
**Theory authority:** `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`  
**Hostile-review authority:** `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`  
**Journal ledger:** `docs/JOURNAL_REQUIREMENTS_LEDGER.md`  
**Canonical verdict:** **CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**

## 1. Executive QA result

Astra-2 cleared the scientific manuscript before Stage 14. Stage 14 therefore treated the theory and substantive interpretation as frozen and performed only submission-quality, reproducibility, disclosure, source-package, journal-rule, formal-verification-rebuild, and visual QA.

No theorem statement, equation, equilibrium characterization, welfare claim, title, abstract, citation claim, numerical verifier, or Lean theorem was changed.

The non-portal submission package now passes all locally executable Stage-14 checks. The only remaining blockers are authenticated Editorial Manager / journal-Guide items that cannot be established reliably from the public or unauthenticated surfaces available here.

## 2. Current journal-rule refresh

Current official *International Economics* information uses both `Short communication` and `Short paper` terminology. The public Short paper description allows at most 7,000 words, subtracts 200 words per table/figure, permits at most five exhibits, and requires the contribution to be assessable from the main text without reliance on appendices.

The current paper has no figures, no tables, and no appendix. Its theory/results are in the main text. The exact article-type label must nevertheless be taken from the authenticated live submission system because the public journal surface itself uses both labels.

The journal-specific ScienceDirect Guide target returned HTTP 403 in the Stage-14 retrieval environment. Requirements not established from another current official surface remain `UNVERIFIED` rather than guessed.

## 3. Stage-14 CI and reproducibility result

Final Stage-14 head used for the strengthened QA workflow:

`a227b461fcf7287c27456c2697454334fce550dd`

GitHub Actions:

- workflow: `Stage 14 submission QA`;
- run: `34425158086`;
- result: **SUCCESS**.

The final workflow passed all of the following:

1. checkout;
2. rebuild of the frozen Lean proof-critical certificate with the pinned Lean/mathlib project;
3. explicit rejection of `sorry` / `admit` tokens in certified Lean source;
4. Python dependency setup;
5. LaTeX toolchain setup;
6. symbolic and numerical verification;
7. manuscript and submission-package build;
8. Python Stage-14 submission-package audit;
9. clean final LaTeX-log gate;
10. generated-artifact checks;
11. artifact upload.

This final CI update implements the post-v2.1 generic-workflow Formal Verification Gate at submission QA: applicable formal artifacts are rebuilt rather than merely copied into the package. It does not expand the certified Lean scope. Lean still certifies the proof-critical algebraic and quantified-inequality core, not the complete Salop demand correspondence or all Nash equilibria from primitives.

## 4. Automated package diagnostics

The successful Stage-14 Python audit reported:

- abstract: **201 words**;
- manuscript source-token diagnostic: **3,820**;
- keywords: **6**;
- highlights: **4**;
- highlight character counts: **73 / 75 / 82 / 72**;
- flat LaTeX archive: **8 files**, no subdirectories.

The final manuscript build is **9 pages**. The title page is **1 page**.

The source archive contains exactly the flat manuscript source set required by the project build: `main.tex`, `preamble.tex`, `references.bib`, and the five section files. The reproducibility archive contains the symbolic/numerical scripts, requirements file, Lean source, pinned toolchain, Lake configuration, and lock manifest.

## 5. Symbolic / numerical regression result

The Stage-14 run re-executed the frozen symbolic and numerical falsification suite. All checks passed, including:

- corrected long-arc coefficient;
- cost-floor and boundary identities;
- welfare identities;
- exact published-profile counterexample checks;
- 91 valid-family equilibrium-regression profiles;
- Astra counterexample retention;
- necessity regressions;
- asymmetric-perturbation diagnostics;
- grid-convergence check.

No numerical result is treated as proof; these remain falsification/regression diagnostics supporting the analytic theorem.

## 6. Lean formal-verification status

The project already passed C2R-L formal certification. Stage 14 now additionally rebuilt that frozen formal source inside the submission-QA workflow and reran the admitted-proof gate.

**Formal-verification state:** `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE`.

The certified scope remains bounded to the recorded algebraic / quantified-inequality core. In particular, the proof assistant is not claimed to derive the complete economic demand correspondence, the full Nash-equilibrium correspondence, asymmetric/mixed equilibria, or the government stage from primitives.

No Lean theorem or encoded hypothesis changed in Stage 14, so no scientific/formal rollback was triggered.

## 7. PDF parity and visual QA

The Stage-14 CI artifact contained both:

- the ordinary manuscript PDF; and
- the PDF rebuilt from the flat source archive.

Both PDFs were rendered independently at 180 dpi and compared page by page. Result:

- pages compared: **9 / 9**;
- changed pages: **0**;
- pixel difference: **0.0% on every page**.

The 9-page manuscript was also visually inspected page by page after the Stage-14 disclosure additions. No clipping, overlap, malformed glyphs, broken equations, missing text, unreadable references, or other visible layout defect was found.

The 1-page title-page PDF was separately rendered and visually inspected. No visible layout defect was found.

**Visual QA:** PASS.  
**Flat-source rebuild parity:** PASS.

## 8. Highlights / keywords / JEL

Current Elsevier highlights guidance requires 3–5 highlights and at most 85 characters each. The four submitted highlights pass the automated character-count gate.

The manuscript contains six keywords. JEL codes remain F13, L13, and L15. Their content is frozen; any exact portal classification fields are live-system matters.

## 9. Review/anonymity and author identification

The package retains both an identified manuscript and a separate identified title page. The journal-specific Guide could not be directly retrieved in this environment, so the review/anonymity model and title-page upload designation are not inferred from memory.

If the authenticated portal requires anonymization, that is a bounded Stage-14 compliance repair: generate the required anonymous artifact, rebuild, inspect, and refreeze before final submission.

**Status:** `UNVERIFIED — AUTHENTICATED PORTAL/GUIDE`.

## 10. LaTeX / editable-source package

Elsevier Editorial Manager LaTeX support requires a processable archive with all source/style files and does not support subfolders. The generated archive is flat and passes the Stage-14 package audit. It also rebuilds to a PDF pixel-identical to the ordinary manuscript build.

The exact upload item type and whether both PDF and editable source are required at initial submission remain portal-specific.

## 11. Declarations and AI policy

Stage 14 synchronized:

- funding statement;
- competing-interest statement;
- sole-author CRediT statement;
- data/code/reproducibility description;
- generative-AI disclosure.

The AI disclosure distinguishes research/verification support from manuscript-preparation support, does not treat AI output as proof or primary data, and retains human responsibility for checking mathematics, sources, code, and final prose.

These are disclosure/compliance changes only.

## 12. Figure/table and artwork QA

No figures or tables are used by design. Figure/table regeneration, raster DPI, vector-font, color-accessibility, and separate artwork-file checks are therefore `NOT APPLICABLE`, consistent with the frozen exposition architecture rather than omitted work.

## 13. Fees and access — hard gate

The public journal information does not display a submission-fee flag, and Elsevier provides a standard subscription-publication route distinct from optional open access. That is sufficient to continue preflight but not sufficient to clear the project's hard zero-cost rule.

The actual authenticated submission must confirm both:

1. **submission fee = 0**; and
2. **mandatory standard subscription-route publication/page/APC charge = 0**.

Any mandatory charge shown for the actual submission blocks submission.

**Status:** `UNVERIFIED — AUTHENTICATED PORTAL HARD GATE`.

## 14. Authenticated portal preflight blockers

The unresolved live-operational set is recorded in `submission/PORTAL_PREFLIGHT_CHECKLIST.md` and includes:

- exact short-format article-type label;
- review/anonymity and title-page configuration;
- initial PDF/LaTeX/source upload designations;
- journal-specific abstract cap if enforced by the live system;
- highlights designation;
- ORCID/JEL/classification/editor/topic/reviewer fields;
- funding/conflict/CRediT/data/code/AI/originality attestations;
- portal-generated PDF compilation and page-by-page review;
- submission-fee hard gate;
- mandatory-publication/page/APC-charge hard gate.

These items require the authenticated submission record or a journal-specific Guide surface unavailable to the present environment.

## 15. Canonical Stage-14 verdict

All non-portal Stage-14 checks are complete and passed:

- scientific freeze integrity: PASS;
- symbolic/numerical regression: PASS;
- Lean rebuild / admitted-proof gate: PASS;
- manuscript build: PASS;
- flat-source build: PASS;
- Python package audit: PASS;
- clean LaTeX-log gate: PASS;
- source archive structure: PASS;
- ordinary-vs-flat PDF pixel parity: PASS;
- manuscript visual QA: PASS;
- title-page visual QA: PASS.

The authenticated portal requirements remain material and unverified. Therefore the strongest valid verdict is:

`CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.

This is a successful Stage-14 exit into Stage 15 preflight, not permission to declare the paper submitted.

## 16. Stage-15 contract

Stage 15 may now:

1. freeze the exact Stage-14-approved artifact set and canonical repository SHA;
2. preserve build and formal-verification provenance;
3. open/reconcile the authenticated Editorial Manager submission record;
4. resolve every item in `submission/PORTAL_PREFLIGHT_CHECKLIST.md`;
5. upload only the frozen artifacts or bounded compliance-only descendants;
6. inspect the portal-generated submission PDF page by page;
7. confirm both zero-cost hard gates;
8. permit final submit only after all material portal items are PASS;
9. record journal confirmation and submission ID before declaring `SUBMITTED`.

A portal-requested file-format, anonymity, declaration-placement, or metadata repair returns to Stage 14 for bounded compliance repair and fresh affected QA. Any scientific change returns to the earliest affected scientific stage.
