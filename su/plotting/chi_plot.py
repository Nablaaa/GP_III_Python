import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
import scipy.interpolate as sci

# change this filename
with open("filled_coil_inductance.dat") as f:
    reader = csv.reader(f, delimiter="\t")
    # maybe change the 7 to whatever fits your header
    d = list(reader)[7:]
    head = d[0]
    d = np.asarray([[float(j) for j in i] for i in d[1:]])
print(head)

T = d[:,0]
L = d[:,1]

def linear_fit(x,a,b):
	return a*x + b

# set these parameters to the ones given by the linear fit
a = 7.209e-5
b = 0.260

L_0 = linear_fit(T, a, b)

# put your errors and constants here
L_0_err = 0.0013
L_err = np.asarray(L) * 0.005 + 0.0000001
V_c = 905
V_s = 693

# hope the maths checks out
chi = (L / L_0 - 1) * (V_c / V_s)
dl = (1 / L_0) * (V_c / V_s)
dl0 = (L/(L_0**2)) * (V_c / V_s)
dvs = (V_c / (V_s**2)) - (L / L_0 * (V_c / (V_s**2)))

chi_err = np.sqrt((dl*L_err)**2+(dl0*L_0_err)**2+(dvs*10)**2)

# plot
plt.errorbar(T, chi, yerr=chi_err, label="data", elinewidth=1, capsize=2, errorevery=1)
plt.xlabel("Temperature [K]")
plt.ylabel("Chi")
plt.title("Chi of the coil filled with BSSCO")

# change values to fit your data
t = 107.3
dt = 100.3
plt.axvline(t, color="black", alpha=0.5)
plt.axvline(dt, color="black", alpha=0.5)
plt.fill_between(np.arange(dt, t, 0.05), -1, 1, alpha=0.2)
plt.axis([78,141,-0.9,0.1])
plt.show()