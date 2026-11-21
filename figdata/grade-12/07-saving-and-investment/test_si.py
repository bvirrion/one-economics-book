import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_saving_investment_loose():
    k = pd.read_csv(OUT / "si_key.csv").iloc[0]
    assert k.n > 120 and 0 < k.slope < 0.6 and 0.2 < k["corr"] < 0.8


def test_crises():
    k = pd.read_csv(OUT / "crisis_key.csv").iloc[0]
    assert k.gdp1933 < 75 and k.u1933 > 20 and k.u1929 < 4
    assert 90 < k.gdp2009 < 100 and k.u2010 > 9 and k.house2012 < 90
