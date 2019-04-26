import numpy as np
from sympy import *
init_printing()
def gauss(func, var, err):
    ableitungen = np.asarray([j * func.diff(i) for i, j in zip(var, err)])
    squared = ableitungen ** 2
    return sqrt(np.sum(squared))

def gesammte_auswertung(func, var, val, error, unit=""):
    print("############Gaußsche Fehlerfortpflanzung###############")
    print(" ")
    for i in zip(var, val, error):
        print("Variable: {}, Wert: {}, Fehler: {}".format(*i))
    print(" ")
    print("Funktion:")
    display(func)
    fehlerfunc = gauss(func, var, error)
    print("Fehlerfunktion:")
    display(fehlerfunc)
    print(" ")
    result = func.subs(zip(var, val))
    print("Ergebnis: {} {}".format(result, unit))
    print(" ")
    end_error = fehlerfunc.subs(zip(var, val))
    print("Fehler: {} {}".format(end_error, unit))