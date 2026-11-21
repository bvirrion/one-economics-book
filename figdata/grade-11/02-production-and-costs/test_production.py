import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_cereal_fit():
    f = pd.read_csv(OUT / "cereal_fit.csv").iloc[0]
    assert f.n > 170 and f.b > 0 and f.mp20 > f.mp200 > 0


def test_fertilizer_steps_fall_per_teaspoon():
    c = pd.read_csv(OUT / "fertilizer.csv")
    per_tsp = (c.step_yield / c.dose.diff()).dropna().tolist()
    assert per_tsp == sorted(per_tsp, reverse=True)
