def test_ex07_four_lines_and_ordering(run_exercise):
    out, _ = run_exercise("ex07_transition")
    lines = out.splitlines()
    assert len(lines) == 4
    falls = [float(x.split("fall of")[1].split("%")[0]) for x in lines]
    # Ukraine's fall was the deepest, Czechia's the shallowest
    assert max(falls) == falls[3] and min(falls) == falls[1]
