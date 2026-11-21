import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_identity_s_minus_i():
    b = pd.read_csv(OUT / "brenland.csv")
    assert ((b.S - b.I) == b.CA).all()
    assert b.q.iloc[0] == 100


def test_price_level_rises_with_income():
    k = pd.read_csv(OUT / "pli_key.csv").iloc[0]
    assert k.n > 150 and k.slope > 0.1 and k["corr"] > 0.4


def test_current_accounts():
    k = pd.read_csv(OUT / "bop_key.csv").iloc[0]
    assert k.usa2024 < -500 and k.chn2024 > 200
