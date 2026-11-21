"""Facts the energy--income charts of b1 ch. 3 show."""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_2019():
    d = pd.read_csv(OUT / "energy_income_2019.csv")
    s = pd.read_csv(OUT / "energy_income_stats.csv").set_index("year")
    assert len(d) == s.loc[2019, "n"] > 150 and not d.iso3.duplicated().any()
    b = np.polyfit(np.log(d.gdppc), np.log(d.energy), 1)[0]
    assert 0.9 < b < 1.6 and abs(b - s.loc[2019, "slope"]) < 0.01
    usa = d.set_index("iso3").loc["USA"]
    assert usa.energy > 250 and usa.gdppc > 60000


def test_fit_line_and_common_sample():
    s = pd.read_csv(OUT / "energy_income_stats.csv").set_index("year")
    f = pd.read_csv(OUT / "energy_fit_2019.csv")
    pred = np.exp(s.loc[2019, "intercept"] + s.loc[2019, "slope"] * np.log(f.gdppc))
    # the stats table rounds the slope to 2 decimals: at ln(gdppc) near 12 that moves the
    # prediction by up to exp(0.005 x 12) - 1, about 6%
    assert np.allclose(pred, f.fit, rtol=0.07)
    c = pd.read_csv(OUT / "energy_income_common.csv").set_index("year")
    assert c.loc[1990, "n"] == c.loc[2019, "n"]
