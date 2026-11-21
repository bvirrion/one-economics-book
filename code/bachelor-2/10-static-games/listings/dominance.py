"""Iterated elimination of strictly dominated strategies, then pure Nash equilibria."""

import numpy as np

rows, cols = ["U", "M", "D"], ["L", "C", "R"]
a = np.array([[4, 5, 6], [2, 8, 3], [3, 9, 2]])  # row player's payoffs
b = np.array([[3, 1, 2], [1, 4, 6], [0, 6, 8]])  # column player's payoffs

r, c = list(range(3)), list(range(3))
changed = True
while changed:
    changed = False
    for s in r[:]:  # is row s strictly worse than some other row?
        if any(all(a[t, k] > a[s, k] for k in c) for t in r if t != s):
            r.remove(s)
            print(f"remove row {rows[s]}")
            changed = True
    for s in c[:]:
        if any(all(b[k, t] > b[k, s] for k in r) for t in c if t != s):
            c.remove(s)
            print(f"remove column {cols[s]}")
            changed = True
print("survivors:", [rows[i] for i in r], [cols[j] for j in c])

nash = [
    (rows[i], cols[j])
    for i in range(3)
    for j in range(3)
    if a[i, j] == a[:, j].max() and b[i, j] == b[i, :].max()
]
print("pure Nash equilibria of the full game:", nash)
