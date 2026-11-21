import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_falling_marginal_gain():
    f = pd.read_csv(OUT / "life_fit.csv").iloc[0]
    assert f.n > 180 and f.b > 0
    assert f.gain100_at100 > f.gain100_at1000 > f.gain100_at5000 > 0


def test_tax_rates():
    t = pd.read_csv(OUT / "tax_rates.csv").set_index("income")
    assert t.loc[12000, "average"] == 0 and t.loc[13000, "marginal"] == 20
    assert t.loc[50000, "marginal"] == 35 and abs(t.loc[50000, "average"] - 18.2) < 0.01
    assert (t.average <= t.marginal + 1e-9).all()
