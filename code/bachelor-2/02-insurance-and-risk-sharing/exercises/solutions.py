"""The numbers printed in the solutions of Book 4, chapter 2 (risk sharing)."""

from math import exp, log, sqrt

from econdata import wdi

CONS, GDP = "NE.CON.PRVT.PC.KD.ZG", "NY.GDP.PCAP.KD.ZG"


def cover_log(z0, loss, mu, psi):
    """Best cover for u = ln: cover costs psi per unit, pays in the loss state."""
    c = (mu * (1 - psi) * z0 - (1 - mu) * psi * (z0 - loss)) / (psi * (1 - psi))
    return min(max(c, 0.0), loss)


def ex_contingent():
    z0, loss, mu, psi = 50_000, 20_000, 0.1, 0.12
    full = z0 - psi * loss
    return {
        "slope": -(1 - psi) / psi,
        "fair_slope": -(1 - mu) / mu,
        "full": full,
        "loading": psi / mu - 1,
    }


def ex_cover():
    z0, loss, mu = 50_000, 20_000, 0.1
    c12 = cover_log(z0, loss, mu, 0.12)
    c15 = cover_log(z0, loss, mu, 0.15)
    psi0 = mu * z0 / (mu * z0 + (1 - mu) * (z0 - loss))
    return {
        "c12": c12,
        "good12": z0 - 0.12 * c12,
        "bad12": z0 - loss + 0.88 * c12,
        "c15": c15,
        "psi0": psi0,
        "load0": psi0 / mu - 1,
    }


def ex_borch():
    a1, a2 = 0.0002, 0.0001
    share1 = a2 / (a1 + a2)
    k = 30_000 - share1 * 80_000
    z1 = [share1 * om + k for om in (100_000, 60_000)]
    return {"share1": share1, "k": k, "z1": z1, "z2": [100_000 - z1[0], 60_000 - z1[1]]}


def ex_six_countries():
    """Exercise 8: ratio of the standard deviations of the growth rates, 1991-2023."""
    out = {}
    for iso in ["USA", "JPN", "KOR", "FRA", "BRA", "IND"]:
        c = wdi(CONS, isos=[iso], since=1991, until=2023).dropna().value
        y = wdi(GDP, isos=[iso], since=1991, until=2023).dropna().value
        out[iso] = (round(y.std(), 2), round(c.std(), 2), round(c.std() / y.std(), 2))
    return out


def world_sd():
    c = wdi(CONS, isos=["WLD"], since=1991, until=2023).value
    return round(c.std(), 2)


def ex_pooling(n, loss=10_000, mu=0.1, a=0.0001):
    """Certainty-equivalent cost per household of n pooled independent losses (CARA)."""
    t = a * loss / n
    return n * log(1 - mu + mu * exp(t)) / a


def ex_portfolio(xi=0.05, sigma=0.18, gamma=3):
    return xi / (gamma * sigma**2)


# ---- weekend problem: two Kestrian boats (incomes in kests) ----
HI, LO = 30_000, 10_000
P = {"GG": 0.4, "GB": 0.2, "BG": 0.2, "BB": 0.2}


def problem():
    pg = P["GG"] + P["GB"]
    mean = pg * HI + (1 - pg) * LO
    var = pg * (1 - pg) * (HI - LO) ** 2
    cov = (HI - LO) ** 2 * (P["GG"] - pg**2)
    eu_alone = pg * log(HI) + (1 - pg) * log(LO)
    shared = {"GG": HI, "GB": (HI + LO) / 2, "BG": (HI + LO) / 2, "BB": LO}
    eu_sh = sum(P[s] * log(shared[s]) for s in P)
    var_sh = sum(P[s] * (shared[s] - mean) ** 2 for s in P)
    # CARA skippers with a1 = 2 a2: skipper 1 bears a2/(a1+a2) = 1/3 of aggregate risk
    om = {"GG": 2 * HI, "GB": HI + LO, "BG": HI + LO, "BB": 2 * LO}
    e_om = sum(P[s] * om[s] for s in P)
    k = mean - e_om / 3
    z1 = {s: om[s] / 3 + k for s in ("GG", "GB", "BB")}
    # outside insurer, own bad catch, loading 20 %
    mu, psi = 1 - pg, 1.2 * (1 - pg)
    c = cover_log(HI, HI - LO, mu, psi)
    good, bad = HI - psi * c, LO + (1 - psi) * c
    eu_ins = pg * log(good) + mu * log(bad)
    return {
        "pg": pg,
        "mean": mean,
        "sd": sqrt(var),
        "corr": cov / var,
        "eu_alone": eu_alone,
        "ce_alone": exp(eu_alone),
        "sd_agg": sqrt(var_sh),
        "sd_idio": sqrt(var - var_sh),
        "eu_shared": eu_sh,
        "ce_shared": exp(eu_sh),
        "gain": exp(eu_sh) - exp(eu_alone),
        "var_cut": 1 - var_sh / var,
        "k": k,
        "z1": z1,
        "psi": psi,
        "cover": c,
        "good": good,
        "bad": bad,
        "ce_ins": exp(eu_ins),
        "profit": (psi - mu) * c,
    }


def problem_bb_cover():
    """Question 17: the cooperative shares, then buys cover paid in state BB."""
    from scipy.optimize import brentq

    psi = 1.2 * P["BB"]

    def foc(c):
        return (
            0.2 * (1 - psi) / (LO + (1 - psi) * c)
            - 0.4 * psi / (HI - psi * c)
            - 0.4 * psi / ((HI + LO) / 2 - psi * c)
        )

    c = brentq(foc, 0, 20_000)
    eu = (
        0.4 * log(HI - psi * c)
        + 0.4 * log((HI + LO) / 2 - psi * c)
        + 0.2 * log(LO + (1 - psi) * c)
    )
    return {"psi": psi, "cover": c, "ce": exp(eu)}
