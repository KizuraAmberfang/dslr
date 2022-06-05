# What are the two features that are similar?

import sys
from describeUtils import * 
from utils.read_csv import read_csv
import matplotlib.pyplot as plt

def plot_hist(gryf, raven, huffle, slyth, label, axs):

	hg = gryf[label]
	hg = hg[~np.isnan(hg)]
	axs.hist(hg, color='red', alpha=0.4)

	hs = slyth[label]
	hs = hs[~np.isnan(hs)]
	axs.hist(hs, color='green', alpha=0.4)

	hr = raven[label]
	hr = hr[~np.isnan(hr)]
	axs.hist(hr, color='blue', alpha=0.4)

	hh = huffle[label]
	hh = hh[~np.isnan(hh)]
	axs.hist(hh, color='yellow', alpha=0.4)

	axs.set_title(label)

if len(sys.argv) != 2:
	print("Usage: python3 histogram.py fileName")
	sys.exit(0)

matrix = read_csv(sys.argv[1], ',')
labels = matrix.dtype.names

# Gryffindor
temp = np.where(matrix[labels[1]] == "Gryffindor")
gryf = matrix[temp[0]]

# Ravenclaw
temp = np.where(matrix[labels[1]] == "Ravenclaw")
raven = matrix[temp[0]]

# Hufflepuff
temp = np.where(matrix[labels[1]] == "Hufflepuff")
huffle = matrix[temp[0]]

# Slytherin
temp = np.where(matrix[labels[1]] == "Slytherin")
slyth = matrix[temp[0]]

plt.title("What are the two features that are similar?")
plt.scatter(gryf[labels[6]], gryf[labels[7]], color='red', alpha=0.4)
plt.scatter(raven[labels[6]], raven[labels[7]], color='blue', alpha=0.4)
plt.scatter(huffle[labels[6]], huffle[labels[7]], color='yellow', alpha=0.4)
plt.scatter(slyth[labels[6]], slyth[labels[7]], color='green', alpha=0.4)

plt.legend(["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"], loc="upper center", ncol=4)

plt.xlabel = labels[6]
plt.ylabel = labels[7]
print(labels[6])
print(labels[7])
plt.show()
