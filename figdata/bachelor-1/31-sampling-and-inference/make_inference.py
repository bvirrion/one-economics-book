"""Charts of b1 ch. 31.

unemp: Eurostat une_rt_q, unemployment rate, ages 15-74, both sexes, per cent of the labour
force, seasonally adjusted (SA) and trend-cycle (TC), Germany and Estonia, 2010-Q1 to the
last quarter with both series. noise: sd of SA - TC and mean absolute quarterly change.
coverage: the 100 intervals of listing coverage.py (seed 2026, n = 30, PSID 1978 earnings);
coverage_stats: the share of 20,000 such intervals (same seed) that contain the mean.
power: power of a two-sided 5% test of a difference in means against the effect, with the
NSW control group's standard deviation and n/2 per arm, n = 100, 445 and 2,000 (formula).
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from econdata import eurostat, nsw
from figout import write_table
from scipy import stats

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "code/bachelor-1/31-sampling-and-inference/listings"))
from coverage import intervals  # noqa: E402

e = eurostat("une_rt_q")
e = e[(e.age == "Y15-74") & (e.sex == "T") & (e.unit == "PC_ACT") & (e.time >= "2010")]
e = e[e.geo.isin(["DE", "EE"])].pivot_table(index="time", columns=["geo", "s_adj"], values="value")
e = e.dropna()
e.columns = [f"{g}_{s}" for g, s in e.columns]
e = e[[c for c in e.columns if not c.endswith("NSA")]]
e["t"] = [int(q[:4]) + (int(q[-1]) - 1) / 4 for q in e.index]
write_table(e.reset_index().round(2), __file__, "unemp")
rows = []
for g in ("DE", "EE"):
    rows.append({"geo": g, "first": e.index[0], "last": e.index[-1],
                 "sd_noise": round((e[f"{g}_SA"] - e[f"{g}_TC"]).std(), 3),
                 "mean_abs_change": round(e[f"{g}_SA"].diff().abs().mean(), 3)})
write_table(pd.DataFrame(rows), __file__, "noise")

lo, hi, mu = intervals()
miss = ((lo > mu) | (hi < mu)).astype(int)
cov = pd.DataFrame({"k": np.arange(1, 101), "lo": lo.round(0), "hi": hi.round(0), "miss": miss})
write_table(cov[cov.miss == 0], __file__, "cover_hit")
write_table(cov[cov.miss == 1], __file__, "cover_miss")
lo2, hi2, _ = intervals(reps=20_000)
write_table(pd.DataFrame([{"reps": 20_000, "covered": round(((lo2 <= mu) & (hi2 >= mu)).mean(), 4)}]),
            __file__, "coverage_stats")

sd = nsw("nsw_dw").query("treat == 0").re78.std()
eff = np.arange(0, 4001, 50)
pw = {"effect": eff}
for n in (100, 445, 2000):
    se = sd * np.sqrt(4 / n)
    pw[f"n{n}"] = (stats.norm.sf(1.96 - eff / se) + stats.norm.cdf(-1.96 - eff / se)).round(4)
write_table(pd.DataFrame(pw), __file__, "power")
