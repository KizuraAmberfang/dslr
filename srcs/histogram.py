# which hogwarts course has a homogeneous score distribution between all four houses?

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

fig, axs = plt.subplots(ncols=4, nrows=4, sharey=True, constrained_layout=True)
plt.figtext(0.1, 0.9, "Which hogwarts course has a homogeneous score distribution between all four houses?", wrap=True)
fig.supylabel("student")
fig.supxlabel("score")
axs[0, 0].remove()
axs[0, 1].remove()
axs[0, 2].remove()
plot_hist(gryf, raven, huffle, slyth, labels[6], axs[0, 3])
plot_hist(gryf, raven, huffle, slyth, labels[7], axs[1, 0])
plot_hist(gryf, raven, huffle, slyth, labels[8], axs[1, 1])
plot_hist(gryf, raven, huffle, slyth, labels[9], axs[1, 2])
plot_hist(gryf, raven, huffle, slyth, labels[10], axs[1, 3])
plot_hist(gryf, raven, huffle, slyth, labels[11], axs[2, 0])
plot_hist(gryf, raven, huffle, slyth, labels[12], axs[2, 1])
plot_hist(gryf, raven, huffle, slyth, labels[13], axs[2, 2])
plot_hist(gryf, raven, huffle, slyth, labels[14], axs[2, 3])
plot_hist(gryf, raven, huffle, slyth, labels[15], axs[3, 0])
plot_hist(gryf, raven, huffle, slyth, labels[16], axs[3, 1])
plot_hist(gryf, raven, huffle, slyth, labels[17], axs[3, 2])
plot_hist(gryf, raven, huffle, slyth, labels[18], axs[3, 3])

fig.legend(["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"], loc="upper left", bbox_to_anchor=(0.1, -0.12, 1.0, 1.0), ncol=2)

plt.show()
