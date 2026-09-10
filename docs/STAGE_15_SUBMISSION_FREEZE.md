# Stage 15 — Submission Freeze / Authenticated Portal Preflight

**Date:** 2026-09-10  
**Target journal:** *International Economics*  
**Live article type:** `Short Paper`  
**Title:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Stage-15 branch:** `stage15/submission-freeze`  
**Stage-14 main baseline:** `3f34a1a77a14e65a91aa2ecda7e169c40052374c`  
**Generic workflow authority:** `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`, `templates/STAGE_15_SUBMISSION_FREEZE.md`  
**Current Stage-15 state:** `SUBMITTED — AUTHENTICATED PORTAL CONFIRMATION VERIFIED; SUBMISSION ID PENDING`

## 1. Entry and scientific freeze

Stage 14 exited with `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`. Stage 15 resolved the live portal items without changing any theorem, equation, equilibrium characterization, welfare result, numerical verifier, Lean theorem, title, abstract, or substantive interpretation.

The scientific authority remains the C3R freeze plus the later C4R/Astra-2 scope controls. No scientific rollback was triggered.

## 2. Canonical submission-content baseline

The Stage-14-approved submission-content baseline was:

- `main@3f34a1a77a14e65a91aa2ecda7e169c40052374c`;
- Git tree `c723990f31d1d15bb534cdc9794a23ba709dbab1`;
- final Stage-14 technical head `9634ee92beb650db03bb9b89db6195b2ddf44278`;
- final Stage-14 technical run `34425892795` — SUCCESS;
- artifact `stage14-build`, ID `10132717858`.

The final technical head and merged Stage-14 main had the identical Git tree. The manuscript itself was not changed during the authenticated portal sequence.

Bounded compliance-only ancillary changes made during Stage 15 were limited to:

- confirming the portal's live article type as `Short Paper`;
- adding `Acknowledgements: None.` to the separate title page because the live upload instruction required an acknowledgements field;
- rendering the existing cover-letter content to PDF and changing only its article-route wording to `Short Paper`;
- rendering the frozen highlights as an editable `Highlights.docx` without changing the four highlight sentences.

The latest Stage-15 branch head after these ancillary changes passed the Stage-14 submission-QA workflow again (`run 34487836179` — SUCCESS). The title page and cover letter were also visually inspected after rendering.

## 3. Frozen-candidate artifact provenance

Original Stage-14 artifact provenance retained for the unchanged manuscript and reproducibility package:

| Artifact | SHA-256 |
|---|---|
| `output/international-economics-manuscript.pdf` | `9b20d2a661bdec42a7bb27a7054ad71ef87232079c3a287f185e1ec1cf31c935` |
| `output/international-economics-submission-source.zip` | `198fe86fbf3c099a941063d1ef489c320f960a31bef15a1c3628b72f1b56cc49` |
| `output/international-economics-flat/main.pdf` | `676a2d67a753c05d0ecf3570cbeef574c6acfa0c8caaabbb058af70569ca6d9a` |
| `output/reproducibility-supplement.zip` | `58de8276d5f6af703d3b807c1141932b3c3fe39ceb7c7ce8d9d345bda20f8718` |

The ordinary manuscript and flat-source rebuild had 9/9-page pixel parity in Stage 14. Formal state remains `FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE`.

## 4. Authenticated portal facts verified

The live Elsevier submission workflow established the following for this actual submission:

- journal: **International Economics**;
- article type: **Short Paper**;
- required upload categories were satisfied;
- LaTeX initial submission used the manuscript PDF; source files were not required at initial submission;
- separate title page with author details was required;
- no-competing-interests confirmation was accepted through the portal route;
- title, abstract, and six keywords were entered and confirmed;
- author: **Ryota Matsuki**;
- corresponding author: **Ryota Matsuki**;
- affiliation displayed on the confirmation page: **Independent Researcher**;
- no funder was added, consistent with the manuscript funding statement;
- publication route selected: **subscription**;
- five classifications were selected;
- the required final sections were accepted as complete by the portal.

The optional upload area was used for the editable highlights file and reproducibility supplement. No LaTeX source was uploaded at initial submission because the live instruction stated that source files are not needed until revision.

## 5. Portal submission confirmation

The authenticated terminal confirmation page explicitly displayed:

> `Your manuscript has now been submitted`

and recorded:

- **Submitted:** `23:54, September 10, 2026`;
- **Journal:** `International Economics`;
- **Article type:** `Short Paper`;
- **Title:** `Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)`;
- **Author:** `Ryota Matsuki`;
- **Corresponding author:** yes;
- **Affiliation:** `Independent Researcher`.

It further states that the manuscript and other files have been sent to *International Economics* and that the corresponding author will receive a confirmation email.

This is direct authenticated-portal evidence that the submission action itself completed successfully.

## 6. Cost/access gate evidence

The live review screen recorded `You have chosen to publish subscription`. No mandatory submission payment screen blocked completion, and the portal accepted the submission through to the terminal confirmation page. Therefore the actual submission had no mandatory submission fee payable at the point of submission, and no optional gold-OA APC route was selected.

The project should still monitor any later production-stage charge disclosure if the paper is accepted. No optional open-access charge is authorized under the zero-cost rule.

## 7. Submission ID / confirmation-email item

The terminal portal confirmation screenshot does **not** display a manuscript/submission ID. The portal states that a confirmation email will be sent to the corresponding author.

Accordingly:

- actual submission completion: **VERIFIED**;
- submission timestamp: **VERIFIED**;
- journal/article type/title/author: **VERIFIED**;
- submission ID: **PENDING CONFIRMATION EMAIL / TRACKING RECORD**.

Under the project's provenance rule, the paper is operationally submitted, but Stage 15 should not be marked `SUBMITTED — CLOSED` until the journal-generated manuscript/submission ID is recorded.

## 8. Current Stage-15 verdict

`SUBMITTED — AUTHENTICATED PORTAL CONFIRMATION VERIFIED; SUBMISSION ID PENDING`.

This supersedes the earlier `PREFLIGHT IN PROGRESS` state. There is no remaining upload, metadata, scientific, Lean, or submission-action blocker known from the portal sequence.

Final bookkeeping action after receipt of the Elsevier confirmation email/tracking record:

1. record the submission/manuscript ID;
2. reconcile the confirmation email title/journal/article type against this record;
3. change the terminal state to `SUBMITTED — CLOSED`;
4. merge PR #18 and preserve the resulting main SHA as the post-submission provenance state.
