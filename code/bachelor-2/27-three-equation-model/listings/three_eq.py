"""The three-equation model after an inflation shock: invented parameters.

IS: x[t] = -A * (r[t-1] - R_STAR). PC: pi[t] = pi[t-1] + ALPHA * x[t]. The bank
minimises (pi - TARGET)**2 + LAM * x**2: it aims at x = -(ALPHA / LAM) (pi - TARGET).
"""

A, ALPHA, LAM, R_STAR, TARGET = 0.5, 0.5, 0.5, 2.0, 2.0


def path(pi0, periods=8):
    rows, pi = [], pi0
    for t in range(periods):
        # choose next period's gap on the MR curve, given this period's inflation
        pi_next = TARGET + (pi - TARGET) / (1 + ALPHA**2 / LAM)
        x_next = -(ALPHA / LAM) * (pi_next - TARGET)
        r = R_STAR - x_next / A
        rows.append((t, pi, r, r + pi))
        pi = pi_next
    return rows


print("period  inflation  real rate  nominal rate")
total = path(5.0, periods=60)
for t, pi, r, i in total[:6]:
    print(f"{t:6}  {pi:9.2f}  {r:9.2f}  {i:12.2f}")
loss = sum(A * (r - R_STAR) for _, _, r, _ in total)
print(f"cumulated output loss {loss:.2f}, sacrifice ratio {loss / 3:.2f}")
