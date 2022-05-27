import sys
from describeUtils import *
import pandas as pd
import csv

# total arguments

if len(sys.argv) != 2:
	print("Usage: python3 describe.py fileName")
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
csvRead = pd.read_csv(sys.argv[1])
df = pd.DataFrame(csvRead)

# gestione dell'headbar
tr_matrix = transpose(matrix)
count = count(matrix)
mean = mean(matrix)
variance = variance(matrix, mean)
std = std(variance)
min = min(matrix)
max = max(matrix)
cent_25 = cent(tr_matrix, count, 0.25)
cent_50 = cent(tr_matrix, count, 0.5)
cent_75 = cent(tr_matrix, count, 0.75)

print_desc("count", count)
print_desc("mean", mean)
print_desc("var", variance)
print_desc("std", std)
print_desc("min", min)
print_desc("25%", cent_25)
print_desc("50%", cent_50)
print_desc("75%", cent_75)
print_desc("max", max)
print(df.describe())
with open('GFG', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(tr_matrix)
