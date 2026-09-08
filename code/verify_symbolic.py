#!/usr/bin/env python3
"""C2R symbolic checks for the reopened Gandal-Shy equilibrium audit.

These checks certify algebraic identities and theorem-side inequalities used by
C0-C1R. They are not a substitute for the analytic equilibrium proofs or for
the later Lean certification.
"""
import sympy as sp

c, V, p1, p2, x = sp.symbols("c V p1 p2 x", real=True)
s, r, sA, sB = sp.symbols("s r sA sB", real=True)


def check(name, condition):
    if condition is not True and condition != sp.true:
        raise AssertionError(f"FAIL: {name}: {condition}")
    print(f"PASS: {name}")


# Interior SU benchmark and foreclosure threshold.
pM_int = 1 + c / 5
qO_int = 1 - 2 * c / 5
check(
    "outsider share is zero at c=5/2",
    sp.simplify(qO_int.subs(c, sp.Rational(5, 2))) == 0,
)
check(
    "interior member price reaches 3/2 at c=5/2",
    sp.simplify(pM_int.subs(c, sp.Rational(5, 2)) - sp.Rational(3, 2)) == 0,
)

# Primitive quadratic indifference equations.
short = sp.solve(sp.Eq(p1 + x**2, p2 + (1 - x) ** 2), x)[0]
long = sp.solve(sp.Eq(p1 + x**2, p2 + (2 - x) ** 2), x)[0]
check(
    "short-arc boundary",
    sp.simplify(short - (sp.Rational(1, 2) + (p2 - p1) / 2)) == 0,
)
check(
    "long-arc correction has coefficient 1/4",
    sp.simplify(long - (1 + (p2 - p1) / 4)) == 0,
)

q1 = sp.simplify(short + long)
check(
    "two-member demand on regular branch",
    sp.simplify(q1 - (sp.Rational(3, 2) + sp.Rational(3, 4) * (p2 - p1)))
    == 0,
)

profit_two = sp.expand(p1 * q1)
br_two = sp.solve(sp.Eq(sp.diff(profit_two, p1), 0), p1)[0]
check("two-member best response", sp.simplify(br_two - (1 + p2 / 2)) == 0)
p_duo = sp.solve(sp.Eq(p1, br_two.subs(p2, p1)), p1)[0]
check("symmetric unconstrained duopoly price", sp.simplify(p_duo - 2) == 0)

# Theorem U: candidate profit and branch derivatives.
candidate_profit = sp.Rational(3, 2) * s
regular_profit = sp.expand(
    p1 * (sp.Rational(3, 2) + sp.Rational(3, 4) * (s - p1))
)
regular_derivative_at_s = sp.simplify(sp.diff(regular_profit, p1).subs(p1, s))
check(
    "regular-branch derivative at symmetric price",
    sp.simplify(regular_derivative_at_s - sp.Rational(3, 4) * (2 - s)) == 0,
)

entry_profit = sp.expand(p1 * (s + sp.Rational(3, 2) - p1))
entry_derivative_at_s = sp.simplify(sp.diff(entry_profit, p1).subs(p1, s))
check(
    "outsider-relevant right derivative at symmetric price",
    sp.simplify(entry_derivative_at_s - (sp.Rational(3, 2) - s)) == 0,
)
entry_vertex = sp.solve(sp.Eq(sp.diff(entry_profit, p1), 0), p1)[0]
check(
    "entry-side vertex",
    sp.simplify(entry_vertex - (s + sp.Rational(3, 2)) / 2) == 0,
)
check(
    "entry vertex relative to candidate",
    sp.simplify(s - entry_vertex - (s - sp.Rational(3, 2)) / 2) == 0,
)

low_price_bound = 3 * (s - 1)
check(
    "large-downward-deviation bound gap",
    sp.simplify(candidate_profit - low_price_bound - (3 - sp.Rational(3, 2) * s))
    == 0,
)

# Cost-floor characterization algebra.
check("cost-floor F1 price identity", sp.simplify((c - 1) + 1 - c) == 0)
check("piecewise branches meet at c=3", sp.simplify((c - 1).subs(c, 3) - 2) == 0)
check(
    "foreclosure-threshold branch meets at c=5/2",
    sp.simplify((c - 1).subs(c, sp.Rational(5, 2)) - sp.Rational(3, 2))
    == 0,
)

# Transportation cost and welfare.
T = 2 * sp.integrate(x**2, (x, 0, sp.Rational(1, 2))) + 2 * sp.integrate(
    x**2, (x, 0, 1)
)
check("foreclosure transportation cost", sp.simplify(T - sp.Rational(3, 4)) == 0)

common_CS = 3 * V - 3 * s - sp.Rational(3, 4)
common_PI = 3 * s + 1
common_TS = sp.simplify(common_CS + common_PI)
TS_MR = 3 * V - sp.Rational(1, 4)
check(
    "common-price SU member welfare",
    sp.simplify(common_TS - (3 * V + sp.Rational(1, 4))) == 0,
)
check(
    "common-price welfare gap",
    sp.simplify(common_TS - TS_MR - sp.Rational(1, 2)) == 0,
)

# Market-specific continuation prices. Country A consumers pay sA in A;
# firm A earns 3/2*sA in A and 3/2*sB in B, plus unit third-market profit.
CS_A = 3 * V - 3 * sA - sp.Rational(3, 4)
PI_A = sp.Rational(3, 2) * (sA + sB) + 1
TS_A = sp.simplify(CS_A + PI_A)
check(
    "cross-market welfare-selection identity",
    sp.simplify(
        TS_A
        - (
            3 * V
            + sp.Rational(1, 4)
            + sp.Rational(3, 2) * (sB - sA)
        )
    )
    == 0,
)

# Exact published-profile counterexample at c=4.
base = sp.Rational(3, 2) * sp.Rational(3, 2)
dev_q = sp.Rational(3, 2) + sp.Rational(3, 4) * (
    sp.Rational(3, 2) - sp.Rational(7, 4)
)
dev = sp.Rational(7, 4) * dev_q
check("published c=4 base profit", sp.simplify(base - sp.Rational(9, 4)) == 0)
check(
    "published c=4 deviation profit",
    sp.simplify(dev - sp.Rational(147, 64)) == 0,
)
check(
    "published c=4 profitable deviation gain",
    sp.simplify(dev - base - sp.Rational(3, 64)) == 0,
)

print("All C2R symbolic checks passed.")
