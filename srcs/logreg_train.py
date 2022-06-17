import sys
import numpy as np
import math
from utils.read_csv import read_csv

def hThetafunc(thetas, x):
	temp = 0
	for i in range(len(thetas)):
		if ~np.isnan(x[6 + i]):
			temp += x[6 + i] * thetas[i]
	ret = 1 / (1 + math.exp(temp * -1))
	return ret

def sumPartialDer(thetas, matrix, y, labels, j):
	ret = 0
	for i in range(len(matrix[labels[j + 6]])):
		ret += (hThetafunc(thetas, matrix[i]) - y[i]) * matrix[labels[j + 6]][i]
	return ret

if len(sys.argv) != 2:
	print("Usage: python3 logreg_train.py fileName")
	sys.exit(0)

matrix = read_csv(sys.argv[1], ',')
labels = matrix.dtype.names
step = 30
lr = 1 / 100

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

thetas = np.zeros(12)
tempThetas = np.zeros(12)
nRow = len(matrix[labels[0]])

y = np.fromiter((x == "Gryffindor" for x in matrix["Hogwarts House"]), int)

for i in range(step):
	for i in range(len(thetas)):
		tempThetas[i] = thetas[i] - lr * (1/nRow) * sumPartialDer(thetas, matrix, y, labels, i)
	thetas = tempThetas
print(thetas)