import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
import scipy.interpolate as sci

# change to your file
with open("filled_coil_inductance.dat") as f:
    reader = csv.reader(f, delimiter="\t")
    # maybe change header file.
    d = list(reader)[7:]
    head = d[0]
    d = np.asarray([[float(j) for j in i] for i in d[1:]])
print(head)
T = d[:,0]
L = d[:,1]
print(np.mean(L))
print(np.std(L))

L_err = np.asarray(L) * 0.005 + 0.0000001
print(np.mean(L_err))


# plot
plt.errorbar(T, L, yerr=L_err, label="data", elinewidth=1, capsize=2, errorevery=1)
plt.xlabel("Temperature [K]")
plt.ylabel("Inductance [mH]")
plt.title("Inductance of the coil filled with BSSCO")
# change to your T
plt.axvline(107.8, color="black", alpha=0.5)
plt.show()