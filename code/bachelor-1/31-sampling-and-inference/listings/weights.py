"""A stratified sample of Brenland households: owners over-sampled."""

import numpy as np
import pandas as pd
from country import load

h = load("households")
rng = np.random.default_rng(2026)
take = {1: 150, 0: 150}  # 150 owners and 150 renters
parts = [h[h.owner == k].sample(m, random_state=rng) for k, m in take.items()]
sample = pd.concat(parts)
N = h.owner.value_counts()  # households in each stratum
sample["weight"] = sample.owner.map(N) / sample.owner.map(take)  # 1 / P(drawn)
y, w = sample.disposable, sample.weight
print(f"true mean {h.disposable.mean():,.0f}")
print(f"unweighted {y.mean():,.0f}; weighted {(w * y).sum() / w.sum():,.0f}")
print("weights:", sample.groupby("owner").weight.first().round(2).to_dict())
deff = 1 + (w.std(ddof=0) / w.mean()) ** 2  # Kish's design effect of weighting
print(f"design effect {deff:.3f}; effective sample size {len(sample) / deff:.0f}")
