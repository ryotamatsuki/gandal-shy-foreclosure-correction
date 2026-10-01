# BER revision kickoff and change control

**Date:** 2026-10-01 JST  
**Phase:** Stage 4A independent attack completed  
**Phase decision:** PASS — GO TO STAGE 6  
**Scientific certification of new claims:** Stage 4/4A mathematical GO; formal closure and downstream contribution/journal certification pending  
**Primary target:** Bulletin of Economic Research (BER), correction/note route; exact portal type unverified  
**Working branch:** `revision/ber-change-control-20261001`

## 1. Authority and baseline

- Current project baseline / submission closeout: `fff18e6165e5801de2ab6770ed78d27592d9b510`.
- Baseline tree: `3d931468fe5d7e306ea05e8eff90ddb4e9b57110`.
- Archive reference: `archive/inteco-submitted-20260910`, pointing to the same baseline commit.
- Uploaded manuscript's Stage-14 source baseline: `3f34a1a77a14e65a91aa2ecda7e169c40052374c`.
- Stage-14 source tree: `c723990f31d1d15bb534cdc9794a23ba709dbab1`.
- Comparing the Stage-14 source baseline with the closeout commit showed no changes under `paper/`. Ancillary submission files and records did change; the two complete trees are not identical.
- Generic workflow: `ryotamatsuki/research-paper-workflow@7d754032f292205264bd404116b561366836c7fd`.
- Authority order: GOVERNANCE → THEORY_PAPER_RESEARCH_PIPELINE → templates → checklists.
- Use the pinned working-main instructions, including portability, AI accountability and reviewer verifiability. Do not describe the prospective refinements as a released v2.7 tag.

The International Economics submission is closed by a desk rejection, not an R&R or an invited resubmission. BER will be a new submission after the required gates.

## 2. Submission artifact provenance

Recorded from [the historical submission freeze](STAGE_15_SUBMISSION_FREEZE.md) and [its manifest](../submission/FREEZE_MANIFEST.sha256):

| Artifact | Recorded SHA-256 |
|---|---|
| International Economics manuscript PDF | `9b20d2a661bdec42a7bb27a7054ad71ef87232079c3a287f185e1ec1cf31c935` |
| International Economics submission-source ZIP | `198fe86fbf3c099a941063d1ef489c320f960a31bef15a1c3628b72f1b56cc49` |
| Reproducibility supplement ZIP | `58de8276d5f6af703d3b807c1141932b3c3fe39ceb7c7ce8d9d345bda20f8718` |

Historical build: run `34425892795`, head `9634ee92beb650db03bb9b89db6195b2ddf44278`, artifact `10132717858`.

These artifact hashes are retained provenance, not a claim that the binary artifacts were downloaded or rehashed during this kickoff. The archive branch preserves committed source and records; it is not a new upload of the historical PDFs/ZIPs. The fixed SHA, rather than an editable branch name, identifies the baseline.

## 3. Authorized scope of this phase

User instruction: proceed with the previously agreed 改稿開始・変更管理 phase.

This phase creates:
- decision intake and editorial-objection response planning;
- BER revision scope and the next-stage contract;
- certification inheritance / reopening records;
- an initial BER requirements ledger;
- AI provenance for the kickoff;
- source-baseline and protected-file records;
- repository navigation and a reviewable pull request.

The manuscript, verification code, Lean project, dependencies and frozen submission artifacts remain the baseline inputs to the next phase. No new mathematical, novelty, significance or journal-compliance PASS is issued here.

## 4. Change register

| ID | Proposed change | Earliest gate | Current state |
|---|---|---|---|
| CC-01 | Add a below-marginal-cost weak-dominance lemma with exact strategy quantifiers | Stage 4 → 4A | STAGE-4A PASS; independently reconstructed from primitive delivered prices; formal closure pending; not added to paper |
| CC-02 | Establish the exact relation between deleting those prices and the existing cost-floor game | Stage 4 → 4A | STAGE-4A PASS; restricted NE = feasible unrestricted NE via independent best-response partition; formal closure pending |
| CC-03 | Examine the status of an outsider quote exactly at marginal cost and the limits of any admissibility/refinement interpretation | Stage 4 → 4A / 7.5A | STAGE-4A PASS: at-cost quote is weakly dominated by any fixed strictly above-cost quote; full weak-dominance/admissibility interpretation prohibited; wording/formal gate remains |
| CC-04 | Make corrected prices and distributional consequences central; downgrade unrestricted multiplicity as a headline | Stages 6, 7, 7.5A → 8 | PROPOSED; contribution not refrozen |
| CC-05 | Move unrestricted U1/U2 and market-specific transfer analysis to auditable appendices | Stage 10 → 11 → 13 | PLANNED; proof bridges must survive |
| CC-06 | Reconcile title, abstract, keywords, conclusion and cover letter with the certified scope | Stage 10 → 12 → 13 → 14 | PLANNED |
| CC-07 | Update claim/formal mapping and formalize new proof-critical objects as warranted | Stage 4A → 7.5A → 14 | FORMAL TARGET MAP ESTABLISHED in Stage 4A; implementation/closure pending Stage 7.5A |
| CC-08 | Reconcile actual AI assistance and author verification with current Wiley/BER policy | Cross-stage log; Stages 7.5A, 14, 15 | PENDING later author/policy records |

## 5. State semantics and inheritance

Historical PASS/CLEARED records remain evidence for the exact September submission. An editorial rejection does not itself invalidate their mathematics.

For the BER edition:
- unchanged proofs and artifacts are reusable inputs, subject to the inheritance map;
- new lemmas, interpretations and contribution claims have no inherited PASS;
- the old contribution freeze, novelty assessment, significance/fit decision and integrated submission clearance do not clear the proposed BER edition;
- affected downstream states are REOPENED/PENDING until the required gates close;
- unchanged formal statements retain historical bounded coverage; new dominance/refinement statements are outside that coverage until separately mapped and certified.

See [BER certification inheritance](BER_CERTIFICATION_INHERITANCE.md).

## 6. Change and rollback rules

A change to primitives, strategy sets, equilibrium concept, theorem domains, welfare assumptions or a new headline mechanism requires explicit Stage-4 change control and affected recertification. A wording-only scope defect with correct narrow mathematics returns to Stage 7.5A; architecture/compression defects return to Stage 10/13.

In particular:
- distinguish exclusion of below-cost prices from elimination of every weakly dominated strategy;
- distinguish a cost-floor game from the unrestricted original game;
- keep asymmetric/mixed equilibria and government-stage policy selection outside the current theorem claim;
- preserve candidate-deviation and equilibrium-set tests as separate obligations;
- retain the existing deleted-deviation/nonnegative-profit bridge;
- record failed significance/portability tests rather than expanding the model to force BER fit.

## 7. Kickoff completion and next contract

This phase closes when the decision summaries, source references, proposed changes, inheritance states, next-stage tasks and requirements unknowns are committed and the diff is verified to contain only planning/status documentation.

Stage 4 is recorded in [the targeted theory recheck](BER_STAGE_04_TARGETED_THEORY_RECHECK.md). Stage 4A is recorded in [the independent primitive attack](BER_STAGE_04A_INDEPENDENT_ATTACK.md) with **PASS — GO TO STAGE 6**. Next: re-kill the revised novelty/contribution. No manuscript integration, submission action, or external correspondence is authorized by the Stage-4A result.

## 8. Kickoff verification

Local documentation verification on 2026-10-01:
- 10 changed documentation/status files; no protected scientific or submission file scheduled for modification.
- 29 baseline scientific/submission blobs recorded in the manifest.
- Relative repository links resolve against the baseline plus new files.
- Historical route/certification reports differ only by the dated supersession note.
- New decision summaries contain no private mailbox locator, delivery header or authenticated email link.

Result: PASS for documentation integrity. Mathematical scripts, Lean and manuscript builds are not newly certified by this documentation-only check. GitHub publication is separately checked against the fixed baseline before closeout.
