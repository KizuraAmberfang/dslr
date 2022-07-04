# What are the two features that are similar?

import sys
import numpy as np
from utils.plot_scatter import plot_scatter 
from utils.read_csv import read_csv
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

fig, ax = plt.subplots()
plt.title("What are the two features that are similar?")
plot_scatter(gryf, raven, huffle, slyth, labels[7], labels[9], ax)

plt.legend(["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"], loc="upper right")

plt.show()
