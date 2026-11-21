import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_sixties_trade_off():
    d = pd.read_csv(OUT / "phil6069.csv")
    assert d.u.corr(d.pi) < -0.5


def test_seventies_break():
    d = pd.read_csv(OUT / "phil7083.csv").set_index("year")
    assert d.loc[1980, "pi"] > 10 and d.loc[1975, "u"] > 8


def test_ratio():
    k = pd.read_csv(OUT / "phillips_key.csv").iloc[0]
    v = pd.read_csv(OUT / "volcker.csv").set_index("year")
    assert abs(v.loc[1980:1986, "excess"].sum() - k.excess_8086) < 0.05
    assert abs(k.ratio - k.excess_8086 / k.fall) < 0.01
