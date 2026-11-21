"""Tests of the listings of b1 ch. 28."""

import hashlib
import os
import subprocess
import sys
from pathlib import Path

import numpy as np

LST = Path(__file__).resolve().parents[1] / "listings"
sys.path.insert(0, str(LST))
from cpi_tools import monthly  # noqa: E402
from seasonal_by_hand import adjust  # noqa: E402


def test_seasonal():
    nsa = monthly("CUUR0000SA0")
    f, adj = adjust(nsa)
    assert abs(f.mean() - 1) < 1e-12
    sa = monthly("CUSR0000SA0")
    c = np.corrcoef(adj.pct_change().loc[2015:2024], sa.pct_change().loc[2015:2024])[
        0, 1
    ]
    assert c > 0.9


def test_changes():
    cpi = monthly("CUUR0000SA0")
    yoy = 100 * (cpi / cpi.shift(12) - 1)
    assert 8.9 < yoy.loc[(2022, 6)] < 9.2


def test_join_and_deflate():
    from country import load
    from econdata import pwt, wdi

    w = wdi("NY.GDP.PCAP.PP.KD", since=2019, until=2019)
    p = pwt(since=2019, until=2019, cols=["rgdpe"])
    m = w.merge(p, on=["iso3", "year"], how="outer", indicator=True)
    assert (m["_merge"] != "both").sum() > 0
    a = load("accounts").set_index("year")
    real = a.gdp / a.deflator * 100
    assert abs(real.loc[2015] - a.gdp.loc[2015]) < 1


def test_reproducible(tmp_path):
    root = LST.parents[3]
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join(
        str(root / p) for p in ("code/shared", "figdata/lib")
    )
    digests = []
    for _ in range(2):
        subprocess.run(
            [sys.executable, str(LST / "write_chart_table.py")],
            cwd=tmp_path,
            check=True,
            capture_output=True,
            env=env,
        )
        digests.append(
            hashlib.sha256((tmp_path / "chart.csv").read_bytes()).hexdigest()
        )
    assert digests[0] == digests[1]
