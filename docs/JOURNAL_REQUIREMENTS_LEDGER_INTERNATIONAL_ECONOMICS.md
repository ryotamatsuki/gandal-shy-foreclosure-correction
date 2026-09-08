# Journal Requirements Ledger — International Economics

Stage: 12R initial baseline

Access date: 2026-09-09

Workflow authority: `research-paper-workflow` v2.1

Target journal: **International Economics** (Elsevier / CEPII)

Intended route: **Short paper / Short communication**

Author-cost rule: **zero submission fee and zero mandatory publication/page/APC charge**; use standard non-OA/subscription publication only.

## Evidence hierarchy

1. Direct current editorial-office instruction for the actual submission
2. Authenticated submission-portal instruction / required field
3. Current journal-specific Guide for Authors / journal policy page
4. Current publisher-wide official guidance
5. Prior official source, secondary source, memory, or inference

Material `UNVERIFIED` or unresolved `CONFLICT` items block Stage-14 `SUBMISSION QA PASS`.

## Current official sources

| Source | Level | Access date | Use |
|---|---:|---|---|
| https://shop.elsevier.com/journals/international-economics/2110-7017 | 3 | 2026-09-09 | current scope, short-format rules, current journal description |
| https://www.sciencedirect.com/journal/international-economics/publish/guide-for-authors | 3 | 2026-09-09 | canonical Guide URL; granular content not fully retrievable in the present research environment and therefore not silently assumed |
| https://www.elsevier.com/researcher/author/policies-and-guidelines/submission-fees | 4 | 2026-09-09 | submission-fee policy: fee-charging journals are flagged in Guide/submission process |
| `docs/C5_JOURNAL_REQUIREMENTS.md` | 5 | prior official-source audit dated 2026-08-30 | historical baseline only; cannot by itself close a v2.1 current-rule gate |

## Ledger

| Requirement / topic | Current evidence and operative rule | Affected artifact / action | Verification method | Status |
|---|---|---|---|---|
| Journal identity | `International Economics`, ISSN 2110-7017, Elsevier; current official journal page | submission metadata | compare portal journal identity with official page | **PASS** |
| Scope fit | Applied international economics; trade and trade policy explicitly in scope; empirical contributions especially welcomed but page does not state empirical-only | abstract, Introduction, cover letter | Stage-13 framing + Stage-14 current recheck | **PASS** |
| Intended short-format route exists | Current page lists additional form `Short communication`; same page calls length-limited section `Short paper` | article-type selection | reconcile exact live portal label | **PASS / PORTAL LABEL UNVERIFIED** |
| Exact live article-type label | Public page uses two labels; exact current submission dropdown not yet inspected | portal field | authenticated portal preflight | **UNVERIFIED** |
| Short-paper word limit | At most 7,000 words | manuscript | reproducible word-count check | **PASS** |
| Exhibit adjustment | Each figure/table reduces permitted word count by 200 words | manuscript | count exhibits + adjusted word ceiling | **PASS** |
| Maximum exhibits | Five exhibits | manuscript | count figures/tables | **PASS** |
| Self-contained requirement | Contribution must be assessable from main text without relying on appendices | manuscript architecture | referee-style main-text audit | **PASS** |
| Review model / anonymity | Prior 2026-08-30 official audit recorded single-anonymized review, but current granular Guide content has not been freshly retrieved | manuscript identity/title page | current Guide + authenticated portal | **UNVERIFIED** |
| Author names in main manuscript | Prior official audit indicated identified title page; current operative placement must be reverified | main `.tex`, title page | current Guide + portal file designations | **UNVERIFIED** |
| Separate title page | Prior official audit prepared one; exact current requirement not freshly closed | title-page file | current Guide + portal | **UNVERIFIED** |
| Corresponding-author details | Prior official audit required current contact details | title page / portal | current Guide + portal | **UNVERIFIED** |
| Initial editable source requirement | Prior official audit stated editable source files required and `.tex` accepted; fresh Guide content not yet closed | LaTeX package | current Guide + upload options + clean compile | **UNVERIFIED** |
| PDF-only initial submission allowed? | Historical official audit said PDF alone is not sufficient source; current rule needs refresh | uploaded files | current Guide + portal | **UNVERIFIED** |
| LaTeX archive/folder rules | Historical official audit prepared flat source because Elsevier did not process TeX subfolders; current operative rule needs refresh | source archive | current Guide + clean-extraction build + portal | **UNVERIFIED** |
| Bibliography/style/source dependencies | Must be sufficient to compile exact submitted source; exact journal restrictions to be refreshed | `.bib`, `.bst`, `.sty`, source archive | clean environment build | **UNVERIFIED** |
| Abstract limit | Historical official audit recorded 250-word maximum; current granular Guide not freshly closed | abstract | current Guide + portal validation | **UNVERIFIED** |
| Keywords | Historical official audit recorded 1–6 English keywords | manuscript + portal | current Guide + portal | **UNVERIFIED** |
| JEL codes | Historical audit found no explicit JEL requirement; absence of requirement cannot be presumed current | manuscript + portal | current Guide + portal | **UNVERIFIED** |
| Highlights | Historical audit: encouraged, 3–5 bullets, <=85 characters; current status to refresh | highlights file | current Guide + portal designation | **UNVERIFIED** |
| Graphical abstract | No current journal-specific requirement established | ancillary file | current Guide + portal | **UNVERIFIED** |
| Figures/tables/artwork | Current short-format count rules verified; technical artwork specifications not yet rechecked | artwork files if any | current Guide | **UNVERIFIED** for technical specs |
| Supplementary material | Historical official audit allowed supplement; current requirement/designation needs refresh | reproducibility supplement | current Guide + portal | **UNVERIFIED** |
| Data availability | Historical official audit recorded Elsevier research-data Option B and encouraged availability statement | manuscript statement / portal | current Guide + current data policy | **UNVERIFIED** |
| Code availability | Historical official audit treated code/models as research data; current rule needs refresh | repository/code statement | current Guide + data policy | **UNVERIFIED** |
| Funding statement | Historical official audit required funding disclosure | manuscript / portal | current Guide + portal | **UNVERIFIED** |
| Competing interests | Historical official audit required Elsevier competing-interest declaration workflow | declaration / portal | current Guide + portal | **UNVERIFIED** |
| CRediT / contribution statement | Historical official audit required corresponding-author CRediT statement | submission metadata / manuscript if required | current Guide + portal | **UNVERIFIED** |
| Generative-AI declaration | Historical official audit required disclosure for manuscript-preparation AI use; wording and placement must be refreshed | declaration section | current Elsevier/journal AI policy + portal | **UNVERIFIED** |
| Ethics/consent | No human/animal/empirical subject data in this paper; exact portal attestations not yet visible | portal | authenticated portal | **UNVERIFIED / likely N.A.** |
| Preprint / prior-publication questions | Exact current portal questions not inspected | portal | authenticated portal | **UNVERIFIED** |
| Prior journal submission disclosure | RIO desk rejection exists; whether portal asks about prior submission/transfer must be checked. No external RIO reports exist. | cover letter / portal | authenticated portal | **UNVERIFIED** |
| Informal cascading route | Current journal page requires prior referee reports and a response document for this route. RIO produced no external reports. | submission route | use ordinary direct short-paper route | **NOT APPLICABLE** |
| Reviewer suggestions/oppositions | Current requirement not established | portal | current Guide + portal | **UNVERIFIED** |
| Submission portal identity | Exact current authenticated submission endpoint not yet reconciled | portal | Stage-14 authenticated preflight | **UNVERIFIED** |
| Submission fee | Elsevier says fee-charging economics journals are clearly flagged in the journal Guide and during submission. Current official International Economics page shows no fee flag. | payment gate | recheck current Guide + authenticated portal before submit | **PASS FOR STAGE 12 BASELINE; LIVE RECHECK MANDATORY** |
| Mandatory publication/page/color fees | No current target-specific mandatory charge has been established in this Stage-12 research. Author permits only zero-cost standard route. | publication-route choice | current Guide + portal; abort if mandatory | **UNVERIFIED** |
| Optional OA/APC | Do not elect paid OA. Exact current APC is irrelevant unless OA is voluntarily selected. | license/access choice | choose standard non-OA route | **NOT APPLICABLE to intended route; live choice must be checked** |
| Portal-generated PDF | Must be generated/inspected if portal supports it | final submission PDF | page-by-page authenticated portal QA | **UNVERIFIED — Stage 15 action** |

## Stage-12 compliance interpretation

The **journal selection** is sufficiently verified to proceed to Stage 13R because the current official journal page directly establishes the target's scope and short-format rules, and the zero-fee baseline has current Elsevier policy support.

The **submission package is not yet certified**. The v2.1 workflow deliberately carries current granular submission-rule gaps as `UNVERIFIED` rather than treating the 2026-08-30 official-source audit as timeless authority.

## Stage-13 carry-forward requirements

Stage 13R may prepare the International Economics manuscript/package, but it must preserve an explicit list of all still-unverified items. It may use the prior audit as a drafting baseline, not as final compliance proof.

In particular Stage 13R must prepare for:

- exact short-paper/short-communication article type;
- editable LaTeX source and clean compile;
- title-page/author-identity arrangement;
- abstract/keywords/JEL/highlights;
- funding, competing interests, CRediT, AI-use and code/data statements;
- ordinary direct submission rather than cascading transfer;
- zero-fee standard route only.

## Stage-14 fail-closed contract

Immediately before submission, Stage 14 must re-open current official instructions and authenticated portal fields. Full `SUBMISSION QA PASS` is prohibited while any material row above remains `UNVERIFIED` or in unresolved `CONFLICT`.

If a material rule cannot be resolved from the current journal Guide, publisher guidance and authenticated portal, contact journal/publisher submission support and retain the reply as evidence.

If the live portal requests any mandatory submission or publication charge, stop and do not submit to this journal under the current author-cost rule.

## Stage-15 contract

Stage 15 may freeze the reconciled package only after Stage 14 passes. `SUBMITTED` may be declared only after authenticated portal preflight, successful generation of the journal submission PDF when available, page-by-page inspection, final metadata reconciliation, and journal submission confirmation.