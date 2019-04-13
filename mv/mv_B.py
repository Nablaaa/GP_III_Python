"""
This programme is supposed to compute the gaussian uncertainity
propagation for:

Experiment: Millikan′s oil drop experiment
Formula: electric charge e_n
"""


import numpy as np
from sympy import *


def Gauss(Ausgangsfunktion, var, fehler):
    """ Hier soll die Ableitung gebildet werden und Gauss ausgerechnet werden. """
    
    ergebnis = list()
    
    i = 0
    for i in range(len(var)):
        ableitung = Ausgangsfunktion.diff(var[i])   # Differenzieren
        faktor = ableitung * fehler[i]   # Berechnet Wert in der Klammer
        Fehler = faktor * faktor # berechnet einzelnen Fehler als Quadrat
        ergebnis.append(Fehler)
        i = i + 1
    
    Gauss = np.sum((ergebnis)) 
        
    return Gauss

def main():
    """ Hier sollen die Funktion und die Fehlerwerte eingegeben werden. """

    
    ####################################################################
    # Part which has to be edited for each new experiment/formula

    # Variablen und deren Formelzeichen festlegen
    T = symbols('T')
    var = ['T']   # Variablen als Liste speichern um spaeter danach
                  # abzuleiten
    
    # Messwerte bzw. errechnete Mittelwerte (Reihenfolge entspricht der
    # der Variablen)
    messwerte = [18]
    
    # Fehler der Messwerte eintragen (in Reihenfolge wie Variablen)
    fehler = [0.1]
    
    formel = (6.25 + 0.027 * (T - 23)) * 10e-5

    einheit = "Torr * m"
    ####################################################################
    print("Ausgangsformel: ", formel)
    Fehlerformel_quadrat =  Gauss(formel, var=var, fehler=fehler)
    
    print("Fehlerfortpflanzungsformel zum Quadrat: ", Fehlerformel_quadrat)
       
    
    # Gesuchten Wert der Formel berechnen
    i = 0
    for i in range(len(messwerte)):
        formel = formel.subs([(var[i], messwerte[i])])
        # print(Fehlerformel_quadrat)
    
    # Fehler berechnen
    i = 0
    for i in range(len(messwerte)):
        Fehlerformel_quadrat = Fehlerformel_quadrat.subs([(var[i], messwerte[i])])
        # print(Fehlerformel_quadrat)

    
    # Ergebnis ausgeben
    print("Absolutwert des Ergebnisses: ", formel, " ", einheit)
#    print("Fehler zum Quadrat: ", Fehlerformel_quadrat)
#    print( "Bilde nun die Wurzel aus dem Fehler zum Quadrat: ")
    
    Endergebnis = sqrt(Fehlerformel_quadrat)   
    print("Fehler: ", Endergebnis, " ", einheit)


if __name__ == '__main__':
    main()
