import numpy as np
from agrarian import YBAR, becker_lewis, path
from make_brenland import payg
from make_dependency import tables as dep
from make_england import stats as eng_stats
from make_england import table as eng
from make_fert_income import table as fert
from make_tfr import tables as tfr


def test_plague_premium_by_hand():
    d = path().set_index("year")
    # y = A / sqrt(L): killing 40 % raises income by 1 / sqrt(0.6) - 1
    assert np.isclose(d.y[1600] / d.y[1599], 1 / np.sqrt(0.6), rtol=1e-3)


def test_malthusian_steady_state():
    d = path(plague=False).set_index("year")
    # with A growing 0.1 % a year, L grows 0.2 %, so 0.1 ln(y / 300) = 0.002
    assert np.isclose(d.y[1700], YBAR * np.exp(0.02), rtol=1e-3)


def test_becker_lewis_by_grid_search():
    a, b, tau, p, income = 0.5, 0.2, 0.04, 0.01, 1.0
    best, arg = -np.inf, None
    for n in np.linspace(1, 10, 451):
        for q in np.linspace(0.5, 15, 291):
            c = income - n * (tau + p * q)
            if c > 0:
                u = np.log(c) + a * np.log(n) + b * np.log(q)
                if u > best:
                    best, arg = u, (n, q)
    n, q = becker_lewis(income, a, b, tau, p)
    assert abs(arg[0] - n) < 0.05 and abs(arg[1] - q) < 0.1


def test_payg_by_hand():
    s = payg()
    assert np.isclose(s["payg_rate"], 40 * 1950 / s["emp2025"])


def test_data_charts():
    t = eng()
    assert t.year.min() <= 1270 and t.year.max() == 1850
    assert eng_stats(t).set_index("stat").value["plague_rise"] > 10
    out, st = tfr()
    assert (st.y2024 < st.y_first).all()
    assert st.set_index("iso3").loc[["KOR", "IND", "NGA"], "first"].tolist() == [1901, 1880, 1925]
    assert fert().tfr.between(0.5, 8).all()
    d, s = dep()
    assert (s.set_index("iso3").loc[["JPN", "ITA"], "y2025"] > 35).all()


def test_first_estimate_drops_flat_fill():
    import pandas as pd
    from make_tfr import first_estimate
    s = pd.Series([6.0] * 12 + [5.9, 5.7], index=range(1800, 1814))
    assert first_estimate(s) == 1811
    assert first_estimate(pd.Series([4.0, 4.1, 4.2], index=[1800, 1801, 1802])) == 1800


def test_decade_mean_by_hand():
    import pandas as pd
    from make_england import decade_mean
    s = pd.Series(range(100), index=range(1600, 1700), dtype=float)
    assert decade_mean(s, 1650) == sum(range(45, 55)) / 10
