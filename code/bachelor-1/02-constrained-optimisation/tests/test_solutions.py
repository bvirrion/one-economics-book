"""The numbers the solutions of b1 ch. 2 print, checked against a numerical optimiser."""

import importlib.util
import math
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "sol02", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def eq(g):
    return [{"type": "eq", "fun": g}]


def test_worked_example():
    w = sol.worked_example()
    x = sol.numeric_max(
        lambda v: math.sqrt(max(v[0] * v[1], 0)),
        eq(lambda v: v[0] + 2 * v[1] - 12),
        [4, 4],
    )
    assert x == pytest.approx([6, 3], abs=1e-4)
    assert round(w["lam"], 4) == 0.3536 and round(w["f_14"], 4) == 4.9497


def test_exercises():
    assert sol.ex_substitution() == {"x": 6.0, "y": 4.0, "f": 24.0}
    x = sol.numeric_max(
        lambda v: v[0] * v[1], eq(lambda v: 2 * v[0] + 3 * v[1] - 24), [3, 3]
    )
    assert x == pytest.approx([6, 4], abs=1e-4)
    assert sol.ex_level_slope() == -4
    r = sol.ex_lagrange_log()
    assert (r["x"], r["y"], r["lam"]) == (10, 10, 0.1)
    assert round(r["dv_exact"], 3) == 0.863
    c = sol.ex_corner()
    assert (c["x"], c["y"], c["lam"]) == (0, 0.5, 2)
    k = sol.student_kinks()
    assert round(k["h1"], 2) == 6.67 and round(k["h2"], 2) == 33.33
    assert round(k["y1"]) == 300 and round(k["y2"]) == 500
    assert k["slopes"] == (15, 7.5, 15)
    d = sol.ex_dual()
    assert round(d["cost"], 6) == 12 and d["mu"] * d["lam_primal"] == pytest.approx(1)


def test_farm():
    f = sol.farm()
    assert (f["x"], f["y"], f["profit"], f["lam"]) == (16, 4, 12000, 300)
    x = sol.numeric_max(
        lambda v: 2400 * math.sqrt(max(v[0], 0)) + 1200 * math.sqrt(max(v[1], 0)),
        eq(lambda v: v[0] + v[1] - 20),
        [10, 10],
        bounds=[(0, 20), (0, 20)],
    )
    assert x == pytest.approx([16, 4], abs=1e-3)
    assert f["water_used"] == 8400 and sol.farm(water=9000)["mu"] == 0
    assert round(sol.farm_value(21) - sol.farm_value(20), 2) == 296.34
    w = sol.farm(water=6000)
    assert (w["x"], w["y"]) == (10, 10) and round(w["profit"]) == 11384
    assert round(w["mu"], 4) == 0.4743 and round(w["lam"], 1) == 142.3
