import sys
import pandas as pd
from sklearn.metrics import accuracy_score

if len(sys.argv) != 3:
	print("Usage: python3 compare.py fileName1 fileName2")
	sys.exit(0)

df1 = pd.read_csv(sys.argv[1], sep=',')
y1 = df1.values[:, 1]

df2 = pd.read_csv(sys.argv[2], sep=',')
y2 = df2.values[:, 1]

if len(y1) == len(y2):
	print("Miss: ", sum(y1 != y2), "/", len(y1))
	print(f"Accuracy score: {(accuracy_score(y1, y2) * 100):.2f}%")
else:
	print("Error: data is invalid")
