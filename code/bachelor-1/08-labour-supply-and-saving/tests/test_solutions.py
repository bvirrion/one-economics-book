"""The numbers the solutions of b1 ch. 8 print."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "sol08", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_budget_and_optima():
    p = sol.problem()
    assert (p["c800"], p["c1250"], p["c1200"], p["keep2"]) == (
        15240,
        17400,
        17160,
        0.32,
    )
    assert (p["h_ana"], p["c_ana"], p["u_ana"], p["u_kink1250"]) == (
        507.7,
        12960,
        8.4804,
        8.3861,
    )
    assert p["best_ana"] == pytest.approx(507.7) and p["best_ben"] == 800
    assert p["ben_h1"] == pytest.approx(923.08, abs=0.01)
    assert (p["ben_h2"], p["ben_h3"]) == (312.5, 1400)
    assert p["prod_kink"] > p["prod_3"]
    assert (p["res_ana"], p["res_ben"], p["h18"]) == (8.65, 5.77, 623.1)
    assert (p["h_new"], p["c_new"], p["best_ana_new"]) == (685.7, 16200, 685.7)
    assert (p["ben_old"], p["ben_new"], p["cost"]) == (5344.6, 5914.3, 569.7)
    assert p["best_ben_new"] == 800


def test_saving():
    assert sol.saving(16200, 12960, 0.04) == {
        "wealth": 28661.54,
        "c1": 14623.23,
        "s": 1576.77,
        "c2": 14599.84,
    }
    assert sol.saving(16200, 12960, 0.08)["s"] == 1812.24
    assert sol.saving(9000, 30000, 0.04)["s"] == -10309.26
    e = sol.exercises()
    assert e["res"] == 2 and e["h_log"](20, 6000) == 1350
    assert e["c1_two"]["c1"] == 25814.54 and e["c1_two"]["c2"] == 24394.74
