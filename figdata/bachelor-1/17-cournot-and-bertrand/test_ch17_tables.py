"""Facts the opening chart of b1 ch. 17 shows."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_ratios():
    r = pd.read_csv(OUT / "ratios.csv").set_index("profession")
    assert (r.loc[r.index != "Cournot", "r21"] > 1).all()
    assert r.loc["Doctors", "r21"] > r.loc["Cournot", "r21"]
