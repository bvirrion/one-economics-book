import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_orders_of_magnitude():
    k = pd.read_csv(OUT / "sugar_key.csv").iloc[0]
    assert k.farms == 8070
    assert 5 < k.cost_pp < 10 and 100000 < k.benefit_pf < 150000
