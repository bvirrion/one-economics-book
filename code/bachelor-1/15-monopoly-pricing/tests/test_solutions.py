"""Check the printed numbers of b1 ch. 15."""

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
    s, d = p["single"], p["disc"]
    assert (s["p"], s["Q"], s["profit"], s["dwl"]) == (29, 95, 1805, 902.5)
    assert s["tourists_only"] < s["profit"]
    assert (d["profit"], d["dwl"]) == (2125, 1062.5)
    assert p["pass"]["removed"] == 32.13
    assert p["reg"]["pac"] == 21.19


def test_exercises():
    e = sol.exercises()
    assert e["welfare"]["dwl_disc"] == 1000 and e["welfare"]["dwl_single"] == 900
    assert e["ramsey"]["p"] == 40 and e["bundle"] == {"separate": 16, "bundle": 22}
