"""Exercise 8: the factor content of a country's trade, F = A T, for three goods and
two factors (capital in machine-hours, labour in worker-hours, per unit of output)."""
import numpy as np

A = np.array([[4.0, 2.0, 1.0],      # capital per unit: steel, cars, clothing
              [1.0, 2.0, 3.0]])     # labour per unit
T = np.array([10.0, -5.0, -8.0])    # net exports, units
V = np.array([400.0, 500.0])        # endowments
F = A @ T
print("factor content of trade: capital", F[0], " labour", F[1])
print("as a share of the endowment: capital", round(F[0] / V[0], 3),
      " labour", round(F[1] / V[1], 3))
