import sys
import numpy as np
import math
from utils.read_csv import read_csv_to_list
# from sklearn.metrics import accuracy_score

def hThetafunc(thetas, x):
	temp = 0
	for i in range(len(thetas)):
		if ~np.isnan(x[1 + i]):
			temp += x[1 + i] * thetas[i]
	try:
		ret = 1 / (1 + math.exp(temp * -1))
	except:
		if temp > 0:
			ret = 1
		else:
			ret = 0
	return ret

# def sumPartialDer(thetas, matrix, y, labels, j):
# 	ret = 0
# 	for i in range(len(matrix[labels[j + 1]])):
# 		if ~np.isnan(matrix[labels[j + 1]][i]):
# 			ret += (hThetafunc(thetas, matrix[i]) - y[i]) * matrix[labels[j + 1]][i]
# 	return ret

def sumPartialDer(thetas, matrix, y, j):
	ret = 0
	for i in range(matrix.shape[0]):
		if ~np.isnan(matrix[i][j + i]):
			ret += (hThetafunc(thetas, matrix[i]) - y[i]) * matrix[i][j + 1]
	return ret

if len(sys.argv) != 2:
	print("Usage: python3 logreg_train.py fileName")
	sys.exit(0)

matrix_temp = read_csv_to_list(sys.argv[1], ',')
# labels = matrix_temp.dtype.names
# print(labels)
# matrix = matrix_temp[[labels[1], labels[6], labels[7], labels[8], labels[10], labels[11], labels[12], labels[13], labels[14], labels[15], labels[16], labels[17], labels[18]]]
matrix = matrix_temp[:, [1, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

# labels = matrix.dtype.names
# n = len(labels) - 1
n = matrix.shape[1] - 1
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

gthetas = np.zeros(n)
rthetas = np.zeros(n)
hthetas = np.zeros(n)
sthetas = np.zeros(n)

tempThetas = np.zeros(n)
nRow = matrix.shape[0]

gryf = np.fromiter((x == "Gryffindor" for x in matrix[:, 1]), int)
raven = np.fromiter((x == "Ravenclaw" for x in matrix[:, 1]), int)
huff = np.fromiter((x == "Hufflepuff" for x in matrix[:, 1]), int)
slyth = np.fromiter((x == "Slytherin" for x in matrix[:, 1]), int)


for i in range(step):
	for i in range(len(gthetas)):
		tempThetas[i] = gthetas[i] - lr * (1/nRow) * sumPartialDer(gthetas, matrix, gryf, i)
	gthetas = tempThetas
print(gthetas)

for i in range(step):
	for i in range(len(rthetas)):
		tempThetas[i] = rthetas[i] - lr * (1/nRow) * sumPartialDer(rthetas, matrix, raven, i)
	rthetas = tempThetas
print(rthetas)

for i in range(step):
	for i in range(len(hthetas)):
		tempThetas[i] = hthetas[i] - lr * (1/nRow) * sumPartialDer(hthetas, matrix, huff, i)
	hthetas = tempThetas
print(hthetas)

for i in range(step):
	for i in range(len(sthetas)):
		tempThetas[i] = sthetas[i] - lr * (1/nRow) * sumPartialDer(sthetas, matrix, slyth, i)
	sthetas = tempThetas
print(sthetas)

# y_pred = ...
# y_true = ...
# print("Accuracy score: ", accuracy_score(y_true, y_pred))
# thetas[0] = 1/1600 sum (g(thetas * riga i-esima) - risultato iesimo)) * matrix[i][0]
# thetas * riga i-esima = 0 -> g = 1/2
# risultato iesimo 1/2 o -1/2 che moltiplicano gli x[i][0]
