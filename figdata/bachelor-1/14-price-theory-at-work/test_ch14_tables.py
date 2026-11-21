"""Facts the charts of b1 ch. 14 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_yields():
    d = pd.read_csv(OUT / "rent_yield.csv")
    assert len(d) == 71
    y = d[["yield_fra", "yield_gbr", "yield_usa"]]
    assert (y > 1).all().all() and (y < 10).all().all()


def test_seasonal():
    r = pd.read_csv(OUT / "seasonal_range.csv").set_index("item")
    assert r.loc["strawberries", "range"] > 3 * r.loc["potatoes", "range"]
    assert r.loc["potatoes", "range"] > r.loc["rice", "range"]
