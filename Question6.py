import numpy as np
from Constantes import A, g, mu, dt, T, Transition
import matplotlib.pyplot as plt




# Conditions initiales
omega = 2 * np.pi * 1.5  # Exemple de fréquence angulaire
x0_1 = 1.0
v0_1 = 0.2
x0_2 = 2.0
v0_2 = 0.2+1e-50

# Distance fixe entre les billes/longueure du fil reliant les billes
L = abs(x0_2 - x0_1)

# Fonction de simulation simulation
def simulation(omega, x0_1, v0_1, x0_2, v0_2, L):
    time = np.arange(0, T, dt)
    x1 = x0_1
    v1 = v0_1
    x2 = x0_2
    v2 = v0_2
    positions_1 = []
    positions_2 = []

    for t in time:
        y = A * np.sin(omega * t)
        v_plateau = A * omega * np.cos(omega * t)
        
        # Mise à jour de la bille 1
        v1 += -g * dt
        x1 += v1 * dt
        if x1 <= y:
            v1 = -mu * (v1 - v_plateau) + v_plateau
            x1 = y
        
        # Mise à jour de la bille 2
        v2 += -g * dt
        x2 += v2 * dt
        if x2 <= y:
            v2 = -mu * (v2 - v_plateau) + v_plateau
            x2 = y
        
        # Contrainte de distance fixe entre les billes
        if abs(x2 - x1) > L:
            midpoint = (x1 + x2) / 2
            x1 = midpoint - L / 2
            x2 = midpoint + L / 2
        
        positions_1.append(x1)
        positions_2.append(x2)
    
    return time, positions_1, positions_2

# Simuler les trajectoires des deux billes
time, positions_1, positions_2 = simulation(omega, x0_1, v0_1, x0_2, v0_2, L)

# Tracer les trajectoires des deux billes
plt.figure(figsize=(12, 6))
plt.plot(time, positions_1, label='Trajectoire de la bille 1')
plt.plot(time, positions_2, label='Trajectoire de la bille 2')
plt.xlabel('Temps (s)')
plt.ylabel('Hauteur (m)')
plt.legend()
plt.title('Trajectoires des deux billes attachées par un fil sans masse')
plt.show()
