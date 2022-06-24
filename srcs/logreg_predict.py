import sys
import numpy as np
import pandas as pd
from utils.regression_model import GradientDescent, SetNormalizer

if len(sys.argv) != 3:
	print("Usage: python3 logreg_predict.py fileName fileWeight")
	sys.exit(0)

df1 = pd.read_csv(sys.argv[1], sep=',')
df2 = pd.read_csv(sys.argv[2], sep=',')
cl = list(df2)
gd = GradientDescent(weight=df2.values.T, classes=cl)

df1 = df1.fillna(method='ffill')
X = np.array(df1.values[:, [7, 8, 10, 11, 12, 17, 18]], dtype=float)

sc = SetNormalizer()
sc.calc(X)
X = sc.conv(X)

y_pred = gd.predict(X)

with open('./data/houses.csv', 'w+') as file:
	file.write('Index,Hogwarts House\n')
	i = 0
	for x in y_pred:
		file.write(f'{i},{x}\n')
		i += 1