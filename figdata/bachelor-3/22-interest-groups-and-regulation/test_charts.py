import numpy as np
from electricians import competitive, demand, stats, supply
from make_licensing import tables
from tullock import dissipation, symmetric_bid, two_player


def test_symmetric_total():
    for n in (2, 3, 10):
        assert np.isclose(n * symmetric_bid(n), dissipation(n))


def test_two_player_best_response():
    v1, v2 = 3.0, 2.0
    b1, b2 = two_player(v1, v2)
    # first-order condition of player 1: v1 b2 / (b1 + b2)^2 = 1
    assert np.isclose(v1 * b2 / (b1 + b2) ** 2, 1)
    assert np.isclose(v2 * b1 / (b1 + b2) ** 2, 1)


def test_competitive_clears():
    q, p = competitive()
    assert np.isclose(demand(q), supply(q)) and np.isclose(p, 50)


def test_total_cost():
    s = stats()
    assert np.isclose(s["total_cost"], s["harberger"] + s["rent_seeking"])


def test_three_measures():
    assert set(tables()) == {"state", "survey", "cps"}
