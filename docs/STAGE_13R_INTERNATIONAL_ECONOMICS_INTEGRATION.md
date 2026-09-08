# Stage 13R — International Economics Full-Paper Integration

Date: 2026-09-09

Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1, Stage 13 — Full-Paper Integration.

Stage-12R merge commit / Stage-13R base: `da1c1bee3d7ee20329a31d05ff22df9cb8eb0174`.

Stage-13R branch: `stage13r/international-economics-integration`.

Pre-closeout integration-content head: `a708d0511c99511c705e165c002f3c64fe20ae05`.

Primary target: **International Economics — short-format route**.

## 1. Executive integration verdict

**INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA.**

The RIO production manuscript has been integrated for *International Economics* without changing the frozen theory. The paper now leads with international product standards, recognition rules, foreign-market access, the standardization-union institution, and the original welfare comparison. The stronger RIO-era mechanism explanation is retained: a zero-sales outsider can remain a binding competitive constraint, generating a nondegenerate limit-pricing region before unconstrained duopoly begins.

No substantive scientific problem was exposed by integration. The remaining uncertainties are journal-compliance items intentionally carried to Stage 14 under workflow v2.1.

## 2. Frozen scientific content

Stage 13R changes no equation, proposition, parameter restriction, welfare definition, or verification script.

The two frozen results remain:

1. for `5/2<c<3`, `p_M=c-1`; for `3<=c<5`, `p_M=2`; after foreclosure `q_1=q_2=3/2`, `q_3=0`;
2. `TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`, so the member-country welfare gap remains `1/2`.

## 3. Section-role audit

### Abstract — PASS

The abstract now opens with cross-border market access and international product standards rather than generic IO foreclosure. It identifies the exact benchmark, the missing post-foreclosure equilibrium regimes, the limit-pricing mechanism, and welfare robustness. It does not claim a welfare reversal or general novelty for limit pricing.

Approximate abstract length: **177 words**. The current Stage-12 ledger keeps the exact journal abstract limit `UNVERIFIED`, so this count is an integration diagnostic rather than a final compliance certification.

### Introduction — PASS

The Introduction now follows a journal-appropriate sequence:

1. international product standards and recognition rules;
2. Gandal–Shy standardization union as the benchmark institution;
3. Costinot/Klimenko as the subsequent standards/compatibility genealogy;
4. exact post-foreclosure pricing defect;
5. corrected piecewise equilibrium and zero-sales competitive constraint;
6. welfare robustness;
7. deliberately narrow contribution statement.

The question appears before the geometry and algebra. No new institutional environment or policy theorem is promised.

### Post-foreclosure demand — PASS

The former generic `The foreclosure calculation` heading is replaced by `Post-foreclosure demand in a standardization union`. The mathematical content is unchanged. The section clearly separates the correct three-firm foreclosure threshold from the post-foreclosure residual-demand calculation.

### Corrected equilibrium — PASS

No substantive edit was made. The global member-deviation proof remains in the main text, preserving the paper's principal defense against a local-kink objection. The final interpretation continues to distinguish zero realized sales from disappearance of competitive pressure.

### Welfare — PASS

The section is retitled `Welfare under standardization and mutual recognition` and its opening/final interpretation are aligned with the international-policy comparison. The exact welfare derivation and Proposition 2 are unchanged.

### Conclusion — PASS

The Conclusion now answers the standards-policy question first. It states the corrected piecewise equilibrium, explains what changes in implementation of the standardization regime, and closes with the robustness of the original member-country welfare comparison. It adds no new result.

## 4. Contribution-claim audit

The title/abstract/Introduction/Conclusion consistently make only the following contribution claims:

- a published post-foreclosure Nash-equilibrium characterization is incorrect over a nondegenerate interval;
- correcting it creates a binding-exclusion limit-pricing regime for `5/2<c<3`;
- a zero-sales outsider remains strategically relevant in that interval;
- the original Proposition-3 member-country welfare ranking survives under the corrected equilibrium.

Explicitly not claimed:

- novelty of foreclosure or limit pricing as general mechanisms;
- a new theory of international standards;
- a new standardization institution;
- a reversal of the original welfare ranking;
- a general welfare-invariance theorem.

**Claim inflation audit: PASS.**

## 5. Related-literature structure audit

This short note does not create a separate literature-review section. That is appropriate at the present length. The Introduction uses two conceptual blocks:

- standards and international compatibility: Gandal–Shy, Costinot, Klimenko;
- mechanism interpretation: Milgrom–Roberts and Rey–Tirole.

The first block now has priority. The second is used only to interpret the corrected price equilibrium, not to recast the paper as a general IO contribution.

**Literature positioning: PASS.**

## 6. Results / policy interpretation separation

The manuscript preserves a clean distinction:

- Sections 2–3 establish the corrected equilibrium;
- Section 4 separately recomputes national welfare under the original recognition behavior;
- the policy implication is limited to robustness of the original standardization-union versus mutual-recognition ranking.

No empirical prediction or unmodeled policy recommendation is added.

**PASS.**

## 7. Abstract / Introduction / Conclusion alignment

All three now use the same hierarchy:

`international standards / recognition -> outsider foreclosure -> binding-exclusion price constraint -> limit pricing -> unconstrained duopoly -> welfare robustness`.

The new working title is:

> **Standardization Unions, Foreclosure, and Limit Pricing: Revisiting Gandal and Shy (2001)**

Keywords are reordered around the target audience:

`product standards; mutual recognition; standardization unions; foreclosure; limit pricing; trade policy`.

JEL ordering is now `F13; L13; L15`.

**Cross-document alignment: PASS.**

## 8. Figure / table architecture

The paper contains **zero figures and zero tables**. No visual is needed to establish either proposition, and the corrected piecewise price formula is more efficiently communicated as a proposition than as a decorative figure.

This is also advantageous under the verified short-paper rule that each exhibit reduces the permitted word ceiling.

**Decision: retain zero exhibits.**

## 9. Journal Requirements Ledger integration status

The Stage-12 requirements ledger remains authoritative:

- `docs/JOURNAL_REQUIREMENTS_LEDGER_INTERNATIONAL_ECONOMICS.md`.

Known Stage-12 facts incorporated in Stage 13R:

- short-format manuscript remains far below the verified 7,000-word ceiling;
- zero exhibits remain below the maximum five and incur no word-limit reduction;
- all proposition-critical proof material remains in the main text, satisfying the verified self-contained architecture requirement;
- the paper is prepared as editable LaTeX plus bibliography/source dependencies;
- the intended publication route remains zero-fee standard non-OA only.

Stage-13 manuscript `texcount -inc -sum` diagnostic:

- total count: **2,777**;
- text words: **2,513**;
- figures/tables: **0**.

These are production diagnostics; Stage 14 must apply the journal's operative counting rule if it differs.

## 10. Submission-package integration

Added/updated working artifacts:

- `submission/cover_letter.md`;
- `submission/highlights.txt`;
- `submission/title_page.tex`;
- `submission/credit_statement.md`;
- `submission/build_flat_package.py`;
- `submission/build_reproducibility_package.py`;
- `submission/README.md`;
- International-Economics output targets in `Makefile`.

The four provisional highlight lines contain **71, 54, 57, and 62 characters**, respectively. Their exact current requirement remains `UNVERIFIED` and is not treated as a compliance PASS.

The identified title page is a working artifact only. Stage 13R does not assume that separate-title-page or author-identification rules are final.

## 11. Reproducibility and build audit

Independent Stage-13R rerun in the available local environment:

### Mathematical verification

- symbolic verification: **PASS**;
- dense numerical falsification: **PASS** on 453 `c` values;
- maximum apparent fine-grid member gain: `5.6249531e-05 < 0.00075` fixed discretization bound;
- maximum outsider profitable gain: `0`;
- convergence artifact: `0.0002249925` at `N=20000` -> `5.6249531e-05` at `N=80000`;
- exact `c=4` published-profile deviation: `2.25 -> 2.296875`, gain `0.046875`.

### Modular manuscript build

- LaTeX/BibTeX compilation: **PASS**;
- final manuscript: **8 pages**;
- undefined citations/references after final pass: **0**;
- overfull/underfull-box warnings: **0**;
- rendered visual inspection of all 8 pages: **PASS**; no clipping, overlap, broken equations, or malformed references observed.

The local container had a broken `/usr/bin/bibtex` alternatives symlink; invoking the installed BibTeX executable directly resolved the environment issue. This is not a manuscript/source defect.

### Flat source package

The source-package builder now flattens the directory structure without inlining section bodies. It rewrites section input paths and copies all `.tex`/`.bib` dependencies into a single-level directory.

- flat source clean build: **PASS**;
- flat PDF: **8 pages**;
- modular versus flat rendered pages: **pixel-identical on 8/8 pages**;
- generated archive: `output/international-economics-submission-source.zip`;
- archive contains eight source files: `main.tex`, `preamble.tex`, five section files, and `references.bib`.

### Reproducibility package

- generated archive: `output/reproducibility-supplement.zip`;
- contents: README, symbolic verifier, numerical verifier, requirements file;
- manuscript remains self-contained and does not depend on the supplement for proposition assessment.

### Title page

- provisional identified title-page LaTeX build: **PASS**, 1 page.

## 12. `UNVERIFIED` requirements carried to Stage 14

Stage 13R intentionally does **not** convert the following into assumptions:

- exact live article-type label (`Short paper` vs `Short communication`);
- current review/anonymity model;
- author names/affiliation placement in the main manuscript;
- whether a separate title page is required;
- corresponding-author fields and any required postal details;
- initial editable-source versus PDF file requirements;
- exact LaTeX archive/folder/file-designation rules;
- current abstract/keyword/JEL/highlight requirements;
- technical artwork rules, if any become relevant;
- supplementary-material designation;
- data/code availability placement and repository requirements;
- funding, competing-interest, CRediT, and generative-AI declaration placement/wording;
- preprint/prior-submission questions;
- reviewer-suggestion/opposition fields;
- current submission portal identity and required attestations;
- current mandatory publication/page/color charges;
- portal-generated PDF behavior.

The identified manuscript, title page, highlights, declarations, flat source archive, and reproducibility package are therefore **working candidates**, not yet the certified final upload set.

## 13. Remaining blockers

No scientific blocker remains at Stage 13R.

The only blockers are Stage-14 compliance questions listed above. Under workflow v2.1, any material `UNVERIFIED` or unresolved `CONFLICT` item blocks full `SUBMISSION QA PASS`.

## 14. Final verdict

**INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA**

Theory status: **FROZEN — NO CHANGE**.

Primary target: **International Economics — short-format route**.

## 15. Stage 14 contract

Stage 14 must:

1. reopen and date all material *International Economics* submission requirements using current official sources;
2. inspect the authenticated submission portal and reconcile the exact article type and file designations;
3. determine the operative anonymity/author-information/title-page requirements;
4. determine exact editable-source/LaTeX archive rules and rebuild the package if necessary;
5. verify abstract/keywords/JEL/highlights and every declaration/metadata field;
6. verify data/code/supplement handling;
7. recheck the zero-fee hard gate in the live system and **stop if any mandatory charge appears**;
8. compile the exact upload package in a clean environment;
9. inspect the exact generated manuscript and, if supported, the portal-generated PDF page by page;
10. return `SUBMISSION QA PASS`, a fail-closed conditional result, or route back only if a substantive defect is discovered.

Stage 14 may repair formatting/package defects but may not add new theory or materially inflate the contribution.
