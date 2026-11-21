"""The numbers the solutions and the listing of b2 ch. 4 print, recomputed."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
ENV = {
    **os.environ,
    "PYTHONPATH": os.pathsep.join(
        str(ROOT / p) for p in ("code/shared", "figdata/lib")
    ),
}
spec = importlib.util.spec_from_file_location(
    "sol04", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_listing_puzzle():
    out = subprocess.run(
        [sys.executable, "puzzle.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
        env=ENV,
    ).stdout
    assert "gamma needed              312.1" in out and "corr = 1         25.1" in out
    assert (HERE / "outputs" / "puzzle.txt").read_text().endswith(out)


def test_one_star():
    q = sol.ex_state_prices()
    assert [round(x, 4) for x in q] == [0.4133, 0.5467]
    assert round(sol.ex_rf(), 4) == 1.0616


def test_two_star():
    c = sol.ex_capm()
    assert c["beta"] == 0.6 and round(c["er"], 3) == 0.046
    p = sol.ex_premium_size()
    assert round(p["g2"], 4) == 0.0032 and round(p["need"], 1) == 37.5
    g = sol.ex_geomean()
    assert (
        round(100 * g["USA"]["geo"], 2) == 6.66
        and round(100 * g["GBR"]["geo"], 2) == 4.88
    )
    assert round(100 * g["USA"]["arith"], 2) == 8.47 and g["USA"]["n"] == 121
    m = sol.ex_minvar()
    assert round(m["w1"], 3) == 0.2 and round(m["sd"], 4) == 0.0894


def test_three_star():
    s = sol.ex_gamma_needed()
    assert s.usa_gamma == 312.1 and s.usa_gamma_bound == 25.1
    assert round(sol.ex_gamble(), 3) == 0.177


def test_problem():
    p = sol.problem()
    assert [round(x, 4) for x in p["q"]] == [0.3762, 0.5762]
    assert round(p["rf"], 4) == 1.05 and round(p["er"], 4) == 1.1053
    assert round(p["call"], 2) == 11.29 and round(p["gamma"], 2) == 7.17
    assert round(p["beta"], 3) == 0.997 and abs(p["prem_cov"] - p["prem"]) < 1e-12
    assert round(p["w3"], 3) == 0.466 and round(p["g_6040"], 2) == 2.28
    assert round(p["w_min"], 4) == 0.0455 and round(p["sharpe_t"], 3) == 0.300
    assert [round(x, 4) for x in p["wt"]] == [0.4231, 0.5769]
    assert p["pred"].t == -1.19 and round(p["t_diff"], 2) == 0.24
    assert round(p["lev3"], 4) == 1.1145 and round(p["eq3_total"], 3) == 0.472
    assert round(p["sharpe60"], 3) == 0.295
