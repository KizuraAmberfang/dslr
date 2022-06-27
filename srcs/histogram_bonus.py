import sys
from describeUtils import * 
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

dateArray = matrix[labels[4]]
mesi = dateArray.astype('datetime64[M]').astype(int) % 12
fig, axs = plt.subplots(ncols=1, nrows=2, sharey=True, constrained_layout=True)
	
hg = gryf[labels[4]]
hs = slyth[labels[4]]
hr = raven[labels[4]]
hh = huffle[labels[4]]

# mesi

hgm = hg.astype('datetime64[M]').astype(int) % 12
axs[0].hist(hgm, color='red', alpha=0.4)

hsm = hs.astype('datetime64[M]').astype(int) % 12
axs[0].hist(hsm, color='green', alpha=0.4)

hrm = hr.astype('datetime64[M]').astype(int) % 12
axs[0].hist(hrm, color='blue', alpha=0.4)

hhm = hh.astype('datetime64[M]').astype(int) % 12
axs[0].hist(hhm, color='yellow', alpha=0.4)

hg = gryf[labels[5]]
axs[1].hist(hg, color='red', alpha=0.4)

hs = slyth[labels[5]]
axs[1].hist(hs, color='green', alpha=0.4)

hr = raven[labels[5]]
axs[1].hist(hr, color='blue', alpha=0.4)

hh = huffle[labels[5]]
axs[1].hist(hh, color='yellow', alpha=0.4)

fig.legend(["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"])

plt.show()
