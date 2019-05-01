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
    d, h = symbols('d h')

    # Variablen als Liste speichern um spaeter danach abzuleiten
    var = ['d', 'h']
    
    # Messwerte bzw. errechnete Mittelwerte (Reihenfolge entspricht der
    # der Variablen
    messwerte = [0.71, 1.92]
    
    # Fehler der Messwerte eintragen (in Reihenfolge wie Variablen)
    fehler = [50*1e-6 + 5*0,71 * 1e-4, 50*1e-6 + 5*1,92 * 1e-4]

    # Formel zur Berechnung der gesuchten Grosse
    formel = np.pi * (d/2)**2 * h

    # Einheit (sollte der uebersichtlichkeit halber hinzugefuegt werden)
    einheit = " cm^3"
    
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
