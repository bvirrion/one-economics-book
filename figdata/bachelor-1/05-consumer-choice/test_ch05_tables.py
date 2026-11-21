"""Facts the charts of b1 ch. 5 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_cex():
    d = pd.read_csv(OUT / "cex_shares.csv")
    assert len(d) == 15
    for _, g in d.groupby("year"):
        g = g.set_index("fifth")
        assert g.loc[1, "food_home"] > g.loc[5, "food_home"]
        assert g.loc[1, "shelter"] > g.loc[5, "shelter"]
        assert g.spending.is_monotonic_increasing
    s = pd.read_csv(OUT / "cex_slopes.csv").set_index(["year", "item"]).slope
    assert (s.xs("food_home", level="item") < 1).all()


def test_brenland():
    t = pd.read_csv(OUT / "brenland_tenths.csv")
    assert len(pd.read_csv(OUT / "brenland_food.csv")) == 2000
    assert t.share.iloc[0] > t.share.iloc[-1]
    f = pd.read_csv(OUT / "brenland_fit.csv").iloc[0]
    assert f.log_slope < 1 and 0 < f.b < f.agg_share
