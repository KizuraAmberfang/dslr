# What feature are you going to use for your logistic regression?

import sys
from describeUtils import * 
from utils.read_csv import read_csv
from utils.plot_hist import plot_hist
from utils.plot_scatter import plot_scatter
import matplotlib.pyplot as plt

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

fig, axs = plt.subplots(ncols=13, nrows=13, sharey=True)
plt.figtext(0.1, 0.9, "Which hogwarts course has a homogeneous score distribution between all four houses?", wrap=True)
fig.supylabel("student")
fig.supxlabel("score")
for i in range(13):
	for j in range(13):
		if i == j:
			plot_hist(gryf, raven, huffle, slyth, labels[i + 6], axs[i, j])
		else:
			plot_scatter(gryf, raven, huffle, slyth, labels[i + 6], labels[j + 6], axs[i, j])
fig.legend(["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"], loc="upper left", bbox_to_anchor=(0.1, -0.12, 1.0, 1.0), ncol=2)

plt.show()
