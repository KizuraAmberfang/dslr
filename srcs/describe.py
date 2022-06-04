import sys
from describeUtils import *
from utils.read_csv import read_csv
import numpy as np

# total arguments

if len(sys.argv) != 2:
	print("Usage: python3 describe.py fileName")
	sys.exit(0)

matrix = read_csv(sys.argv[1], ',')

labels = matrix.dtype.names
count = count(matrix)
mean = mean(matrix)
variance = variance(matrix, mean)
std = std(variance)
min = min(matrix)
max = max(matrix)
cent_25 = cent(matrix, 25)
cent_50 = cent(matrix, 50)
cent_75 = cent(matrix, 75)

len_print = []
for i in range(len(labels)):
	temp = len(labels[i])
	f_len = ft_len(count[i])
	if f_len > temp:
		temp = f_len
	f_len = ft_len(mean[i])
	if f_len > temp:
		temp = f_len
	f_len = ft_len(std[i])
	if f_len > temp:
		temp = f_len
	f_len = ft_len(min[i])
	if f_len > temp:
		temp = f_len
	f_len = ft_len(max[i])
	if f_len > temp:
		temp = f_len
		f_len = ft_len(cent_25[i])
	if f_len > temp:
		temp = f_len
	f_len = ft_len(cent_50[i])
	if f_len > temp:
		temp = f_len
	f_len = ft_len(cent_75[i])
	if f_len > temp:
		temp = f_len
	len_print.append(temp + 2)

head_print = "     "
for i in range(len(labels)):
	if ~np.isnan(count[i]):
		temp = "{:>" + str(len_print[i]) + "}"
		head_print += temp.format(labels[i])

print(head_print)
print_desc("count", count, len_print)
print_desc("mean ", mean, len_print)
print_desc("std  ", std, len_print)
print_desc("min  ", min, len_print)
print_desc("25%  ", cent_25, len_print)
print_desc("50%  ", cent_50, len_print)
print_desc("75%  ", cent_75, len_print)
print_desc("max  ", max, len_print)
