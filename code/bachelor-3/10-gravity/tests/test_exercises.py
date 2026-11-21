from pathlib import Path

import numpy as np
import pandas as pd

FIG = Path(__file__).resolve().parents[4] / "figdata/bachelor-3/10-gravity/out"


def test_ex05_language_positive(run_exercise):
    out, _ = run_exercise("ex05_language")
    lines = out.splitlines()
    lang = float(lines[1].split("language ")[1])
    factor = float(lines[-1].split()[-1])
    # the factor is exp of the printed coefficient, and the language dummy takes
    # part of the colonial link (1.412 -> 0.945)
    assert abs(factor - np.exp(lang)) < 0.01 and lang > 0
    col = [float(x.split("colony ")[1].split(",")[0]) for x in lines[:2]]
    assert col[1] < col[0]


def test_ex10_trend_printed(run_exercise):
    out, _ = run_exercise("ex10_distance_puzzle")
    lines = out.splitlines()
    years = [int(x.split()[0]) for x in lines[:7]]
    elast = [float(x.split()[-1]) for x in lines[:7]]
    # independent route: the chart's own regressions, written by figdata
    ref = pd.read_csv(FIG / "distance_by_year.csv").set_index("year").ols
    assert np.allclose(elast, ref.loc[years].to_numpy(), atol=0.001)
    slope = np.polyfit(np.array(years) - 2008.0, ref.loc[years].to_numpy(), 1)[0]
    trend = float(lines[7].split("decade ")[1].split()[0])
    t = float(lines[7].split("t = ")[1])
    assert abs(trend - 10 * slope) < 0.001 and -2 < t < -1.5


def test_ex12_ols_biased_ppml_not(run_exercise):
    out, _ = run_exercise("ex12_ppml_vs_ols")
    first = out.splitlines()[0]
    ols = float(first.split("OLS on logs ")[1].split(",")[0])
    ppml = float(first.split("PPML ")[1])
    assert abs(ppml - 1) < 0.05 and abs(ols - 1) > 0.3
