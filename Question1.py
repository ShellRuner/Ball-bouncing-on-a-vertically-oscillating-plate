from Constantes import A, g, mu, dt, T
import TraceCourbe as Tc
import numpy as np
import matplotlib.pyplot as plt

#Conditions initiales
x0 = 1.0 # position de la bille a t = 0
v0 = 0.0 # vitesse initiale de la bille

#Valeurs de Omega (pulsation)
"""Creation d'une plage de 5 valeurs de omega
comprises entre 2pi et 20pi c-a-d pour des frequences comprises
entre 1Hz et 10Hz
"""
valeurs_omega = np.linspace(2*np.pi, 20*np.pi, 5)

#Fonction de simulation
def simulation(omega):
    """Cette fonction pour une pulsation retourne les valeurs
    des positions de la bille en fonction de temps
    """
    time = np.arange(0, T, dt) #Creation d'une plage de valeures
                                #pour l'axe des temps
                        
    x = x0
    v = v0
    positions = [] #Initialisation de la variable reccueillant la plage
                   #des positions pour l'axe des ordonnees
                   
    for t in time:
        y = A * np.sin(omega * t) #Fonction decrivant les differentes positions
                                  #prises par le plateau durant sont mouvouvement
                                  #d'oscillation
                                  
        vitesse_plateau = A*omega*np.cos(omega*t)
        #Mise a jour des vitesses et positions de la bille
        #en fonction du temps
        v = v + (-g * dt)
        x = x + v * dt
        
        #Choc entre bille et plateau a l'instant t
        if x <= y:
            v = -mu * (v-vitesse_plateau) + vitesse_plateau #Vitesse apres choc
            x = y #faire ressortir la notion de choc
            
        positions.append(x)
    return time, positions

#Tracer les courbes  pour differentes valeurs de omega
plt.figure(figsize=(12, 12))          
Tc.OmegaCourbe(simulation, valeurs_omega)
Tc.TracerOmeg()
plt.show()