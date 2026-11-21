import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_cross_section():
    k = pd.read_csv(OUT / "qtm_key.csv").iloc[0]
    assert k.n >= 120 and k["corr"] > 0.95
    t = pd.read_csv(OUT / "qtm.csv").set_index("iso3")
    assert (t.money > 0).all() and (t.infl > 0).all()
    assert t.infl.idxmax() == "COD" and t.infl.idxmin() == "JPN"


def test_velocity_fell_after_2007():
    v = pd.read_csv(OUT / "velocity.csv").set_index("year").v
    assert v.loc[2007] > 1.9 and v.loc[2019] < 1.5 and v.idxmax() < 2007


def test_us_two_years():
    u = pd.read_csv(OUT / "qtm_us.csv").set_index("year")
    assert 2.0 < u.loc[2019, "money"] / u.loc[2007, "money"] < 2.1
    assert 1.23 < u.loc[2019, "cpi"] / u.loc[2007, "cpi"] < 1.24
