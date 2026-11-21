"""The numbers the solutions of b1 ch. 1 print."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "sol01", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_growth_and_real():
    g = sol.ex_growth_per_worker()
    assert (
        round(100 * g["continuous"], 2) == 2.00
        and round(100 * g["discrete"], 2) == 1.98
    )
    b = sol.ex_brenland_real_growth()
    assert b["real_2025"] == b["table_real_2025"] == 292390
    assert (b["g_nom"], b["g_real"], b["g_defl"]) == (4.59, 1.63, 2.96)
    h = sol.ex_real_growth_high_inflation()
    assert round(100 * h["exact"], 2) == 7.14 and round(100 * h["log"], 2) == 6.90
    d = sol.ex_doubling()
    assert round(d["continuous"], 1) == 34.7 and round(d["yearly"], 1) == 35.0


def test_cloud_slopes():
    assert sol.cloud_slope(2, 1, 1, 3) == pytest.approx(-1.25)
    assert sol.cloud_slope(2, 1, 1, 3, 1) == pytest.approx(-2.0)
    assert sol.simulate_cloud_slope(2, 1, 1, 3, 1) == pytest.approx(-2.0, abs=0.02)
    assert sol.cloud_slope(2, 1, 1, 0) == 1 and sol.cloud_slope(2, 1, 0, 1) == -2
    r = sol.ex_shifter_both(-10, -30, 10, 10)
    assert (r["dp"], r["dq"], r["ratio"]) == (1.0, -20.0, -20.0)


def test_problem():
    assert sol.problem_cold_store() == [50.0, 60.0, 54.8, 93.7]
    r = sol.problem_real_price()
    assert (r["nominal"], r["inflation"], r["real_exact"]) == (7.6, 2.5, 5.0)
    assert r["real_price_2025_in_2024_dalens"] == 8.29
    f = sol.problem_fish()
    assert f["means"]["calm"] == (7.9912, 101.12) and f["means"]["storm"] == (
        9.425,
        84.8,
    )
    assert f["means"]["fest"] == (9.4925, 113.25) and f["means"]["all"] == (
        8.4998,
        98.25,
    )
    assert (f["dp_storm"], f["dq_storm"]) == (1.4338, -16.32)
    assert (f["slope_storm"], f["slope_fest"], f["elasticity"]) == (-11.38, 8.08, -0.98)
    assert f["elasticity_true"] == -0.87 and f["elasticity_cloud"] == -0.46
    assert f["arc_storm"] == -1.07
    assert (f["revenue_calm"], f["revenue_storm"]) == (8081, 7992)
