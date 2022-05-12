import sys

# total arguments

if len(sys.argv) != 2:
	print("Usage: python3 describe.py fileName")
	sys.exit(0)

file = open(sys.argv[1], "r")

# ci aspettiamo che sia un csv, diviso per ',', e che si abbia come prima riga l'intestazione
# RIGA 1 intestazione
row = (file.readline())
row = row.split(',')
head = []
for x in row:
	head.append(x.strip())

# RIGA 2 e tutte le successive, creiamo una matrice di dati.
for x in file:
	print(x)

file.close()

print(head)

