import re


def test_ex07_bunching_by_hand(run_exercise):
    out, _ = run_exercise("ex07_bunching")
    lines = out.splitlines()
    assert len(lines) == 3
    nums = [float(x) for x in re.findall(r"-?\d+\.\d", out)]
    # below 10: treated (0+0+1+2) - (5+9+14+16) = -41, control unchanged
    # 10-13: treated (40+25+16+12) - (15+14+12+11) = 41, control (15+14+12+11) - (15+13+12+10) = 2
    # base: jobs below 14 dollars before, 5+9+14+16+15+14+12+11 = 96
    assert nums[:3] == [-41.0, 39.0, -2.0]
    assert abs(nums[3] - 100 * -2 / 96) < 0.05


def test_ex11_recovers_elasticity(run_exercise):
    out, _ = run_exercise("ex11_supply")
    est = float(out.splitlines()[0].split(":")[1])
    assert 3.5 < est < 4.5
