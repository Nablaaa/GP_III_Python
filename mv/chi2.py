# -*- encoding: utf-8 -*-


import functools
import numpy as np
import matplotlib.pyplot as plt



def getchi(e,data):
   chi=0
   for i in range (len(data)):
      n=int(data[i]/e+0.5)
      
      chi+=(n*e-data[i])**2
   #print (chi)
   return chi




def main():
    """Hauptprogramm"""
    print(__doc__)                                  # Ausgabe Programm Doc-String

    
    # Erstelle einen Plotbereich
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    #ax.axis([10**-19, 2*10**-19, 0, 2*10**-35])       # Achsengrenzen
    ax.set_xlabel("e")                          # Beschriftung x-Achse
    ax.set_ylabel("chi2")                       # Beschriftung y-Achse
    ax.grid(linestyle='-', linewidth=1)
    N=200000
    x=np.linspace(1.5*10**-19, 1.8*10**-19, N)
    y=np.zeros(N)
    #print (x)
    data=[5.197*10**-18,3.0229*10**-18,7.674*10**-18,3.378*10**-18,5.689*10**-18,1.219*10**-18]
    #data=[5.197*10**-18]
    for i in range(N):
      y[i]=getchi(x[i],data)
      #print (y[i])
    
    ax.plot(x, y, marker='o',linestyle='', lw=1, markersize=1)
    plt.show()


if __name__ == "__main__":
    main()
