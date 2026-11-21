import numpy as np
from make_boom import tables as boom
from make_endow import tables as endow
from make_kpw import tables as kpw


def test_endow_shares():
    o, m = endow()
    assert len(o) == 12 and (o[["capital", "workers", "output"]] > 0).all().all()
    assert o.output.is_monotonic_increasing and o['rank'].iloc[0] == 1


def test_kpw():
    p, f, s = kpw()
    slope = s.set_index("stat").value["slope"]
    assert 0.3 < slope < 1.2 and len(p) > 100


def test_boom_hov_and_rybczynski():
    _, r = boom()
    v = dict(zip(r.item, r.value))
    assert np.isclose(v["autarky w"], 0.45) and np.isclose(v["autarky r"], 0.10)
    assert np.isclose(v["trade w"], 1) and np.isclose(v["trade r"], 1)
    for c in ["Kestria", "Brenland", "Kestria boom"]:
        if c != "Kestria boom":
            assert np.isclose(v[f"{c} F_K"], v[f"{c} HOV_K"])
            assert np.isclose(v[f"{c} F_L"], v[f"{c} HOV_L"])
    assert np.isclose(v["Kestria boom Q_T"], 9) and np.isclose(v["Kestria boom Q_M"], 22)
