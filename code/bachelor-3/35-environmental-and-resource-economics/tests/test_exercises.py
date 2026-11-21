

def test_ex07_three_peaks(run_exercise):
    out, _ = run_exercise("ex07_so2_peaks")
    assert len(out.splitlines()) == 3


def test_ex12_against_closed_form(run_exercise):
    out, _ = run_exercise("ex12_scc")
    # geometric series: 1.5 / (1 + r) * (1 - q^300) / (1 - q), q = 1.02 / (1 + r)
    r = 0.03
    q = 1.02 / (1 + r)
    pv = 1.5 / (1 + r) * (1 - q**300) / (1 - q)
    assert f"constant 3.0 %: {pv:7.1f}" in out
