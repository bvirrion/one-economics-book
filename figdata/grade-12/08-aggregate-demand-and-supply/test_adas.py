import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_gap_and_recessions():
    g = pd.read_csv(OUT / "gap.csv").set_index("year").gap
    assert g[2009] < 0 and g[2020] < 0 and g[1982] < 0 and g[2007] > 0
    r = pd.read_csv(OUT / "recessions.csv")
    assert len(r) == 9 and (r.end > r.start).all()


def test_trend_and_key():
    d = pd.read_csv(OUT / "gdp.csv")
    assert d.gdp.iloc[-1] > 6 * d.gdp.iloc[0]
    k = pd.read_csv(OUT / "adas_key.csv").iloc[0]
    assert 2.5 < k.linear_growth < 3.5 and k.cpi1974 > 10 and k.cpi2022 > 7
