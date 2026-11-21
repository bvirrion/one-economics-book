"""The numbers printed in the solutions of Book 4, chapter 1 (Expected Utility).

Each function returns the quantities one exercise or problem part prints; the
tests check them against the rounded values in the solutions file.
"""

from math import cosh, exp, log, sqrt

from scipy.optimize import brentq


def crra_ce(gamma, prizes, probs):
    """Certainty equivalent for u(x) = x**(1 - gamma) / (1 - gamma) (log at 1)."""
    scale = max(prizes)
    xs = [x / scale for x in prizes]
    if abs(gamma - 1) < 1e-12:
        return scale * exp(sum(p * log(x) for x, p in zip(xs, probs)))
    m = sum(p * x ** (1 - gamma) for x, p in zip(xs, probs))
    return scale * m ** (1 / (1 - gamma))


def cara_ce(a, prizes, probs):
    """Certainty equivalent for u(x) = -exp(-a x) / a."""
    lo = min(prizes)
    return lo - log(sum(p * exp(-a * (x - lo)) for x, p in zip(prizes, probs))) / a


def ex_rabin_gamma(w=100_000):
    """The example of section 5: the CRRA gamma that rejects lose 100 / gain 110."""
    g = brentq(lambda g: crra_ce(g, [w - 100, w + 110], [0.5, 0.5]) - w, 2, 500)
    # with gamma > 1 utility is bounded above: rejects lose L, gain anything, when
    # 0.5 * (1 - L/w) ** (1 - g) > 1, i.e. L > w * (1 - 2 ** (-1 / (g - 1)))
    lmax = w * (1 - 2 ** (-1 / (g - 1)))
    return {"gamma": g, "approx": w * 10 / 105**2, "loss_any_gain": lmax}


def ex_calibration(lose=100, gain=110):
    """Exercise 10: the factor per (lose + gain) dollars and the loss bound."""
    return {
        "factor": lose / gain,
        "step": lose + gain,
        "bound": (lose + gain) * gain / (gain - lose),
        "after_100_steps": (lose / gain) ** 100,
    }


def ex_small_risk(w=50_000, h=5_000, gamma=3):
    exact = w - crra_ce(gamma, [w - h, w + h], [0.5, 0.5])
    approx = 0.5 * gamma / w * h**2
    exact2 = 2 * w - crra_ce(gamma, [2 * w - h, 2 * w + h], [0.5, 0.5])
    return {"exact": exact, "approx": approx, "exact_rich": exact2}


def ex_cara(a=0.0005, h=1000):
    return {"premium": log(cosh(a * h)) / a, "approx": 0.5 * a * h**2}


def ex_dominance():
    f = {0: 0.2, 50: 0.3, 100: 0.5}
    h = {0: 0.1, 50: 0.6, 100: 0.3}
    out = {}
    for name, u in [("mean", lambda x: x), ("sqrt", sqrt)]:
        out[name] = (
            sum(p * u(x) for x, p in f.items()),
            sum(p * u(x) for x, p in h.items()),
        )
    return out


def deductible_a(extra_premium, d_low, d_high, mu):
    """CARA coefficient at which the low deductible is just worth its extra premium."""
    def f(a):
        low = exp(a * extra_premium) * (1 - mu + mu * exp(a * d_low))
        return low - (1 - mu + mu * exp(a * d_high))

    return brentq(f, 1e-9, 0.1)


def ex_deductible():
    """Exercise 9: 54 dollars a year buys a deductible of 1,000 instead of 2,000.

    The claim rate is 2 % a year.
    """
    a = deductible_a(54, 1000, 2000, 0.02)
    return {
        "expected_saving": 0.02 * 1000,
        "load": 54 / (0.02 * 1000),
        "a": a,
        "rra_200k": a * 200_000,
    }


def price_list_gamma(k):
    """Exercise 12: the CRRA gamma that makes row k (risky chance k/10) a tie."""
    p = k / 10

    def d(g):
        if abs(g - 1) < 1e-12:
            u = log
        else:

            def u(x):
                return x ** (1 - g) / (1 - g)

        return p * u(38) + (1 - p) * u(1) - (p * u(20) + (1 - p) * u(16))

    return brentq(d, -3, 0.999999) if k <= 8 else brentq(d, 1.000001, 10)


# ---- weekend problem: the farmer (prizes in dalens) ----
GOOD, BAD, P = 60_000, 20_000, 0.7


def problem():
    mean = P * GOOD + (1 - P) * BAD
    sd = sqrt(P * (1 - P)) * (GOOD - BAD)
    eu = P * log(GOOD) + (1 - P) * log(BAD)
    ce = exp(eu)
    approx = 0.5 / mean * sd**2
    ce_sqrt = (P * sqrt(GOOD) + (1 - P) * sqrt(BAD)) ** 2
    s_mean = P * 55_000 + (1 - P) * 30_000
    eu_s = P * log(55_000) + (1 - P) * log(30_000)
    g_tie = brentq(
        lambda g: (
            crra_ce(g, [GOOD, BAD], [P, 1 - P])
            - crra_ce(g, [55_000, 30_000], [P, 1 - P])
        ),
        0.01,
        0.99,
    )
    eu_half = P * log(57_500) + (1 - P) * log(25_000)
    fair = (1 - P) * (GOOD - BAD)
    pmax = GOOD - ce
    q = 0.36
    cover = (18_000 - 32_000 * q) / (q * (1 - q))
    q0 = 18_000 / 32_000
    a = brentq(
        lambda a: mean - cara_ce(a, [GOOD, BAD], [P, 1 - P]) - (mean - ce), 1e-7, 1e-3
    )
    ce_sav = exp(P * log(GOOD + 30_000) + (1 - P) * log(BAD + 30_000))
    return {
        "mean": mean,
        "sd": sd,
        "eu": eu,
        "ce": ce,
        "premium": mean - ce,
        "approx": approx,
        "ce_sqrt": ce_sqrt,
        "premium_sqrt": mean - ce_sqrt,
        "s_mean": s_mean,
        "eu_s": eu_s,
        "ce_s": exp(eu_s),
        "gamma_tie": g_tie,
        "eu_half": eu_half,
        "ce_half": exp(eu_half),
        "fair": fair,
        "pmax": pmax,
        "loading": pmax / fair - 1,
        "cover_036": cover,
        "q0": q0,
        "load0": q0 / 0.3 - 1,
        "a": a,
        "premium_sav": mean + 30_000 - ce_sav,
        "pmax_sav": GOOD + 30_000 - ce_sav,
        "loading_sav": (GOOD + 30_000 - ce_sav) / fair - 1,
    }
