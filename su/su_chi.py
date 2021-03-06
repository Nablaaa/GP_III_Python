# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:20:49 2019

@author: Eric
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
    Vc, Vs, L, L0 = symbols('Vc Vs L L0')
    
    """
    VARIABLENBENENNUNG
    Vc - volume coil
    Vs - volume sample 
    L0 - L without sample 
    """

    # Variablen als Liste speichern um spaeter danach abzuleiten
    var = ['Vc', 'Vs', 'L', 'L0']
    
    # Messwerte bzw. errechnete Mittelwerte (Reihenfolge entspricht der
    # der Variablen)
    messwerte = [2.48, 1.79, 0.3567, 0.26056]
    
    # Fehler der Messwerte eintragen (in Reihenfolge wie Variablen)
    fehler = [0.012, 0.0096, 0.005*0.3567, 0.00007 ]

    # Formel zur Berechnung der gesuchten Grosse
    formel = Vc/Vs * (L/L0 - 1)
    # Herleitung siehe zB ExPhy 2 - Uebungsblatt 9, Aufgabe 2

    # Einheit (sollte der uebersichtlichkeit halber hinzugefuegt werden)
    einheit = " "
    # einheitenlos
    
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
    Endergebnis = sqrt(Fehlerformel_quadrat)   
    print("Fehler: ", Endergebnis, " ", einheit)
    

if __name__ == '__main__':
    main()
