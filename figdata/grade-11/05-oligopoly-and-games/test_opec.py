import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_saudi_swing():
    d = pd.read_csv(OUT / "opec.csv").set_index("year")
    assert d.loc[1981, "sau"] > 2.5 * d.loc[1985, "sau"]
    assert d.loc[1986, "sau"] > d.loc[1985, "sau"]
    assert d.loc[1986, "gas"] < d.loc[1985, "gas"]
