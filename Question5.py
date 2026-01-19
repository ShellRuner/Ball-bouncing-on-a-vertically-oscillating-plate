import numpy as np
from Constantes import A, g, mu, dt, T
import matplotlib.pyplot as plt


# Conditions initiales
omega = 2 * np.pi * 1.5  # Exemple de fréquence angulaire (peut être ajustée)

x0 = 1.0
v0 = 0.0

# Fonction de simulation
def simulation(omega, x0, v0):
    time = np.arange(0, T, dt)
    x = x0
    v = v0
    chocs = [] #initialisation de la variable contenant la liste 
               #des  coordonnees des points de chocs entre la bille et le plateau

    for t in time:
        y = A * np.sin(omega * t)
        vitesse_plateau = A * omega * np.cos(omega * t)
        v += -g * dt
        x += v * dt
        
        if x <= y:
            v = -mu * (v - vitesse_plateau) + vitesse_plateau
            x = y
            chocs.append((t, v))
    
    return chocs

# Simuler les trajectoires
chocs = np.array(simulation(omega, x0, v0))

# Extraire les temps entre les chocs et les vitesses
times_between_chocs = []
for i in range(len(chocs) - 1):
    times_between_chocs.append(chocs[i+1][0] - chocs[i][0])
    
vitesse_apres_chocs = []
for i in range(1, len(chocs)):
    vitesse_apres_chocs.append(chocs[i][1])


# Tracer le temps entre les chocs en fonction de la vitesse après le choc
plt.figure(figsize=(12, 6))
plt.scatter(vitesse_apres_chocs, times_between_chocs, s=5)
plt.xlabel('Vitesse après le choc (m/s)')
plt.ylabel('Temps entre deux chocs (s)')
plt.title('Temps entre deux chocs en fonction de la vitesse après le choc')
plt.show()
