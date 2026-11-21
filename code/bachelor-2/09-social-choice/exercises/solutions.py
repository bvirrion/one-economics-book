"""Worked numbers for the exercises and the problem of Book 4, chapter 9."""

from itertools import combinations

import numpy as np


def pairwise(profile):
    """profile: list of (count, ranking). Returns {(x, y): votes for x over y}."""
    cands = profile[0][1]
    out = {}
    for x in cands:
        for y in cands:
            if x != y:
                out[x, y] = sum(n for n, r in profile if r.index(x) < r.index(y))
    return out


def condorcet_winner(profile):
    cands = profile[0][1]
    total = sum(n for n, _ in profile)
    pw = pairwise(profile)
    for x in cands:
        if all(pw[x, y] > total / 2 for y in cands if y != x):
            return x
    return None


def borda(profile):
    cands = profile[0][1]
    m = len(cands)
    return {x: sum(n * (m - 1 - r.index(x)) for n, r in profile) for x in cands}


def plurality(profile):
    cands = profile[0][1]
    return {x: sum(n for n, r in profile if r[0] == x) for x in cands}


def single_peaked(ranking, order):
    """True if the ranking falls on both sides of its top along `order`."""
    pos = [order.index(x) for x in ranking]
    lo = hi = pos[0]
    for p in pos[1:]:
        if p == lo - 1:
            lo = p
        elif p == hi + 1:
            hi = p
        else:
            return False
    return True


# Exercises 1, 5 and 12
EX1 = [(2, "ABC"), (2, "BCA"), (1, "CAB")]
EX5 = [(3, "ABC"), (2, "BCA")]
EX5_BURY = [(3, "ACB"), (2, "BCA")]

# Exercise 2: utility pairs of three states
STATES = {"x": (5, 3), "y": (6, 3), "z": (8, 1)}


def pareto_better(a, b):
    return all(p >= q for p, q in zip(a, b)) and any(p > q for p, q in zip(a, b))


def kh(state, frontier):
    """Best u1 on a linear frontier a u1 + b u2 = c at the other state's u2."""
    a, b, c = frontier
    u1, u2 = state
    return (c - b * u2) / a >= u1


def ex8():
    fa, fb = (1, 3, 12), (3, 1, 12)
    a, b = (1.5, 3.5), (3.5, 1.5)
    on_a = a[0] + 3 * a[1] == 12
    on_b = 3 * b[0] + b[1] == 12
    b_from_a = (12 - 3.5) / 3  # u1 on F_B at u2 = 3.5
    a_from_b = (12 - 3.5) / 3  # u2 on F_A at u1 = 3.5
    return on_a, on_b, kh(a, fb), b_from_a, a_from_b, kh(b[::-1], fa)


def transfers(leak=0.8, rich=80, poor=20):
    """Utilitarian (log) and maximin transfers with a leaky transfer."""
    t_util = (leak * rich - poor) / (2 * leak)
    t_max = (rich - poor) / (1 + leak)
    return (
        t_util,
        rich - t_util,
        poor + leak * t_util,
        t_max,
        rich - t_max,
        poor + leak * t_max,
    )


def median_shift():
    before = [10, 20, 30, 40, 50]
    after = before + [60, 70]
    return float(np.median(before)), float(np.median(after))


# The problem: seven councillors, four budgets (thousands of dalens)
OPTIONS = [200, 400, 600, 800]
IDEALS = [250, 380, 450, 520, 640, 690, 900]


def ballots(ideals=IDEALS):
    return [(1, tuple(sorted(OPTIONS, key=lambda o: abs(o - i)))) for i in ideals]


def problem():
    prof = ballots()
    out = {
        "ballots": [r for _, r in prof],
        "plurality": plurality(prof),
        "borda": borda(prof),
        "winner": condorcet_winner(prof),
        "pairwise_600": {y: pairwise(prof)[600, y] for y in OPTIONS if y != 600},
        "single_peaked": all(single_peaked(r, OPTIONS) for _, r in prof),
        "median": float(np.median(IDEALS)),
    }
    swap = ballots([950] + IDEALS[1:])
    out["median_swap"] = float(np.median([950] + IDEALS[1:]))
    out["winner_swap"] = condorcet_winner(swap)
    bury = list(prof)
    bury[1] = (1, (400, 200, 800, 600))
    bury[2] = (1, (400, 200, 800, 600))
    out["borda_bury_one"] = borda(prof[:1] + [bury[1]] + prof[2:])
    out["borda_bury_two"] = borda(bury)
    return out


BLOCS = [(3, "XYZ"), (2, "YZX"), (2, "ZXY")]


def agenda(first, second, third, profile=BLOCS):
    """Vote first against second, then the winner against third."""
    pw = pairwise(profile)
    w = first if pw[first, second] > pw[second, first] else second
    return w if pw[w, third] > pw[third, w] else third


def part4():
    pw = pairwise(BLOCS)
    pairs = {f"{x}{y}": pw[x, y] for x, y in combinations("XYZ", 2)}
    return pairs, agenda("X", "Y", "Z"), agenda("Y", "Z", "X"), agenda("X", "Z", "Y")


if __name__ == "__main__":
    print(condorcet_winner(EX1), pairwise(EX1))
    print(condorcet_winner(EX5), borda(EX5), borda(EX5_BURY))
    print(ex8(), transfers(), median_shift())
    print([single_peaked(r, "LMR") for r in ["LMR", "MRL", "RLM"]])
    for k, v in problem().items():
        print(k, v)
    print(part4())
