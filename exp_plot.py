""" Plots for GP III
"""

import numpy as np
from matplotlib import pyplot as plt
from sympy import *
from scipy.optimize import curve_fit


def main():

# Everything within here has to be subsituted for each new experiment
########################################################################  
    
    # text file with data
    filename = 'Geschwindigkeit.dat'
    
    x, y = np.loadtxt(filename, skiprows=1, unpack=True)
    
    # example variable error bar values, can be subtituted by
    # gaussian uncertainity propagation if possible
    xerr = 0.1 * x + 0.0003
    yerr = 0.1 + 0.2 * np.sqrt(x)
    
########################################################################

    # create a grid
    plt.style.use('seaborn-whitegrid')
    
    fig, ax = plt.subplots()
	# to connect single dots: fmt='-k'
    ax.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='.k', capsize=3)

    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_title('Title')
    
    plt.show()
    
if __name__ == '__main__':
    main()

