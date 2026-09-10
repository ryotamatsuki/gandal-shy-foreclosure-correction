# Authenticated Portal Preflight — International Economics

Use this checklist in the actual Elsevier Editorial Manager submission record after Stage-14 local QA and before any final submit action.

**Controlling rule:** the live portal/direct journal instruction overrides generic publisher guidance. Record any conflict in `docs/JOURNAL_REQUIREMENTS_LEDGER.md`, repair the package if needed, and rerun affected Stage-14 checks before submission.

## 1. Article identity

- [x] Confirm journal is **International Economics**, ISSN 2110-7017.
- [x] Inspect the complete article-type drop-down.
- [x] Select the live short-format label that corresponds to the journal's 7,000-word Short paper route: **`Short Paper`**.
- [ ] Confirm title exactly: `Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)`.

**Live portal evidence, 2026-09-10:** the article-type screen offered `Short Paper`, `Data, Tools and Replication`, `Research Paper`, and VSI routes. `Short Paper` is therefore the controlling portal label for this submission.

## 2. Review/anonymity and title page

- [ ] Read the live review/anonymity instruction shown for this submission.
- [ ] Confirm whether the main manuscript must contain author name/affiliation/email.
- [x] Confirm a separate **Title page with author details** is required by the live upload screen.
- [ ] Upload/use only the manuscript/title-page configuration that the live instruction requires.
- [ ] If anonymization is required, also inspect PDF metadata and source files for identifying information before upload.

**Live upload-screen evidence, 2026-09-10:** the title page should include article title, author name(s), affiliation(s), acknowledgements, and corresponding-author email address. The current prepared title page contains title, author, affiliation, corresponding email, funding and competing-interest statements, but does not yet contain an acknowledgements field. Treat this as a bounded Stage-14 compliance item before title-page upload.

## 3. Files and designations

- [x] Inspect every required file type marked by the live upload screen.
- [x] Confirm initial LaTeX submission accepts the **manuscript PDF**; the live instruction explicitly says that if the manuscript was written using LaTeX, upload a PDF and LaTeX source files are not needed until revision.
- [x] Required upload categories shown by the live screen: **Manuscript; Cover letter; Declaration of competing interests; Title page with author details**.
- [x] Live screen permits the author to satisfy the no-competing-interests requirement by ticking the confirmation box stating that no authors have competing financial or non-financial interests; use that route unless the portal nevertheless requests a declaration file after confirmation.
- [ ] Confirm exact upload file type/designation selected for the manuscript PDF.
- [ ] Convert/upload the prepared cover-letter content in a portal-accepted file format.
- [ ] Repair the title page to include the live-required acknowledgements field, rerun affected Stage-14 title-page QA, then upload under the exact title-page designation.
- [ ] Confirm `Highlights` designation and accepted file format; convert the current content without changing wording if the portal requires Word rather than text.
- [ ] Map `reproducibility-supplement.zip` to the appropriate supplementary/code/research-data item only if the live system accepts or requires it.
- [ ] Confirm no internal audit documents, workflow records or private files are included in the submission upload.

## 4. Metadata

- [ ] Author: Ryota Matsuki.
- [ ] Affiliation: Independent Researcher; location/address fields completed consistently with the title page.
- [ ] Corresponding author: Ryota Matsuki.
- [ ] Email matches title page.
- [ ] ORCID: enter only the author's actual ORCID if requested; do not invent one.
- [ ] Abstract copied exactly from the frozen manuscript; verify any live word/character cap before continuing.
- [ ] Keywords copied exactly and accepted by the live fields.
- [ ] JEL/classification fields reconciled with F13, L13, L15 if the system exposes those fields.
- [ ] Select editor/section/topic only from live options and record the selection.

## 5. Declarations and attestations

- [ ] Funding answer matches the no-specific-grant statement.
- [ ] Competing-interest answer matches the manuscript declaration.
- [ ] CRediT roles match the manuscript and `credit_statement.md`.
- [ ] Data statement says no empirical data were used.
- [ ] Code/reproducibility response matches the accompanying symbolic/numerical/Lean materials.
- [ ] Generative-AI answers match both manuscript AI disclosures.
- [ ] Originality/concurrent-submission attestation matches the cover letter.
- [ ] Prior-publication/preprint questions answered from actual history, not by default.
- [ ] Suggested/opposed reviewer fields completed only as required by the portal.

**Live upload-screen evidence, 2026-09-10:** for manuscripts prepared using generative AI or AI-assisted technology, the portal instructs that the disclosure statement be included directly before the references. The frozen manuscript already contains a dedicated manuscript-preparation AI disclosure before the bibliography; verify rendered placement in the uploaded PDF.

## 6. Cost hard gates

- [ ] **Submission fee = 0.** If any mandatory submission payment appears, STOP; do not pay or submit.
- [ ] **Standard non-OA/subscription publication route has no mandatory author publication/page/APC charge.**
- [ ] Do not select optional gold OA if it would incur an APC under the user's zero-cost rule.
- [ ] Record any fee/access/licensing screen or explicit portal statement in the Stage-15 provenance.

## 7. Generated PDF / final technical review

- [ ] Build/generate the portal submission PDF.
- [ ] Read compiler/log pages for LaTeX errors or missing source files.
- [ ] Inspect every PDF page at readable scale.
- [ ] Check first page author identification/anonymity against the current portal rule.
- [ ] Check title, abstract, equations, propositions, citations, bibliography and declarations.
- [ ] Confirm there are no duplicated/missing/misordered files or stale versions.
- [ ] Confirm the portal PDF represents the exact Stage-15 frozen content.

## 8. Final gate

Proceed to the final submit action only when every required portal item above is closed and both cost hard gates pass.

If the portal reveals a new requirement that changes only formatting, metadata or file packaging, repair under Stage 14 and rerun the affected QA. If it would change a theorem, model assumption, quantitative result or substantive interpretation, stop and return to the earliest affected scientific stage.
