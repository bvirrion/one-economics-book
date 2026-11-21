import pytest
import numpy as np
from bank import income_floor, overnight, rule
from make_balance_sheets import table as cb
from make_inflation import peaks, table as infl


def test_corridor_bounds_and_floor():
    assert overnight(3.0, 10) == 3.5 and overnight(3.0, 100) == 2.5
    assert np.isclose(overnight(3.0, 40), 3.0)


def test_income_falls_with_rate_after_qe():
    assert income_floor(5.0) < income_floor(1.0)


def test_rule_at_target():
    assert np.isclose(rule(2.0), 3.0)


def test_balance_sheets_grew():
    t = cb().set_index("year")
    assert t.loc[2021, "fed"] > 3 * t.loc[2007, "fed"]


def test_inflation_peaks_2022():
    p = peaks(infl())
    assert (p.year == 2022).all()


def test_local_projection_recovers_a_known_response():
    """Simulate an economy with a known response to an i.i.d. rate shock and check
    that lp.irf recovers it (an independent check of the method)."""
    import pandas as pd
    from lp import add_lags, irf
    rng = np.random.default_rng(15)
    n, true = 4000, [0.0, -0.2, -0.4, -0.5, -0.5, -0.4]
    e = rng.normal(0, 1, n)
    dy = rng.normal(0, 0.5, n)
    for k in range(1, len(true)):          # growth responds to past shocks
        dy[k:] += (true[k] - true[k - 1]) * e[:-k]
    d = pd.DataFrame({"dy": dy, "dp": rng.normal(0, 0.3, n)})
    d["i"] = 0.5 * d.dy + 0.3 * d.dp + e   # the shock is the residual by design
    d["y"] = d.dy.cumsum()
    lags = add_lags(d)
    d = d.dropna().reset_index(drop=True)
    d["shock"] = e[4:]
    r = irf(d, lags, "y", H=5)
    assert np.allclose(r.b, true, atol=0.05)


def test_lp_output_falls_and_prices_fall_later():
    from make_lp import tables
    t, _ = tables()
    assert t.y.iloc[0] == pytest.approx(0, abs=1e-9)
    assert t.y.min() < 0 and t.p.iloc[16] < 0 and t.p.iloc[16] < t.p.iloc[4]


def test_lsap_events_all_negative():
    from make_lsap import table
    d = table()
    assert (d.events < 0).all() and d.set_index("asset").whole["10-year Treasury"] > 0
