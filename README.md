# Gandal-Shy Foreclosure Correction

Research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

**Current workflow status:** Stage 12R journal positioning completed; **International Economics — Short paper / Short communication** selected as the primary next target under a zero-fee hard gate.  
**Previous submission:** *Review of Industrial Organization* (RIO), submitted 2026-09-04 (JST) and rejected at editorial screening on 2026-09-09 (JST) before external review.  
**RIO submission ID:** `2d499871-b72e-4168-94c9-e179a47abc8e`.  
**RIO submitted package SHA:** `57b9515e3db3419835d404d9c8ea21ff170422cf`.  
**Current primary target:** *International Economics* — short-format route.  
**Canonical manuscript title entering Stage 13R:** *Foreclosure and Limit Pricing in Standardization Unions: Revisiting Gandal and Shy (2001)*.  
**Research objective:** Re-solve the post-foreclosure price subgame in the published quadratic-transport specification and determine whether the corrected equilibrium changes the member-country welfare comparison in Proposition 3.

The manuscript contains exactly two main propositions:

1. the corrected post-foreclosure equilibrium has a limit-pricing region for `5/2 < c < 3` and the unconstrained duopoly price for `3 <= c < 5`;
2. the member-country welfare ranking in Gandal and Shy (2001), Proposition 3, survives the equilibrium correction.

The RIO editorial decision identified audience/journal fit rather than a mathematical defect. No external RIO referee reports exist. Stage 12R therefore keeps the theory frozen and retargets the completed contribution to international economics rather than adding a new model extension.

## Canonical Stage 12R route

The active post-RIO workflow follows `ryotamatsuki/research-paper-workflow` v2.1:

1. **Stage 12R — Journal Positioning:** complete. Primary target: *International Economics* short-format route.
2. **Stage 13R — Full-Paper Integration:** next. Reframe the RIO manuscript for international standards/trade policy and rebuild the Elsevier submission package without changing the theory.
3. **Stage 14 — Submission QA:** mandatory current Guide-for-Authors and authenticated-portal compliance recheck under fail-closed rules.
4. **Stage 15 — Submission Freeze / Portal Preflight:** freeze and submit only after portal metadata/file reconciliation and generated-PDF inspection.

Author-cost hard gate: **no submission fee and no mandatory publication/page/APC charge**. Paid open access will not be selected. If the live portal presents a mandatory charge, stop and move to the next zero-fee journal.

Stage-12 records:

- `docs/STAGE_12R_INTERNATIONAL_ECONOMICS_POSITIONING.md`
- `docs/JOURNAL_REQUIREMENTS_LEDGER_INTERNATIONAL_ECONOMICS.md`

## Build and verification

The mathematical and computational verification baseline remains unchanged:

```bash
python -m pip install -r requirements.txt
make verify
make pdf
# or
make all
```

At the Stage-12R branch, the production manuscript and build configuration are intentionally still the **RIO-framed** version. Stage 12 selects the journal but does not rewrite the manuscript. Stage 13R is responsible for the International Economics integration and exact Elsevier source-package rebuild.

The existing RIO build writes `output/rio-manuscript.pdf` and `output/rio-submission-source.zip`; these remain historical production artifacts until Stage 13R replaces the active submission configuration. Generated PDFs and source archives are not committed.

## Frozen mathematical results

- Foreclosure threshold: `c=5/2`.
- For `5/2<c<3`: `p_M=c-1`.
- For `3<=c<5`: `p_M=2`.
- After foreclosure: `q_1=q_2=3/2`, `q_3=0`.
- Member-country surplus under the standardization union: `TS_M^SU=3V+1/4`.
- Mutual-recognition benchmark: `TS^MR=3V-1/4`.
- Welfare gap: `1/2`.

No Stage-12R edit changes these results.

## RIO submission provenance

- Springer Nature SNAPP accepted the RIO submission on 2026-09-04 (JST).
- Submission ID: `2d499871-b72e-4168-94c9-e179a47abc8e`.
- The submitted manuscript package was independently built and visually checked before submission.
- RIO rejected the manuscript at editorial screening on 2026-09-09 (JST), before external peer review.
- The decision is retained as submission provenance; it does not reopen the verified mathematics.
- `docs/RIO_SUBMISSION_RECORD.md` retains the RIO closeout evidence where present in the repository history.

## Structure

- `docs/` — C0–C6 historical provenance, RIO records, and current Stage-12R positioning/compliance ledger
- `paper/` — modular self-contained LaTeX manuscript; RIO-framed until Stage 13R
- `code/` — symbolic and numerical equilibrium verification
- `submission/` — existing RIO and superseded historical submission materials; Stage 13R will create the active International Economics package
- `output/` — generated manuscript/package outputs, not committed
