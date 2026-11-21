def test_ex12_recovers_effect(run_exercise):
    out, _ = run_exercise("ex12_licensing_did")
    did = float(out.splitlines()[1].split(":")[1].split()[0])
    assert -0.09 < did < -0.03
