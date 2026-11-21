"""Two ways to read the factor content of trade: Leontief's and Leamer's."""
import numpy as np

A = np.array([[4.0, 1.0, 2.0],      # capital per unit: machines, clothing, furniture
              [1.0, 3.0, 2.0]])     # labour per unit
exports = np.array([60.0, 0.0, 10.0])
imports = np.array([30.0, 0.0, 0.0])
V = np.array([540.0, 250.0])        # Home's capital and labour
V_world = np.array([2000.0, 1000.0])

FX, FM = A @ exports, A @ imports   # factors embodied in exports and in imports
F = FX - FM                         # factor content of net exports
print("capital per worker in exports:", FX[0] / FX[1])
print("capital per worker in imports:", FM[0] / FM[1])
print("net exports of factor services: capital", F[0], " labour", F[1])

C = V - F                           # factors embodied in what Home consumes
print("capital per worker in production: ", round(V[0] / V[1], 3))
print("capital per worker in consumption:", C[0] / C[1])
print("capital per worker in the world:  ", V_world[0] / V_world[1])
print("consumption share s:", C / V_world)
