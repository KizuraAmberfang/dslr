import math
import numpy as np

class FtSeries:
	def __init__(self, data=None, index=None, dtype=None):
		self.data = data
		self.index = index
		self.dtype = dtype

	def __str__(self):
		return(self.dtype)


class MyDataset:
	def __init__(self, data=None):
		self.data = data
		self.labels = data.dtype.names
		self.types = data.dtype
		self.__countLabelChar()
		self.__count()
		self.__unique()
		self.__mean()
		self.__variance()
		self.__std()
		self.__minmax()
		self.perc25 = self.__cent(25)
		self.perc50 = self.__cent(50)
		self.perc75 = self.__cent(75)

	def __str__(self):
		print(self.data)
		return ('MyDataset')

	def __countLabelChar(self):
		self.labelChar = 0
		for x in self.labels:
			if (len(x) > self.labelChar):
				self.labelChar = len(x)

	def __count(self):
		count = len(self.data[0])
		self.cnt = []
		for i in range(count):
			n = 0
			if (self.data.dtype[i] == 'float32'):
				for x in self.data:
					try:
						float(x[i])
						if ~np.isnan(float(x[i])):
							n += 1
					except:
						pass
			elif (self.data.dtype[i] == 'object'):
				for x in self.data:
					try:
						np.datetime64(x[i])
						if ~np.isnat(np.datetime64(x[i])):
							n += 1
					except:
						pass
			else:
				for x in self.data:
					if x[i] != "":
						n += 1
			if n > 0:
				self.cnt.append(n)
			else:
				self.cnt.append(np.nan)

	def __mean(self):
		count = len(self.labels)
		self.media = []
		for i in range(count):
			n = 0
			sum = 0
			if (self.data.dtype[i] == 'float32'):
				for x in self.data:
					try:
						value = float(x[i])
						if (~np.isnan(value)):
							n += 1
							sum += value
					except:
						pass
			if n != 0:
				self.media.append(sum / n)
			else:
				self.media.append(np.nan)
		
	def __variance(self):
		count = len(self.labels)
		self.var = []
		for i in range(count):
			sum = 0
			n = 0
			if (self.data.dtype[i] == 'float32' and ~np.isnan(self.media[i])):
				for x in self.data:
					try:
						value = float(x[i])
						if ~np.isnan(value):
							sum += (value - self.media[i]) ** 2
							n += 1
					except:
						pass
			if n > 1:
				self.var.append(sum / (n - 1))
			else:
				self.var.append(np.nan)
	
	def __std(self):
		self.stddev = []
		for x in self.var:
			if ~np.isnan(x):
				self.stddev.append(math.sqrt(x))
			else:
				self.stddev.append(np.nan)
		
	def __unique(self):
		count = len(self.labels)
		self.uni = []
		self.tp = []
		self.frq = []
		for i in range(count):
			if (self.data.dtype[i] != 'float32'):
				temp = self.data[self.labels[i]]
				temp2 = np.unique(temp, return_counts=True)
				self.uni.append(len(temp2[0]))
				self.tp.append(temp2[0][temp2[1].argmax()])
				self.frq.append(temp2[1][temp2[1].argmax()])
			else:
				self.uni.append(np.NaN)
				self.tp.append("nan")
				self.frq.append(np.nan)
	
	def __minmax(self):
		count = len(self.labels)
		self.minA = []
		self.maxA = []
		for i in range(count):
			min = float("inf")
			max = float("-inf")
			n = 0
			m = 0
			if self.data.dtype[i] == 'float32':
				for x in self.data:
					try: 
						f = float(x[i])
						if ~np.isnan(f):
							if f < min:
								n += 1
								min = f
							if f > max:
								m += 1
								max = f
					except:
						pass
			if n != 0:
				self.minA.append(min)
			else:
				self.minA.append(np.nan)
			if m != 0:
				self.maxA.append(max)
			else:
				self.maxA.append(np.nan)

	def __cent(self, nquant):
		ret = []
		for i in range(len(self.labels)):
			try:
				col = np.array(self.data[self.labels[i]], dtype=float)
			except:
				col = np.empty(len(self.data[self.labels[i]]))
				col[:] = np.nan
			col = col[~np.isnan(col)]
			if col.any():
				col.sort()
				index = (len(col) - 1) * (nquant / 100)
				lower = np.floor(index)
				upper = np.ceil(index)
				if lower == upper:
					ret.append(col[int(index)])
				else:
					first = col[int(lower)] * (upper - index)
					second = col[int(upper)] * (index - lower)
					ret.append(first + second)
			else:
				ret.append(np.nan)
		return ret

	def count(self):
		for i in range(len(self.cnt)):
			print(f'{self.labels[i] : <{self.labelChar}}    {self.cnt[i]}')	

	def mean(self):
		lenprint = self.__calcLenArrFloat(self.media, decimal=6)
		for i in range(len(self.media)):
			if ~np.isnan(self.media[i]):
				temp = f'{self.media[i]:.6f}'
				print(f'{self.labels[i] : <{self.labelChar}}  {temp:>{lenprint}}')

	def variance(self):
		lenprint = self.__calcLenArrFloat(self.var, decimal=6)
		for i in range(len(self.var)):
			if ~np.isnan(self.var[i]):
				temp = f'{self.var[i]:.6f}'
				print(f'{self.labels[i] : <{self.labelChar}}  {temp:>{lenprint}}')
	
	def std(self):
		lenprint = self.__calcLenArrFloat(self.stddev, decimal=6)
		for i in range(len(self.stddev)):
			if ~np.isnan(self.stddev[i]):
				temp = f'{self.stddev[i]:.6f}'
				print(f'{self.labels[i] : <{self.labelChar}}  {temp:>{lenprint}}')

	def unique(self):
		lenprint = self.__calcLenArrInt(self.media)
		for i in range(len(self.uni)):
			if ~np.isnan(self.uni[i]):
				print(f'{self.labels[i] : <{self.labelChar}}  {self.uni[i]:>{lenprint}}')	

	def top(self):
		lenprint = self.__calcLenArrStr(self.tp)
		for i in range(len(self.tp)):
			if self.tp[i] != "nan":
				print(f'{self.labels[i] : <{self.labelChar}}  {self.tp[i]:>{lenprint}}')	

	def freq(self):
		lenprint = self.__calcLenArrInt(self.frq)
		for i in range(len(self.frq)):
			if ~np.isnan(self.frq[i]):
				print(f'{self.labels[i] : <{self.labelChar}}  {self.frq[i]:>{lenprint}}')	

	def max(self):
		lenprint = self.__calcLenArrFloat(self.maxA, 6)
		for i in range(len(self.maxA)):
			if ~np.isnan(self.maxA[i]):
				temp = f'{self.maxA[i]:.6f}'
				print(f'{self.labels[i] : <{self.labelChar}}  {temp:>{lenprint}}')

	def min(self):
		lenprint = self.__calcLenArrFloat(self.minA, 6)
		for i in range(len(self.minA)):
			if ~np.isnan(self.minA[i]):
				temp = f'{self.minA[i]:.6f}'
				print(f'{self.labels[i] : <{self.labelChar}}  {temp:>{lenprint}}')


	def __calcLenArrFloat(self, array, decimal=2):
		ret = 0
		for x in array:
			if ~np.isnan(x):
				temp = len(str(np.trunc(x))) + decimal + 1
				if temp > ret:
					ret = temp
		return ret

	def __calcLenArrInt(self, array):
		ret = 0
		for x in array:
			if ~np.isnan(x):
				temp = len(str(x))
				if temp > ret:
					ret = temp
		return ret

	def __calcLenArrStr(self, array):
		ret = 0
		for x in array:
			temp = len(str(x))
			if temp > ret:
				ret = temp
		return ret

	# def __calcLenPrint(self):
	# 	ret = []
	# 	for i in range(len(self.labels)):
	# 		temp = len(self.labels[i])
	# 		f_len = self.__len(self.cnt[i])
	# 		if f_len > temp:
	# 			temp = f_len
	# 		ret.append(temp + 2)
	# 	return ret

	# def __len(self, value: int) -> int:
	# 	str_len = 0
	# 	if ~np.isnan(value):
	# 		str_len = len(str(value)) + 2
	# 	return(str_len)
	
	# def __len(self, value: np.float32) -> int:
	# 	str_len = 0
	# 	if ~np.isnan(value):
	# 		str_len = len(str(np.trunc(value))) + 5
	# 	return(str_len)
	
	def describe(self):
		lenUni = self.__calcLenArrInt(self.uni)
		lenTop = self.__calcLenArrStr(self.tp)
		lenFreq = self.__calcLenArrInt(self.frq)
		lenMedia = self.__calcLenArrFloat(self.media, 6)
		lenStd = self.__calcLenArrFloat(self.stddev, 6)
		lenMin = self.__calcLenArrFloat(self.minA, 6)
		lenMax = self.__calcLenArrFloat(self.maxA, 6)
		lenPerc25 = self.__calcLenArrFloat(self.perc25, 6)
		lenPerc50 = self.__calcLenArrFloat(self.perc50, 6)
		lenPerc75 = self.__calcLenArrFloat(self.perc75, 6)
		if lenUni < 6:
			lenUni = 6 
		if lenTop < 3:
			lenTop = 3
		if lenFreq < 4:
			lenFreq = 4
		print(f"{'=======':=<{self.labelChar}}==|=======|={'======':=<{lenUni}}=|={'===':=<{lenTop}}=|={'====':=<{lenFreq}}=|={'====':=<{lenMedia}}=|={'===':=<{lenStd}}=|={'===':=<{lenMin}}=|={'===':=<{lenPerc25}}=|={'===':=<{lenPerc50}}=|={'===':=<{lenPerc75}}=|={'===':=<{lenMax}}==")
		print(f"{'Feature':<{self.labelChar}}  | count | {'unique':^{lenUni}} | {'top':^{lenTop}} | {'freq':^{lenFreq}} | {'mean':^{lenMedia}} | {'std':^{lenStd}} | {'min':^{lenMin}} | {'%25':^{lenPerc25}} | {'%50':^{lenPerc50}} | {'%75':^{lenPerc75}} | {'max':^{lenMax}} |")
		print(f"{'=======':=<{self.labelChar}}==|=======|={'======':=<{lenUni}}=|={'===':=<{lenTop}}=|={'====':=<{lenFreq}}=|={'====':=<{lenMedia}}=|={'===':=<{lenStd}}=|={'===':=<{lenMin}}=|={'===':=<{lenPerc25}}=|={'===':=<{lenPerc50}}=|={'===':=<{lenPerc75}}=|={'===':=<{lenMax}}==")
		for i in range(len(self.labels)):
			if self.types[i] == 'float32':
				media = f'{self.media[i]:.6f}'
				std = f'{self.stddev[i]:.6f}'
				min = f'{self.minA[i]:.6f}'
				max = f'{self.maxA[i]:.6f}'
				p25 = f'{self.perc25[i]:.6f}'
				p50 = f'{self.perc50[i]:.6f}'
				p75 = f'{self.perc75[i]:.6f}'
				uniq = "NaN"
				top = "NaN"
				freq = "NaN"
			else:
				media = "NaN"
				std = "NaN"
				min = "NaN"
				max = "NaN"
				p25 = "NaN"
				p50 = "NaN"
				p75 = "NaN"
				uniq = self.uni[i]
				top = self.tp[i]
				freq = self.frq[i]
			print(f'{self.labels[i] : <{self.labelChar}}  |  {self.cnt[i]} | {uniq:>{lenUni}} | {top:>{lenTop}} | {freq:>{lenFreq}} | {media:>{lenMedia}} | {std:>{lenStd}} | {min:>{lenMin}} | {p25:>{lenPerc25}} | {p50:>{lenPerc50}} | {p75:>{lenPerc75}} | {max:>{lenMax}} |')
		print(f"{'=======':=<{self.labelChar}}==|=======|={'======':=<{lenUni}}=|={'===':=<{lenTop}}=|={'====':=<{lenFreq}}=|={'====':=<{lenMedia}}=|={'===':=<{lenStd}}=|={'===':=<{lenMin}}=|={'===':=<{lenPerc25}}=|={'===':=<{lenPerc50}}=|={'===':=<{lenPerc75}}=|={'===':=<{lenMax}}==")


