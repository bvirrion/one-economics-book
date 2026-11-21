import numpy as np
from hicks import hicks_marshall, wedge_cut
import pandas as pd
from make_hours import interpolated, table as hours
from make_ushape import tables as ushape


def test_hicks_limits():
    assert np.isclose(hicks_marshall(0, 0.7, 1.5), -0.7)
    assert np.isclose(hicks_marshall(1, 0.7, 1.5), -1.5)


def test_wedge_shares_add_up():
    th, cost, hrs = wedge_cut(0.05, 0.5, 1.0)
    assert np.isclose(th + cost, 0.05) and np.isclose(hrs, 0.5 * th)


def test_hours_fell():
    t = hours().set_index("year")
    assert (t.loc[2023].drop("DEU") < t.loc[1963].drop("DEU")).all()
    assert t.loc[2023, "DEU"] < t.loc[1960, "DEU"]


def test_interpolated_runs():
    s = pd.Series([100 * 1.02 ** k for k in range(5)] + [110, 108, 112],
                  index=range(2000, 2008))
    assert interpolated(s) == [2000, 2001, 2002, 2003]
    t = pd.Series([1.0, 2.0, 2.2, 2.42, 2.662, 2.5], index=range(2000, 2006))
    assert interpolated(t) == [2002, 2003]


def test_chart_has_no_constant_growth_runs():
    t = hours().set_index("year")
    for iso in t.columns:
        assert interpolated(t[iso].dropna()) == []


def test_u_shape_convex():
    _, _, st = ushape()
    assert st.set_index("stat").value["b2"] > 0
