import numpy as np
import TraceCourbe as Tc
from Constantes import A, g, mu, dt, T, Transition
import matplotlib.pyplot as plt



# Conditions initiales
x0 = 1.0
v0 = 0.0

# Plage de valeurs pour omega
omega_values_increasing = np.linspace(2 * np.pi, 20 * np.pi, 100)  # Augmenter la fréquence de 1 Hz à 10 Hz
omega_values_decreasing = np.linspace(20 * np.pi, 2 * np.pi, 100)  # Diminuer la fréquence de 10 Hz à 1 Hz

# Fonction de simulation
def simulate(omega, x0, v0):
    time = np.arange(0, T, dt)
    x = x0
    v = v0
    positions = []

    for t in time:
        y = A * np.sin(omega * t)
        v_plateau = A * omega * np.cos(omega * t)
        v += -g * dt
        x += v * dt
        
        if x <= y:
            v = -mu * (v - v_plateau) + v_plateau
            x = y
        
        # Enregistrer les positions après le régime transitoire
        if t > Transition:
            if abs(t % (2 * np.pi / omega)) < dt:
                positions.append(x)
    
    return positions

# Tracer les résultats pour l'hystérésis
positions_increasing = []
positions_decreasing = []

for omega in omega_values_increasing:
    positions = simulate(omega, x0, v0)
    positions_increasing.append(np.mean(positions[-10:]))  # Moyenne des dernières positions pour éviter les transitoires

for omega in omega_values_decreasing:
    positions = simulate(omega, x0, v0)
    positions_decreasing.append(np.mean(positions[-10:]))  # Moyenne des dernières positions pour éviter les transitoires

# Conversion des données en un tableau numpy pour un tracé plus facile
omega_values_increasing_hz = omega_values_increasing / (2 * np.pi)
omega_values_decreasing_hz = omega_values_decreasing / (2 * np.pi)

#Tracer la courbe permettant de visualiser l'hysteresis
plt.figure(figsize=(12, 6))
Tc.TracerHysteresis(omega_values_increasing_hz, positions_increasing, omega_values_decreasing_hz, positions_decreasing)
plt.show()
