import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_decomposition_adds_up():
    d = pd.read_csv(OUT / "uk_decomp.csv").set_index("item")
    k = pd.read_csv(OUT / "debt_key.csv").iloc[0]
    assert abs(d.points.sum() + k.fall) < 0.5
    assert abs(d.share.sum() - 100) < 0.5
    assert 30 < k.growth_net_share < 70


def test_series():
    k = pd.read_csv(OUT / "debt_key.csv").iloc[0]
    assert k.gbr1946 > 200 and k.usa1946 > 100 and k.gbr_max > 250
    e = pd.read_csv(OUT / "debt_euro.csv").set_index("year")
    assert e.loc[2011, "EL"] > 150 and k.euro12_over3 > 30
