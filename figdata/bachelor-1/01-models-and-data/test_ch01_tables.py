"""Facts the charts and the weekend problem of b1 ch. 1 show."""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def t(name):
    return pd.read_csv(OUT / f"{name}.csv")


def test_labour_cloud():
    d = t("labour_cloud")
    assert len(d) == 43 and d.year.min() == 1981 and d.year.max() == 2023
    y2009 = d[d.year == 2009].iloc[0]
    assert y2009.dhours < 0 < y2009.dwage
    s = t("labour_cloud_stats").iloc[0]
    assert s.n == 43
    assert round(np.corrcoef(d.dwage, d.dhours)[0, 1], 2) == s["corr"]
    assert -0.6 < s["corr"] < -0.2


def test_us_gdppc_deflator_is_the_ratio():
    d = t("us_gdppc")
    assert d.year.min() == 1960 and d.year.max() == 2024
    assert d.loc[d.year == 2020, "deflator"].iloc[0] == 100
    ratio = 100 * d.nominal / d.real
    assert (abs(ratio - d.deflator) < 0.05).all()


def test_long_levels_and_growth():
    d = t("gbr_jpn")
    assert d.year.min() == 1870 and d.year.max() == 2022
    g = t("gbr_jpn_growth")
    fastest = g.loc[g.growth.idxmax()]
    assert (fastest.iso3, fastest.start, fastest.end) == ("JPN", 1950, 1973)
    for _, r in g.iterrows():
        assert abs(100 * np.log(r.x1 / r.x0) / (r.end - r.start) - r.growth) < 0.01


def test_curves_cross_at_cloud_points():
    c, cl = t("curves"), t("cloud")
    for k in (1, 2, 3):
        # the k-th pair of lines crosses at the k-th point of the cloud
        bd = (c[f"qd{k}"][1] - c[f"qd{k}"][0]) / 8
        bs = (c[f"qs{k}"][1] - c[f"qs{k}"][0]) / 8
        p = (c[f"qs{k}"][0] - bs - (c[f"qd{k}"][0] - bd)) / (bd - bs)
        assert abs(p - cl.p[k - 1]) < 0.002
    s = t("cloud_stats").iloc[0]
    assert abs((s.var_ud - s.var_us) / (s.var_ud + s.var_us) - s.model_slope) < 0.002


def test_fish_market():
    d, s = t("fish"), t("fish_stats").iloc[0]
    assert len(d) == 40 and d.storm.sum() == 10 and d.festival.sum() == 4
    assert not ((d.storm == 1) & (d.festival == 1)).any()
    g = t("fish_groups")
    assert g.days.tolist() == [26, 10, 4] and g.sum_crates.sum() == d.crates.sum()
    assert round(g.sum_price[0] / 26, 4) == s.p_calm
    slope = (s.q_storm - s.q_calm) / (s.p_storm - s.p_calm)
    assert round(slope, 2) == s.slope_storm == -11.38
    assert round(s.slope_storm * s.p_mean / s.q_mean, 2) == s.elasticity == -0.98
