"""Tests of the listings and exercises of b1 ch. 32.

The listings themselves are run (as the book prints them), and the numbers they
print are checked against values computed here independently with numpy, not
with the listings' statsmodels formulas.
"""

import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from econdata import nsw

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]


def load(name):
    spec = importlib.util.spec_from_file_location(
        name, HERE / "exercises" / f"{name}.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(path, tmp_path):
    """Run one file as a script, from a scratch directory, and return its stdout."""
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join(
        [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib"), str(path.parent)]
    )
    r = subprocess.run(
        [sys.executable, str(path)],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert r.returncode == 0, r.stderr
    assert "Traceback" not in r.stdout + r.stderr
    return r.stdout


def ols(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    b = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum()
    return b, y.mean() - b * x.mean()


def numbers(line):
    return [float(t.replace(",", "")) for t in re.findall(r"-?[\d,]*\.\d+|-?\d+", line)]


def test_every_listing_runs(tmp_path):
    for path in sorted((HERE / "listings").glob("*.py")):
        run(path, tmp_path)
    run(HERE / "exercises" / "exo_07.py", tmp_path)


def test_ols_statsmodels(tmp_path):
    out = run(HERE / "listings" / "ols_statsmodels.py", tmp_path)
    d = nsw("psid_controls").query("re78 > 0")
    x, y = d.education.to_numpy(float), np.log(d.re78.to_numpy())
    b, a = ols(x, y)
    u = y - a - b * x
    se = np.sqrt((u**2).sum() / (len(x) - 2) / ((x - x.mean()) ** 2).sum())
    r2 = 1 - (u**2).sum() / ((y - y.mean()) ** 2).sum()
    row = next(s for s in out.splitlines() if s.startswith("education"))
    coef, stderr = numbers(row)[:2]
    assert abs(coef - b) < 5e-5 and abs(stderr - se) < 5e-4
    assert f"R-squared {r2:.4f}; observations {len(x)}" in out


def test_reading_slopes(tmp_path):
    out = run(HERE / "listings" / "reading_slopes.py", tmp_path)
    d = nsw("psid_controls").query("re78 > 0 and education > 0")
    e, w = d.education.to_numpy(float), d.re78.to_numpy(float)
    expected = [
        ols(e, w)[0],
        ols(e, np.log(w))[0],
        ols(np.log(e), w)[0],
        ols(np.log(e), np.log(w))[0],
    ]
    # each line is f"{formula:34s} {slope:10.4f}  {reading}"
    printed = [float(s[35:45]) for s in out.splitlines()[:4]]
    for p, x in zip(printed, expected):
        assert abs(p - x) < 1e-3 * max(1, abs(x))


def test_cps_cap(tmp_path):
    out = run(HERE / "listings" / "cps_cap.py", tmp_path).splitlines()
    psid = nsw("psid_controls").query("re78 > 0")
    cps = nsw("cps_controls").query("re78 > 0")
    cap = nsw("cps_controls").re78.max()
    b_psid = ols(psid.education, np.log(psid.re78))[0]
    b_cps = ols(cps.education, np.log(cps.re78))[0]
    b_cap = ols(psid.education, np.log(np.minimum(psid.re78, cap)))[0]
    assert f"slope {b_psid:.4f}" in out[0] and f"slope {b_cps:.4f}" in out[1]
    assert f"slope {b_cap:.4f}" in out[2]
    assert round((cps.re78 == cps.re78.max()).mean(), 3) == 0.3
    assert b_cps < b_cap < b_psid


def test_exo_07(tmp_path):
    out = run(HERE / "exercises" / "exo_07.py", tmp_path)
    r = load("exo_07").result
    assert (
        r["n"] == 183 and abs(r["slope"] - 1.247) < 1e-3 and abs(r["se"] - 0.033) < 1e-3
    )
    assert "183" in out


def test_r2_and_toward_mean():
    d = nsw("psid_controls").query("re78 > 0")
    x, y = d.education.to_numpy(float), np.log(d.re78.to_numpy())
    b, a = ols(x, y)
    u = y - a - b * x
    r2 = 1 - (u**2).sum() / ((y - y.mean()) ** 2).sum()
    assert abs(np.corrcoef(x, y)[0, 1] ** 2 - r2) < 1e-12
    p = nsw("psid_controls")
    assert ols(p.re75, p.re78)[0] < 1


def test_problem():
    p = load("solutions").problem()
    assert abs(p["gap"] - p["bias_identity"]) < 1e-3 and p["short"] > p["long"]
    assert abs(p["long"] - 0.05) < 0.01
