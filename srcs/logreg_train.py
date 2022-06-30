import sys
import numpy as np
import pandas as pd
from utils.regression_model import GradientDescent, SetNormalizer

if len(sys.argv) < 2:
	print("Usage: python3 logreg_train.py fileName")
	sys.exit(0)

visual = False
if len(sys.argv) == 3:
	if (sys.argv[2] == "-v"):
		visual = True

df = pd.read_csv(sys.argv[1], sep=',')
df = df.dropna(subset=['Astronomy'])
df = df.dropna(subset=['Herbology'])
df = df.dropna(subset=['Divination'])
df = df.dropna(subset=['Muggle Studies'])
df = df.dropna(subset=['Ancient Runes'])
df = df.dropna(subset=['Charms'])
df = df.dropna(subset=['Flying'])
matrix = np.array(df.values[:, [7, 8, 10, 11, 12, 17, 18]], dtype=float)
y = df.values[:, 1]

gd = GradientDescent(lr=0.01, iter=50)

# standardizzo i valori delle colonne
sn = SetNormalizer()
sn.calc(matrix)

X = sn.conv(matrix)

gd.calculate_weight(X, y)

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
# necessarie 10 * (n + 1) casi per stimare un modello con n variabili indipendenti -> quindi in realtà ci bastano 130 elementi
# la distribuzione teorica di riferimento è la binomiale (che io adoro)

# P(Y = 1) = e^(a + b * x) / (1 + e^(a + bx))

with open('./data/weight.csv', 'w+') as file:
	for i in range(0, len(gd.cl) - 1):
		file.write(f'{gd.cl[i]},')
	file.write(f'{gd.cl[len(gd.cl) - 1]}\n')

	for j in range(gd.w.shape[1]):
		for i in range(gd.w.shape[0] - 1):
			file.write(f'{gd.w[i][j]},')
		file.write(f'{gd.w[gd.w.shape[0] - 1][j]}\n')

if visual:
	gd.plot()