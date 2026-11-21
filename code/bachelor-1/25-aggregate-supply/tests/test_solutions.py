"""Check the printed numbers of b1 ch. 25."""

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_problem():
    p = sol.problem()
    assert p["cold"]["excess"] == p["grad"]["excess"] == 12
    assert p["saving"] == 8


def test_exercises():
    e = sol.exercises()
    assert e["y"] == 10100 and e["pi"] == 3.5


def test_natural_rate_matches_the_chart_fit():
    # The printed coefficients give the crossing the chart's own fit reports.
    import pandas as pd

    root = HERE.parents[2]
    s = pd.read_csv(
        root / "figdata/bachelor-1/25-aggregate-supply/out/accel_stats.csv"
    ).iloc[0]
    assert sol.exercises()["un_hat"] == s["un"]
    assert round(s["slope"], 2) == -0.47 and round(s["intercept"], 3) == 2.853
