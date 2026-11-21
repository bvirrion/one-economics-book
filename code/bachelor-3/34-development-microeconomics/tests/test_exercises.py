import numpy as np


def test_ex05_measures_rise_with_the_line(run_exercise):
    out, _ = run_exercise("ex05_fgt_kenya")
    heads = [float(x.split("headcount")[1].split("%")[0]) for x in out.splitlines()]
    assert heads == sorted(heads) and len(heads) == 3


def test_ex11_against_a_direct_computation(run_exercise):
    out, _ = run_exercise("ex11_heterogeneity")
    # fixed effect computed here independently, with weights 1 / se^2
    e = np.array([12, 3, 25, -4, 8, 15, 1.0])
    s = np.array([5, 4, 9, 6, 3, 7, 4.0])
    fe = np.average(e, weights=s**-2)
    assert f"fixed effect {fe:.2f}" in out
