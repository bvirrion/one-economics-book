"""Worked numbers for the text, exercises and problem of Book 4, chapter 19."""

from math import log


def life_cycle(work=40, retire=20, income=30.0, wealth=0.0):
    c = (wealth + work * income) / (work + retire)
    return {"c": c, "saving": income - c, "peak": wealth + work * (income - c)}


def precautionary(y1=100.0, y2=(50.0, 150.0), lo=0.0, hi=50.0):
    """Saving s maximising ln(y1 - s) + mean ln(y2_i + s), r = 0, beta = 1."""

    def du(s):
        return -1 / (y1 - s) + sum(1 / (y + s) for y in y2) / len(y2)

    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if du(mid) > 0 else (lo, mid)
    s = (lo + hi) / 2
    return s, log(y1 - s) + sum(log(y + s) for y in y2) / len(y2)


def prudence_gap(c=(50.0, 150.0)):
    """Mean of 1/c against 1/mean(c)."""
    mean_mu = sum(1 / x for x in c) / len(c)
    return mean_mu, 1 / (sum(c) / len(c))


def hand_to_mouth(mpc, mpc_pih):
    """Share h solving mpc = h + (1 - h) mpc_pih."""
    return (mpc - mpc_pih) / (1 - mpc_pih)


def constrained(y=(20.0, 40.0), bonus=0.0):
    """Two periods, r = 0, no borrowing: first-period consumption."""
    want = (y[0] + y[1] + bonus) / 2
    return min(want, y[0] + bonus)


def household():
    years, work, income, wealth = 50, 25, 30.0, 250.0
    res = wealth + work * income
    c = res / years
    return {
        "resources": res,
        "c": c,
        "saving": income - c,
        "wealth_retire": wealth + work * (income - c),
        "bonus_dc": 10 / years,
        "raise_work_dc": 2 * work / years,
        "raise_life_dc": 2 * years / years,
        "quarterly_mpc": 1 / (4 * years),
    }


def population(n=2000, payment=600.0, mpc=0.30):
    q = household()["quarterly_mpc"]
    h = hand_to_mouth(mpc, q)
    return {
        "q": q,
        "h": h,
        "spent": n * payment * mpc,
        "h_low": hand_to_mouth(0.20, q),
        "h_high": hand_to_mouth(0.40, q),
        "mpc_half": 0.5 + 0.5 * q,
    }


def lambda_iv(use_consumption_lags=True):
    """The listing's estimate, optionally with lagged income growth only."""
    import numpy as np
    from statsmodels.datasets import macrodata

    d = macrodata.load_pandas().data
    dc = 100 * np.diff(np.log(d.realcons.to_numpy()))
    dy = 100 * np.diff(np.log(d.realdpi.to_numpy()))
    t = np.arange(4, len(dc))
    series = (dy, dc) if use_consumption_lags else (dy,)
    lags = [x[t - k] for x in series for k in (2, 3, 4)]
    z = np.column_stack([np.ones(len(t))] + lags)
    fitted = z @ np.linalg.lstsq(z, dy[t], rcond=None)[0]
    r2 = 1 - np.var(dy[t] - fitted) / np.var(dy[t])
    k = len(lags)
    f_stat = (r2 / k) / ((1 - r2) / (len(t) - k - 1))
    x_hat = np.column_stack([np.ones(len(t)), fitted])
    b = np.linalg.lstsq(x_hat, dc[t], rcond=None)[0]
    resid = dc[t] - np.column_stack([np.ones(len(t)), dy[t]]) @ b
    var = resid @ resid / (len(t) - 2) * np.linalg.inv(x_hat.T @ x_hat)[1, 1]
    return {"lambda": b[1], "se": var**0.5, "r2": r2, "f": f_stat}
