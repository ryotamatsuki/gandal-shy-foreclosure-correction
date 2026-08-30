# C6 Submission Freeze

## Status

C6 theory/manuscript freeze completed. Submission package is **CONDITIONAL GO** pending author metadata and live-portal confirmation only.

## Target

- Journal: International Economics
- Article type: Short communication / Short paper (exact portal label to confirm manually)
- Title: *Foreclosure and Limit Pricing in Standardization Unions: A Correction to Gandal and Shy (2001)*
- C6 package baseline commit: `7b73192be64f6b79314403dc1e80c8b859bcc91e`

## Frozen propositions

1. For `5/2<c<3`, `p_M=c-1`; for `3<=c<5`, `p_M=2`; after foreclosure `q_1=q_2=3/2` and `q_3=0`.
2. `TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`, so the member-country welfare gap is `1/2`.

No C6 edit changes the mathematical content of either proposition.

## Final manuscript metrics

- exactly two proposition environments
- zero theorem/lemma/corollary environments
- zero exhibits
- no technical appendix
- 7 PDF pages including references and declarations
- TeXcount: 2,154 text words in the included LaTeX files after C6 declarations (2,415 summed count including headers/caption-like text)
- bibliography: 5 references

## Submission architecture

- self-contained main manuscript
- secondary consistency corrections remain repository-only
- AI declaration and code-availability statement placed before references
- source package prepared as `output/international-economics-submission-source.zip`
- verification supplement prepared as `output/reproducibility-supplement.zip`

## Metadata/declarations

Prepared:
- generative-AI disclosure
- highlights
- cover-letter draft
- CRediT draft
- code/data availability statement
- title-page template
- submission checklist

Manual confirmation still required:
- legal/academic author name as it should appear in print
- full standard institutional affiliation and postal address
- corresponding-author email and phone number
- ORCID if desired
- competing-interest status through Elsevier declarations tool
- dedicated funding status
- exact live portal article-type label
- portal fee display
- OA/subscription choice

## Reproducibility

Final clean C6 rerun preserved C5 settings and passed:

- symbolic checks: PASS (22 checks)
- dense numerical grid: PASS on 453 `c` values over `[2.5001,4.999]`
- maximum apparent member gain: `5.6249531e-05`, below fixed discretization bound `0.00075`
- maximum outsider profitable gain: `0`
- convergence: `0.0002249925` at `N=20000` to `5.6249531e-05` at `N=80000`
- exact `c=4` counterexample: `2.25 -> 2.296875`, gain `0.046875 = 3/64`
- final LaTeX log: zero undefined citations/references and zero overfull/underfull warnings
- rendered visual inspection: PASS on all 7 pages

## Package policy

The development repository remains private during review. Verification code is prepared as a separate reproducibility supplement; no copyrighted publisher PDFs or working-paper PDFs are included.

## PR recommendation

**NOT READY TO MERGE** until the author confirms the submission-only metadata and the package is rebuilt once with those fields completed. The theory itself requires no further revision.
