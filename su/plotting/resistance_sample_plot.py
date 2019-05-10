import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
import scipy.interpolate as sci

# change to your file
with open("resistance_sample.dat") as f:
    reader = csv.reader(f, delimiter="\t")
    # maybe change to the right starting line in header
    d = list(reader)[3:]
    head = d[0]
    d = np.asarray([[float(j) for j in i] for i in d[1:]])
print(head)
T = d[:,0]
R = d[:,2]*1000

R_err = R * 0.01


# plot
plt.errorbar(T, R, yerr=R_err, label="data", elinewidth=1, capsize=2, errorevery=3)
plt.xlabel("Temperature [K]")
plt.ylabel("Resistance [mOhm]")
plt.title("Resistance of the BSSCO sample")
# change to your T
plt.axvline(107.8, color="black", alpha=0.5)
plt.show()