"""The numbers the text and solutions of b2 ch. 20 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol20", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_wait():
    out = subprocess.run(
        [sys.executable, "wait.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "break-even profit (net present value zero): 9.09" in out
    for u, x in (("0.00", "9.09"), ("0.25", "11.48"), ("0.50", "15.58")):
        assert f"u = {u}: invest at once if profit is at least {x}" in out
    assert "u = 0.75: invest at once if profit is at least 24.24" in out
    assert "at x0 = 12, u = 0.5: now 32.00, wait 44.55" in out
    assert (HERE / "outputs" / "wait.txt").read_text().endswith(out)


def test_text_and_exercises():
    assert r(sol.user_cost(1, 0.05, 0.10), 2) == 0.15
    assert r(sol.desired_capital(0.3, 1000, 0.15), 1) == 2000.0
    assert r(sol.desired_capital(0.3, 1000, 0.17), 1) == 1764.7
    assert r(sol.user_cost(200, 0.04, 0.06, 0.01), 2) == 18.0
    assert r(sol.q_investment(1.3), 3) == 0.11
    assert (r(sol.now(10), 2), r(sol.wait(10, 0.5), 2)) == (10.0, 29.55)
    assert (r(sol.now(10), 2), r(sol.wait(10, 0.25), 2)) == (10.0, 17.05)
    for u, x in ((0.0, 9.09), (0.25, 11.48), (0.5, 15.58), (0.75, 24.24)):
        assert r(sol.trigger(u), 2) == x
    g = sol.grunfeld()
    assert [r(v, 3) for v in g["fe"]] == [0.11, 0.31]
    assert [r(v, 3) for v in g["fe_se"]] == [0.011, 0.017]
    assert [r(v, 3) for v in g["pooled"]] == [0.115, 0.228]
    assert (r(g["fe_r2"], 2), r(g["pooled_r2"], 2)) == (0.95, 0.82)


def test_terminal():
    t = sol.terminal()
    assert (r(t["uc"], 2), r(t["k"], 2)) == (6.0, 14.0)
    assert (r(t["uc_r8"], 2), r(t["uc_noinf"], 2), r(t["uc_sub"], 2)) == (
        7.0,
        7.0,
        5.4,
    )
    assert (t["q_avg"], r(t["ik"], 3), r(t["ik_q1"], 3), r(t["ik_q08"], 3)) == (
        1.8,
        0.16,
        0.08,
        0.06,
    )
    assert (r(t["now"], 2), r(t["wait"], 2), r(t["wait_25"], 2)) == (
        32.0,
        44.55,
        29.55,
    )
    assert (r(t["trig"], 2), r(t["trig75"], 2), r(t["breakeven"], 2)) == (
        15.58,
        24.24,
        9.09,
    )
