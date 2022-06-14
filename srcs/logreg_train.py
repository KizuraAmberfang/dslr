import sys
from utils.read_csv import read_csv

if len(sys.argv) != 2:
	print("Usage: python3 logreg_train.py fileName")
	sys.exit(0)

matrix = read_csv(sys.argv[1], ',')
labels = matrix.dtype.names
# la nostra variabile dicotomica è la casata di Hogwarts


