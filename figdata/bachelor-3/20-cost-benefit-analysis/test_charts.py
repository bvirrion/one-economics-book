import numpy as np
from bridge import irr, npv
from make_overruns import tables as over
from make_pv import table as pv


def test_npv_zero_at_irr():
    assert abs(npv(irr())) < 1e-6 and irr(0.338) < irr()


def test_npv_falls_with_rate():
    assert npv(0.02) > npv(0.035) > npv(0.07)


def test_pv_discount():
    d = pv().set_index("t")
    assert np.isclose(d.r3[0], 1) and d.r7[100] < d.r3[100] < d.r14[100]


def test_overruns_all_row():
    t = over()["all"].set_index("type")
    parts = t.drop(index="All")
    assert t.loc["All", "n"] == 258 == parts.n.sum()
    # the cited mean of all projects is the count-weighted mean of the three types
    assert np.isclose(t.loc["All", "mean"], 27.6)
    assert abs((parts.n * parts["mean"]).sum() / 258 - 27.6) < 0.05
