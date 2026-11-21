import numpy as np
from dalen import ar1, forecasts, table
from jstreal import half_life
from make_pli import tables as pli
from make_real_rates import tables as real
from make_uip import tables as uip
import pandas as pd


def test_half_life_of_known_ar1():
    rng = np.random.default_rng(1)
    q = [0.0]
    for _ in range(4000):
        q.append(0.8 * q[-1] + rng.normal())
    rho, hl = half_life(pd.Series(q, index=range(len(q))))
    assert abs(rho - 0.8) < 0.03 and abs(hl - np.log(0.5) / np.log(0.8)) < 0.5


def test_richer_countries_dearer():
    _, _, s = pli()
    assert s.set_index("stat").value["slope"] > 0


def test_float_half_lives_shorter():
    _, h, _ = real()
    assert h.hl_float.median() < h.hl_all.median()


def test_uip_slope_below_one():
    _, _, s = uip()
    v = s.set_index("stat").value
    assert v["slope"] + 2 * v["slope_se"] < 1


def test_dalen_real_rate_indexed():
    d = table()
    assert np.isclose(d.loc[d.year == 2015, "real"].iloc[0], 100)
    rho, _ = ar1(d)
    assert 0 < rho < 1
    assert len(forecasts(d)) == 10


def test_war_years_left_out_of_chart():
    from make_real_rates import WARS, tables
    w = tables()[0].set_index("year")
    assert w.loc[WARS].isna().all().all() and w.loc[1913].notna().any()
