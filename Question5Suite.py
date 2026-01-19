import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Paramètres du système de Lorenz
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# Équations différentielles du système de Lorenz
def lorenz(t, y):
    x, y, z = y
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Conditions initiales
y0 = [1.0, 1.0, 1.0]
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Résolution des équations différentielles
sol = solve_ivp(lorenz, t_span, y0, t_eval=t_eval, method='RK45')

# Traçage de l'attracteur étrange de Lorenz
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], lw=0.5, color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Attracteur étrange de Lorenz')

plt.show()
