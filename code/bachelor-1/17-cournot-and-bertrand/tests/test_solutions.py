"""Check the printed numbers of b1 ch. 17."""

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
    assert p["A"] == {"q": 80, "Q": 80, "p": 40, "profit": 800}
    assert p["B2"]["q"] == 120 and p["B2"]["profit"] == 800
    assert p["thresholds"] == [2, 4.5, 8, 12.5] and p["S3_over_S1"] == 4
    assert p["n_on_B"] == 3 and p["stackelberg"]["pi1"] == 1000


def test_exercises():
    e = sol.exercises()
    assert e["third"] == 52.5 and e["ts"][0] == 3037.5 and e["dentists"] == 1.79
