import numpy as np
from auctions import optimal_reserve, revenue_reserve, simulate_revenue
from make_spectrum import table
from schools import PREFS, blocking_pairs, boston, deferred_acceptance


def test_formula_matches_simulation():
    for r, n in ((0.0, 2), (0.5, 2), (0.5, 5), (0.3, 4)):
        assert abs(revenue_reserve(r, n) - simulate_revenue(r, n)) < 0.003


def test_known_values():
    # no reserve: the expected second-highest of n uniforms, (n - 1)/(n + 1)
    assert np.isclose(revenue_reserve(0, 4), 0.6)
    assert np.isclose(revenue_reserve(0.5, 2), 5 / 12)
    grid = np.linspace(0, 1, 10_001)
    for n in (2, 5):
        assert abs(grid[np.argmax(revenue_reserve(grid, n))] - optimal_reserve()) < 1e-3


def test_schools_by_hand():
    da, rounds = deferred_acceptance()
    assert da == {"Ana": "South", "Ben": "West", "Cai": "North", "Dee": "West"}
    assert rounds == 5 and blocking_pairs(da) == []
    bo = boston()
    assert bo == {"Ana": "West", "Ben": "West", "Cai": "South", "Dee": "North"}
    assert ("Ana", "South") in blocking_pairs(bo) and len(PREFS) == 4


def test_nine_auctions():
    assert len(table()) == 9 and table().euros.max() == 650
