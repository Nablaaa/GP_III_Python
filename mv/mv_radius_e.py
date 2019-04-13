# coding=utf8
"""
This programme is supposed to compute the gaussian uncertainity
propagation for:

Experiment: Millikan′s oil drop experiment
Formula: radius of an electron 
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
    
    gauss = np.sum((ergebnis)) 
        
    return gauss


def main():
    """ Hier sollen die Funktion und die Fehlerwerte eingegeben werden. """

    ####################################################################
    # Part which has to be edited for each new experiment/formula
    
    g = 9.80665

    # Variablen und deren Formelzeichen festlegen
    eta, p, B, nu_f, rho_oil, rho_air = symbols('eta p B nu_f rho_oil rho_air')

    # Variablen als Liste speichern um spaeter danach abzuleiten
    var = ['eta', 'p', 'B', 'nu_f', 'rho_oil', 'rho_air']
    
    # Messwerte bzw. errechnete Mittelwerte (Reihenfolge entspricht der
    # der Variablen
    messwerte = [1, 2, 3, 4, 6, 5]
    
    # Fehler der Messwerte eintragen (in Reihenfolge wie Variablen)
    fehler = [1, 1, 1, 1, 1, 1]

    # Formel zur Berechnung der gesuchten Größe
    formel = (sqrt(4* p**2 * (9 * eta * nu_f / ( 2 * g * (rho_oil - rho_air) ) ) )- B)/(2 * p)

    # Einheit (kann der Übersichtlichkeit halber hinzugefügt werden)
    einheit = "m"
    
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