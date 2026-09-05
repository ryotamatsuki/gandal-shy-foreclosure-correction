# C4 Build Report

Status: **DRAFT COMPLETE / GO TO C5**.

## Manuscript

- Title: *Foreclosure and Limit Pricing in Standardization Unions: A Correction to Gandal and Shy (2001)*
- Main propositions: exactly 2
- Abstract: approximately 96 words
- Main-text section words (TeXcount text words): Introduction 504; Section 2 426; Section 3 741; Section 4 597; Conclusion 169; total 2,437
- PDF: 9 pages total; main text concludes on page 7, technical appendix begins on page 8, references end on page 9

The prose count is below the initial 3,000-3,600 design target, but the mathematical manuscript occupies the full 7-page main-text envelope. C5 should decide whether further prose would improve exposition or merely weaken the short-note format.

## Verification

`make all` passes from a clean state.

Symbolic checks pass for the interior foreclosure threshold, short and long arcs, two-firm demand, unconstrained duopoly price, kink derivatives, boundaries, transportation cost, welfare levels, welfare difference, and the c=4 counterexample.

Numerical best-response / entry checks pass at `c = 2.51, 2.75, 2.99, 3.00, 3.01, 4.00, 4.90`.

Final LaTeX log contains no undefined citations, undefined references, overfull/underfull box warnings, or fatal errors.

## C5 items

1. Decide whether the current concise 7-page main text should remain below the original prose-word target.
2. Re-check current *International Economics* Short Paper formatting and submission policy.
3. Decide whether all secondary corrections belong in supplementary material.
4. Perform a fresh referee-style attack on the global equilibrium proof and contribution positioning.
