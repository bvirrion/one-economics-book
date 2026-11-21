"""The numbers the solutions of b1 ch. 6 print."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "sol06", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_household_a():
    a = sol.household("A")
    assert (a["f0"], a["f1"], a["m_s"], a["f_s"]) == (1000, 800, 20500, 820)
    assert a["sub_s"] == pytest.approx(-180) and a["inc_s"] == pytest.approx(-20)
    assert (a["cv"], a["f_h"], a["sub_h"], a["inc_h"]) == (451.3, 818.1, -181.9, -18.1)


def test_cheque():
    w = sol.with_cheque()
    assert (w["F0"], w["F1"], w["rev1"]) == (3700, 2960, 1480)
    assert w["F"] == pytest.approx(7400 / 2.46, abs=0.05)
    assert (w["c"], w["fall"], w["fall_no"]) == (501.4, 18.7, 20.0)
    assert w["cv"] == {"A": 451.3, "B": 540.4, "C": 673.9} and w["cv_sum"] == 1665.6
    assert (w["FH"], w["fall_h"]) == (3011.6, 18.6)
    assert w["gain"] == {"A": 50.1, "B": -39.0, "C": -172.5}


def test_exercises():
    e = sol.exercises()
    assert (e["x0"], e["x1"], e["xs"], e["sub_s"], e["inc_s"]) == (
        50,
        25,
        37.5,
        -12.5,
        -12.5,
    )
    assert (e["m_h"], e["xh"], e["sub_h"], e["inc_h"]) == (
        141.42,
        35.36,
        -14.64,
        -10.36,
    )


def test_proportional():
    assert sol.proportional_cheque() == {"F": 3004.47, "fall": 18.8}
