"""The numbers the solutions of b2 ch. 5 print, recomputed."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
ENV = {**os.environ, "PYTHONPATH": f"{ROOT / 'code/shared'}:{ROOT / 'figdata/lib'}"}
spec = importlib.util.spec_from_file_location(
    "sol05", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_listing_winners_curse():
    out = subprocess.run(
        [sys.executable, "winners_curse.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
        env=ENV,
    ).stdout
    assert "mean published estimate     0.262" in out
    assert "relative effect size        0.568" in out
    assert (HERE / "outputs" / "winners_curse.txt").read_text().endswith(out)


def test_one_star():
    r = sol.ex_replication()
    assert (r["below"], r["negative"]) == (15, 3)
    assert round(r["mean_orig"], 3) == 0.472 and round(r["mean_rep"], 3) == 0.277
    assert sol.ex_mixed() == {"v150": -25.0, "min_g": 200.0}
    assert sol.ex_endowment() == {"wta": 10.0, "wtp_goods": 5.0, "wtp_both": 2.5}


def test_two_star():
    p = sol.ex_prospect()
    assert round(p["g"], 1) == 501.2 and round(p["l"], 1) == 219.7
    assert round(p["v"], 1) == 30.9
    d = sol.ex_default()
    assert (d["in"], d["out"], d["extra"], d["at_default"]) == (740, 1720, 980, 1220)
    s = sol.ex_salience()
    assert s["posted"] == 720 and round(s["theta"], 3) == 0.217


def test_three_star():
    f = sol.ex_fourfold()
    assert round(f["w"][0.01], 3) == 0.047 and round(f["w"][0.99], 3) == 0.930
    assert round(f["gain_low"], 1) == 46.9 and round(f["gain_high"], 1) == 930.3
    e = sol.ex_eu_endowment()
    assert round(e["ratio"], 5) == 1.00017
    lab = sol.ex_labour()
    assert lab["lo"] == 20 and round(lab["hi"], 2) == 28.28
    assert [round(h, 2) for h in lab["hours"].values()] == [8, 10, 8, 7.14, 8]


def test_problem():
    p = sol.problem()
    assert round(p["lam_curv"], 3) == 1.866 and p["rabin"] == 1125
    assert round(p["k_goods"], 2) == 2.29 and round(p["k_both"], 2) == 1.51
    assert round(p["chi"], 4) == 0.7061 and round(p["mu"], 4) == 0.3742
    assert round(p["mu_b"], 4) == 0.5804 and round(100 * p["p_out"], 1) == 90.1
    assert round(p["contrib_out"], 2) == 3.58 and p["contrib_in"] == 2.7
    assert (
        round(100 * p["worse_out"], 1) == 18.2 and round(100 * p["miss_in"], 1) == 26.9
    )
    assert round(p["w05"], 4) == 0.1215 and round(p["k_needed"], 2) == 1.65
    assert round(100 * p["share_low"], 1) == 71.1


def test_text():
    assert round(sol.crossing(), 2) == 0.36
    a = sol.allais()
    assert round(a["w80"], 3) == 0.640 and round(a["w20"], 3) == 0.260
    assert round(a["w25"], 3) == 0.293
    assert a["B"] > a["A"] and a["C"] > a["D"]
    assert [round(a[k]) for k in "ABCD"] == [1117, 1347, 454, 395]
