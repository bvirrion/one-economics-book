import re

import numpy as np
from econdata import nsw


def _sample():
    d = nsw("cps_controls")
    d = d[d.re78 > 0].copy()
    d["lw"] = np.log(d.re78)
    d["exp"] = (d.age - d.education - 6).clip(lower=0)
    return d


def test_ex05_coefficients_match_least_squares(run_exercise):
    out, _ = run_exercise("ex05_mincer")
    lines = out.splitlines()
    assert len(lines) == 2
    d = _sample()
    base = [np.ones(len(d)), d.education, d.exp, d.exp**2]
    for line, extra in zip(lines, ([], [d.black, d.hispanic, d.married])):
        n, b, prem = re.match(r"(\d+) men: schooling ([\d.]+) .*premium ([\d.]+) %", line).groups()
        X = np.column_stack(base + list(extra))
        beta = np.linalg.lstsq(X, d.lw.to_numpy(), rcond=None)[0]
        assert int(n) == len(d) and abs(beta[1] - float(b)) < 6e-5
        assert abs(100 * (np.exp(float(b)) - 1) - float(prem)) < 0.06
    assert float(re.search(r"schooling ([\d.]+)", lines[1]).group(1)) < float(
        re.search(r"schooling ([\d.]+)", lines[0]).group(1))


def test_ex11_peaks_match_quadratic_fits(run_exercise):
    out, _ = run_exercise("ex11_profiles")
    lines = out.splitlines()
    assert len(lines) == 4
    d = _sample()
    masks = [d.education < 12, d.education == 12, d.education.between(13, 15),
             d.education >= 16]
    for line, m in zip(lines, masks):
        n, peak = re.search(r": (\d+) men, peak at age ([\d.]+)", line).groups()
        c2, c1, _ = np.polyfit(d.age[m], d.lw[m], 2)
        assert int(n) == m.sum() and abs(-c1 / (2 * c2) - float(peak)) < 0.06
