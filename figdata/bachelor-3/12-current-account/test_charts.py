import numpy as np
from make_borrow import stats, table
from make_ca_world import tables as ca_world
from make_fh import tables as fh
from make_lucas import tables as lucas
from make_sudden import table as sudden


def test_world_sum_is_not_zero_but_small():
    t, _ = ca_world()
    assert (t["sum"].abs() < 1.5).all() and (t["sum"].abs() > 0).any()
    # the U.S. current account was in deficit every year except 1991
    assert (t.USA[t.year != 1991] < 0).all() and t.USA[t.year == 1991].item() > 0


def test_fh_slope_positive_below_one():
    _, _, s = fh()
    slope = s.set_index("stat").value["slope"]
    assert 0 < slope < 1


def test_lucas_ratio():
    _, _, s = lucas()
    v = s.set_index("stat").value
    assert np.isclose(v["mpk_ratio"], v["ypw_ratio_us_india"] ** 1.5)


def test_reversals():
    d = sudden().set_index("k")
    assert d.THA[1] - d.THA[-1] > 10 and d.MEX[1] - d.MEX[0] > 4


def test_borrow_accounting():
    t = table()
    assert np.allclose(t.debt.diff().iloc[1:], -t.ca.iloc[1:])
    s = stats(t).set_index("stat").value
    assert 0 < s["nx_star_pct"] < s["nx_stop_pct"]


def test_balanced_panel_is_balanced():
    from make_ca_world import balanced, tables
    b = balanced()
    t = tables()[0].set_index("year")
    assert b.countries.nunique() == 1 and b.countries.iloc[0] <= t.countries.loc[2000:].min()
    assert b["sum"].iloc[0] < 0 < b.set_index("year")["sum"].loc[2021]
