# which hogwarts course has a homogeneous score distribution between all four houses?

import sys
from describeUtils import * 
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) != 2:
	print("Usage: python3 histogram.py fileName")
	sys.exit(0)

file = open(sys.argv[1], "r")

# ci aspettiamo che sia un csv, diviso per ',', e che si abbia come prima riga l'intestazione
# RIGA 1 intestazione
row = file.readline()
row = row.split(',')
head = []
for x in row:
	head.append(x.strip())

# RIGA 2 e tutte le successive, creiamo una matrice di dati.
matrix = []
for row in file:
	temp = row.split(',')
	temp2 = []
	for x in temp:
		temp2.append(x.strip())
	matrix.append(temp2)

# chiusura file

file.close()

gryf = []
raven = []
huffle = []
slyth = []
for x in matrix:
	if x[1] == "Gryffindor":
		gryf.append(x)
	if x[1] == "Ravenclaw":
		raven.append(x)
	if x[1] == "Hufflepuff":
		huffle.append(x)
	if x[1] == "Slytherin":
		slyth.append(x)


gryf_t = transpose(gryf)
raven_t = transpose(raven)
huffle_t = transpose(huffle)
slyth_t = transpose(slyth)

h1 = gryf_t
plt.hist(h1, color="red", alpha=0.5)
# axs[1].hist(gryf_t[7])
# axs[1].hist(raven_t[7])
# axs[1].hist(huffle_t[7])
# axs[1].hist(slyth_t[7])

# axs[2].hist(gryf_t[8])
# axs[2].hist(raven_t[8])
# axs[2].hist(huffle_t[8])
# axs[2].hist(slyth_t[8])

# axs[3].hist(gryf_t[9])
# axs[3].hist(raven_t[9])
# axs[3].hist(huffle_t[9])
# axs[3].hist(slyth_t[9])
plt.show()