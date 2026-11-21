import numpy as np
from make_patents import fit
from make_patents import table as patents
from make_rnd import table as rnd
from platform_model import fhk, rohlfs_equilibria, two_sided
from ride import decomposition, panel


def test_rohlfs_by_hand():
    # 10 n (1 - n) = 1.6 has roots 0.2 and 0.8
    assert np.allclose(rohlfs_equilibria(1.6, 10.0), [0.2, 0.8])


def test_two_sided_prices_are_profit_maximising():
    a, al, f = (4.0, 2.0), (1.2, 0.4), (1.0, 1.0)
    n, p, best = two_sided(a, al, f)

    def profit(p):
        A = np.array([[1.0, -al[0]], [-al[1], 1.0]])
        m = np.linalg.solve(A, np.array([a[0] - p[0], a[1] - p[1]]))
        return ((p - np.array(f)) * m).sum()
    assert np.isclose(profit(p), best)
    for dp in ([0.01, 0], [-0.01, 0], [0, 0.01], [0, -0.01]):
        assert profit(p + np.array(dp)) < best


def test_fhk_identity():
    d = fhk(*panel())
    parts = d["within"] + d["between"] + d["cross"] + d["entry"] + d["exit"]
    assert np.isclose(parts, d["P1"] - d["P0"])
    assert decomposition()["exits"] == 33


def test_fhk_small_table():
    # two continuing firms and one exit, by hand: P0 = 0.5*10 + 0.3*20 + 0.2*5 = 12
    p0, s0 = np.array([10.0, 20, 5, 0]), np.array([0.5, 0.3, 0.2, 0])
    p1, s1 = np.array([11.0, 20, 0, 30]), np.array([0.5, 0.3, 0, 0.2])
    d = fhk(p0, s0, p1, s1, ["c", "c", "x", "n"])
    assert np.isclose(d["P0"], 12) and np.isclose(d["within"], 0.5)
    assert np.isclose(d["entry"], 0.2 * 18) and np.isclose(d["exit"], 0.2 * 7)


def test_data_charts():
    assert rnd().shape[1] == 7
    d = patents()
    _, s = fit(d)
    assert len(d) > 60 and s.value[0] > 0


def test_dynamism_sorted_and_eu_inside_country_range():
    from make_dynamism import stats, table
    t = table()
    assert t.birth.is_monotonic_increasing and (t.pos == range(len(t))).all()
    s = stats().set_index("stat").value
    assert s["min_birth"] <= s["eu_birth"] <= s["max_birth"]
    assert 0 < s["eu_surv2"] < s["eu_surv1"] < 100
