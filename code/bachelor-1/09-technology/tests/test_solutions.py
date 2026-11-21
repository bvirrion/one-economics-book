"""Check the printed numbers of b1 ch. 9."""

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
    assert p["ya"] == 342.65 and p["yb"] == 400.0
    assert p["ya2"] == 2 * p["ya"]
    assert p["k_iso"] == 2.494 and p["k_min"] == 1.414
    assert p["sigma"] == 0.6 and p["sigma_hat"] == 0.602
    assert p["sh_kest0"] == 0.715 and p["sh_bren0"] == 0.5
    assert p["sh_kest1"] < p["sh_kest0"] and p["sh_bren1"] < p["sh_bren0"]
    assert p["kl_kest1"] < p["kl_kest"]


def test_exercises():
    e = sol.exercises()
    assert e["mrts_cd"] == 0.6914 and e["scale_8"] == 2.0 and e["scale_16"] == 1.143
