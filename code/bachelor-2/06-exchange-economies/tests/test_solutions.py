"""The numbers the text and solutions of b2 ch. 6 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol06", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(x, n)


def test_listing_tatonnement():
    out = subprocess.run(
        [sys.executable, "tatonnement.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "start 1.01  ->  price 2.0000" in out
    assert "start 0.99  ->  price 0.5000" in out
    assert (HERE / "outputs" / "tatonnement.txt").read_text().endswith(out)


def test_text_example():
    t = sol.text_example()
    assert r(t["p"], 4) == 1.3571 and r(t["xa"][0], 3) == 4.737
    assert r(t["xa"][1], 3) == 6.429 and r(t["xb"][0], 3) == 5.263
    assert r(t["xb"][1], 3) == 3.571
    assert [r(x, 2) for x in t["core"]] == [3.26, 6.27]
    assert [r(x, 2) for x in t["core_x2"]] == [4.91, 7.70]
    assert t["mrs_w"] == (0.25, 8.0)


def test_three():
    t = sol.three()
    assert r(t["r"], 4) == 0.7717
    assert all(abs(z) < 1e-12 for z in t["z"].values())
    s = t["slope"]
    assert s[0.5] < 0 and s[1.0] > 0 and s[2.0] < 0


def test_exercises():
    f = sol.ex_feasible()
    assert f["i"][1] and not f["ii"][2] and f["iii"][2] and not f["iii"][1]
    assert sol.ex_mrs() == {"mrs_a": 1.5, "mrs_b": 4 / 12}
    e = sol.ex_cd_eq()
    assert e["p"] == 0.5 and e["xa"] == (5.0, 2.5) and e["xb"] == (5.0, 7.5)
    c = sol.ex_contract()
    assert [r(c[x], 3) for x in (2, 5, 8)] == [0.769, 2.5, 5.714]
    t = sol.ex_transfer()
    assert r(t["p1"], 4) == 0.5833 and r(t["dp"], 4) == r(t["formula"], 4) == 0.0833
    w = sol.ex_walras()
    assert (w["z1"], w["z2"], w["value"]) == (-3.0, 3.0, 0.0)


def test_problem():
    p = sol.problem()
    assert [r(x, 4) for x in p["mrs_w"]] == [0.1667, 1.5]
    assert p["trade"][0] > 0 and p["trade"][1] > 0
    assert [r(x, 2) for x in p["core"]] == [32.42, 42.25]
    assert r(p["p"], 4) == 0.6111
    assert [r(x, 2) for x in p["xa"]] == [38.18, 23.33]
    assert [r(x, 2) for x in p["xb"]] == [41.82, 76.67]
    assert [r(x, 2) for x in p["ev"]] == [4.85, 8.04]
    assert r(p["p2"], 4) == 0.6667 and p["xa2"] == (45.0, 30.0)
    assert [r(x, 6) for x in p["xb2"]] == [35.0, 70.0]
    assert p["u2"][0] > p["u"][0] and p["u2"][1] < p["u"][1]
    assert r(p["x2_check"], 6) == 30.0
