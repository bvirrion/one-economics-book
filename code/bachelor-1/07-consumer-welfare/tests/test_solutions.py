"""The numbers the solutions of b1 ch. 7 print."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "sol07", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_indices():
    i = sol.indices()
    assert (i["total"], i["cost25"], i["lasp"]) == (10850, 15565.68, 143.46)
    assert (i["harm"], i["paasche"], i["geo"]) == (7612.72, 142.52, 142.97)
    assert sol.growth(143.46) == 3.67 and sol.growth(142.97) == 3.64


def test_new_good_and_pension():
    n = sol.new_good()
    assert (n["choke"], n["q25"], n["cs25"], n["cs20"]) == (30, 40, 400, 100)
    assert (n["share"], n["e_old"], n["e_new"], n["idx"]) == (
        2.57,
        15512.25,
        15112.25,
        139.28,
    )
    assert (n["g_new"], n["g_geo"]) == (3.37, 3.64)
    p = sol.pension()
    assert (p["lasp"], p["geo"], p["gap25"], p["cum"]) == (21519, 21445.5, 73.5, 271.5)
    assert (p["chain"], p["chain_gap"]) == (21490.5, 28.5)


def test_exercises():
    e = sol.exercises()
    assert (e["cs_loss"], e["cv"], e["ev"], e["cs"]) == (375, 414.21, 292.89, 346.57)
    assert (e["true"], e["lasp"], e["L2"]) == (1.4142, 1.5, 1.5)
