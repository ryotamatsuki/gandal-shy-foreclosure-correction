# Journal Requirements Ledger — International Economics

**Stage:** 14 — Submission QA  
**Access date:** 2026-09-10  
**Target journal:** *International Economics* (Elsevier), ISSN 2110-7017  
**Stage-14 branch:** `stage14/submission-qa`  
**Scientific baseline entering Stage 14:** `main@9f1839a941470a411e6236f9d6848e352dc44490`

## Evidence hierarchy

1. direct current instruction from the journal/editorial office;
2. authenticated submission-portal instruction/required field/file designation;
3. current journal-specific official guidance;
4. current publisher-wide official guidance;
5. secondary source/internal record/inference.

Material portal-dependent items remain `UNVERIFIED` until the authenticated preflight. Public-source checks below do not override a more specific live portal instruction.

## Current official sources

- Journal page: https://shop.elsevier.com/journals/international-economics/2110-7017
- Journal Guide for Authors landing target: https://www.sciencedirect.com/journal/international-economics/publish/guide-for-authors
- Elsevier highlights support: https://www.elsevier.support/publishing/answer/how-do-i-include-highlights-with-my-manuscript
- Elsevier LaTeX / Editorial Manager support: https://www.elsevier.support/publishing/answer/how-to-submit-a-latex-file-in-editorial-manager
- Elsevier generative-AI policy: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier CRediT policy: https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement
- Elsevier submission-fee policy: https://www.elsevier.com/researcher/author/policies-and-guidelines/submission-fees
- Elsevier pricing policy: https://www.elsevier.com/about/policies-and-standards/pricing
- Elsevier general author guide / Your Paper Your Way: https://www.elsevier.com/en-in/subject/next/guide-for-authors

The ScienceDirect journal Guide itself returned HTTP 403 to the Stage-14 retrieval environment. Therefore any requirement that is only exposed there, or whose exact journal-specific wording cannot be established from another current official surface, is deliberately left for the authenticated portal/Guide preflight rather than inferred.

## Requirements ledger

| Topic | Evidence level | Operative rule / Stage-14 finding | Affected artifact or portal field | Verification | Status |
|---|---:|---|---|---|---|
| Journal identity / scope | 3 | *International Economics* publishes applied international economics, including trade and trade policy. | journal selection | Current official journal page opened 2026-09-10. | PASS |
| Short-format route | 3 + 2 pending | Official page refers to both an additional form called “Short communication” and a “Short paper” section. Exact portal article-type label must be selected from the live list, not guessed. | article type | Public page checked; portal list still required. | UNVERIFIED — PORTAL |
| Short-paper length | 3 | At most 7,000 words; each exhibit reduces limit by 200 words; at most five exhibits; main text must be self-contained. | manuscript | Current paper is a compact nine-page note with no figures/tables and no appendix; Stage-14 CI audits package structure. Exact final word diagnostic remains far below 7,000. | PASS |
| Figures/tables | 3 | Maximum five exhibits for short paper. | manuscript/artwork | Manuscript intentionally has zero figures and zero tables. | NOT APPLICABLE |
| Review/anonymity model | 3/2 pending | Exact current review-model wording was not retrievable from the journal Guide in this environment. Author-identification placement must therefore be confirmed in the live journal Guide/portal before submit. | manuscript/title page | Identified manuscript and separate identified title page are both prepared; choose the configuration required by portal. | UNVERIFIED — PORTAL/GUIDE |
| Corresponding author / affiliation / email | 2 pending | Exact portal fields and required placement are journal-specific. | title page + portal | `submission/title_page.tex` contains author, affiliation, location, email, and corresponding-author designation. | UNVERIFIED — PORTAL |
| Initial manuscript file type | 4 + 2 pending | Elsevier supports LaTeX in Editorial Manager, but exact journal item types/initial-file expectations are portal-specific. | upload items | PDF and self-contained LaTeX archive are both ready. | UNVERIFIED — PORTAL |
| LaTeX archive | 4 | EM supports ZIP/tar.gz; LaTeX submissions cannot contain subfolders; referenced source files must be present. | source ZIP | `international-economics-submission-source.zip` is generated flat; Stage-14 Python audit enforces no subdirectories and required source members. | PASS |
| Portal-generated PDF | 4 + 2 pending | Elsevier instructs authors to rebuild/view the submission PDF and inspect compiler errors/formatting. | EM generated PDF | Local package compiles; authenticated EM PDF must still be generated and inspected. | UNVERIFIED — PORTAL |
| Abstract | 3/4 + 2 pending | Exact journal-specific abstract cap could not be retrieved from the current Guide. | manuscript + portal abstract | Abstract exists and Stage-14 Python audit reports its count; exact live cap to confirm in portal/Guide. | UNVERIFIED — PORTAL/GUIDE |
| Keywords | 4 | General Elsevier guidance: maximum six keywords immediately after abstract. | manuscript + portal | Manuscript has six keywords; Stage-14 Python audit enforces `<=6`. | PASS |
| JEL codes | 2 pending | Current manuscript contains F13, L13, L15; exact portal classification fields are journal-specific. | manuscript + portal | Content prepared; portal field availability/format to confirm. | UNVERIFIED — PORTAL |
| Highlights — count/length | 4 | 3–5 highlights; each maximum 85 characters including spaces; core results only. | highlights file | Four highlights; Stage-14 Python audit enforces count and character limits. | PASS |
| Highlights — upload type/file format | 4 + 2 pending | Elsevier normally requests a separate source file and a `Highlights` upload item unless the journal Guide instructs otherwise. | upload designation | Text content is ready; exact accepted format/designation to confirm in portal. | UNVERIFIED — PORTAL |
| Graphical abstract | 2 pending | No verified evidence that one is mandatory for this journal/article type. | portal | Do not create one unless the live portal requires it. | UNVERIFIED — PORTAL |
| Funding | 4 | If no funding, Elsevier recommends the sentence already used in the manuscript. | manuscript + portal | Wording synchronized with current general Elsevier guidance. | PASS |
| Competing interests | 4 + 2 pending | Disclosure is required as applicable; exact portal attestation/file handling is live-system dependent. | manuscript + portal | Manuscript states no relevant financial or non-financial interests. Portal answer must match. | PASS — PORTAL RECONCILIATION REQUIRED |
| CRediT | 4 + 2 pending | Elsevier says CRediT roles should be provided during submission and appear above acknowledgments in publication. | manuscript + portal | Sole-author CRediT statement added to manuscript and synchronized with `submission/credit_statement.md`; portal entry remains. | PASS — PORTAL RECONCILIATION REQUIRED |
| Data/code availability | 4 + 2 pending | Actual data/code statements and repository/supplement handling must accurately describe the work. | manuscript + supplement + portal | No empirical data; symbolic/numerical/Lean materials are in reproducibility package. Portal designation/link remains to confirm. | PASS — PORTAL RECONCILIATION REQUIRED |
| Generative AI — manuscript preparation | 4 | Elsevier requires a separate AI declaration when AI materially assists manuscript preparation, naming tool, purpose and oversight. | manuscript | Dedicated declaration with OpenAI ChatGPT, purposes, human review, responsibility added at Stage 14. | PASS |
| Generative AI — research/verification use | 4 | AI use forming part of research methods should be transparently described; AI output must not substitute for human evaluation. | manuscript | Separate research/verification disclosure states use in algebraic cross-checking and code drafting, no AI output as proof/data, independent checking and responsibility. | PASS |
| Ethics/consent | 3/4 | No human participants, animals, personal data or experiments. | manuscript/portal | Not applicable to this analytical theory note unless portal asks a mandatory attestation. | NOT APPLICABLE |
| Prior publication / concurrent submission | 4 + 2 pending | Manuscript must not be concurrently under consideration elsewhere; exact attestations are portal fields. | cover letter + portal | Cover letter states not under consideration elsewhere and unpublished; portal attestation remains. | PASS — PORTAL RECONCILIATION REQUIRED |
| References / citation metadata | 4 + source checks | References must be complete/consistent; exact house style can be applied later under Elsevier flexible initial formatting where applicable. | `.bib` / PDF | Core references and DOIs were spot-checked in earlier audit; clean LaTeX build must resolve all citations. | PASS SUBJECT TO CI |
| Figure/artwork technical rules | 3/4 | No figures/tables in the chosen exposition architecture. | artwork | No artwork files required. | NOT APPLICABLE |
| Submission fee | 3 + 4 + 2 hard-gate confirmation | Elsevier states journals that levy a submission fee flag it clearly in the journal Guide and submission process. The current *International Economics* public journal page shows no submission-fee flag. Because zero fee is a hard author constraint, the live portal must still show no required payment before submission. | portal/payment step | Current public evidence supports zero submission fee; final portal check mandatory. | UNVERIFIED — PORTAL HARD GATE |
| Mandatory publication/page/APC charge | 4 + 2 hard-gate confirmation | Elsevier distinguishes subscription publication, funded by readers, from optional OA publication funded by APCs; subscription publishing is available across its journal portfolio. Confirm *International Economics* offers a no-author-charge standard route in the actual workflow and select it. | access/licensing/payment | Public publisher evidence supports subscription/no-APC route; final journal/portal choice must be checked before submit. | UNVERIFIED — PORTAL HARD GATE |
| Suggested/opposed reviewers | 2 pending | Exact number/mandatory status cannot be inferred. | portal | Inspect current required fields. | UNVERIFIED — PORTAL |
| Editor/section/topic selection | 2 pending | Exact live options are portal-specific. | portal | Inspect current required fields; choose only options actually offered. | UNVERIFIED — PORTAL |
| Originality/authorship/AI/data attestations | 2 pending | Exact required checkboxes/questions are portal-specific. | portal | Reconcile answers with manuscript and declarations. | UNVERIFIED — PORTAL |
| Source-file designations | 2 pending | Exact upload item types are journal-specific even though EM supports LaTeX archives. | portal | Map manuscript, title page, highlights, source archive and reproducibility package to the live item list. | UNVERIFIED — PORTAL |

## Public-source compliance conclusion

The manuscript satisfies the publicly verifiable short-paper structure, short-paper length/exhibit rule, keyword limit, highlights count/length rule, flat LaTeX archive rule, funding wording, CRediT content, AI disclosure policy, and the paper-specific no-figure/no-table architecture.

The remaining material unknowns are operational requirements exposed by the inaccessible journal Guide and/or the authenticated submission portal: exact article-type label, author-identification/title-page configuration, initial-upload item types, exact abstract cap if the portal enforces one, highlight file designation, portal metadata/attestations, generated-PDF behavior, and the author's zero-fee hard gates.

Accordingly, a full `SUBMISSION QA PASS` is prohibited until the authenticated preflight. If all local Stage-14 CI/build/visual checks pass, the strongest permitted Stage-14 verdict is:

`CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`.
