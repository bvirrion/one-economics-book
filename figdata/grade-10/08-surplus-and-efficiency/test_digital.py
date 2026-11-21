import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_table():
    d = pd.read_csv(OUT / "digital_wta.csv")
    assert len(d) == 8
    top = d[d["rank"] == 1].iloc[0]
    assert top.category == "search engines" and top.wta2017 == 17530
    assert (d.wta2017 >= d.wta2016).all()
