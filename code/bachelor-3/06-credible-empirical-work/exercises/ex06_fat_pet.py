"""Exercise 6: FAT--PET on the twelve estimates printed in the exercise."""
import numpy as np
from metatools import fat_pet, fixed_effect

se = np.array([0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15, 0.18, 0.20, 0.25])
est = np.array([0.05, 0.07, 0.06, 0.11, 0.13, 0.17, 0.21, 0.26, 0.31, 0.38, 0.42, 0.53])
pet, pet_se, fat, fat_se = fat_pet(est, se)
print(f"simple mean {est.mean():.3f},"
      f" inverse-variance mean {fixed_effect(est, se)[0]:.3f}")
print(f"FAT {fat:.3f} (s.e. {fat_se:.3f}), t = {fat / fat_se:.1f}")
print(f"PET {pet:.4f} (s.e. {pet_se:.4f}), t = {pet / pet_se:.1f}")
