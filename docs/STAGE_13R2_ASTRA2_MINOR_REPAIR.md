# Stage 13R2 — Astra-2 Minor Repair

**Date:** 2026-09-10  
**Return source:** `docs/ASTRA_2_HOSTILE_REFEREE_GATE.md`  
**Audited baseline:** `main@ad506bec2e8c787dcb7d7ab4e08b3e120cf26bf6`  
**Repair branch:** `stage13r2/astra2-minor-repair`  
**Verified repair head:** `72ed861e3460cbcaf5eaf0a763f789c70ed07332`  
**PR:** `#14`  
**Status:** **PASS — READY FOR LIMITED ASTRA-2 RECHECK**

## 1. Repair contract

Astra-2 returned `B. MINOR EXPOSITION REPAIR` and directed the project back to Stage 13R2 only. It found no new equilibrium counterexample and did not require reopening C0–C4R, C2R-L, or Stage 12R2.

The repair was deliberately limited to the three required items. No theorem statement, title, abstract, Lean theorem, numerical verifier, or journal target was changed.

## 2. Repair 1 — cost-floor proof bridge

`paper/sections/03_corrected_equilibrium.tex` now closes the logical gap before intersecting U1/U2 with the cost-floor strategy set.

The added argument states that, at a cost-floor-feasible symmetric foreclosed candidate, candidate profits are nonnegative. Any deleted deviation has `p_i < mc_i`; because demand is nonnegative, the deleted deviation yields

`(p_i-mc_i)q_i <= 0`.

It therefore cannot strictly improve on the candidate profit. Hence a symmetric foreclosed pure-strategy equilibrium of the cost-floor game is also an equilibrium of the unrestricted game, making the subsequent intersection with U1/U2 valid.

This is an exposition/proof-completeness repair. It does not alter Proposition 1.

## 3. Repair 2 — highlight scope

The third highlight is now:

> Within symmetric foreclosed pure equilibria, a cost floor pins down member prices.

This makes the restricted equilibrium class explicit in the standalone submission artifact.

Python character-count verification of the four current highlights gives `73`, `75`, `82`, and `72` characters respectively.

## 4. Repair 3 — cover-letter welfare wording

The cover letter no longer claims to identify the `exact continuation conditions` under which the welfare comparison is preserved.

It now states the exact result actually established by the paper: a common symmetric continuation recovers the original one-half member-country welfare gap, while market-specific continuation prices leave the cross-market transfer term.

No government-stage reversal or necessary-and-sufficient ranking condition is asserted.

## 5. CI and build verification

GitHub Actions manuscript-integration run:

- run ID: `34379361638`;
- head: `72ed861e3460cbcaf5eaf0a763f789c70ed07332`;
- conclusion: **success**.

The run passed:

- Python dependency installation;
- symbolic and numerical verification;
- manuscript and submission-package build;
- clean final LaTeX-log gate;
- generated-artifact checks;
- Stage-13R2 artifact upload.

No scientific verifier or Lean source changed in this bounded repair, so a new C2R-L cycle is not required.

## 6. Exit decision

All three Astra-2 required repairs have been implemented and the integrated build is clean.

Stage-13R2 bounded-repair verdict:

`PASS — READY FOR LIMITED ASTRA-2 RECHECK`

PR #14 should remain unmerged until the limited Astra-2 recheck confirms that these three repairs are complete and have not introduced a new substantive inconsistency. Stage 14 remains blocked until that re-clearance.
