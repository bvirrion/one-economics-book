import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_transfers_lower_gini():
    e = pd.read_csv(OUT / "eu_gini.csv")
    assert (e.before > e.after).all()


def test_brenland():
    f = pd.read_csv(OUT / "bren_fifths.csv")
    assert abs(f.market.sum() - 100) < 1e-9 and abs(f.disposable.sum() - 100) < 1e-9
    k = pd.read_csv(OUT / "bren_key.csv").iloc[0]
    assert k.gini_m > k.gini_d


def test_lorenz_ends():
    for iso in ["SWE", "USA", "BRA", "ZAF"]:
        x = pd.read_csv(OUT / f"lorenz_{iso}.csv")
        assert x["cum"].iloc[0] == 0 and abs(x["cum"].iloc[-1] - 100) < 0.01
