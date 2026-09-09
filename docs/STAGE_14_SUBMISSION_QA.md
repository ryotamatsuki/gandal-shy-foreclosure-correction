# Stage 14 — Submission QA

**Date:** 2026-09-10  
**Primary journal:** *International Economics* (Elsevier)  
**Working title:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Stage-14 branch:** `stage14/submission-qa`  
**Scientific baseline entering Stage 14:** `main@9f1839a941470a411e6236f9d6848e352dc44490`  
**Theory authority:** `docs/C3R_REVISED_CANONICAL_THEORY_FREEZE.md`  
**Hostile-review authority:** `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`  
**Journal ledger:** `docs/JOURNAL_REQUIREMENTS_LEDGER.md`  
**Current status:** **ACTIVE — CI / local visual QA pending**

## 1. Executive QA status

Astra-2 has cleared the scientific manuscript. Stage 14 therefore treats the theory and substantive interpretation as frozen and performs only submission-quality, reproducibility, disclosure, source-package, and journal-rule work.

Fresh official-source research on 2026-09-10 confirms the journal's short-paper architecture and several publisher-wide operational rules. It also confirms that a number of item types and metadata choices remain live-portal dependent. Those unknowns are recorded explicitly rather than inferred.

Stage 14 has made only compliance-level changes:

1. added a synchronized sole-author CRediT statement to the manuscript;
2. separated generative-AI research/verification use from manuscript-preparation use and aligned the disclosure language with current Elsevier policy;
3. created an auditable journal-requirements ledger;
4. added an authenticated portal preflight checklist;
5. added a Python Stage-14 package audit and integrated it into CI.

No theorem statement, equation, equilibrium characterization, welfare claim, title, abstract, citation claim, numerical verifier, or Lean theorem was changed.

## 2. Current journal-rule refresh

Current official *International Economics* information states that the journal publishes applied international economics including trade and trade policy. The journal page calls one additional submission form `Short communication` while separately describing a `Short paper` section. The Short paper section allows at most 7,000 words, subtracts 200 words per table/figure, permits at most five exhibits, and requires the contribution to be assessable from the main text without reliance on appendices.

The current paper has no figures, no tables, and no appendix. Its theory/results are in the main text. The exact article-type label in Editorial Manager must nevertheless be taken from the live portal because the public journal page itself uses both labels.

The journal-specific ScienceDirect Guide target was opened from the current journal page but returned HTTP 403 in the Stage-14 retrieval environment. Requirements that cannot be established from another current official surface are therefore not guessed. They are carried to authenticated preflight.

## 3. Manuscript-format and length result

The Stage-13R2 integrated manuscript was nine pages with a `texcount` sum count of 3,044 before the Stage-14 disclosure additions. The only Stage-14 manuscript additions are disclosure/CRediT prose; the scientific body is unchanged. The 7,000-word short-paper ceiling therefore has very large margin.

A fresh Stage-14 Python audit is run in CI to report abstract words, keyword count and highlight character counts. It also checks for stale `TODO`/`TBD`/`PLACEHOLDER`/`FIXME` markers.

**Status:** pending the Stage-14 CI record; no known length blocker.

## 4. Highlights / keywords / JEL

Current general Elsevier guidance limits keywords to six. The manuscript contains six.

Current Elsevier highlights support specifies 3–5 highlights, each at most 85 characters including spaces. The package contains four; the automated Stage-14 check enforces both count and character limit. The exact portal item/file format remains a live-system matter.

JEL codes are F13, L13, and L15. Their content is stable; exact live classification fields remain portal-dependent.

## 5. Review/anonymity and author identification

The Stage-14 package retains both:

- an identified `paper/main.tex`; and
- a separate identified `submission/title_page.tex`.

The current journal-specific Guide could not be directly retrieved in this environment, so Stage 14 does not infer the review/anonymity model or title-page designation from memory. The authenticated portal must determine which combination is uploaded. If anonymization is required, Stage 14 must generate and inspect the corresponding anonymous artifact before final submit.

**Status:** `UNVERIFIED — AUTHENTICATED PORTAL/GUIDE`.

## 6. LaTeX / editable-source package

Elsevier's current Editorial Manager LaTeX support states that ZIP and `tar.gz` archives are supported, that all required source/style files must be present, and that LaTeX submissions containing subfolders cannot be processed.

The repository's `submission/build_flat_package.py` creates a one-level ZIP containing the `.tex`, preamble, `.bib`, and section source files. `code/stage14_submission_audit.py` fails if the generated archive contains a subdirectory or omits `main.tex`, `preamble.tex`, or `references.bib`.

The exact live upload item type and whether both PDF and editable source are required at initial submission remain portal-specific.

## 7. Declarations and AI policy

Funding wording matches Elsevier's recommended no-specific-grant sentence. Competing-interest wording is present and must be reconciled with the portal field.

A sole-author CRediT statement has been placed in the manuscript and synchronized with `submission/credit_statement.md`. Elsevier's current CRediT guidance says roles should be provided during submission and that the published statement appears above acknowledgments.

Current Elsevier generative-AI policy requires a separate disclosure for material AI-assisted manuscript preparation and says research-process use should be transparently described rather than allowing AI output to substitute for human critical evaluation. The revised manuscript now distinguishes:

- research/verification support: algebraic cross-checking and assistance in drafting portions of symbolic/numerical verification code, with no AI output treated as proof or primary data and with independent checking; and
- manuscript preparation: source searching, organization, drafting, language and readability, followed by author review/editing and source checking.

These are disclosure changes only and do not alter the scientific result.

## 8. Data, code, reproducibility and Lean

No empirical data are used. The reproducibility package contains symbolic/numerical verification and the pinned Lean project. The substantive scope of the Lean certification remains unchanged: proof-critical algebraic and quantified-inequality core, not a complete formal derivation of the Salop demand correspondence or all Nash equilibria.

Stage-14 CI reruns the existing symbolic and numerical verification before building the manuscript and packages, then runs the new package audit.

**Status:** pending fresh Stage-14 CI execution.

## 9. Figure/table and artwork QA

Stage 13 deliberately selected theorem/prose exposition and no figures/tables. Stage 14 finds no reason to reverse that architecture. The journal Short paper limit allows up to five exhibits, but none is needed for the central result.

Therefore quantitative-figure/table regeneration, raster DPI, vector-font embedding, color accessibility, figure numbering, and separate artwork-file checks are **NOT APPLICABLE**. This is not a missing-output waiver; it follows the documented Stage-10/13 exposition choice.

## 10. References and cross-references

The bibliography includes the original Gandal–Shy article, its working-paper version, Salop, Costinot, Klimenko, Milgrom–Roberts, and Rey–Tirole. Core bibliographic metadata and available DOIs were spot-checked during the project. Stage-14 CI must again fail on undefined citations/references or overfull boxes.

No reference-style-only change is made because Elsevier initial-submission formatting is flexible where permitted and the live journal Guide must control any more specific requirement.

## 11. Fees and access

Elsevier states that economics journals levying submission fees flag them clearly in the journal's Guide and during the submission process. The current *International Economics* public journal page does not display a submission-fee flag. This is strong public evidence of a zero-fee submission route, but the project's zero-cost rule is a hard gate, so the authenticated submission must still be checked for any payment requirement.

Elsevier distinguishes subscription publication, funded by readers, from optional open access funded by APCs, and states that subscription publishing options are available. The project will use only a no-mandatory-charge standard subscription route. Any mandatory submission, publication, page or APC charge shown for the actual submission blocks submission.

**Status:** `UNVERIFIED — AUTHENTICATED PORTAL HARD GATE` until the actual record is checked.

## 12. Authenticated portal preflight

The exact unresolved operational set is recorded in `submission/PORTAL_PREFLIGHT_CHECKLIST.md` and includes:

- exact short-format article-type label;
- review/anonymity and title-page configuration;
- initial PDF/LaTeX/source item designations;
- journal-specific abstract cap if the live system enforces one;
- highlights file designation;
- ORCID/JEL/classification/editor/topic/reviewer fields;
- funding/conflict/CRediT/data/code/AI/originality attestations;
- portal-generated PDF compilation and page-by-page review;
- submission-fee hard gate;
- mandatory-publication-charge/APC hard gate.

These items genuinely require the authenticated journal workflow or the journal-specific Guide surface unavailable to the current retrieval environment.

## 13. Package inventory

Planned submission/preflight artifacts:

- identified manuscript PDF/source generated from `paper/main.tex`;
- flat LaTeX source archive `output/international-economics-submission-source.zip`;
- `submission/title_page.pdf` if required by the live item list;
- `submission/highlights.txt` content, converted only if the live item type requires another editable format;
- `submission/cover_letter.md` content for the portal/file as required;
- `output/reproducibility-supplement.zip` if accepted/required under the live supplement/code designation;
- CRediT/data/code/AI declarations synchronized with portal metadata.

Internal audit reports, workflow documents, CI logs, and other repository-internal material are not submission files.

## 14. Current blockers and planned verdict

No known scientific blocker remains after Astra-2. No new scientific issue has been introduced in Stage 14.

The current blockers are technical/procedural only:

1. fresh Stage-14 CI/build/package audit;
2. final local PDF visual QA after the Stage-14 disclosure additions;
3. authenticated portal/Guide preflight items listed above.

If (1) and (2) pass with no new issue, the canonical Stage-14 verdict will be:

`CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.

A full `SUBMISSION QA PASS` is prohibited while material portal items remain unverified.

## 15. Next-stage contract

After local Stage-14 QA passes, Stage 15 may create the immutable preflight freeze and open the actual authenticated submission record. Stage 15 must close every portal item, inspect the portal-generated PDF, confirm both zero-cost hard gates, and only then permit the final submit action.

If the portal requires a bounded file-format, anonymity, declaration-placement or metadata repair, return to Stage 14, make that compliance-only change, rerun affected checks, and create a new freeze. Any change to theorem/model/result/interpretation requires return to the earliest affected scientific stage.
