"""Facts the charts of b1 ch. 31 show, and the coverage replication."""
import sys
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"
ROOT = Path(__file__).resolve().parents[3]


def test_noise():
    n = pd.read_csv(OUT / "noise.csv").set_index("geo")
    assert n.loc["EE", "sd_noise"] > 3 * n.loc["DE", "sd_noise"]


def test_coverage_replication():
    sys.path.insert(0, str(ROOT / "code/bachelor-1/31-sampling-and-inference/listings"))
    from coverage import intervals

    lo, hi, mu = intervals(reps=1_000, seed=11)
    assert 0.93 <= ((lo <= mu) & (hi >= mu)).mean() <= 0.97


def test_power():
    p = pd.read_csv(OUT / "power.csv")
    assert abs(p.n100.iloc[0] - 0.05) < 1e-3 and (p.n2000 >= p.n445).all()
