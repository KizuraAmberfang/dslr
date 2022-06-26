import os
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

	def __unique(self):
		count = len(self.labels)
		self.uni = []
		for i in range(count):
			n = 0
			if (self.data.dtype[i] != 'float32'):
				temp = self.data[self.labels[i]]
				self.uni.append(len(np.unique(temp)))
			else:
				self.uni.append(np.NaN)

	def count(self):
		for i in range(len(self.cnt)):
			print(f'{self.labels[i] : <{self.labelChar}}    {self.cnt[i]}')	

	def mean(self):
		lenprint = self.__calcLenArrFloat(self.media, decimal=6)
		for i in range(len(self.media)):
			if ~np.isnan(self.media[i]):
				temp = f'{self.media[i]:.6f}'
				print(f'{self.labels[i] : <{self.labelChar}}  {temp:>{lenprint}}')	

	def unique(self):
		lenprint = self.__calcLenArrInt(self.media)
		for i in range(len(self.uni)):
			if ~np.isnan(self.uni[i]):
				print(f'{self.labels[i] : <{self.labelChar}}  {self.uni[i]:>{lenprint}}')	

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

	def __calcLenPrint(self):
		ret = []
		for i in range(len(self.labels)):
			temp = len(self.labels[i])
			f_len = self.__len(self.cnt[i])
			if f_len > temp:
				temp = f_len
			ret.append(temp + 2)
		return ret

	def __len(self, value: int) -> int:
		str_len = 0
		if ~np.isnan(value):
			str_len = len(str(value)) + 2
		return(str_len)
	
	def __len(self, value: np.float32) -> int:
		str_len = 0
		if ~np.isnan(value):
			str_len = len(str(np.trunc(value))) + 5
		return(str_len)
	
	def describe(self):
		lenMedia = self.__calcLenArrFloat(self.media, 6)
		lenUni = self.__calcLenArrInt(self.uni)
		if lenUni < 6:
			lenUni = 6 
		print(f"{'Feature':<{self.labelChar}}   count {'mean':>{lenMedia}}  {'unique':>{lenUni}}")
		print("*=================================================================*")
		for i in range(len(self.labels)):
			if self.types[i] == 'float32':
				media = f'{self.media[i]:.6f}'
				uniq = "NaN"
			else:
				media = "NaN"
				uniq = self.uni[i]
			print(f'{self.labels[i] : <{self.labelChar}}    {self.cnt[i]} {media:>{lenMedia}}  {uniq:>{lenUni}}')


