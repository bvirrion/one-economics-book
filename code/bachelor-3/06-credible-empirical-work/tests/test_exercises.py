def test_ex06_pet_near_zero(run_exercise):
    out, _ = run_exercise("ex06_fat_pet")
    t = float(out.splitlines()[2].split("t = ")[1])
    assert abs(t) < 1.96


def test_ex11_random_effects_wider(run_exercise):
    out, _ = run_exercise("ex11_random_effects")
    lines = out.splitlines()
    fe_se = float(lines[0].split("s.e. ")[1].rstrip(")"))
    re_se = float(lines[2].split("s.e. ")[1].rstrip(")"))
    assert re_se > fe_se
