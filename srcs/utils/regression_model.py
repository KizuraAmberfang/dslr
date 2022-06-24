import numpy as np

class GradientDescent(object):
	"""

"""
	def __init__(self, lr=0.1, iter=50, weight=None):
		self.lr = lr
		self.iter = iter
		self.w = weight
		self.error = []
		self.cost = []
		self.cl = None
	
	def calculate_weight(self, X, y):
		# calcolo il numero di classi
		self.cl = np.unique(y).tolist()
		ncl = len(self.cl)
		# per motivi pratici inseriamo come prima colonna degli 0
		tempX = np.insert(X, 0, 1, axis=1)
		# la matrice ha row righe ed col colonne
		row = tempX.shape[0]
		col = tempX.shape[1]
		self.w = np.zeros((ncl, col))
		yV = np.zeros((len(y), ncl))
		for i in range(0, len(y)):
			yV[i, self.cl.index(y[i])] = 1
		# iterazioni per calcolare i pesi!
		for _ in range(0, self.iter):
			htheta = self.sigmoid(tempX).T
			self.w = self.w - (self.lr * (1 / row) * (htheta - yV).T.dot(tempX)) 
		return self

	def predict(self, X):
		tempX = np.insert(X, 0, 1, axis=1)
		calc = self.sigmoid(tempX).T
		ret = []
		for x in calc.argmax(1):
			ret.append(self.cl[x])
		return ret

	def sigmoid(self, X):
		temp = self.w.dot(X.T)
		g = 1.0 / (1.0 + np.exp(-temp))
		return g