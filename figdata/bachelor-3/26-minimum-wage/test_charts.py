import numpy as np
from make_brenland import hist, stats
from make_elasticities import table
from monopsony import competitive, employment, monopsony, supply_elasticity


def test_monopsony_below_competitive():
    lm, wm = monopsony()
    lc, wc = competitive()
    # by hand: 6 + 0.2 L = 20 - 0.1 L and 6 + 0.1 L = 20 - 0.1 L
    assert np.isclose(lm, 140 / 3) and np.isclose(wm, 6 + 14 / 3)
    assert np.isclose(lc, 70) and np.isclose(wc, 13)


def test_floor_at_competitive_maximises():
    grid = np.linspace(8, 19, 221)
    best = grid[np.argmax([employment(f) for f in grid])]
    assert abs(best - competitive()[1]) < 0.06


def test_markdown_formula():
    lm, wm = monopsony()
    e = supply_elasticity(lm)
    assert np.isclose(wm / (20 - 0.1 * lm), e / (1 + e))


def test_bunching_counts():
    h = hist()
    s = stats().set_index("stat").value
    assert np.isclose(h.after.sum() - h.before.sum(), s["bunch_change"])


def test_five_estimates():
    assert len(table()) == 5
