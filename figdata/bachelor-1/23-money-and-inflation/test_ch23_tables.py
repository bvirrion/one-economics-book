"""Facts the charts of b1 ch. 23 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_velocity():
    v = pd.read_csv(OUT / "velocity.csv")
    assert v.shape[1] == 5
    us = v.set_index("year").usa
    assert us[2020] < us[1960]


def test_qt():
    s = pd.read_csv(OUT / "qt_stats.csv").iloc[0]
    assert s["corr"] > 0.5


def test_qt_slopes_recomputed():
    # Slopes recomputed from the plotted points as cov/var, not with the script's polyfit.
    d = pd.read_csv(OUT / "qt_decades.csv")
    s = pd.read_csv(OUT / "qt_stats.csv").iloc[0]

    def slope(x):
        return x.gm.cov(x.pi) / x.gm.var()

    assert len(d) == s["n"] == 228
    assert round(slope(d), 3) == s["slope"]
    low = d[d.pi <= 30]
    assert len(d) - len(low) == 2
    assert round(slope(low), 3) == s["low30_slope"]
    assert round(slope(d[d.gm < 15]), 3) == s["gm15_slope"]
    assert round(slope(d[d.decade >= 1950]), 3) == s["since1950_slope"]
    assert d.pi.max() < 55 and d.gm.max() < 40  # every point inside the chart's axes
