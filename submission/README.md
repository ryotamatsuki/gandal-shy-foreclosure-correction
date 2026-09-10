# International Economics submission package — Stage 14

Target: **International Economics** (Elsevier)  
Intended route: **short-format submission**. The current official journal page uses both `Short communication` and `Short paper`; the exact live Editorial Manager article-type label must therefore be selected from the authenticated portal rather than guessed.  
Cost rule: proceed only if the live submission confirms **zero submission fee and zero mandatory publication/page/APC charge on the standard subscription route**.

## Stage 14 package

- `cover_letter.md` — journal-specific cover letter aligned to equilibrium multiplicity and continuation selection.
- `highlights.txt` — four highlights. Current Elsevier general specification is 3–5 highlights, each at most 85 characters; the content passes the automated Stage-14 check. Exact portal file type/designation remains a live preflight item.
- `title_page.tex` — identified title page containing author, affiliation/location, corresponding-author designation, email, funding and competing-interest information.
- `credit_statement.md` — sole-author CRediT roles, synchronized with the manuscript.
- `build_flat_package.py` — creates a self-contained one-level LaTeX source tree and `output/international-economics-submission-source.zip`.
- `build_reproducibility_package.py` — creates `output/reproducibility-supplement.zip` containing symbolic/numerical verification and the pinned Lean formal-certification project.
- `../code/stage14_submission_audit.py` — enforces package-level Stage-14 checks for highlights, keywords, declarations, stale markers, flat archive structure and expected artifacts.

## Manuscript identity and declarations

`paper/main.tex` is currently an **identified manuscript**. Stage 14 keeps both the identified manuscript and separate identified title page ready because the exact author-identification/title-page file configuration must be confirmed from the current journal Guide/Editorial Manager record before final upload.

The manuscript now contains synchronized declarations for:

- funding;
- competing interests;
- sole-author CRediT roles;
- data/code availability;
- generative-AI use in research/verification;
- generative-AI use in manuscript preparation.

The AI disclosures distinguish verification support from manuscript-preparation assistance and state the author's independent checking and full responsibility. They do not represent AI output as proof or primary data.

## Current public-rule checks

Fresh official-source checks on 2026-09-10 establish:

- short paper maximum: 7,000 words;
- maximum five exhibits, with 200 words deducted per exhibit;
- short paper must be assessable from the main text without relying on appendices;
- general Elsevier keyword maximum: six;
- highlights: 3–5, maximum 85 characters each;
- Editorial Manager supports LaTeX ZIP/tar.gz archives and does not process LaTeX submissions containing subfolders;
- Elsevier requires disclosure of material generative-AI manuscript-preparation use and transparent description of AI use in research methods;
- CRediT roles should be supplied during submission;
- Elsevier states that journals charging submission fees flag that fact in the journal Guide and submission process; no fee flag appears on the current *International Economics* public journal page;
- Elsevier distinguishes subscription publication from optional open access funded by APCs.

The auditable source-by-source record is `docs/JOURNAL_REQUIREMENTS_LEDGER.md`.

## Authenticated portal preflight still required

The following are deliberately not inferred from old submissions or generic Elsevier behavior:

- exact article-type label (`Short paper` versus `Short communication` in the live list);
- current review/anonymity rule and resulting author-information/title-page configuration;
- exact required upload item types and whether the source ZIP/PDF are both required initially;
- exact journal-specific abstract limit if the live system enforces one;
- highlights file format/designation;
- JEL/classification fields;
- corresponding-author/ORCID fields;
- suggested/opposed reviewer requirements;
- editor/section/topic selection;
- funding/conflict/CRediT/data/code/AI/originality attestations;
- portal-generated PDF rendering;
- zero-submission-fee hard gate;
- zero-mandatory-charge subscription-route hard gate.

These are the only remaining compliance class to be closed after local Stage-14 CI/build/visual QA. The expected Stage-14 exit, if those local checks pass, is:

`CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.

Do not click final submit until the portal record, generated PDF, declarations and cost gates have been reconciled.
