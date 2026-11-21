import numpy as np
from brenmoor import ideal, mr_rate, setter, utility
from make_spending import table as sp
from make_wagner import tables as wag


def test_ideal_maximises():
    q = ideal(2)
    assert utility(q, 2) > utility(q - 0.1, 2) and utility(q, 2) > utility(q + 0.1, 2)


def test_setter_indifferent():
    q = setter(2)
    assert q > ideal(2) and np.isclose(utility(q, 2), utility(2.0, 2))


def test_mr_rises_with_inequality():
    assert mr_rate(0.7, 1) > mr_rate(0.9, 1) > mr_rate(1.0, 1) == 0


def test_spending_quartiles():
    t = sp()
    assert (t.q25 <= t["median"]).all() and (t["median"] <= t.q75).all()


def test_wagner_positive():
    _, s = wag()
    assert s.set_index("stat").value["slope"] > 0


def test_europe_pre_transfer_gini_above_disposable():
    from make_mr_test import europe
    e = europe()
    assert len(e) >= 30 and (e.b > e.c).all()
