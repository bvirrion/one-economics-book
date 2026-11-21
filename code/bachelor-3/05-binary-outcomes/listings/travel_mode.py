"""Discrete choice on real data: 210 travellers choose air, train, bus or car.
Conditional logit with a constant for each mode (car is the base), cost and times."""
import numpy as np
from choicetools import clogit
from econdata import sm_dataset

m = sm_dataset("modechoice")                 # one row per traveller and mode
names = ["air", "train", "bus"]
for k, name in enumerate(names, start=1):
    m[name] = (m["mode"] == k).astype(float)
cols = names + ["invc", "invt", "ttme"]  # cost ($); in-vehicle, terminal time (min)
r = clogit(m.choice.values, m[cols].values, m.individual.values)
for name, b, se in zip(cols, r["beta"], r["se"]):
    print(f"{name:6s} {b:8.4f} ({se:.4f})")
b = dict(zip(cols, r["beta"]))
print(f"value of in-vehicle time: {60 * b['invt'] / b['invc']:.1f} dollars an hour")

P = r["prob"].reshape(210, 4)               # rows: travellers; columns: air .. car
print("actual shares    ", np.round(m.groupby("mode").choice.mean().values, 3))
print("predicted shares ", np.round(P.mean(0), 3))
no_air = P[:, 1:] / (1 - P[:, [0]])          # the same model with air removed
print("without air      ", np.round(no_air.mean(0), 3), "(train, bus, car)")
