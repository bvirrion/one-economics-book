"""The weekend problem's data: the dalen against the kest, 2000--2025.

The rate (dalens per kest) and Brenland's CPI and policy rate come from the country
tables. Kestria's CPI and interest rate are the problem's assumptions: Kestrian
prices rise by 2.0 % a year (2015 = 100) and its interest rate is 2.5 %. The real
rate is q = rate x P_K / P_B, indexed to 2015 = 100.
"""
import numpy as np
import pandas as pd
from country import load

K_INFL, K_RATE = 2.7, 3.0


def table():
    a = load("accounts")[["year", "cpi", "policy_rate"]]
    d = a.merge(load("trade")[["year", "rate"]], on="year")
    d["cpi_k"] = 100 * (1 + K_INFL / 100) ** (d.year - 2015)
    q = d.rate * d.cpi_k / d.cpi
    d["real"] = 100 * q / q[d.year == 2015].iloc[0]
    d["i_k"] = K_RATE
    return d.reset_index(drop=True)


def ar1(d):
    """OLS of log q_t on a constant and log q_{t-1}: (rho, half-life in years)."""
    lq = np.log(d.real.to_numpy())
    x, y = lq[:-1], lq[1:]
    rho = np.polyfit(x, y, 1)[0]
    return rho, np.log(0.5) / np.log(rho)


def forecasts(d, first=2016):
    """One-year-ahead forecasts of the rate made at t for t + 1, judged over
    first..2025: random walk; UIP (rate x (1 + i_B - i_K)); PPP reversion (the real
    rate closes the gap to its 2000--t mean at the AR(1) speed estimated on data up
    to t, plus the inflation differential)."""
    rows = []
    for t in range(first - 1, 2025):
        past = d[d.year <= t]
        now = past.iloc[-1]
        rho, _ = ar1(past)
        lq = np.log(past.real)
        gap = lq.iloc[-1] - lq.mean()
        nxt = d[d.year == t + 1].iloc[0]
        infl_gap = np.log(nxt.cpi / now.cpi) - np.log(nxt.cpi_k / now.cpi_k)
        rows.append({"year": t + 1, "actual": nxt.rate, "rw": now.rate,
                     "uip": now.rate * (1 + (now.policy_rate - now.i_k) / 100),
                     "ppp": now.rate * np.exp((rho - 1) * gap + infl_gap)})
    f = pd.DataFrame(rows)
    for m in ("rw", "uip", "ppp"):
        f[f"err_{m}"] = 100 * np.log(f[m] / f.actual)
    return f
