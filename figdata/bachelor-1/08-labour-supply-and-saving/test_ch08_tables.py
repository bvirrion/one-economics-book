"""Facts the charts of b1 ch. 8 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_hours():
    p = pd.read_csv(OUT / "hours_points.csv")
    f = pd.read_csv(OUT / "hours_first.csv").set_index("iso3")
    h19 = p[p.year == 2019].set_index("iso3").avh
    assert (h19 < f.avh.reindex(h19.index)).all()
    assert len(h19) == 6


def test_participation():
    p = pd.read_csv(OUT / "participation_points.csv")
    w = p[p.sex == "women"]
    assert len(w) == 6 and (w.y2024 > w.y1991).sum() >= 5
