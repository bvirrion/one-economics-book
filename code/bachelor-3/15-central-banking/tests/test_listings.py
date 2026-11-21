from pathlib import Path

import pandas as pd

FIG = Path(__file__).resolve().parents[4] / "figdata/bachelor-3/15-central-banking/out"


def test_local_projection(run):
    out, _ = run("local_projection")
    lines = out.splitlines()
    assert lines[0].startswith("quarters 191")
    # the chart's estimates come from figdata/lp.py, tested on simulated data
    ref = pd.read_csv(FIG / "lp.csv").set_index("h")
    for line in lines[1:]:
        h = int(line.split("=")[1].split(":")[0])
        y = float(line.split("output ")[1].split()[0])
        p = float(line.split("prices ")[1].split()[0])
        assert abs(y - ref.y[h]) < 0.006 and abs(p - ref.p[h]) < 0.006
