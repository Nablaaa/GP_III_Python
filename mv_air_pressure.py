# coding=utf8
"""
This programme is supposed to compute the gaussian uncertainity
propagation for:

Experiment: Millikan′s oil drop experiment
Formula: air pressure
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

    # Variablen und deren Formelzeichen festlegen
    l, h, T = symbols('l h T')

    # Variablen als Liste speichern um spaeter danach abzuleiten
    var = ['l', 'h', 'T']
    
    # Messwerte bzw. errechnete Mittelwerte (Reihenfolge entspricht der
    # der Variablen
    messwerte = [752.2, 142, 19] # l in mmm h in m
    
    # T in Celsius
    # l in mm
    # h in m
    
    # Fehler der Messwerte eintragen (in Reihenfolge wie Variablen)
    fehler = [0.0577, 4, ]

    # Formel zur Berechnung der gesuchten Größe
    formel = 1.00005 * (133.3 * ((1 - 1.6e-4 * T) * l - 4.5e-3 * (T - 20))) * (1 - 2e-7 * h)

    # Einheit (kann der Übersichtlichkeit halber hinzugefügt werden)
    einheit = "Pa"
    
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
    print("oder auch: ", 1e-5 * formel, " bar ")
#    print("Fehler zum Quadrat: ", Fehlerformel_quadrat)
#    print( "Bilde nun die Wurzel aus dem Fehler zum Quadrat: ")
    
    Endergebnis = sqrt(Fehlerformel_quadrat)   
    print("Fehler: ", Endergebnis, " ", einheit)


if __name__ == '__main__':
    main()