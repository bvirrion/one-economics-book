import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_crude_shale_rise():
    d = pd.read_csv(OUT / "crude_us.csv").set_index("year")
    assert d.index.min() == 1976 and d.index.max() == 2024
    assert d.loc[2008, "mbd"] < 5.1 and d.loc[2014, "mbd"] > 8.5 and d.loc[2024, "mbd"] > 13
    assert abs(d.loc[2024, "price"] - 3.45) < 0.01


def test_soy_area():
    d = pd.read_csv(OUT / "soy_area.csv").set_index("year")
    assert d.index.min() == 1990
    assert d.loc[d.index.max(), "bra"] > 3 * d.loc[1990, "bra"]
