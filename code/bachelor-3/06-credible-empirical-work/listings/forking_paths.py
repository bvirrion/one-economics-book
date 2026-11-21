"""The garden of forking paths: data in which the treatment does nothing, analysed in
16 defensible ways (2 outcomes x 2 control sets x 2 samples x 2 outlier rules)."""
import itertools

import numpy as np
import statsmodels.api as sm


def dataset(rng, n=400):
    age = rng.uniform(20, 60, n)
    school = rng.integers(8, 17, n).astype(float)
    treat = rng.integers(0, 2, n).astype(float)
    common = rng.normal(0, 1, n)              # the two outcomes share a component
    ys = [0.02 * age + 0.1 * school + common + rng.normal(0, 1, n) for _ in range(2)]
    return age, school, treat, ys


def p_values(rng):
    age, school, treat, ys = dataset(rng)
    out = []
    for y, ctrl, young, trim in itertools.product(ys, [0, 1], [0, 1], [0, 1]):
        keep = (age < 50) if young else np.ones(len(y), bool)
        if trim:
            keep &= np.abs(y - y.mean()) < 2.5 * y.std()
        cols = [treat] + ([age, school] if ctrl else [])
        X = sm.add_constant(np.column_stack(cols)[keep])
        out.append(sm.OLS(y[keep], X).fit(cov_type="HC1").pvalues[1])
    return np.array(out)


rng = np.random.default_rng(16)
p = p_values(rng)
print("one dataset, 16 p-values, sorted:")
print("   ", " ".join(f"{x:.2f}" for x in np.sort(p)))
print(f"significant at 5 %: {(p < 0.05).sum()} of 16")
many = np.array([p_values(rng) for _ in range(1000)])
print(f"share of 1,000 null datasets significant on the first path: "
      f"{(many[:, 0] < 0.05).mean():.3f}")
print(f"share with at least one significant path: {(many < 0.05).any(1).mean():.3f}")
print(f"if the 16 tests were independent: {1 - 0.95**16:.3f}")
