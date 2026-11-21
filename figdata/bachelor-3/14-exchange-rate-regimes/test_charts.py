import numpy as np
from attack import attack_time, path
from make_euro_prices import table as euro
from make_pegs import table as pegs
from make_trilemma import tables as tri


def test_attack_when_shadow_meets_peg():
    t = attack_time()
    p = path(step=0.001, until=t + 0.01)
    at = p.iloc[(p.t - t).abs().argmin()]
    assert np.isclose(at.shadow, 1.20, atol=1e-3) and np.isclose(t, 8.0)


def test_pegs_share_bounds():
    t = pegs()
    assert t.share.between(0, 100).all()


def test_pegs_follow_base_more_since_1999():
    *_, eras = tri()
    e = eras[eras.era == "1999-2020"].set_index("regime").slope
    assert e["peg"] > e["float"]


def test_euro_rebased():
    t = euro()
    assert np.allclose(t.iloc[0, 1:], 100)
