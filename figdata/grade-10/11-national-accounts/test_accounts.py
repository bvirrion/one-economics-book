import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_shares_near_100():
    d = pd.read_csv(OUT / "shares.csv")
    assert len(d) == 6 and d.notna().all().all()
    assert ((d.total - 100).abs() < 6).all()


def test_brenland_identity():
    r = pd.read_csv(OUT / "bren_2025.csv").iloc[0]
    assert r.C_25 + r.I_25 + r.G_25 + r.X_25 - r.M_25 == r.gdp_25
    assert abs(r.gdp_25 / r.deflator_25 * 100 - r.real_gdp_25) < 5
