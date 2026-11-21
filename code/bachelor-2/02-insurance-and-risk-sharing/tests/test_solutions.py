"""The numbers the solutions of b2 ch. 2 print, recomputed."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "sol02", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_contingent_and_cover():
    c = sol.ex_contingent()
    assert (
        round(c["slope"], 2) == -7.33 and c["fair_slope"] == -9 and c["full"] == 47600
    )
    assert round(100 * c["loading"]) == 20
    v = sol.ex_cover()
    assert round(v["c12"]) == 10985 and round(v["good12"]) == 48682
    assert round(v["bad12"]) == 39667 and round(v["c15"]) == 1569
    assert v["psi0"] == 0.15625 and round(100 * v["load0"], 2) == 56.25


def test_borch_cara():
    b = sol.ex_borch()
    assert round(b["share1"], 4) == 0.3333 and round(b["k"]) == 3333
    assert [round(x) for x in b["z1"]] == [36667, 23333]
    assert [round(x) for x in b["z2"]] == [63333, 36667]


def test_six_countries_and_world():
    s = sol.ex_six_countries()
    assert s["USA"] == (1.76, 1.97, 1.12) and s["JPN"] == (2.05, 1.5, 0.73)
    assert s["KOR"] == (3.23, 4.4, 1.36) and s["FRA"] == (2.22, 1.85, 0.83)
    assert s["BRA"] == (2.65, 3.13, 1.18) and s["IND"] == (2.89, 2.83, 0.98)
    assert sol.world_sd() == 1.79


def test_pooling_and_portfolio():
    assert [round(sol.ex_pooling(n), 1) for n in (1, 10, 100)] == [
        1585.7,
        1046.2,
        1004.5,
    ]
    assert round(sol.ex_portfolio(), 3) == 0.514


def test_problem():
    p = sol.problem()
    assert (
        round(p["pg"], 2) == 0.6
        and round(p["mean"]) == 22000
        and round(p["sd"]) == 9798
    )
    assert round(p["corr"], 3) == 0.167
    assert round(p["eu_alone"], 4) == 9.8695 and round(p["ce_alone"]) == 19332
    assert round(p["sd_agg"]) == 7483 and round(p["sd_idio"]) == 6325
    assert round(p["eu_shared"], 4) == 9.927 and round(p["ce_shared"]) == 20477
    assert round(p["gain"]) == 1145 and round(100 * p["var_cut"], 1) == 41.7
    assert round(p["k"]) == 7333
    assert [round(p["z1"][s]) for s in ("GG", "GB", "BB")] == [27333, 20667, 14000]
    assert round(p["psi"], 2) == 0.48 and round(p["cover"]) == 13462
    assert round(p["good"]) == 23538 and round(p["bad"]) == 17000
    assert round(p["ce_ins"]) == 20666 and round(p["profit"]) == 1077
    b = sol.problem_bb_cover()
    assert (
        round(b["psi"], 2) == 0.24
        and round(b["cover"]) == 9391
        and round(b["ce"]) == 21072
    )
