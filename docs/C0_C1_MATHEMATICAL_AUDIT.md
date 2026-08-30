# C0-C1 Mathematical Audit

## Status

C1 verdict: **GO TO C2**.

## Canonical findings

1. The published three-firm interior equilibrium in Gandal and Shy (2001), equations (2)-(4), is reproduced from the primitive quadratic-transport demand system.
2. In a standardization-union member market with costs `(0,0,c)`, the interior outsider share is `q_O = 1 - 2c/5`; therefore the foreclosure threshold `c = 5/2` is unchanged.
3. After foreclosure, the short-arc indifferent consumer is `x^S = 1/2 + (p_2-p_1)/2`.
4. Under quadratic transportation costs, the long-arc indifferent consumer is `x^L = 1 + (p_2-p_1)/4`.
5. Hence two-active-firm demand is `q_1 = 3/2 + (3/4)(p_2-p_1)`.
6. The published post-foreclosure price `p_1=p_2=3/2` is not a Nash equilibrium for strict `c>5/2`. At `c=4`, the deviation `p_1: 3/2 -> 7/4` raises profit from `9/4` to `147/64`.
7. The corrected symmetric member price is piecewise: `p_M=c-1` for `5/2<c<3` (binding foreclosure constraint / limit pricing) and `p_M=2` for `3<=c<5` (unconstrained duopoly).
8. The member-country welfare calculation under foreclosure simplifies to `TS_M^SU=3V+1/4`, so the Proposition 3 ranking over mutual recognition survives.
9. Secondary audit findings include a Table 2 coefficient correction (`16c^2 -> 20c^2` in the first conversion-cost row), a boundary qualification at `c=5/4` in Proposition 2, and piecewise corrections to the country-size and network-effect foreclosure calculations.

These findings are independently re-checked in `code/verify_symbolic.py` and `code/verify_numerical.py`.
