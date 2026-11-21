def test_ex08_cement_by_hand(run_exercise):
    out, _ = run_exercise("ex08_hhi")
    # 30^2 + 25^2 + 20^2 + 15^2 + 10^2 = 2,250; merging 15 and 10 adds 2 x 15 x 10 = 300
    assert "HHI  2250 ->  2550 (+ 300)" in out.splitlines()[0]
    assert out.count("presumed: yes") >= 1


def test_ex11_year_five(run_exercise):
    out, _ = run_exercise("ex11_cap")
    last = out.splitlines()[4]
    # 100 x 0.99^5 = 95.10 and 90 x 0.96^5 = 73.38
    assert "95.10" in last and "73.38" in last
