# which hogwarts course has a homogeneous score distribution between all four houses?

import sys
from describeUtils import * 
from utils.read_csv import read_csv
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
	print("Usage: python3 histogram.py fileName")
	sys.exit(0)

matrix = read_csv(sys.argv[1], ',')

print(matrix)
gryf = []
raven = []
huffle = []
slyth = []
# for x in matrix:
# 	if x[1] == "Gryffindor":
# 		gryf.append(x)
# 	if x[1] == "Ravenclaw":
# 		raven.append(x)
# 	if x[1] == "Hufflepuff":
# 		huffle.append(x)
# 	if x[1] == "Slytherin":
# 		slyth.append(x)


# gryf_t = transpose(gryf)
# raven_t = transpose(raven)
# huffle_t = transpose(huffle)
# slyth_t = transpose(slyth)

# h1 = gryf_t
# plt.hist(h1, color="red", alpha=0.5)
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
# plt.show()