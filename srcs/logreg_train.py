import sys
import numpy as np
import math
import pandas as pd
from utils.regression_model import GradientDescent
from sklearn.metrics import accuracy_score

def isnan(x):
	if x != x:
		return True
	else:
		return False
		
def hThetafunc(thetas, x):
	temp = 0
	for i in range(len(thetas)):
		if ~np.isnan(x[i]):
			temp += x[i] * thetas[i]
	try:
		ret = 1 / (1 + math.exp(temp * -1))
	except:
		if temp > 0:
			ret = 1
		else:
			ret = 0
	return ret

def sumPartialDer(thetas, matrix, y, j):
	ret = 0
	for i in range(matrix.shape[0]):
		if ~np.isnan(matrix[i][j]):
			ret += (hThetafunc(thetas, matrix[i]) - y[i]) * matrix[i][j]
	return ret

if len(sys.argv) != 2:
	print("Usage: python3 logreg_train.py fileName")
	sys.exit(0)

df = pd.read_csv(sys.argv[1], sep=',')
df = df.dropna()
matrix = np.array(df.values[:, [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]], dtype=float)
y = df.values[:, 1]
n = matrix.shape[1]

gd = GradientDescent(lr=0.01, iter=30)
gd.calculate_weight(matrix, y)
print(gd.w)
# la nostra variabile dicotomica è la casata di Hogwarts
# la variabili indipendenti o regressori le altre variabili numeriche
#  Y = ln(p / 1 - p) = b0 + b1 * x1 + .. + bn * xn
# p = 1 / (1 + e^-(b0 + b1 * x1 + ... + bn * xn)) + eps
# gli esponenziali dei coefficienti bi si intrepretano come l'odds ratio di accadimento dell'evento
# quando bi è > 1 è un fattore di rischio
# quando è < 1 è un fattore di protezione
# quando è nullo non influenza Y

# devono essere assenti outliers -> rimuovere valori sballati
# non deve essere presente multicollinearità --> usiamo solo una tra le due variabili simili
# necessarie 10 * (n + 1) casi per stimare un modello con n variabili indipendenti
# la distribuzione teorica di riferimento è la binomiale (che io adoro)

# P(Y = 1) = e^(a + b * x) / (1 + e^(a + bx))

y_pred = gd.predict(matrix)
print("Accuracy score: ", accuracy_score(y, y_pred))
# thetas[0] = 1/1600 sum (g(thetas * riga i-esima) - risultato iesimo)) * matrix[i][0]
# thetas * riga i-esima = 0 -> g = 1/2
# risultato iesimo 1/2 o -1/2 che moltiplicano gli x[i][0]
