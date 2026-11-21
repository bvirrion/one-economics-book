def test_ex08_positive_rnd(run_exercise):
    out, _ = run_exercise("ex08_rnd_patents")
    coefs = [float(line.split("coefficient")[1].split(",")[0]) for line in
             out.splitlines()]
    assert coefs[0] > 0 and len(coefs) == 2


def test_ex12_parts_add_up(run_exercise):
    out, _ = run_exercise("ex12_fhk")
    first, second = out.splitlines()
    change = float(first.split("change")[1].split()[0])
    parts = [float(x.split()[-1]) for x in second.split(",")]
    assert abs(sum(parts) - change) < 0.02
