# -*- encoding: utf-8 -*-


import functools
import numpy as np
import matplotlib.pyplot as plt



def getchi(e,data, error):
   chi=0
   for i, j in zip(data, error):
      n=int(i/e+0.5)
      chi+=(n*e-i)**2 / (j**2)
   #print (chi)
   return chi




def main():
    """Hauptprogramm"""
    print(__doc__)                                  # Ausgabe Programm Doc-String

    
    # Erstelle einen Plotbereich
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    #ax.set_xlim(1.8e-19, 2.1e-19)       # Achsengrenzen
    #ax.set_ylim(0,2)
    ax.set_xlabel("e [C]")                          # Beschriftung x-Achse
    ax.set_ylabel("chi2")                       # Beschriftung y-Achse
    ax.grid(linestyle='-', linewidth=1)
    N=200000
    x=np.linspace(0.1*10**-19, 4*10**-19, N)
    y=np.zeros(N)
    #print (x)
    data=[7.157e-18,8.516e-18,6.755e-16,3.84e-19]
    error = [1.696e-19, 1.722e-19, 5.345e-18, 6.518e-21]
    #data=[5.197*10**-18]
    for i in range(N):
      y[i]=getchi(x[i],data, error)
      #print (y[i])
    data = np.asarray(data)
    print(data/1.6e-19)
    print(data/1.9e-19)
    ax.set_title("Chi squared fit")
    ax.plot(x, y, marker='o',linestyle='', lw=1, markersize=1)
    plt.axvline(1.91e-19, color="red")
    plt.axhline(1, color = "orange")
    plt.show()


if __name__ == "__main__":
    main()
