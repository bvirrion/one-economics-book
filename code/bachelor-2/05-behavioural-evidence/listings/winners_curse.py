"""Publishing only significant results exaggerates effects: a simulation."""

import numpy as np

rng = np.random.default_rng(505)
true_r, n, studies = 0.15, 100, 20_000
se = 1 / np.sqrt(n)  # standard error of a correlation near zero

estimate = true_r + se * rng.standard_normal(studies)
significant = estimate > 1.96 * se  # one-sided filter: a positive result
published = estimate[significant]

replication = true_r + se * rng.standard_normal(published.size)
print(f"true effect                 {true_r:.3f}")
print(f"share significant (power)   {significant.mean():.3f}")
print(f"mean published estimate     {published.mean():.3f}")
print(f"mean replication estimate   {replication.mean():.3f}")
print(f"replications significant    {(replication > 1.96 * se).mean():.3f}")
print(f"relative effect size        {replication.mean() / published.mean():.3f}")
