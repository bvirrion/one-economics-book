"""A life in six decades: the consumption plan that the Euler equation gives."""

income = [20.0, 32.0, 38.0, 40.0, 30.0, 10.0]  # thousand dalens a year, each decade
r = 0.48  # interest over a decade (about 4 per cent a year)
gamma = 2.0  # CRRA coefficient: the EIS is 1/gamma


def plan(beta):
    growth = (beta * (1 + r)) ** (1 / gamma)  # Euler: c[t+1] / c[t]
    disc = [(1 + r) ** -t for t in range(len(income))]
    resources = sum(m * d for m, d in zip(income, disc))  # present value
    c0 = resources / sum(growth**t * d for t, d in enumerate(disc))
    c = [c0 * growth**t for t in range(len(income))]
    assets, b = [], 0.0
    for m, ct in zip(income, c):
        b = b * (1 + r) + m - ct  # wealth at the end of the decade
        assets.append(b)
    return c, assets


for beta in (1 / (1 + r), 0.5):
    c, assets = plan(beta)
    print(f"beta = {beta:.3f}   beta(1+r) = {beta * (1 + r):.2f}")
    print("decade  income  consumption  assets (per year of the decade)")
    for t, (m, ct, b) in enumerate(zip(income, c, assets), start=1):
        print(f"{t:6d} {m:7.1f} {ct:12.1f} {round(b, 1) + 0.0:7.1f}")
