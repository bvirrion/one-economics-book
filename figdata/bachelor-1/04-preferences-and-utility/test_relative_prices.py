"""Facts the opening chart of b1 ch. 4 shows."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_indices():
    w = pd.read_csv(OUT / "hicp_categories.csv")
    assert w.year.min() == 1996 and w.year.max() == 2024 and len(w) == 29
    base = w[w.year == 2015].drop(columns="year").iloc[0]
    assert (base == 100).all()
    r = pd.read_csv(OUT / "hicp_ratios.csv").set_index("category")
    assert r.loc["audiovisual", "ratio"] < 0.25 and r.loc["electricity", "ratio"] > 2
