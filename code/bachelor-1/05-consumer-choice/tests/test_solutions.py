"""The numbers the solutions of b1 ch. 5 print."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "sol05", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_exercises():
    assert sol.cd_demand(0.25, 2, 5, 100) == (12.5, 15)
    assert sol.complements(2, 1, 70) == (30, 10)
    assert sol.quasi(0.5, 20) == (16, 12)
    assert sol.quasi(0.5, 5) == (10, 0)


def test_problem():
    p = sol.problem()
    assert sol.gamma() == 3532
    assert (p["cd_poor"], p["cd_rich"]) == (2316, 8504)
    assert (p["sg_poor"], p["sg_rich"]) == (3986, 5727)
    assert (p["s_sg_poor"], p["s_sg_rich"]) == (0.342, 0.134)
    assert (p["eta_poor"], p["eta_rich"]) == (0.164, 0.418)
    assert p["c_new"] == 12803 and p["f_cd"] == 4099
    assert (p["f_log"], p["s_log"]) == (3842, 0.3)
    assert (p["sg_new"], p["s_sg_new"]) == (4051, 0.316)
    assert (p["f_sg_obs"], p["s_sg_obs"]) == (3791, 0.296)
    assert p["s_log"] == pytest.approx(0.300)
