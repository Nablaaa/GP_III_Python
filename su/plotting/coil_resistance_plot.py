import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
import scipy.interpolate as sci

# change to your file
with open("empty_coil_refference.dat") as f:
    reader = csv.reader(f, delimiter="\t")
    # maybe change to right starting line
    d = list(reader)[3:]
    head = d[0]
    d = np.asarray([[float(j) for j in i] for i in d[1:]])
print(head)
T = d[:,0]
R = d[:,2]
R_err = 0.005 * R

# plot
plt.errorbar(T, R, yerr=R_err, label="data", elinewidth=1, capsize=2, errorevery=3)
plt.xlabel("Temperature [K]")
plt.ylabel("Resistance [Ohm]")
plt.title("Resistance of the coil")
plt.show()