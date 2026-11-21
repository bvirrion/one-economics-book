import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_log_relation_positive():
    k = pd.read_csv(OUT / "well_key.csv").iloc[0]
    assert k.n_ls >= 30 and 0 < k.per_doubling < 2 and k.corr_ls > 0.3


def test_hours_fall_with_income():
    k = pd.read_csv(OUT / "well_key.csv").iloc[0]
    assert k.hours_per_doubling < 0 and k.corr_hr < 0


def test_five_countries_double():
    f = pd.read_csv(OUT / "five.csv")
    assert (f.income.iloc[1:].values == 2 * f.income.iloc[:-1].values).all()
    assert f.lifesat.is_monotonic_increasing


def test_composite_reorders():
    c = pd.read_csv(OUT / "composite.csv").set_index("iso3")
    assert len(c) == 13 and c.loc["USA", "r_y"] == 1 and c.loc["USA", "r_c"] > 1
    assert c.loc["JPN", "r_c"] < c.loc["JPN", "r_y"]
    assert ((c["i_le"] > 0) & (c["i_le"] <= 1) & (c.i_y > 0) & (c.i_y <= 1)).all()


def test_co2_rises_with_income():
    k = pd.read_csv(OUT / "nature_key.csv").iloc[0]
    assert k.n_co2 > 150 and k["corr_co2"] > 0.6 and 0.7 < k.slope_co2 < 1.3


def test_spread_lowers_mean_satisfaction():
    d = pd.read_csv(OUT / "dist.csv").set_index("case")
    assert d.loc["spread", "mean"] == d.loc["equal", "mean"] and d.loc["spread", "sat_gap"] > 0
