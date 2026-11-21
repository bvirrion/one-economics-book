from pathlib import Path

import numpy as np
import pandas as pd

FIG = Path(__file__).resolve().parents[4] / "figdata/bachelor-3/11-trade-policy/out"


def test_ex08_overhang(run_exercise):
    out, _ = run_exercise("ex08_overhang")
    lines = out.splitlines()
    n = int(lines[0].split()[1].rstrip(";"))
    # independent route: the chart's table (same sample before the income merge)
    chart = pd.read_csv(FIG / "bound.csv")
    assert 0.95 * len(chart) <= n <= len(chart)
    med = float(lines[0].split("overhang ")[1].split()[0])
    assert abs(med - chart.overhang.median()) < 2
    share = float(lines[1].split()[-1])
    assert abs(share - (chart.bound >= 2 * chart.applied).mean()) < 0.03
    assert float(lines[2].split()[-1]) < 0


def test_ex12_slope(run_exercise):
    out, _ = run_exercise("ex12_shift_share")
    lines = out.splitlines()
    e = [float(x.split("exposure ")[1].split(",")[0]) for x in lines[:5]]
    y = [float(x.split("change ")[1].split()[0]) for x in lines[:5]]
    # by hand: region A's exposure 0.30*8 + 0.10*3 + 0.05*1
    assert e[0] == 2.75
    slope = float(lines[5].split()[1])
    assert abs(slope - np.polyfit(e, y, 1)[0]) < 0.001
