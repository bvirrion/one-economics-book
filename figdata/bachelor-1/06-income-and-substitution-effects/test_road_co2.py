"""Facts the opening chart of b1 ch. 6 shows."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_road():
    d = pd.read_csv(OUT / "road_co2.csv").set_index("year")
    assert d.index.min() == 1960 and d.index.max() == 2022
    assert d.loc[2019, "sweden"] < d.loc[2019, "peers"]
    assert d.notna().all().all()
