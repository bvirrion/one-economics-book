"""The numbers the solutions of b2 ch. 1 print, recomputed."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "sol01", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_calibration_numbers():
    r = sol.ex_rabin_gamma()
    assert round(r["gamma"]) == 91 and round(r["approx"]) == 91
    assert round(r["loss_any_gain"]) == 769
    c = sol.ex_calibration()
    assert c["bound"] == 2310 and c["step"] == 210
    assert f"{c['after_100_steps']:.1e}" == "7.3e-05"
    assert round(1 / c["after_100_steps"], -2) == 13800


def test_small_risks():
    s = sol.ex_small_risk()
    assert (
        round(s["approx"]) == 750
        and round(s["exact"]) == 746
        and round(s["exact_rich"]) == 374
    )
    c = sol.ex_cara()
    assert round(c["premium"], 2) == 240.23 and round(c["approx"]) == 250


def test_dominance_example():
    d = sol.ex_dominance()
    assert d["mean"] == (65.0, 60.0)
    assert round(d["sqrt"][0], 2) == 7.12 and round(d["sqrt"][1], 2) == 7.24


def test_deductible_exercise():
    d = sol.ex_deductible()
    assert d["expected_saving"] == 20 and round(d["load"], 1) == 2.7
    assert f"{d['a']:.2e}" == "6.74e-04" and round(d["rra_200k"]) == 135


def test_price_list_interval():
    g6, g7 = sol.price_list_gamma(6), sol.price_list_gamma(7)
    assert round(g6, 2) == 0.40 and round(g7, 2) == 0.66
    # the tie gamma rises with the row: one switch point for every CRRA agent
    gs = [sol.price_list_gamma(k) for k in range(1, 10)]
    assert gs == sorted(gs)


def test_farmer_problem():
    p = sol.problem()
    assert p["mean"] == 48000 and round(p["sd"]) == 18330
    assert round(p["eu"], 4) == 10.6725 and round(p["ce"]) == 43153
    assert round(p["premium"]) == 4847 and round(p["approx"]) == 3500
    assert round(p["ce_sqrt"]) == 45749 and round(p["premium_sqrt"]) == 2251
    assert (
        p["s_mean"] == 47500
        and round(p["eu_s"], 4) == 10.7332
        and round(p["ce_s"]) == 45855
    )
    assert round(p["gamma_tie"], 2) == 0.18
    assert round(p["eu_half"], 4) == 10.7097 and round(p["ce_half"]) == 44787
    assert round(p["fair"]) == 12000 and round(p["pmax"]) == 16847
    assert round(100 * p["loading"], 1) == 40.4
    assert p["cover_036"] == 28125 and p["q0"] == 0.5625 and p["load0"] == 0.875
    assert f"{p['a']:.2e}" == "2.61e-05"
    assert round(p["premium_sav"]) == 2550 and round(p["pmax_sav"]) == 14550
    assert round(100 * p["loading_sav"], 1) == 21.2
