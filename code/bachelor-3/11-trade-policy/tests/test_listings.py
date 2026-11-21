def test_strategic_trade(run):
    out, _ = run("strategic_trade")
    lines = out.splitlines()
    # Cournot by hand: s* = (A - C)/4 = 2; welfare (A-C)^2/9 -> (A-C)^2/8
    assert "best s = +2.000" in lines[0]
    assert "7.111 -> 8.000" in lines[0]
    # Bertrand: the optimal policy is a tax; closed form s* = -5/14 on this demand
    s = float(lines[1].split("best s = ")[1].split(";")[0])
    assert s < 0 and abs(s + 5 / 14) < 0.001
    assert "Home sells 4.000, Foreign 2.000" in lines[2]
