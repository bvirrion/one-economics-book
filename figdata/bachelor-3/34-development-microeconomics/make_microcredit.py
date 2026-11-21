"""Opening chart: the general effect of expanding access to microcredit on six
household outcomes, pooled over seven randomized experiments by a Bayesian
hierarchical model (posterior mean and central 95 % interval, USD PPP per two weeks,
2010), with the general control-group mean (Meager 2016, Appendix A; cited table
src/meager.csv). Writes out/microcredit.csv (pos, tau, lo, hi, pct of the control
mean)."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "meager")
    for c in ("tau", "lo", "hi", "control"):
        d[c] = d[c].astype(float)
    d["pos"] = range(len(d), 0, -1)
    d["pct"] = 100 * d.tau / d.control
    d["el"] = d.tau - d.lo
    d["eh"] = d.hi - d.tau
    return d[["pos", "outcome", "tau", "lo", "hi", "el", "eh", "control", "pct"]]


if __name__ == "__main__":
    write_table(table(), __file__, "microcredit")
