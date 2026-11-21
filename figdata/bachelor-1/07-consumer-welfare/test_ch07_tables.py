"""Facts the chart and problem of b1 ch. 7 rely on."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_us():
    d = pd.read_csv(OUT / "us_indices.csv").set_index("year")
    assert d.loc[1990, "cpi"] == 100 and d.loc[1990, "deflator"] == 100
    assert d.loc[2024, "cpi"] > d.loc[2024, "deflator"]


def test_brenland():
    d = pd.read_csv(OUT / "brenland_indices.csv").set_index("year")
    last = d.loc[2025]
    assert last.laspeyres >= last.chained >= last.geometric >= last.paasche
    assert abs(pd.read_csv(OUT / "brenland_basket.csv").share.sum() - 1) < 1e-3
