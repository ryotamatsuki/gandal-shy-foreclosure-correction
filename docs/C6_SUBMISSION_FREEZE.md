# C6 Submission Freeze

## Status

C6 theory/manuscript freeze completed. Submission package remains **CONDITIONAL GO** pending live-portal confirmation only. Author-identifying metadata has been populated from the author's prior submitted manuscript supplied on 2026-08-30.

## Target

- Journal: International Economics
- Article type: Short communication / Short paper (exact portal label to confirm manually)
- Title: *Foreclosure and Limit Pricing in Standardization Unions: A Correction to Gandal and Shy (2001)*
- Author: Ryota Matsuki
- Affiliation: Independent Researcher, Matsuyama, Ehime, Japan
- Corresponding email: ryota.matsuki@gmail.com

## Frozen propositions

1. For `5/2<c<3`, `p_M=c-1`; for `3<=c<5`, `p_M=2`; after foreclosure `q_1=q_2=3/2` and `q_3=0`.
2. `TS_M^SU=3V+1/4`, `TS^MR=3V-1/4`, so the member-country welfare gap is `1/2`.

No metadata edit changes the mathematical content of either proposition.

## Final manuscript metrics

- exactly two proposition environments
- zero theorem/lemma/corollary environments
- zero exhibits
- no technical appendix
- 7 PDF pages including references and declarations
- bibliography: 5 references

## Submission architecture

- self-contained main manuscript
- author name, affiliation/location, and corresponding email populated
- secondary consistency corrections remain repository-only
- AI declaration and code-availability statement placed before references
- source package prepared as `output/international-economics-submission-source.zip`
- verification supplement prepared as `output/reproducibility-supplement.zip`

## Metadata/declarations

Populated from the author-provided prior submitted manuscript:
- author: Ryota Matsuki
- affiliation/location: Independent Researcher, Matsuyama, Ehime, Japan
- corresponding email: ryota.matsuki@gmail.com
- competing-interest content: no competing interests
- funding status: no funding; current Elsevier no-specific-grant wording used in the package

Prepared:
- generative-AI disclosure
- highlights
- cover letter
- CRediT statement
- code/data availability statement
- title page
- submission checklist

Manual confirmation still required only for items not present in the prior manuscript or visible only in the live portal:
- corresponding-author phone if required
- ORCID if desired/required
- Elsevier competing-interest declarations tool and generated file if required
- exact live portal article-type label
- suggested-reviewer field if any
- portal fee display if any
- OA/subscription choice and any current APC if OA is chosen
- confirmation at submission time that the manuscript is not under consideration elsewhere

## Reproducibility

The metadata update does not alter the C5/C6 verification scripts or mathematical source. The prior final clean C6 run passed 22 symbolic checks, the 453-point dense numerical grid, zero outsider profitable deviation, and the exact `c=4` counterexample. The metadata-filled manuscript was rebuilt locally and remained 7 pages.

## Package policy

The development repository remains private during review. Verification code is prepared as a separate reproducibility supplement; no copyrighted publisher PDFs or working-paper PDFs are included.

## PR recommendation

Keep PR #1 **OPEN / DRAFT / UNMERGED** until the remaining live-portal fields are checked. No further theoretical revision is required.
