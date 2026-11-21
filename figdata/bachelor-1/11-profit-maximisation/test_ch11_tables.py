"""Facts the charts of b1 ch. 11 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_area():
    d = pd.read_csv(OUT / "crop_area.csv").set_index("year")
    assert d.loc[2024, "soya_bra"] > 10 * d.loc[1970, "soya_bra"]


def test_yield():
    g = pd.read_csv(OUT / "yield_growth.csv").set_index("region")
    assert (g.ratio > 1.5).all()


def test_flour():
    f = pd.read_csv(OUT / "flour.csv").set_index("year")
    assert f.loc[2008, "flour"] > 1.4 * f.loc[2006, "flour"]
