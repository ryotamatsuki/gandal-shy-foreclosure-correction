# Stage 15 — Submission Freeze / Authenticated Portal Preflight

**Date:** 2026-09-10  
**Target journal:** *International Economics*  
**Article route:** short-format route; exact live portal label remains to be confirmed  
**Working title:** *Equilibrium Multiplicity and Welfare in Standardization Unions: Revisiting Gandal and Shy (2001)*  
**Stage-15 branch:** `stage15/submission-freeze`  
**Stage-14 main baseline:** `3f34a1a77a14e65a91aa2ecda7e169c40052374c`  
**Generic workflow authority:** `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`, `templates/STAGE_15_SUBMISSION_FREEZE.md`  
**Current Stage-15 state:** `PREFLIGHT IN PROGRESS — AUTHENTICATED PORTAL ITEMS OPEN`

## 1. Entry gate

Stage 14 exited with:

`CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.

This is an allowed Stage-15 entry state under the canonical workflow, but only for resolving the explicitly portal-only requirements. It does not authorize final submission while any material portal requirement remains unresolved.

No scientific, theorem, numerical, Lean, title, abstract, citation, or journal-target change is authorized in Stage 15.

## 2. Canonical submission-content candidate

The submission-content candidate is:

`main@3f34a1a77a14e65a91aa2ecda7e169c40052374c`.

Its Git tree is:

`c723990f31d1d15bb534cdc9794a23ba709dbab1`.

The final Stage-14 technical CI head was:

`9634ee92beb650db03bb9b89db6195b2ddf44278`,

and it has the same Git tree:

`c723990f31d1d15bb534cdc9794a23ba709dbab1`.

Therefore the source tree merged to `main` is exactly the source tree that passed the final Stage-14 technical QA run. The Stage-15 branch is administrative/provenance-only unless the live portal forces a bounded compliance repair.

## 3. Final Stage-14 technical evidence

Final technical run:

- GitHub Actions workflow: `Stage 14 submission QA`;
- run ID: `34425892795`;
- result: `SUCCESS`;
- final technical head: `9634ee92beb650db03bb9b89db6195b2ddf44278`;
- artifact: `stage14-build`, artifact ID `10132717858`;
- artifact ZIP SHA-256: `0de9fc0daf05bd98a1bb2394082dded547a7cc54b07d44fca4419b8e8c2f9313`.

The run passed:

- pinned Lean/mathlib rebuild;
- explicit `sorry` / `admit` rejection;
- symbolic/numerical verification;
- manuscript and flat-source builds;
- Stage-14 Python package audit;
- clean final LaTeX-log gate;
- generated-artifact checks/upload.

Stage-14 visual QA had already established 9/9-page parity between the ordinary manuscript and flat-source rebuild and separate visual PASS for the manuscript and title page.

## 4. Frozen-candidate artifact inventory and hashes

The downloaded Stage-14 artifact ZIP was independently hashed after download. Its SHA-256 matches GitHub's artifact digest exactly.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `output/international-economics-manuscript.pdf` | 317527 | `9b20d2a661bdec42a7bb27a7054ad71ef87232079c3a287f185e1ec1cf31c935` |
| `output/international-economics-submission-source.zip` | 13355 | `198fe86fbf3c099a941063d1ef489c320f960a31bef15a1c3628b72f1b56cc49` |
| `output/international-economics-flat/main.pdf` | 317527 | `676a2d67a753c05d0ecf3570cbeef574c6acfa0c8caaabbb058af70569ca6d9a` |
| `output/reproducibility-supplement.zip` | 11127 | `58de8276d5f6af703d3b807c1141932b3c3fe39ceb7c7ce8d9d345bda20f8718` |
| `submission/title_page.pdf` | 104499 | `75e9ddb37cde2009b8625957ebe102bacd1bf469d77c25514acc08cf0afcb019` |

The two manuscript PDFs are visually/pixel identical under the Stage-14 render comparison even though their binary hashes differ, consistent with differing PDF build metadata rather than content/rendering differences.

## 5. Journal-specific ancillary files

Prepared repository-side materials include:

- `submission/cover_letter.md`;
- `submission/highlights.txt`;
- `submission/credit_statement.md`;
- `submission/title_page.tex` and built `submission/title_page.pdf`;
- `submission/PORTAL_PREFLIGHT_CHECKLIST.md`;
- `docs/JOURNAL_REQUIREMENTS_LEDGER.md`;
- flat editable LaTeX source archive;
- reproducibility supplement containing symbolic/numerical and Lean materials.

No internal workflow/audit document is intended for journal upload unless explicitly requested by the journal.

## 6. Formal-verification provenance

Formal state carried into the freeze candidate:

`FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE`.

Stage 15 preserves, but does not enlarge, the certified scope. The Lean project certifies the recorded proof-critical algebraic and quantified-inequality core; it does not claim complete formal reconstruction of the Salop game, all Nash equilibria, asymmetric/mixed equilibria, or the government stage.

Any Lean theorem/hypothesis change invalidates this freeze candidate and triggers the workflow return rule.

## 7. Journal Requirements Ledger state

The public-source/local-QA items are closed to the extent documented at Stage 14. Material remaining items are all authenticated-portal/Guide dependent and therefore remain open:

- exact live short-format article-type label;
- review/anonymity model and author-identification placement;
- title-page handling;
- initial manuscript/source upload requirements and file designations;
- exact portal abstract cap if enforced;
- JEL/classification/editor/topic fields;
- highlights upload format/designation;
- declarations and attestations as exposed by the live system;
- suggested/opposed reviewer requirements;
- portal-generated PDF behavior and final approval;
- submission-fee hard gate;
- mandatory standard non-OA/subscription-route publication/page/APC hard gate.

Because these material items are still `UNVERIFIED — PORTAL`, Stage 15 must not yet be declared `SUBMISSION FROZEN`, `UPLOADED`, or `SUBMITTED`.

## 8. Zero-cost hard gates

Submission is prohibited unless both are confirmed in the actual submission workflow:

1. `submission fee = 0`;
2. `mandatory standard non-OA/subscription-route publication/page/APC charge = 0`.

Optional gold OA must not be selected if it incurs an APC under the project's zero-cost constraint.

## 9. Authenticated portal preflight — required next action

Use the actual *International Economics* submission record and close every item in `submission/PORTAL_PREFLIGHT_CHECKLIST.md`.

The live portal/direct journal instruction controls over lower-level public guidance. If the portal introduces a bounded format/file-designation requirement, return to Stage 14, make only the required compliance change, rerun affected QA, and create a new freeze candidate. If a scientific claim/theorem/model/result would change, return to the earliest affected scientific stage.

Before final submit, the live record must confirm article type, author/corresponding-author metadata, affiliation/email/ORCID fields, anonymity/title-page configuration, all upload designations, abstract/keywords/JEL/classifications, disclosures/attestations, both cost gates, and all warnings.

When supported/required, generate the portal submission PDF and inspect it page by page before final approval.

## 10. Current Stage-15 verdict

`PREFLIGHT IN PROGRESS — AUTHENTICATED PORTAL ITEMS OPEN`.

This is not yet one of the terminal Stage-15 verdicts. In particular:

- `SUBMISSION FROZEN`: **NOT YET DECLARED**;
- `UPLOADED`: **NO EVIDENCE YET**;
- `SUBMITTED`: **NO**.

The exact locally validated submission-content candidate and artifact hashes are now recorded. The only remaining Stage-15 work is authenticated portal reconciliation and, if necessary, bounded Stage-14 compliance repair followed by a replacement freeze candidate.
