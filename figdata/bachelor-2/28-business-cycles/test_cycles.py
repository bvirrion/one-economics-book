import numpy as np
from econdata import sm_dataset
from make_cycles import moderation, moments, recessions, vol_summary


def test_vol():
    v = vol_summary().set_index("year")
    assert (v.loc[1950, "DEU"], v.loc[1950, "median"]) == (27.29, 6.2)
    assert (v.loc[2007, "USA"], v.loc[2007, "median"]) == (1.11, 1.13)
    assert v["median"].min() == v.loc[2019, "median"] == 0.89


def test_moments():
    m = moments().set_index("var")
    assert (m.loc["investment", "rel"], m.loc["consumption", "rel"]) == (4.66, 0.8)
    assert (m.loc["unemployment", "corr"], m.loc["government", "corr"]) == (
        -0.88,
        -0.06,
    )


def test_moderation_by_hand():
    # independent route: annual sums instead of annual means give the same growth rates
    d = sm_dataset("macrodata")
    a = d.groupby("year").realgdp.sum()
    g = 100 * (a / a.shift(1) - 1)
    sd = round(float(np.std(g.loc[1960:1983], ddof=1)), 2)
    assert sd == moderation().set_index("period").loc["1960--1983", "sd"] == 2.47
    assert list(moderation()["sd"]) == [2.47, 1.58, 1.01]


def test_recessions():
    r = recessions()
    assert len(r) == 8 and (r.start.iloc[-1], r.end.iloc[-1]) == (2007.75, 2009.25)
