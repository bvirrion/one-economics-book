"""The semi-endogenous growth model: what doubling the research share does.

Ideas grow as dA/dt = NU * s * L * A**PHI; output per worker is A * (1 - s); the
workforce grows at rate N. The economy starts on its balanced growth path with s = 2%.
"""

PHI, N, NU, DT = 0.5, 0.01, 1.0, 0.01


def simulate(share, years=200):
    a = (0.02 * (1 - PHI) / N) ** (1 / (1 - PHI))  # on the baseline's balanced path
    labour, out = 1.0, {}
    for step in range(int(years / DT) + 1):
        if step % int(1 / DT) == 0:
            g = NU * share * labour * a ** (PHI - 1)
            out[round(step * DT)] = (a, g)
        a += NU * share * labour * a**PHI * DT
        labour *= 1 + N * DT
    return out


base, double = simulate(0.02), simulate(0.04)
print("year  growth of A (%)  output per worker, doubled share / baseline")
for t in (0, 10, 25, 50, 100, 200):
    ratio = double[t][0] * (1 - 0.04) / (base[t][0] * (1 - 0.02))
    print(f"{t:4}  {100 * double[t][1]:15.2f}  {ratio:10.3f}")
growth, level = N / (1 - PHI), 2 ** (1 / (1 - PHI)) * 0.96 / 0.98
print(f"long run: growth {100 * growth:.2f}%, level ratio {level:.3f}")
