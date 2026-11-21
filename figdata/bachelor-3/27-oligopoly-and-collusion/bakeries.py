"""Three bakeries in Brenmoor (weekend problem). Logit demand with alpha = 0.8 per
dalen, mean utilities 2.5, 2.5 and 2.1, marginal cost 2.0 dalens a loaf for all; a
market of 3,000 loaves a day. Bakeries 1 and 2 propose to merge. Two years later the
mean price in Brenmoor is 0.40 dalens above its pre-merger level, and in a comparison
town it has gone from 3.90 to 4.05."""
import numpy as np
from logit import equilibrium, shares, surplus, upp
from scipy.optimize import brentq

ALPHA, MARKET = 0.8, 3000.0
DELTA = np.array([2.5, 2.5, 2.1])
COST = np.array([2.0, 2.0, 2.0])
PRE, POST = [0, 1, 2], [0, 0, 2]


def outcome(owner, cost=COST):
    p = equilibrium(DELTA, cost, ALPHA, owner)
    return p, shares(p, DELTA, ALPHA)


def neutral_cost():
    """The marginal cost of the merged bakeries at which their prices stay at the
    pre-merger level."""
    p0, _ = outcome(PRE)

    def gap(c):
        p, _ = outcome(POST, np.array([c, c, 2.0]))
        return p[0] - p0[0]
    return brentq(gap, 0.0, 2.0)


def stats():
    p0, s0 = outcome(PRE)
    p1, s1 = outcome(POST)
    cs0, cs1 = surplus(p0, DELTA, ALPHA, MARKET), surplus(p1, DELTA, ALPHA, MARKET)
    cn = neutral_cost()
    pre_mean = float((p0 * s0).sum() / s0.sum())
    post_mean = float((p1 * s1).sum() / s1.sum())
    did = 0.40 - (4.05 - 3.90)
    return {"p1_pre": p0[0], "p3_pre": p0[2], "s1_pre": s0[0], "s3_pre": s0[2],
            "out_pre": 1 - s0.sum(), "p1_post": p1[0], "p3_post": p1[2],
            "s1_post": s1[0], "s3_post": s1[2], "out_post": 1 - s1.sum(),
            "rise1": p1[0] - p0[0], "rise3": p1[2] - p0[2], "cs_pre": cs0,
            "cs_post": cs1, "cs_loss": cs0 - cs1,
            "diversion": s0[1] / (1 - s0[0]), "margin2": p0[1] - COST[1],
            "upp": upp(p0, COST, s0, 0, 1),
            "e_star": upp(p0, COST, s0, 0, 1) / COST[0],
            "c_neutral": cn, "saving": 100 * (1 - cn / 2.0), "pre_mean": pre_mean,
            "post_mean": post_mean,
            "mean_rise": post_mean - pre_mean,
            "did": did,
            "profit1_pre": (p0[0] - COST[0]) * s0[0] * MARKET,
            "profit12_post": 2 * (p1[0] - COST[0]) * s1[0] * MARKET}
