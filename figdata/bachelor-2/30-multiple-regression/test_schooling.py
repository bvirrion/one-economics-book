"""Checks the statsmodels coefficients with numpy least squares (a second method)."""

import numpy as np
from make_schooling import CONTROLS, sample, sample_summary, steps


def test_steps_against_lstsq():
    d = sample()
    s = steps().set_index("step")
    for k in range(len(CONTROLS) + 1):
        x = np.column_stack(
            [np.ones(len(d)), d.education] + [d[c] for c in CONTROLS[:k]]
        )
        b = np.linalg.lstsq(x, d.lre78.to_numpy(), rcond=None)[0]
        assert round(100 * b[1], 2) == s.loc[k, "b"]
    assert (s.loc[0, "b"], s.loc[1, "b"], s.loc[6, "b"]) == (4.10, 5.22, 2.04)


def test_sample():
    r = sample_summary().iloc[0]
    assert (r.n, r.share_capped, r.cap) == (13055, 0.259, 25564.7)
