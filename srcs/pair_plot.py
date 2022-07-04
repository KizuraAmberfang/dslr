# What feature are you going to use for your logistic regression?

import sys
from utils.read_csv import read_csv
from utils.plot_hist import plot_hist
from utils.plot_scatter import plot_scatter
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

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

fig, axs = plt.subplots(ncols=13, nrows=13)
plt.subplots_adjust(wspace=0.0, hspace=0.0)
plt.figtext(0.1, 0.9, "What feature are you going to use for your logistic regression?", wrap=True)
labels_temp = ['\n'.join(wrap(l, 15)) for l in labels]
for i in range(13):
	for j in range(13):
		if i == j:
			plot_hist(gryf, raven, huffle, slyth, labels[i + 6], axs[i, j], False)
			axs[i, j].tick_params(direction="in", labelbottom=False, labelleft=False)
			# axs[i, j].set_xticklabels(fontdict={'fontsize': 7})
		elif i < j:
			axs[i, j].remove()
		else:
			plot_scatter(gryf, raven, huffle, slyth, labels[i + 6], labels[j + 6], axs[i, j], False)
			axs[i, j].tick_params(direction="in", labelbottom=False, labelleft=False)
		if j == 0:
			axs[i, j].set_ylabel(labels_temp[i + 6], fontsize=7)
		if i == 12:
			axs[i,j].set_xlabel(labels_temp[j + 6], fontsize=7)

fig.legend(["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"], loc="upper right", bbox_to_anchor=(-0.5, -0.1, 1.0, 1.0))

plt.show()
