"""Opening chart (simulated): what a significance filter does to the published record.

6,000 simulated studies; each has its own true effect (exponential, mean 0.1) and its own
size (log-uniform from 25 to 2,000 per arm, s.e. sqrt(2/n)). Every study with |z| > 1.96
is published; the others one time in four. Histograms of |z| in bins of 0.245 (1.96 / 8,
so that 1.96 is an edge) from 0 to 5.88,
for all studies and for the published ones, as counts. Seed 1996.
Writes out/filter_hist.csv (z, all, published) and out/filter_meta.csv.
"""
import numpy as np
import pandas as pd
from figout import write_table

EDGES = np.arange(25) * 0.245


def simulate():
    rng = np.random.default_rng(1996)
    k = 6000
    beta = rng.exponential(0.1, k)
    n = np.exp(rng.uniform(np.log(25), np.log(2000), k))
    se = np.sqrt(2 / n)
    z = np.abs(rng.normal(beta, se) / se)
    pub = (z > 1.96) | (rng.uniform(size=k) < 0.25)
    return z, pub


def tables():
    z, pub = simulate()
    a = np.histogram(z, EDGES)[0]
    p = np.histogram(z[pub], EDGES)[0]
    hist = pd.DataFrame({"z": EDGES[:-1] + 0.1225, "all": a, "published": p})
    meta = pd.DataFrame({"stat": ["studies", "published", "share_sig_all", "share_sig_pub"],
                         "value": [len(z), pub.sum(), (z > 1.96).mean(),
                                   (z[pub] > 1.96).mean()]})
    return hist, meta


if __name__ == "__main__":
    h, m = tables()
    write_table(h, __file__, "filter_hist")
    write_table(m, __file__, "filter_meta")
