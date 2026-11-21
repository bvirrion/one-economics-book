import numpy as np
from bakeries import COST, DELTA, outcome, stats

from make_mergers import table


def test_prices_are_best_responses():
    # independent of the markup formula: each owner's profit, computed from the
    # shares, has a zero numerical derivative in its own price
    from logit import shares
    for owner in ([0, 1, 2], [0, 0, 2]):
        p, _ = outcome(owner)
        for j in range(3):
            mine = [k for k in range(3) if owner[k] == owner[j]]

            def profit(x, j=j, p=p, mine=mine):
                q = p.copy()
                q[j] = x
                return sum((q[k] - COST[k]) * shares(q, DELTA, 0.8)[k] for k in mine)
            h = 1e-5
            assert abs(profit(p[j] + h) - profit(p[j] - h)) / (2 * h) < 1e-6


def test_merger_raises_all_prices():
    st = stats()
    assert st["rise1"] > 0 and st["rise3"] > 0 and st["cs_loss"] > 0


def test_neutral_cost_restores_price():
    st = stats()
    p, _ = outcome([0, 0, 2], np.array([st["c_neutral"]] * 2 + [2.0]))
    p0, _ = outcome([0, 1, 2])
    assert abs(p[0] - p0[0]) < 1e-6 and len(DELTA) == 3


def test_six_products():
    assert len(table()) == 6
