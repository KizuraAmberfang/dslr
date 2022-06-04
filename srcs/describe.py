import sys
from describeUtils import *
import pandas as pd
import csv
from utils.read_csv import read_csv

# total arguments

if len(sys.argv) != 2:
	print("Usage: python3 describe.py fileName")
	sys.exit(0)

matrix = read_csv(sys.argv[1], ',')
print(matrix)

csvRead = pd.read_csv(sys.argv[1])
print(type(csvRead))
df = pd.DataFrame(csvRead)
# gestione dell'headbar
# tr_matrix = transpose(matrix)
count = count(matrix)
mean = mean(matrix)
variance = variance(matrix, mean)
std = std(variance)
min = min(matrix)
max = max(matrix)
# cent_25 = cent(tr_matrix, count, 0.25)
# cent_50 = cent(tr_matrix, count, 0.5)
# cent_75 = cent(tr_matrix, count, 0.75)

# describe(head, count, mean, std, min, cent_25, cent_50, cent_75, max)
# print_head("", head, count)
# print_desc("count", count)
# print_desc("mean", mean)
# print_desc("var", variance)
# print_desc("std", std)
# print_desc("min", min)
# print_desc("25%", cent_25)
# print_desc("50%", cent_50)
# print_desc("75%", cent_75)
# print_desc("max", max)
print(df.describe())
# with open('GFG', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
    # write.writerow(tr_matrix)
