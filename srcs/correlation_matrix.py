import sys
from utils.ft_pandas import MyDataset
from utils.read_csv import read_csv
# total arguments
if len(sys.argv) != 2:
	print("Usage: python3 describe.py fileName")
	sys.exit(0)

csv = read_csv(sys.argv[1])
md = MyDataset(csv)
