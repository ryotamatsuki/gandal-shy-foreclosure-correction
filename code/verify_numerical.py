#!/usr/bin/env python3
"""C2R numerical falsification for reopened post-foreclosure equilibrium claims.

This verifier deliberately separates:
  * the unrestricted original price game; and
  * the explicit cost-floor game p_i >= marginal cost.

It does NOT prove equilibrium-set completeness. It stress-tests the analytic
C0-C1R theorems from primitives by allowing all three posted prices to vary,
computing global unilateral best responses on a dense discretization of the
Salop circle, and preserving known counterexamples as regression tests.
"""
from __future__ import annotations

import numpy as np

LOCATIONS = np.array([0.0, 1.0, 2.0])
MARKET_LENGTH = 3.0
N_FINE = 80000
N_COARSE = 20000
MAX_TEST_PRICE = 6.0
FINE_ERROR_BOUND = 4.0 * MAX_TEST_PRICE * (MARKET_LENGTH / N_FINE)


def geometry(n: int) -> np.ndarray:
    x = (np.arange(n) + 0.5) * MARKET_LENGTH / n
    dist = np.abs(x[:, None] - LOCATIONS[None, :])
    return np.minimum(dist, MARKET_LENGTH - dist) ** 2


def costs(c: float) -> np.ndarray:
    return np.array([0.0, 0.0, float(c)])


def quantities(prices: np.ndarray, dist2: np.ndarray) -> np.ndarray:
    delivered = dist2 + prices[None, :]
    winner = np.argmin(delivered, axis=1)
    return np.bincount(winner, minlength=3).astype(float) * (
        MARKET_LENGTH / len(dist2)
    )


def profits(prices: np.ndarray, c: float, dist2: np.ndarray) -> np.ndarray:
    q = quantities(prices, dist2)
    return (prices - costs(c)) * q


def admissible(prices: np.ndarray, c: float, cost_floor: bool) -> bool:
    if not cost_floor:
        return True
    return bool(np.all(prices + 1e-12 >= costs(c)))


def global_best_response(
    i: int,
    c: float,
    prices: np.ndarray,
    dist2: np.ndarray,
    *,
    cost_floor: bool,
) -> tuple[float, float, float]:
    """Global best response in the discretized covered market.

    For each consumer point, the maximum price at which firm i weakly wins is
    the lower delivered-price envelope of the other two firms minus i's
    transport cost. Sorting these thresholds evaluates every discrete demand
    plateau. Thus a maximizer occurs at one of the thresholds, subject to the
    optional cost floor. Zero demand provides profit zero.
    """
    mc = costs(c)
    others = [j for j in range(3) if j != i]
    threshold = (
        np.minimum(
            prices[others[0]] + dist2[:, others[0]],
            prices[others[1]] + dist2[:, others[1]],
        )
        - dist2[:, i]
    )
    ordered = np.sort(threshold)[::-1]
    k = np.arange(1, len(ordered) + 1, dtype=float)
    q = k * (MARKET_LENGTH / len(ordered))
    candidate_profit = (ordered - mc[i]) * q

    floor = mc[i] if cost_floor else -np.inf
    feasible = ordered >= floor - 1e-14
    if np.any(feasible):
        feasible_idx = np.flatnonzero(feasible)
        local = int(np.argmax(candidate_profit[feasible]))
        idx = int(feasible_idx[local])
        best_profit = max(0.0, float(candidate_profit[idx]))
        return best_profit, float(ordered[idx]), float(q[idx])

    return 0.0, float(mc[i] if cost_floor else ordered[0] + 1.0), 0.0


def regret(
    prices: np.ndarray,
    c: float,
    dist2: np.ndarray,
    *,
    cost_floor: bool,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not admissible(prices, c, cost_floor):
        return (
            np.array([np.inf, np.inf, np.inf]),
            profits(prices, c, dist2),
            quantities(prices, dist2),
        )
    base_profit = profits(prices, c, dist2)
    gains = np.empty(3)
    for i in range(3):
        best, _, _ = global_best_response(
            i, c, prices, dist2, cost_floor=cost_floor
        )
        gains[i] = best - base_profit[i]
    return gains, base_profit, quantities(prices, dist2)


def assert_equilibrium(
    label: str,
    prices: tuple[float, float, float],
    c: float,
    dist2: np.ndarray,
    *,
    cost_floor: bool,
    bound: float = FINE_ERROR_BOUND,
) -> float:
    p = np.array(prices, dtype=float)
    if not admissible(p, c, cost_floor):
        raise AssertionError(f"{label}: candidate violates strategy restriction: {p}")
    gains, base_profit, q = regret(p, c, dist2, cost_floor=cost_floor)
    max_gain = float(np.max(gains))
    if max_gain > bound:
        raise AssertionError(
            f"{label}: profitable deviation found; gains={gains}, "
            f"profit={base_profit}, q={q}, bound={bound}"
        )
    if q[2] > 2.0 * MARKET_LENGTH / len(dist2):
        raise AssertionError(f"{label}: outsider not foreclosed numerically; q={q}")
    return max_gain


def assert_not_equilibrium(
    label: str,
    prices: tuple[float, float, float],
    c: float,
    dist2: np.ndarray,
    *,
    cost_floor: bool,
    min_gain: float = 1e-3,
) -> float:
    p = np.array(prices, dtype=float)
    if not admissible(p, c, cost_floor):
        raise AssertionError(
            f"{label}: use an admissible profile when testing profitable deviations"
        )
    gains, _, _ = regret(p, c, dist2, cost_floor=cost_floor)
    max_gain = float(np.max(gains))
    if max_gain <= min_gain:
        raise AssertionError(
            f"{label}: verifier failed to expose expected non-equilibrium; gains={gains}"
        )
    return max_gain


def run_valid_families(dist2: np.ndarray) -> tuple[int, float]:
    tested = 0
    max_artifact = 0.0

    # U1: lower-price unrestricted family. Multiple c values are combined
    # with multiple member prices, so p3 is not fixed at c.
    for c in [2.5001, 2.60, 2.75, 2.90, 3.00, 3.50, 4.00, 4.90]:
        upper = min(2.0, c - 1.0)
        if upper < 1.5:
            continue
        s_grid = np.linspace(1.5, upper, 7)
        for s in s_grid:
            if s >= 2.0 - 1e-12:
                continue
            r = s + 1.0
            gain = assert_equilibrium(
                f"U1 c={c:.4f}, s={s:.6f}, r={r:.6f}",
                (s, s, r),
                c,
                dist2,
                cost_floor=False,
            )
            max_artifact = max(max_artifact, gain)
            tested += 1

    # U2: at s=2 the zero-sales outsider quote can vary independently of c,
    # provided r>=3 and c>=3.
    for c in [3.00, 3.10, 3.50, 4.00, 4.90]:
        for r in sorted(set([3.0, c, max(3.0, (3.0 + c) / 2.0), c + 0.5])):
            if r < 3.0:
                continue
            gain = assert_equilibrium(
                f"U2 c={c:.4f}, r={r:.6f}",
                (2.0, 2.0, r),
                c,
                dist2,
                cost_floor=False,
            )
            max_artifact = max(max_artifact, gain)
            tested += 1

    # F1/F2: explicit cost-floor game.
    for c in [2.5001, 2.55, 2.60, 2.75, 2.90, 2.99]:
        s = c - 1.0
        gain = assert_equilibrium(
            f"F1 c={c:.4f}",
            (s, s, c),
            c,
            dist2,
            cost_floor=True,
        )
        max_artifact = max(max_artifact, gain)
        tested += 1

    for c in [3.00, 3.10, 3.50, 4.00, 4.90]:
        for r in [c, c + 0.25, c + 0.75]:
            gain = assert_equilibrium(
                f"F2 c={c:.4f}, r={r:.6f}",
                (2.0, 2.0, r),
                c,
                dist2,
                cost_floor=True,
            )
            max_artifact = max(max_artifact, gain)
            tested += 1

    return tested, max_artifact


def run_regressions(dist2: np.ndarray) -> dict[str, float]:
    found: dict[str, float] = {}

    # Published Appendix-B profile: must be rejected.
    found["published_c4"] = assert_not_equilibrium(
        "published c=4 profile",
        (1.5, 1.5, 4.0),
        4.0,
        dist2,
        cost_floor=False,
        min_gain=0.04,
    )

    # Astra counterexample: must be accepted in the unrestricted game.
    found["astra_c4"] = assert_equilibrium(
        "Astra c=4 equilibrium",
        (1.5, 1.5, 2.5),
        4.0,
        dist2,
        cost_floor=False,
    )

    # Necessity diagnostics for Theorem U.
    found["r_too_high"] = assert_not_equilibrium(
        "U necessity: r>s+1 when s<2",
        (1.75, 1.75, 3.0),
        4.0,
        dist2,
        cost_floor=False,
    )
    found["s_too_low"] = assert_not_equilibrium(
        "U necessity: s<3/2",
        (1.40, 1.40, 2.40),
        4.0,
        dist2,
        cost_floor=False,
    )
    found["s_too_high"] = assert_not_equilibrium(
        "U necessity: s>2",
        (2.10, 2.10, 3.10),
        4.0,
        dist2,
        cost_floor=False,
    )
    found["outsider_can_enter"] = assert_not_equilibrium(
        "U necessity: c<s+1",
        (1.80, 1.80, 2.80),
        2.60,
        dist2,
        cost_floor=False,
    )

    # Cost-floor restriction must exclude the below-cost Astra support.
    astra = np.array([1.5, 1.5, 2.5])
    if admissible(astra, 4.0, cost_floor=True):
        raise AssertionError("cost-floor mode failed to exclude below-cost outsider quote")

    # Representative asymmetric perturbations of valid restricted equilibria.
    for label, c, p in [
        ("asym F1 down", 2.75, (1.65, 1.75, 2.75)),
        ("asym F1 up", 2.75, (1.85, 1.75, 2.75)),
        ("asym F2 down", 4.00, (1.85, 2.00, 4.00)),
        ("asym F2 up", 4.00, (2.15, 2.00, 4.00)),
    ]:
        found[label] = assert_not_equilibrium(
            label, p, c, dist2, cost_floor=True, min_gain=0.01
        )

    return found


def convergence_check() -> tuple[float, float]:
    fine = geometry(N_FINE)
    coarse = geometry(N_COARSE)
    test_cases = [
        (4.0, (1.5, 1.5, 2.5), False),
        (4.0, (2.0, 2.0, 4.0), False),
        (2.75, (1.75, 1.75, 2.75), True),
        (4.0, (2.0, 2.0, 4.0), True),
    ]
    max_fine = 0.0
    max_coarse = 0.0
    for c, p, mode in test_cases:
        fine_gain = float(np.max(regret(np.array(p), c, fine, cost_floor=mode)[0]))
        coarse_gain = float(np.max(regret(np.array(p), c, coarse, cost_floor=mode)[0]))
        max_fine = max(max_fine, fine_gain)
        max_coarse = max(max_coarse, coarse_gain)

    if max_fine >= 0.40 * max_coarse:
        raise AssertionError(
            f"grid artifact did not shrink enough: coarse={max_coarse}, fine={max_fine}"
        )
    return max_coarse, max_fine


def main() -> None:
    dist2 = geometry(N_FINE)
    tested, max_artifact = run_valid_families(dist2)
    regressions = run_regressions(dist2)
    coarse, fine = convergence_check()

    print(
        f"PASS C2R valid-family falsification: {tested} profiles; "
        f"max apparent equilibrium gain={max_artifact:.8g} "
        f"< bound={FINE_ERROR_BOUND:.8g}"
    )
    print(
        "PASS published-profile detector: "
        f"discretized max gain={regressions['published_c4']:.8g}"
    )
    print(
        "PASS Astra regression: c=4 (1.5,1.5,2.5) retained as unrestricted NE "
        f"within grid bound; apparent gain={regressions['astra_c4']:.8g}"
    )
    print(
        "PASS necessity regressions: "
        f"r-too-high={regressions['r_too_high']:.8g}, "
        f"s-too-low={regressions['s_too_low']:.8g}, "
        f"s-too-high={regressions['s_too_high']:.8g}, "
        f"outsider-entry={regressions['outsider_can_enter']:.8g}"
    )
    print(
        "PASS asymmetric perturbation diagnostics: "
        + ", ".join(
            f"{k}={v:.8g}"
            for k, v in regressions.items()
            if k.startswith("asym ")
        )
    )
    print(
        f"PASS convergence: max apparent equilibrium gain shrinks "
        f"{coarse:.8g} -> {fine:.8g} when N={N_COARSE}->{N_FINE}"
    )
    print("All C2R numerical falsification checks passed.")


if __name__ == "__main__":
    main()
