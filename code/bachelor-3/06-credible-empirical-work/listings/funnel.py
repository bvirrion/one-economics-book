"""A simulated literature: 400 studies of a true effect of 0.1, of very different sizes.
Significant positive results are always published, the others one time in ten.
The naive mean, the inverse-variance mean and FAT--PET, before and after the filter."""
import numpy as np
from metatools import fat_pet, fixed_effect

rng = np.random.default_rng(400)
n = np.exp(rng.uniform(np.log(25), np.log(2000), 400)).round()   # per arm
se = np.sqrt(2 / n)
est = rng.normal(0.1, se)
published = (est / se > 1.96) | (rng.uniform(size=400) < 0.1)

for name, keep in [("all 400 studies", np.ones(400, bool)),
                   (f"the {published.sum()} published", published)]:
    pet, pet_se, fat, fat_se = fat_pet(est[keep], se[keep])
    print(f"{name}: simple mean {est[keep].mean():.3f},"
          f" inverse-variance mean {fixed_effect(est[keep], se[keep])[0]:.3f}")
    print(f"  FAT (slope on s.e.) {fat:6.3f} (s.e. {fat_se:.3f}),"
          f" PET (effect at s.e. 0) {pet:.3f} (s.e. {pet_se:.3f})")
