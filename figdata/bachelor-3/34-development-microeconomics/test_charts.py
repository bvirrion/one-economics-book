import numpy as np
from cashprog import THRESHOLD, experiment, line, weighted_median
from fgt import fgt
from make_aid import table as aid
from make_fgt import table as fgt_table
from make_microcredit import table as micro


def test_fgt_by_hand():
    y = [2, 4, 6, 10, 12]
    # poor: 2, 4, 6 with gaps 0.75, 0.5, 0.25 at z = 8
    assert np.isclose(fgt(y, 8, 0), 0.6)
    assert np.isclose(fgt(y, 8, 1), 1.5 / 5)
    assert np.isclose(fgt(y, 8, 2), (0.5625 + 0.25 + 0.0625) / 5)


def test_weighted_median_and_line():
    assert weighted_median([1, 2, 3], [1, 1, 5]) == 3
    assert line() > 0


def test_threshold_rule():
    e = experiment()
    t = e[e.treat]
    ratio = t.a2 / (t.a0 + t["T"])
    above = (t.a0 + t["T"]) >= THRESHOLD
    assert np.allclose(ratio[above], 1.25) and np.allclose(ratio[~above], 0.55)
    assert abs(e.treat.sum() - (~e.treat).sum()) <= 1


def test_charts():
    m = micro()
    assert (m.lo < 0).all() and len(m) == 6
    f = fgt_table()
    assert (f.p0 >= f.p1).all() and (f.p1 >= f.p2).all()
    assert len(aid()) > 100
