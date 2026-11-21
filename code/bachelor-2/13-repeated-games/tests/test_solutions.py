"""The numbers the text and solutions of b2 ch. 13 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol13", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_repeated_pd():
    out = subprocess.run(
        [sys.executable, "repeated_pd.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "    always D       5.000       1.000       3.400       3.400" in out
    assert "    always D       5.000       1.000       1.400       1.400" in out
    assert (HERE / "outputs" / "repeated_pd.txt").read_text().endswith(out)


def test_thresholds():
    assert sol.grim_threshold(5, 3, 1) == 0.5
    assert r(sol.grim_threshold(6, 4, 1), 2) == 0.4
    assert r(sol.tft_threshold(5, 3, 0), 3) == 0.667
    assert r(sol.alternating_average(5, 0, 0.6), 3) == 3.125
    assert r(sol.bertrand_threshold(5), 2) == 0.8
    assert r(sol.bertrand_threshold(2, lag=3), 4) == 0.8409
    assert sol.max_lag(2, 0.95) == 12
    assert r(sol.bertrand_threshold(2, growth=1.2), 4) == 0.4167
    assert r(sol.survival_beta(0.9, 0.05), 3) == 0.857
    assert sol.max_firms(sol.survival_beta(0.9, 0.05)) == 7
    assert [r(x, 2) for x in sol.ebay_levels()] == [1.33, 0.76]


def test_cement():
    c = sol.cement()
    assert [r(x, 1) for x in c["cournot"]] == [53.3, 2844.4, 93.3]
    assert c["collude"] == (40.0, 3200.0)
    assert c["deviate"] == (60.0, 3600.0, 100.0, 2400.0)
    assert r(c["threshold"], 3) == 0.529 and r(c["deviation_stream"], 1) == 2995.6
    assert (r(c["lag1"], 2), r(c["lag2"], 3), c["max_lag"]) == (0.64, 0.512, 1)
    assert [r(x, 2) for x in c["price_lag2"]] == [119.07, 40.46]
    assert [r(x, 2) for x in c["price_lag3"]] == [113.68, 43.16]
    (qn, pn), (qc, pc), (qd, pd) = c["three"]
    assert (qn, pn) == (40.0, 1600.0)
    assert [r(x, 1) for x in (qc, pc, qd, pd)] == [26.7, 2133.3, 53.3, 2844.4]
    assert r(c["threshold3"], 3) == 0.571
