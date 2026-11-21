import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_cross():
    k = pd.read_csv(OUT / "cross_key.csv").iloc[0]
    assert k.n > 120 and 0.5 < k.slope < 1.1
    assert k.usa_y > 5 * k.ind_y


def test_accounts_add_up():
    a = pd.read_csv(OUT / "accounts.csv")
    assert ((a.cap + a.tfp - a.gy).abs() < 0.02).all()
    g = a.set_index("iso3")
    assert g.loc["KOR", "gy"] > g.loc["USA", "gy"]


def test_brenland():
    b = pd.read_csv(OUT / "bren.csv").set_index("year")
    assert abs(b.loc[2001, "K"] - (0.95 * b.loc[2000, "K"] + b.loc[2000, "I_real"])) < 1.5
    k = pd.read_csv(OUT / "bren_key.csv").iloc[0]
    assert abs(k.cap + k.tfp - k.gy) < 0.02 and 0.4 < k.tfp_share < 0.6
    assert k.tfp_share_k25 < k.tfp_share
