import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
import scipy.interpolate as sci

# change to your file
with open("empty_coil_refference.dat") as f:
    reader = csv.reader(f, delimiter="\t")
    # maybe check if header ends here.
    d = list(reader)[3:]
    head = d[0]
    d = np.asarray([[float(j) for j in i] for i in d[1:]])
print(head)
T = d[:,0]
L = d[:,1]
print(np.mean(L))
print(np.std(L))

def linear_fit(x,a,b):
	return a*x + b

# dont even ask...
combined = zip(T,L)
corrected = sorted(combined, key = lambda x: x[0])
T = [i[0] for i in corrected]
L = [i[1] for i in corrected]

L_err = np.asarray(L) * 0.005 + 0.0000001
print(np.mean(L_err))

# fit prep (still... dont ask.)
T_red = list(set(T))
index = [T.index(i) for i in T_red]
L_red = [L[i] for i in index]

# fitting (so much work for this.)
t_lin = np.linspace(80,140, 5000)
f = sci.interp1d(T_red, L_red, kind="cubic")
l_lin = f(t_lin)
popt, pcov = sco.curve_fit(linear_fit, t_lin, l_lin)
l_lin = linear_fit(t_lin, *popt)


print(pcov)

# plot
plt.errorbar(T, L, yerr=L_err, label="data", elinewidth=1, capsize=2, errorevery=3)
plt.plot(t_lin, l_lin, label="ax+b where:\na = {:.3e}\nb = {:.3f}".format(*popt))
plt.xlabel("Temperature [K]")
plt.ylabel("Inductance [mH]")
plt.title("Inductance of the empty coil")
plt.axvline(107.8, color="black", alpha=0.5)
plt.legend()
plt.show()