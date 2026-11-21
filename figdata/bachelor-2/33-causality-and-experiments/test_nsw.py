"""Group means by a plain loop over the rows, against the script."""

import math

from econdata import nsw
from make_nsw import means


def test_means_by_loop():
    d = nsw("nsw_dw")
    m = means().set_index("group")
    for g in (0, 1):
        x = [v for v, t in zip(d.re78, d.treat) if t == g]
        mu = sum(x) / len(x)
        sd = math.sqrt(sum((v - mu) ** 2 for v in x) / (len(x) - 1))
        assert m.loc[g, "n"] == len(x)
        assert m.loc[g, "mean"] == round(mu)
        assert m.loc[g, "hi"] == round(mu + 1.96 * sd / math.sqrt(len(x)))
    assert (m.loc[1, "mean"], m.loc[0, "mean"], m.loc[1, "n"], m.loc[0, "n"]) == (
        6349,
        4555,
        185,
        260,
    )
