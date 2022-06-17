import sys
from utils.read_csv import read_csv

if len(sys.argv) != 2:
	print("Usage: python3 logreg_train.py fileName")
	sys.exit(0)

matrix = read_csv(sys.argv[1], ',')
labels = matrix.dtype.names
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

# primo test con solo Aritmanzia (colonna 6)
