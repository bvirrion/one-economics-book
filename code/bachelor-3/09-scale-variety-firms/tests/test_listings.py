def test_melitz_selection(run):
    out, _ = run("melitz_selection")
    lines = out.splitlines()
    assert "closed 2.000" in lines[0] and "open 2.099" in lines[0]
    assert "export 3.779" in lines[0]
    assert 0.12 < float(lines[2].split()[-1]) < 0.24
    assert 0.06 < float(lines[3].split()[-1]) < 0.13
