"""A new bus line in Brenmoor (invented): a commuter survey for the weekend problem.

1,500 commuters choose car, bus or bicycle. Cost (dalens per trip) and door-to-door time
(minutes) vary by commuter and mode. Utility V = constant - 0.25 cost - 0.06 time, with
constants car 0.5, bus 0, bicycle -0.4, plus iid Gumbel taste shocks (so the true model is
a multinomial logit; value of time 0.06/0.25 x 60 = 14.4 dalens an hour). Seed 2026.
Estimation: (a) binary logit of car against bus among commuters who chose one of the two,
on the differences in cost and time; (b) three-way conditional logit (bus is the base);
both by Newton's method (inlined). Forecast: an express line with the bus fare and 10
minutes less than the bus, added to the estimated model.
Writes out/commuters_binary.csv, out/commuters_mnl.csv (term, est, se) and
out/commuters_shares.csv (mode, actual, fitted, forecast). Book 5, chapter 5, weekend problem.
"""
import numpy as np
import pandas as pd
from figout import write_table

MODES = ["car", "bus", "bicycle"]


def data():
    rng = np.random.default_rng(2026)
    n = 1500
    dist = rng.uniform(2, 15, n)                               # km
    cost = np.column_stack([1.0 + 0.35 * dist + rng.normal(0, 0.5, n),
                            np.full(n, 2.5), np.zeros(n)])
    time = np.column_stack([8 + 2.2 * dist + rng.normal(0, 4, n),
                            15 + 2.8 * dist + rng.normal(0, 5, n),
                            4.0 * dist + rng.normal(0, 3, n)])
    V = np.array([0.5, 0.0, -0.4]) - 0.25 * cost - 0.06 * time
    choice = (V + rng.gumbel(size=V.shape)).argmax(1)
    return cost, time, choice


def newton(loglik_parts, k):
    b = np.zeros(k)
    for _ in range(100):
        g, H = loglik_parts(b)
        step = np.linalg.solve(H, -g)
        b = b + step
        if np.max(np.abs(step)) < 1e-12:
            break
    g, H = loglik_parts(b)
    return b, np.sqrt(np.diag(np.linalg.inv(-H)))


def binary(cost, time, choice):
    keep = choice < 2
    y = (choice[keep] == 0).astype(float)                       # 1 = car
    X = np.column_stack([np.ones(keep.sum()), cost[keep, 0] - cost[keep, 1],
                         time[keep, 0] - time[keep, 1]])

    def parts(b):
        p = 1 / (1 + np.exp(-X @ b))
        return X.T @ (y - p), -(X.T * (p * (1 - p))) @ X
    return newton(parts, 3), keep.sum()


def mnl_X(cost, time, consts=3):
    n = len(cost)
    X = np.zeros((n, consts, 4))                 # constants car, bicycle; cost; time
    X[:, 0, 0] = 1
    X[:, 2, 1] = 1
    X[:, :, 2] = cost
    X[:, :, 3] = time
    return X


def mnl_prob(X, b):
    v = X @ b
    e = np.exp(v - v.max(1, keepdims=True))
    return e / e.sum(1, keepdims=True)


def mnl(cost, time, choice):
    X = mnl_X(cost, time)
    Y = np.eye(3)[choice]

    def parts(b):
        P = mnl_prob(X, b)
        xbar = np.einsum("nj,njk->nk", P, X)
        dev = X - xbar[:, None, :]
        g = np.einsum("nj,njk->k", Y, dev)
        H = -np.einsum("nj,njk,njl->kl", P, dev, dev)
        return g, H
    return newton(parts, 4), X


def tables():
    cost, time, choice = data()
    (bb, bse), nbin = binary(cost, time, choice)
    (mb, mse), X = mnl(cost, time, choice)
    binary_t = pd.DataFrame({"term": ["constant (car)", "cost difference",
                                      "time difference"], "est": bb, "se": bse})
    mnl_t = pd.DataFrame({"term": ["car constant", "bicycle constant", "cost", "time"],
                          "est": mb, "se": mse})
    P = mnl_prob(X, mb)
    # forecast: add an express line = bus fare, bus time - 10, bus constant (0)
    Xn = np.concatenate([X, X[:, [1], :]], axis=1)
    Xn[:, 3, 3] -= 10
    Pn = mnl_prob(Xn, mb)
    shares = pd.DataFrame({"mode": MODES + ["express"],
                           "actual": list(np.bincount(choice, minlength=3) / len(choice))
                           + [np.nan],
                           "fitted": list(P.mean(0)) + [np.nan],
                           "forecast": Pn.mean(0)})
    meta = pd.DataFrame({"stat": ["commuters", "car_or_bus"], "value": [len(choice), nbin]})
    return binary_t, mnl_t, shares, meta


if __name__ == "__main__":
    for t, n in zip(tables(), ["commuters_binary", "commuters_mnl", "commuters_shares",
                               "commuters_meta"]):
        write_table(t, __file__, n)
