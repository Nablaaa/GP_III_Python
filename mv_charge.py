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
    
    gauss = np.sum((ergebnis)) 
        
    return gauss


def main():
    """ Hier sollen die Funktion und die Fehlerwerte eingegeben werden. """

    ####################################################################
    # Part which has to be edited for each new experiment/formula
    
    g = 9.80665 

    # Variablen und deren Formelzeichen festlegen
    eta, d, U, nu_f, nu_s, rho_oil, rho_air, B, p, r = symbols('eta d U nu_f nu_s rho_oil rho_air B p r')

    # Variablen als Liste speichern um spaeter danach abzuleiten
    var = ['eta', 'd', 'U', 'nu_f', 'nu_s', 'rho_oil', 'rho_air', 'B', 'p', 'r']
    
    # Messwerte bzw. errechnete Mittelwerte (Reihenfolge entspricht der
    # der Variablen
    messwerte = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
    
    # Fehler der Messwerte eintragen (in Reihenfolge wie Variablen)
    fehler = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # Formel zur Berechnung der gesuchten Größe
    formel = 18 * np.pi * eta * d * (1 / U) * sqrt(eta * nu_f / (2 * g * (rho_oil - rho_air))) * (nu_f + nu_s) * ((1 + B / (p * r))**(-1.5))

    # Einheit (kann der Übersichtlichkeit halber hinzugefügt werden)
    einheit = "C"
    
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
