#!/usr/bin/env python3
"""Numerical falsification checks for the corrected equilibrium."""
import numpy as np

TEST_C = [2.51, 2.75, 2.99, 3.00, 3.01, 4.00, 4.90]
N = 60000
TOL = 8e-4
x = (np.arange(N) + 0.5) * 3.0 / N
loc = np.array([0.0, 1.0, 2.0])
dist = np.abs(x[:, None] - loc[None, :])
dist = np.minimum(dist, 3.0-dist)
dist2 = dist**2


def demand(prices):
    util = -np.asarray(prices)[None, :] - dist2
    choice = np.argmax(util, axis=1)
    return np.bincount(choice, minlength=3) * 3.0 / N


def candidate(c):
    if c < 3.0:
        return np.array([c-1.0, c-1.0, c])
    return np.array([2.0, 2.0, c])


def max_member_gain(c, prices):
    q0 = demand(prices)
    base = prices[0] * q0[0]
    grid = np.linspace(0.05, max(4.5, c+0.5), 1001)
    best = -1e100
    best_p = None
    for z in grid:
        pp = prices.copy(); pp[0] = z
        val = z*demand(pp)[0]
        if val > best:
            best, best_p = val, z
    local = np.linspace(max(0.001,best_p-0.015), best_p+0.015, 601)
    for z in local:
        pp = prices.copy(); pp[0] = z
        val = z*demand(pp)[0]
        if val > best:
            best, best_p = val, z
    return best-base, best_p


def max_outsider_gain(c, prices):
    q0 = demand(prices)
    base = max(0.0,(prices[2]-c)*q0[2])
    grid = np.linspace(c, c+3.0, 601)
    best = -1e100
    best_p = c
    for z in grid:
        pp = prices.copy(); pp[2] = z
        val = (z-c)*demand(pp)[2]
        if val > best:
            best, best_p = val, z
    return best-base, best_p

for c in TEST_C:
    p = candidate(c)
    q = demand(p)
    member_gain, brp = max_member_gain(c,p)
    outsider_gain, obr = max_outsider_gain(c,p)
    if abs(q[0]-1.5) > 1.5e-3 or q[2] > 1.5e-3:
        raise AssertionError(f"allocation failure at c={c}: p={p}, q={q}")
    if member_gain > TOL:
        raise AssertionError(f"member profitable deviation at c={c}: gain={member_gain}, best p={brp}, candidate={p[0]}")
    if outsider_gain > TOL:
        raise AssertionError(f"outsider profitable entry at c={c}: gain={outsider_gain}, best p={obr}")
    print(f"PASS c={c:4.2f}: pM={p[0]:.4f}, qM={q[0]:.4f}, qO={q[2]:.6f}, max member gain={member_gain:.6g}, max outsider gain={outsider_gain:.6g}")

p = np.array([1.5,1.5,4.0])
q = demand(p)
pd = np.array([1.75,1.5,4.0])
qd = demand(pd)
base = 1.5*q[0]
dev = 1.75*qd[0]
if abs(base-2.25) > 2e-4 or abs(dev-2.296875) > 3e-4 or dev <= base:
    raise AssertionError(f"counterexample failed: base={base}, dev={dev}")
print(f"PASS c=4 published-profile counterexample: {base:.6f} -> {dev:.6f}, gain={dev-base:.6f}")
print("All numerical checks passed.")
