import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_break_after_2008():
    x = pd.read_csv(OUT / "usa_money.csv").set_index("year")
    assert x.loc[2007, "ratio"] > 8 and x.loc[2014, "ratio"] < 3.5
    assert x.loc[2019, "narrowm"] > 4 * 0.98 * x.loc[2007, "narrowm"]


def test_ratio_moved_before_2008():
    r = pd.read_csv(OUT / "usa_ratio_long.csv").set_index("year").ratio
    assert r.loc[1950] < 6 and r.loc[1985] > 11 and 7 < r.loc[2000] < 9 and r.loc[2020] < 5
