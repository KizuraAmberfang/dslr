import numpy as np

def read_csv(pathfile, sep=','):
	with open(pathfile, 'r') as file:
	# RIGA 1 labels
		row = file.readline()
		label = []
		temp = row.split(sep)
		for x in temp:
			label.append((x.strip(), 'f4'))
	# RIGA 2 e tutte le successive, creiamo una matrice di dati.
		matrix = []
		for row in file:
			temp = row.split(sep)
			temp2 = []
			for x in temp:
				try:
					value = float(x)
				except:
					value = np.nan
				temp2.append(value)
			matrix.append(tuple(temp2))
	ret = np.array(matrix, dtype=label)
	return ret
