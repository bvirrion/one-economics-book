"""Second routes: t from the correlation, the ACF by hand, inflation by pandas."""

import numpy as np
from econdata import sm_dataset
from make_ts import acf_table, forecasts, rmse, walks, walks_fit


def test_walks_t_from_correlation():
    w = walks()
    r = np.corrcoef(w.a, w.b)[0, 1]
    t = r * np.sqrt((len(w) - 2) / (1 - r**2))
    f = walks_fit().iloc[0]
    assert (f.r2, f.t) == (round(r**2, 3), round(t, 2)) == (0.548, -15.5)


def test_acf_by_hand():
    d = sm_dataset("macrodata")
    for col in ("infl", "unemp"):
        x = d[col].to_numpy() - d[col].mean()
        r1 = (x[1:] @ x[:-1]) / (x @ x)
        assert round(r1, 3) == acf_table().set_index("lag").loc[1, col]
    assert tuple(acf_table().iloc[0, 1:]) == (0.642, 0.956)


def test_rmse_and_last_forecast():
    f = forecasts()
    assert len(f) == 95 and f.t.iloc[0] == 1986 and f.t.iloc[-1] == 2009.5
    d = sm_dataset("macrodata")
    pi4 = 100 * np.log(d.cpi).diff(4)
    assert round(pi4.iloc[-1], 3) == f.actual.iloc[-1] == -0.233
    assert round(pi4.iloc[-5], 3) == f.rw.iloc[-1]
    r = rmse().set_index("model").rmse
    assert (r["ar"], r["rw"]) == (1.772, 1.624)
