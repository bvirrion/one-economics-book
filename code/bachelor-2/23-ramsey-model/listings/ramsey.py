"""The Ramsey model's saddle path, found by shooting from a quarter of the steady-state
capital. f(k) = k**ALPHA; time in years; Euler steps of a hundredth of a year."""

ALPHA, DELTA, RHO, N = 1 / 3, 0.05, 0.03, 0.01
K_STAR = (ALPHA / (RHO + DELTA)) ** (1 / (1 - ALPHA))


def path(c, theta, k, dt=0.01, years=150):
    out = []
    for step in range(int(years / dt)):
        if step % 100 == 0:
            out.append((k, c))  # one point a year
        dk = k**ALPHA - c - (N + DELTA) * k
        dc = c * (ALPHA * k ** (ALPHA - 1) - DELTA - RHO) / theta
        if dk < 0 or dc < 0:  # consumption too high, or too low
            return "high" if dk < 0 else "low"
        k, c = k + dk * dt, c + dc * dt
    return out


def saddle(theta, k0):
    lo, hi, best = 0.0, k0**ALPHA, None
    for _ in range(50):  # bisection on initial consumption
        res = path((lo + hi) / 2, theta, k0)
        best = res if isinstance(res, list) else best
        lo, hi = ((lo + hi) / 2, hi) if res == "low" else (lo, (lo + hi) / 2)
    return best


s_star = (N + DELTA) * K_STAR ** (1 - ALPHA)
print(f"steady state: k* = {K_STAR:.3f}, saving rate {s_star:.3f}")
for theta in (2, 6):
    p = saddle(theta, K_STAR / 4)
    rate = [1 - c / k**ALPHA for k, c in p]
    half = next(t for t, (k, c) in enumerate(p) if k > K_STAR * (1 - 0.375))
    print(f"theta {theta}: saving rate {rate[0]:.3f}, {rate[10]:.3f} after 10 years,")
    print(f"  {rate[40]:.3f} after 40; capital gap halved after {half} years")
