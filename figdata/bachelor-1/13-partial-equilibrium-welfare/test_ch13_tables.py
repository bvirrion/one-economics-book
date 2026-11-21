"""Facts the opening chart of b1 ch. 13 shows."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_jump():
    p = pd.read_csv(OUT / "de_hicp_points.csv").set_index("month")
    assert p.loc["2021-01", "all"] - p.loc["2020-12", "all"] > 2
    assert p.loc["2020-07", "all"] < p.loc["2020-06", "all"]
