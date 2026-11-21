"""The numbers the text and solutions of b2 ch. 23 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol23", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_ramsey():
    out = subprocess.run(
        [sys.executable, "ramsey.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "steady state: k* = 8.505, saving rate 0.250" in out
    assert "theta 2: saving rate 0.343, 0.294 after 10 years," in out
    assert "0.257 after 40; capital gap halved after 13 years" in out
    assert "theta 6: saving rate 0.209, 0.221 after 10 years," in out
    assert "0.240 after 40; capital gap halved after 27 years" in out
    assert (HERE / "outputs" / "ramsey.txt").read_text().endswith(out)


def test_text_and_exercises():
    st = sol.steady(1 / 3, 0.05, 0.03, 0.01)
    assert [r(st[k], 3) for k in ("k", "y", "c", "s")] == [8.505, 2.041, 1.531, 0.25]
    assert r(sol.golden(1 / 3, 0.05, 0.01), 2) == 13.09
    e = sol.eigen(1 / 3, 0.05, 0.03, 0.01, 2)
    assert [r(e[k], 4) for k in ("a", "b", "pos", "neg")] == [
        0.02,
        -0.0048,
        0.08,
        -0.06,
    ]
    assert r(e["half"], 1) == 11.6
    assert r(sol.eigen(1 / 3, 0.05, 0.03, 0.01, 6)["half"], 1) == 22.2
    hi = sol.steady(1 / 3, 0.05, 0.04, 0.01)
    assert (r(hi["k"], 3), r(hi["c"], 3), r(hi["s"], 3)) == (7.128, 1.497, 0.222)
    assert r(sol.euler_growth(0.05, 0.03, 2), 3) == 0.01


def test_kestria():
    k = sol.kestria()
    assert [r(k[x], 3) for x in ("k", "y", "c", "s", "wage")] == [
        4.804,
        1.601,
        1.313,
        0.18,
        1.121,
    ]
    assert (r(k["kg"], 2), r(k["r"], 3)) == (9.97, 0.04)
    assert [r(k[x], 4) for x in ("e_a", "e_b", "e_pos", "e_neg")] == [
        0.04,
        -0.0096,
        0.1198,
        -0.0798,
    ]
    assert (r(k["e_half"], 1), r(k["half_theta4"], 1)) == (8.7, 13.3)
    assert r(k["c_after_g"], 3) == 1.213


def test_initial_saving():
    assert r(sol.initial_saving(0.3, 0.06, 0.04, 0.0, 2), 3) == 0.303
    assert r(sol.initial_saving(1 / 3, 0.05, 0.03, 0.01, 2), 3) == 0.343
