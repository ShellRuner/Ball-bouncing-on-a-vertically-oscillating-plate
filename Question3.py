import numpy as np
from Constantes import A, g, mu, dt, T
import matplotlib.pyplot as plt


omega = 2 * np.pi * 1.5  # Fréquence angulaire

# Conditions initiales
x0_1 = 0.0 #conditions initiales pour
v0_1 = 0.2 #la premiere bille

x0_2 = 0.2 + 1e-50  # ( ou 0.5+1e-50) Condition initiale légèrement différente pour la deuxième bille
v0_2 = 0.2 + 1e-50

# Fonction de simulation modifiee
def simulation(omega, x0, v0):
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
        
        positions.append(x)
    
    return time, positions

# Simuler les deux trajectoires
time1, positions_1 = simulation(omega, x0_1, v0_1)
time2, positions_2 = simulation(omega, x0_2, v0_2)

#Calcul de l'exposant de Lyapunov
    # Calculer la distance entre les deux trajectoires
distances = np.abs(np.array(positions_1) - np.array(positions_2))

    # Estimer l'exposant de Lyapunov
distances_new = distances[distances>0] #extraire les distance > 0 car log(0) n'existe pas
lyapunov_exp = np.mean(np.log(distances_new / distances[0])) / dt #calcul de la moyenne

# Tracer les trajectoires
plt.figure(figsize=(12, 6))
plt.plot(time1, positions_1, label='Trajectoire de la bille 1', color='purple')
plt.plot(time2, positions_2, label='Trajectoire de la bille 2', color= 'yellow')
plt.xlabel('Temps (s)')
plt.ylabel('Hauteur (m)')
plt.legend()
plt.title('Trajectoires des deux billes')
plt.show()

print(f"""Conditions initiales:
         Fequence: {omega/2*np.pi:.2f} Hz 
         Bille1: x01 = 0.0 ; v01 = 0.2
         Bille2: x02 = 0.2 + 10-50 ; v02 = 0.2 + 10-50
      """)

print(f"Exposant de Lyapunov estimé : {lyapunov_exp}")
