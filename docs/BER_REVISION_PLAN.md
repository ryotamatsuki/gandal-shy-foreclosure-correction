# BER revision plan

**Date:** 2026-10-01 JST  
**Kickoff:** COMPLETE — GO TO TARGETED STAGE 4  
**New scientific gates:** NOT YET EXECUTED  
**Baseline:** `fff18e6165e5801de2ab6770ed78d27592d9b510`  
**Workflow authority:** `research-paper-workflow@7d754032f292205264bd404116b561366836c7fd`  
**Target:** Bulletin of Economic Research; correction/note exposition profile

## 1. Research objective and constraints

国際的な標準化協定における排除後価格の訂正として、弱く支配される価格を除いた後にも残る内容と限界を示す。

- 掲載意義は、証明済みの結果と先行研究との差から評価する。
- 投稿料と必須の通常掲載料・ページ料・APCはともにゼロ。任意OAや有料オプションは選択しない。
- BERを第一目標とする。最終的な投稿適合は認証後のStage 12で判定する。
- 新たな一般理論・政策逆転・全均衡一意性は、この改稿の既定目標に含めない。
- Stage 0–3の既存研究とStage 9のリポジトリ基盤は、変化した入力がなければ再利用する。変更箇所と最新の追加義務は差分で検証する。

仮題（未採用・未凍結）:
*Post-Foreclosure Pricing in Standardization Unions: A Correction to Gandal and Shy (2001)*.

## 2. Proposed claim set

| Claim | Proposed role | Current evidence / work required |
|---|---|---|
| BER-P0: published complete profile is non-Nash for strict 5/2 < c < 5 | Main correction | Existing analytic and bounded formal evidence; manuscript/source consistency recheck |
| BER-L1: a below-cost outsider quote is weakly dominated by a cost quote | Main lemma supporting a precisely stated deletion | NEW; analytic proof, independent attack and formal applicability pending |
| BER-P1: cost-floor member price is min(c-1,2) within symmetric, foreclosed, pure-strategy equilibria | Main corrected price result | Existing restricted-game proof; dominance interpretation and mapping pending |
| BER-W1: corrected consumer surplus and worldwide firm profit; preserved common-price national welfare | Main economic consequence | Existing identities; revised comparison artifact and scope audit pending |
| Original unrestricted U1/U2 set and market-specific transfer term | Appendix / scope record | Preserve full evidence and limitations; reviewer-verifiability audit pending |

BER-P1 retains the original and restricted games as different objects. BER-L1 does not automatically certify elimination of all weakly dominated strategies or a perfect/proper equilibrium. The status of quotes exactly at marginal cost is an explicit diagnostic question.

## 3. Required route

| Stage | Work | Exit contract |
|---|---|---|
| 4 | Prove the proposed dominance statement, strategy-deletion relationship and exact scope; retain primitive/global-price logic | Claim statements, proofs and counterexample/search record |
| 4A | Reconstruct the affected logic independently; attack zero-sales/zero-profit, at-cost, boundary and finite-deviation cases | Evidence-bearing mathematical GO; formal target map |
| 6 | Re-kill actual revised novelty; separate known dominance/limit-pricing facts from the source correction; inspect potential downstream use | Bounded contribution/prior-art map |
| 7 | Recompute distribution and welfare from utility/profit accounting; choose useful exposition vehicles | Verified comparison and benchmark/scope record |
| 7.5 / 7.5A | Judge correction/note strength; certify quantifiers and MODEL-SPECIFIC boundaries; close new formal obligations and author-contribution record | Contribution Robustness Certificate and exact maximum wording |
| 8 | Freeze the actual surviving claims, assumptions, proof coverage and nonclaims | New BER theory freeze; no inherited blanket clearance |
| 9 | Update existing reproducibility links and artifact mappings where needed | Reproducibility structure matches new freeze |
| 10 | Design correction/comment exposition; construct results before finalizing Introduction | Section-role map, exposition architecture and reviewer-verifiability map |
| 11 | Attack significance, imposed conclusions, theorem absorption and manuscript reconstruction | Independent late audit; unresolved fatal objections block progress |
| 12 | Calibrate BER against certified strength and comparable papers; retain candidate/exclusion and requirements records | Evidence-bearing BER fit verdict |
| 13 | Integrate and compress; preserve source-to-defect, deletion-to-equilibrium and accounting-to-welfare bridges | Streamlining and reviewer-verifiability reports |
| 14 | Clean rebuild, formal/code checks, final PDF, current requirements and accurate AI disclosure | Actual-package QA; material unknowns remain blockers |
| 15 | Exact commit/PDF/package, live portal reconciliation and actual author sign-off | Frozen submission candidate; SUBMITTED only after receipt evidence |

The generic Stage-7.5 full-paper assessment must not be turned into an automatic GO by relabeling a weak full paper as a note. A supported narrow correction route can proceed through the inherited certification gates, with an explicit note-scope decision and a later journal-fit verdict.

Portability tests are required for broader economic claims actually made. An accurately classified model-specific correction does not need a new generalization merely to seek BER publication. Any proposed substantive expansion returns to the earliest affected research stage.

## 4. Next-stage contract: targeted Stage 4

Inputs:
- pinned baseline manuscript and source audit;
- C0–C1R global equilibrium derivation;
- C2R primitive numerical/symbolic evaluator;
- existing cost-floor deleted-deviation bridge;
- C2R-L formal coverage map;
- editorial objections E-02 through E-04.

Tasks:
1. Restate actual price strategy domains, marginal costs, demand nonnegativity and payoffs from the published model.
2. For each proposed below-cost quote, prove weak payoff dominance for every admissible rival-price profile and identify a feasible profile giving strict improvement. Zero sales at the candidate alone is insufficient.
3. Prove exactly how deleting this family relates to the existing cost-floor game, including why deleted deviations cannot create additional equilibria in the stated class.
4. Examine whether an outsider quote exactly at cost is itself weakly dominated by an above-cost quote. If it is, record the implications for the lower branch and keep the price-floor result separate from a stronger admissibility claim.
5. Keep partial deletion, simultaneous deletion of all weakly dominated strategies, iterated deletion and perfection/properness distinct. Do not infer the latter concepts from a cost floor.
6. Recheck the stated-class price characterization, the c=3 transition, relevant equality cases and finite/global deviations. Retain limiting/boundary cases separately from strict-domain propositions.
7. Preserve the c=4 unrestricted equilibrium regression (3/2,3/2,5/2), the failing published profile (3/2,3/2,4), and the cost-floor profile (2,2,4).
8. Produce the analytic claim/proof map, unresolved questions, proposed symbolic/numerical/formal targets and a GO / CONDITIONAL GO / NO-GO verdict. An unfavorable result narrows the contribution; it is not repaired silently in prose.

Expected report: `docs/BER_STAGE_04_TARGETED_THEORY_RECHECK.md` (not created as a completed audit by this kickoff).
Stage 4A must use a logically different attack path; rerunning the production verifier alone is not independence.

## 5. Planned manuscript architecture

1. Introduction: source result, defect, corrected result and substantive consequence.
2. Source calculation and non-Nash proof: retain the long-arc 1/4 coefficient and profitable-deviation bridge.
3. Corrected pricing: new bounded dominance lemma, restricted-game definition and price characterization.
4. Distribution and welfare: one verified comparison table if it improves assessment; retain worldwide-profit accounting and benchmark assumptions.
5. Short conclusion: answer and exact limitations.
6. Appendices: unrestricted U1/U2 and market-specific transfer analysis, with precise main-text cross-references.

本文5–7ページ程度は編集上の目標であり、BERの公式上限ではない。必要な証明を削って合わせない。要旨はBERの確認済み上限に合わせる。

At Stage 10/13 retain short bridge equations that connect primitives to demand, corrected demand to a deviation/equilibrium, and consumer/export-profit accounting to welfare. Routine expansions may move; these conceptual links may not become opaque code/Lean references.

## 6. Stop and return rules

- Unproved/false substantive claims: Stage 4 → 4A.
- Correct narrow theorem with excessive wording: Stage 7.5A.
- New prior-art absorption: Stage 6.
- Proof-architecture problem: Stage 10; compression-only problem: Stage 13.
- BER significance mismatch after certified scope: record NO-GO for that journal route rather than enlarging the theory to protect the target.
- Material fees/portal/disclosure unknowns: remain unresolved before submission QA closure.

The current kickoff authorizes the next research gate's preparation. It does not itself clear any of those gates.
