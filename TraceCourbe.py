"""Ce fichier contient des fonction permettant de representer et visualiser
les courbes sur un graphe, il sert aussi de module pour importer ces fonctions
"""


import numpy as np
import matplotlib.pyplot as plt

#Tracer lescourbes pour chaque valeurs de Omega
def OmegaCourbe(func,value):
    """Cette fonction permet de preparer le jeux de donnees
    en abscisses et en ordonnees des courbes representant les
    differentes trajectoires de la billes pour differentes valeurs de
    Omega
    """
    for omega in value:
        time, positions = func(omega)
        plt.plot(time, positions, label=f'omegae={omega/(2*np.pi):.2f} Hz')
        
def TracerOmeg():
    """Cette fonction permet de tracer et visualiser les courbes representant les trajectoires
    a proprement parler de la bille pour differentes valeurs de Omega
    """
    plt.xlabel('Temps (s)')
    plt.ylabel('Hauteur (m)')
    plt.title('Position de la bille')
    plt.legend()
    plt.show()
    
#Tracer le diagramme de bifurcation
def Bifurcation_Diagrame(func, value):
    """Cette fonction permet de preparer les donnees en abscisse et en ordonnees
    pour representer le diagramme de bifurcation
    """
    donnee_De_bifurcation = []
    for omega in value:
        positions = func(omega)
        for position in positions:
            donnee_De_bifurcation.append((omega / (2 * np.pi), position))
    return donnee_De_bifurcation

def TracerBifurc(donnee_De_bifurcation_tab):
    """Cette fonction permet de tracer le diagramme de bifurcation
    """
    print(np.shape(donnee_De_bifurcation_tab))
    plt.plot(donnee_De_bifurcation_tab[:, 0], donnee_De_bifurcation_tab[:, 1], 'r.', markersize=0.5)
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Position de la bille (m)')
    plt.title('Diagramme de bifurcation de la bille rebondissante')
    
#Observation de l'Hysteresis
def TracerHysteresis(omega_increas, position_increas, omega_decreas, position_decreas):
    """Cette fonction permet d'observer le phenomene d'hysteresis
    """
    plt.plot(omega_increas, position_increas, 'b-', label='Augmentation de omega')
    plt.plot(omega_decreas, position_decreas, 'r-', label='Diminution de omega')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Position moyenne de la bille (m)')
    plt.title('Phénomène d\'hystérésis dans le système de la bille rebondissante')
    plt.legend()
