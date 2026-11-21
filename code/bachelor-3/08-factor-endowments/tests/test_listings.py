def test_leontief_leamer(run):
    out, _ = run("leontief_leamer")
    vals = [float(x.split(":")[1].split()[0]) for x in out.splitlines()
            if x.startswith("capital per worker")]
    exp_x, imp_x, prod, cons, world = vals
    # by hand: exports (60 machines, 10 furniture) embody 260 K and 80 L; imports 120 K, 30 L
    assert (exp_x, imp_x) == (260 / 80, 120 / 30)
    # Leontief's comparison says labour-abundant, Leamer's says capital-abundant
    assert exp_x < imp_x and prod > cons
    # HOV: consumption embodies the world's capital-labour ratio
    assert cons == world == 2.0
