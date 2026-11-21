import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_youth_above_total():
    e = pd.read_csv(OUT / "eu_unemp.csv")
    assert (e.youth > e.total).all()


def test_steady_states():
    k = pd.read_csv(OUT / "bren_key.csv").iloc[0]
    assert k.uA == 4.0 and k.uB == 10.0 and k.uall == 5.5


def test_usa_2019_fixed():
    u = pd.read_csv(OUT / "jst_USA.csv").set_index("year").unemp
    assert 3.5 < u.loc[2019] < 4.0


def test_path_returns():
    p = pd.read_csv(OUT / "bren_path.csv")
    assert abs(p["all"].iloc[-1] - 5.5) < 0.1


def test_growth_2024():
    g = pd.read_csv(OUT / "growth_2024.csv").set_index("iso3")
    assert g.loc["DEU", "growth"] < 0 < g.loc["SWE", "growth"] < g.loc["ESP", "growth"]
