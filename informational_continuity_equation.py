# Informational Continuity Equation Verification (vOmega Law 35)

import numpy as np

# 1D domain
N = 400
x = np.linspace(0, 1, N)
dx = x[1] - x[0]

# Informational density rho and flux J
rho = np.exp(-((x - 0.5)**2) / 0.01)
J = -np.gradient(rho, dx)

# Compute time derivative approximation from continuity equation
# drho/dt + dJ/dx = 0 -> drho/dt = -dJ/dx
dJdx = np.gradient(J, dx)
drho_dt = -dJdx

# Check conservation: integral(rho) remains constant
initial_mass = np.sum(rho) * dx
predicted_mass_change = np.sum(drho_dt) * dx

print("Initial informational mass:", initial_mass)
print("Predicted mass change (should be ~0):", predicted_mass_change)
print("Sample drho/dt values:", drho_dt[:10])
