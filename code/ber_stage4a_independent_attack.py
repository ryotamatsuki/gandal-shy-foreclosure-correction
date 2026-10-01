#!/usr/bin/env python3
"""Independent BER Stage-4A attack from primitive delivered prices.

This file intentionally does not import or reuse code/verify_numerical.py.
Demand is reconstructed consumer-by-consumer from the Salop primitive:
posted price plus squared shortest-arc distance. Ties are split equally.

The script is falsification evidence, not a proof of equilibrium-set completeness.
"""
from __future__ import annotations
import numpy as np

L = 3.0
LOC = np.array([0.0, 1.0, 2.0])
N = 6001
TOL = 1e-12
DOM_TOL = 1e-10
SURVIVE_TOL = 2e-3
REJECT_TOL = 1e-4

def geometry(n: int = N) -> np.ndarray:
    x = (np.arange(n) + 0.5) * L / n
    d = np.abs(x[:, None] - LOC[None, :])
    return np.minimum(d, L - d) ** 2

D2 = geometry()

def quantities(prices) -> np.ndarray:
    p = np.asarray(prices, dtype=float)
    delivered = D2 + p[None, :]
    low = delivered.min(axis=1, keepdims=True)
    winners = np.isclose(delivered, low, rtol=0.0, atol=TOL)
    shares = winners / winners.sum(axis=1, keepdims=True)
    return shares.sum(axis=0) * (L / N)

def profits(prices, c: float) -> np.ndarray:
    p = np.asarray(prices, dtype=float)
    mc = np.array([0.0, 0.0, float(c)])
    return (p - mc) * quantities(p)

def outsider_profit(p1: float, p2: float, p3: float, c: float) -> float:
    return float(profits((p1, p2, p3), c)[2])

def dominance_scan():
    rival_grid = np.linspace(-1.0, 7.0, 17)
    cs = [2.55, 2.75, 3.0, 4.0, 4.9]
    gaps = [0.1, 0.5, 1.0, 2.0]
    deltas = [0.05, 0.25, 1.0]
    below_comparisons = at_comparisons = 0
    min_below_gain = min_at_gain = np.inf
    strict_below = strict_at = 0
    for c in cs:
        for gap in gaps:
            p3 = c - gap
            for p1 in rival_grid:
                for p2 in rival_grid:
                    below = outsider_profit(p1, p2, p3, c)
                    at = outsider_profit(p1, p2, c, c)
                    gain = at - below
                    if gain < -DOM_TOL:
                        raise AssertionError(("below-cost dominance failed", c, p3, p1, p2, gain))
                    min_below_gain = min(min_below_gain, gain)
                    strict_below += int(gain > DOM_TOL)
                    below_comparisons += 1
        for delta in deltas:
            for p1 in rival_grid:
                for p2 in rival_grid:
                    at = outsider_profit(p1, p2, c, c)
                    above = outsider_profit(p1, p2, c + delta, c)
                    gain = above - at
                    if gain < -DOM_TOL:
                        raise AssertionError(("at-cost diagnostic failed", c, delta, p1, p2, gain))
                    min_at_gain = min(min_at_gain, gain)
                    strict_at += int(gain > DOM_TOL)
                    at_comparisons += 1
    return below_comparisons, at_comparisons, float(min_below_gain), float(min_at_gain), strict_below, strict_at

def strict_witnesses():
    cases = [(2.75, 2.25, 0.25), (4.00, 2.50, 0.50), (4.00, 3.50, 0.25)]
    out = []
    for c, below_price, delta in cases:
        above_price = c + delta
        high = max(c, below_price, above_price) + 3.0
        below = outsider_profit(high, high, below_price, c)
        at = outsider_profit(high, high, c, c)
        above = outsider_profit(high, high, above_price, c)
        qb = float(quantities((high, high, below_price))[2])
        qa = float(quantities((high, high, above_price))[2])
        if not (below < -DOM_TOL and abs(at) <= DOM_TOL and above > DOM_TOL):
            raise AssertionError(("strict witness failed", c, below, at, above))
        if qb <= 0 or qa <= 0:
            raise AssertionError("strict witness did not generate positive demand")
        out.append((c, below_price, delta, below, at, above, qb, qa))
    return out

def one_firm_demand_grid(i: int, fixed_prices, candidates: np.ndarray) -> np.ndarray:
    """Primitive grid demand for one deviating firm; no threshold sorting."""
    fixed = np.asarray(fixed_prices, dtype=float)
    other = [j for j in range(3) if j != i]
    own = candidates[:, None] + D2[None, :, i]
    a = fixed[other[0]] + D2[:, other[0]]
    b = fixed[other[1]] + D2[:, other[1]]
    less_a = own < a[None, :] - TOL
    less_b = own < b[None, :] - TOL
    eq_a = np.isclose(own, a[None, :], rtol=0.0, atol=TOL)
    eq_b = np.isclose(own, b[None, :], rtol=0.0, atol=TOL)
    share = (
        (less_a & less_b).astype(float)
        + 0.5 * (eq_a & less_b).astype(float)
        + 0.5 * (eq_b & less_a).astype(float)
        + (1.0 / 3.0) * (eq_a & eq_b).astype(float)
    )
    return share.sum(axis=1) * (L / N)

def grid_best_response(i: int, profile, c: float, lo=-0.5, hi=6.5, step=0.005):
    candidates = np.arange(lo, hi + step / 2.0, step)
    q = one_firm_demand_grid(i, profile, candidates)
    mc = (0.0, 0.0, c)[i]
    pi = (candidates - mc) * q
    k = int(np.argmax(pi))
    return float(pi[k]), float(candidates[k]), float(q[k])

def profile_regret(profile, c: float):
    base = profits(profile, c)
    detail = []
    max_gain = -np.inf
    for i in range(3):
        best_pi, best_p, best_q = grid_best_response(i, profile, c)
        gain = best_pi - float(base[i])
        detail.append((i, gain, best_p, best_q))
        max_gain = max(max_gain, gain)
    return float(max_gain), detail

def boundary_attack():
    results = {}
    lower_cases = [
        ("c2.55", 2.55, (1.55, 1.55, 2.65)),
        ("c2.75", 2.75, (1.75, 1.75, 2.85)),
        ("c2.95", 2.95, (1.95, 1.95, 3.05)),
    ]
    for label, c, profile in lower_cases:
        gain, detail = profile_regret(profile, c)
        if gain <= REJECT_TOL:
            raise AssertionError(("strict-above-cost lower branch not rejected", label, profile, gain, detail))
        results[f"lower_{label}_gain"] = gain

    surviving_cases = [
        ("c3", 3.0, (2.0, 2.0, 3.10)),
        ("c3.5", 3.5, (2.0, 2.0, 3.60)),
        ("c4.9", 4.9, (2.0, 2.0, 5.00)),
    ]
    for label, c, profile in surviving_cases:
        gain, detail = profile_regret(profile, c)
        if gain > SURVIVE_TOL:
            raise AssertionError(("strict-above-cost U2 case rejected", label, profile, gain, detail))
        results[f"upper_{label}_gain"] = gain

    bad_gain, _ = profile_regret((1.5, 1.5, 4.0), 4.0)
    if bad_gain < 0.04:
        raise AssertionError(("published c=4 profile not rejected strongly enough", bad_gain))
    results["published_c4_gain"] = bad_gain

    astra_gain, _ = profile_regret((1.5, 1.5, 2.5), 4.0)
    if astra_gain > SURVIVE_TOL:
        raise AssertionError(("Astra c=4 unrestricted equilibrium rejected", astra_gain))
    results["astra_c4_gain"] = astra_gain

    costfloor_gain, _ = profile_regret((2.0, 2.0, 4.0), 4.0)
    if costfloor_gain > SURVIVE_TOL:
        raise AssertionError(("c=4 cost-floor profile rejected", costfloor_gain))
    results["costfloor_c4_gain"] = costfloor_gain
    return results

def main():
    below_n, at_n, min_below, min_at, strict_below, strict_at = dominance_scan()
    witnesses = strict_witnesses()
    boundary = boundary_attack()
    print(
        f"PASS primitive dominance scan: {below_n} below-cost comparisons; "
        f"min(at-cost - below-cost)={min_below:.12g}; strict cases={strict_below}"
    )
    print(
        f"PASS at-cost diagnostic scan: {at_n} comparisons; "
        f"min(above-cost - at-cost)={min_at:.12g}; strict cases={strict_at}"
    )
    for c, p, delta, below, at, above, qb, qa in witnesses:
        print(
            f"PASS strict witness: c={c:.2f}, below={p:.2f}, delta={delta:.2f}, "
            f"q=({qb:.6f},{qa:.6f}), profits=({below:.6f},{at:.6f},{above:.6f})"
        )
    print(
        "PASS lower-branch strict-above-cost rejection: "
        f"c=2.55 gain={boundary['lower_c2.55_gain']:.8g}, "
        f"c=2.75 gain={boundary['lower_c2.75_gain']:.8g}, "
        f"c=2.95 gain={boundary['lower_c2.95_gain']:.8g}"
    )
    print(
        "PASS c>=3 strict-above-cost survival: "
        f"c=3 gain={boundary['upper_c3_gain']:.8g}, "
        f"c=3.5 gain={boundary['upper_c3.5_gain']:.8g}, "
        f"c=4.9 gain={boundary['upper_c4.9_gain']:.8g}"
    )
    print(
        "PASS c=4 independent regressions: "
        f"published={boundary['published_c4_gain']:.8g}, "
        f"Astra={boundary['astra_c4_gain']:.8g}, "
        f"cost-floor={boundary['costfloor_c4_gain']:.8g}"
    )
    print("All independent BER Stage-4A primitive attacks passed.")

if __name__ == "__main__":
    main()
