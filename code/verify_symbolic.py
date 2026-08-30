#!/usr/bin/env python3
"""Symbolic verification of the two frozen propositions and C5 global-proof bounds."""
import sympy as sp

c, V, p1, p2, x = sp.symbols("c V p1 p2 x", real=True)


def check(name, condition):
    if condition is not True and condition != sp.true:
        raise AssertionError(f"FAIL: {name}: {condition}")
    print(f"PASS: {name}")

# Interior SU quantities.
pM_int = 1 + c / 5
qO_int = 1 - 2 * c / 5
check("outsider share is zero at c=5/2", sp.simplify(qO_int.subs(c, sp.Rational(5, 2))) == 0)
check("member price approaches 3/2 at c=5/2", sp.simplify(pM_int.subs(c, sp.Rational(5, 2)) - sp.Rational(3, 2)) == 0)

# Short and long arcs from primitive indifference equations.
short = sp.solve(sp.Eq(p1 + x**2, p2 + (1 - x)**2), x)[0]
long = sp.solve(sp.Eq(p1 + x**2, p2 + (2 - x)**2), x)[0]
check("short arc", sp.simplify(short - (sp.Rational(1, 2) + (p2 - p1) / 2)) == 0)
check("long arc", sp.simplify(long - (1 + (p2 - p1) / 4)) == 0)

q1 = sp.simplify(short + long)
check("two-firm demand", sp.simplify(q1 - (sp.Rational(3, 2) + sp.Rational(3, 4) * (p2 - p1))) == 0)

profit = sp.expand(p1 * q1)
br = sp.solve(sp.Eq(sp.diff(profit, p1), 0), p1)[0]
check("best response", sp.simplify(br - (1 + p2 / 2)) == 0)
p_duo = sp.solve(sp.Eq(p1, br.subs(p2, p1)), p1)[0]
check("unconstrained symmetric duopoly price", sp.simplify(p_duo - 2) == 0)

# Foreclosure boundary and kink derivatives.
p_lim = c - 1
left = sp.simplify(sp.diff(profit, p1).subs({p1: p_lim, p2: p_lim}))
check("left derivative formula", sp.simplify(left - sp.Rational(3, 4) * (3 - c)) == 0)

# With p2=c-1 and p3=c, direct comparison with the two competitors gives
# q1 = c + 1/2 - p1 on the positive-demand entry side p1 >= c-1.
p3 = c
q1_entry = c + sp.Rational(1, 2) - p1
profit_entry = sp.expand(p1 * q1_entry)
right = sp.simplify(sp.diff(profit_entry, p1).subs(p1, p_lim))
check("right derivative formula", sp.simplify(right - (sp.Rational(5, 2) - c)) == 0)
entry_vertex = sp.solve(sp.Eq(sp.diff(profit_entry, p1), 0), p1)[0]
check("entry-side vertex", sp.simplify(entry_vertex - (c + sp.Rational(1, 2)) / 2) == 0)
check("limit price minus entry vertex", sp.simplify(p_lim - entry_vertex - (2 * c - 5) / 4) == 0)

# Region-II global low-price bound.  If p1 <= c-2, q1 <= 3, so profit <= 3(c-2).
# Candidate profit is (3/2)(c-1); their difference is positive for c<3.
candidate_profit_II = sp.Rational(3, 2) * (c - 1)
low_price_bound = 3 * (c - 2)
check("region-II low-price bound gap", sp.simplify(candidate_profit_II - low_price_bound - sp.Rational(3, 2) * (3 - c)) == 0)

# Region-III two-firm objective on the regular two-boundary range p1 in [1,3]
# with p2=2 is p1(3-3p1/4), uniquely maximized at p1=2 with profit 3.
profit_III_mid = sp.expand(p1 * (3 - sp.Rational(3, 4) * p1))
vertex_III = sp.solve(sp.Eq(sp.diff(profit_III_mid, p1), 0), p1)[0]
check("region-III middle-range vertex", sp.simplify(vertex_III - 2) == 0)
check("region-III candidate profit", sp.simplify(profit_III_mid.subs(p1, 2) - 3) == 0)
check("region-III demand at p1=3", sp.simplify((3 - sp.Rational(3, 4) * p1).subs(p1, 3) - sp.Rational(3, 4)) == 0)

check("continuity at c=3", sp.simplify(p_lim.subs(c, 3) - 2) == 0)
check("continuity at c=5/2", sp.simplify(p_lim.subs(c, sp.Rational(5, 2)) - sp.Rational(3, 2)) == 0)

# Two-active-firm transport cost: half-arcs 1/2,1/2,1,1.
T = 2 * sp.integrate(x**2, (x, 0, sp.Rational(1, 2))) + 2 * sp.integrate(x**2, (x, 0, 1))
check("foreclosure transportation cost", sp.simplify(T - sp.Rational(3, 4)) == 0)

pM = sp.symbols("pM", real=True)
CS = 3 * V - 3 * pM - sp.Rational(3, 4)
PI = 3 * pM + 1
TS_SU = sp.simplify(CS + PI)
TS_MR = 3 * V - sp.Rational(1, 4)
check("SU member welfare", sp.simplify(TS_SU - (3 * V + sp.Rational(1, 4))) == 0)
check("MR welfare", sp.simplify(TS_MR - (3 * V - sp.Rational(1, 4))) == 0)
check("welfare difference", sp.simplify(TS_SU - TS_MR - sp.Rational(1, 2)) == 0)

# Direct c=4 counterexample.
base = sp.Rational(3, 2) * sp.Rational(3, 2)
dev_q = sp.Rational(3, 2) + sp.Rational(3, 4) * (sp.Rational(3, 2) - sp.Rational(7, 4))
dev = sp.Rational(7, 4) * dev_q
check("c=4 counterexample gain", sp.simplify(dev - base - sp.Rational(3, 64)) == 0)

print("All symbolic checks passed.")
