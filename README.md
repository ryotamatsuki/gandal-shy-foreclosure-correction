# Gandal-Shy Foreclosure Correction

Research repository for a short theory note revisiting the post-foreclosure equilibrium in Gandal and Shy (2001).

**Current workflow status:** Stage 13R full-paper integration completed on the active branch; ready for Stage 14 submission QA after merge.  
**Current primary target:** *International Economics* — Short paper / Short communication, exact live portal label to be verified.  
**Canonical Stage-13R title:** *Standardization Unions, Foreclosure, and Limit Pricing: Revisiting Gandal and Shy (2001)*.  
**Previous submission:** *Review of Industrial Organization* (RIO), submitted 2026-09-04 (JST) and rejected at editorial screening on 2026-09-09 (JST) before external review.  
**RIO submission ID:** `2d499871-b72e-4168-94c9-e179a47abc8e`.  
**Author-cost hard gate:** zero submission fee and zero mandatory publication/page/APC charge under the standard non-OA route.

The manuscript contains exactly two main propositions:

1. the corrected post-foreclosure equilibrium has a limit-pricing region for `5/2 < c < 3` and the unconstrained duopoly price for `3 <= c < 5`;
2. the member-country welfare ranking in Gandal and Shy (2001), Proposition 3, survives the equilibrium correction.

The RIO editorial decision identified audience/journal fit rather than a mathematical defect. No external RIO referee reports exist. The theory remains frozen.

## Canonical Stage 12R–15 route

The active workflow follows `ryotamatsuki/research-paper-workflow` v2.1:

1. **Stage 12R — Journal Positioning:** complete. Primary target: *International Economics* short-format route.
2. **Stage 13R — Full-Paper Integration:** complete on the active branch. The paper is recentered on international product standards, recognition policy, and the standardization-union welfare comparison while retaining the stronger zero-sales-rival/limit-pricing mechanism explanation developed for RIO.
3. **Stage 14 — Submission QA:** next. Refresh all material journal requirements from current official sources, reconcile the authenticated portal, build the exact required package, and fail closed on unresolved requirements.
4. **Stage 15 — Submission Freeze / Portal Preflight:** freeze and submit only after portal metadata/file reconciliation and page-by-page inspection of the portal-generated PDF.

If the live submission system presents any mandatory author charge, stop and move to the next zero-fee journal in the Stage-12R ladder.

Current workflow records:

- `docs/STAGE_12R_INTERNATIONAL_ECONOMICS_POSITIONING.md`
- `docs/JOURNAL_REQUIREMENTS_LEDGER_INTERNATIONAL_ECONOMICS.md`
- `docs/STAGE_13R_INTERNATIONAL_ECONOMICS_INTEGRATION.md`

## Stage 13R manuscript integration

The Stage-13R manuscript now:

- opens with international product standards, recognition rules, and foreign-market access;
- treats the standardization union as the institutional object and foreclosure/limit pricing as the mechanism;
- makes Costinot (2008) and Klimenko (2009) visible in the international-standards genealogy;
- retains the global deviation proof and the `5/2<c<3` binding-exclusion interpretation;
- presents the Proposition-3 welfare ranking as a separately verified robustness result;
- uses international-economics-first keywords and JEL ordering;
- adds an International Economics cover-letter draft, highlights, title-page draft, CRediT draft, reproducibility package builder, and flat LaTeX source-package builder.

No equation, proposition, parameter restriction, welfare definition, or verification script is changed by Stage 13R.

## Build and verification

```bash
python -m pip install -r requirements.txt
make verify
make pdf
make packages
make title-page
# or
make all
```

Generated outputs are not committed:

- `output/international-economics-manuscript.pdf`
- `output/international-economics-submission-source.zip`
- `output/reproducibility-supplement.zip`
- `output/international-economics-flat/`
- `submission/title_page.pdf`

The flat source package contains a single-level LaTeX source tree and is designed to preserve the modular manuscript exactly. Whether this exact archive structure is the operative journal requirement remains a Stage-14 live-compliance question.

## Frozen mathematical results

- Foreclosure threshold: `c=5/2`.
- For `5/2<c<3`: `p_M=c-1`.
- For `3<=c<5`: `p_M=2`.
- After foreclosure: `q_1=q_2=3/2`, `q_3=0`.
- Member-country surplus under the standardization union: `TS_M^SU=3V+1/4`.
- Mutual-recognition benchmark: `TS^MR=3V-1/4`.
- Welfare gap: `1/2`.

## RIO submission provenance

- Springer Nature SNAPP accepted the RIO submission on 2026-09-04 (JST).
- Submission ID: `2d499871-b72e-4168-94c9-e179a47abc8e`.
- RIO rejected the manuscript at editorial screening on 2026-09-09 (JST), before external peer review.
- The decision is retained as submission provenance and does not reopen the verified mathematics.

## Structure

- `docs/` — mathematical provenance, RIO records, Stage-12R positioning/requirements ledger, and Stage-13R integration audit
- `paper/` — modular self-contained LaTeX manuscript
- `code/` — symbolic and numerical equilibrium verification
- `submission/` — current International Economics working package and package builders
- `output/` — generated manuscript/package outputs, not committed
