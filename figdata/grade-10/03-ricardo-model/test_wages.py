import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_axes_and_shares():
    d = pd.read_csv(OUT / "wages_productivity.csv")
    assert d.opw.between(1000, 300000).all() and d.comp.between(100, 300000).all()
    assert (d.comp < d.opw).all()            # labour gets a share below one
    assert len(d) > 120


def test_close_link():
    s = pd.read_csv(OUT / "wages_summary.csv").iloc[0]
    assert s.r > 0.9 and 0.9 < s.slope < 1.2
    sel = pd.read_csv(OUT / "wages_selected.csv")
    assert list(sel.iso3) == ["USA", "DEU", "MEX", "CHN", "IND", "KEN"]
