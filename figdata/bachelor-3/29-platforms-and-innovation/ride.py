"""Brenmoor's ride platform (weekend problem). Part I: 10,000 residents, network value
10 theta n dalens a month, price 1.6. Part II: riders a = 4, alpha = 1.2; drivers a = 2,
alpha = 0.4; cost 1 per participant on each side (hundreds of participants, dalens).
Part IV: Brenland's services firms in the 2025 census (load("firms")); for 2027,
firms in the bottom tenth of output per worker exit, continuing firms raise output
per worker by 2 % and keep their workers, and 30 entrants each have the median
workforce and output per worker 10 % above the 2025 employment-weighted mean."""
import numpy as np
from country import load
from platform_model import fhk, rohlfs_equilibria, two_sided


def network():
    lo, hi = rohlfs_equilibria(1.6, 10.0)
    return {"low": lo, "high": hi, "pmax": 10.0 / 4}


def platform():
    n, p, profit = two_sided((4.0, 2.0), (1.2, 0.4), (1.0, 1.0))
    return {"n_r": n[0], "n_d": n[1], "p_r": p[0], "p_d": p[1], "profit": profit}


def panel():
    f = load("firms")
    s = f[f.sector == "services"].reset_index(drop=True)
    w0 = s.workers.to_numpy(float)
    p0 = s.output.to_numpy(float) / w0
    cut = np.quantile(p0, 0.1)
    status = np.where(p0 < cut, "x", "c")
    mean0 = (w0 * p0).sum() / w0.sum()
    w_new = np.full(30, float(np.median(w0)))
    p_new = np.full(30, 1.10 * mean0)
    w1 = np.concatenate([np.where(status == "c", w0, 0.0), w_new])
    p1 = np.concatenate([np.where(status == "c", 1.02 * p0, 0.0), p_new])
    p0a = np.concatenate([p0, np.zeros(30)])
    w0a = np.concatenate([w0, np.zeros(30)])
    st = np.concatenate([status, np.full(30, "n")])
    return p0a, w0a / w0a.sum(), p1, w1 / w1.sum(), st


def decomposition():
    d = fhk(*panel())
    d["change"] = d["P1"] - d["P0"]
    d["growth"] = 100 * d["change"] / d["P0"]
    d["net_entry_share"] = 100 * (d["entry"] + d["exit"]) / d["change"]
    d["exits"] = int((panel()[4] == "x").sum())
    return d
