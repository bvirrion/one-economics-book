import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_the_four_episodes():
    d = pd.read_csv(OUT / "world_oil.csv").set_index("year")
    assert d.loc[2009, "q"] < d.loc[2008, "q"] and d.loc[2009, "price"] < d.loc[2008, "price"]     # demand fell
    assert d.loc[2015, "q"] > d.loc[2014, "q"] and d.loc[2015, "price"] < d.loc[2014, "price"]     # supply rose
    assert d.loc[2020, "q"] < d.loc[2019, "q"] and d.loc[2020, "price"] < d.loc[2019, "price"]     # demand fell
    assert d.loc[2021, "q"] > d.loc[2020, "q"] and d.loc[2021, "price"] > d.loc[2020, "price"]     # demand rose
    assert (abs(d.us + d.row - d.q) < 0.011).all()
