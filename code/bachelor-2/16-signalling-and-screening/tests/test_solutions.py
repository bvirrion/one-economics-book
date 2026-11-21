"""The numbers the text and solutions of b2 ch. 16 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol16", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_menu():
    out = subprocess.run(
        [sys.executable, "menu.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "light plan: 2.00 units for 10.00" in out
    assert "heavy plan: 8.00 units for 40.00" in out
    assert "rent 8.00; profit per user 12.00" in out
    assert (HERE / "outputs" / "menu.txt").read_text().endswith(out)
    s = sol.screen(6.0, 10.0, 2.0, 2 / 3)
    assert (r(s["q_l"], 6), s["q_h"], r(s["fee_l"], 6), r(s["fee_h"], 6)) == (
        2.0,
        8,
        10.0,
        40.0,
    )


def test_signalling():
    assert sol.separating_range() == (2.5, 5.0)
    assert sol.separating_range(12, 18, 3, 1.5) == (2.0, 4.0)
    assert sol.pooling_bound() == (15.0, 1.25)
    assert sol.pooling_bound(share_high=0.8) == (18.0, 2.0)
    assert sol.deviation() == (8.0, 14.0, 12.0)
    assert sol.waste(share_high=0.8)["pooled"] == 18.0


def test_insurance():
    u = sol.rs_utilities()
    assert (r(u["x"], 2), r(u["premium"], 2), r(u["low_sep"], 3)) == (9.12, 1.82, 4.479)
    assert r(u["low_full_high"], 3) == 4.317
    x, w1, w2, check = sol.rs_low_cover()
    assert (r(w1, 2), r(w2, 2), abs(check) < 1e-12) == (98.18, 57.29, True)
    b = sol.pooling_breaks()
    assert (r(b["premium"], 1), r(b["u_pool"], 3)) == (11.5, 4.483)
    assert (r(b["p_star"], 4), r(b["share_star"], 3)) == (0.237, 0.877)


def test_menus():
    assert sol.menu_checks() == {
        "light_own": 0.0,
        "light_other": -24.0,
        "heavy_own": 8.0,
        "heavy_other": 8.0,
    }
    half = sol.screen(6.0, 10.0, 2.0, 0.5)
    assert (half["q_l"], half["fee_h"], half["profit"]) == (0.0, 48.0, 16.0)


def test_phones():
    p = sol.phones()
    s = p["screen"]
    assert (s["q_l"], s["q_h"], s["fee_l"], s["fee_h"], s["rent"]) == (
        15.0,
        30.0,
        337.5,
        600.0,
        150.0,
    )
    assert s["full"]["fee"] == (400.0, 750.0)
    assert (p["full_profit"], p["profit"], p["rents"], p["dwl"]) == (
        2_550_000,
        2_025_000,
        450_000,
        75_000,
    )
    assert (p["heavy_envy"], p["q_l_half"]) == (200.0, 10.0)
    m = sol.phones_more()
    assert (m["open_menu"], m["heavy_only"], m["heavy_value_light_plan"]) == (
        1_800_000,
        1_350_000,
        487.5,
    )


def test_best_pooled_by_grid_search():
    # brute force: every break-even pooled contract (cover x on a fine grid, price
    # equal to the pooled probability), against the low risks' separating utility
    import numpy as np

    target = sol.rs_utilities()["low_sep"]
    xs = np.linspace(0.0, 50.0, 50001)

    def best_low(n_low):
        p_bar = 0.2 * n_low + 0.5 * (1 - n_low)
        u = 0.8 * np.log(100 - p_bar * xs) + 0.2 * np.log(50 + (1 - p_bar) * xs)
        return u.max(), xs[u.argmax()]

    shares = np.arange(0.800, 0.900, 0.0005)
    first = next(n for n in shares if best_low(n)[0] > target)
    assert abs(first - sol.pooled_threshold()) < 1e-3
    assert round(sol.pooled_threshold(), 3) == 0.838
    u9, x9 = best_low(0.9)
    b9 = sol.best_pooled(0.9)
    assert abs(x9 - b9["x"]) < 2e-3 and abs(u9 - b9["u_low"]) < 1e-9
    assert (round(b9["x"], 1), round(b9["u_low"], 3)) == (35.0, 4.486)
    bt = sol.best_pooled(sol.pooled_threshold())
    assert round(bt["x"], 1) == 27.2 and bt["u_high"] > np.log(
        75
    )  # high risks buy it too
